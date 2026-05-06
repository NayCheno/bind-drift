# Positive: SignatureDrift for `REFCOUNT_INIT`

## Summary

`REFCOUNT_INIT` produced `W-000004` and is included as an adjudicated positive review target with label `TRUE_WRAPPER_FIX`.

## Old Version Evidence

- Version: `v6.12`
- Old value or indicators: `{'params': [{'name': 'n', 'type': 'core::ffi::c_int'}], 'return_type': 'refcount_t'}`

## New Version Evidence

- Version: `v6.13`
- New value or indicators: `{'params': [{'name': 'n', 'type': 'ffi::c_int'}], 'return_type': 'refcount_t'}`

## C-Side Diff

- Old indicators/value: `{'params': [{'name': 'n', 'type': 'core::ffi::c_int'}], 'return_type': 'refcount_t'}`
- New indicators/value: `{'params': [{'name': 'n', 'type': 'ffi::c_int'}], 'return_type': 'refcount_t'}`

## Rust-Side Dependency

- `.binddrift/worktrees/v6.13/rust/kernel/sync/arc.rs:199` in `Arc<T>::new`
- `.binddrift/worktrees/v6.13/rust/kernel/sync/arc.rs:318` in `Arc<T>::into_unique_or_drop`
- `.binddrift/worktrees/v6.13/rust/kernel/sync/arc.rs:646` in `UniqueArc<T>::new_uninit`
- safe API `Arc<T>::new`
- safe API `Arc<T>::into_unique_or_drop`
- safe API `UniqueArc<T>::new_uninit`
- `.binddrift/worktrees/v6.13/rust/kernel/sync/arc.rs:194`: `/// Constructs a new reference counted instance of `T`.`
- `.binddrift/worktrees/v6.13/rust/kernel/sync/arc.rs:198`: `// SAFETY: There are no safety requirements for this FFI call.`
- `.binddrift/worktrees/v6.13/rust/kernel/sync/arc.rs:313`: `// SAFETY: We own a refcount, so the pointer is not dangling.`
- `.binddrift/worktrees/v6.13/rust/kernel/sync/arc.rs:195` error mapping `RESULT_RETURN`
- `.binddrift/worktrees/v6.13/rust/kernel/sync/arc.rs:641` error mapping `RESULT_RETURN`
- wrapper_fix: `bb38f35b35f9de0cebc4d62ea73482454e38cef3`
- wrapper_fix: `076acb647c1f448177d8b3b0e4f33de959713d7d`
- wrapper_fix: `9ba1aaf25ab7dadb910348b6857865e87b4c5689`

## Safe API / Contract Assumption

The warning reaches a public safe Rust API, so the maintainer review question is whether that API's documented contract remains synchronized with the C-side behavior.

## Manual Review Label

- Adjudicated label: `TRUE_WRAPPER_FIX`
- Reviewer 1: `BENIGN_DRIFT` -- The reported REFCOUNT_INIT drift is only core::ffi to ffi type spelling in generated binding evidence. Rust Arc/Refcount exposure is real, but the packet does not show a C contract change beyond equivalent type paths.
- Reviewer 2: `TRUE_WRAPPER_FIX` -- Later Rust wrapper/helper/binding evidence is in the same exposed API area and plausibly addresses the warned symbol or contract. C source evidence may be binding-only and no build log is present, so this is a wrapper-fix label, not build breakage.
- Adjudication: No build oracle. Rust reaches REFCOUNT_INIT through Arc<T>::new, Arc<T>::into_unique_or_drop, UniqueArc<T>::new_uninit, and refcount helper/Refcount or Arc conversion fixes directly cover the same refcount wrapper contract.

## Why This Is Not Generated-Binding-Only

The case has Rust reachability or contract/oracle evidence beyond a generated binding delta; generated-binding-only rows are excluded from positive case selection.

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

Review considered whether this was semantic drift; adjudication classifies it as wrapper-fix-backed validation instead of standalone semantic evidence.

## Maintainer Review Implication

A maintainer should inspect the Rust wrapper or safe abstraction path when carrying this C-side change across versions.

## Reproduction Pointers

- Warning: `W-000004`
- Warning UID: `399880825c439eb15d3e73aa711d383a87e7dbba9e9a3173f6a97bdef4e841b7`
- Replay pair: `latest-p012-v6.12-to-v6.13`
- Drift type: `SignatureDrift`
- C symbol: `REFCOUNT_INIT`
- Risk: `High`
- Score: `15.0`
