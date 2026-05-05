# SignatureDrift Case Study

## One-Line Summary

`security_release_secctx` produced `W-000017` with adjudicated true-positive contract evidence.

## Old Version Evidence

- Version: `v6.13`
- Old value or indicators: `{'params': ['char *secdata', 'u32 seclen'], 'return_type': 'static inline void'}`

## New Version Evidence

- Version: `v6.14`
- New value or indicators: `{'params': ['struct lsm_context *cp'], 'return_type': 'static inline void'}`

## C-Side Diff Or Indicator Change

BindDrift observed `SignatureDrift` evidence for `security_release_secctx`.

- Old indicators/value: `{'params': ['char *secdata', 'u32 seclen'], 'return_type': 'static inline void'}`
- New indicators/value: `{'params': ['struct lsm_context *cp'], 'return_type': 'static inline void'}`

## Rust Wrapper Or Safe API Dependency

BindDrift attached the following Rust impact evidence.

- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/security.rs:68` in `drop`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/security.rs:65`: `// SAFETY: By the invariant of `Self`, this frees a context that came from a successful`

## Reviewer Adjudicated Label

The adjudicated review label is `TRUE_SEMANTIC_DRIFT`.

## Why The Compiler Cannot Fully Catch It

This case is treated as a contract-review target. The type checker can validate the current call shape, but it does not verify that Rust wrapper assumptions about nullability, error representation, ownership, or context remain synchronized with C-side behavior.

## Why This Is Not Generated-Binding-Only

This case includes C-side source or indicator evidence plus Rust-side contract, safe API, or oracle evidence; generated bindings alone are not sufficient for case-study selection.

## BindDrift Warning

- Warning: `W-000017`
- Drift type: `SignatureDrift`
- C symbol: `security_release_secctx`
- Risk: `Medium`
- Score: `10.0`
- Adjudicated label: `TRUE_SEMANTIC_DRIFT`
- Replay pair: `latest-p013-v6.13-to-v6.14`

## Evidence

The evidence above is copied from the ranked BindDrift warning report. The current artifact keeps this case within the warning/prioritization claim boundary.

## Impact

Historical warning from `v6.13` to `v6.14`.

## Lesson

Safe Rust APIs can depend on C-side contracts that are not represented in the Rust function signature. BindDrift makes that dependency explicit so maintainers can prioritize review.
