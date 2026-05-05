# Positive: NullabilityDrift for `mdiobus_write`

## Summary

`mdiobus_write` produced `W-000005` and is included as an adjudicated positive review target with label `TRUE_WRAPPER_FIX`.

## Old Version Evidence

- Version: `v6.14`
- Old value or indicators: `{'params': ['phydev->mdio.bus', 'addr', 'regnum', 'val'], 'return_type': 'return'}`

## New Version Evidence

- Version: `v6.15`
- New value or indicators: `{'params': ['phydev->mdio.bus', 'phydev->mdio.addr', 'regnum', 'val'], 'return_type': 'return'}`

## C-Side Diff

- Old indicators/value: `{'params': ['phydev->mdio.bus', 'addr', 'regnum', 'val'], 'return_type': 'return'}`
- New indicators/value: `{'params': ['phydev->mdio.bus', 'phydev->mdio.addr', 'regnum', 'val'], 'return_type': 'return'}`

## Rust-Side Dependency

- `.binddrift/worktrees/v6.15/rust/kernel/net/phy/reg.rs:123` in `write`
- `.binddrift/worktrees/v6.15/rust/kernel/net/phy/reg.rs:119`: `// SAFETY: `phydev` is pointing to a valid object by the type invariant of `Device`.`
- `.binddrift/worktrees/v6.15/rust/kernel/net/phy/reg.rs:122` error mapping `TO_RESULT_MAPPING`
- wrapper_fix: `b2e47002b2350f57bfa8fe1c231e9fbb6baef78b`

## Safe API / Contract Assumption

The warning reaches Rust error-mapping code, so the review question is whether the C return convention still matches Rust Result/Error handling.

## Manual Review Label

- Adjudicated label: `TRUE_WRAPPER_FIX`
- Reviewer 1: `TRUE_WRAPPER_FIX` -- The C-side drift shows changed mdiobus_write call contract in the phy path, and Rust exposure is an unsafe wrapper with error mapping. The oracle directly matches mdiobus_write and the net::phy read/write API fix in Rust phy files.
- Reviewer 2: `TRUE_WRAPPER_FIX` -- Concrete C evidence shows mdiobus_write call arguments changing from addr to phydev->mdio.addr. Rust net/phy/reg.rs reaches the helper, and b2e47002b235 changes that same Rust file for unified read/write APIs while matching mdiobus_write.
- Adjudication: b2e47002b235 directly changes rust/kernel/net/phy/reg.rs and the net::phy read/write API while matching mdiobus_write. Rust exposure is an unsafe wrapper with error mapping. The C evidence shows the MDIO address argument source changing, so wrapper-fix is the supported priority label.

## Why This Is Not Generated-Binding-Only

The case includes C-side source or indicator evidence plus Rust-side dependency evidence.

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

Review considered whether this was semantic drift; adjudication classifies it as wrapper-fix-backed validation instead of standalone semantic evidence.

## Maintainer Review Implication

A maintainer should inspect the Rust wrapper or safe abstraction path when carrying this C-side change across versions.

## Reproduction Pointers

- Warning: `W-000005`
- Warning UID: `a43f69159ca0eea7926e237192cc664924f3b30281339f73fecb06be4a8d8bb8`
- Replay pair: `latest-p014-v6.14-to-v6.15`
- Drift type: `NullabilityDrift`
- C symbol: `mdiobus_write`
- Risk: `High`
- Score: `19.0`
