#!/usr/bin/env bash
set -euo pipefail

uv run pytest -q
uv run binddrift --help >/dev/null
test -s paper/draft.md
test -s data/replay/latest/warnings.md
test -s paper/tables/evaluation_summary.json
uv run python -m binddrift.artifact validate --strict-ccfb --stage final >/dev/null
