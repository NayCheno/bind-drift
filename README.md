# BindDrift

BindDrift is a research prototype for detecting cross-language API and contract drift in Rust-for-Linux safe abstractions.

The artifact treats `vendor/linux` as an input Linux source tree. BindDrift code, experiment data, reports, and paper material live in the repository root.

## Quick Start

```bash
python -m binddrift --help
```

The prototype is implemented as a staged command-line workflow. See `docs/artifact-guide.md` for the reproducible pilot pipeline.
