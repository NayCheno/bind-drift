# SignatureDrift Case Study

## One-Line Summary

`mdiobus_read` produced `W-000004` with adjudicated true-positive oracle evidence.

## Old Version Evidence

- Version: `v6.14`
- Old value or indicators: `{'params': ['phydev->mdio.bus', 'addr', 'regnum'], 'return_type': 'return'}`

## New Version Evidence

- Version: `v6.15`
- New value or indicators: `{'params': ['phydev->mdio.bus', 'phydev->mdio.addr', 'regnum'], 'return_type': 'return'}`

## C-Side Diff Or Indicator Change

BindDrift observed `SignatureDrift` evidence for `mdiobus_read`.

- Old indicators/value: `{'params': ['phydev->mdio.bus', 'addr', 'regnum'], 'return_type': 'return'}`
- New indicators/value: `{'params': ['phydev->mdio.bus', 'phydev->mdio.addr', 'regnum'], 'return_type': 'return'}`

## Rust Wrapper Or Safe API Dependency

BindDrift attached the following Rust impact evidence.

- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.15/rust/kernel/net/phy/reg.rs:111` in `read`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.15/rust/kernel/net/phy/reg.rs:107`: `// SAFETY: `phydev` is pointing to a valid object by the type invariant of `Device`.`
- `/home/nya/workspace/bind-drift/.binddrift/worktrees/v6.15/rust/kernel/net/phy/reg.rs:113` error mapping `TO_RESULT_MAPPING`
- wrapper_fix: `b2e47002b2350f57bfa8fe1c231e9fbb6baef78b`

## Reviewer Adjudicated Label

The adjudicated review label is `TRUE_WRAPPER_FIX`.

## Why The Compiler Cannot Fully Catch It

This case is treated as a contract-review target. The type checker can validate the current call shape, but it does not verify that Rust wrapper assumptions about nullability, error representation, ownership, or context remain synchronized with C-side behavior.

## Why This Is Not Generated-Binding-Only

This case includes C-side source or indicator evidence plus Rust-side contract, safe API, or oracle evidence; generated bindings alone are not sufficient for case-study selection.

## BindDrift Warning

- Warning: `W-000004`
- Drift type: `SignatureDrift`
- C symbol: `mdiobus_read`
- Risk: `High`
- Score: `15.0`
- Adjudicated label: `TRUE_WRAPPER_FIX`
- Replay pair: `latest-p014-v6.14-to-v6.15`

## Evidence

The evidence above is copied from the ranked BindDrift warning report. The current artifact keeps this case within the warning/prioritization claim boundary.

## Impact

Historical warning from `v6.14` to `v6.15`.

## Lesson

Safe Rust APIs can depend on C-side contracts that are not represented in the Rust function signature. BindDrift makes that dependency explicit so maintainers can prioritize review.
