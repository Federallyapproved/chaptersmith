import logging
from pathlib import Path
from typing import Callable

from ebooklib import epub

from chaptersmith.ingest_epub import ingest_epub
from chaptersmith.normalize import paragraphs, to_markdown


def _write_epub(tmp_path: Path, mutate: Callable[[epub.EpubBook], None]) -> Path:
    book = epub.EpubBook()
    book.set_identifier("book-123")
    book.set_title("A Sample Book")
    book.set_language("en")
    book.add_author("Author Name")

    nav = epub.EpubNav()
    book.add_item(nav)
    book.add_item(epub.EpubNcx())

    mutate(book)

    output_path = tmp_path / "sample.epub"
    epub.write_epub(str(output_path), book)
    return output_path


def test_to_markdown_strips_scripts_and_formats_headings() -> None:
    html = """
    <html>
      <head><title>Ignored</title><script>console.log('skip');</script></head>
      <body>
        <h1>The Title</h1>
        <p>First paragraph with <strong>emphasis</strong>.</p>
        <ul><li>Point one</li><li>Point two</li></ul>
        <script>alert('nope');</script>
      </body>
    </html>
    """

    markdown = to_markdown(html, is_html=True)
    assert markdown.startswith("# The Title")
    assert "alert" not in markdown
    para_list = paragraphs(markdown)
    assert para_list[0] == "# The Title"
    assert "Point one" in para_list[-1]


def test_to_markdown_passthrough_for_text() -> None:
    text = "Line one\r\n\r\nLine two\n\nLine three"
    markdown = to_markdown(text, is_html=False)
    assert "\r" not in markdown
    assert "Line three" in markdown


def test_ingest_epub_builds_chapters_with_front_and_back(tmp_path) -> None:
    def _builder(book: epub.EpubBook) -> None:
        front = epub.EpubHtml(title="Prelude", file_name="front.xhtml", lang="en")
        front.content = "<p>Preface text.</p>"

        ch1 = epub.EpubHtml(title="Chapter One", file_name="ch1.xhtml", lang="en")
        ch1.content = "<h1 id='ch1'>Chapter One</h1><p>First chapter body.</p>"

        ch2 = epub.EpubHtml(title="Chapter Two", file_name="ch2.xhtml", lang="en")
        ch2.content = "<h1 id='ch2'>Chapter Two</h1><p>Second chapter body.</p>"

        back = epub.EpubHtml(title="Appendix", file_name="back.xhtml", lang="en")
        back.content = "<p>Appendix details.</p>"

        for item in (front, ch1, ch2, back):
            book.add_item(item)

        book.spine = ["nav", front, ch1, ch2, back]
        book.toc = (
            epub.Link("ch1.xhtml#ch1", "Chapter One", "ch1"),
            epub.Link("ch2.xhtml#ch2", "Chapter Two", "ch2"),
        )

    epub_path = _write_epub(tmp_path, _builder)
    result = ingest_epub(epub_path)

    assert result.title == "A Sample Book"
    assert len(result.chapters) == 4
    assert result.chapters[0].title == "Front Matter"
    assert result.chapters[0].meta.get("gray_zone") is True
    assert result.chapters[1].source["anchor"] == "ch1"
    assert result.chapters[1].est_tokens and result.chapters[1].est_tokens > 0
    assert result.chapters[-1].title == "Back Matter"


def test_ingest_epub_marks_missing_anchor(tmp_path, caplog) -> None:
    def _builder(book: epub.EpubBook) -> None:
        ch1 = epub.EpubHtml(title="Chapter One", file_name="c1.xhtml", lang="en")
        ch1.content = "<h1 id='c1'>Chapter One</h1><p>First.</p>"

        ch2 = epub.EpubHtml(title="Chapter Two", file_name="c2.xhtml", lang="en")
        ch2.content = "<h1>Chapter Two</h1><p>Second.</p>"

        for item in (ch1, ch2):
            book.add_item(item)

        book.spine = ["nav", ch1, ch2]
        book.toc = (
            epub.Link("c1.xhtml#c1", "Chapter One", "c1"),
            epub.Link("c2.xhtml#missing", "Chapter Two", "c2"),
        )

    epub_path = _write_epub(tmp_path, _builder)

    with caplog.at_level(logging.WARNING):
        result = ingest_epub(epub_path)

    assert any("Missing anchor" in record.getMessage() for record in caplog.records)
    assert result.chapters[1].meta.get("gray_zone") is True
    assert "warnings" in result.meta
