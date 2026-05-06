# BindDrift

BindDrift is a research prototype for detecting cross-language API and contract drift in Rust-for-Linux safe abstractions.

The artifact treats `vendor/linux` as an input Linux source tree. BindDrift code, experiment data, reports, and paper material live in the repository root.

## Quick Start

```bash
uv run pytest
uv run binddrift --help
uv run binddrift toolchain check --run-rustavailable
uv run binddrift toolchain matrix --start v6.1
uv run binddrift toolchain bootstrap --install-matrix
uv run binddrift dataset versions --fetch-tags
uv run binddrift extract all --max-files 5000
uv run binddrift graph build
uv run binddrift detect all
uv run binddrift rank
uv run binddrift eval all
uv run binddrift paper build --stage final
```

The prototype is implemented as a staged command-line workflow. The pilot pipeline records missing generated bindings or build prerequisites as artifact data rather than treating them as successful extraction.

For the stronger multi-version evaluation path, first generate and bootstrap the
per-kernel Rust-for-Linux toolchain matrix, then run adjacent-release replay.
The matrix starts at `v6.1` and records the libclang family needed by each
bindgen release. On hosts that provide LLVM 15, BindDrift automatically runs
the `v6.1` through `v6.5` bindgen `0.56.0` entries against libclang 15, avoiding
the known LLVM/libclang 16+ anonymous C item-name failure.

```bash
uv run binddrift toolchain matrix --start v6.1 --fetch-tags
uv run binddrift toolchain bootstrap --install-matrix
uv run binddrift replay versions --start v6.1 --include-head --fetch-tags --build-bindings --configure --arch x86_64 --toolchain auto --jobs 1
uv run binddrift --data-dir data/replay/latest eval all --top-k 100 --run-id latest
uv run binddrift paper build --stage final
```

To regenerate the checked-in main evaluation tables and run the full strict
artifact gate from the canonical replay artifacts, use the artifact reproduction
entrypoint:

```bash
uv run python -m binddrift.artifact reproduce
```

Replay outputs are stored under `data/replay/latest/`. Each `replay versions`
run clears that directory and replaces the SQLite `latest` replay rows before
writing new pair outputs, so generated replay artifacts stay stable in commits
without overwriting the pilot warning report.

`toolchain matrix` reads each checked-out kernel version's
`scripts/min-tool-version.sh`, writes `data/toolchain_matrix.json`, and records
the exact `RUSTC`, `RUSTDOC`, `RUSTFMT`, `CLIPPY_DRIVER`, `RUST_LIB_SRC`,
`BINDGEN`, and when needed `LLVM` values replay will inject into kernel builds.
It also records `LIBCLANG_PATH` and `LLVM_CONFIG_PATH`; old bindgen releases are
pinned to a compatible LLVM/libclang family when available. This avoids running
old release tags with a newer Rust compiler or mismatched libclang that may no
longer match the kernel's Rust build assumptions.

## Documentation

- `docs/artifact-guide.md`: reproducible pilot and CCF-B-strength replay workflow.
- `docs/schema-guide.md`: database and warning data model.
- `docs/review-guide.md`: manual review labels and reviewer workflow.
- `docs/scope.md`: locked claim boundary for the tool, evaluation, and paper.
- `docs/plan.md` and `docs/idea.md`: original research plan and positioning.

## Current Pilot Limitation

The checked-in Linux tree does not include generated Rust bindings in the source tree. BindDrift therefore records generated binding files as build outputs under the configured object tree. Run `binddrift kernel prepare --run-make` only after the required Rust-for-Linux toolchain is available.
