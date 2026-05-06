# Positive: NullabilityDrift for `errname`

## Summary

`errname` produced `W-000017` and is included as an adjudicated positive review target with label `TRUE_WRAPPER_FIX`.

## Old Version Evidence

- Version: `v6.12`
- Old value or indicators: `{'params': [{'name': 'err', 'type': 'core::ffi::c_int'}], 'return_type': '*const core::ffi::c_char'}`

## New Version Evidence

- Version: `v6.13`
- New value or indicators: `{'params': [{'name': 'err', 'type': 'ffi::c_int'}], 'return_type': '*const ffi::c_char'}`

## C-Side Diff

- Old indicators/value: `{'params': [{'name': 'err', 'type': 'core::ffi::c_int'}], 'return_type': '*const core::ffi::c_char'}`
- New indicators/value: `{'params': [{'name': 'err', 'type': 'ffi::c_int'}], 'return_type': '*const ffi::c_char'}`

## Rust-Side Dependency

- `.binddrift/worktrees/v6.13/rust/kernel/error.rs:167` in `Error::name`
- safe API `Error::name`
- safe API `Error::name`
- `.binddrift/worktrees/v6.13/rust/kernel/error.rs:163`: `/// Returns a string representing the error, if one exists.`
- `.binddrift/worktrees/v6.13/rust/kernel/error.rs:166`: `// SAFETY: Just an FFI call, there are no extra safety requirements.`
- `.binddrift/worktrees/v6.13/rust/kernel/error.rs:171`: `// SAFETY: The string returned by `errname` is static and `NUL`-terminated.`
- `.binddrift/worktrees/v6.13/rust/kernel/error.rs:165` error mapping `OPTION_RETURN`
- wrapper_fix: `d2e3115d717197cb2bc020dd1f06b06538474ac3`
- wrapper_fix: `e9759c5b9ea555d09f426c70c880e9522e9b0576`

## Safe API / Contract Assumption

The warning reaches a public safe Rust API, so the maintainer review question is whether that API's documented contract remains synchronized with the C-side behavior.

## Manual Review Label

- Adjudicated label: `TRUE_WRAPPER_FIX`
- Reviewer 1: `TRUE_WRAPPER_FIX` -- errname is reached by Error::name and the oracle hit explicitly integrates errname into Error Debug in rust/helpers.c and rust/kernel/error.rs. This matches the same Error wrapper surface.
- Reviewer 2: `TRUE_WRAPPER_FIX` -- Later Rust wrapper/helper/binding evidence is in the same exposed API area and plausibly addresses the warned symbol or contract. C source evidence may be binding-only and no build log is present, so this is a wrapper-fix label, not build breakage.
- Adjudication: No build oracle. Error::name reaches errname, and the oracle explicitly integrates errname into the Rust Error formatting/helper path, matching the same wrapper contract.

## Why This Is Not Generated-Binding-Only

The case has Rust reachability or contract/oracle evidence beyond a generated binding delta; generated-binding-only rows are excluded from positive case selection.

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

Review considered whether this was semantic drift; adjudication classifies it as wrapper-fix-backed validation instead of standalone semantic evidence.

## Maintainer Review Implication

A maintainer should inspect the Rust wrapper or safe abstraction path when carrying this C-side change across versions.

## Reproduction Pointers

- Warning: `W-000017`
- Warning UID: `f8dcd9f2cd00551e7fcbf283302d8a99ffb5521ed87acb06c679f5224daad64e`
- Replay pair: `latest-p012-v6.12-to-v6.13`
- Drift type: `NullabilityDrift`
- C symbol: `errname`
- Risk: `Medium`
- Score: `11.0`
