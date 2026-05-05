# Failure Analysis: NullabilityDrift for `PTR_ERR`

## Summary

`PTR_ERR` produced `W-000006` and is included as a negative/failure-analysis case with adjudicated label `FALSE_POSITIVE`.

## Old Version Evidence

- Version: `v6.15`
- Old value or indicators: `{'params': ['ptr'], 'return_type': 'return'}`

## New Version Evidence

- Version: `v6.16`
- New value or indicators: `{'params': ['opp'], 'return_type': 'return'}`

## C-Side Diff

- Old indicators/value: `{'params': ['ptr'], 'return_type': 'return'}`
- New indicators/value: `{'params': ['opp'], 'return_type': 'return'}`

## Rust-Side Dependency

- `.binddrift/worktrees/v6.16/rust/kernel/error.rs:414` in `From<core::convert::Infallible>::to_result`
- safe API `From<core::convert::Infallible>::to_result`
- `.binddrift/worktrees/v6.16/rust/kernel/error.rs:411`: `// SAFETY: The FFI function does not deref the pointer.`
- `.binddrift/worktrees/v6.16/rust/kernel/error.rs:413`: `// SAFETY: The FFI function does not deref the pointer.`
- `.binddrift/worktrees/v6.16/rust/kernel/error.rs:412` error mapping `IS_ERR_MAPPING`
- wrapper_fix: `752417b3f0e7721f1d630f40da22d57e0dae043e`

## Safe API / Contract Assumption

The warning reaches a public safe Rust API, so the maintainer review question is whether that API's documented contract remains synchronized with the C-side behavior.

## Manual Review Label

- Adjudicated label: `FALSE_POSITIVE`
- Reviewer 1: `FALSE_POSITIVE` -- Fresh Reviewer1 re-review: claimed PTR_ERR C drift is parser/call-site or missing-old-evidence noise; Rust exposure does not establish drift.
- Reviewer 2: `FALSE_POSITIVE` -- Fresh Reviewer2 re-review: evidence does not support a real PTR_ERR API/contract drift; treat as unsupported warning.
- Adjudication: Fresh adjudication: both reviewers found the claimed PTR_ERR drift unsupported or parser/call-site noise despite Rust exposure.

## Why This Is Not Generated-Binding-Only

The case includes C-side source or indicator evidence plus Rust-side dependency evidence.

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

Review considered whether the warning should be promoted, but adjudication found the evidence benign, unsupported, or incomplete.

## Maintainer Review Implication

This case documents why similar high-scoring warnings need manual review before being counted as true positives.

## Reproduction Pointers

- Warning: `W-000006`
- Warning UID: `5ec7e735433ea17d474dbc803baf4b16cb67fbddd317ec06ceaf246b4b06e33e`
- Replay pair: `latest-p015-v6.15-to-v6.16`
- Drift type: `NullabilityDrift`
- C symbol: `PTR_ERR`
- Risk: `High`
- Score: `23.0`
