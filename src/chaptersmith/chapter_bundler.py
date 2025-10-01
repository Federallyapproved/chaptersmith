"""Utilities for grouping chapters into model-sized chunks."""

from __future__ import annotations

import json
import string
from pathlib import Path
from typing import Iterable

from .models import Book, Chapter, SuperChunk
from .normalize import paragraphs
from .profiles import ModelProfile
from .tokenize_count import TokenCounter, count_gpt5_tokens

_CHUNK_HEADER_TEMPLATE = "# [Chapter {order} — {title}]"
_PART_HEADER_TEMPLATE = "# [Chapter {order} — {title} ({label})]"


def bundle_book(
    book: Book,
    profile: ModelProfile,
    tokenizer: TokenCounter | None = None,
    *,
    output_dir: Path | None = None,
) -> tuple[list[SuperChunk], list[SuperChunk]]:
    """Greedily pack chapters into super-chunks for the given profile."""

    if tokenizer is None:
        tokenizer = count_gpt5_tokens

    ordered_chapters = sorted(book.chapters, key=lambda chapter: chapter.order)
    standard_chunks: list[SuperChunk] = []
    oversized_chunks: list[SuperChunk] = []

    chunk_index = 1
    buffer: list[Chapter] = []

    for chapter in ordered_chapters:
        chapter_tokens = _estimate_tokens(chapter, tokenizer)
        if chapter_tokens > profile.safe_input_budget:
            if buffer:
                standard_chunks.append(
                    _build_chunk(book, buffer, profile, tokenizer, chunk_index)
                )
                chunk_index += 1
                buffer = []
            oversized_chunks.extend(
                _split_oversized_chapter(chapter, profile, tokenizer)
            )
            continue

        projected_tokens = _buffer_tokens(buffer, profile, tokenizer) + chapter_tokens
        if buffer:
            projected_tokens += profile.overlap_tokens

        if buffer and projected_tokens > profile.safe_input_budget:
            standard_chunks.append(
                _build_chunk(book, buffer, profile, tokenizer, chunk_index)
            )
            chunk_index += 1
            buffer = []

        buffer.append(chapter)

    if buffer:
        standard_chunks.append(
            _build_chunk(book, buffer, profile, tokenizer, chunk_index)
        )

    _write_superchunks(book, profile, standard_chunks, oversized_chunks, output_dir)

    return standard_chunks, oversized_chunks


def validate_superchunks(
    superchunks: Iterable[SuperChunk],
    profile: ModelProfile,
    tokenizer: TokenCounter | None = None,
) -> None:
    """Validate that all super-chunks stay within the profile budget."""

    if tokenizer is None:
        tokenizer = count_gpt5_tokens

    for chunk in superchunks:
        tokens = tokenizer(chunk.text)
        if tokens > profile.safe_input_budget:
            raise ValueError(
                f"SuperChunk '{chunk.id}' exceeds budget: {tokens} > {profile.safe_input_budget}"
            )


def _estimate_tokens(chapter: Chapter, tokenizer: TokenCounter) -> int:
    if chapter.est_tokens is not None:
        return chapter.est_tokens
    return tokenizer(chapter.text)


def _buffer_tokens(buffer: list[Chapter], profile: ModelProfile, tokenizer: TokenCounter) -> int:
    if not buffer:
        return 0
    tokens = sum(_estimate_tokens(chapter, tokenizer) for chapter in buffer)
    overlaps = profile.overlap_tokens * max(len(buffer) - 1, 0)
    return tokens + overlaps


def _build_chunk(
    book: Book,
    chapters: list[Chapter],
    profile: ModelProfile,
    tokenizer: TokenCounter,
    index: int,
) -> SuperChunk:
    chunk_id = f"{book.id}-{profile.name}-chunk-{index:02d}"
    text = _compose_chunk_text(chapters)
    est_tokens = tokenizer(text)
    meta = {"chapter_count": len(chapters)}
    return SuperChunk(
        id=chunk_id,
        profile=profile.name,
        chapter_ids=[chapter.id for chapter in chapters],
        text=text,
        est_tokens=est_tokens,
        meta=meta,
    )


def _compose_chunk_text(chapters: list[Chapter]) -> str:
    parts: list[str] = []
    for position, chapter in enumerate(chapters):
        header = _CHUNK_HEADER_TEMPLATE.format(order=chapter.order, title=chapter.title)
        divider = "" if position == 0 else "\n\n---\n"
        parts.append(f"{divider}{header}\n\n{chapter.text}")
    return "".join(parts)


def _split_oversized_chapter(
    chapter: Chapter,
    profile: ModelProfile,
    tokenizer: TokenCounter,
) -> list[SuperChunk]:
    paras = paragraphs(chapter.text)
    if not paras:
        paras = [chapter.text]

    target = profile.safe_input_budget
    lower_bound = int(target * 0.9)

    # Determine paragraph ranges for each segment.
    segments: list[tuple[int, int]] = []
    start = 0
    while start < len(paras):
        tokens = 0
        end = start
        while end < len(paras):
            tokens += tokenizer(paras[end])
            end += 1
            if tokens >= lower_bound or tokens >= target:
                break
        if end == start:
            end += 1
        segments.append((start, min(end, len(paras))))
        start = end

    enriched_segments = _apply_overlap(paras, segments, profile, tokenizer)

    chunks: list[SuperChunk] = []
    for part_index, (start, end, text_block) in enumerate(enriched_segments):
        label = _part_label(part_index)
        chunk_id = f"{chapter.id}__{label}"
        header = _PART_HEADER_TEMPLATE.format(
            order=chapter.order,
            title=chapter.title,
            label=label,
        )
        text = f"{header}\n\n{text_block}"
        est_tokens = tokenizer(text)
        chunk = SuperChunk(
            id=chunk_id,
            profile=profile.name,
            chapter_ids=[chapter.id],
            text=text,
            est_tokens=est_tokens,
            meta={
                "source_chapter": chapter.id,
                "part_index": part_index,
                "segment_range": (start, end),
                "overlap_tokens": profile.overlap_tokens,
            },
        )
        chunks.append(chunk)
    return chunks


def _apply_overlap(
    paras: list[str],
    segments: list[tuple[int, int]],
    profile: ModelProfile,
    tokenizer: TokenCounter,
) -> list[tuple[int, int, str]]:
    enriched: list[tuple[int, int, str]] = []
    for idx, (start, end) in enumerate(segments):
        content = paras[start:end]
        if idx > 0:
            overlap_tokens = 0
            overlap: list[str] = []
            prev_start, prev_end = segments[idx - 1]
            pointer = prev_end - 1
            while pointer >= prev_start and overlap_tokens < profile.overlap_tokens:
                para = paras[pointer]
                overlap_tokens += tokenizer(para)
                overlap.insert(0, para)
                pointer -= 1
            if overlap:
                content = overlap + content
        enriched.append((start, end, "\n\n".join(content)))
    return enriched


def _write_superchunks(
    book: Book,
    profile: ModelProfile,
    standard: list[SuperChunk],
    oversized: list[SuperChunk],
    output_dir: Path | None,
) -> None:
    base_dir = output_dir or Path("superchunks")
    profile_dir = base_dir / profile.name
    profile_dir.mkdir(parents=True, exist_ok=True)

    all_chunks = [(chunk, "standard") for chunk in standard] + [
        (chunk, "oversized") for chunk in oversized
    ]

    index_entries = [
        {
            "id": chunk.id,
            "chapter_ids": chunk.chapter_ids,
            "est_tokens": chunk.est_tokens,
            "kind": kind,
        }
        for chunk, kind in all_chunks
    ]

    index_path = profile_dir / "index.json"
    index_path.write_text(
        json.dumps(
            {
                "book_id": book.id,
                "profile": profile.name,
                "chunks": index_entries,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    for chunk, kind in all_chunks:
        filename = profile_dir / f"{_safe_filename(chunk.id)}.md"
        front_matter = {
            "profile": profile.name,
            "book_id": book.id,
            "chapter_ids": chunk.chapter_ids,
            "est_tokens": chunk.est_tokens,
            "kind": kind,
            "meta": chunk.meta,
        }
        body = chunk.text.rstrip("\n")
        content = "\n".join(("---", json.dumps(front_matter, indent=2), "---", body))
        filename.write_text(content + "\n", encoding="utf-8")


def _safe_filename(name: str) -> str:
    return name.replace("/", "-").replace("\\", "-")


def _part_label(index: int) -> str:
    alphabet = string.ascii_uppercase
    if index < len(alphabet):
        return alphabet[index]

    label = ""
    base = len(alphabet)
    idx = index
    while idx >= 0:
        idx, remainder = divmod(idx, base)
        label = alphabet[remainder] + label
        idx -= 1
        if idx < 0:
            break
    return label


__all__ = ["bundle_book", "validate_superchunks"]
