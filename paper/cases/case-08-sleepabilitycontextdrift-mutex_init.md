# Positive: SleepabilityContextDrift for `__mutex_init`

## Summary

`__mutex_init` produced `W-000001` and is included as an adjudicated positive review target with label `TRUE_BUILD_BREAKAGE`.

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

- `.binddrift/worktrees/v6.12/rust/kernel/sync/lock/mutex.rs:104` in `example`
- `.binddrift/worktrees/v6.12/rust/kernel/sync/lock/mutex.rs:102`: `// SAFETY: The safety requirements ensure that `ptr` is valid for writes, and `name` and`
- wrapper_fix: `d065cc76054d21e48a839a2a19ba99dbc51a4d11`

## Safe API / Contract Assumption

The warning is connected to later Rust wrapper/helper evidence and is reported separately from semantic-only drift.

## Manual Review Label

- Adjudicated label: `TRUE_BUILD_BREAKAGE`
- Reviewer 1: `TRUE_WRAPPER_FIX` -- __mutex_init has a parameter-name binding drift and reaches Rust mutex initialization. Commit d065cc76054d directly adds rust_helper___mutex_init for PREEMPT_RT, matching the symbol and helper path.
- Reviewer 2: `TRUE_BUILD_BREAKAGE` -- The later mutex helper commit includes an explicit PREEMPT_RT build error for bindings::__mutex_init and adds rust_helper___mutex_init. That connects the warning symbol to objective build breakage.
- Adjudication: Reviewer 2 cites explicit E0425 build-error evidence for bindings::__mutex_init in rust/kernel/sync/lock/mutex.rs, and the packet has the same-symbol PREEMPT_RT helper fix in rust/helpers/mutex.c. Build breakage takes priority over the wrapper-fix label.

## Why This Is Not Generated-Binding-Only

The case has Rust reachability or contract/oracle evidence beyond a generated binding delta; generated-binding-only rows are excluded from positive case selection.

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

Review considered whether this was a soft contract warning; adjudication uses build evidence as the stronger label.

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
