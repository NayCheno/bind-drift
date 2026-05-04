# BindDrift Artifact Guide

## Reader And Goal

This guide is for an artifact evaluator or future maintainer. After reading it, they should be able to run the pilot workflow, inspect the generated database, and produce ranked warnings plus evaluation tables.

## Pilot Workflow

Run the commands from the repository root:

```bash
uv run binddrift toolchain check --run-rustavailable
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

## Expected Outputs

- Environment metadata captures Linux commit, host architecture, tool versions, and config hash.
- The SQLite database stores version, commit, binding, Rust usage, C API, indicator, and graph facts.
- Ranked warnings are written as JSONL and as a Markdown report.
- Evaluation tables and case skeletons are generated for paper integration.

## Interpreting Empty Warnings

An empty warning set means the current pilot inputs did not contain a comparable two-version drift or a symbol-level C indicator that reaches a Rust binding use. It does not mean the Linux tree has no drift. Use a wider C scan, generated bindings, and at least two versions for the replay experiment.
