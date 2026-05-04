# BindDrift Scope Lock

BindDrift is a warning and prioritization artifact for Rust-for-Linux API and
contract drift. It detects evidence that a Linux C API change may stale a Rust
binding, helper, unsafe wrapper, or safe abstraction.

BindDrift does not claim to prove Rust abstraction soundness. Tier 2 semantic
findings are review targets, not confirmed bugs. Reported evaluation numbers
must come from replay outputs, build logs, wrapper-fix mining, or the manual
review CSV included with the artifact.

The default artifact scope is Linux mainline, x86_64, Rust-enabled builds where
the local toolchain supports them, and the Rust-for-Linux `rust/bindings`,
`rust/helpers`, and `rust/kernel` surfaces.
