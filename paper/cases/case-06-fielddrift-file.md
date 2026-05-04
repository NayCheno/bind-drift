# FieldDrift Case Study

## One-Line Summary

`file` produced `W-001012` because C-side contract evidence reaches Rust-for-Linux wrapper code.

## C-Side Change

BindDrift observed `FieldDrift` evidence for `file`.

- Old indicators/value: `[]`
- New indicators/value: `[{'name': '__bindgen_anon_1', 'type': 'file__bindgen_ty_1'}, {'name': 'f_lock', 'type': 'spinlock_t'}, {'name': 'f_mode', 'type': 'fmode_t'}, {'name': 'f_count', 'type': 'atomic_long_t'}, {'name': 'f_pos_lock', 'type': 'mutex'}, {'name': 'f_pos', 'type': 'loff_t'}, {'name': 'f_flags', 'type': 'core::ffi::c_uint'}, {'name': 'f_owner', 'type': 'fown_struct'}, {'name': 'f_cred', 'type': '*const cred'}, {'name': 'f_ra', 'type': 'file_ra_state'}, {'name': 'f_path', 'type': 'path'}, {'name': 'f_inode', 'type': '*mut inode'}, {'name': 'f_op', 'type': '*const file_operations'}, {'name': 'f_version', 'type': 'u64_'}, {'name': 'f_security', 'type': '*mut core::ffi::c_void'}, {'name': 'private_data', 'type': '*mut core::ffi::c_void'}, {'name': 'f_ep', 'type': '*mut hlist_head'}, {'name': 'f_mapping', 'type': '*mut address_space'}, {'name': 'f_wb_err', 'type': 'errseq_t'}, {'name': 'f_sb_err', 'type': 'errseq_t'}]`

## Rust-Side Dependency

The symbol is used through Rust binding calls or nearby wrapper code.

- No Rust-side evidence was attached to this warning.

## Why The Compiler Cannot Fully Catch It

This case is treated as a contract-review target. The type checker can validate the current call shape, but it does not verify that Rust wrapper assumptions about nullability, error representation, ownership, or context remain synchronized with C-side behavior.

## BindDrift Warning

- Warning: `W-001012`
- Drift type: `FieldDrift`
- C symbol: `file`
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
