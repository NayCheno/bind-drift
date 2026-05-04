# SleepabilityDrift Case Study

## One-Line Summary

`clk_prepare` produced `W-001100` because C-side contract evidence reaches Rust-for-Linux wrapper code.

## C-Side Change

BindDrift observed `SleepabilityDrift` evidence for `clk_prepare`.

- Old indicators/value: `[]`
- New indicators/value: `['MAY_SLEEP']`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/clk.h:330`: `might_sleep();`

## Rust-Side Dependency

The symbol is used through Rust binding calls or nearby wrapper code.

- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:188` in `Clk::prepare`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:183`: `/// [`clk_prepare`]: https://docs.kernel.org/core-api/kernel-api.html#c.clk_prepare`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:186`: `// SAFETY: By the type invariants, self.as_raw() is a valid argument for`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:191`: `/// Unprepare the clock.`

## Why The Compiler Cannot Fully Catch It

This case is treated as a contract-review target. The type checker can validate the current call shape, but it does not verify that Rust wrapper assumptions about nullability, error representation, ownership, or context remain synchronized with C-side behavior.

## BindDrift Warning

- Warning: `W-001100`
- Drift type: `SleepabilityDrift`
- C symbol: `clk_prepare`
- Risk: `High`
- Score: `11.2`
- Oracle label: `UNLABELED`
- Replay pair: `replay-20260504T224640Z-p010-v6.15-to-v6.16`

## Evidence

The evidence above is copied from the ranked BindDrift warning report. The current artifact keeps this case within the warning/prioritization claim boundary.

## Impact

Historical warning from `v6.15` to `v6.16`.

## Lesson

Safe Rust APIs can depend on C-side contracts that are not represented in the Rust function signature. BindDrift makes that dependency explicit so maintainers can prioritize review.
