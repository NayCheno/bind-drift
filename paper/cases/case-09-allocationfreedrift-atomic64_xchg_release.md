# Failure Analysis: AllocationFreeDrift for `atomic64_xchg_release`

## Summary

`atomic64_xchg_release` produced `W-000086` and is included as a negative/failure-analysis case with adjudicated label `FALSE_POSITIVE`.

## Old Version Evidence

- Version: `v6.17`
- Old value or indicators: `absent`

## New Version Evidence

- Version: `v6.18`
- New value or indicators: `added`

## C-Side Diff

- Old indicators/value: `absent`
- New indicators/value: `added`

## Rust-Side Dependency

- exposure `GENERATED_FROM`: `CFunction:atomic64_xchg_release` -> `RustBindingFunction:atomic64_xchg_release`
- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## Safe API / Contract Assumption

The warning is connected to later Rust wrapper/helper evidence and is reported separately from semantic-only drift.

## Manual Review Label

- Adjudicated label: `FALSE_POSITIVE`
- Reviewer 1: `FALSE_POSITIVE` -- Warning is generated/binding-only or unsupported for atomic64_xchg_release with no non-generated C proof and no reachable Rust impact.
- Reviewer 2: `FALSE_POSITIVE` -- Unsupported generated binding target rule matched.
- Adjudication: Unsupported generated binding target calibration is present; adjudicated FALSE_POSITIVE per v3 policy.

## Why This Is Not Generated-Binding-Only

The case has Rust reachability or contract/oracle evidence beyond a generated binding delta; generated-binding-only rows are excluded from positive case selection.

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

Review considered whether the warning should be promoted, but adjudication found the evidence benign, unsupported, or incomplete.

## Maintainer Review Implication

This case documents why similar high-scoring warnings need manual review before being counted as true positives.

## Reproduction Pointers

- Warning: `W-000086`
- Warning UID: `9f03fab34e6f2ea2db53979fc5d8f6010b2fba2efaeed2a9e004fc1e12c5b283`
- Replay pair: `latest-p017-v6.17-to-v6.18`
- Drift type: `AllocationFreeDrift`
- C symbol: `atomic64_xchg_release`
- Risk: `Low`
- Score: `-8.0`
