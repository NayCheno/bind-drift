# Failure Analysis: OwnershipRefcountDrift for `refcount_set`

## Summary

`refcount_set` produced `W-000176` and is included as a negative/failure-analysis case with adjudicated label `FALSE_POSITIVE`.

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

- exposure `GENERATED_FROM`: `CFunction:refcount_set` -> `RustBindingFunction:refcount_set`
- exposure `AFFECTS_LIFETIME`: `RustBindingFunction:refcount_set` -> `RustLifetimeFact:.binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:55:AS_PTR`
- exposure `AFFECTS_LIFETIME`: `RustBindingFunction:refcount_set` -> `RustLifetimeFact:.binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:56:AS_PTR`
- exposure `HAS_SAFETY_COMMENT`: `RustBindingFunction:refcount_set` -> `RustSafetyComment:.binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:52`
- exposure `HAS_SAFETY_COMMENT`: `RustBindingFunction:refcount_set` -> `RustSafetyComment:.binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:55`
- `.binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:56` in `Refcount::set` (unsafe block)
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

- Adjudicated label: `FALSE_POSITIVE`
- Reviewer 1: `UNCLEAR` -- refcount_set reaches Rust safe or unsafe code, but the wrapper oracle is broad-family only and the packet lacks exact same-symbol/direct contract proof. This is plausible but not enough for TRUE_WRAPPER_FIX or semantic drift.
- Reviewer 2: `UNCLEAR` -- refcount_set has Rust safe_api exposure and broad/plausible context, but lacks direct same-symbol wrapper evidence or complete old/new C/binding proof.
- Adjudication: refcount_set: broad-family wrapper evidence is auxiliary only. Without direct same-symbol/same-contract proof or a semantic C-to-Rust contract chain, the warning is unsupported as a Rust-impact target.

## Why This Is Not Generated-Binding-Only

The case has Rust reachability or contract/oracle evidence beyond a generated binding delta; generated-binding-only rows are excluded from positive case selection.

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

Review considered whether the warning should be promoted, but adjudication found the evidence benign, unsupported, or incomplete.

## Maintainer Review Implication

This case documents why similar high-scoring warnings need manual review before being counted as true positives.

## Reproduction Pointers

- Warning: `W-000176`
- Warning UID: `f6741da33cd41c225aef023b1b2a71f2e315f0610d131c539603cbe7aedb8ec6`
- Replay pair: `latest-p017-v6.17-to-v6.18`
- Drift type: `OwnershipRefcountDrift`
- C symbol: `refcount_set`
- Risk: `Medium`
- Score: `10.0`
