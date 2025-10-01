"""Data models used across Chaptersmith."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal


SourceFormat = Literal["epub", "html", "md", "fb2"]


@dataclass(slots=True)
class Chapter:
    """Represents an individual chapter from an ingest pipeline."""

    id: str
    title: str
    text: str
    order: int
    source: dict[str, str | None] = field(default_factory=dict)
    est_tokens: int | None = None
    meta: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class Book:
    """Represents a logical book with structured chapters."""

    id: str
    title: str
    author: str
    source_format: SourceFormat
    chapters: list[Chapter] = field(default_factory=list)
    meta: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class SuperChunk:
    """Represents a chunk of chapters tailored to a model profile."""

    id: str
    profile: str
    chapter_ids: list[str]
    text: str
    est_tokens: int
    meta: dict[str, Any] = field(default_factory=dict)
