# Positive: SignatureDrift for `IS_ERR`

## Summary

`IS_ERR` produced `W-000002` and is included as an adjudicated positive review target with label `TRUE_WRAPPER_FIX`.

## Old Version Evidence

- Version: `v6.12`
- Old value or indicators: `{'params': [{'name': 'ptr', 'type': '*const core::ffi::c_void'}], 'return_type': 'bool_'}`

## New Version Evidence

- Version: `v6.13`
- New value or indicators: `{'params': [{'name': 'ptr', 'type': '*const ffi::c_void'}], 'return_type': 'bool_'}`

## C-Side Diff

- Old indicators/value: `{'params': [{'name': 'ptr', 'type': '*const core::ffi::c_void'}], 'return_type': 'bool_'}`
- New indicators/value: `{'params': [{'name': 'ptr', 'type': '*const ffi::c_void'}], 'return_type': 'bool_'}`

## Rust-Side Dependency

- `.binddrift/worktrees/v6.13/rust/kernel/error.rs:295` in `to_result`
- safe API `to_result`
- `.binddrift/worktrees/v6.13/rust/kernel/error.rs:290`: `/// ````
- `.binddrift/worktrees/v6.13/rust/kernel/error.rs:291` error mapping `ERR_PTR_MAPPING`
- wrapper_fix: `752417b3f0e7721f1d630f40da22d57e0dae043e`

## Safe API / Contract Assumption

The warning reaches a public safe Rust API, so the maintainer review question is whether that API's documented contract remains synchronized with the C-side behavior.

## Manual Review Label

- Adjudicated label: `TRUE_WRAPPER_FIX`
- Reviewer 1: `TRUE_WRAPPER_FIX` -- IS_ERR is reached by to_result, and the oracle hit adds a helper to convert C ERR_PTR to Result in rust/helpers.c and rust/kernel/error.rs. That directly matches the error-pointer wrapper contract.
- Reviewer 2: `TRUE_WRAPPER_FIX` -- Later Rust wrapper/helper/binding evidence is in the same exposed API area and plausibly addresses the warned symbol or contract. C source evidence may be binding-only and no build log is present, so this is a wrapper-fix label, not build breakage.
- Adjudication: No build oracle. Rust reaches IS_ERR through to_result, and the Error/ERR_PTR helper fixes in rust helpers and error.rs directly cover the same error-pointer conversion contract.

## Why This Is Not Generated-Binding-Only

The case has Rust reachability or contract/oracle evidence beyond a generated binding delta; generated-binding-only rows are excluded from positive case selection.

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

Review considered whether this was semantic drift; adjudication classifies it as wrapper-fix-backed validation instead of standalone semantic evidence.

## Maintainer Review Implication

A maintainer should inspect the Rust wrapper or safe abstraction path when carrying this C-side change across versions.

## Reproduction Pointers

- Warning: `W-000002`
- Warning UID: `4b538a23e5b7e22f2cc86f95ffea064b2634aa0ab97449ad304889083dc27efd`
- Replay pair: `latest-p012-v6.12-to-v6.13`
- Drift type: `SignatureDrift`
- C symbol: `IS_ERR`
- Risk: `Medium`
- Score: `11.0`
