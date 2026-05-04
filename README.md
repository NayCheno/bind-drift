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
uv run binddrift paper build
```

The prototype is implemented as a staged command-line workflow. The pilot pipeline records missing generated bindings or build prerequisites as artifact data rather than treating them as successful extraction.

For the stronger multi-version evaluation path, first generate and bootstrap the
per-kernel Rust-for-Linux toolchain matrix, then run adjacent-release replay.
The matrix should still start at `v6.1` so old tags are classified, but the
current reproducible main window starts at `v6.6`: `v6.1` through `v6.5` require
bindgen `0.56.0`, which is known to fail with LLVM/libclang 16+ anonymous C item
names. BindDrift records those tags as toolchain-incompatible on this host
instead of treating the failures as drift evidence.

```bash
uv run binddrift toolchain matrix --start v6.1 --fetch-tags
uv run binddrift toolchain bootstrap --install-matrix
uv run binddrift replay versions --start v6.6 --include-head --fetch-tags --build-bindings --configure --arch x86_64 --toolchain auto --jobs 1
uv run binddrift --data-dir data/replay/<run_id> eval all --top-k 100 --run-id <run_id>
uv run binddrift paper build
```

Replay outputs are stored under `data/replay/<run_id>/` and are also indexed in the SQLite `replay_runs` and `replay_pairs` tables so historical runs do not overwrite the pilot warning report.

`toolchain matrix` reads each checked-out kernel version's
`scripts/min-tool-version.sh`, writes `data/toolchain_matrix.json`, and records
the exact `RUSTC`, `RUSTDOC`, `RUSTFMT`, `CLIPPY_DRIVER`, `RUST_LIB_SRC`, and
`BINDGEN` values replay will inject into kernel builds. It also records
`LIBCLANG_PATH` and `LLVM_CONFIG_PATH` so bindgen uses the same libclang family
as the compiler used by `LLVM=1`. This avoids running old release tags with a
newer Rust compiler or mismatched libclang that may no longer match the kernel's
Rust build assumptions.

## Documentation

- `docs/artifact-guide.md`: reproducible pilot and CCF-B-strength replay workflow.
- `docs/schema-guide.md`: database and warning data model.
- `docs/review-guide.md`: manual review labels and reviewer workflow.
- `docs/scope.md`: locked claim boundary for the tool, evaluation, and paper.
- `docs/plan.md` and `docs/idea.md`: original research plan and positioning.

## Current Pilot Limitation

The checked-in Linux tree does not include generated Rust bindings in the source tree. BindDrift therefore records generated binding files as build outputs under the configured object tree. Run `binddrift kernel prepare --run-make` only after the required Rust-for-Linux toolchain is available.
