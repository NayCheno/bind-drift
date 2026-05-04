# BindDrift

BindDrift is a research prototype for detecting cross-language API and contract drift in Rust-for-Linux safe abstractions.

The artifact treats `vendor/linux` as an input Linux source tree. BindDrift code, experiment data, reports, and paper material live in the repository root.

## Quick Start

```bash
uv run pytest
uv run binddrift --help
uv run binddrift toolchain check --run-rustavailable
uv run binddrift dataset versions --fetch-tags
uv run binddrift extract all --max-files 5000
uv run binddrift graph build
uv run binddrift detect all
uv run binddrift rank
uv run binddrift eval all
uv run binddrift paper build
```

The prototype is implemented as a staged command-line workflow. The pilot pipeline records missing generated bindings or build prerequisites as artifact data rather than treating them as successful extraction.

## Documentation

- `docs/artifact-guide.md`: reproducible pilot workflow.
- `docs/schema-guide.md`: database and warning data model.
- `docs/review-guide.md`: manual review labels and reviewer workflow.
- `docs/scope.md`: locked claim boundary for the tool, evaluation, and paper.
- `docs/plan.md` and `docs/idea.md`: original research plan and positioning.

## Current Pilot Limitation

The checked-in Linux tree does not include generated Rust bindings in the source tree. BindDrift therefore records generated binding files as build outputs under the configured object tree. Run `binddrift kernel prepare --run-make` only after the required Rust-for-Linux toolchain is available.
