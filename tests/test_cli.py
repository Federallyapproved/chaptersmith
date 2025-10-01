from pathlib import Path

from typer.testing import CliRunner

from chaptersmith import cli


def _fake_tokenizer(text: str) -> int:
    return len(text.split())


def test_cli_flow_split_bundle_validate_stats(tmp_path, monkeypatch) -> None:
    html_content = """
    <html><body>
    <h1 id="intro">Intro</h1>
    <p>Alpha beta gamma.</p>
    <h1 id="chapter-1">Chapter One</h1>
    <p>Delta epsilon zeta.</p>
    </body></html>
    """
    source = tmp_path / "book.html"
    source.write_text(html_content, encoding="utf-8")

    outdir = tmp_path / "out"

    monkeypatch.setattr("chaptersmith.ingest_html_md.count_gpt5_tokens", _fake_tokenizer)
    monkeypatch.setattr("chaptersmith.chapter_bundler.count_gpt5_tokens", _fake_tokenizer)
    monkeypatch.setattr("chaptersmith.cli.count_gpt5_tokens", _fake_tokenizer)

    runner = CliRunner()

    result = runner.invoke(
        cli.app,
        [
            "split",
            str(source),
            "--format",
            "html",
            "--out",
            str(outdir),
        ],
        catch_exceptions=False,
    )
    assert result.exit_code == 0

    manifest = outdir / "book" / "manifest.json"
    chapters_index = outdir / "chapters_index.json"
    chapter_files = sorted((outdir / "chapters").glob("*.md"))

    assert manifest.exists()
    assert chapters_index.exists()
    assert len(chapter_files) == 2

    result = runner.invoke(
        cli.app,
        [
            "bundle",
            str(outdir),
            "--profile",
            "gpt-pro-fast",
        ],
        catch_exceptions=False,
    )
    assert result.exit_code == 0

    superchunk_dir = outdir / "superchunks" / "gpt-pro-fast"
    assert (superchunk_dir / "index.json").exists()
    assert list(superchunk_dir.glob("*.md"))

    result = runner.invoke(
        cli.app,
        [
            "validate",
            str(outdir),
            "--profile",
            "gpt-pro-fast",
        ],
        catch_exceptions=False,
    )
    assert result.exit_code == 0

    result = runner.invoke(
        cli.app,
        [
            "stats",
            str(outdir),
        ],
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    assert "Total tokens" in result.stdout
