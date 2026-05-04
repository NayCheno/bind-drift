#!/usr/bin/env bash
set -euo pipefail

uv run binddrift toolchain check --run-rustavailable
uv run binddrift dataset versions --fetch-tags
uv run binddrift extract commits --limit 200
uv run binddrift extract all --max-files 5000
uv run binddrift graph build
uv run binddrift detect all
uv run binddrift rank
uv run binddrift eval all
uv run binddrift paper build
