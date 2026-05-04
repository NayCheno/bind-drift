# OwnershipRefcountDrift Case Study

## One-Line Summary

`get_pid_ns` produced `W-004440` because C-side contract evidence reaches Rust-for-Linux wrapper code.

## C-Side Change

BindDrift observed `OwnershipRefcountDrift` evidence for `get_pid_ns`.

- Old indicators/value: `[]`
- New indicators/value: `['REFCOUNT_GET']`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.13/include/linux/pid_namespace.h:54`: `refcount_inc(&ns->ns.count);`

## Rust-Side Dependency

The symbol is used through Rust binding calls or nearby wrapper code.

- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.13/rust/kernel/pid_namespace.rs:51` in `inc_ref`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.13/rust/kernel/pid_namespace.rs:46`: `// SAFETY: Instances of `PidNamespace` are always reference-counted.`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.13/rust/kernel/pid_namespace.rs:50`: `// SAFETY: The existence of a shared reference means that the refcount is nonzero.`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.13/rust/kernel/pid_namespace.rs:51` lifetime fact `AS_PTR`

## Why The Compiler Cannot Fully Catch It

This case is treated as a contract-review target. The type checker can validate the current call shape, but it does not verify that Rust wrapper assumptions about nullability, error representation, ownership, or context remain synchronized with C-side behavior.

## BindDrift Warning

- Warning: `W-004440`
- Drift type: `OwnershipRefcountDrift`
- C symbol: `get_pid_ns`
- Risk: `High`
- Score: `13.0`
- Oracle label: `UNLABELED`
- Replay pair: `replay-20260504T224640Z-p007-v6.12-to-v6.13`

## Evidence

The evidence above is copied from the ranked BindDrift warning report. The current artifact keeps this case within the warning/prioritization claim boundary.

## Impact

Historical warning from `v6.12` to `v6.13`.

## Lesson

Safe Rust APIs can depend on C-side contracts that are not represented in the Rust function signature. BindDrift makes that dependency explicit so maintainers can prioritize review.
