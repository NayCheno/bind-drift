# Positive: AllocationFreeDrift for `firmware_request_nowarn`

## Summary

`firmware_request_nowarn` produced `W-000019` and is included as an adjudicated positive review target with label `TRUE_WRAPPER_FIX`.

## Old Version Evidence

- Version: `v6.12`
- Old value or indicators: `{'params': [{'name': 'fw', 'type': '*mut *const firmware'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'device', 'type': '*mut device'}], 'return_type': 'core::ffi::c_int'}`

## New Version Evidence

- Version: `v6.13`
- New value or indicators: `{'params': [{'name': 'fw', 'type': '*mut *const firmware'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'device', 'type': '*mut device'}], 'return_type': 'ffi::c_int'}`

## C-Side Diff

- Old indicators/value: `{'params': [{'name': 'fw', 'type': '*mut *const firmware'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'device', 'type': '*mut device'}], 'return_type': 'core::ffi::c_int'}`
- New indicators/value: `{'params': [{'name': 'fw', 'type': '*mut *const firmware'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'device', 'type': '*mut device'}], 'return_type': 'ffi::c_int'}`

## Rust-Side Dependency

- `.binddrift/worktrees/v6.13/rust/kernel/firmware.rs:24` in `request_nowarn`
- `.binddrift/worktrees/v6.13/rust/kernel/firmware.rs:28`: `/// Abstraction around a C `struct firmware`.`
- `.binddrift/worktrees/v6.13/rust/kernel/firmware.rs:29`: `///`
- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`

## Safe API / Contract Assumption

The warning is connected to later Rust wrapper/helper evidence and is reported separately from semantic-only drift.

## Manual Review Label

- Adjudicated label: `TRUE_WRAPPER_FIX`
- Reviewer 1: `TRUE_WRAPPER_FIX` -- firmware_request_nowarn is reached from the Firmware request wrapper. The oracle hit fixes a soundness issue in request_internal in rust/kernel/firmware.rs, plausibly addressing the same firmware request contract.
- Reviewer 2: `FALSE_POSITIVE` -- The packet shows generated binding churn or a namespace/type-alias-only change rather than supported C contract drift. Wrapper evidence is absent or not tied to the claimed drift, so the warning is not supported.
- Adjudication: No build oracle. request_nowarn reaches the firmware request path, and the oracle fixes request_internal soundness in rust/kernel/firmware.rs, the same Rust exposure path.

## Why This Is Not Generated-Binding-Only

The case has Rust reachability or contract/oracle evidence beyond a generated binding delta; generated-binding-only rows are excluded from positive case selection.

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

Review considered whether this was semantic drift; adjudication classifies it as wrapper-fix-backed validation instead of standalone semantic evidence.

## Maintainer Review Implication

A maintainer should inspect the Rust wrapper or safe abstraction path when carrying this C-side change across versions.

## Reproduction Pointers

- Warning: `W-000019`
- Warning UID: `a7b50f9e01fa519b3ca5429567469093b01a1a6e6aac05980f9c6eb72628692a`
- Replay pair: `latest-p012-v6.12-to-v6.13`
- Drift type: `AllocationFreeDrift`
- C symbol: `firmware_request_nowarn`
- Risk: `Low`
- Score: `4.0`
