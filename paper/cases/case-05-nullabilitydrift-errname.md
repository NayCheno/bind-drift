# Positive: NullabilityDrift for `errname`

## Summary

`errname` produced `W-000001` and is included as an adjudicated positive review target with label `TRUE_WRAPPER_FIX`.

## Old Version Evidence

- Version: `v6.4`
- Old value or indicators: `absent`

## New Version Evidence

- Version: `v6.5`
- New value or indicators: `added`

## C-Side Diff

- Old indicators/value: `absent`
- New indicators/value: `added`

## Rust-Side Dependency

- exposure `HAS_C_INDICATOR`: `CFunction:errname` -> `CBehaviorIndicator:errname:NULL_RETURN:.binddrift/worktrees/v6.5/include/linux/errname.h:12`
- exposure `GENERATED_FROM`: `CFunction:errname` -> `RustBindingFunction:errname`
- exposure `HAS_ERROR_MAPPING`: `RustBindingFunction:errname` -> `RustErrorMapping:.binddrift/worktrees/v6.5/rust/kernel/error.rs:142:OPTION_RETURN`
- exposure `HAS_SAFETY_COMMENT`: `RustBindingFunction:errname` -> `RustSafetyComment:.binddrift/worktrees/v6.5/rust/kernel/error.rs:140`
- exposure `HAS_SAFETY_COMMENT`: `RustBindingFunction:errname` -> `RustSafetyComment:.binddrift/worktrees/v6.5/rust/kernel/error.rs:143`
- `.binddrift/worktrees/v6.5/rust/kernel/error.rs:144` in `Error::name` (unsafe block)
- safe API `Error::name`
- safe API `Error::name`
- `.binddrift/worktrees/v6.5/rust/kernel/error.rs:140`: `/// Returns a string representing the error, if one exists.`
- `.binddrift/worktrees/v6.5/rust/kernel/error.rs:143`: `// SAFETY: Just an FFI call, there are no extra safety requirements.`
- `.binddrift/worktrees/v6.5/rust/kernel/error.rs:148`: `// SAFETY: The string returned by `errname` is static and `NUL`-terminated.`
- `.binddrift/worktrees/v6.5/rust/kernel/error.rs:142` error mapping `OPTION_RETURN`
- wrapper_fix: `d2e3115d717197cb2bc020dd1f06b06538474ac3`
- wrapper_fix: `e9759c5b9ea555d09f426c70c880e9522e9b0576`

## Safe API / Contract Assumption

The warning reaches a public safe Rust API, so the maintainer review question is whether that API's documented contract remains synchronized with the C-side behavior.

## Manual Review Label

- Adjudicated label: `TRUE_WRAPPER_FIX`
- Reviewer 1: `TRUE_WRAPPER_FIX` -- Packet reports a direct same-symbol Rust wrapper/helper/binding fix for errname.
- Reviewer 2: `TRUE_WRAPPER_FIX` -- Same-symbol wrapper oracle matched before lower-priority rules.
- Adjudication: Direct same-symbol wrapper oracle is present; adjudicated TRUE_WRAPPER_FIX per v3 policy.

## Why This Is Not Generated-Binding-Only

The case has Rust reachability or contract/oracle evidence beyond a generated binding delta; generated-binding-only rows are excluded from positive case selection.

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

Review considered whether this was semantic drift; adjudication classifies it as wrapper-fix-backed validation instead of standalone semantic evidence.

## Maintainer Review Implication

A maintainer should inspect the Rust wrapper or safe abstraction path when carrying this C-side change across versions.

## Reproduction Pointers

- Warning: `W-000001`
- Warning UID: `294099e6983e2b23170870a24c569e1b11781c73105816716babe3dd7be19618`
- Replay pair: `latest-p004-v6.4-to-v6.5`
- Drift type: `NullabilityDrift`
- C symbol: `errname`
- Risk: `High`
- Score: `12.0`
