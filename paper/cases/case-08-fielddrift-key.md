# FieldDrift Case Study

## One-Line Summary

`key` produced `W-001019` because C-side contract evidence reaches Rust-for-Linux wrapper code.

## C-Side Change

BindDrift observed `FieldDrift` evidence for `key`.

- Old indicators/value: `[{'name': '_address', 'type': 'u8'}]`
- New indicators/value: `[{'name': 'usage', 'type': 'refcount_t'}, {'name': 'serial', 'type': 'key_serial_t'}, {'name': '__bindgen_anon_1', 'type': 'key__bindgen_ty_1'}, {'name': 'sem', 'type': 'rw_semaphore'}, {'name': 'user', 'type': '*mut key_user'}, {'name': 'security', 'type': '*mut core::ffi::c_void'}, {'name': '__bindgen_anon_2', 'type': 'key__bindgen_ty_2'}, {'name': 'last_used_at', 'type': 'time64_t'}, {'name': 'uid', 'type': 'kuid_t'}, {'name': 'gid', 'type': 'kgid_t'}, {'name': 'perm', 'type': 'key_perm_t'}, {'name': 'quotalen', 'type': 'core::ffi::c_ushort'}, {'name': 'datalen', 'type': 'core::ffi::c_ushort'}, {'name': 'state', 'type': 'core::ffi::c_short'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_3', 'type': 'key__bindgen_ty_3'}, {'name': '__bindgen_anon_4', 'type': 'key__bindgen_ty_4'}, {'name': 'restrict_link', 'type': '*mut key_restriction'}]`

## Rust-Side Dependency

The symbol is used through Rust binding calls or nearby wrapper code.

- No Rust-side evidence was attached to this warning.

## Why The Compiler Cannot Fully Catch It

This case is treated as a contract-review target. The type checker can validate the current call shape, but it does not verify that Rust wrapper assumptions about nullability, error representation, ownership, or context remain synchronized with C-side behavior.

## BindDrift Warning

- Warning: `W-001019`
- Drift type: `FieldDrift`
- C symbol: `key`
- Risk: `High`
- Score: `12.6`
- Oracle label: `UNLABELED`
- Replay pair: `replay-20260504T220545Z-p006-v6.6-to-v6.7`

## Evidence

The evidence above is copied from the ranked BindDrift warning report. The current artifact keeps this case within the warning/prioritization claim boundary.

## Impact

Historical warning from `v6.6` to `v6.7`.

## Lesson

Safe Rust APIs can depend on C-side contracts that are not represented in the Rust function signature. BindDrift makes that dependency explicit so maintainers can prioritize review.
