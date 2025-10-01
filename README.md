# Chaptersmith

Tools for splitting books/documents into normalized Markdown chapters, estimating token usage, and greedily bundling chapters into **LLM‑sized “super‑chunks”** tailored to model profiles (GPT Pro, GPT‑5 API, Gemini 2.5 Pro). Comes with a clean CLI, selection filters, stats, and export helpers.

---

## How to run it (CLI) — with **all options**

> Requires **Python 3.11+**. Install:
>
> ```bash
> # from the repo root
> pip install -e .
> # or with uv/pipx if you prefer
> ```

### Command overview

* `chaptersmith split` — Ingest *epub / html / md* into normalized chapter Markdown.
* `chaptersmith bundle` — Pack chapters into super‑chunks for a chosen model profile.
* `chaptersmith validate` — Ensure all super‑chunks fit the chosen profile budget.
* `chaptersmith stats` — Show per‑chapter token counts and estimated chunk counts.
* `chaptersmith export` — Export a selected subset; optionally join to one Markdown file.

There are also two utility scripts:

* `scripts/combine_mybooks.sh` — Concatenate a Chaptersmith book folder into one LLM‑ready Markdown bundle.
* `scripts/export_project_md.sh` — Export this project’s source files as a single Markdown document.

---

### `chaptersmith split` — options

> **Purpose:** Split a source file into normalized chapters and write them to an output directory.

```bash
chaptersmith split INPUT_PATH --format {epub|html|md|fb2} [OPTIONS]
```

**Positional:**

* `INPUT_PATH` – Path to the source book.

**Required:**

* `-f, --format {epub|html|md|fb2}` – Source format.
  ⚠️ **Note:** `fb2` ingestion is *not implemented yet* (you’ll get an error).

**Common options:**

* `--out PATH` – Output directory (default: a slug of the book title).
* `--book-id TEXT` – Override book identifier.
* `--title TEXT` – Override book title.
* `--author TEXT` – Override book author.

**Selective slicing (during split):**

* `--skip-kinds KIND ...` *(repeatable)* – Omit kinds (e.g. `--skip-kinds cover --skip-kinds title-page --skip-kinds part-cover`).
* `--start-title TEXT` – Start from the first chapter whose title contains this text (case‑insensitive).
* `--end-title TEXT` – End **after** the first chapter whose title contains this text (case‑insensitive).

> **Chapter “kind” values** are auto‑classified (e.g., `cover`, `title-page`, `copyright`,
> `dedication`, `contents`, `acknowledgments`, `preface`, `part-cover`,
> `appendix`, `notes`, `bibliography`, `index`, or `chapter`).

---

### `chaptersmith bundle` — options

> **Purpose:** Greedily pack (and, if necessary, split) chapters into super‑chunks sized for a model profile. Writes Markdown artifacts with JSON front‑matter.

```bash
chaptersmith bundle OUTDIR --profile PROFILE [OPTIONS]
```

**Positional:**

* `OUTDIR` – Directory containing book manifest and chapters (i.e., the output of `split`).

**Required:**

* `--profile {gpt-pro-fast|gpt-pro-thinking|gpt5-api|gemini-2.5-pro}` – Target profile.

**Optional selection (applied at bundle time):**

* `--select PATH` – Selection file (YAML/JSON; see examples below).
* `--skip-front` – Skip front matter.
* `--skip-parts` – Skip “Part …” pages.
* `--skip-back` – Skip back matter.
* `--from TEXT` – Start chapter (match by **id/slug/title/order**).
* `--to TEXT` – End chapter (match by **id/slug/title/order**).
* `--include-regex REGEX` – Include chapters whose **title or slug** matches.
* `--exclude-regex REGEX` – Exclude chapters whose **title or slug** matches.
* `--only-ids CSV` – Only include specific chapter IDs (comma‑separated).
* `--only-slugs CSV` – Only include specific chapter slugs (comma‑separated).

---

### `chaptersmith validate` — options

> **Purpose:** Verify all previously written super‑chunks fit within the chosen profile budget.

```bash
chaptersmith validate OUTDIR --profile PROFILE
```

* `OUTDIR` – Directory containing bundled super‑chunks.
* `--profile` – One of: `gpt-pro-fast`, `gpt-pro-thinking`, `gpt5-api`, `gemini-2.5-pro`.

---

### `chaptersmith stats` — options

> **Purpose:** Show per‑chapter token counts and totals, plus a rough estimate of super‑chunk counts per profile.

```bash
chaptersmith stats OUTDIR [OPTIONS]
```

* `OUTDIR` – Directory with chapters and manifest (the output of `split`).

**Optional selection (for the subtotal):**

* `--skip-kinds KIND ...` *(repeatable)*
* `--start-title TEXT`
* `--end-title TEXT`

---

### `chaptersmith export` — options

> **Purpose:** Export a selected subset of chapters; optionally produce one joined Markdown file.

```bash
chaptersmith export OUTDIR [OPTIONS]
```

* `OUTDIR` – Directory with chapters and manifest.

**Selection options (same semantics as `bundle`):**

* `--select PATH`
* `--skip-front`
* `--skip-parts`
* `--skip-back`
* `--from TEXT`
* `--to TEXT`
* `--include-regex REGEX`
* `--exclude-regex REGEX`
* `--only-ids CSV`
* `--only-slugs CSV`

**Output controls:**

* `--join PATH` – Write a single joined Markdown file to this path.
* `--print-total` – Print total tokens for the selected set.

---

### Utility scripts

#### `scripts/combine_mybooks.sh`

```bash
Usage: combine_mybooks.sh [book_dir] [output_path|-]
# Combines manifests and chapter markdown into one LLM-friendly Markdown bundle.

# Examples
scripts/combine_mybooks.sh mybook                 # -> scripts/outputs/mybook-llm_bundle.md
scripts/combine_mybooks.sh mybook -               # -> stdout
scripts/combine_mybooks.sh mybook /tmp/bundle.md  # -> absolute path
scripts/combine_mybooks.sh mybook bundle.md       # -> scripts/outputs/bundle.md
```

#### `scripts/export_project_md.sh`

```bash
Usage: export_project_md.sh [output_path]
# Concatenate project source files into one Markdown file (defaults: scripts/outputs/project_export.md).

# Environment variables:
#   INCLUDE_EXTS  (comma list; default covers py, toml, json, yaml/yml, sh, rs, js/ts/tsx/jsx, cfg/ini, txt, env)
#   INCLUDE_NAMES (comma list; defaults: Makefile,Dockerfile)

# Example
INCLUDE_EXTS=py,sh,toml scripts/export_project_md.sh docs/project.md  # -> scripts/outputs/docs/project.md
```

---

## Quickstart

```bash
# 1) Split a book into chapters
chaptersmith split ./example.epub -f epub --out ./mybook

# 2) Bundle for GPT Pro (fast)
chaptersmith bundle ./mybook --profile gpt-pro-fast

# 3) Validate budgets
chaptersmith validate ./mybook --profile gpt-pro-fast

# 4) Get token stats (and a rough chunk estimate per profile)
chaptersmith stats ./mybook

# 5) Export a subset as one joined Markdown
chaptersmith export ./mybook --skip-front --skip-back --join ./mybook/novel_only.md --print-total

# 6) Produce an LLM bundle with manifests + chapters for copy/paste
scripts/combine_mybooks.sh ./mybook
```

---

## Features

* **Robust ingestion**

  * **EPUB**: Parses EPUB 3 nav or EPUB 2 NCX; falls back to library ToC; collects front/back matter if it’s not in ToC; slices between ToC anchors; enriches chapter titles from in‑document headings; flags “gray‑zone” chapters when anchors are missing.
  * **HTML / Markdown**: Splits on headings; normalizes text/HTML into compact Markdown; flags heading level anomalies.
  * **FB2**: Command surface exists but ingestion is **not implemented**.

* **Normalization**

  * Converts HTML to concise Markdown (headings, lists, blockquotes, code blocks).
  * Scrubs scripts/styles, normalizes whitespace, and splits into logical paragraphs.

* **Token budgeting**

  * Uses OpenAI `tiktoken` **o200k_base** (`count_gpt5_tokens`) for accurate token counts.
  * Provides a simple Gemini estimator (length/4) for convenience.

* **Bundling algorithm**

  * Greedy packing of chapters into **super‑chunks** with configurable **overlap**.
  * Oversized chapters are auto‑split by paragraphs to stay within the profile budget, with backward overlap for continuity.

* **Profiles (budgets & overlap)**

  | Profile            | Safe Input Budget | Output Limit | Overlap |
  | ------------------ | ----------------: | -----------: | ------: |
  | `gpt-pro-fast`     |           100,000 |       16,384 |     200 |
  | `gpt-pro-thinking` |           150,000 |       16,384 |     200 |
  | `gpt5-api`         |           240,000 |      128,000 |     200 |
  | `gemini-2.5-pro`   |           950,000 |       65,536 |     300 |

---

## Installation & requirements

* **Python**: 3.11+
* **Dependencies**: `ebooklib`, `beautifulsoup4`, `lxml`, `markdown-it-py`, `tiktoken`, `typer[all]`, `rich`, `chardet`, `PyYAML`.
* Install for development:

```bash
pip install -e .
# Optional: dev tools
pip install -e ".[dev]"   # if you add a dev extra, otherwise:
pip install pytest pytest-cov ruff mypy types-beautifulsoup4 types-chardet
```

> If `lxml` wheels aren’t available on your platform, you may need system build tools and libxml2/libxslt dev packages.

---

## What gets written where?

After **split** (`--out ./mybook`), you’ll have:

```
mybook/
  book/manifest.json
  chapters_index.json
  chapters/
    <slug>.md   # JSON front matter + Markdown body
```

Each `chapters/*.md` file begins with JSON front‑matter:

```json
{
  "id": "...",
  "title": "...",
  "order": 1,
  "source": {"href": "...", "anchor": "..."},
  "est_tokens": 1234,
  "meta": {"kind": "chapter", "filename": "slug.md"}
}
```

After **bundle**, the tool writes super‑chunks with JSON front matter and a Markdown body, plus an index.

**Intended layout:**

```
mybook/
  superchunks/
    <profile>/
      index.json
      <chunk-id>.md
```

> **Known inconsistency (current snapshot):**
> The bundler helper writes to `(<output_dir or .>)/<profile>/…`, while the validator and CLI discovery expect `OUTDIR/superchunks/<profile>/…`.
> Workarounds:
>
> * Create `mybook/superchunks/` yourself and **bundle into that path**, e.g. point `OUTDIR` to `mybook/superchunks` when calling the lower‑level API; or
> * Move the generated `<profile>/` folder under `mybook/superchunks/`.
>
> Suggested code fix (in `chapter_bundler._write_superchunks`):
>
> ```python
> base_dir = (output_dir or Path(".")) / "superchunks"
> profile_dir = base_dir / profile.name
> ```
>
> The CLI tests already expect `mybook/superchunks/<profile>/…`.

---

## Selection files (YAML/JSON)

You can pass `--select path/to/selection.(yaml|json)` to `bundle` or `export`. Keys:

```yaml
# booleans
skip_front: true
skip_parts: true
skip_back: false

# windowing (match by id/slug/title/order)
from: "chapter-03"
to: "chapter-17"

# regex filters (match title or slug; case-insensitive)
include: "appendix|notes"
exclude: "index"

# explicit lists
only_ids: ["ch-01", "ch-02"]
only_slugs: ["introduction", "methods"]
```

Notes:

* Windowing (`from`/`to`) applies **before** inclusive filters.
* `only_ids` / `only_slugs` narrow the set before other filters.
* `--include-regex` and `--exclude-regex` operate on **title or slug**.

---

## Programmatic use (Python)

```python
from pathlib import Path
from chaptersmith.ingest_epub import ingest_epub
from chaptersmith.chapter_bundler import bundle_book, validate_superchunks
from chaptersmith.profiles import gpt_pro_chat_fast
from chaptersmith.tokenize_count import count_gpt5_tokens

# 1) Ingest
book = ingest_epub(Path("example.epub"))

# 2) Bundle
standard, oversized = bundle_book(
    book,
    gpt_pro_chat_fast,
    tokenizer=count_gpt5_tokens,
    output_dir=Path("mybook") / "superchunks",  # see known inconsistency note
)

# 3) Validate
validate_superchunks(standard + oversized, gpt_pro_chat_fast, tokenizer=count_gpt5_tokens)
```

---

## How it works (high level)

* **Normalization** (`normalize.py`)

  * HTML → Markdown via block‑level traversal (headings, lists, quotes, code).
  * Cleans whitespace, collapses runs of newlines, fixes hyphenated line breaks.
  * `paragraphs()` splits on blank lines — used when splitting oversized chapters.

* **EPUB ingest** (`ingest_epub.py`)

  * Builds ToC from EPUB3 `nav`, then EPUB2 `ncx`, then library fallback.
  * Collects front/back matter not referenced by ToC.
  * Slices content from current ToC anchor to the next (across files when needed).
  * Enriches titles by reading the heading cluster near the start anchor.
  * Flags `meta.gray_zone = true` when anchors are missing or slicing is approximate.

* **HTML/MD ingest** (`ingest_html_md.py`)

  * Splits by heading levels (`h1` preferred, falls back to `h2` or first heading found).
  * Flags heading level anomalies with `meta.gray_zone = true`.

* **Bundling** (`chapter_bundler.py`)

  * Greedy packing by `safe_input_budget` (profile‑specific).
  * If a single chapter exceeds the budget, it’s split into parts:

    * Segment paragraphs to hit ~90–100% of budget.
    * Add backward overlap from previous part up to `overlap_tokens`.
  * Chunk header syntax:

    * Whole chapter: `# [Chapter {order} — {title}]`
    * Part:         `# [Chapter {order} — {title} ({A|B|...})]`

* **Tokenization** (`tokenize_count.py`)

  * `count_gpt5_tokens`: OpenAI `o200k_base`.
  * `estimate_gemini_tokens`: characters/4 heuristic.
  * `count_gemini_tokens_via_api`: stub (not implemented here).

---

## Testing & quality

```bash
# run tests
pytest

# lint & format
ruff check .
ruff format .

# type checking
mypy chaptersmith tests
```

---

## Troubleshooting

* **“FB2 ingestion is not yet implemented.”**
  That format is a stub for now.

* **`lxml` install issues**
  Use prebuilt wheels if available; otherwise install OS build tooling and libxml2/libxslt dev packages.

* **Super‑chunk path mismatch**
  See the **Known inconsistency** note above.

---

## Roadmap

* Implement `ingest_fb2`.
* Expose a CLI flag to explicitly set super‑chunk output root (resolving the path inconsistency).
* Optional Gemini token counting via API.
* More ingestion heuristics for complex HTML/EPUB structures.

---

## License

**MIT** — see `pyproject.toml`.

---

## Acknowledgments

* Built on excellent libraries: `ebooklib`, `beautifulsoup4`, `lxml`, `tiktoken`, `typer`, `rich`.
