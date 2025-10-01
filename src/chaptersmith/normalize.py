"""Utilities for normalizing book content."""

from __future__ import annotations

import re
import unicodedata
from typing import Iterable

from bs4 import BeautifulSoup, Tag

NBSP = "\u00A0"
_HEADING_LEVELS = {f"h{level}": level for level in range(1, 7)}
_BLOCK_TAGS = tuple(_HEADING_LEVELS) + ("p", "li", "pre", "blockquote", "code", "figcaption")


def _strip_scripts_and_styles(soup: BeautifulSoup) -> None:
    for tag in soup.find_all(["script", "style"]):
        tag.decompose()


def _render_block(tag: Tag) -> str | None:
    name = tag.name
    if not name:
        return None

    if name == "pre":
        raw = tag.get_text("\n", strip=False)
        normalized = raw.rstrip("\n")
        return f"```\n{normalized}\n```"

    if name == "blockquote":
        lines = [line.rstrip() for line in tag.get_text("\n", strip=True).splitlines()]
        rendered = "\n".join(f"> {line}" if line else ">" for line in lines)
        return rendered if rendered.strip(" >") else None

    text = tag.get_text(" ", strip=True)
    if not text:
        return None

    if name in _HEADING_LEVELS:
        level = _HEADING_LEVELS[name]
        prefix = "#" * level
        return f"{prefix} {text}"

    if name == "li":
        return f"- {text}"

    if name == "code":
        return f"`{text}`"

    return text


def _iter_blocks(soup: BeautifulSoup) -> Iterable[str]:
    for tag in soup.find_all(_BLOCK_TAGS):
        rendered = _render_block(tag)
        if rendered:
            yield rendered


def to_markdown(text_or_html: str, is_html: bool) -> str:
    """Normalize text or HTML into Markdown.

    If is_html: render lightweight Markdown by walking block-ish tags. If that
    misses too much text (tables, dl/dt/dd, div+br indices), fall back to the
    page's raw text to avoid data loss.
    """
    if not is_html:
        return clean_text(text_or_html)

    soup = BeautifulSoup(text_or_html, "lxml")
    _strip_scripts_and_styles(soup)

    blocks = list(_iter_blocks(soup))
    raw_text = soup.get_text("\n", strip=True)

    if not blocks:
        markdown = raw_text
    else:
        joined = "\n\n".join(blocks)
        if len(raw_text) > 200 and len(joined) < 0.5 * len(raw_text):
            markdown = raw_text
        else:
            markdown = joined

    return clean_text(markdown)


def clean_text(s: str) -> str:
    """Normalize whitespace and line breaks for downstream processing."""

    normalized = s.replace("\r\n", "\n").replace("\r", "\n")
    normalized = normalized.replace(NBSP, " ")
    normalized = re.sub(r"(?<=\w)-\n(?=\w)", "", normalized)
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)
    normalized = re.sub(r"[ \t]+\n", "\n", normalized)
    return normalized.strip()


def paragraphs(s: str) -> list[str]:
    """Split text into paragraphs separated by blank lines."""

    cleaned = clean_text(s)
    parts = re.split(r"\n{2,}", cleaned)
    return [part.strip() for part in parts if part.strip()]


_DASH_RE = re.compile(r"[\u2012\u2013\u2014\u2015\u2212]+")


def slugify(text: str) -> str:
    """Convert text to lowercase ASCII kebab-case. Collapse/trim dashes. Return 'untitled' if empty."""
    if not text:
        return "untitled"
    # Normalize and replace Unicode dashes with "-"
    s = unicodedata.normalize("NFKD", text)
    s = _DASH_RE.sub("-", s)
    # ASCII fold (drop accents); then lowercase
    s = s.encode("ascii", "ignore").decode("ascii").lower()
    # Replace non-alnum with "-"
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    # Collapse duplicate dashes
    s = re.sub(r"-{2,}", "-", s)
    return s or "untitled"
