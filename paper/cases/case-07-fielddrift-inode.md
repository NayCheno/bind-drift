# FieldDrift Case Study

## One-Line Summary

`inode` produced `W-001016` because C-side contract evidence reaches Rust-for-Linux wrapper code.

## C-Side Change

BindDrift observed `FieldDrift` evidence for `inode`.

- Old indicators/value: `[]`
- New indicators/value: `[{'name': 'i_mode', 'type': 'umode_t'}, {'name': 'i_opflags', 'type': 'core::ffi::c_ushort'}, {'name': 'i_uid', 'type': 'kuid_t'}, {'name': 'i_gid', 'type': 'kgid_t'}, {'name': 'i_flags', 'type': 'core::ffi::c_uint'}, {'name': 'i_acl', 'type': '*mut posix_acl'}, {'name': 'i_default_acl', 'type': '*mut posix_acl'}, {'name': 'i_op', 'type': '*const inode_operations'}, {'name': 'i_sb', 'type': '*mut super_block'}, {'name': 'i_mapping', 'type': '*mut address_space'}, {'name': 'i_security', 'type': '*mut core::ffi::c_void'}, {'name': 'i_ino', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'inode__bindgen_ty_1'}, {'name': 'i_rdev', 'type': 'dev_t'}, {'name': 'i_size', 'type': 'loff_t'}, {'name': '__i_atime', 'type': 'timespec64'}, {'name': '__i_mtime', 'type': 'timespec64'}, {'name': '__i_ctime', 'type': 'timespec64'}, {'name': 'i_lock', 'type': 'spinlock_t'}, {'name': 'i_bytes', 'type': 'core::ffi::c_ushort'}, {'name': 'i_blkbits', 'type': 'u8_'}, {'name': 'i_write_hint', 'type': 'u8_'}, {'name': 'i_blocks', 'type': 'blkcnt_t'}, {'name': 'i_state', 'type': 'core::ffi::c_ulong'}, {'name': 'i_rwsem', 'type': 'rw_semaphore'}, {'name': 'dirtied_when', 'type': 'core::ffi::c_ulong'}, {'name': 'dirtied_time_when', 'type': 'core::ffi::c_ulong'}, {'name': 'i_hash', 'type': 'hlist_node'}, {'name': 'i_io_list', 'type': 'list_head'}, {'name': 'i_lru', 'type': 'list_head'}, {'name': 'i_sb_list', 'type': 'list_head'}, {'name': 'i_wb_list', 'type': 'list_head'}, {'name': '__bindgen_anon_2', 'type': 'inode__bindgen_ty_2'}, {'name': 'i_version', 'type': 'atomic64_t'}, {'name': 'i_sequence', 'type': 'atomic64_t'}, {'name': 'i_count', 'type': 'atomic_t'}, {'name': 'i_dio_count', 'type': 'atomic_t'}, {'name': 'i_writecount', 'type': 'atomic_t'}, {'name': 'i_readcount', 'type': 'atomic_t'}, {'name': '__bindgen_anon_3', 'type': 'inode__bindgen_ty_3'}, {'name': 'i_flctx', 'type': '*mut file_lock_context'}, {'name': 'i_data', 'type': 'address_space'}, {'name': 'i_devices', 'type': 'list_head'}, {'name': '__bindgen_anon_4', 'type': 'inode__bindgen_ty_4'}, {'name': 'i_generation', 'type': '__u32'}, {'name': 'i_fsnotify_mask', 'type': '__u32'}, {'name': 'i_fsnotify_marks', 'type': '*mut fsnotify_mark_connector'}, {'name': 'i_private', 'type': '*mut core::ffi::c_void'}]`

## Rust-Side Dependency

The symbol is used through Rust binding calls or nearby wrapper code.

- No Rust-side evidence was attached to this warning.

## Why The Compiler Cannot Fully Catch It

This case is treated as a contract-review target. The type checker can validate the current call shape, but it does not verify that Rust wrapper assumptions about nullability, error representation, ownership, or context remain synchronized with C-side behavior.

## BindDrift Warning

- Warning: `W-001016`
- Drift type: `FieldDrift`
- C symbol: `inode`
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
