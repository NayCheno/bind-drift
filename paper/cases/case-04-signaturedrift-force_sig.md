# SignatureDrift Case Study

## One-Line Summary

`force_sig` produced `W-000353` because C-side contract evidence reaches Rust-for-Linux wrapper code.

## C-Side Change

BindDrift observed `SignatureDrift` evidence for `force_sig`.

- Old indicators/value: `absent`
- New indicators/value: `added`

## Rust-Side Dependency

The symbol is used through Rust binding calls or nearby wrapper code.

- No Rust-side evidence was attached to this warning.

## Why The Compiler Cannot Fully Catch It

This case is treated as a contract-review target. The type checker can validate the current call shape, but it does not verify that Rust wrapper assumptions about nullability, error representation, ownership, or context remain synchronized with C-side behavior.

## BindDrift Warning

- Warning: `W-000353`
- Drift type: `SignatureDrift`
- C symbol: `force_sig`
- Risk: `High`
- Score: `12.8`
- Oracle label: `UNLABELED`
- Replay pair: `replay-20260504T220545Z-p006-v6.6-to-v6.7`

## Evidence

The evidence above is copied from the ranked BindDrift warning report. The current artifact keeps this case within the warning/prioritization claim boundary.

## Impact

Historical warning from `v6.6` to `v6.7`.

## Lesson

Safe Rust APIs can depend on C-side contracts that are not represented in the Rust function signature. BindDrift makes that dependency explicit so maintainers can prioritize review.
