# BindDrift Ranked Warnings

## W-000001 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: dev_set_drvdata
- Explanation: dev_set_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/device.rs:202 `Device<CoreInternal>::set_drvdata` unsafe=1
- safe API `Device<CoreInternal>::set_drvdata`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/device.rs:199 `/// Store a pointer to the bound driver's private data.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/device.rs:201 `// SAFETY: By the type invariants, `self.as_raw()` is a valid pointer to a `struct device`.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/device.rs:205 `/// Take ownership of the private data stored in this [`Device`].`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/device.rs:200 `FOREIGN_OWNABLE`
- wrapper_fix: `0242623384c767b1156b61b67894b4ecf6682b8b`

## W-000004 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: poll_wait
- Explanation: poll_wait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/sync/poll.rs:61 `PollTable<'a>::register_wait` unsafe=1
- safe API `PollTable<'a>::register_wait`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/sync/poll.rs:65 `/// A wrapper around [`CondVar`] that makes it usable with [`PollTable`].`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/sync/poll.rs:66 `///`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/sync/poll.rs:61 `AS_PTR`
- wrapper_fix: `de747bd023c09b5b7f3bf5c952d7b1da77a9caaa`

## W-000007 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: regulator_get_voltage
- Explanation: regulator_get_voltage changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:269 `Regulator<T>::get_voltage` unsafe=1
- safe API `Regulator<T>::get_voltage`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:266 `/// Gets the current voltage of the regulator.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:268 `// SAFETY: Safe as per the type invariants of `Regulator`.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:267 `RESULT_RETURN`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:269 `AS_PTR`
- wrapper_fix: `8121353a4bf8e38afee26299419a78ec108e14a6`

## W-000008 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: regulator_is_enabled
- Explanation: regulator_is_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:383 `Regulator<T>::is_enabled` unsafe=1
- safe API `Regulator<T>::is_enabled`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:380 `/// Checks if the regulator is enabled.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:382 `// SAFETY: Safe as per the type invariants of `Regulator`.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:383 `AS_PTR`
- wrapper_fix: `8121353a4bf8e38afee26299419a78ec108e14a6`

## W-000010 FieldDrift

- Risk: Low
- Score: 6.0
- Symbol: queue_limits
- Explanation: queue_limits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'min_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_write_streams', 'type': 'ffi::c_ushort'}, {'name': 'write_stream_granularity', 'type': 'ffi::c_uint'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`
- New: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'min_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_write_streams', 'type': 'ffi::c_ushort'}, {'name': 'write_stream_granularity', 'type': 'ffi::c_uint'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/block/mq/gen_disk.rs:97 `GenDiskBuilder::capacity_sectors` unsafe=1
- safe API `GenDiskBuilder::capacity_sectors`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/block/mq/gen_disk.rs:96 `// SAFETY: `bindings::queue_limits` contain only fields that are valid when zeroed.`
- wrapper_fix: `5e3b7009f116f684ac6b93d8924506154f3b1f6d`

## W-000002 SignatureDrift

- Risk: Low
- Score: 3.0
- Symbol: fsleep
- Explanation: fsleep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/time/delay.rs:47 `fsleep` unsafe=1
- safe API `fsleep`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/time/delay.rs:42 `// SAFETY: It is always safe to call `fsleep()` with any duration.`
- wrapper_fix: `d4b29ddf82a458935f1bd4909b8a7a13df9d3bdc`

## W-000005 SignatureDrift

- Risk: Low
- Score: 2.0
- Symbol: regulator_disable
- Explanation: regulator_disable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:299 `disable_internal` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:393 `drop` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:298 `// SAFETY: Safe as per the type invariants of `Regulator`.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:304 `/// Obtains a [`Regulator`] instance from the system.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:390 `// SAFETY: By the type invariants, we know that `self` owns a`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:294 `TO_RESULT_MAPPING`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:299 `TO_RESULT_MAPPING`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:299 `AS_PTR`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:393 `AS_PTR`
- wrapper_fix: `8121353a4bf8e38afee26299419a78ec108e14a6`

## W-000006 SignatureDrift

- Risk: Low
- Score: 2.0
- Symbol: regulator_enable
- Explanation: regulator_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:294 `enable_internal` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:293 `// SAFETY: Safe as per the type invariants of `Regulator`.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:294 `AS_PTR`
- wrapper_fix: `8121353a4bf8e38afee26299419a78ec108e14a6`

## W-000009 SignatureDrift

- Risk: Low
- Score: 2.0
- Symbol: regulator_put
- Explanation: regulator_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:397 `drop` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:395 `// SAFETY: By the type invariants, we know that `self` owns a reference,`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:401 `/// A voltage.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:402 `///`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:397 `AS_PTR`
- wrapper_fix: `8121353a4bf8e38afee26299419a78ec108e14a6`

## W-000003 SignatureDrift

- Risk: Low
- Score: -5.0
- Symbol: platform_set_drvdata
- Explanation: platform_set_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Score Breakdown

- binding_only_penalty: `-5.0`

### Rust Evidence

- wrapper_fix: `ef4dc4cc7001e9cce8a3b556362171648be9ad92`
