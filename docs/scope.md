# BindDrift Scope Lock

BindDrift prioritizes review targets for Rust-for-Linux cross-language API and
contract drift. It is a warning and prioritization artifact that detects
evidence that a Linux C API change may stale a Rust binding, helper, unsafe
wrapper, or safe abstraction.

BindDrift does not prove Rust safe abstraction soundness and does not
automatically detect bugs. Tier 2 semantic findings are review targets, not
confirmed bugs. `TRUE_WRAPPER_FIX` is reported separately from
`TRUE_SEMANTIC_DRIFT`; wrapper-fix-backed evidence is not counted as semantic
drift. Reported evaluation numbers must come from replay outputs, build logs,
wrapper-fix mining, or the manual review CSV included with the artifact.

The default artifact scope is Linux mainline, x86_64, Rust-enabled builds where
the local toolchain supports them, and the Rust-for-Linux `rust/bindings`,
`rust/helpers`, and `rust/kernel` surfaces.
