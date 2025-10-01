"""HTML and Markdown ingestion pipelines."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Literal

from bs4 import BeautifulSoup, Tag

from .models import Book, Chapter
from .normalize import clean_text, to_markdown, slugify
from .tokenize_count import count_gpt5_tokens

_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)")


def ingest_html(
    path: Path,
    *,
    book_id: str | None = None,
    title: str | None = None,
    author: str | None = None,
) -> Book:
    """Read an HTML file and return a structured ``Book`` instance."""

    return _ingest_html_md(path, "html", book_id=book_id, title=title, author=author)


def ingest_markdown(
    path: Path,
    *,
    book_id: str | None = None,
    title: str | None = None,
    author: str | None = None,
) -> Book:
    """Read a Markdown file and return a structured ``Book`` instance."""

    return _ingest_html_md(path, "md", book_id=book_id, title=title, author=author)


def _ingest_html_md(
    path: Path,
    format_hint: Literal["html", "md"],
    *,
    book_id: str | None,
    title: str | None,
    author: str | None,
) -> Book:
    content = path.read_text(encoding="utf-8")
    default_title = title or path.stem.replace("_", " ").strip() or "Document"
    book = Book(
        id=book_id or path.stem,
        title=title or default_title,
        author=author or "Unknown",
        source_format=format_hint,
        chapters=[],
        meta={},
    )

    if format_hint == "html":
        chapters, warnings = _split_html(content, path)
    else:
        chapters, warnings = _split_markdown(content, path)

    book.chapters = chapters
    if warnings:
        book.meta["warnings"] = warnings
    return book


def _split_html(content: str, path: Path) -> tuple[list[Chapter], list[str]]:
    soup = BeautifulSoup(content, "lxml")
    warnings: list[str] = []

    heading_tag = "h1"
    headings = soup.find_all(heading_tag)
    primary_level = 1
    if not headings:
        heading_tag = "h2"
        headings = soup.find_all(heading_tag)
        primary_level = 2
    if not headings:
        fallback_heading = soup.find(re.compile(r"^h[1-6]$"))
        if fallback_heading is None:
            text = clean_text(to_markdown(content, is_html=True))
            chapter = _make_chapter(
                chapter_id="chapter-01",
                title=path.stem,
                text=text,
                order=1,
                source={"href": path.name, "anchor": None},
                meta={},
            )
            chapter.est_tokens = count_gpt5_tokens(chapter.text)
            return [chapter], warnings
        heading_tag = fallback_heading.name
        headings = soup.find_all(heading_tag)
        primary_level = int(fallback_heading.name[1])

    chapters: list[Chapter] = []
    previous_level = primary_level
    initial_anomaly = primary_level > 2

    for index, heading in enumerate(headings, start=1):
        level = int(heading.name[1])
        html_segment = _collect_section_html(heading)
        text = clean_text(to_markdown(html_segment, is_html=True))
        title = heading.get_text(strip=True) or f"Section {index}"
        chapter_meta: dict[str, object] = {}

        inconsistent = False
        if initial_anomaly:
            inconsistent = True
        if index == 1 and level > primary_level:
            inconsistent = True
        if index > 1 and level - previous_level > 1:
            inconsistent = True
        if inconsistent:
            chapter_meta["gray_zone"] = True
            warnings.append(f"Heading level anomaly near '{title}'")

        previous_level = level

        chapter = _make_chapter(
            chapter_id=f"chapter-{index:02d}",
            title=title,
            text=text,
            order=index,
            source={"href": path.name, "anchor": heading.get("id")},
            meta=chapter_meta,
        )
        chapter.est_tokens = count_gpt5_tokens(chapter.text)
        chapters.append(chapter)

    return chapters, warnings


def _collect_section_html(heading: Tag) -> str:
    parts: list[str] = [str(heading)]
    level = int(heading.name[1])
    current = heading.next_sibling
    while current is not None:
        if isinstance(current, Tag) and current.name.lower().startswith("h") and len(current.name) == 2 and current.name[1].isdigit():
            next_level = int(current.name[1])
            if next_level <= level:
                break
        parts.append(str(current))
        current = current.next_sibling
    return "".join(parts)


def _split_markdown(content: str, path: Path) -> tuple[list[Chapter], list[str]]:
    lines = content.splitlines()
    warnings: list[str] = []

    headings = [idx for idx, line in enumerate(lines) if _HEADING_RE.match(line)]
    if not headings:
        text = clean_text(to_markdown(content, is_html=False))
        chapter = _make_chapter(
            chapter_id="chapter-01",
            title=path.stem,
            text=text,
            order=1,
            source={"href": path.name, "anchor": None},
            meta={},
        )
        chapter.est_tokens = count_gpt5_tokens(chapter.text)
        return [chapter], warnings

    primary_level = 1
    if not any(lines[idx].startswith("# ") for idx in headings):
        primary_level = 2

    chapters: list[Chapter] = []
    previous_level = primary_level
    for position, start_index in enumerate(headings):
        match = _HEADING_RE.match(lines[start_index])
        assert match is not None  # pragma: no cover - defensive
        level = len(match.group(1))
        title = match.group(2).strip()
        end_index = _next_heading_index(headings, position, len(lines))
        block_lines = lines[start_index:end_index]
        text_block = "\n".join(block_lines)
        text = clean_text(to_markdown(text_block, is_html=False))
        chapter_meta: dict[str, object] = {}
        inconsistent = False
        if position == 0 and level > primary_level:
            inconsistent = True
        if position > 0 and level - previous_level > 1:
            inconsistent = True
        if inconsistent:
            chapter_meta["gray_zone"] = True
            warnings.append(f"Heading level anomaly near '{title}'")

        previous_level = level
        chapter = _make_chapter(
            chapter_id=f"chapter-{position + 1:02d}",
            title=title or f"Section {position + 1}",
            text=text,
            order=position + 1,
            source={"href": path.name, "anchor": slugify(title)},
            meta=chapter_meta,
        )
        chapter.est_tokens = count_gpt5_tokens(chapter.text)
        chapters.append(chapter)

    return chapters, warnings


def _next_heading_index(headings: list[int], position: int, total_lines: int) -> int:
    if position + 1 >= len(headings):
        return total_lines
    return headings[position + 1]


def _make_chapter(
    *,
    chapter_id: str,
    title: str,
    text: str,
    order: int,
    source: dict[str, str | None],
    meta: dict[str, object],
) -> Chapter:
    return Chapter(
        id=chapter_id,
        title=title,
        text=text,
        order=order,
        source=source,
        est_tokens=None,
        meta=meta,
    )


__all__ = ["ingest_html", "ingest_markdown"]
