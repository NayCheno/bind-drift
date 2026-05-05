# BindDrift Ranked Warnings

## W-000002 FieldDrift

- Risk: High
- Score: 13.0
- Symbol: request
- Explanation: request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'q', 'type': '*mut request_queue'}, {'name': 'mq_ctx', 'type': '*mut blk_mq_ctx'}, {'name': 'mq_hctx', 'type': '*mut blk_mq_hw_ctx'}, {'name': 'cmd_flags', 'type': 'blk_opf_t'}, {'name': 'rq_flags', 'type': 'req_flags_t'}, {'name': 'tag', 'type': 'ffi::c_int'}, {'name': 'internal_tag', 'type': 'ffi::c_int'}, {'name': 'timeout', 'type': 'ffi::c_uint'}, {'name': '__data_len', 'type': 'ffi::c_uint'}, {'name': '__sector', 'type': 'sector_t'}, {'name': 'bio', 'type': '*mut bio'}, {'name': 'biotail', 'type': '*mut bio'}, {'name': '__bindgen_anon_1', 'type': 'request__bindgen_ty_1'}, {'name': 'part', 'type': '*mut block_device'}, {'name': 'alloc_time_ns', 'type': 'u64_'}, {'name': 'start_time_ns', 'type': 'u64_'}, {'name': 'io_start_time_ns', 'type': 'u64_'}, {'name': 'stats_sectors', 'type': 'ffi::c_ushort'}, {'name': 'nr_phys_segments', 'type': 'ffi::c_ushort'}, {'name': 'nr_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'state', 'type': 'mq_rq_state'}, {'name': 'ref_', 'type': 'atomic_t'}, {'name': 'deadline', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_2', 'type': 'request__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'request__bindgen_ty_3'}, {'name': 'elv', 'type': 'request__bindgen_ty_4'}, {'name': 'flush', 'type': 'request__bindgen_ty_5'}, {'name': 'fifo_time', 'type': 'u64_'}, {'name': 'end_io', 'type': 'rq_end_io_fn'}, {'name': 'end_io_data', 'type': '*mut ffi::c_void'}]`
- New: `[{'name': 'q', 'type': '*mut request_queue'}, {'name': 'mq_ctx', 'type': '*mut blk_mq_ctx'}, {'name': 'mq_hctx', 'type': '*mut blk_mq_hw_ctx'}, {'name': 'cmd_flags', 'type': 'blk_opf_t'}, {'name': 'rq_flags', 'type': 'req_flags_t'}, {'name': 'tag', 'type': 'ffi::c_int'}, {'name': 'internal_tag', 'type': 'ffi::c_int'}, {'name': 'timeout', 'type': 'ffi::c_uint'}, {'name': '__data_len', 'type': 'ffi::c_uint'}, {'name': '__sector', 'type': 'sector_t'}, {'name': 'bio', 'type': '*mut bio'}, {'name': 'biotail', 'type': '*mut bio'}, {'name': '__bindgen_anon_1', 'type': 'request__bindgen_ty_1'}, {'name': 'part', 'type': '*mut block_device'}, {'name': 'alloc_time_ns', 'type': 'u64_'}, {'name': 'start_time_ns', 'type': 'u64_'}, {'name': 'io_start_time_ns', 'type': 'u64_'}, {'name': 'stats_sectors', 'type': 'ffi::c_ushort'}, {'name': 'nr_phys_segments', 'type': 'ffi::c_ushort'}, {'name': 'nr_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'phys_gap_bit', 'type': 'ffi::c_uchar'}, {'name': 'state', 'type': 'mq_rq_state'}, {'name': 'ref_', 'type': 'atomic_t'}, {'name': 'deadline', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_2', 'type': 'request__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'request__bindgen_ty_3'}, {'name': 'elv', 'type': 'request__bindgen_ty_4'}, {'name': 'flush', 'type': 'request__bindgen_ty_5'}, {'name': 'fifo_time', 'type': 'u64_'}, {'name': 'end_io', 'type': 'rq_end_io_fn'}, {'name': 'end_io_data', 'type': '*mut ffi::c_void'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/block/mq/operations.rs:158 `commit_rqs_callback` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/block/mq/operations.rs:214 `complete_callback` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/block/mq/operations.rs:219 `complete_callback` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/block/mq/operations.rs:246 `complete_callback` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/block/mq/request.rs:60 `None` unsafe=0
- safe API `Request<T>::start_unchecked`
- safe API `Request<T>::complete`
- safe API `Request<T>::wrapper_ptr`
- .binddrift/worktrees/v6.19/rust/kernel/block/mq/operations.rs:153 `/// # Safety`
- .binddrift/worktrees/v6.19/rust/kernel/block/mq/operations.rs:154 `///`
- .binddrift/worktrees/v6.19/rust/kernel/block/mq/operations.rs:155 `/// This function may only be called by blk-mq C infrastructure. `rq` must`
- .binddrift/worktrees/v6.19/rust/kernel/block/mq/request.rs:76 `NONNULL_MAPPING`
- .binddrift/worktrees/v6.19/rust/kernel/block/mq/request.rs:104 `RESULT_RETURN`
- .binddrift/worktrees/v6.19/rust/kernel/block/mq/request.rs:60 `OPAQUE`
- .binddrift/worktrees/v6.19/rust/kernel/block/mq/request.rs:63 `AREF`
- .binddrift/worktrees/v6.19/rust/kernel/block/mq/request.rs:72 `AREF`
- wrapper_fix: `28e848386b92645f93b9f2fdba5882c3ca7fb3e2`
- wrapper_fix: `a307bf1db5448eccd72a1d7857f7661c6330d5ad`

## W-000028 SignatureDrift

- Risk: High
- Score: 13.0
- Symbol: dev_get_drvdata
- Explanation: dev_get_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['&pdev->dev'], 'return_type': 'return'}`
- New: `{'params': ['&intf->dev'], 'return_type': 'return'}`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/device.rs:239 `None` unsafe=1
- .binddrift/worktrees/v6.19/rust/kernel/device.rs:281 `None` unsafe=1
- .binddrift/worktrees/v6.19/rust/kernel/device.rs:317 `None` unsafe=1
- .binddrift/worktrees/v6.19/rust/kernel/device.rs:234 `///`
- .binddrift/worktrees/v6.19/rust/kernel/device.rs:235 `/// - The type `T` must match the type of the `ForeignOwnable` previously stored by`
- .binddrift/worktrees/v6.19/rust/kernel/device.rs:236 `///   [`Device::set_drvdata`].`
- .binddrift/worktrees/v6.19/rust/kernel/device.rs:315 `RESULT_RETURN`

## W-000001 FieldDrift

- Risk: Medium
- Score: 10.0
- Symbol: queue_limits
- Explanation: queue_limits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'min_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_write_streams', 'type': 'ffi::c_ushort'}, {'name': 'write_stream_granularity', 'type': 'ffi::c_uint'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`
- New: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'max_fast_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_write_streams', 'type': 'ffi::c_ushort'}, {'name': 'write_stream_granularity', 'type': 'ffi::c_uint'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/block/mq/gen_disk.rs:110 `GenDiskBuilder::capacity_sectors` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/block/mq/gen_disk.rs:111 `GenDiskBuilder::capacity_sectors` unsafe=1
- safe API `GenDiskBuilder::capacity_sectors`
- .binddrift/worktrees/v6.19/rust/kernel/block/mq/gen_disk.rs:106 `// SAFETY: T::QueueData was created by the call to `into_foreign()` above`
- .binddrift/worktrees/v6.19/rust/kernel/block/mq/gen_disk.rs:110 `// SAFETY: `bindings::queue_limits` contain only fields that are valid when zeroed.`
- wrapper_fix: `5e3b7009f116f684ac6b93d8924506154f3b1f6d`

## W-000003 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_ACCOUNT
- Explanation: VM_ACCOUNT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00100000	/* Is a VM accounted object */`
- New: `INIT_VM_FLAG(ACCOUNT)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:438 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:434 `/// Lock the pages covered when they are faulted in.`

## W-000004 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_ARCH_1
- Explanation: VM_ARCH_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x01000000	/* Architecture-specific flag */`
- New: `INIT_VM_FLAG(ARCH_1)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:450 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:446 `/// Synchronous page faults. (DAX-specific)`

## W-000005 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_DONTCOPY
- Explanation: VM_DONTCOPY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00020000      /* Do not copy this vma on fork */`
- New: `INIT_VM_FLAG(DONTCOPY)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:429 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:425 `/// Memory mapped I/O or similar.`

## W-000006 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_DONTDUMP
- Explanation: VM_DONTDUMP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x04000000	/* Do not include in the core dump */`
- New: `INIT_VM_FLAG(DONTDUMP)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:456 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:452 `/// Wipe VMA contents in child on fork.`

## W-000007 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_DONTEXPAND
- Explanation: VM_DONTEXPAND changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00040000	/* Cannot expand with mremap() */`
- New: `INIT_VM_FLAG(DONTEXPAND)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:432 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:428 `/// Do not copy this vma on fork.`

## W-000008 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_EXEC
- Explanation: VM_EXEC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000004`
- New: `INIT_VM_FLAG(EXEC)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:405 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:401 `/// Mapping allows writes.`

## W-000009 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_HUGEPAGE
- Explanation: VM_HUGEPAGE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x20000000	/* MADV_HUGEPAGE marked this vma */`
- New: `INIT_VM_FLAG(HUGEPAGE)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:465 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:461 `/// Can contain `struct page` and pure PFN pages.`

## W-000010 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_HUGETLB
- Explanation: VM_HUGETLB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00400000	/* Huge TLB Page VM */`
- New: `INIT_VM_FLAG(HUGETLB)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:444 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:440 `/// Should the VM suppress accounting.`

## W-000011 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_IO
- Explanation: VM_IO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00004000	/* Memory mapped I/O or similar */`
- New: `INIT_VM_FLAG(IO)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:426 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:422 `/// Page-ranges managed without `struct page`, just pure PFN.`

## W-000012 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_LOCKONFAULT
- Explanation: VM_LOCKONFAULT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00080000	/* Lock the pages covered when they are faulted in */`
- New: `INIT_VM_FLAG(LOCKONFAULT)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:435 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:431 `/// Cannot expand with mremap().`

## W-000013 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_MAYEXEC
- Explanation: VM_MAYEXEC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000040`
- New: `INIT_VM_FLAG(MAYEXEC)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:417 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:413 `/// Mapping may be updated to allow writes.`

## W-000014 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_MAYREAD
- Explanation: VM_MAYREAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000010	/* limits for mprotect() etc */`
- New: `INIT_VM_FLAG(MAYREAD)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:411 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:407 `/// Mapping is shared.`

## W-000015 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_MAYSHARE
- Explanation: VM_MAYSHARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000080`
- New: `INIT_VM_FLAG(MAYSHARE)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:420 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:416 `/// Mapping may be updated to allow execution.`

## W-000016 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_MAYWRITE
- Explanation: VM_MAYWRITE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000020`
- New: `INIT_VM_FLAG(MAYWRITE)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:414 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:410 `/// Mapping may be updated to allow reads.`

## W-000017 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_MERGEABLE
- Explanation: VM_MERGEABLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `BIT(31)		/* KSM may merge identical pages */`
- New: `INIT_VM_FLAG(MERGEABLE)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:471 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:467 `/// MADV_NOHUGEPAGE marked this vma.`
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:470 `/// KSM may merge identical pages.`

## W-000018 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_MIXEDMAP
- Explanation: VM_MIXEDMAP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x10000000	/* Can contain "struct page" and pure PFN pages */`
- New: `INIT_VM_FLAG(MIXEDMAP)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:462 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:458 `/// Not soft dirty clean area.`

## W-000019 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_NOHUGEPAGE
- Explanation: VM_NOHUGEPAGE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x40000000	/* MADV_NOHUGEPAGE marked this vma */`
- New: `INIT_VM_FLAG(NOHUGEPAGE)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:468 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:464 `/// MADV_HUGEPAGE marked this vma.`

## W-000020 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_NORESERVE
- Explanation: VM_NORESERVE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00200000	/* should the VM suppress accounting */`
- New: `INIT_VM_FLAG(NORESERVE)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:441 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:437 `/// Is a VM accounted object.`

## W-000021 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_PFNMAP
- Explanation: VM_PFNMAP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000400	/* Page-ranges managed without "struct page", just pure PFN */`
- New: `INIT_VM_FLAG(PFNMAP)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:423 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:419 `/// Mapping may be updated to be shared.`

## W-000022 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_READ
- Explanation: VM_READ changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000001	/* currently active flags */`
- New: `INIT_VM_FLAG(READ)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:399 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:395 `/// No flags are set.`

## W-000023 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_SHARED
- Explanation: VM_SHARED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000008`
- New: `INIT_VM_FLAG(SHARED)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:408 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:404 `/// Mapping allows execution.`

## W-000024 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_SOFTDIRTY
- Explanation: VM_SOFTDIRTY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0`
- New: `VM_NONE`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:459 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:455 `/// Do not include in the core dump.`

## W-000025 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_SYNC
- Explanation: VM_SYNC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00800000	/* Synchronous page faults */`
- New: `INIT_VM_FLAG(SYNC)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:447 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:443 `/// Huge TLB Page VM.`

## W-000026 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_WIPEONFORK
- Explanation: VM_WIPEONFORK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x02000000	/* Wipe VMA contents in child. */`
- New: `INIT_VM_FLAG(WIPEONFORK)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:453 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:449 `/// Architecture-specific flag.`

## W-000027 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_WRITE
- Explanation: VM_WRITE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000002`
- New: `INIT_VM_FLAG(WRITE)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:402 `None` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/mm/virt.rs:398 `/// Mapping allows reads.`
