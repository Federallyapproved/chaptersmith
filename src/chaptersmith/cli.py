"""Command line interface for Chaptersmith."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Iterable, Literal, Optional

import typer
from rich.console import Console
from rich.table import Table

from .chapter_bundler import bundle_book, validate_superchunks
from .ingest_epub import ingest_epub
from .ingest_html_md import ingest_html, ingest_markdown
from .models import Book, Chapter, SuperChunk
from .profiles import ALL_PROFILES, ModelProfile
from .tokenize_count import count_gpt5_tokens
from .selection import (
    Selection,
    any_filters_set,
    load_selection_file,
    select_chapters,
)

app = typer.Typer(name="chaptersmith")
console = Console()

_FORMATS = {"epub", "html", "md", "fb2"}


def _resolve_profile(profile_name: str) -> ModelProfile:
    try:
        return ALL_PROFILES[profile_name]
    except KeyError as exc:  # pragma: no cover - defensive branch
        raise typer.BadParameter(f"Unknown profile '{profile_name}'.") from exc


_SLUG_MAX = 160


def _slugify_title(title: str) -> str:
    s = title.lower()
    # normalize dashes and remove accents-ish by dropping non-ascii chars that aren't alnum/space/hyphen
    s = s.replace("–", "-").replace("—", "-")
    s = re.sub(r"[^\w\s-]", "", s, flags=re.ASCII)  # keep alnum, underscore, hyphen, space
    s = re.sub(r"[_\s]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s[:_SLUG_MAX] or "untitled"


def _norm_title(s: str) -> str:
    s = s.lower()
    s = re.sub(r"^\s*(?:[ivxlcdm]+|\d+)[\.\):\-\u2013\u2014]?\s+", "", s, flags=re.IGNORECASE)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


_FRONT_KEYS = {
    "cover",
    "half title page",
    "title page",
    "copyright",
    "dedication",
    "contents",
    "acknowledgments",
    "preface",
}

_BACK_KEYS = {
    "appendix",
    "notes",
    "bibliography",
    "selected bibliography",
    "index",
}


def _classify_kind(title: str, est_tokens: int | None) -> str:
    title = title or ""
    base = _norm_title(title)
    if base in ("cover", "half title page", "title page"):
        return "title-page" if base != "cover" else "cover"
    for k in _FRONT_KEYS:
        if base == k:
            return k.replace(" ", "-")
    for k in _BACK_KEYS:
        if base.startswith(k):
            return "bibliography" if "bibliograph" in base else k.replace(" ", "-")
    if base.startswith("part ") or base.startswith("section "):
        if (est_tokens or 0) < 150:
            return "part-cover"
    return "chapter"


def _apply_selection(
    chapters: list[Chapter],
    start_title: str | None,
    end_title: str | None,
    skip_kinds: Iterable[str],
) -> list[Chapter]:
    def title_matches(ch: Chapter, needle: str) -> bool:
        return needle.lower() in (ch.title or "").lower()

    start_idx = 0
    end_idx = len(chapters) - 1
    if start_title:
        for i, ch in enumerate(chapters):
            if title_matches(ch, start_title):
                start_idx = i
                break
    if end_title:
        for i, ch in enumerate(chapters[start_idx:], start=start_idx):
            if title_matches(ch, end_title):
                end_idx = i
                break

    window = [ch for ch in chapters[start_idx : end_idx + 1]]
    skip = {k.lower() for k in skip_kinds if isinstance(k, str)}
    if not skip:
        return window
    return [ch for ch in window if (ch.meta or {}).get("kind", "chapter").lower() not in skip]


@app.command()
def split(
    input_path: Path = typer.Argument(..., help="Path to the source book."),
    format: Literal["epub", "html", "md", "fb2"] = typer.Option(
        ..., "--format", "-f", help="Source format."
    ),
    out: Path | None = typer.Option(None, help="Output directory (default: slug of book title)."),
    book_id: str | None = typer.Option(None, help="Override book identifier."),
    title: str | None = typer.Option(None, help="Override book title."),
    author: str | None = typer.Option(None, help="Override book author."),
    skip_kinds: list[str] = typer.Option(
        [],
        "--skip-kinds",
        help="Kinds to omit (repeatable). E.g., --skip-kinds cover --skip-kinds title-page --skip-kinds part-cover",
    ),
    start_title: str | None = typer.Option(
        None,
        "--start-title",
        help="Start from the first chapter whose title contains this text (case-insensitive).",
    ),
    end_title: str | None = typer.Option(
        None,
        "--end-title",
        help="End after the first chapter whose title contains this text (case-insensitive).",
    ),
) -> None:
    """Split a book into normalized chapters."""

    if format not in _FORMATS:
        raise typer.BadParameter(f"Unsupported format '{format}'.")

    if format == "epub":
        book = ingest_epub(input_path, book_id=book_id, title=title, author=author)
    elif format == "html":
        book = ingest_html(input_path, book_id=book_id, title=title, author=author)
    elif format == "md":
        book = ingest_markdown(input_path, book_id=book_id, title=title, author=author)
    else:  # fb2
        raise typer.BadParameter("FB2 ingestion is not yet implemented.")

    # Compute default outdir if not provided
    outdir = out or Path(_slugify_title(book.title))

    # Classify chapters and optionally select subset
    for ch in book.chapters:
        ch.meta = ch.meta or {}
        kind = _classify_kind(ch.title, ch.est_tokens)
        ch.meta["kind"] = kind

    selected = _apply_selection(
        book.chapters,
        start_title,
        end_title,
        skip_kinds,
    )
    book.chapters = selected

    _write_manifest(book, input_path, outdir)
    _write_chapters(book, outdir)
    _write_index(book, outdir)

    console.print(f"[green]Wrote chapters to {outdir}[/]")


@app.command()
def bundle(
    outdir: Path = typer.Argument(..., help="Directory containing book manifest and chapters."),
    profile: str = typer.Option(..., help="Profile used for bundling."),
    select: Optional[Path] = typer.Option(None, help="Selection YAML/JSON."),
    skip_front: bool = typer.Option(False, help="Skip front matter."),
    skip_parts: bool = typer.Option(False, help="Skip 'Part ...' pages."),
    skip_back: bool = typer.Option(False, help="Skip back matter."),
    from_spec: Optional[str] = typer.Option(None, "--from", help="Start chapter (id/slug/title/order)."),
    to_spec: Optional[str] = typer.Option(None, "--to", help="End chapter (id/slug/title/order)."),
    include_regex: Optional[str] = typer.Option(None, help="Regex to include (title or slug)."),
    exclude_regex: Optional[str] = typer.Option(None, help="Regex to exclude (title or slug)."),
    only_ids: Optional[str] = typer.Option(None, help="Comma-separated ids to include."),
    only_slugs: Optional[str] = typer.Option(None, help="Comma-separated slugs to include."),
) -> None:
    """Bundle chapter data into superchunks."""

    book = _load_book(outdir)
    sel = _build_selection(select, skip_front, skip_parts, skip_back, from_spec, to_spec, include_regex, exclude_regex, only_ids, only_slugs)
    if any_filters_set(sel):
        chosen = select_chapters(book, sel)
        book = Book(
            id=book.id,
            title=book.title,
            author=book.author,
            source_format=book.source_format,
            chapters=chosen,
            meta=book.meta,
        )

    model_profile = _resolve_profile(profile)
    standard, oversized = bundle_book(book, model_profile, output_dir=outdir)
    validate_superchunks(standard + oversized, model_profile)
    console.print(
        f"[green]Generated {len(standard)} standard and {len(oversized)} oversized super-chunks[/]"
    )


@app.command()
def validate(
    outdir: Path = typer.Argument(..., help="Directory containing bundled superchunks."),
    profile: str = typer.Option(..., help="Profile used for validation."),
) -> None:
    """Validate super-chunk artifacts against the profile budgets."""

    model_profile = _resolve_profile(profile)
    chunks = list(_discover_superchunks(outdir, model_profile))
    validate_superchunks(chunks, model_profile)
    console.print("[green]All super-chunks are within budget.[/]")


@app.command()
def stats(
    outdir: Path = typer.Argument(..., help="Directory with chapters and manifest."),
    skip_kinds: list[str] = typer.Option(
        [],
        "--skip-kinds",
        help="Kinds to omit when computing selected totals (repeatable).",
    ),
    start_title: str | None = typer.Option(
        None, "--start-title", help="Start from the first chapter whose title contains this text."
    ),
    end_title: str | None = typer.Option(
        None, "--end-title", help="End after the first chapter whose title contains this text."
    ),
) -> None:
    """Show token usage statistics for a chapter set."""

    book = _load_book(outdir)

    # Classify (in case split did not add kinds) and compute table
    for chapter in book.chapters:
        chapter.meta = chapter.meta or {}
        if "kind" not in chapter.meta:
            chapter.meta["kind"] = _classify_kind(chapter.title, chapter.est_tokens)

    table = Table(title=f"Token Stats for {book.title}")
    table.add_column("Chapter")
    table.add_column("Title")
    table.add_column("Tokens", justify="right")

    total_tokens = 0
    tokenizer = count_gpt5_tokens
    for chapter in book.chapters:
        tokens = chapter.est_tokens or tokenizer(chapter.text)
        total_tokens += tokens
        table.add_row(str(chapter.order), chapter.title, str(tokens))

    console.print(table)

    # Selected subtotal
    selected = _apply_selection(
        book.chapters,
        start_title,
        end_title,
        (k.lower() for k in skip_kinds),
    )
    selected_tokens = sum((ch.est_tokens or tokenizer(ch.text)) for ch in selected)

    console.print(
        f"[bold]Selected tokens:[/] {selected_tokens} (selected {len(selected)} of {len(book.chapters)})"
    )
    console.print(f"[bold]Total tokens:[/] {total_tokens}")

    console.print("\n[bold]Estimated Super-Chunks:[/]")
    for profile in ALL_PROFILES.values():
        estimate = max(1, (total_tokens + profile.safe_input_budget - 1) // profile.safe_input_budget)
        console.print(f"- {profile.name}: ~{estimate}")

@app.command()
def export(
    outdir: Path = typer.Argument(..., help="Directory with chapters and manifest."),
    select: Optional[Path] = typer.Option(None, help="Selection YAML/JSON."),
    skip_front: bool = typer.Option(False, help="Skip front matter."),
    skip_parts: bool = typer.Option(False, help="Skip 'Part ...' pages."),
    skip_back: bool = typer.Option(False, help="Skip back matter."),
    from_spec: Optional[str] = typer.Option(None, "--from", help="Start chapter (id/slug/title/order)."),
    to_spec: Optional[str] = typer.Option(None, "--to", help="End chapter (id/slug/title/order)."),
    include_regex: Optional[str] = typer.Option(None, help="Regex to include (title or slug)."),
    exclude_regex: Optional[str] = typer.Option(None, help="Regex to exclude (title or slug)."),
    only_ids: Optional[str] = typer.Option(None, help="Comma-separated ids to include."),
    only_slugs: Optional[str] = typer.Option(None, help="Comma-separated slugs to include."),
    join: Optional[Path] = typer.Option(None, help="Write a single joined Markdown to this path."),
    print_total: bool = typer.Option(False, help="Print total tokens for the selected set."),
) -> None:
    book = _load_book(outdir)
    sel = _build_selection(select, skip_front, skip_parts, skip_back, from_spec, to_spec, include_regex, exclude_regex, only_ids, only_slugs)
    chosen = select_chapters(book, sel) if any_filters_set(sel) else book.chapters
    tokenizer = count_gpt5_tokens
    total = sum((ch.est_tokens or tokenizer(ch.text)) for ch in chosen)

    if join:
        join_path = join if join.is_absolute() else (outdir / join)
        join_path.parent.mkdir(parents=True, exist_ok=True)
        blocks = [
            f"# [Chapter {ch.order} — {ch.title}]\n\n{ch.text.rstrip()}"
            for ch in chosen
        ]
        join_path.write_text("\n\n---\n".join(blocks) + "\n", encoding="utf-8")
        console.print(f"[green]Wrote joined Markdown:[/] {join_path}")

    if print_total:
        console.print(f"[bold]Selected tokens:[/] {total} ({len(chosen)} chapters)")



def _write_manifest(book: Book, input_path: Path, outdir: Path) -> None:
    manifest_path = outdir / "book"
    manifest_path.mkdir(parents=True, exist_ok=True)
    manifest_file = manifest_path / "manifest.json"

    data = {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "source_format": book.source_format,
        "source_path": str(input_path),
        "meta": book.meta,
    }
    manifest_file.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def _write_chapters(book: Book, outdir: Path) -> None:
    chapters_dir = outdir / "chapters"
    chapters_dir.mkdir(parents=True, exist_ok=True)

    used: set[str] = set()
    for chapter in book.chapters:
        chapter.meta = chapter.meta or {}
        base = _slugify_title(chapter.title)
        slug = base
        suffix = 1
        while slug in used:
            suffix += 1
            slug = f"{base}-{suffix}"
        used.add(slug)

        filename = chapters_dir / f"{slug}.md"
        front_matter = {
            "id": chapter.id,
            "title": chapter.title,
            "order": chapter.order,
            "source": chapter.source,
            "est_tokens": chapter.est_tokens or 0,
            "meta": chapter.meta,
        }
        body = chapter.text.rstrip("\n")
        content = "\n".join(("---", json.dumps(front_matter, indent=2), "---", body))
        filename.write_text(content + "\n", encoding="utf-8")

        # Attach filename to meta for index writing
        chapter.meta["filename"] = f"{slug}.md"


def _write_index(book: Book, outdir: Path) -> None:
    index_file = outdir / "chapters_index.json"
    chapter_entries: list[dict[str, object]] = []
    for chapter in book.chapters:
        meta = chapter.meta or {}
        chapter_entries.append(
            {
                "id": chapter.id,
                "title": chapter.title,
                "order": chapter.order,
                "est_tokens": chapter.est_tokens or 0,
                "source": chapter.source,
                "meta": meta,
                "filename": meta.get("filename", f"{chapter.id}.md"),
                "kind": meta.get("kind", "chapter"),
            }
        )

    data = {
        "book": {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "source_format": book.source_format,
        },
        "chapters": chapter_entries,
    }
    index_file.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def _load_book(outdir: Path) -> Book:
    manifest_path = outdir / "book" / "manifest.json"
    index_path = outdir / "chapters_index.json"
    if not manifest_path.exists() or not index_path.exists():
        raise typer.BadParameter(
            "Output directory must contain book/manifest.json and chapters_index.json"
        )

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    index = json.loads(index_path.read_text(encoding="utf-8"))

    chapters: list[Chapter] = []
    chapters_dir = outdir / "chapters"
    for chapter_info in index.get("chapters", []):
        filename = chapter_info.get("filename") or chapter_info.get("file") or f"{chapter_info['id']}.md"
        chapter_file = chapters_dir / filename
        fallback_meta_raw = chapter_info.get("meta") or {}
        fallback_meta = fallback_meta_raw if isinstance(fallback_meta_raw, dict) else {}
        file_meta: dict[str, object] = dict(fallback_meta)
        file_meta.setdefault("filename", filename)
        kind_hint = chapter_info.get("kind")
        if isinstance(kind_hint, str) and kind_hint:
            file_meta.setdefault("kind", kind_hint)

        est_tokens = chapter_info.get("est_tokens") or None
        text = ""
        if chapter_file.exists():
            text, front_meta = _read_markdown_payload(chapter_file, fallback_meta=fallback_meta)
            est_tokens = front_meta.get("est_tokens", est_tokens)
            meta_candidate = front_meta.get("meta", fallback_meta)
            if isinstance(meta_candidate, dict):
                file_meta = dict(meta_candidate)
            file_meta.setdefault("filename", filename)
            slug_value = front_meta.get("slug")
            if isinstance(slug_value, str) and slug_value and "slug" not in file_meta:
                file_meta["slug"] = slug_value
            file_value = front_meta.get("file") or front_meta.get("filename")
            if isinstance(file_value, str) and file_value and "filename" not in file_meta:
                file_meta["filename"] = file_value
        elif not file_meta.get("filename"):
            file_meta["filename"] = filename

        if isinstance(kind_hint, str) and kind_hint and "kind" not in file_meta:
            file_meta["kind"] = kind_hint

        slug_hint = chapter_info.get("slug")
        if isinstance(slug_hint, str) and slug_hint and "slug" not in file_meta:
            file_meta["slug"] = slug_hint

        chapter = Chapter(
            id=chapter_info["id"],
            title=chapter_info["title"],
            text=text,
            order=chapter_info["order"],
            source=chapter_info.get("source", {}),
            est_tokens=est_tokens,
            meta=file_meta,
        )
        chapters.append(chapter)

    return Book(
        id=manifest.get("id", "unknown"),
        title=manifest.get("title", "Untitled"),
        author=manifest.get("author", "Unknown"),
        source_format=manifest.get("source_format", "unknown"),
        chapters=chapters,
        meta=manifest.get("meta", {}),
    )


def _discover_superchunks(outdir: Path, profile: ModelProfile) -> Iterable[SuperChunk]:
    profile_dir = outdir / "superchunks" / profile.name
    if not profile_dir.exists():
        raise typer.BadParameter(
            f"No superchunk directory found for profile {profile.name} in {profile_dir}"
        )

    index_path = profile_dir / "index.json"
    if not index_path.exists():
        raise typer.BadParameter(f"Missing index.json for profile {profile.name}")

    index = json.loads(index_path.read_text(encoding="utf-8"))
    chunks: list[SuperChunk] = []
    for entry in index.get("chunks", []):
        chunk_file = profile_dir / f"{entry['id']}.md"
        if not chunk_file.exists():
            raise typer.BadParameter(f"Missing chunk file {chunk_file}")
        text, metadata = _read_markdown_payload(chunk_file)
        chunk = SuperChunk(
            id=entry["id"],
            profile=metadata.get("profile", profile.name),
            chapter_ids=metadata.get("chapter_ids", entry.get("chapter_ids", [])),
            text=text,
            est_tokens=entry.get("est_tokens") or metadata.get("est_tokens", 0),
            meta=metadata.get("meta", {}),
        )
        chunks.append(chunk)
    return chunks


def _build_selection(
    select_path: Optional[Path],
    skip_front: bool,
    skip_parts: bool,
    skip_back: bool,
    from_spec: Optional[str],
    to_spec: Optional[str],
    include_regex: Optional[str],
    exclude_regex: Optional[str],
    only_ids: Optional[str],
    only_slugs: Optional[str],
) -> Selection:
    def _split_csv(value: Optional[str]) -> list[str] | None:
        if not value:
            return None
        parts = [segment.strip() for segment in re.split(r"[,\s]+", value) if segment.strip()]
        return parts or None

    sel = Selection(
        skip_front=skip_front,
        skip_parts=skip_parts,
        skip_back=skip_back,
        from_spec=from_spec,
        to_spec=to_spec,
        include_regex=include_regex,
        exclude_regex=exclude_regex,
        only_ids=_split_csv(only_ids),
        only_slugs=_split_csv(only_slugs),
    )

    if select_path:
        file_sel = load_selection_file(select_path)
        sel = Selection(
            skip_front=sel.skip_front or file_sel.skip_front,
            skip_parts=sel.skip_parts or file_sel.skip_parts,
            skip_back=sel.skip_back or file_sel.skip_back,
            from_spec=sel.from_spec or file_sel.from_spec,
            to_spec=sel.to_spec or file_sel.to_spec,
            include_regex=sel.include_regex or file_sel.include_regex,
            exclude_regex=sel.exclude_regex or file_sel.exclude_regex,
            only_ids=sel.only_ids or file_sel.only_ids,
            only_slugs=sel.only_slugs or file_sel.only_slugs,
        )

    return sel



def _read_markdown_payload(
    path: Path,
    *,
    fallback_meta: dict[str, object] | None = None,
) -> tuple[str, dict[str, object]]:
    content = path.read_text(encoding="utf-8")
    if content.startswith("---\n"):
        end = content.find("\n---", 4)
        if end != -1:
            json_payload = content[4:end].strip()
            remainder = content[end + 4 :].lstrip("\n")
            try:
                metadata = json.loads(json_payload)
            except json.JSONDecodeError:
                metadata = fallback_meta.copy() if fallback_meta else {}
            return remainder.rstrip("\n"), metadata or (fallback_meta.copy() if fallback_meta else {})
    return content.rstrip("\n"), fallback_meta.copy() if fallback_meta else {}


if __name__ == "__main__":  # pragma: no cover
    app()
