# Positive: SignatureDrift for `mdiobus_write`

## Summary

`mdiobus_write` produced `W-000003` and is included as an adjudicated positive review target with label `TRUE_WRAPPER_FIX`.

## Old Version Evidence

- Version: `v6.7`
- Old value or indicators: `absent`

## New Version Evidence

- Version: `v6.8`
- New value or indicators: `added`

## C-Side Diff

- Old indicators/value: `absent`
- New indicators/value: `added`

## Rust-Side Dependency

- `.binddrift/worktrees/v6.8/rust/kernel/net/phy.rs:202` in `Device::write`
- safe API `Device::write`
- `.binddrift/worktrees/v6.8/rust/kernel/net/phy.rs:198`: `// SAFETY: `phydev` is pointing to a valid object by the type invariant of `Self`.`
- `.binddrift/worktrees/v6.8/rust/kernel/net/phy.rs:201` error mapping `TO_RESULT_MAPPING`
- wrapper_fix: `b2e47002b2350f57bfa8fe1c231e9fbb6baef78b`

## Safe API / Contract Assumption

The warning reaches a public safe Rust API, so the maintainer review question is whether that API's documented contract remains synchronized with the C-side behavior.

## Manual Review Label

- Adjudicated label: `TRUE_WRAPPER_FIX`
- Reviewer 1: `TRUE_WRAPPER_FIX` -- mdiobus_write is added and reached by Device::write. The oracle hit is a Rust net::phy unified read/write API touching rust/kernel/net/phy.rs, plausibly addressing the same MDIO wrapper contract.
- Reviewer 2: `TRUE_WRAPPER_FIX` -- Later Rust wrapper/helper/binding evidence is in the same exposed API area and plausibly addresses the warned symbol or contract. C source evidence may be binding-only and no build log is present, so this is a wrapper-fix label, not build breakage.
- Adjudication: No build oracle. Rust net PHY code reaches mdiobus_write, and the unified C22/C45 read/write API fix in rust/kernel/net/phy.rs matches the same MDIO/PHY wrapper contract.

## Why This Is Not Generated-Binding-Only

The case has Rust reachability or contract/oracle evidence beyond a generated binding delta; generated-binding-only rows are excluded from positive case selection.

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

Review considered whether this was semantic drift; adjudication classifies it as wrapper-fix-backed validation instead of standalone semantic evidence.

## Maintainer Review Implication

A maintainer should inspect the Rust wrapper or safe abstraction path when carrying this C-side change across versions.

## Reproduction Pointers

- Warning: `W-000003`
- Warning UID: `46b1fb124f9b8010a0bbad8532aec2f2ce82c1cb9537c8e6d0662155e5c3b565`
- Replay pair: `latest-p007-v6.7-to-v6.8`
- Drift type: `SignatureDrift`
- C symbol: `mdiobus_write`
- Risk: `High`
- Score: `12.0`
