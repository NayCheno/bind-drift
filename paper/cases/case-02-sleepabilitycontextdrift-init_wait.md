# Positive: SleepabilityContextDrift for `init_wait`

## Summary

`init_wait` produced `W-000002` and is included as an adjudicated positive review target with label `TRUE_SEMANTIC_DRIFT`.

## Old Version Evidence

- Version: `v6.14`
- Old value or indicators: `\`

## New Version Evidence

- Version: `v6.15`
- New value or indicators: `init_wait_func(wait, autoremove_wake_function)`

## C-Side Diff

- Old indicators/value: `\`
- New indicators/value: `init_wait_func(wait, autoremove_wake_function)`

## Rust-Side Dependency

- exposure `GENERATED_FROM`: `CFunction:init_wait` -> `RustBindingFunction:init_wait`
- exposure `CALLS_BINDING`: `RustBindingFunction:init_wait` -> `RustUnsafeCall:.binddrift/worktrees/v6.15/rust/kernel/sync/condvar.rs:123:init_wait`
- `.binddrift/worktrees/v6.15/rust/kernel/sync/condvar.rs:123` in `CondVar::new` (unsafe block)
- safe API `CondVar::new`

## Safe API / Contract Assumption

The warning reaches a public safe Rust API, so the maintainer review question is whether that API's documented contract remains synchronized with the C-side behavior.

## Manual Review Label

- Adjudicated label: `TRUE_SEMANTIC_DRIFT`
- Reviewer 1: `TRUE_SEMANTIC_DRIFT` -- Direct C evidence shows real MacroConstDrift for init_wait, and the Rust unsafe/safe exposure depends on that contract. No wrapper oracle is needed because the packet has direct C evidence plus Rust contract dependence.
- Reviewer 2: `TRUE_SEMANTIC_DRIFT` -- Direct C-side drift plus Rust safe_api evidence shows a maintainer-relevant contract dependency for init_wait; no build or wrapper oracle is needed for this semantic label.
- Adjudication: init_wait: direct C source/behavior evidence plus Rust safe/unsafe contract evidence support a stale-contract review target without build or wrapper oracle.

## Why This Is Not Generated-Binding-Only

The case includes C-side source or indicator evidence plus Rust-side dependency evidence.

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

Review considered whether this was only signature churn or generated binding noise; adjudication kept it because C-side drift, Rust exposure, and contract dependence were all present.

## Maintainer Review Implication

A maintainer should inspect the Rust wrapper or safe abstraction path when carrying this C-side change across versions.

## Reproduction Pointers

- Warning: `W-000002`
- Warning UID: `8cb338b4e53ee4c1819885eef759ed2bbd759c1d0e7ff27b73628604a0eea56b`
- Replay pair: `latest-p014-v6.14-to-v6.15`
- Drift type: `SleepabilityContextDrift`
- C symbol: `init_wait`
- Risk: `Medium`
- Score: `8.0`
