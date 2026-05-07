# Positive: AllocationFreeDrift for `dma_free_attrs`

## Summary

`dma_free_attrs` produced `W-000004` and is included as an adjudicated positive review target with label `TRUE_SEMANTIC_DRIFT`.

## Old Version Evidence

- Version: `v6.19`
- Old value or indicators: `{'params': ['struct device *dev', 'size_t size', 'void *cpu_addr', 'dma_addr_t dma_handle', 'unsigned long attrs'], 'return_type': 'static void'}`

## New Version Evidence

- Version: `v7.0`
- New value or indicators: `{'params': ['struct device *dev', 'size_t size', 'void *cpu_addr', 'dma_addr_t dma_handle', 'unsigned long attrs'], 'return_type': 'static inline void'}`

## C-Side Diff

- Old indicators/value: `{'params': ['struct device *dev', 'size_t size', 'void *cpu_addr', 'dma_addr_t dma_handle', 'unsigned long attrs'], 'return_type': 'static void'}`
- New indicators/value: `{'params': ['struct device *dev', 'size_t size', 'void *cpu_addr', 'dma_addr_t dma_handle', 'unsigned long attrs'], 'return_type': 'static inline void'}`

## Rust-Side Dependency

- exposure `GENERATED_FROM`: `CFunction:dma_free_attrs` -> `RustBindingFunction:dma_free_attrs`
- exposure `HAS_SAFETY_COMMENT`: `RustBindingFunction:dma_free_attrs` -> `RustSafetyComment:.binddrift/worktrees/v7.0/rust/kernel/dma.rs:648`
- exposure `CALLS_BINDING`: `RustBindingFunction:dma_free_attrs` -> `RustUnsafeCall:.binddrift/worktrees/v7.0/rust/kernel/dma.rs:652:dma_free_attrs`
- `.binddrift/worktrees/v7.0/rust/kernel/dma.rs:652` in `drop` (unsafe block)
- `.binddrift/worktrees/v7.0/rust/kernel/dma.rs:648`: `// SAFETY: Device pointer is guaranteed as valid by the type invariant on `Device`.`

## Safe API / Contract Assumption

The warning reaches Rust code and should be reviewed as an evidence-backed target, not as an automatically confirmed defect.

## Manual Review Label

- Adjudicated label: `TRUE_SEMANTIC_DRIFT`
- Reviewer 1: `TRUE_SEMANTIC_DRIFT` -- Real C-side SignatureDrift plus reachable Rust wrapper/API/safety evidence supports plausible stale Rust contract impact for dma_free_attrs.
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

- Warning: `W-000004`
- Warning UID: `c4edd1024dd2d95c013e77ab1f56971125358b9c202731c97e2b15c3855c5e09`
- Replay pair: `latest-p019-v6.19-to-v7.0`
- Drift type: `AllocationFreeDrift`
- C symbol: `dma_free_attrs`
- Risk: `Medium`
- Score: `10.0`
