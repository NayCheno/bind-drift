# Positive: SleepabilityContextDrift for `__mutex_init`

## Summary

`__mutex_init` produced `W-000001` and is included as an adjudicated positive review target with label `TRUE_WRAPPER_FIX`.

## Old Version Evidence

- Version: `v6.11`
- Old value or indicators: `{'params': [{'name': 'lock', 'type': '*mut mutex'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'key', 'type': '*mut lock_class_key'}], 'return_type': '()'}`

## New Version Evidence

- Version: `v6.12`
- New value or indicators: `{'params': [{'name': 'mutex', 'type': '*mut mutex'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'key', 'type': '*mut lock_class_key'}], 'return_type': '()'}`

## C-Side Diff

- Old indicators/value: `{'params': [{'name': 'lock', 'type': '*mut mutex'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'key', 'type': '*mut lock_class_key'}], 'return_type': '()'}`
- New indicators/value: `{'params': [{'name': 'mutex', 'type': '*mut mutex'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'key', 'type': '*mut lock_class_key'}], 'return_type': '()'}`

## Rust-Side Dependency

- exposure `GENERATED_FROM`: `CFunction:__mutex_init` -> `RustBindingFunction:__mutex_init`
- exposure `HAS_SAFETY_COMMENT`: `RustBindingFunction:__mutex_init` -> `RustSafetyComment:.binddrift/worktrees/v6.12/rust/kernel/sync/lock/mutex.rs:102`
- exposure `CALLS_BINDING`: `RustBindingFunction:__mutex_init` -> `RustUnsafeCall:.binddrift/worktrees/v6.12/rust/kernel/sync/lock/mutex.rs:104:__mutex_init`
- `.binddrift/worktrees/v6.12/rust/kernel/sync/lock/mutex.rs:104` in `example` (unsafe block)
- `.binddrift/worktrees/v6.12/rust/kernel/sync/lock/mutex.rs:102`: `// SAFETY: The safety requirements ensure that `ptr` is valid for writes, and `name` and`
- wrapper_fix: `d065cc76054d21e48a839a2a19ba99dbc51a4d11`

## Safe API / Contract Assumption

The warning is connected to later Rust wrapper/helper evidence and is reported separately from semantic-only drift.

## Manual Review Label

- Adjudicated label: `TRUE_WRAPPER_FIX`
- Reviewer 1: `TRUE_WRAPPER_FIX` -- Packet reports a direct same-symbol Rust wrapper/helper/binding fix for __mutex_init.
- Reviewer 2: `TRUE_WRAPPER_FIX` -- Same-symbol wrapper oracle matched before lower-priority rules.
- Adjudication: Direct same-symbol wrapper oracle is present; adjudicated TRUE_WRAPPER_FIX per v3 policy.

## Why This Is Not Generated-Binding-Only

The case has Rust reachability or contract/oracle evidence beyond a generated binding delta; generated-binding-only rows are excluded from positive case selection.

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

Review considered whether this was semantic drift; adjudication classifies it as wrapper-fix-backed validation instead of standalone semantic evidence.

## Maintainer Review Implication

A maintainer should inspect the Rust wrapper or safe abstraction path when carrying this C-side change across versions.

## Reproduction Pointers

- Warning: `W-000001`
- Warning UID: `5bdc46821e9ba95cda0154dcb8f39973f1121cf83b337b0c1249880a16419fe4`
- Replay pair: `latest-p011-v6.11-to-v6.12`
- Drift type: `SleepabilityContextDrift`
- C symbol: `__mutex_init`
- Risk: `Medium`
- Score: `8.0`
