#!/usr/bin/env bash
set -euo pipefail

VERSION_START="${BINDDRIFT_VERSION_START:-v6.1}"
MATRIX_START="${BINDDRIFT_MATRIX_START:-$VERSION_START}"
REPLAY_START="${BINDDRIFT_REPLAY_START:-$VERSION_START}"

uv run binddrift toolchain matrix \
  --start "$MATRIX_START" \
  --fetch-tags

if [[ "${BINDDRIFT_BOOTSTRAP_TOOLCHAINS:-0}" == "1" ]]; then
  uv run binddrift toolchain bootstrap --install-matrix
fi

uv run binddrift replay versions \
  --start "$REPLAY_START" \
  --include-head \
  --fetch-tags \
  --build-bindings \
  --configure \
  --arch "${BINDDRIFT_REPLAY_ARCH:-x86_64}" \
  --toolchain auto \
  --jobs "${BINDDRIFT_REPLAY_JOBS:-4}"
