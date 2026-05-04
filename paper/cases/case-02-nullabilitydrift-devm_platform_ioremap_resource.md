# NullabilityDrift Case Study

## One-Line Summary

`devm_platform_ioremap_resource` produced `W-000850` because C-side contract evidence reaches Rust-for-Linux wrapper code.

## C-Side Change

BindDrift observed `NullabilityDrift` evidence for `devm_platform_ioremap_resource`.

- Old indicators/value: `[]`
- New indicators/value: `['ERROR_CODE', 'ERR_PTR_RETURN']`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/include/linux/platform_device.h:91`: `return ERR_PTR(-EINVAL);`

## Rust-Side Dependency

The symbol is used through Rust binding calls or nearby wrapper code.

- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:283` in `From<core::convert::Infallible>::to_result`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:278`: `///     pdev: &mut PlatformDevice,`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:279`: `///     index: u32,`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:280`: `/// ) -> Result<*mut kernel::ffi::c_void> {`

## Why The Compiler Cannot Fully Catch It

This case is treated as a contract-review target. The type checker can validate the current call shape, but it does not verify that Rust wrapper assumptions about nullability, error representation, ownership, or context remain synchronized with C-side behavior.

## BindDrift Warning

- Warning: `W-000850`
- Drift type: `NullabilityDrift`
- C symbol: `devm_platform_ioremap_resource`
- Risk: `High`
- Score: `13.2`
- Oracle label: `UNLABELED`
- Replay pair: `replay-20260504T224640Z-p008-v6.13-to-v6.14`

## Evidence

The evidence above is copied from the ranked BindDrift warning report. The current artifact keeps this case within the warning/prioritization claim boundary.

## Impact

Historical warning from `v6.13` to `v6.14`.

## Lesson

Safe Rust APIs can depend on C-side contracts that are not represented in the Rust function signature. BindDrift makes that dependency explicit so maintainers can prioritize review.
