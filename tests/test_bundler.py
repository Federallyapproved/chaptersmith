import json
from pathlib import Path

import pytest

from chaptersmith.chapter_bundler import bundle_book, validate_superchunks
from chaptersmith.models import Book, Chapter, SuperChunk
from chaptersmith.profiles import ModelProfile
from chaptersmith.tokenize_count import (
    cap_to_budget,
    count_gemini_tokens_via_api,
    count_gpt5_tokens,
    estimate_gemini_tokens,
)


def _chapter(idx: int, text: str, order: int, tokens: int | None = None) -> Chapter:
    return Chapter(
        id=f"ch-{idx:02d}",
        title=f"Chapter {idx}",
        text=text,
        order=order,
        est_tokens=tokens,
        source={"href": f"ch-{idx}.xhtml", "anchor": None},
    )


def _profile() -> ModelProfile:
    return ModelProfile(
        name="test-profile",
        input_limit=200,
        output_limit=64,
        safe_input_budget=60,
        overlap_tokens=5,
    )


def test_bundle_book_groups_chapters_and_writes_files(tmp_path) -> None:
    profile = _profile()
    chapters = [
        _chapter(1, "Alpha text block", order=1, tokens=20),
        _chapter(2, "Beta text block", order=2, tokens=18),
    ]
    book = Book(
        id="book-1",
        title="Book One",
        author="Author",
        source_format="md",
        chapters=chapters,
        meta={},
    )

    output_dir = tmp_path / "output"
    standard, oversized = bundle_book(
        book,
        profile,
        tokenizer=lambda text: len(text.split()),
        output_dir=output_dir,
    )

    assert len(standard) == 1
    assert not oversized
    chunk = standard[0]
    assert chunk.chapter_ids == ["ch-01", "ch-02"]
    assert "# [Chapter 1 — Chapter 1]" in chunk.text

    index_path = output_dir / profile.name / "index.json"
    assert index_path.exists()
    data = json.loads(index_path.read_text(encoding="utf-8"))
    assert data["book_id"] == "book-1"
    assert data["chunks"][0]["id"] == chunk.id

    markdown_path = output_dir / profile.name / f"{chunk.id}.md"
    assert markdown_path.exists()
    markdown_content = markdown_path.read_text(encoding="utf-8")
    assert "---" in markdown_content.splitlines()[0]


def test_bundle_book_splits_oversized_chapter(tmp_path) -> None:
    profile = _profile()
    large_text = "\n\n".join(f"Paragraph {i}" for i in range(20))
    chapter = _chapter(1, large_text, order=1, tokens=None)
    book = Book(
        id="book-big",
        title="Oversized",
        author="Author",
        source_format="md",
        chapters=[chapter],
        meta={},
    )

    tokenizer = lambda text: len(text.split())
    standard, oversized = bundle_book(
        book,
        profile,
        tokenizer=tokenizer,
        output_dir=tmp_path,
    )

    assert not standard
    assert len(oversized) >= 2
    assert oversized[0].id.startswith("ch-01__")
    assert "Paragraph 0" in oversized[0].text
    assert oversized[1].meta["source_chapter"] == "ch-01"


def test_validate_superchunks_detects_over_budget() -> None:
    profile = _profile()
    chunk = SuperChunk(
        id="chunk-1",
        profile=profile.name,
        chapter_ids=["ch-01"],
        text="word " * 100,
        est_tokens=0,
        meta={},
    )

    with pytest.raises(ValueError):
        validate_superchunks([chunk], profile, tokenizer=lambda text: len(text.split()))


def test_count_gpt5_tokens_simple_phrase() -> None:
    assert count_gpt5_tokens("Hello world") == 2


def test_estimate_gemini_tokens_rounding() -> None:
    text = "abcd" * 5  # 20 characters -> ceil(20/4) == 5
    assert estimate_gemini_tokens(text) == 5
    assert estimate_gemini_tokens("") == 0


def test_cap_to_budget_uses_tokenizer() -> None:
    def fake_tokenizer(val: str) -> int:
        return len(val.split())

    count, fits = cap_to_budget("one two three", 4, fake_tokenizer)
    assert count == 3
    assert fits is True
    assert cap_to_budget("one two three four", 3, fake_tokenizer)[1] is False


def test_count_gemini_tokens_via_api_is_stub() -> None:
    with pytest.raises(NotImplementedError):
        count_gemini_tokens_via_api("sample text")
