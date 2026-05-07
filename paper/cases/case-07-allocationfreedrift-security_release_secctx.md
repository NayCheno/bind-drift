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

- exposure `GENERATED_FROM`: `CFunction:security_release_secctx` -> `RustBindingFunction:security_release_secctx`
- exposure `HAS_SAFETY_COMMENT`: `RustBindingFunction:security_release_secctx` -> `RustSafetyComment:.binddrift/worktrees/v6.14/rust/kernel/security.rs:65`
- exposure `CALLS_BINDING`: `RustBindingFunction:security_release_secctx` -> `RustUnsafeCall:.binddrift/worktrees/v6.14/rust/kernel/security.rs:68:security_release_secctx`
- `.binddrift/worktrees/v6.14/rust/kernel/security.rs:68` in `drop` (unsafe block)
- `.binddrift/worktrees/v6.14/rust/kernel/security.rs:65`: `// SAFETY: By the invariant of `Self`, this frees a context that came from a successful`

## Safe API / Contract Assumption

The warning reaches Rust code and should be reviewed as an evidence-backed target, not as an automatically confirmed defect.

## Manual Review Label

- Adjudicated label: `TRUE_SEMANTIC_DRIFT`
- Reviewer 1: `TRUE_SEMANTIC_DRIFT` -- Real C-side SignatureDrift plus reachable Rust wrapper/API/safety evidence supports plausible stale Rust contract impact for security_release_secctx.
- Reviewer 2: `TRUE_SEMANTIC_DRIFT` -- Calibration marks a semantic candidate without oracle evidence.
- Adjudication: Semantic-candidate calibration is present without wrapper/build oracle; adjudicated TRUE_SEMANTIC_DRIFT per v3 policy.

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
