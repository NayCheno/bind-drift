# Positive: NullabilityDrift for `security_secid_to_secctx`

## Summary

`security_secid_to_secctx` produced `W-000018` and is included as an adjudicated positive review target with label `TRUE_SEMANTIC_DRIFT`.

## Old Version Evidence

- Version: `v6.13`
- Old value or indicators: `{'params': ['u32 secid', 'char **secdata', 'u32 *seclen'], 'return_type': 'static inline int'}`

## New Version Evidence

- Version: `v6.14`
- New value or indicators: `{'params': ['u32 secid', 'struct lsm_context *cp'], 'return_type': 'static inline int'}`

## C-Side Diff

- Old indicators/value: `{'params': ['u32 secid', 'char **secdata', 'u32 *seclen'], 'return_type': 'static inline int'}`
- New indicators/value: `{'params': ['u32 secid', 'struct lsm_context *cp'], 'return_type': 'static inline int'}`

## Rust-Side Dependency

- `.binddrift/worktrees/v6.14/rust/kernel/security.rs:31` in `SecurityCtx::from_secid`
- safe API `SecurityCtx::from_secid`
- `.binddrift/worktrees/v6.14/rust/kernel/security.rs:27`: `// SAFETY: `struct lsm_context` can be initialized to all zeros.`
- `.binddrift/worktrees/v6.14/rust/kernel/security.rs:30`: `// SAFETY: Just a C FFI call. The pointer is valid for writes.`
- `.binddrift/worktrees/v6.14/rust/kernel/security.rs:26` error mapping `RESULT_RETURN`
- `.binddrift/worktrees/v6.14/rust/kernel/security.rs:31` error mapping `TO_RESULT_MAPPING`

## Safe API / Contract Assumption

The warning reaches a public safe Rust API, so the maintainer review question is whether that API's documented contract remains synchronized with the C-side behavior.

## Manual Review Label

- Adjudicated label: `TRUE_SEMANTIC_DRIFT`
- Reviewer 1: `TRUE_SEMANTIC_DRIFT` -- C-side signature drift is concrete: security_secid_to_secctx changes from char **/u32 * to struct lsm_context *. Rust exposes a public SecurityCtx::from_secid safe API, initializes lsm_context, calls the binding, maps the result, and relies on the returned context invariants. No build or wrapper-fix oracle is present.
- Reviewer 2: `TRUE_SEMANTIC_DRIFT` -- Concrete C evidence shows security_secid_to_secctx changing from char **/u32 * outputs to struct lsm_context *. Rust exposes a safe SecurityCtx::from_secid API that initializes lsm_context, passes it to the binding, maps errors, and relies on that contract.
- Adjudication: Concrete C evidence shows security_secid_to_secctx changing from char ** plus length outputs to struct lsm_context *. Rust exposes SecurityCtx::from_secid as a safe API, initializes lsm_context, passes it to the binding, and maps errors. No build or wrapper-fix oracle is present.

## Why This Is Not Generated-Binding-Only

The case includes C-side source or indicator evidence plus Rust-side dependency evidence.

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

Review considered whether this was only signature churn or generated binding noise; adjudication kept it because C-side drift, Rust exposure, and contract dependence were all present.

## Maintainer Review Implication

A maintainer should inspect the Rust wrapper or safe abstraction path when carrying this C-side change across versions.

## Reproduction Pointers

- Warning: `W-000018`
- Warning UID: `ccf6ca0711b3a3fb07496b72daf90fe34a85e1a14e33485ddbfd4e0f281baa75`
- Replay pair: `latest-p013-v6.13-to-v6.14`
- Drift type: `NullabilityDrift`
- C symbol: `security_secid_to_secctx`
- Risk: `High`
- Score: `17.0`
