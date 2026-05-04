# AllocationFreePairingDrift Case Study

## One-Line Summary

`auxiliary_device_uninit` produced `W-001093` because C-side contract evidence reaches Rust-for-Linux wrapper code.

## C-Side Change

BindDrift observed `AllocationFreePairingDrift` evidence for `auxiliary_device_uninit`.

- Old indicators/value: `[]`
- New indicators/value: `['FREE', 'REFCOUNT_PUT']`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/auxiliary_bus.h:241`: `mutex_destroy(&auxdev->sysfs.lock);`

## Rust-Side Dependency

The symbol is used through Rust binding calls or nearby wrapper code.

- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/auxiliary.rs:331` in `Registration::new`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/auxiliary.rs:354` in `drop`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/auxiliary.rs:329`: `// SAFETY: `adev` is guaranteed to be a valid pointer to a `struct auxiliary_device`,`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/auxiliary.rs:336`: `// SAFETY: `adev` is guaranteed to be non-null, since the `KBox` was allocated successfully.`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/auxiliary.rs:352`: `// SAFETY: By the type invariant of `Self`, `self.0.as_ptr()` is a valid registered`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/auxiliary.rs:352` lifetime fact `AS_PTR`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/auxiliary.rs:354` lifetime fact `AS_PTR`

## Why The Compiler Cannot Fully Catch It

This case is treated as a contract-review target. The type checker can validate the current call shape, but it does not verify that Rust wrapper assumptions about nullability, error representation, ownership, or context remain synchronized with C-side behavior.

## BindDrift Warning

- Warning: `W-001093`
- Drift type: `AllocationFreePairingDrift`
- C symbol: `auxiliary_device_uninit`
- Risk: `High`
- Score: `13.7`
- Oracle label: `UNLABELED`
- Replay pair: `replay-20260504T224640Z-p010-v6.15-to-v6.16`

## Evidence

The evidence above is copied from the ranked BindDrift warning report. The current artifact keeps this case within the warning/prioritization claim boundary.

## Impact

Historical warning from `v6.15` to `v6.16`.

## Lesson

Safe Rust APIs can depend on C-side contracts that are not represented in the Rust function signature. BindDrift makes that dependency explicit so maintainers can prioritize review.
