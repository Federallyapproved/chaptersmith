"""EPUB ingestion pipeline."""

from __future__ import annotations

import logging
import re as _re
import warnings
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator, Tuple
from urllib.parse import urldefrag
from xml.etree import ElementTree as ET

from bs4 import BeautifulSoup, Tag, XMLParsedAsHTMLWarning
from ebooklib import epub

from .models import Book, Chapter
from .normalize import clean_text, to_markdown
from .tokenize_count import count_gpt5_tokens

LOGGER = logging.getLogger(__name__)


# BeautifulSoup may emit XMLParsedAsHTMLWarning when parsing EPUB fragments.
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

@dataclass(slots=True)
class TocEntry:
    title: str
    href: str
    file_href: str
    fragment: str | None
    order: int


def ingest_epub(
    path: Path,
    *,
    book_id: str | None = None,
    title: str | None = None,
    author: str | None = None,
) -> Book:
    """Read an EPUB file and return a structured ``Book`` instance."""

    epub_book = epub.read_epub(str(path))

    book_id = book_id or _first_or_default(epub_book.get_metadata("DC", "identifier")) or path.stem
    title = title or _first_or_default(epub_book.get_metadata("DC", "title")) or path.stem
    author = author or _first_or_default(epub_book.get_metadata("DC", "creator")) or "Unknown"

    spine_items = _ordered_spine_items(epub_book)
    href_to_spine_index = _href_to_spine_index(spine_items)

    toc_entries = _load_toc_entries(epub_book)
    chapters: list[Chapter] = []
    warnings: list[str] = []

    if not toc_entries:
        LOGGER.warning("EPUB %s has no navigation entries; treating each spine item as a chapter", path)
        toc_entries = [
            TocEntry(
                title=item.title or f"Section {idx + 1}",
                href=item.file_name,
                file_href=item.file_name,
                fragment=None,
                order=idx,
            )
            for idx, item in enumerate(spine_items)
        ]

    # Front matter before first ToC entry
    front_matter = _collect_front_matter(spine_items, toc_entries, href_to_spine_index)
    if front_matter:
        text = clean_text(to_markdown(front_matter, is_html=True))
        chapters.append(
            _make_chapter(
                chapter_id="front-matter",
                title="Front Matter",
                text=text,
                order=0,
                source={"href": spine_items[0].file_name, "anchor": None},
                est_tokens=count_gpt5_tokens(text),
                meta={"gray_zone": True},
            )
        )

    # Core chapters from ToC
    for index, entry in enumerate(toc_entries, start=1):
        item = _resolve_spine_item(epub_book, entry.file_href)
        if item is None:
            LOGGER.warning("Missing manifest item for href '%s' in %s", entry.file_href, path)
            warnings.append(f"Missing manifest item for {entry.file_href}")
            continue

        html_segment, missing_anchor = _gather_chapter_html(
            epub_book,
            spine_items,
            href_to_spine_index,
            toc_entries,
            index - 1,
        )
        if missing_anchor:
            start_label = entry.fragment or "<start>"
            LOGGER.warning(
                "Missing start anchor while slicing %s (from %s).",
                entry.file_href,
                start_label,
            )
            warnings.append(
                f"Missing anchor while slicing {entry.file_href} (from {start_label})"
            )

        markdown = to_markdown(html_segment, is_html=True)
        # Enrich the title using the start-of-chapter heading cluster in this file
        try:
            # Only analyze the start file (entry.file_href)
            start_item = _resolve_spine_item(epub_book, entry.file_href)
            enriched = entry.title
            if start_item is not None:
                soup_local = BeautifulSoup(start_item.get_content(), "lxml-xml")
                pieces = _extract_heading_cluster(soup_local, entry.fragment)
                enriched = _merge_nav_and_heading(entry.title, pieces) or entry.title
        except Exception:
            enriched = entry.title  # stay conservative on any error

        text = clean_text(markdown)
        chapter_meta: dict[str, object] = {}
        if missing_anchor:
            chapter_meta["gray_zone"] = True

        chapter = _make_chapter(
            chapter_id=f"chapter-{index:02d}",
            title=enriched or entry.title or f"Chapter {index}",
            text=text,
            order=index,
            source={"href": entry.file_href, "anchor": entry.fragment},
            est_tokens=count_gpt5_tokens(text),
            meta=chapter_meta | {"nav_title": entry.title, "enriched_from": "start-heading"},
        )
        chapters.append(chapter)

    # Back matter after final chapter
    back_matter = _collect_back_matter(spine_items, toc_entries, href_to_spine_index)
    if back_matter:
        text = clean_text(to_markdown(back_matter, is_html=True))
        chapters.append(
            _make_chapter(
                chapter_id="back-matter",
                title="Back Matter",
                text=text,
                order=len(chapters),
                source={"href": spine_items[-1].file_name, "anchor": None},
                est_tokens=count_gpt5_tokens(text),
                meta={"gray_zone": True},
            )
        )

    book_meta: dict[str, object] = {}
    if warnings:
        book_meta["warnings"] = warnings

    return Book(
        id=book_id,
        title=title,
        author=author,
        source_format="epub",
        chapters=chapters,
        meta=book_meta,
    )


def _make_chapter(
    *,
    chapter_id: str,
    title: str,
    text: str,
    order: int,
    source: dict[str, str | None],
    est_tokens: int,
    meta: dict[str, object] | None = None,
) -> Chapter:
    return Chapter(
        id=chapter_id,
        title=title,
        text=text,
        order=order,
        source=source,
        est_tokens=est_tokens,
        meta=meta or {},
    )


def _collect_front_matter(
    spine_items: list[epub.EpubHtml],
    toc_entries: list[TocEntry],
    href_to_spine_index: dict[str, int],
) -> str:
    if not spine_items or not toc_entries:
        return ""

    spined = [href_to_spine_index.get(_normalize_href(e.file_href)) for e in toc_entries]
    spined = [i for i in spined if i is not None]
    if not spined:
        return ""

    min_index = min(spined)
    if min_index <= 0:
        return ""

    html_parts = [
        spine_items[i].get_content().decode("utf-8", errors="ignore")
        for i in range(min_index)
    ]
    return "\n".join(html_parts)


def _collect_back_matter(
    spine_items: list[epub.EpubHtml],
    toc_entries: list[TocEntry],
    href_to_spine_index: dict[str, int],
) -> str:
    if not spine_items or not toc_entries:
        return ""

    spined = [href_to_spine_index.get(_normalize_href(e.file_href)) for e in toc_entries]
    spined = [i for i in spined if i is not None]
    if not spined:
        return ""

    max_index = max(spined)
    if max_index >= len(spine_items) - 1:
        return ""

    html_parts = [
        spine_items[i].get_content().decode("utf-8", errors="ignore")
        for i in range(max_index + 1, len(spine_items))
    ]
    return "\n".join(html_parts)


def _ordered_spine_items(epub_book: epub.EpubBook) -> list[epub.EpubHtml]:
    items: list[epub.EpubHtml] = []
    for item_id, _props in epub_book.spine:
        try:
            item = epub_book.get_item_with_id(item_id)
        except KeyError:
            continue
        if isinstance(item, epub.EpubHtml):
            items.append(item)
    return items


def _href_to_spine_index(spine_items: list[epub.EpubHtml]) -> dict[str, int]:
    mapping: dict[str, int] = {}
    for index, item in enumerate(spine_items):
        for candidate in {item.file_name, getattr(item, "href", None), item.get_name()}:
            if candidate:
                mapping[_normalize_href(candidate)] = index
    return mapping


def _normalize_href(href: str | None) -> str:
    if href is None:
        return ""
    return str(Path(href).as_posix())


def _load_toc_entries(epub_book: epub.EpubBook) -> list[TocEntry]:
    # Prefer EPUB 3 Navigation Document if present
    nav_items = [it for it in epub_book.get_items() if isinstance(it, epub.EpubNav)]
    nav_entries = _parse_nav_items(nav_items)
    if nav_entries:
        return nav_entries

    # Fallback: EPUB 2 NCX if present
    ncx_items = [it for it in epub_book.get_items() if isinstance(it, epub.EpubNcx)]
    ncx_entries = _parse_ncx_items(ncx_items)
    if ncx_entries:
        return ncx_entries

    # Final fallback: ebooklib's synthesized book.toc
    return _parse_book_toc(epub_book.toc)


def _nav_leaf_lis(nav: Tag) -> Iterator[Tuple[int, Tag]]:
    """Yield (depth, <li>) for leaf nodes only (no nested <ol>/<ul>) in document order."""

    def _walk_list(list_node: Tag, depth: int) -> Iterator[Tuple[int, Tag]]:
        for li in list_node.find_all("li", recursive=False):
            # If this li contains a nested list, it's a container; walk its children, don't emit it.
            nested = li.find(["ol", "ul"], recursive=False)
            if nested:
                yield from _walk_list(nested, depth + 1)
            else:
                yield depth, li

    top_list = nav.find(["ol", "ul"])
    if top_list:
        yield from _walk_list(top_list, 0)
    else:
        # If the nav has no lists (rare), treat all immediate <li> as leaves.
        for li in nav.find_all("li", recursive=False):
            yield 0, li


def _parse_nav_items(items: Iterable[epub.EpubItem]) -> list[TocEntry]:
    def _best_anchor(li: Tag) -> tuple[Tag, str, str] | None:
        anchors = li.find_all("a", href=True)
        for anchor in anchors:
            file_href, fragment = urldefrag(anchor["href"])
            if file_href:
                return anchor, file_href, fragment or ""
        if anchors:
            anchor = anchors[0]
            file_href, fragment = urldefrag(anchor["href"])
            return anchor, file_href or "", fragment or ""
        return None

    entries: list[TocEntry] = []
    for nav_item in items:
        soup = BeautifulSoup(nav_item.get_content(), "lxml-xml")
        nav = (
            soup.find("nav", attrs={"epub:type": "toc"})
            or soup.find("nav", attrs={"role": "doc-toc"})
            or soup.find("nav")
        )
        if not nav:
            continue

        order = 1
        for _depth, li in _nav_leaf_lis(nav):
            picked = _best_anchor(li)
            if not picked:
                continue
            anchor, file_href, fragment = picked
            entries.append(
                TocEntry(
                    title=anchor.get_text(strip=True) or f"Chapter {order}",
                    href=anchor["href"],
                    file_href=file_href or nav_item.file_name,
                    fragment=fragment or None,
                    order=order,
                )
            )
            order += 1

        if entries:
            break

    # De-duplicate identical targets and prefer entries with a fragment
    return _dedupe_toc_entries(entries)


def _dedupe_toc_entries(entries: list[TocEntry]) -> list[TocEntry]:
    """Remove duplicate targets keyed by (normalized file_href, fragment).
    If duplicates exist, prefer the entry that has a fragment (more precise)."""

    seen: dict[tuple[str, str], TocEntry] = {}
    for e in entries:
        key = (_normalize_href(e.file_href), (e.fragment or ""))
        if key not in seen:
            seen[key] = e
        else:
            prev = seen[key]
            prev_has_frag = bool(prev.fragment)
            cur_has_frag = bool(e.fragment)
            if not prev_has_frag and cur_has_frag:
                seen[key] = e
            # else keep the earlier (reading order) entry

    # preserve original order
    kept: list[TocEntry] = []
    kept_keys: set[tuple[str, str]] = set()
    for e in entries:
        key = (_normalize_href(e.file_href), (e.fragment or ""))
        if key in seen and key not in kept_keys:
            kept.append(seen[key])
            kept_keys.add(key)
    return kept


def _next_spined_entry(
    toc_entries: list[TocEntry],
    start_toc_index: int,
    href_to_spine_index: dict[str, int],
) -> tuple[int | None, int | None]:
    """Return (next_toc_index, spine_index) for the next ToC entry that is in the spine."""

    for candidate in range(start_toc_index + 1, len(toc_entries)):
        normalized = _normalize_href(toc_entries[candidate].file_href)
        spine_idx = href_to_spine_index.get(normalized)
        if spine_idx is not None:
            return candidate, spine_idx
    return None, None


def _parse_ncx_items(items: Iterable[epub.EpubItem]) -> list[TocEntry]:
    entries: list[TocEntry] = []
    for ncx_item in items:
        try:
            root = ET.fromstring(ncx_item.get_content())
        except ET.ParseError:
            continue
        nav_map = root.find("{*}navMap")
        if nav_map is None:
            continue
        for order, nav_point in enumerate(nav_map.findall("{*}navPoint"), start=1):
            label = nav_point.find("{*}navLabel/{*}text")
            content = nav_point.find("{*}content")
            if content is None:
                continue
            file_href, fragment = urldefrag(content.attrib.get("src", ""))
            entries.append(
                TocEntry(
                    title=(label.text if label is not None else f"Chapter {order}") or f"Chapter {order}",
                    href=content.attrib.get("src", ""),
                    file_href=file_href,
                    fragment=fragment or None,
                    order=order,
                )
            )
        if entries:
            break
    return entries


def _parse_book_toc(toc: list[object]) -> list[TocEntry]:
    entries: list[TocEntry] = []
    for order, item in enumerate(toc, start=1):
        title = None
        href = None
        if isinstance(item, epub.Link):
            title = item.title
            href = item.href
        elif isinstance(item, epub.Section):
            title = item.title
            href = item.href
        elif isinstance(item, tuple) and len(item) >= 2:
            title = str(item[0])
            href = str(item[1])
        if not href:
            continue
        file_href, fragment = urldefrag(href)
        entries.append(
            TocEntry(
                title=title or f"Chapter {order}",
                href=href,
                file_href=file_href,
                fragment=fragment or None,
                order=order,
            )
        )
    return entries


def _resolve_spine_item(epub_book: epub.EpubBook, file_href: str) -> epub.EpubHtml | None:
    normalized = _normalize_href(file_href)
    try:
        return epub_book.get_item_with_href(normalized)
    except KeyError:
        # Some manifests use different relative paths; try without normalization
        try:
            return epub_book.get_item_with_href(file_href)
        except KeyError:
            return None


def _as_body_inner(content: bytes, parser: str = "lxml-xml") -> str:
    """Return concatenated HTML of <body> children only (no outer <html>/<body>)."""
    soup = BeautifulSoup(content, parser)
    body = soup.body or soup
    return "".join(str(child) for child in body.children)


_BLOCK_CONTAINERS = {
    "div",
    "p",
    "section",
    "article",
    "li",
    "td",
    "th",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "header",
    "footer",
    "main",
    "nav",
    "figure",
    "figcaption",
    "table",
    "tbody",
    "thead",
    "tr",
    "ul",
    "ol",
    "pre",
    "blockquote",
    "code",
    "aside",
    "body",
}


def _to_block_container(tag: Tag | None) -> Tag | None:
    cur = tag
    while cur and isinstance(cur, Tag) and cur.name not in _BLOCK_CONTAINERS:
        cur = cur.parent
    return cur or tag


def _extract_html_segment(
    content: bytes,
    fragment: str | None,
    next_fragment: str | None,
) -> tuple[str, bool]:
    soup = BeautifulSoup(content, "lxml-xml")
    body = soup.body or soup

    start_container = _locate_fragment_container(soup, fragment)
    missing_anchor = fragment is not None and start_container is None
    if start_container is None:
        start_container = body

    stop_container = _locate_fragment_container(soup, next_fragment)

    if isinstance(start_container, Tag) and start_container.name == "a" and start_container.parent:
        start_container = start_container.parent

    parts: list[str] = []
    for node in _iterate_from_node(start_container):
        if stop_container is not None and isinstance(node, Tag):
            if node is stop_container or stop_container in node.descendants:
                break
        parts.append(str(node))
    return "".join(parts), missing_anchor


def _extract_from_fragment_to_end(content: bytes, fragment: str | None) -> tuple[str, bool]:
    soup = BeautifulSoup(content, "lxml-xml")
    body = soup.body or soup
    start_container = _locate_fragment_container(soup, fragment)
    missing_anchor = fragment is not None and start_container is None
    if start_container is None:
        start_container = body
    parts: list[str] = []
    for node in _iterate_from_node(start_container):
        parts.append(str(node))
    return "".join(parts), missing_anchor


def _extract_start_to_fragment(content: bytes, fragment: str | None) -> tuple[str, bool]:
    soup = BeautifulSoup(content, "lxml-xml")
    body = soup.body or soup
    if fragment is None:
        return "", False  # do not include anything from this file if there's no stop anchor
    stop_container = _locate_fragment_container(soup, fragment)
    missing_anchor = stop_container is None
    if stop_container is None:
        return "", True
    parts: list[str] = []
    for node in body.children:
        if isinstance(node, Tag) and (node is stop_container or stop_container in node.descendants):
            break
        parts.append(str(node))
    return "".join(parts), missing_anchor


def _normalize_title(s: str | None) -> str:
    """Lowercase, strip numbering/punct, collapse whitespace for robust matching."""
    if not s:
        return ""
    s = s.lower()
    # drop leading numbering like "1.", "10:", "iv)", etc.
    s = _re.sub(r"^\s*(?:[ivxlcdm]+|\d+)[\.\):\-\u2013\u2014]?\s+", "", s, flags=_re.IGNORECASE)
    # remove punctuation/non-alnum -> spaces, collapse
    s = _re.sub(r"[^a-z0-9]+", " ", s)
    return _re.sub(r"\s+", " ", s).strip()


def _find_heading_stop_node(soup: BeautifulSoup, normalized_title: str) -> Tag | None:
    """Find the first H1/H2/H3 whose normalized text matches normalized_title."""
    if not normalized_title:
        return None
    for tag in soup.find_all(["h1", "h2", "h3"]):
        raw = tag.get_text(" ", strip=True)
        norm = _normalize_title(raw)
        # allow exact or prefix match either way to be resilient to slight differences
        if norm == normalized_title or norm.startswith(normalized_title) or normalized_title.startswith(norm):
            return tag
    return None


def _extract_until_title(content: bytes, next_title: str | None) -> tuple[str, bool]:
    """Return HTML from top of document up to (but not including) first matching heading.

    Returns (html, matched), where 'matched' is True if we found a stop heading.
    """
    soup = BeautifulSoup(content, "lxml-xml")
    body = soup.body or soup
    stop = _find_heading_stop_node(soup, _normalize_title(next_title))
    if stop is None:
        # No stop heading in this file -> include whole body
        return "".join(str(child) for child in body.children), False

    parts: list[str] = []
    for node in body.children:
        if isinstance(node, Tag) and (node is stop or stop in node.descendants):
            break
        parts.append(str(node))
    return "".join(parts), True


def _gather_chapter_html(
    epub_book: epub.EpubBook,
    spine_items: list[epub.EpubHtml],
    href_to_spine_index: dict[str, int],
    toc_entries: list[TocEntry],
    entry_index: int,
) -> tuple[str, bool]:
    """Gather HTML for the current ToC entry bounded by the next ToC anchor or file.

    - Includes from entry.fragment -> end of its file.
    - Includes whole body of intermediate files (body inner HTML only) when the next entry is in a later file.
    - If there is NO next ToC entry, do NOT include subsequent spine files (Back Matter collector will handle them).
    """
    entry = toc_entries[entry_index]
    start_idx = href_to_spine_index.get(_normalize_href(entry.file_href))
    if start_idx is None:
        return "", True

    missing_any = False
    html_parts: list[str] = []

    next_toc_idx, stop_idx = _next_spined_entry(toc_entries, entry_index, href_to_spine_index)

    # Same file: slice from entry.fragment to next fragment
    if next_toc_idx is not None and stop_idx == start_idx:
        next_entry = toc_entries[next_toc_idx]
        seg, miss = _extract_html_segment(
            spine_items[start_idx].get_content(),
            entry.fragment,
            next_entry.fragment,
        )
        missing_any |= miss
        html_parts.append(seg)
        return "".join(html_parts), missing_any

    # Start file: from entry.fragment to end of file
    start_seg, miss = _extract_from_fragment_to_end(spine_items[start_idx].get_content(), entry.fragment)
    missing_any |= miss
    html_parts.append(start_seg)

    # If there is no next entry: stop at end of current file (no cross-file spillover)
    if stop_idx is None:
        return "".join(html_parts), missing_any

    # Include intermediate whole files (body inner) up to (but not including) the end file
    for i in range(start_idx + 1, stop_idx):
        html_parts.append(_as_body_inner(spine_items[i].get_content()))

    # End file: include up to the stop anchor if present
    stop_entry = toc_entries[next_toc_idx]
    if stop_entry.fragment:
        end_seg, miss2 = _extract_start_to_fragment(
            spine_items[stop_idx].get_content(),
            stop_entry.fragment,
        )
        missing_any |= miss2
        html_parts.append(end_seg)

    return "".join(html_parts), missing_any


def _locate_fragment_container(soup: BeautifulSoup, fragment: str | None) -> Tag | None:
    if not fragment:
        return soup.body or soup
    tag = soup.find(id=fragment) or soup.find(attrs={"name": fragment})
    if tag is None:
        return None
    if not isinstance(tag, Tag):
        tag = getattr(tag, "parent", None)
        if tag is None:
            return None
    return _to_block_container(tag)


def _iterate_from_node(node: Tag | None) -> Iterable[object]:
    if node is None:
        return []
    yield node
    current = node.next_sibling
    while current is not None:
        yield current
        current = current.next_sibling


_HEADING_CLASS_HINTS = _re.compile(
    r"\b(chap(?:ter)?[-_ ]?(?:num|number|no)|chaptitle|chapter[-_ ]?title|title|subtitle|subhead)\b",
    _re.I,
)
_HEADING_TAGS = {"h1", "h2", "h3"}
_MAX_TITLE_LEN = 200


def _text_of(tag: Tag) -> str:
    return (tag.get_text(" ", strip=True) if isinstance(tag, Tag) else "").strip()


def _is_heading_candidate(tag: Tag) -> bool:
    if not isinstance(tag, Tag):
        return False
    if tag.name in _HEADING_TAGS:
        return True
    cls = " ".join(tag.get("class", [])) if tag.has_attr("class") else ""
    if _HEADING_CLASS_HINTS.search(cls or ""):
        return True
    # some publishers put headings in <div> without classes but visually isolated
    # keep it conservative: short-ish text in a block tag near the anchor
    if tag.name in ("div", "p") and len(_text_of(tag)) <= 140:
        # avoid pure ornaments
        t = _text_of(tag)
        if t and not _re.fullmatch(r"[-–—•\s]+", t):
            return True
    return False


def _extract_heading_cluster(soup: BeautifulSoup, fragment: str | None) -> dict[str, str]:
    """
    Return possible pieces: {'chapnum': 'Chapter 3' or '3', 'title': 'Subtitle'} based on nodes
    nearest to the start fragment within the same file.
    """
    body = soup.body or soup
    start = _locate_fragment_container(soup, fragment) or body

    # Collect up to ~8 nodes starting from start and its immediate siblings
    candidates: list[Tag] = []
    scan = 0
    for node in _iterate_from_node(start):
        if isinstance(node, Tag):
            candidates.append(node)
            scan += 1
            if scan >= 8:
                break
    # Also peek at immediate children of start (if it's a block)
    if isinstance(start, Tag):
        for child in list(start.children)[:4]:
            if isinstance(child, Tag):
                candidates.insert(0, child)

    chapnum = ""
    title = ""

    # First pass: direct class/tag hints
    for tag in candidates:
        if not _is_heading_candidate(tag):
            continue
        txt = _text_of(tag)
        if not txt:
            continue
        # Is this a chapter number?
        if not chapnum:
            # patterns: "Chapter 3", "CHAPTER III", bare number "3"
            if _re.search(r"\bchapter\b", txt, _re.I):
                chapnum = txt
            elif _re.fullmatch(r"[IVXLCDM]+", txt) or _re.fullmatch(r"\d{1,3}", txt):
                chapnum = txt
        # Title/subtitle candidate
        if not title:
            # avoid reusing the pure number as title
            if not _re.fullmatch(r"\d{1,3}", txt):
                title = txt

        if chapnum and title:
            break

    # Second pass: if still missing title, look for first heading-like text
    if not title:
        for tag in candidates:
            if _is_heading_candidate(tag):
                t = _text_of(tag)
                if t and not _re.fullmatch(r"\d{1,3}", t):
                    title = t
                    break

    return {"chapnum": chapnum.strip(), "title": title.strip()}


_CHAPTER_NUM_RE = _re.compile(r"\bchapter\s+([0-9]+|[IVXLCDM]+)\b", _re.I)


def _merge_nav_and_heading(nav_title: str, pieces: dict[str, str]) -> str:
    """
    Compose an enriched title from NAV text and extracted headings.
    Rules:
      - If both chapnum and title exist: "Chapter N — Title" (avoid duplicating 'Chapter N' if nav already has it).
      - If only title exists and looks richer than nav, prefer title.
      - Else keep nav_title.
    """
    nav = (nav_title or "").strip()
    chapnum = pieces.get("chapnum", "")
    local_title = pieces.get("title", "")

    def has_chapnum(s: str) -> bool:
        return bool(_CHAPTER_NUM_RE.search(s))

    # Normalize dash
    def cap_len(s: str) -> str:
        return s if len(s) <= _MAX_TITLE_LEN else s[: _MAX_TITLE_LEN - 1] + "…"

    if chapnum and local_title:
        # If NAV already starts with chapnum, avoid repeating it
        if has_chapnum(nav):
            return cap_len(f"{nav} — {local_title}") if local_title.lower() not in nav.lower() else cap_len(nav)
        # If chapnum is just a number "3", format as "Chapter 3"
        if not has_chapnum(chapnum):
            chapnum_fmt = f"Chapter {chapnum}"
        else:
            chapnum_fmt = chapnum
        return cap_len(f"{chapnum_fmt} — {local_title}")

    if local_title:
        # Prefer richer title if NAV looks generic ("Chapter 3", "Chapter")
        if has_chapnum(nav) or nav.lower().startswith("chapter"):
            return cap_len(local_title)
        # If NAV already contains local title, keep NAV
        if local_title.lower() in nav.lower():
            return cap_len(nav)
        return cap_len(local_title)

    return cap_len(nav or "Untitled")


def _first_or_default(metadata: list[tuple[str, dict]]) -> str | None:
    if not metadata:
        return None
    return metadata[0][0]


__all__ = ["ingest_epub"]
