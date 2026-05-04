#!/usr/bin/env bash
set -euo pipefail

uv run pytest -q
uv run binddrift --help >/dev/null
test -s paper/draft.md
test -s data/warnings.md
test -s paper/tables/evaluation_summary.json
