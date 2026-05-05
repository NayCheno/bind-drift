# BindDrift Artifact Guide

## Reader And Goal

This guide is for an artifact evaluator or future maintainer. After reading it, they should be able to run the pilot workflow, inspect the generated database, and produce ranked warnings plus evaluation tables.

## Pilot Workflow

Run the commands from the repository root:

```bash
uv run binddrift toolchain check --run-rustavailable
uv run binddrift toolchain matrix --start v6.1
uv run binddrift dataset versions --fetch-tags
uv run binddrift extract commits --limit 200
uv run binddrift extract all --max-files 5000
uv run binddrift graph build
uv run binddrift detect all
uv run binddrift rank
uv run binddrift eval all
uv run binddrift paper build
```

The pilot does not require a full kernel build. If generated bindings are absent, the binding extractor reports the missing object-tree files and continues. This is expected for a fresh checkout without a Rust-enabled kernel build.

## Versioned Rust Toolchains

Rust-for-Linux release tags do not all use the same Rust and bindgen versions.
Before historical replay, generate the matrix:

```bash
uv run binddrift toolchain matrix --start v6.1 --fetch-tags
```

The command reads each selected kernel version's minimum-tool script and writes
`data/toolchain_matrix.json`. The file contains the exact Make variables used by
replay: `RUSTC`, `HOSTRUSTC`, `RUSTDOC`, `RUSTFMT`, `CLIPPY_DRIVER`,
`RUST_LIB_SRC`, `BINDGEN`, and where needed `LLVM`. It also records environment
variables such as `LIBCLANG_PATH` and `LLVM_CONFIG_PATH`, plus compatibility
issues that would make a version invalid for binding-built replay on the current
host. To install the missing Rust toolchains and per-version bindgen binaries:

```bash
uv run binddrift toolchain bootstrap --install-matrix
```

Do not use the host's current stable Rust compiler for the main replay unless
the matrix says it matches the checked-out kernel version. Newer Rust releases
or mismatched libclang versions can break older kernel Rust build rules, which
would contaminate the experiment with toolchain noise. When LLVM 15 is
available, the matrix pins `v6.1` through `v6.5` bindgen `0.56.0` to libclang
15 and injects an LLVM 15 tool prefix for kernel Make, avoiding the known
LLVM/libclang 16+ anonymous C item-name failure.

## Full Binding Extraction

Generated Rust bindings are build artifacts. To extract them, first prepare the kernel object tree and run the Rust availability check:

```bash
uv run binddrift kernel prepare --run-make --configure
uv run binddrift kernel build-bindings --configure
```

After the Linux build system has produced generated bindings, rerun:

```bash
uv run binddrift extract bindings
uv run binddrift graph build
uv run binddrift detect all
uv run binddrift rank
```

## Multi-Version Replay

The CCF-B-strength experiment should use a Linux mirror with official release
tags and the kernel build dependencies needed for Rust bindings (`flex`,
`bison`, `bc`, `pahole`, OpenSSL headers, libelf headers, and the Rust-for-Linux
toolchain). Run:

```bash
uv run binddrift replay versions \
  --start v6.1 \
  --include-head \
  --fetch-tags \
  --build-bindings \
  --configure \
  --toolchain auto \
  --jobs 1
```

This creates one replay run under `data/replay/latest/`, clearing any previous
contents of that directory first. Each adjacent version pair writes its own
`warnings.jsonl`, `warnings.md`, `manual_review.csv`, and evaluation tables,
while the SQLite database records the current run as `latest` in `replay_runs`,
`replay_pairs`, pair-scoped drift events, build oracle rows, and wrapper-fix
oracle rows. Failed pairs are recorded with an error instead of being silently
skipped.

After replay completes, generate the aggregate review sheet and paper tables:

```bash
uv run binddrift --data-dir data/replay/latest eval all --top-k 100 --run-id latest
uv run binddrift paper build
```

For the arm64 external-validity slice, repeat a small run over the latest six
release tags:

```bash
uv run binddrift replay versions \
  --start v6.1 \
  --limit 6 \
  --no-include-head \
  --build-bindings \
  --configure \
  --toolchain auto \
  --arch arm64
```

## Expected Outputs

- Environment metadata captures Linux commit, host architecture, tool versions, and config hash.
- Toolchain matrix metadata captures per-version Rust, rust-src, bindgen, and injected Make variables.
- The SQLite database stores version, commit, binding, Rust usage, C API, indicator, and graph facts.
- Ranked warnings are written as JSONL and as a Markdown report.
- Evaluation tables include replay, fact-count, manual-review, runtime/scalability, baseline, ablation, and case-study outputs for paper integration.

## Interpreting Empty Warnings

An empty warning set means the current pilot inputs did not contain a comparable two-version drift or a symbol-level C indicator that reaches a Rust binding use. It does not mean the Linux tree has no drift. Use a wider C scan, generated bindings, and at least two versions for the replay experiment.
