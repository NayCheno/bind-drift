#!/usr/bin/env bash
set -euo pipefail

uv run binddrift toolchain matrix \
  --start "${BINDDRIFT_MATRIX_START:-v6.1}" \
  --fetch-tags

if [[ "${BINDDRIFT_BOOTSTRAP_TOOLCHAINS:-0}" == "1" ]]; then
  uv run binddrift toolchain bootstrap --install-matrix
fi

uv run binddrift replay versions \
  --start "${BINDDRIFT_REPLAY_START:-v6.6}" \
  --include-head \
  --fetch-tags \
  --build-bindings \
  --configure \
  --toolchain auto \
  --jobs "${BINDDRIFT_REPLAY_JOBS:-1}"
