#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: export_project_md.sh [output_path]

Creates a markdown file that concatenates project source files.
Set INCLUDE_EXTS (comma list) or INCLUDE_NAMES (comma list) to widen coverage.
Output files default to scripts/outputs/ within the project.
USAGE
}

for arg in "$@"; do
  if [[ "$arg" == "-h" || "$arg" == "--help" ]]; then
    usage
    exit 0
  fi
  break
done

if git_root=$(git rev-parse --show-toplevel 2>/dev/null); then
  root="$git_root"
else
  root=$(pwd)
fi

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
outputs_dir="$script_dir/outputs"

output_name="${1:-project_export.md}"
if [[ "$output_name" == /* ]]; then
  output_path="$output_name"
else
  output_path="$outputs_dir/$output_name"
fi

mkdir -p "$(dirname "$output_path")"
if [[ "$output_path" == "$root"/* ]]; then
  output_rel="${output_path#$root/}"
else
  output_rel=""
fi

if git -C "$root" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  mapfile -t files < <(cd "$root" && git ls-files)
else
  mapfile -t files < <(find "$root" -type f ! -path '*/.git/*')
  for i in "${!files[@]}"; do
    files[$i]="${files[$i]#$root/}"
  done
fi

IFS=',' read -r -a include_exts <<< "${INCLUDE_EXTS:-py,pyi,pyx,pxd,pxi,toml,json,yaml,yml,cfg,ini,txt,sh,rs,js,ts,tsx,jsx,env}"
IFS=',' read -r -a include_names <<< "${INCLUDE_NAMES:-Makefile,Dockerfile}"

exclude_globs=(
  "*/__pycache__/*"
  "*.pyc"
  "*.pyo"
  "*.log"
  "*.md"
  "*.rst"
  "*.png"
  "*.jpg"
  "*.jpeg"
  "*.gif"
  "*.svg"
  "*.ico"
  "*.pdf"
  "*.zip"
  "*.tar"
  "*.gz"
  "*.egg-info/*"
  ".venv/*"
  "*/.venv/*"
  "venv/*"
  "*/venv/*"
  ".mypy_cache/*"
  "*/.mypy_cache/*"
  ".pytest_cache/*"
  "*/.pytest_cache/*"
  ".ruff_cache/*"
  "*/.ruff_cache/*"
  "node_modules/*"
  "*/node_modules/*"
  ".idea/*"
  "*/.idea/*"
  ".vscode/*"
  "*/.vscode/*"
  "data/*"
  "*/data/*"
  "build/*"
  "*/build/*"
  "dist/*"
  "*/dist/*"
)

should_skip() {
  local file="$1"
  if [[ -n "$output_rel" && "$file" == "$output_rel" ]]; then
    return 0
  fi
  for glob in "${exclude_globs[@]}"; do
    [[ $file == $glob ]] && return 0
  done
  return 1
}

matches_name_list() {
  local file="$1"
  for name in "${include_names[@]}"; do
    [[ -z "$name" ]] && continue
    [[ "$file" == "$name" ]] && return 0
  done
  return 1
}

should_include() {
  local file="$1"
  local base ext
  if should_skip "$file"; then
    return 1
  fi
  base=${file##*/}
  if matches_name_list "$base"; then
    return 0
  fi
  if [[ "$file" != *.* ]]; then
    return 1
  fi
  ext=${file##*.}
  ext=${ext,,}
  for candidate in "${include_exts[@]}"; do
    [[ -z "$candidate" ]] && continue
    if [[ "$ext" == "$candidate" ]]; then
      return 0
    fi
  done
  return 1
}

lang_for() {
  local file="$1" ext
  ext=${file##*.}
  ext=${ext,,}
  case "$ext" in
    py) printf 'python' ;;
    toml) printf 'toml' ;;
    json) printf 'json' ;;
    yaml|yml) printf 'yaml' ;;
    sh) printf 'bash' ;;
    cfg|ini) printf 'ini' ;;
    rs) printf 'rust' ;;
    js) printf 'javascript' ;;
    ts) printf 'typescript' ;;
    tsx) printf 'tsx' ;;
    jsx) printf 'jsx' ;;
    env) printf 'sh' ;;
    *) printf 'text' ;;
  esac
}

mapfile -t filtered < <(
  for file in "${files[@]}"; do
    [[ -z "$file" ]] && continue
    if should_include "$file"; then
      printf '%s\n' "$file"
    fi
  done | sort
)

{
  printf '# Combined Project Snapshot: %s\n\n' "$(basename "$root")"
  printf '_Generated on %s_\n\n' "$(date -Iseconds)"
  for file in "${filtered[@]}"; do
    [[ -z "$file" ]] && continue
    lang=$(lang_for "$file")
    printf '## %s\n\n' "$file"
    printf '```%s\n' "$lang"
    cat "$root/$file"
    printf '\n```\n\n'
  done
} > "$output_path"

echo "Wrote $((${#filtered[@]})) files to $output_path"
