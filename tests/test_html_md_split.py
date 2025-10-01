import logging
from pathlib import Path

from chaptersmith.ingest_html_md import ingest_html, ingest_markdown
from chaptersmith.normalize import clean_text, paragraphs


def test_clean_text_normalizes_whitespace() -> None:
    raw = (
        "Hello\u00A0world!\r\n"
        "Line break\n\n\nTrailing  \n"
        "hyphen-\nated text"
    )
    cleaned = clean_text(raw)
    assert "\r" not in cleaned
    assert "\u00A0" not in cleaned
    assert "hyphenated text" in cleaned
    assert "\n\n\n" not in cleaned


def test_paragraphs_split_on_blank_lines() -> None:
    text = "Para one.\n\nPara two with more text.\n\n\nPara three."
    para_list = paragraphs(text)
    assert para_list == [
        "Para one.",
        "Para two with more text.",
        "Para three.",
    ]


def test_ingest_html_splits_on_headings(tmp_path) -> None:
    html = """
    <html><body>
    <h1 id="intro">Introduction</h1>
    <p>Welcome text.</p>
    <h1 id="chapter-1">Chapter One</h1>
    <p>Body content.</p>
    </body></html>
    """
    path = tmp_path / "sample.html"
    path.write_text(html, encoding="utf-8")

    book = ingest_html(path)
    assert book.source_format == "html"
    assert [c.title for c in book.chapters] == ["Introduction", "Chapter One"]
    assert book.chapters[0].source["anchor"] == "intro"


def test_ingest_markdown_uses_hash_headings(tmp_path) -> None:
    md = """# Alpha\nFirst block.\n\n# Beta\nSecond block."""
    path = tmp_path / "sample.md"
    path.write_text(md, encoding="utf-8")

    book = ingest_markdown(path)
    assert len(book.chapters) == 2
    assert book.chapters[0].title == "Alpha"
    assert book.chapters[1].source["anchor"] == "beta"
    assert all(chapter.est_tokens for chapter in book.chapters)


def test_ingest_html_marks_heading_anomaly(tmp_path, caplog) -> None:
    html = """
    <html><body>
    <h3 id="odd">Odd Heading</h3>
    <p>Content.</p>
    </body></html>
    """
    path = tmp_path / "odd.html"
    path.write_text(html, encoding="utf-8")

    with caplog.at_level(logging.WARNING):
        book = ingest_html(path)

    assert book.chapters[0].meta.get("gray_zone") is True
    assert book.meta.get("warnings")
