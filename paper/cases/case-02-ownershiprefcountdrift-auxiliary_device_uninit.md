# OwnershipRefcountDrift Case Study

## One-Line Summary

`auxiliary_device_uninit` produced `W-000004` because C-side contract evidence reaches Rust-for-Linux wrapper code.

## C-Side Change

BindDrift observed `OwnershipRefcountDrift` evidence for `auxiliary_device_uninit`.

- Old indicators/value: `[]`
- New indicators/value: `['FREE', 'REFCOUNT_PUT']`
- `/home/nya/workspace/bind-drift/vendor/linux/include/linux/auxiliary_bus.h:242`: `put_device(&auxdev->dev);`

## Rust-Side Dependency

The symbol is used through Rust binding calls or nearby wrapper code.

- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/auxiliary.rs:377` in `None`
- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/auxiliary.rs:404` in `drop`
- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/auxiliary.rs:375`: `// SAFETY: `adev` is guaranteed to be a valid pointer to a`
- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/auxiliary.rs:402`: `// SAFETY: By the type invariant of `Self`, `self.0.as_ptr()` is a valid registered`
- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/auxiliary.rs:408`: `// SAFETY: A `Registration` of a `struct auxiliary_device` can be released from any thread.`
- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/auxiliary.rs:402` lifetime fact `AS_PTR`
- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/auxiliary.rs:404` lifetime fact `AS_PTR`

## Why The Compiler Cannot Fully Catch It

This case is treated as a contract-review target. The type checker can validate the current call shape, but it does not verify that Rust wrapper assumptions about nullability, error representation, ownership, or context remain synchronized with C-side behavior.

## BindDrift Warning

- Warning: `W-000004`
- Drift type: `OwnershipRefcountDrift`
- C symbol: `auxiliary_device_uninit`
- Risk: `High`
- Score: `13.7`

## Evidence

The evidence above is copied from the ranked BindDrift warning report. The current artifact keeps this case within the warning/prioritization claim boundary.

## Impact

Single-version review candidate: no historical baseline was available for this warning, so the artifact does not claim a confirmed drift bug.

## Lesson

Safe Rust APIs can depend on C-side contracts that are not represented in the Rust function signature. BindDrift makes that dependency explicit so maintainers can prioritize review.
