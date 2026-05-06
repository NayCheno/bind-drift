# Failure Analysis: NullabilityDrift for `device_add_disk`

## Summary

`device_add_disk` produced `W-000016` and is included as a negative/failure-analysis case with adjudicated label `FALSE_POSITIVE`.

## Old Version Evidence

- Version: `v6.12`
- Old value or indicators: `{'params': [{'name': 'parent', 'type': '*mut device'}, {'name': 'disk', 'type': '*mut gendisk'}, {'name': 'groups', 'type': '*mut *const attribute_group'}], 'return_type': 'core::ffi::c_int'}`

## New Version Evidence

- Version: `v6.13`
- New value or indicators: `{'params': [{'name': 'parent', 'type': '*mut device'}, {'name': 'disk', 'type': '*mut gendisk'}, {'name': 'groups', 'type': '*mut *const attribute_group'}], 'return_type': 'ffi::c_int'}`

## C-Side Diff

- Old indicators/value: `{'params': [{'name': 'parent', 'type': '*mut device'}, {'name': 'disk', 'type': '*mut gendisk'}, {'name': 'groups', 'type': '*mut *const attribute_group'}], 'return_type': 'core::ffi::c_int'}`
- New indicators/value: `{'params': [{'name': 'parent', 'type': '*mut device'}, {'name': 'disk', 'type': '*mut gendisk'}, {'name': 'groups', 'type': '*mut *const attribute_group'}], 'return_type': 'ffi::c_int'}`

## Rust-Side Dependency

- `.binddrift/worktrees/v6.13/rust/kernel/block/mq/gen_disk.rs:160` in `GenDiskBuilder::capacity_sectors`
- safe API `GenDiskBuilder::capacity_sectors`
- `.binddrift/worktrees/v6.13/rust/kernel/block/mq/gen_disk.rs:157`: `// SAFETY: `gendisk` points to a valid and initialized instance of`
- `.binddrift/worktrees/v6.13/rust/kernel/block/mq/gen_disk.rs:156` error mapping `TO_RESULT_MAPPING`
- wrapper_fix: `0c5928deada15a8d075516e6e0d9ee19011bb000`

## Safe API / Contract Assumption

The warning reaches a public safe Rust API, so the maintainer review question is whether that API's documented contract remains synchronized with the C-side behavior.

## Manual Review Label

- Adjudicated label: `FALSE_POSITIVE`
- Reviewer 1: `BENIGN_DRIFT` -- device_add_disk evidence shows only core::ffi to ffi type spelling changes. Rust GenDiskBuilder exposure is real, but the oracle hit is documentation formatting and no changed API contract is shown.
- Reviewer 2: `FALSE_POSITIVE` -- The packet shows generated binding churn or a namespace/type-alias-only change rather than supported C contract drift. Wrapper evidence is absent or not tied to the claimed drift, so the warning is not supported.
- Adjudication: The old/new evidence for device_add_disk is only type-path or namespace churn such as core::ffi to ffi, with no supported C contract drift or direct same-drift wrapper fix.

## Why This Is Not Generated-Binding-Only

The case has Rust reachability or contract/oracle evidence beyond a generated binding delta; generated-binding-only rows are excluded from positive case selection.

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

Review considered whether the warning should be promoted, but adjudication found the evidence benign, unsupported, or incomplete.

## Maintainer Review Implication

This case documents why similar high-scoring warnings need manual review before being counted as true positives.

## Reproduction Pointers

- Warning: `W-000016`
- Warning UID: `fd7adb7aa151991c0fadce9167e16b157fdd69559e3aaba40a8ec27f668cded0`
- Replay pair: `latest-p012-v6.12-to-v6.13`
- Drift type: `NullabilityDrift`
- C symbol: `device_add_disk`
- Risk: `Medium`
- Score: `11.0`
