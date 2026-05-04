# NullabilityDrift Case Study

## One-Line Summary

`dma_alloc_attrs` produced `W-000031` because C-side contract evidence reaches Rust-for-Linux wrapper code.

## C-Side Change

BindDrift observed `NullabilityDrift` evidence for `dma_alloc_attrs`.

- Old indicators/value: `[]`
- New indicators/value: `['NULL_RETURN']`
- `/home/nya/workspace/bind-drift/vendor/linux/include/linux/dma-mapping.h:266`: `return NULL;`

## Rust-Side Dependency

The symbol is used through Rust binding calls or nearby wrapper code.

- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/dma.rs:722` in `None`
- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/dma.rs:839` in `Coherent<T>::zeroed`
- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/dma.rs:1063` in `None`
- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/dma.rs:720`: `// SAFETY: Device pointer is guaranteed as valid by the type invariant on `Device`.`
- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/dma.rs:837`: `// SAFETY: Device pointer is guaranteed as valid by the type invariant on `Device`.`
- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/dma.rs:1061`: `// SAFETY: `dev.as_raw()` is valid by the type invariant on `device::Device`.`

## Why The Compiler Cannot Fully Catch It

This case is treated as a contract-review target. The type checker can validate the current call shape, but it does not verify that Rust wrapper assumptions about nullability, error representation, ownership, or context remain synchronized with C-side behavior.

## BindDrift Warning

- Warning: `W-000031`
- Drift type: `NullabilityDrift`
- C symbol: `dma_alloc_attrs`
- Risk: `High`
- Score: `14.0`

## Evidence

The evidence above is copied from the ranked BindDrift warning report. The current artifact keeps this case within the warning/prioritization claim boundary.

## Impact

Single-version review candidate: no historical baseline was available for this warning, so the artifact does not claim a confirmed drift bug.

## Lesson

Safe Rust APIs can depend on C-side contracts that are not represented in the Rust function signature. BindDrift makes that dependency explicit so maintainers can prioritize review.
