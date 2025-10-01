# Chaptersmith

Tools for normalizing, tokenizing, selecting, and bundling book chapters for LLM workflows.

## Installation

```bash
pip install -e .
Split an EPUB into normalized chapter markdown:
chaptersmith split mybook.epub -f epub
# Output in: data/<slug-of-book-title>/
# A short stats summary prints after the split.
Bundle for a model profile:
chaptersmith bundle data/<slug> --profile gpt-pro-fast
Validate chunks against the chosen profile:
chaptersmith validate data/<slug> --profile gpt-pro-fast
Export selected chapters to a single Markdown:
chaptersmith export data/<slug> --from "Chapter 3" --to "Chapter 8" --join join/chapters.md --print-total
```
Commands & Options
split
chaptersmith split [INPUT] --format {epub|html|md} [--out DIR]
                   [--book-id STR] [--title STR] [--author STR]
                   [--skip-kinds KIND ...]
                   [--start-title TEXT] [--end-title TEXT]
INPUT: Path to the source book file (EPUB/HTML/MD).

--format / -f: Source format: epub | html | md.
(FB2 is not implemented yet.)

--out: Output directory (default data/<slug-of-book-title>).

--skip-kinds: Repeatable; omit structural pages. Examples:
cover, title-page, contents, acknowledgments, part-cover,
appendix, notes, bibliography, index.

--start-title / --end-title: Fence the range by title substring (case-insensitive).

What it writes

book/manifest.json — metadata

chapters/*.md — one file per chapter (prunes stale files each run)

chapters_index.json — index of chapter metadata

Post‑split stats
After every split, Chaptersmith prints:

Chapters written

Total tokens (o200k)

Estimated super-chunks by profile

bundle
chaptersmith bundle OUTDIR --profile PROFILE
                          [--select selection.yaml]
                          [--skip-front] [--skip-parts] [--skip-back]
                          [--from SPEC] [--to SPEC]
                          [--include-regex RX] [--exclude-regex RX]
                          [--only-ids LIST] [--only-slugs LIST]
PROFILE: One of the names in profiles.py (e.g., gpt-pro-fast, gpt5-api, chatgpt-paste-safe, gemini-2.5-pro).

Selection can be provided via flags or a YAML/JSON file (--select).
SPEC may match by id, slug, exact title, or order number.

validate
chaptersmith validate OUTDIR --profile PROFILE
Ensures all super-chunks in OUTDIR/superchunks/PROFILE/ are within budget.

stats
chaptersmith stats OUTDIR [--skip-kinds KIND ...]
                          [--start-title TEXT] [--end-title TEXT]
Prints a table with per-chapter token counts, totals, and estimated super-chunks.

export
chaptersmith export OUTDIR [--select selection.yaml]
                           [--skip-front] [--skip-parts] [--skip-back]
                           [--from SPEC] [--to SPEC]
                           [--include-regex RX] [--exclude-regex RX]
                           [--only-ids LIST] [--only-slugs LIST]
                           [--join PATH] [--print-total]
-join writes a single Markdown containing the chosen chapters
(relative to OUTDIR if not absolute).

LIST for --only-* can be comma or whitespace separated.

Selection File Schema (YAML/JSON)
skip_front: true
skip_parts: true
skip_back: false
from: "chapter-03"   # id | slug | title | order number
to: "chapter-12"
include: "security|crypto"    # regex
exclude: "appendix|index"
only_ids: ["chapter-03", "chapter-07"]     # optional whitelist
only_slugs: ["introduction", "threat-models"]

---

## What you’ll see after `split`

With the patch, the end of a `split` run looks like:
Wrote chapters to data/my-book
Split Summary

Chapters written: 27

Total tokens (o200k): 183457

Estimated super-chunks by profile:
• gpt-pro-fast: ~2
• gpt-pro-thinking: ~2
• gpt5-api: ~1
• chatgpt-paste-safe: ~2
• gemini-2.5-pro: ~1

---

## Notes

- This keeps `ingest_fb2.py` in the codebase as a stub, but the CLI no longer advertises `fb2` as an accepted `--format`.
- The stats printed by `split` reuse the same token counter used throughout (o200k / `count_gpt5_tokens`) and mirror the `stats` command’s “Estimated super-chunks” logic—just in a compact summary.

If you want an even richer post-split summary (e.g., show the top 5 largest chapters or a mini table), I can wire that in too.
