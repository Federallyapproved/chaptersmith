#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: combine_mybooks.sh [book_dir] [output_path|-]

Combines book manifests and chapter markdown into a single markdown bundle
that is easy to paste into an LLM.

Arguments:
  book_dir       Directory containing the Chaptersmith output (default: mybook)
  output_path    Where to write the bundle. Use '-' for stdout.
                 If omitted, writes to scripts/outputs/<book>-llm_bundle.md.
USAGE
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

book_dir_input=${1:-mybook}
output_arg=${2:-}

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
outputs_dir="$script_dir/outputs"

if ! book_dir_abs=$(cd "$book_dir_input" 2>/dev/null && pwd); then
  printf 'error: %s is not a readable directory\n' "$book_dir_input" >&2
  exit 1
fi
book_dir="$book_dir_abs"

case "$output_arg" in
  "")
    book_slug=$(basename "$book_dir")
    output_path="$outputs_dir/${book_slug}-llm_bundle.md"
    ;;
  "-")
    output_path=""
    ;;
  /*)
    output_path="$output_arg"
    ;;
  *)
    output_path="$outputs_dir/$output_arg"
    ;;
esac

mapfile -t manifest_files < <(
  find "$book_dir" -type f \
    \( -name 'manifest.json' -o -name 'manifest-*.json' -o -name 'manifest_*.json' -o -name 'chapters_index.json' \) \
    -print | LC_ALL=C sort
)

chapters_md=""
if [[ -f "$book_dir/chapters.md" ]]; then
  chapters_md="$book_dir/chapters.md"
fi

mapfile -t chapter_files < <(
  find "$book_dir" -type f -path '*/chapters/*.md' -print | LC_ALL=C sort
)

render_bundle() {
  local title
  title=$(basename "$book_dir")
  printf '# Book Bundle: %s\n\n' "$title"

  if ((${#manifest_files[@]})); then
    printf '## Manifests\n\n'
    for manifest in "${manifest_files[@]}"; do
      local rel
      rel=${manifest#"$book_dir/"}
      printf '### %s\n\n```json\n' "$rel"
      cat "$manifest"
      printf '\n```\n\n'
    done
  else
    printf '_No manifest files found._\n\n'
  fi

  if [[ -n "$chapters_md" ]]; then
    local rel
    rel=${chapters_md#"$book_dir/"}
    printf '## Chapters (%s)\n\n' "$rel"
    cat "$chapters_md"
    printf '\n'
  elif ((${#chapter_files[@]})); then
    printf '## Chapters\n\n'
    for chapter in "${chapter_files[@]}"; do
      local rel
      rel=${chapter#"$book_dir/"}
      printf '### %s\n\n' "$rel"
      cat "$chapter"
      printf '\n'
    done
  else
    printf '_No chapter markdown found._\n'
  fi
}

write_bundle() {
  if [[ -n "$output_path" ]]; then
    mkdir -p "$(dirname "$output_path")"
    local tmp
    tmp=$(mktemp "${TMPDIR:-/tmp}/combine_mybooks.XXXXXX")
    trap 'rm -f "$tmp"' EXIT
    render_bundle >"$tmp"
    mv "$tmp" "$output_path"
    trap - EXIT
    printf 'Wrote bundle to %s\n' "$output_path" >&2
  else
    render_bundle
  fi
}

write_bundle
