# BindDrift Scope Lock

BindDrift prioritizes review targets for Rust-for-Linux cross-language API and
contract drift. It is a warning-prioritization artifact that surfaces evidence
that a Linux C API change may stale a Rust binding, helper, unsafe wrapper, or
safe abstraction.

BindDrift does not prove Rust safe abstraction soundness and does not
automatically detect bugs. Warnings are review targets, not confirmed bugs.
Tier 2 semantic findings are review targets, not confirmed bugs.
`TRUE_WRAPPER_FIX` is reported separately from
`TRUE_SEMANTIC_DRIFT`; wrapper-fix-backed evidence is not counted as semantic
drift. Reported evaluation numbers must come from replay outputs, build logs,
wrapper-fix mining, or the manual review CSV included with the artifact.

BindDrift keeps four boundaries explicit in every paper-facing artifact:

- Drift facts are low-level cross-version C, Rust, or generated-binding facts.
- Promoted warnings are Rust-impact review targets derived from detection-time
  evidence.
- `TRUE_SEMANTIC_DRIFT` is an adjudicated stale-contract review label.
- `TRUE_WRAPPER_FIX` is later wrapper/helper/binding repair evidence and is
  reported separately from `TRUE_SEMANTIC_DRIFT`.

The primary ranker is `BindDrift-oracle-blind`. Build-breakage and wrapper-fix
oracles are labels and auxiliary validation only; they do not enter the primary
score or Top-K selection. Known threats include incomplete regex/AST extraction,
Linux-specific and Rust-for-Linux-specific scope, generated-binding availability,
toolchain/config dependence, and semantic-label subjectivity.

The default artifact scope is Linux mainline, x86_64, Rust-enabled builds where
the local toolchain supports them, and the Rust-for-Linux `rust/bindings`,
`rust/helpers`, and `rust/kernel` surfaces.
