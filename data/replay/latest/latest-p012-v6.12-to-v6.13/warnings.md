# BindDrift Ranked Warnings

## W-000002 SignatureDrift

- Risk: Medium
- Score: 9.0
- Symbol: IS_ERR
- Explanation: IS_ERR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'ptr', 'type': '*const core::ffi::c_void'}], 'return_type': 'bool_'}`
- New: `{'params': [{'name': 'ptr', 'type': '*const ffi::c_void'}], 'return_type': 'bool_'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/error.rs:295 `to_result` unsafe=1
- safe API `to_result`
- .binddrift/worktrees/v6.13/rust/kernel/error.rs:290 `/// ````
- .binddrift/worktrees/v6.13/rust/kernel/error.rs:291 `ERR_PTR_MAPPING`
- wrapper_fix: `752417b3f0e7721f1d630f40da22d57e0dae043e`

## W-000003 SignatureDrift

- Risk: Medium
- Score: 9.0
- Symbol: PTR_ERR
- Explanation: PTR_ERR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'ptr', 'type': '*const core::ffi::c_void'}], 'return_type': 'core::ffi::c_long'}`
- New: `{'params': [{'name': 'ptr', 'type': '*const ffi::c_void'}], 'return_type': 'ffi::c_long'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/error.rs:297 `to_result` unsafe=1
- safe API `to_result`
- .binddrift/worktrees/v6.13/rust/kernel/error.rs:294 `// SAFETY: The FFI function does not deref the pointer.`
- .binddrift/worktrees/v6.13/rust/kernel/error.rs:296 `// SAFETY: The FFI function does not deref the pointer.`
- .binddrift/worktrees/v6.13/rust/kernel/error.rs:295 `IS_ERR_MAPPING`
- .binddrift/worktrees/v6.13/rust/kernel/error.rs:297 `PTR_ERR_MAPPING`
- wrapper_fix: `752417b3f0e7721f1d630f40da22d57e0dae043e`

## W-000004 SignatureDrift

- Risk: Medium
- Score: 9.0
- Symbol: REFCOUNT_INIT
- Explanation: REFCOUNT_INIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'n', 'type': 'core::ffi::c_int'}], 'return_type': 'refcount_t'}`
- New: `{'params': [{'name': 'n', 'type': 'ffi::c_int'}], 'return_type': 'refcount_t'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/sync/arc.rs:199 `Arc<T>::new` unsafe=1
- .binddrift/worktrees/v6.13/rust/kernel/sync/arc.rs:318 `Arc<T>::into_unique_or_drop` unsafe=1
- .binddrift/worktrees/v6.13/rust/kernel/sync/arc.rs:646 `UniqueArc<T>::new_uninit` unsafe=1
- safe API `Arc<T>::new`
- safe API `Arc<T>::into_unique_or_drop`
- safe API `UniqueArc<T>::new_uninit`
- .binddrift/worktrees/v6.13/rust/kernel/sync/arc.rs:194 `/// Constructs a new reference counted instance of `T`.`
- .binddrift/worktrees/v6.13/rust/kernel/sync/arc.rs:198 `// SAFETY: There are no safety requirements for this FFI call.`
- .binddrift/worktrees/v6.13/rust/kernel/sync/arc.rs:313 `// SAFETY: We own a refcount, so the pointer is not dangling.`
- .binddrift/worktrees/v6.13/rust/kernel/sync/arc.rs:195 `RESULT_RETURN`
- .binddrift/worktrees/v6.13/rust/kernel/sync/arc.rs:641 `RESULT_RETURN`
- weak lifetime name .binddrift/worktrees/v6.13/rust/kernel/sync/arc.rs:199 `LIFETIME_NAMING_PATTERN`
- weak lifetime name .binddrift/worktrees/v6.13/rust/kernel/sync/arc.rs:318 `LIFETIME_NAMING_PATTERN`
- weak lifetime name .binddrift/worktrees/v6.13/rust/kernel/sync/arc.rs:646 `LIFETIME_NAMING_PATTERN`
- wrapper_fix: `bb38f35b35f9de0cebc4d62ea73482454e38cef3`
- wrapper_fix: `076acb647c1f448177d8b3b0e4f33de959713d7d`
- wrapper_fix: `9ba1aaf25ab7dadb910348b6857865e87b4c5689`

## W-000016 SignatureDrift

- Risk: Medium
- Score: 9.0
- Symbol: device_add_disk
- Explanation: device_add_disk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'parent', 'type': '*mut device'}, {'name': 'disk', 'type': '*mut gendisk'}, {'name': 'groups', 'type': '*mut *const attribute_group'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'parent', 'type': '*mut device'}, {'name': 'disk', 'type': '*mut gendisk'}, {'name': 'groups', 'type': '*mut *const attribute_group'}], 'return_type': 'ffi::c_int'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/block/mq/gen_disk.rs:160 `GenDiskBuilder::capacity_sectors` unsafe=1
- safe API `GenDiskBuilder::capacity_sectors`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/gen_disk.rs:157 `// SAFETY: `gendisk` points to a valid and initialized instance of`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/gen_disk.rs:156 `TO_RESULT_MAPPING`
- wrapper_fix: `0c5928deada15a8d075516e6e0d9ee19011bb000`

## W-000017 SignatureDrift

- Risk: Medium
- Score: 9.0
- Symbol: errname
- Explanation: errname changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'err', 'type': 'core::ffi::c_int'}], 'return_type': '*const core::ffi::c_char'}`
- New: `{'params': [{'name': 'err', 'type': 'ffi::c_int'}], 'return_type': '*const ffi::c_char'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/error.rs:167 `Error::name` unsafe=1
- safe API `Error::name`
- safe API `Error::name`
- .binddrift/worktrees/v6.13/rust/kernel/error.rs:163 `/// Returns a string representing the error, if one exists.`
- .binddrift/worktrees/v6.13/rust/kernel/error.rs:166 `// SAFETY: Just an FFI call, there are no extra safety requirements.`
- .binddrift/worktrees/v6.13/rust/kernel/error.rs:171 `// SAFETY: The string returned by `errname` is static and `NUL`-terminated.`
- .binddrift/worktrees/v6.13/rust/kernel/error.rs:165 `OPTION_RETURN`
- wrapper_fix: `d2e3115d717197cb2bc020dd1f06b06538474ac3`
- wrapper_fix: `e9759c5b9ea555d09f426c70c880e9522e9b0576`

## W-000033 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: device
- Explanation: device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'kobj', 'type': 'kobject'}, {'name': 'parent', 'type': '*mut device'}, {'name': 'p', 'type': '*mut device_private'}, {'name': 'init_name', 'type': '*const core::ffi::c_char'}, {'name': 'type_', 'type': '*const device_type'}, {'name': 'bus', 'type': '*const bus_type'}, {'name': 'driver', 'type': '*mut device_driver'}, {'name': 'platform_data', 'type': '*mut core::ffi::c_void'}, {'name': 'driver_data', 'type': '*mut core::ffi::c_void'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'links', 'type': 'dev_links_info'}, {'name': 'power', 'type': 'dev_pm_info'}, {'name': 'pm_domain', 'type': '*mut dev_pm_domain'}, {'name': 'msi', 'type': 'dev_msi_info'}, {'name': 'dma_mask', 'type': '*mut u64_'}, {'name': 'coherent_dma_mask', 'type': 'u64_'}, {'name': 'bus_dma_limit', 'type': 'u64_'}, {'name': 'dma_range_map', 'type': '*mut bus_dma_region'}, {'name': 'dma_parms', 'type': '*mut device_dma_parameters'}, {'name': 'dma_pools', 'type': 'list_head'}, {'name': 'dma_io_tlb_mem', 'type': '*mut io_tlb_mem'}, {'name': 'archdata', 'type': 'dev_archdata'}, {'name': 'of_node', 'type': '*mut device_node'}, {'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'numa_node', 'type': 'core::ffi::c_int'}, {'name': 'devt', 'type': 'dev_t'}, {'name': 'id', 'type': 'u32_'}, {'name': 'devres_lock', 'type': 'spinlock_t'}, {'name': 'devres_head', 'type': 'list_head'}, {'name': 'class', 'type': '*const class'}, {'name': 'groups', 'type': '*mut *const attribute_group'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'iommu_group', 'type': '*mut iommu_group'}, {'name': 'iommu', 'type': '*mut dev_iommu'}, {'name': 'physical_location', 'type': '*mut device_physical_location'}, {'name': 'removable', 'type': 'device_removable'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 3usize]'}]`
- New: `[{'name': 'kobj', 'type': 'kobject'}, {'name': 'parent', 'type': '*mut device'}, {'name': 'p', 'type': '*mut device_private'}, {'name': 'init_name', 'type': '*const ffi::c_char'}, {'name': 'type_', 'type': '*const device_type'}, {'name': 'bus', 'type': '*const bus_type'}, {'name': 'driver', 'type': '*mut device_driver'}, {'name': 'platform_data', 'type': '*mut ffi::c_void'}, {'name': 'driver_data', 'type': '*mut ffi::c_void'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'links', 'type': 'dev_links_info'}, {'name': 'power', 'type': 'dev_pm_info'}, {'name': 'pm_domain', 'type': '*mut dev_pm_domain'}, {'name': 'msi', 'type': 'dev_msi_info'}, {'name': 'dma_mask', 'type': '*mut u64_'}, {'name': 'coherent_dma_mask', 'type': 'u64_'}, {'name': 'bus_dma_limit', 'type': 'u64_'}, {'name': 'dma_range_map', 'type': '*mut bus_dma_region'}, {'name': 'dma_parms', 'type': '*mut device_dma_parameters'}, {'name': 'dma_pools', 'type': 'list_head'}, {'name': 'dma_io_tlb_mem', 'type': '*mut io_tlb_mem'}, {'name': 'archdata', 'type': 'dev_archdata'}, {'name': 'of_node', 'type': '*mut device_node'}, {'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'numa_node', 'type': 'ffi::c_int'}, {'name': 'devt', 'type': 'dev_t'}, {'name': 'id', 'type': 'u32_'}, {'name': 'devres_lock', 'type': 'spinlock_t'}, {'name': 'devres_head', 'type': 'list_head'}, {'name': 'class', 'type': '*const class'}, {'name': 'groups', 'type': '*mut *const attribute_group'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'iommu_group', 'type': '*mut iommu_group'}, {'name': 'iommu', 'type': '*mut dev_iommu'}, {'name': 'physical_location', 'type': '*mut device_physical_location'}, {'name': 'removable', 'type': 'device_removable'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 3usize]'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/device.rs:44 `None` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/device.rs:57 `Device::get_device` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/device.rs:63 `Device::as_raw` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/device.rs:75 `Device::as_raw` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:15 `None` unsafe=0
- safe API `Device::get_device`
- safe API `Device::as_raw`
- .binddrift/worktrees/v6.13/rust/kernel/device.rs:39 `/// that the allocation remains valid at least until the matching call to `put_device`.`
- .binddrift/worktrees/v6.13/rust/kernel/device.rs:40 `///`
- .binddrift/worktrees/v6.13/rust/kernel/device.rs:41 `/// `bindings::device::release` is valid to be called from any thread, hence `ARef<Device>` can be`
- .binddrift/worktrees/v6.13/rust/kernel/device.rs:41 `AREF`
- .binddrift/worktrees/v6.13/rust/kernel/device.rs:44 `OPAQUE`
- .binddrift/worktrees/v6.13/rust/kernel/device.rs:57 `AREF`
- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`
- wrapper_fix: `4d320e30ee04c25c660eca2bb33e846ebb71a79a`

## W-000037 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: rb_node
- Explanation: rb_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__rb_parent_color', 'type': 'core::ffi::c_ulong'}, {'name': 'rb_right', 'type': '*mut rb_node'}, {'name': 'rb_left', 'type': '*mut rb_node'}]`
- New: `[{'name': '__rb_parent_color', 'type': 'ffi::c_ulong'}, {'name': 'rb_right', 'type': '*mut rb_node'}, {'name': 'rb_left', 'type': '*mut rb_node'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/rbtree.rs:326 `raw_entry` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/rbtree.rs:725 `None` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/rbtree.rs:874 `get_neighbor_raw` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/rbtree.rs:890 `get_neighbor_raw` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/rbtree.rs:901 `get_neighbor_raw` unsafe=0
- safe API `RBTreeNodeReservation<K, V>::into_node`
- .binddrift/worktrees/v6.13/rust/kernel/rbtree.rs:327 `// SAFETY: `raw_self` is a valid pointer to the `RBTree` (created from `self` above).`
- .binddrift/worktrees/v6.13/rust/kernel/rbtree.rs:331 `// SAFETY: All links fields we create are in a `Node<K, V>`.`
- .binddrift/worktrees/v6.13/rust/kernel/rbtree.rs:720 `///`
- .binddrift/worktrees/v6.13/rust/kernel/rbtree.rs:915 `AS_PTR`
- wrapper_fix: `8333ff4d0799aafbe4275cddcbaf45e545e4efba`

## W-000038 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: request
- Explanation: request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'q', 'type': '*mut request_queue'}, {'name': 'mq_ctx', 'type': '*mut blk_mq_ctx'}, {'name': 'mq_hctx', 'type': '*mut blk_mq_hw_ctx'}, {'name': 'cmd_flags', 'type': 'blk_opf_t'}, {'name': 'rq_flags', 'type': 'req_flags_t'}, {'name': 'tag', 'type': 'core::ffi::c_int'}, {'name': 'internal_tag', 'type': 'core::ffi::c_int'}, {'name': 'timeout', 'type': 'core::ffi::c_uint'}, {'name': '__data_len', 'type': 'core::ffi::c_uint'}, {'name': '__sector', 'type': 'sector_t'}, {'name': 'bio', 'type': '*mut bio'}, {'name': 'biotail', 'type': '*mut bio'}, {'name': '__bindgen_anon_1', 'type': 'request__bindgen_ty_1'}, {'name': 'part', 'type': '*mut block_device'}, {'name': 'alloc_time_ns', 'type': 'u64_'}, {'name': 'start_time_ns', 'type': 'u64_'}, {'name': 'io_start_time_ns', 'type': 'u64_'}, {'name': 'stats_sectors', 'type': 'core::ffi::c_ushort'}, {'name': 'nr_phys_segments', 'type': 'core::ffi::c_ushort'}, {'name': 'nr_integrity_segments', 'type': 'core::ffi::c_ushort'}, {'name': 'write_hint', 'type': 'rw_hint'}, {'name': 'ioprio', 'type': 'core::ffi::c_ushort'}, {'name': 'state', 'type': 'mq_rq_state'}, {'name': 'ref_', 'type': 'atomic_t'}, {'name': 'deadline', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_2', 'type': 'request__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'request__bindgen_ty_3'}, {'name': 'elv', 'type': 'request__bindgen_ty_4'}, {'name': 'flush', 'type': 'request__bindgen_ty_5'}, {'name': 'fifo_time', 'type': 'u64_'}, {'name': 'end_io', 'type': 'rq_end_io_fn'}, {'name': 'end_io_data', 'type': '*mut core::ffi::c_void'}]`
- New: `[{'name': 'q', 'type': '*mut request_queue'}, {'name': 'mq_ctx', 'type': '*mut blk_mq_ctx'}, {'name': 'mq_hctx', 'type': '*mut blk_mq_hw_ctx'}, {'name': 'cmd_flags', 'type': 'blk_opf_t'}, {'name': 'rq_flags', 'type': 'req_flags_t'}, {'name': 'tag', 'type': 'ffi::c_int'}, {'name': 'internal_tag', 'type': 'ffi::c_int'}, {'name': 'timeout', 'type': 'ffi::c_uint'}, {'name': '__data_len', 'type': 'ffi::c_uint'}, {'name': '__sector', 'type': 'sector_t'}, {'name': 'bio', 'type': '*mut bio'}, {'name': 'biotail', 'type': '*mut bio'}, {'name': '__bindgen_anon_1', 'type': 'request__bindgen_ty_1'}, {'name': 'part', 'type': '*mut block_device'}, {'name': 'alloc_time_ns', 'type': 'u64_'}, {'name': 'start_time_ns', 'type': 'u64_'}, {'name': 'io_start_time_ns', 'type': 'u64_'}, {'name': 'stats_sectors', 'type': 'ffi::c_ushort'}, {'name': 'nr_phys_segments', 'type': 'ffi::c_ushort'}, {'name': 'nr_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'state', 'type': 'mq_rq_state'}, {'name': 'ref_', 'type': 'atomic_t'}, {'name': 'deadline', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_2', 'type': 'request__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'request__bindgen_ty_3'}, {'name': 'elv', 'type': 'request__bindgen_ty_4'}, {'name': 'flush', 'type': 'request__bindgen_ty_5'}, {'name': 'fifo_time', 'type': 'u64_'}, {'name': 'end_io', 'type': 'rq_end_io_fn'}, {'name': 'end_io_data', 'type': '*mut ffi::c_void'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/block/mq/operations.rs:123 `complete_callback` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/operations.rs:178 `complete_callback` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/operations.rs:205 `complete_callback` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/request.rs:56 `None` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/request.rs:68 `Request<T>::aref_from_raw` unsafe=0
- safe API `Request<T>::aref_from_raw`
- safe API `Request<T>::wrapper_ptr`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/operations.rs:118 `/// implemented, and there is no way to exercise this code path.`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/operations.rs:119 `///`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/operations.rs:120 `/// # Safety`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/request.rs:72 `NONNULL_MAPPING`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/request.rs:56 `OPAQUE`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/request.rs:59 `AREF`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/request.rs:68 `AREF`
- wrapper_fix: `28e848386b92645f93b9f2fdba5882c3ca7fb3e2`
- wrapper_fix: `a307bf1db5448eccd72a1d7857f7661c6330d5ad`

## W-000001 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: ERR_PTR
- Explanation: ERR_PTR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'err', 'type': 'core::ffi::c_long'}], 'return_type': '*mut core::ffi::c_void'}`
- New: `{'params': [{'name': 'err', 'type': 'ffi::c_long'}], 'return_type': '*mut ffi::c_void'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/error.rs:159 `Error::to_blk_status` unsafe=1
- safe API `Error::to_blk_status`
- .binddrift/worktrees/v6.13/rust/kernel/error.rs:154 `/// Returns the error encoded as a pointer.`
- .binddrift/worktrees/v6.13/rust/kernel/error.rs:157 `// SAFETY: `self.0` is a valid error due to its invariant.`
- wrapper_fix: `c7e20faa5fcad7a177cf6c306138010343dd6d3e`
- wrapper_fix: `7bc186731e87482662c4f86da455f435fe838fb6`
- wrapper_fix: `e9759c5b9ea555d09f426c70c880e9522e9b0576`

## W-000014 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: current_euid
- Explanation: current_euid changed across the selected Linux versions.
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

- .binddrift/worktrees/v6.13/rust/kernel/task.rs:347 `Kuid::current_euid` unsafe=1
- safe API `Kuid::current_euid`
- .binddrift/worktrees/v6.13/rust/kernel/task.rs:343 `/// Get the current euid.`
- .binddrift/worktrees/v6.13/rust/kernel/task.rs:346 `// SAFETY: Just an FFI call.`
- .binddrift/worktrees/v6.13/rust/kernel/task.rs:347 `FROM_RAW`
- wrapper_fix: `8ad1a41f7e23287f07a3516c700bc32501d4f104`

## W-000018 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: errno_to_blk_status
- Explanation: errno_to_blk_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'errno', 'type': 'core::ffi::c_int'}], 'return_type': 'blk_status_t'}`
- New: `{'params': [{'name': 'errno', 'type': 'ffi::c_int'}], 'return_type': 'blk_status_t'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/error.rs:151 `Error::to_blk_status` unsafe=1
- safe API `Error::to_blk_status`
- .binddrift/worktrees/v6.13/rust/kernel/error.rs:150 `// SAFETY: `self.0` is a valid error due to its invariant.`
- wrapper_fix: `e9759c5b9ea555d09f426c70c880e9522e9b0576`

## W-000029 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: task_euid
- Explanation: task_euid changed across the selected Linux versions.
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

- .binddrift/worktrees/v6.13/rust/kernel/task.rs:284 `Task::euid` unsafe=1
- safe API `Task::euid`
- .binddrift/worktrees/v6.13/rust/kernel/task.rs:281 `/// Returns the effective UID of the given task.`
- .binddrift/worktrees/v6.13/rust/kernel/task.rs:283 `// SAFETY: It's always safe to call `task_euid` on a valid task.`
- .binddrift/worktrees/v6.13/rust/kernel/task.rs:284 `AS_PTR`
- .binddrift/worktrees/v6.13/rust/kernel/task.rs:284 `FROM_RAW`
- wrapper_fix: `8ad1a41f7e23287f07a3516c700bc32501d4f104`

## W-000030 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: task_tgid_nr_ns
- Explanation: task_tgid_nr_ns changed across the selected Linux versions.
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

- .binddrift/worktrees/v6.13/rust/kernel/task.rs:318 `Task::tgid_nr_ns` unsafe=1
- safe API `Task::tgid_nr_ns`
- .binddrift/worktrees/v6.13/rust/kernel/task.rs:314 `// SAFETY: By the type invariant, we know that `self.0` is valid. We received a valid`
- .binddrift/worktrees/v6.13/rust/kernel/task.rs:318 `AS_PTR`
- wrapper_fix: `8ad1a41f7e23287f07a3516c700bc32501d4f104`

## W-000031 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: task_uid
- Explanation: task_uid changed across the selected Linux versions.
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

- .binddrift/worktrees/v6.13/rust/kernel/task.rs:278 `Task::uid` unsafe=1
- safe API `Task::uid`
- .binddrift/worktrees/v6.13/rust/kernel/task.rs:275 `/// Returns the UID of the given task.`
- .binddrift/worktrees/v6.13/rust/kernel/task.rs:277 `// SAFETY: It's always safe to call `task_uid` on a valid task.`
- .binddrift/worktrees/v6.13/rust/kernel/task.rs:278 `AS_PTR`
- .binddrift/worktrees/v6.13/rust/kernel/task.rs:278 `FROM_RAW`
- wrapper_fix: `8ad1a41f7e23287f07a3516c700bc32501d4f104`

## W-000036 FieldDrift

- Risk: Low
- Score: 6.0
- Symbol: queue_limits
- Explanation: queue_limits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'core::ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'core::ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'max_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'core::ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'core::ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'core::ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'core::ffi::c_uint'}, {'name': 'io_min', 'type': 'core::ffi::c_uint'}, {'name': 'io_opt', 'type': 'core::ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'core::ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'core::ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'core::ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'core::ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'core::ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'core::ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'core::ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'core::ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'core::ffi::c_uint'}, {'name': 'max_segments', 'type': 'core::ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'core::ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'core::ffi::c_ushort'}, {'name': 'max_open_zones', 'type': 'core::ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'core::ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'core::ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'core::ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`
- New: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/block/mq/gen_disk.rs:97 `GenDiskBuilder::capacity_sectors` unsafe=1
- safe API `GenDiskBuilder::capacity_sectors`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/gen_disk.rs:96 `// SAFETY: `bindings::queue_limits` contain only fields that are valid when zeroed.`
- wrapper_fix: `5e3b7009f116f684ac6b93d8924506154f3b1f6d`

## W-000022 SignatureDrift

- Risk: Low
- Score: 5.0
- Symbol: mdiobus_read
- Explanation: mdiobus_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'bus', 'type': '*mut mii_bus'}, {'name': 'addr', 'type': 'core::ffi::c_int'}, {'name': 'regnum', 'type': 'u32_'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'bus', 'type': '*mut mii_bus'}, {'name': 'addr', 'type': 'ffi::c_int'}, {'name': 'regnum', 'type': 'u32_'}], 'return_type': 'ffi::c_int'}`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:111 `read` unsafe=1
- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:107 `// SAFETY: `phydev` is pointing to a valid object by the type invariant of `Device`.`
- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:113 `TO_RESULT_MAPPING`
- wrapper_fix: `b2e47002b2350f57bfa8fe1c231e9fbb6baef78b`

## W-000023 SignatureDrift

- Risk: Low
- Score: 5.0
- Symbol: mdiobus_write
- Explanation: mdiobus_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'bus', 'type': '*mut mii_bus'}, {'name': 'addr', 'type': 'core::ffi::c_int'}, {'name': 'regnum', 'type': 'u32_'}, {'name': 'val', 'type': 'u16_'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'bus', 'type': '*mut mii_bus'}, {'name': 'addr', 'type': 'ffi::c_int'}, {'name': 'regnum', 'type': 'u32_'}, {'name': 'val', 'type': 'u16_'}], 'return_type': 'ffi::c_int'}`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:123 `write` unsafe=1
- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:119 `// SAFETY: `phydev` is pointing to a valid object by the type invariant of `Device`.`
- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:122 `TO_RESULT_MAPPING`
- wrapper_fix: `b2e47002b2350f57bfa8fe1c231e9fbb6baef78b`

## W-000024 SignatureDrift

- Risk: Low
- Score: 5.0
- Symbol: phy_read_mmd
- Explanation: phy_read_mmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'devad', 'type': 'core::ffi::c_int'}, {'name': 'regnum', 'type': 'u32_'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'devad', 'type': 'ffi::c_int'}, {'name': 'regnum', 'type': 'u32_'}], 'return_type': 'ffi::c_int'}`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:202 `read` unsafe=1
- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:199 `// SAFETY: `phydev` is pointing to a valid object by the type invariant of `Device`.`
- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:203 `TO_RESULT_MAPPING`
- wrapper_fix: `b2e47002b2350f57bfa8fe1c231e9fbb6baef78b`

## W-000025 SignatureDrift

- Risk: Low
- Score: 5.0
- Symbol: phy_write_mmd
- Explanation: phy_write_mmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'devad', 'type': 'core::ffi::c_int'}, {'name': 'regnum', 'type': 'u32_'}, {'name': 'val', 'type': 'u16_'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'devad', 'type': 'ffi::c_int'}, {'name': 'regnum', 'type': 'u32_'}, {'name': 'val', 'type': 'u16_'}], 'return_type': 'ffi::c_int'}`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:212 `write` unsafe=1
- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:209 `// SAFETY: `phydev` is pointing to a valid object by the type invariant of `Device`.`
- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:211 `TO_RESULT_MAPPING`
- wrapper_fix: `b2e47002b2350f57bfa8fe1c231e9fbb6baef78b`

## W-000034 FieldDrift

- Risk: Low
- Score: 5.0
- Symbol: firmware
- Explanation: firmware changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'size', 'type': 'usize'}, {'name': 'data', 'type': '*const u8_'}, {'name': 'priv_', 'type': '*mut core::ffi::c_void'}]`
- New: `[{'name': 'size', 'type': 'usize'}, {'name': 'data', 'type': '*const u8_'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:15 `None` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:55 `no_run` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:59 `request_internal` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:60 `request_internal` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:85 `as_raw` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:50 `/// let blob = fw.data();`
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:51 `///`
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:52 `/// # Ok(())`
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:81 `RESULT_RETURN`
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:86 `AS_PTR`
- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`

## W-000015 SignatureDrift

- Risk: Low
- Score: 3.0
- Symbol: current_user_ns
- Explanation: current_user_ns changed across the selected Linux versions.
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

- .binddrift/worktrees/v6.13/rust/kernel/task.rs:368 `Kuid::into_uid_in_current_ns` unsafe=1
- safe API `Kuid::into_uid_in_current_ns`
- .binddrift/worktrees/v6.13/rust/kernel/task.rs:363 `///`
- .binddrift/worktrees/v6.13/rust/kernel/task.rs:364 `/// Uses the namespace of the current task.`
- .binddrift/worktrees/v6.13/rust/kernel/task.rs:367 `// SAFETY: Just an FFI call.`
- wrapper_fix: `8ad1a41f7e23287f07a3516c700bc32501d4f104`

## W-000005 SignatureDrift

- Risk: Low
- Score: 2.0
- Symbol: __mutex_init
- Explanation: __mutex_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'mutex', 'type': '*mut mutex'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'key', 'type': '*mut lock_class_key'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'mutex', 'type': '*mut mutex'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'key', 'type': '*mut lock_class_key'}], 'return_type': '()'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/sync/lock/mutex.rs:104 `example` unsafe=1
- .binddrift/worktrees/v6.13/rust/kernel/sync/lock/mutex.rs:102 `// SAFETY: The safety requirements ensure that `ptr` is valid for writes, and `name` and`
- wrapper_fix: `d065cc76054d21e48a839a2a19ba99dbc51a4d11`

## W-000013 SignatureDrift

- Risk: Low
- Score: 2.0
- Symbol: compat_ptr_ioctl
- Explanation: compat_ptr_ioctl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'file', 'type': '*mut file'}, {'name': 'cmd', 'type': 'core::ffi::c_uint'}, {'name': 'arg', 'type': 'core::ffi::c_ulong'}], 'return_type': 'core::ffi::c_long'}`
- New: `{'params': [{'name': 'file', 'type': '*mut file'}, {'name': 'cmd', 'type': 'ffi::c_uint'}, {'name': 'arg', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_long'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/miscdevice.rs:164 `None` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/miscdevice.rs:168 `// SAFETY: All zeros is a valid value for `bindings::file_operations`.`
- wrapper_fix: `68aabb29a5469e4b7358e70e64a7fac433e27f06`

## W-000019 SignatureDrift

- Risk: Low
- Score: 2.0
- Symbol: firmware_request_nowarn
- Explanation: firmware_request_nowarn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'fw', 'type': '*mut *const firmware'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'device', 'type': '*mut device'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'fw', 'type': '*mut *const firmware'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'device', 'type': '*mut device'}], 'return_type': 'ffi::c_int'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:24 `request_nowarn` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:28 `/// Abstraction around a C `struct firmware`.`
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:29 `///`
- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`

## W-000021 SignatureDrift

- Risk: Low
- Score: 0.0
- Symbol: from_kuid
- Explanation: from_kuid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/task.rs:368 `Kuid::into_uid_in_current_ns` unsafe=1
- safe API `Kuid::into_uid_in_current_ns`
- wrapper_fix: `8ad1a41f7e23287f07a3516c700bc32501d4f104`

## W-000026 SignatureDrift

- Risk: Low
- Score: -1.0
- Symbol: queue_work_on
- Explanation: queue_work_on changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'cpu', 'type': 'core::ffi::c_int'}, {'name': 'wq', 'type': '*mut workqueue_struct'}, {'name': 'work', 'type': '*mut work_struct'}], 'return_type': 'bool_'}`
- New: `{'params': [{'name': 'cpu', 'type': 'ffi::c_int'}, {'name': 'wq', 'type': '*mut workqueue_struct'}, {'name': 'work', 'type': '*mut work_struct'}], 'return_type': 'bool_'}`

### Score Breakdown

- direct_rust_use: `4.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/workqueue.rs:197 `print_2_later` unsafe=1
- wrapper_fix: `d4d791d4aac041fde6eeba0a8f9201d728b52373`

## W-000027 SignatureDrift

- Risk: Low
- Score: -1.0
- Symbol: request_firmware
- Explanation: request_firmware changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'fw', 'type': '*mut *const firmware'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'device', 'type': '*mut device'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'fw', 'type': '*mut *const firmware'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'device', 'type': '*mut device'}], 'return_type': 'ffi::c_int'}`

### Score Breakdown

- direct_rust_use: `4.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:20 `request` unsafe=0
- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`

## W-000032 SignatureDrift

- Risk: Low
- Score: -1.0
- Symbol: uid_eq
- Explanation: uid_eq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/task.rs:376 `eq` unsafe=1
- .binddrift/worktrees/v6.13/rust/kernel/task.rs:375 `// SAFETY: Just an FFI call.`
- wrapper_fix: `8ad1a41f7e23287f07a3516c700bc32501d4f104`

## W-000006 SignatureDrift

- Risk: Low
- Score: -5.0
- Symbol: _find_last_bit
- Explanation: _find_last_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'addr', 'type': '*const core::ffi::c_ulong'}, {'name': 'size', 'type': 'core::ffi::c_ulong'}], 'return_type': 'core::ffi::c_ulong'}`
- New: `{'params': [{'name': 'addr', 'type': '*const ffi::c_ulong'}, {'name': 'size', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_ulong'}`

### Score Breakdown

- binding_only_penalty: `-5.0`

### Rust Evidence

- wrapper_fix: `11eca92a2caebcc2b3b65ca290385ff4b0498946`

## W-000007 SignatureDrift

- Risk: Low
- Score: -5.0
- Symbol: _find_next_bit
- Explanation: _find_next_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'addr1', 'type': '*const core::ffi::c_ulong'}, {'name': 'nbits', 'type': 'core::ffi::c_ulong'}, {'name': 'start', 'type': 'core::ffi::c_ulong'}], 'return_type': 'core::ffi::c_ulong'}`
- New: `{'params': [{'name': 'addr1', 'type': '*const ffi::c_ulong'}, {'name': 'nbits', 'type': 'ffi::c_ulong'}, {'name': 'start', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_ulong'}`

### Score Breakdown

- binding_only_penalty: `-5.0`

### Rust Evidence

- wrapper_fix: `11eca92a2caebcc2b3b65ca290385ff4b0498946`

## W-000008 SignatureDrift

- Risk: Low
- Score: -5.0
- Symbol: _find_next_zero_bit
- Explanation: _find_next_zero_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'addr', 'type': '*const core::ffi::c_ulong'}, {'name': 'nbits', 'type': 'core::ffi::c_ulong'}, {'name': 'start', 'type': 'core::ffi::c_ulong'}], 'return_type': 'core::ffi::c_ulong'}`
- New: `{'params': [{'name': 'addr', 'type': '*const ffi::c_ulong'}, {'name': 'nbits', 'type': 'ffi::c_ulong'}, {'name': 'start', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_ulong'}`

### Score Breakdown

- binding_only_penalty: `-5.0`

### Rust Evidence

- wrapper_fix: `11eca92a2caebcc2b3b65ca290385ff4b0498946`

## W-000009 SignatureDrift

- Risk: Low
- Score: -5.0
- Symbol: bitmap_free
- Explanation: bitmap_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'bitmap', 'type': '*const core::ffi::c_ulong'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'bitmap', 'type': '*const ffi::c_ulong'}], 'return_type': '()'}`

### Score Breakdown

- binding_only_penalty: `-5.0`

### Rust Evidence

- wrapper_fix: `11eca92a2caebcc2b3b65ca290385ff4b0498946`

## W-000010 SignatureDrift

- Risk: Low
- Score: -5.0
- Symbol: bitmap_zalloc
- Explanation: bitmap_zalloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'nbits', 'type': 'core::ffi::c_uint'}, {'name': 'flags', 'type': 'gfp_t'}], 'return_type': '*mut core::ffi::c_ulong'}`
- New: `{'params': [{'name': 'nbits', 'type': 'ffi::c_uint'}, {'name': 'flags', 'type': 'gfp_t'}], 'return_type': '*mut ffi::c_ulong'}`

### Score Breakdown

- binding_only_penalty: `-5.0`

### Rust Evidence

- wrapper_fix: `11eca92a2caebcc2b3b65ca290385ff4b0498946`

## W-000011 SignatureDrift

- Risk: Low
- Score: -5.0
- Symbol: blk_queue_flag_clear
- Explanation: blk_queue_flag_clear changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'flag', 'type': 'core::ffi::c_uint'}, {'name': 'q', 'type': '*mut request_queue'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'flag', 'type': 'ffi::c_uint'}, {'name': 'q', 'type': '*mut request_queue'}], 'return_type': '()'}`

### Score Breakdown

- binding_only_penalty: `-5.0`

### Rust Evidence

- wrapper_fix: `5ddb88f22eb97218d9295e69c39e0ff7cc64e09c`

## W-000012 SignatureDrift

- Risk: Low
- Score: -5.0
- Symbol: blk_queue_flag_set
- Explanation: blk_queue_flag_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'flag', 'type': 'core::ffi::c_uint'}, {'name': 'q', 'type': '*mut request_queue'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'flag', 'type': 'ffi::c_uint'}, {'name': 'q', 'type': '*mut request_queue'}], 'return_type': '()'}`

### Score Breakdown

- binding_only_penalty: `-5.0`

### Rust Evidence

- wrapper_fix: `5ddb88f22eb97218d9295e69c39e0ff7cc64e09c`

## W-000020 SignatureDrift

- Risk: Low
- Score: -5.0
- Symbol: firmware_request_platform
- Explanation: firmware_request_platform changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'fw', 'type': '*mut *const firmware'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'device', 'type': '*mut device'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'fw', 'type': '*mut *const firmware'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'device', 'type': '*mut device'}], 'return_type': 'ffi::c_int'}`

### Score Breakdown

- binding_only_penalty: `-5.0`

### Rust Evidence

- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`

## W-000028 SignatureDrift

- Risk: Low
- Score: -5.0
- Symbol: request_firmware_direct
- Explanation: request_firmware_direct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'fw', 'type': '*mut *const firmware'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'device', 'type': '*mut device'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'fw', 'type': '*mut *const firmware'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'device', 'type': '*mut device'}], 'return_type': 'ffi::c_int'}`

### Score Breakdown

- binding_only_penalty: `-5.0`

### Rust Evidence

- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`

## W-000035 FieldDrift

- Risk: Low
- Score: -5.0
- Symbol: kunit_case
- Explanation: kunit_case changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'run_case', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'generate_params', 'type': '::core::option::Option<'}, {'name': 'attr', 'type': 'kunit_attributes'}, {'name': 'status', 'type': 'kunit_status'}, {'name': 'module_name', 'type': '*mut core::ffi::c_char'}, {'name': 'log', 'type': '*mut string_stream'}]`
- New: `[{'name': 'run_case', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'generate_params', 'type': '::core::option::Option<'}, {'name': 'attr', 'type': 'kunit_attributes'}, {'name': 'status', 'type': 'kunit_status'}, {'name': 'module_name', 'type': '*mut ffi::c_char'}, {'name': 'log', 'type': '*mut string_stream'}]`

### Score Breakdown

- binding_only_penalty: `-5.0`

### Rust Evidence

- wrapper_fix: `7f87c7a003125d5af5ec7abbbc0ac21b4a4661ae`
- wrapper_fix: `be97f3c82021239476ce32cddde32948c597753e`
