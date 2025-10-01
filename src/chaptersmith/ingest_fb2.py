"""FB2 ingestion pipeline stub."""

from __future__ import annotations

from pathlib import Path

from .models import Book


def ingest_fb2(path: Path) -> Book:
    """Read an FB2 file and return a structured ``Book`` instance."""

    raise NotImplementedError("FB2 ingestion not implemented yet.")
