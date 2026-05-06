# Positive: AllocationFreeDrift for `security_release_secctx`

## Summary

`security_release_secctx` produced `W-000017` and is included as an adjudicated positive review target with label `TRUE_SEMANTIC_DRIFT`.

## Old Version Evidence

- Version: `v6.13`
- Old value or indicators: `{'params': ['char *secdata', 'u32 seclen'], 'return_type': 'static inline void'}`

## New Version Evidence

- Version: `v6.14`
- New value or indicators: `{'params': ['struct lsm_context *cp'], 'return_type': 'static inline void'}`

## C-Side Diff

- Old indicators/value: `{'params': ['char *secdata', 'u32 seclen'], 'return_type': 'static inline void'}`
- New indicators/value: `{'params': ['struct lsm_context *cp'], 'return_type': 'static inline void'}`

## Rust-Side Dependency

- `.binddrift/worktrees/v6.14/rust/kernel/security.rs:68` in `drop`
- `.binddrift/worktrees/v6.14/rust/kernel/security.rs:65`: `// SAFETY: By the invariant of `Self`, this frees a context that came from a successful`

## Safe API / Contract Assumption

The warning reaches Rust code and should be reviewed as an evidence-backed target, not as an automatically confirmed defect.

## Manual Review Label

- Adjudicated label: `TRUE_SEMANTIC_DRIFT`
- Reviewer 1: `TRUE_SEMANTIC_DRIFT` -- Direct C signature changed from char pointer/length to lsm_context pointer, and Rust SecurityCtx Drop calls security_release_secctx inside an unsafe block with an invariant comment. The release/lifetime contract plausibly depends on the changed C API.
- Reviewer 2: `TRUE_SEMANTIC_DRIFT` -- Direct C signature changed from secdata/seclen release to struct lsm_context release, and SecurityCtx::drop calls it inside an unsafe wrapper with ownership/lifetime evidence. No build oracle, but the stale release contract is maintainer-reviewable.
- Adjudication: Direct C signature changed from secdata/seclen release to lsm_context, and SecurityCtx drop reaches it through an unsafe ownership path. No build or wrapper oracle, but the release contract reaches Rust.

## Why This Is Not Generated-Binding-Only

The case includes C-side source or indicator evidence plus Rust-side dependency evidence.

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

Review considered whether this was only signature churn or generated binding noise; adjudication kept it because C-side drift, Rust exposure, and contract dependence were all present.

## Maintainer Review Implication

A maintainer should inspect the Rust wrapper or safe abstraction path when carrying this C-side change across versions.

## Reproduction Pointers

- Warning: `W-000017`
- Warning UID: `b89f88bdf55082272dea6523f15128d491086ffe51f6e508731844462aa2de79`
- Replay pair: `latest-p013-v6.13-to-v6.14`
- Drift type: `AllocationFreeDrift`
- C symbol: `security_release_secctx`
- Risk: `Medium`
- Score: `10.0`
