# Positive: SleepabilityContextDrift for `fsleep`

## Summary

`fsleep` produced `W-000002` and is included as an adjudicated positive review target with label `TRUE_WRAPPER_FIX`.

## Old Version Evidence

- Version: `v6.16`
- Old value or indicators: `absent`

## New Version Evidence

- Version: `v6.17`
- New value or indicators: `added`

## C-Side Diff

- Old indicators/value: `absent`
- New indicators/value: `added`

## Rust-Side Dependency

- `.binddrift/worktrees/v6.17/rust/kernel/time/delay.rs:47` in `fsleep`
- safe API `fsleep`
- `.binddrift/worktrees/v6.17/rust/kernel/time/delay.rs:42`: `// SAFETY: It is always safe to call `fsleep()` with any duration.`
- wrapper_fix: `d4b29ddf82a458935f1bd4909b8a7a13df9d3bdc`

## Safe API / Contract Assumption

The warning reaches a public safe Rust API, so the maintainer review question is whether that API's documented contract remains synchronized with the C-side behavior.

## Manual Review Label

- Adjudicated label: `TRUE_WRAPPER_FIX`
- Reviewer 1: `TRUE_WRAPPER_FIX` -- The wrapper-fix oracle is direct: the fsleep wrapper commit matches fsleep and changes Rust time helper/wrapper files. Rust exposes a public fsleep API over bindings::fsleep, so this is a valid wrapper-fix target.
- Reviewer 2: `TRUE_WRAPPER_FIX` -- A later Rust time commit specifically adds the fsleep helper and Rust wrapper. That directly addresses the warned symbol and Rust safe API path. The evidence does not show a build failure, and C drift is only symbol-level.
- Adjudication: The Rust fsleep API calls bindings::fsleep, and the oracle commit specifically adds the fsleep Rust helper/wrapper in rust/helpers/time.c and rust/kernel/time/delay.rs. C evidence is binding-level only, but the wrapper-fix path is direct.

## Why This Is Not Generated-Binding-Only

The case has Rust reachability or contract/oracle evidence beyond a generated binding delta; generated-binding-only rows are excluded from positive case selection.

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

Review considered whether this was semantic drift; adjudication classifies it as wrapper-fix-backed validation instead of standalone semantic evidence.

## Maintainer Review Implication

A maintainer should inspect the Rust wrapper or safe abstraction path when carrying this C-side change across versions.

## Reproduction Pointers

- Warning: `W-000002`
- Warning UID: `6f343849efc7e34b3800ce1b64b2de12eed139f23a9af2df211b2362dac2fa63`
- Replay pair: `latest-p016-v6.16-to-v6.17`
- Drift type: `SleepabilityContextDrift`
- C symbol: `fsleep`
- Risk: `Low`
- Score: `7.0`
