# BindDrift Ranked Warnings

## W-000002 FieldDrift

- Risk: High
- Score: 13.0
- Symbol: device
- Explanation: device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'kobj', 'type': 'kobject'}, {'name': 'parent', 'type': '*mut device'}, {'name': 'p', 'type': '*mut device_private'}, {'name': 'init_name', 'type': '*const core::ffi::c_char'}, {'name': 'type_', 'type': '*const device_type'}, {'name': 'bus', 'type': '*const bus_type'}, {'name': 'driver', 'type': '*mut device_driver'}, {'name': 'platform_data', 'type': '*mut core::ffi::c_void'}, {'name': 'driver_data', 'type': '*mut core::ffi::c_void'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'links', 'type': 'dev_links_info'}, {'name': 'power', 'type': 'dev_pm_info'}, {'name': 'pm_domain', 'type': '*mut dev_pm_domain'}, {'name': 'msi', 'type': 'dev_msi_info'}, {'name': 'dma_ops', 'type': '*mut dma_map_ops'}, {'name': 'dma_mask', 'type': '*mut u64_'}, {'name': 'coherent_dma_mask', 'type': 'u64_'}, {'name': 'bus_dma_limit', 'type': 'u64_'}, {'name': 'dma_range_map', 'type': '*mut bus_dma_region'}, {'name': 'dma_parms', 'type': '*mut device_dma_parameters'}, {'name': 'dma_pools', 'type': 'list_head'}, {'name': 'dma_io_tlb_mem', 'type': '*mut io_tlb_mem'}, {'name': 'archdata', 'type': 'dev_archdata'}, {'name': 'of_node', 'type': '*mut device_node'}, {'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'numa_node', 'type': 'core::ffi::c_int'}, {'name': 'devt', 'type': 'dev_t'}, {'name': 'id', 'type': 'u32_'}, {'name': 'devres_lock', 'type': 'spinlock_t'}, {'name': 'devres_head', 'type': 'list_head'}, {'name': 'class', 'type': '*const class'}, {'name': 'groups', 'type': '*mut *const attribute_group'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'iommu_group', 'type': '*mut iommu_group'}, {'name': 'iommu', 'type': '*mut dev_iommu'}, {'name': 'physical_location', 'type': '*mut device_physical_location'}, {'name': 'removable', 'type': 'device_removable'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 3usize]'}]`
- New: `[{'name': 'kobj', 'type': 'kobject'}, {'name': 'parent', 'type': '*mut device'}, {'name': 'p', 'type': '*mut device_private'}, {'name': 'init_name', 'type': '*const core::ffi::c_char'}, {'name': 'type_', 'type': '*const device_type'}, {'name': 'bus', 'type': '*const bus_type'}, {'name': 'driver', 'type': '*mut device_driver'}, {'name': 'platform_data', 'type': '*mut core::ffi::c_void'}, {'name': 'driver_data', 'type': '*mut core::ffi::c_void'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'links', 'type': 'dev_links_info'}, {'name': 'power', 'type': 'dev_pm_info'}, {'name': 'pm_domain', 'type': '*mut dev_pm_domain'}, {'name': 'msi', 'type': 'dev_msi_info'}, {'name': 'dma_mask', 'type': '*mut u64_'}, {'name': 'coherent_dma_mask', 'type': 'u64_'}, {'name': 'bus_dma_limit', 'type': 'u64_'}, {'name': 'dma_range_map', 'type': '*mut bus_dma_region'}, {'name': 'dma_parms', 'type': '*mut device_dma_parameters'}, {'name': 'dma_pools', 'type': 'list_head'}, {'name': 'dma_io_tlb_mem', 'type': '*mut io_tlb_mem'}, {'name': 'archdata', 'type': 'dev_archdata'}, {'name': 'of_node', 'type': '*mut device_node'}, {'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'numa_node', 'type': 'core::ffi::c_int'}, {'name': 'devt', 'type': 'dev_t'}, {'name': 'id', 'type': 'u32_'}, {'name': 'devres_lock', 'type': 'spinlock_t'}, {'name': 'devres_head', 'type': 'list_head'}, {'name': 'class', 'type': '*const class'}, {'name': 'groups', 'type': '*mut *const attribute_group'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'iommu_group', 'type': '*mut iommu_group'}, {'name': 'iommu', 'type': '*mut dev_iommu'}, {'name': 'physical_location', 'type': '*mut device_physical_location'}, {'name': 'removable', 'type': 'device_removable'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 3usize]'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/device.rs:38 `None` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/device.rs:41 `None` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/device.rs:52 `None` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/device.rs:54 `None` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/device.rs:60 `Device::get_device` unsafe=0
- safe API `Device::get_device`
- safe API `Device::as_raw`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/device.rs:33 `/// A `Device` instance represents a valid `struct device` created by the C portion of the kernel.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/device.rs:34 `///`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/device.rs:35 `/// Instances of this type are always reference-counted, that is, a call to `get_device` ensures`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/device.rs:38 `AREF`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/device.rs:38 `AREF`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/device.rs:38 `AREF`
- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`
- wrapper_fix: `4d320e30ee04c25c660eca2bb33e846ebb71a79a`

## W-000003 FieldDrift

- Risk: High
- Score: 13.0
- Symbol: request
- Explanation: request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'q', 'type': '*mut request_queue'}, {'name': 'mq_ctx', 'type': '*mut blk_mq_ctx'}, {'name': 'mq_hctx', 'type': '*mut blk_mq_hw_ctx'}, {'name': 'cmd_flags', 'type': 'blk_opf_t'}, {'name': 'rq_flags', 'type': 'req_flags_t'}, {'name': 'tag', 'type': 'core::ffi::c_int'}, {'name': 'internal_tag', 'type': 'core::ffi::c_int'}, {'name': 'timeout', 'type': 'core::ffi::c_uint'}, {'name': '__data_len', 'type': 'core::ffi::c_uint'}, {'name': '__sector', 'type': 'sector_t'}, {'name': 'bio', 'type': '*mut bio'}, {'name': 'biotail', 'type': '*mut bio'}, {'name': '__bindgen_anon_1', 'type': 'request__bindgen_ty_1'}, {'name': 'part', 'type': '*mut block_device'}, {'name': 'alloc_time_ns', 'type': 'u64_'}, {'name': 'start_time_ns', 'type': 'u64_'}, {'name': 'io_start_time_ns', 'type': 'u64_'}, {'name': 'stats_sectors', 'type': 'core::ffi::c_ushort'}, {'name': 'nr_phys_segments', 'type': 'core::ffi::c_ushort'}, {'name': 'write_hint', 'type': 'rw_hint'}, {'name': 'ioprio', 'type': 'core::ffi::c_ushort'}, {'name': 'state', 'type': 'mq_rq_state'}, {'name': 'ref_', 'type': 'atomic_t'}, {'name': 'deadline', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_2', 'type': 'request__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'request__bindgen_ty_3'}, {'name': 'elv', 'type': 'request__bindgen_ty_4'}, {'name': 'flush', 'type': 'request__bindgen_ty_5'}, {'name': 'fifo_time', 'type': 'u64_'}, {'name': 'end_io', 'type': 'rq_end_io_fn'}, {'name': 'end_io_data', 'type': '*mut core::ffi::c_void'}]`
- New: `[{'name': 'q', 'type': '*mut request_queue'}, {'name': 'mq_ctx', 'type': '*mut blk_mq_ctx'}, {'name': 'mq_hctx', 'type': '*mut blk_mq_hw_ctx'}, {'name': 'cmd_flags', 'type': 'blk_opf_t'}, {'name': 'rq_flags', 'type': 'req_flags_t'}, {'name': 'tag', 'type': 'core::ffi::c_int'}, {'name': 'internal_tag', 'type': 'core::ffi::c_int'}, {'name': 'timeout', 'type': 'core::ffi::c_uint'}, {'name': '__data_len', 'type': 'core::ffi::c_uint'}, {'name': '__sector', 'type': 'sector_t'}, {'name': 'bio', 'type': '*mut bio'}, {'name': 'biotail', 'type': '*mut bio'}, {'name': '__bindgen_anon_1', 'type': 'request__bindgen_ty_1'}, {'name': 'part', 'type': '*mut block_device'}, {'name': 'alloc_time_ns', 'type': 'u64_'}, {'name': 'start_time_ns', 'type': 'u64_'}, {'name': 'io_start_time_ns', 'type': 'u64_'}, {'name': 'stats_sectors', 'type': 'core::ffi::c_ushort'}, {'name': 'nr_phys_segments', 'type': 'core::ffi::c_ushort'}, {'name': 'nr_integrity_segments', 'type': 'core::ffi::c_ushort'}, {'name': 'write_hint', 'type': 'rw_hint'}, {'name': 'ioprio', 'type': 'core::ffi::c_ushort'}, {'name': 'state', 'type': 'mq_rq_state'}, {'name': 'ref_', 'type': 'atomic_t'}, {'name': 'deadline', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_2', 'type': 'request__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'request__bindgen_ty_3'}, {'name': 'elv', 'type': 'request__bindgen_ty_4'}, {'name': 'flush', 'type': 'request__bindgen_ty_5'}, {'name': 'fifo_time', 'type': 'u64_'}, {'name': 'end_io', 'type': 'rq_end_io_fn'}, {'name': 'end_io_data', 'type': '*mut core::ffi::c_void'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/block/mq/operations.rs:123 `commit_rqs_callback` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/block/mq/operations.rs:173 `complete_callback` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/block/mq/operations.rs:178 `complete_callback` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/block/mq/operations.rs:205 `complete_callback` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/block/mq/request.rs:53 `None` unsafe=0
- safe API `Request<T>::start_unchecked`
- safe API `Request<T>::wrapper_ptr`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/block/mq/operations.rs:118 `/// implemented, and there is no way to exercise this code path.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/block/mq/operations.rs:119 `///`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/block/mq/operations.rs:120 `/// # Safety`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/block/mq/request.rs:67 `NONNULL_MAPPING`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/block/mq/request.rs:93 `RESULT_RETURN`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/block/mq/request.rs:53 `OPAQUE`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/block/mq/request.rs:56 `AREF`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/block/mq/request.rs:63 `AREF`
- wrapper_fix: `28e848386b92645f93b9f2fdba5882c3ca7fb3e2`
- wrapper_fix: `a307bf1db5448eccd72a1d7857f7661c6330d5ad`

## W-000001 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: __mutex_init
- Explanation: __mutex_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'lock', 'type': '*mut mutex'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'key', 'type': '*mut lock_class_key'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'mutex', 'type': '*mut mutex'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'key', 'type': '*mut lock_class_key'}], 'return_type': '()'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/sync/lock/mutex.rs:104 `example` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.12/rust/kernel/sync/lock/mutex.rs:102 `// SAFETY: The safety requirements ensure that `ptr` is valid for writes, and `name` and`
- wrapper_fix: `d065cc76054d21e48a839a2a19ba99dbc51a4d11`
