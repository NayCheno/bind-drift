# Positive: OwnershipRefcountDrift for `refcount_set`

## Summary

`refcount_set` produced `W-000176` and is included as an adjudicated positive review target with label `TRUE_WRAPPER_FIX`.

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

- `.binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:56` in `Refcount::set`
- safe API `Refcount::set`
- `.binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:52`: `/// Set a refcount's value.`
- `.binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:55`: `// SAFETY: `self.as_ptr()` is valid.`
- `.binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:59`: `/// Increment a refcount.`
- `.binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:55` lifetime fact `AS_PTR`
- `.binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:56` lifetime fact `AS_PTR`
- wrapper_fix: `bb38f35b35f9de0cebc4d62ea73482454e38cef3`
- wrapper_fix: `9ba1aaf25ab7dadb910348b6857865e87b4c5689`

## Safe API / Contract Assumption

The warning reaches a public safe Rust API, so the maintainer review question is whether that API's documented contract remains synchronized with the C-side behavior.

## Manual Review Label

- Adjudicated label: `TRUE_WRAPPER_FIX`
- Reviewer 1: `TRUE_WRAPPER_FIX` -- refcount_set is reached through a Rust safe Refcount API, and the refcount wrapper/helper commits directly match the symbol and files. This is supported as a wrapper-fix target with binding-only C evidence.
- Reviewer 2: `TRUE_WRAPPER_FIX` -- A later Refcount wrapper commit adds rust_helper_refcount_set and the safe Refcount::set method. This directly addresses the same symbol and Rust wrapper path. No build failure is shown.
- Adjudication: Refcount::set safely calls bindings::refcount_set, and refcount helper/wrapper commits add or refine Rust helper/API support for refcount_set. No build failure is shown; binding-only C evidence limits the positive claim to wrapper fix.

## Why This Is Not Generated-Binding-Only

The case has Rust reachability or contract/oracle evidence beyond a generated binding delta; generated-binding-only rows are excluded from positive case selection.

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

Review considered whether this was semantic drift; adjudication classifies it as wrapper-fix-backed validation instead of standalone semantic evidence.

## Maintainer Review Implication

A maintainer should inspect the Rust wrapper or safe abstraction path when carrying this C-side change across versions.

## Reproduction Pointers

- Warning: `W-000176`
- Warning UID: `f6741da33cd41c225aef023b1b2a71f2e315f0610d131c539603cbe7aedb8ec6`
- Replay pair: `latest-p017-v6.17-to-v6.18`
- Drift type: `OwnershipRefcountDrift`
- C symbol: `refcount_set`
- Risk: `Medium`
- Score: `10.0`
