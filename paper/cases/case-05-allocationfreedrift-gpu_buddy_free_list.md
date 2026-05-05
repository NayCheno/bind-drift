# Positive: AllocationFreeDrift for `gpu_buddy_free_list`

## Summary

`gpu_buddy_free_list` produced `W-000007` and is included as an adjudicated positive review target with label `TRUE_WRAPPER_FIX`.

## Old Version Evidence

- Version: `v7.0`
- Old value or indicators: `absent`

## New Version Evidence

- Version: `HEAD_6d35786de281`
- New value or indicators: `added`

## C-Side Diff

- Old indicators/value: `absent`
- New indicators/value: `added`

## Rust-Side Dependency

- `.binddrift/worktrees/HEAD_6d35786de281/rust/kernel/gpu/buddy.rs:541` in `drop`
- `.binddrift/worktrees/HEAD_6d35786de281/rust/kernel/gpu/buddy.rs:537`: `// SAFETY:`
- `.binddrift/worktrees/HEAD_6d35786de281/rust/kernel/gpu/buddy.rs:546`: `/// A GPU buddy block.`
- wrapper_fix: `b9616d9721bf8a56d5038e85d2ebbe0ec9d56a94`

## Safe API / Contract Assumption

The warning is connected to later Rust wrapper/helper evidence and is reported separately from semantic-only drift.

## Manual Review Label

- Adjudicated label: `TRUE_WRAPPER_FIX`
- Reviewer 1: `TRUE_WRAPPER_FIX` -- Binding-only old=absent/new=added evidence is partial, but the wrapper-fix oracle directly introduces Rust GPU buddy bindings and matches gpu_buddy_free_list. Rust exposure includes the allocated-block Drop path with safety comments, so this is a connected wrapper-fix target.
- Reviewer 2: `TRUE_WRAPPER_FIX` -- b9616d9721bf adds Rust GPU buddy bindings and Rust AllocatedBlocks drop code calls gpu_buddy_free_list. The wrapper/binding addition is specific to the warned symbol.
- Adjudication: b9616d9721bf adds Rust GPU buddy bindings and an AllocatedBlocks Drop path that calls gpu_buddy_free_list. The wrapper-fix evidence directly addresses the warned helper symbol and Rust exposure path.

## Why This Is Not Generated-Binding-Only

The case has Rust reachability or contract/oracle evidence beyond a generated binding delta; generated-binding-only rows are excluded from positive case selection.

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

Review considered whether this was semantic drift; adjudication classifies it as wrapper-fix-backed validation instead of standalone semantic evidence.

## Maintainer Review Implication

A maintainer should inspect the Rust wrapper or safe abstraction path when carrying this C-side change across versions.

## Reproduction Pointers

- Warning: `W-000007`
- Warning UID: `2a5e3fb41cee7b91e32841323f0c3e07edd883957de4ab77c6bc4762adb70109`
- Replay pair: `latest-p020-v7.0-to-HEAD_6d35786de281`
- Drift type: `AllocationFreeDrift`
- C symbol: `gpu_buddy_free_list`
- Risk: `Low`
- Score: `3.0`
