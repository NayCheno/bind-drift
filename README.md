# BindDrift

BindDrift is a research prototype for detecting cross-language API and contract drift in Rust-for-Linux safe abstractions.

The artifact treats `vendor/linux` as an input Linux source tree. BindDrift code, experiment data, reports, and paper material live in the repository root.

## Quick Start

```bash
python -m binddrift --help
python -m binddrift env check
python -m binddrift extract commits --limit 50
python -m binddrift extract rust
python -m binddrift extract c --root rust/helpers --max-files 50
python -m binddrift graph build
python -m binddrift detect all
python -m binddrift rank
python -m binddrift eval
```

The prototype is implemented as a staged command-line workflow. The pilot pipeline is intentionally lightweight: it proves the artifact wiring on the local Linux tree without requiring a full Rust-enabled kernel build.

## Documentation

- `docs/artifact-guide.md`: reproducible pilot workflow.
- `docs/schema-guide.md`: database and warning data model.
- `docs/review-guide.md`: manual review labels and reviewer workflow.
- `docs/plan.md` and `docs/idea.md`: original research plan and positioning.

## Current Pilot Limitation

The checked-in Linux tree does not include generated Rust bindings in the source tree. BindDrift therefore records generated binding files as build outputs under the configured object tree. Run `binddrift kernel prepare --run-make` only after the required Rust-for-Linux toolchain is available.
