from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Sequence

from .models import Book, Chapter
from .normalize import slugify

_FRONT_SLUGS = {
    "cover", "half-title", "halftitle", "title", "title-page",
    "copyright", "dedication", "contents", "acknowledgments", "acknowledgements",
}
_BACK_SLUGS_PREFIX = ("appendix",)  # appendix a/b/c...
_BACK_SLUGS_EXACT = {"notes", "selected-bibliography", "bibliography", "index"}

@dataclass(slots=True)
class Selection:
    skip_front: bool = False
    skip_parts: bool = False
    skip_back: bool = False
    from_spec: Optional[str] = None
    to_spec: Optional[str] = None
    include_regex: Optional[str] = None
    exclude_regex: Optional[str] = None
    only_ids: Sequence[str] | None = None
    only_slugs: Sequence[str] | None = None

def _chapter_slug(ch: Chapter) -> str:
    s = (ch.meta or {}).get("slug")
    return s if isinstance(s, str) and s else slugify(ch.title)

def _is_part(ch: Chapter) -> bool:
    title = (ch.title or "").strip()
    slug = _chapter_slug(ch)
    return title.lower().startswith("part ") or slug.startswith("part-")

def _is_front(ch: Chapter) -> bool:
    slug = _chapter_slug(ch)
    return slug in _FRONT_SLUGS

def _is_back(ch: Chapter) -> bool:
    slug = _chapter_slug(ch)
    return slug in _BACK_SLUGS_EXACT or any(slug.startswith(p) for p in _BACK_SLUGS_PREFIX)

def _resolve_spec(book: Book, spec: Optional[str]) -> Optional[int]:
    if not spec:
        return None
    s = spec.strip()
    # Try by order integer
    if s.isdigit():
        order = int(s)
        idx = next((i for i, ch in enumerate(book.chapters) if ch.order == order), None)
        if idx is not None:
            return idx
    # Try id, slug, title (casefold)
    s_cf = s.casefold()
    for i, ch in enumerate(book.chapters):
        if ch.id.casefold() == s_cf:
            return i
        if _chapter_slug(ch) == slugify(s):
            return i
        if (ch.title or "").casefold() == s_cf:
            return i
    return None

def _regex_pred(pattern: Optional[str]):
    if not pattern:
        return lambda _ch: True
    rx = re.compile(pattern, re.I)
    return lambda ch: (rx.search(ch.title or "") is not None) or (rx.search(_chapter_slug(ch)) is not None)

def _apply_basic_filters(chapters: list[Chapter], sel: Selection) -> list[Chapter]:
    result = list(chapters)
    if sel.only_ids:
        ids = {s.strip() for s in sel.only_ids if s and s.strip()}
        result = [ch for ch in result if ch.id in ids]
    if sel.only_slugs:
        slugs = {slugify(s.strip()) for s in sel.only_slugs if s and s.strip()}
        result = [ch for ch in result if _chapter_slug(ch) in slugs]

    if sel.skip_front:
        result = [ch for ch in result if not _is_front(ch)]
    if sel.skip_parts:
        result = [ch for ch in result if not _is_part(ch)]
    if sel.skip_back:
        result = [ch for ch in result if not _is_back(ch)]

    inc = _regex_pred(sel.include_regex)
    result = [ch for ch in result if inc(ch)]

    if sel.exclude_regex:
        rx = re.compile(sel.exclude_regex, re.I)
        result = [ch for ch in result if not (rx.search(ch.title or "") or rx.search(_chapter_slug(ch)))]

    return result

def select_chapters(book: Book, sel: Selection) -> list[Chapter]:
    """Return chapters in original order after applying selection rules."""
    if not book.chapters:
        return []
    # Window by from/to on the full list first (by intent)
    start = _resolve_spec(book, sel.from_spec) or 0
    end = _resolve_spec(book, sel.to_spec)
    window = book.chapters[start : (end + 1) if end is not None else None]
    # Now apply inclusive filters on the window
    filtered = _apply_basic_filters(window, sel)
    # Preserve original order
    id_set = {ch.id for ch in filtered}
    return [ch for ch in book.chapters if ch.id in id_set and ch in filtered]

def any_filters_set(sel: Selection) -> bool:
    return any([
        sel.skip_front, sel.skip_parts, sel.skip_back,
        bool(sel.from_spec), bool(sel.to_spec),
        bool(sel.include_regex), bool(sel.exclude_regex),
        bool(sel.only_ids), bool(sel.only_slugs),
    ])

def load_selection_file(path: Path) -> Selection:
    """Load Selection from YAML or JSON file."""
    raw = path.read_text(encoding="utf-8")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        import yaml  # type: ignore
        data = yaml.safe_load(raw) or {}
    def arr(x):
        if x is None:
            return None
        if isinstance(x, str):
            return [p.strip() for p in x.split(",") if p.strip()]
        return list(x)
    return Selection(
        skip_front=bool(data.get("skip_front", False)),
        skip_parts=bool(data.get("skip_parts", False)),
        skip_back=bool(data.get("skip_back", False)),
        from_spec=data.get("from"),
        to_spec=data.get("to"),
        include_regex=data.get("include") or data.get("include_regex"),
        exclude_regex=data.get("exclude") or data.get("exclude_regex"),
        only_ids=arr(data.get("only_ids")),
        only_slugs=arr(data.get("only_slugs")),
    )
