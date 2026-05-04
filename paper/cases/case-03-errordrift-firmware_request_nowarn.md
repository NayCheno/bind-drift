# ErrorDrift Case Study

## One-Line Summary

`firmware_request_nowarn` produced `W-000602` because C-side contract evidence reaches Rust-for-Linux wrapper code.

## C-Side Change

BindDrift observed `ErrorDrift` evidence for `firmware_request_nowarn`.

- Old indicators/value: `[]`
- New indicators/value: `['ERROR_CODE']`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/include/linux/firmware.h:142`: `return -EINVAL;`

## Rust-Side Dependency

The symbol is used through Rust binding calls or nearby wrapper code.

- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:12` in `None`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:24` in `request_nowarn`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:80` in `Firmware::request`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:28`: `/// Abstraction around a C `struct firmware`.`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:29`: `///`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:79`: `/// Send a request for an optional firmware module. See also`

## Why The Compiler Cannot Fully Catch It

This case is treated as a contract-review target. The type checker can validate the current call shape, but it does not verify that Rust wrapper assumptions about nullability, error representation, ownership, or context remain synchronized with C-side behavior.

## BindDrift Warning

- Warning: `W-000602`
- Drift type: `ErrorDrift`
- C symbol: `firmware_request_nowarn`
- Risk: `High`
- Score: `11.45`
- Oracle label: `UNLABELED`
- Replay pair: `replay-20260504T224640Z-p005-v6.10-to-v6.11`

## Evidence

The evidence above is copied from the ranked BindDrift warning report. The current artifact keeps this case within the warning/prioritization claim boundary.

## Impact

Historical warning from `v6.10` to `v6.11`.

## Lesson

Safe Rust APIs can depend on C-side contracts that are not represented in the Rust function signature. BindDrift makes that dependency explicit so maintainers can prioritize review.
