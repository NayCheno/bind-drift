# Positive: SignatureDrift for `REFCOUNT_INIT`

## Summary

`REFCOUNT_INIT` produced `W-000001` and is included as an adjudicated positive review target with label `TRUE_WRAPPER_FIX`.

## Old Version Evidence

- Version: `v6.2`
- Old value or indicators: `absent`

## New Version Evidence

- Version: `v6.3`
- New value or indicators: `added`

## C-Side Diff

- Old indicators/value: `absent`
- New indicators/value: `added`

## Rust-Side Dependency

- `.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:156` in `Arc<T>::try_new`
- safe API `Arc<T>::try_new`
- `.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:151`: `/// Constructs a new reference counted instance of `T`.`
- `.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:155`: `// SAFETY: There are no safety requirements for this FFI call.`
- `.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:152` error mapping `RESULT_RETURN`
- wrapper_fix: `bb38f35b35f9de0cebc4d62ea73482454e38cef3`
- wrapper_fix: `076acb647c1f448177d8b3b0e4f33de959713d7d`
- wrapper_fix: `9ba1aaf25ab7dadb910348b6857865e87b4c5689`

## Safe API / Contract Assumption

The warning reaches a public safe Rust API, so the maintainer review question is whether that API's documented contract remains synchronized with the C-side behavior.

## Manual Review Label

- Adjudicated label: `TRUE_WRAPPER_FIX`
- Reviewer 1: `TRUE_WRAPPER_FIX` -- REFCOUNT_INIT appears as an added binding reached by Arc::try_new, and oracle hits include implementing kernel::sync::Refcount, converting Arc to Refcount, and adding a refcount helper. That plausibly addresses the same refcount wrapper contract.
- Reviewer 2: `TRUE_WRAPPER_FIX` -- Later Rust wrapper/helper/binding evidence is in the same exposed API area and plausibly addresses the warned symbol or contract. C source evidence may be binding-only and no build log is present, so this is a wrapper-fix label, not build breakage.
- Adjudication: No build oracle. Rust reaches REFCOUNT_INIT through Arc<T>::try_new, and refcount helper/Refcount or Arc conversion fixes directly cover the same refcount wrapper contract.

## Why This Is Not Generated-Binding-Only

The case has Rust reachability or contract/oracle evidence beyond a generated binding delta; generated-binding-only rows are excluded from positive case selection.

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

Review considered whether this was semantic drift; adjudication classifies it as wrapper-fix-backed validation instead of standalone semantic evidence.

## Maintainer Review Implication

A maintainer should inspect the Rust wrapper or safe abstraction path when carrying this C-side change across versions.

## Reproduction Pointers

- Warning: `W-000001`
- Warning UID: `a3d89044e191c0409751d7986088db2623ef9ff2bb3853007fe5cd574b88a786`
- Replay pair: `latest-p002-v6.2-to-v6.3`
- Drift type: `SignatureDrift`
- C symbol: `REFCOUNT_INIT`
- Risk: `High`
- Score: `12.0`
