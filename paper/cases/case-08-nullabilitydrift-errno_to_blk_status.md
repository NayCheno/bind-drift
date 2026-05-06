# Failure Analysis: NullabilityDrift for `errno_to_blk_status`

## Summary

`errno_to_blk_status` produced `W-000018` and is included as a negative/failure-analysis case with adjudicated label `FALSE_POSITIVE`.

## Old Version Evidence

- Version: `v6.12`
- Old value or indicators: `{'params': [{'name': 'errno', 'type': 'core::ffi::c_int'}], 'return_type': 'blk_status_t'}`

## New Version Evidence

- Version: `v6.13`
- New value or indicators: `{'params': [{'name': 'errno', 'type': 'ffi::c_int'}], 'return_type': 'blk_status_t'}`

## C-Side Diff

- Old indicators/value: `{'params': [{'name': 'errno', 'type': 'core::ffi::c_int'}], 'return_type': 'blk_status_t'}`
- New indicators/value: `{'params': [{'name': 'errno', 'type': 'ffi::c_int'}], 'return_type': 'blk_status_t'}`

## Rust-Side Dependency

- `.binddrift/worktrees/v6.13/rust/kernel/error.rs:151` in `Error::to_blk_status`
- safe API `Error::to_blk_status`
- `.binddrift/worktrees/v6.13/rust/kernel/error.rs:150`: `// SAFETY: `self.0` is a valid error due to its invariant.`
- wrapper_fix: `e9759c5b9ea555d09f426c70c880e9522e9b0576`

## Safe API / Contract Assumption

The warning reaches a public safe Rust API, so the maintainer review question is whether that API's documented contract remains synchronized with the C-side behavior.

## Manual Review Label

- Adjudicated label: `FALSE_POSITIVE`
- Reviewer 1: `BENIGN_DRIFT` -- errno_to_blk_status evidence shows only core::ffi to ffi type spelling changes. Rust Error::to_blk_status exposure is real, but the oracle summary does not specifically address this symbol or a changed contract.
- Reviewer 2: `FALSE_POSITIVE` -- The packet shows generated binding churn or a namespace/type-alias-only change rather than supported C contract drift. Wrapper evidence is absent or not tied to the claimed drift, so the warning is not supported.
- Adjudication: The old/new evidence for errno_to_blk_status is only type-path or namespace churn such as core::ffi to ffi, with no supported C contract drift or direct same-drift wrapper fix.

## Why This Is Not Generated-Binding-Only

The case has Rust reachability or contract/oracle evidence beyond a generated binding delta; generated-binding-only rows are excluded from positive case selection.

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

Review considered whether the warning should be promoted, but adjudication found the evidence benign, unsupported, or incomplete.

## Maintainer Review Implication

This case documents why similar high-scoring warnings need manual review before being counted as true positives.

## Reproduction Pointers

- Warning: `W-000018`
- Warning UID: `0217c5aca3beed930cd6cd613e9717d4a78ab28013cffd3881c7d5c7ab7db42a`
- Replay pair: `latest-p012-v6.12-to-v6.13`
- Drift type: `NullabilityDrift`
- C symbol: `errno_to_blk_status`
- Risk: `Medium`
- Score: `8.0`
