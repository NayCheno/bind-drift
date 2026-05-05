# SignatureDrift Case Study

## One-Line Summary

`security_secid_to_secctx` produced `W-000018` with adjudicated true-positive contract evidence.

## Old Version Evidence

- Version: `v6.13`
- Old value or indicators: `{'params': ['u32 secid', 'char **secdata', 'u32 *seclen'], 'return_type': 'static inline int'}`

## New Version Evidence

- Version: `v6.14`
- New value or indicators: `{'params': ['u32 secid', 'struct lsm_context *cp'], 'return_type': 'static inline int'}`

## C-Side Diff Or Indicator Change

BindDrift observed `SignatureDrift` evidence for `security_secid_to_secctx`.

- Old indicators/value: `{'params': ['u32 secid', 'char **secdata', 'u32 *seclen'], 'return_type': 'static inline int'}`
- New indicators/value: `{'params': ['u32 secid', 'struct lsm_context *cp'], 'return_type': 'static inline int'}`

## Rust Wrapper Or Safe API Dependency

BindDrift attached the following Rust impact evidence.

- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/security.rs:31` in `SecurityCtx::from_secid`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/security.rs:27`: `// SAFETY: `struct lsm_context` can be initialized to all zeros.`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/security.rs:30`: `// SAFETY: Just a C FFI call. The pointer is valid for writes.`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/security.rs:26` error mapping `RESULT_RETURN`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/security.rs:31` error mapping `TO_RESULT_MAPPING`
- safe API `SecurityCtx::from_secid`

## Reviewer Adjudicated Label

The adjudicated review label is `TRUE_SEMANTIC_DRIFT`.

## Why The Compiler Cannot Fully Catch It

This case is treated as a contract-review target. The type checker can validate the current call shape, but it does not verify that Rust wrapper assumptions about nullability, error representation, ownership, or context remain synchronized with C-side behavior.

## Why This Is Not Generated-Binding-Only

This case includes C-side source or indicator evidence plus Rust-side contract, safe API, or oracle evidence; generated bindings alone are not sufficient for case-study selection.

## BindDrift Warning

- Warning: `W-000018`
- Drift type: `SignatureDrift`
- C symbol: `security_secid_to_secctx`
- Risk: `High`
- Score: `17.0`
- Adjudicated label: `TRUE_SEMANTIC_DRIFT`
- Replay pair: `latest-p013-v6.13-to-v6.14`

## Evidence

The evidence above is copied from the ranked BindDrift warning report. The current artifact keeps this case within the warning/prioritization claim boundary.

## Impact

Historical warning from `v6.13` to `v6.14`.

## Lesson

Safe Rust APIs can depend on C-side contracts that are not represented in the Rust function signature. BindDrift makes that dependency explicit so maintainers can prioritize review.
