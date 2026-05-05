# BindDrift Ranked Warnings

## W-000009 SignatureDrift

- Risk: High
- Score: 20.0
- Symbol: ERR_PTR
- Explanation: ERR_PTR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['-ENODEV'], 'return_type': 'return'}`
- New: `{'params': ['-EINVAL'], 'return_type': 'return'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`
- wrapper_fix_hit: `4.0`
- multi_version_consistency: `2.0`

### Rust Evidence

- .binddrift/worktrees/v6.11/rust/kernel/error.rs:139 `Error::to_blk_status` unsafe=1
- safe API `Error::to_blk_status`
- .binddrift/worktrees/v6.11/rust/kernel/error.rs:135 `/// Returns the error encoded as a pointer.`
- .binddrift/worktrees/v6.11/rust/kernel/error.rs:138 `// SAFETY: `self.0` is a valid error due to its invariant.`
- wrapper_fix: `c7e20faa5fcad7a177cf6c306138010343dd6d3e`
- wrapper_fix: `7bc186731e87482662c4f86da455f435fe838fb6`
- wrapper_fix: `e9759c5b9ea555d09f426c70c880e9522e9b0576`

## W-000006 SignatureDrift

- Risk: High
- Score: 19.0
- Symbol: PTR_ERR
- Explanation: PTR_ERR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['ptr'], 'return_type': 'return'}`
- New: `{'params': ['opp'], 'return_type': 'return'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`
- multi_version_consistency: `2.0`

### Rust Evidence

- .binddrift/worktrees/v6.16/rust/kernel/error.rs:414 `From<core::convert::Infallible>::to_result` unsafe=1
- safe API `From<core::convert::Infallible>::to_result`
- .binddrift/worktrees/v6.16/rust/kernel/error.rs:411 `// SAFETY: The FFI function does not deref the pointer.`
- .binddrift/worktrees/v6.16/rust/kernel/error.rs:413 `// SAFETY: The FFI function does not deref the pointer.`
- .binddrift/worktrees/v6.16/rust/kernel/error.rs:412 `IS_ERR_MAPPING`
- wrapper_fix: `752417b3f0e7721f1d630f40da22d57e0dae043e`

## W-000018 SignatureDrift

- Risk: High
- Score: 17.0
- Symbol: security_secid_to_secctx
- Explanation: security_secid_to_secctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u32 secid', 'char **secdata', 'u32 *seclen'], 'return_type': 'static inline int'}`
- New: `{'params': ['u32 secid', 'struct lsm_context *cp'], 'return_type': 'static inline int'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.14/rust/kernel/security.rs:31 `SecurityCtx::from_secid` unsafe=1
- safe API `SecurityCtx::from_secid`
- .binddrift/worktrees/v6.14/rust/kernel/security.rs:27 `// SAFETY: `struct lsm_context` can be initialized to all zeros.`
- .binddrift/worktrees/v6.14/rust/kernel/security.rs:30 `// SAFETY: Just a C FFI call. The pointer is valid for writes.`
- .binddrift/worktrees/v6.14/rust/kernel/security.rs:26 `RESULT_RETURN`
- .binddrift/worktrees/v6.14/rust/kernel/security.rs:31 `TO_RESULT_MAPPING`

## W-000003 SignatureDrift

- Risk: High
- Score: 17.0
- Symbol: kmap_local_page
- Explanation: kmap_local_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['scatterwalk_page(walk)) + offset_in_page(walk->offset'], 'return_type': 'return'}`
- New: `{'params': ['page'], 'return_type': 'return'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.15/rust/kernel/page.rs:105 `Page::as_ptr` unsafe=1
- safe API `Page::as_ptr`
- .binddrift/worktrees/v6.15/rust/kernel/page.rs:100 `/// different addresses. However, even if the addresses are different, the underlying memory is`
- .binddrift/worktrees/v6.15/rust/kernel/page.rs:101 `/// still the same for these purposes (e.g., it's still a data race if they both write to the`
- .binddrift/worktrees/v6.15/rust/kernel/page.rs:102 `/// same underlying byte at the same time).`
- .binddrift/worktrees/v6.15/rust/kernel/page.rs:105 `AS_PTR`

## W-000181 SignatureDrift

- Risk: High
- Score: 17.0
- Symbol: vma_lookup
- Explanation: vma_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['mm', 'addr'], 'return_type': 'return'}`
- New: `{'params': ['struct mm_struct *mm', 'unsigned long addr'], 'return_type': 'static inline struct vm_area_struct *'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.18/rust/kernel/mm.rs:247 `MmapReadGuard<::vma_lookup` unsafe=1
- safe API `MmapReadGuard<::vma_lookup`
- .binddrift/worktrees/v6.18/rust/kernel/mm.rs:242 `/// Look up a vma at the given address.`
- .binddrift/worktrees/v6.18/rust/kernel/mm.rs:245 `// SAFETY: By the type invariants we hold the mmap read guard, so we can safely call this`
- .binddrift/worktrees/v6.18/rust/kernel/mm.rs:252 `// SAFETY: We just checked that a vma was found, so the pointer references a valid vma.`
- .binddrift/worktrees/v6.18/rust/kernel/mm.rs:244 `OPTION_RETURN`

## W-000011 SignatureDrift

- Risk: High
- Score: 17.0
- Symbol: resource_size_t
- Explanation: resource_size_t changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['*resource_alignf)(void *data, const struct resource *res, resource_size_t size, resource_size_t align'], 'return_type': 'typedef'}`
- New: `{'params': ['*resource_alignf)(void *data, const struct resource *res, const struct resource *empty_res, resource_size_t size, resource_size_t align'], 'return_type': 'typedef'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/io.rs:32 `None` unsafe=0
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/pci.rs:417 `Device::subsystem_device_id` unsafe=0
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/pci.rs:429 `Device::resource_start` unsafe=0
- safe API `Device::subsystem_device_id`
- safe API `Device::resource_start`
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/io.rs:28 `/// Resource Size type.`
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/io.rs:29 `///`
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/io.rs:30 `/// This is a type alias to either `u32` or `u64` depending on the config option`
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/pci.rs:417 `RESULT_RETURN`
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/pci.rs:429 `RESULT_RETURN`

## W-000004 SignatureDrift

- Risk: High
- Score: 15.0
- Symbol: mdiobus_read
- Explanation: mdiobus_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['phydev->mdio.bus', 'addr', 'regnum'], 'return_type': 'return'}`
- New: `{'params': ['phydev->mdio.bus', 'phydev->mdio.addr', 'regnum'], 'return_type': 'return'}`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`
- multi_version_consistency: `2.0`

### Rust Evidence

- .binddrift/worktrees/v6.15/rust/kernel/net/phy/reg.rs:111 `read` unsafe=1
- .binddrift/worktrees/v6.15/rust/kernel/net/phy/reg.rs:107 `// SAFETY: `phydev` is pointing to a valid object by the type invariant of `Device`.`
- .binddrift/worktrees/v6.15/rust/kernel/net/phy/reg.rs:113 `TO_RESULT_MAPPING`
- wrapper_fix: `b2e47002b2350f57bfa8fe1c231e9fbb6baef78b`

## W-000005 SignatureDrift

- Risk: High
- Score: 15.0
- Symbol: mdiobus_write
- Explanation: mdiobus_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['phydev->mdio.bus', 'addr', 'regnum', 'val'], 'return_type': 'return'}`
- New: `{'params': ['phydev->mdio.bus', 'phydev->mdio.addr', 'regnum', 'val'], 'return_type': 'return'}`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`
- multi_version_consistency: `2.0`

### Rust Evidence

- .binddrift/worktrees/v6.15/rust/kernel/net/phy/reg.rs:123 `write` unsafe=1
- .binddrift/worktrees/v6.15/rust/kernel/net/phy/reg.rs:119 `// SAFETY: `phydev` is pointing to a valid object by the type invariant of `Device`.`
- .binddrift/worktrees/v6.15/rust/kernel/net/phy/reg.rs:122 `TO_RESULT_MAPPING`
- wrapper_fix: `b2e47002b2350f57bfa8fe1c231e9fbb6baef78b`

## W-000002 FieldDrift

- Risk: High
- Score: 15.0
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
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.12/rust/kernel/device.rs:38 `None` unsafe=0
- .binddrift/worktrees/v6.12/rust/kernel/device.rs:41 `None` unsafe=0
- .binddrift/worktrees/v6.12/rust/kernel/device.rs:52 `None` unsafe=0
- .binddrift/worktrees/v6.12/rust/kernel/device.rs:54 `None` unsafe=0
- .binddrift/worktrees/v6.12/rust/kernel/device.rs:60 `Device::get_device` unsafe=0
- safe API `Device::get_device`
- safe API `Device::as_raw`
- .binddrift/worktrees/v6.12/rust/kernel/device.rs:33 `/// A `Device` instance represents a valid `struct device` created by the C portion of the kernel.`
- .binddrift/worktrees/v6.12/rust/kernel/device.rs:34 `///`
- .binddrift/worktrees/v6.12/rust/kernel/device.rs:35 `/// Instances of this type are always reference-counted, that is, a call to `get_device` ensures`
- .binddrift/worktrees/v6.12/rust/kernel/device.rs:38 `AREF`
- .binddrift/worktrees/v6.12/rust/kernel/device.rs:38 `AREF`
- .binddrift/worktrees/v6.12/rust/kernel/device.rs:38 `AREF`
- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`
- wrapper_fix: `4d320e30ee04c25c660eca2bb33e846ebb71a79a`

## W-000003 FieldDrift

- Risk: High
- Score: 15.0
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
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.12/rust/kernel/block/mq/operations.rs:123 `commit_rqs_callback` unsafe=0
- .binddrift/worktrees/v6.12/rust/kernel/block/mq/operations.rs:173 `complete_callback` unsafe=0
- .binddrift/worktrees/v6.12/rust/kernel/block/mq/operations.rs:178 `complete_callback` unsafe=0
- .binddrift/worktrees/v6.12/rust/kernel/block/mq/operations.rs:205 `complete_callback` unsafe=0
- .binddrift/worktrees/v6.12/rust/kernel/block/mq/request.rs:53 `None` unsafe=0
- safe API `Request<T>::start_unchecked`
- safe API `Request<T>::wrapper_ptr`
- .binddrift/worktrees/v6.12/rust/kernel/block/mq/operations.rs:118 `/// implemented, and there is no way to exercise this code path.`
- .binddrift/worktrees/v6.12/rust/kernel/block/mq/operations.rs:119 `///`
- .binddrift/worktrees/v6.12/rust/kernel/block/mq/operations.rs:120 `/// # Safety`
- .binddrift/worktrees/v6.12/rust/kernel/block/mq/request.rs:67 `NONNULL_MAPPING`
- .binddrift/worktrees/v6.12/rust/kernel/block/mq/request.rs:93 `RESULT_RETURN`
- .binddrift/worktrees/v6.12/rust/kernel/block/mq/request.rs:53 `OPAQUE`
- .binddrift/worktrees/v6.12/rust/kernel/block/mq/request.rs:56 `AREF`
- .binddrift/worktrees/v6.12/rust/kernel/block/mq/request.rs:63 `AREF`
- wrapper_fix: `28e848386b92645f93b9f2fdba5882c3ca7fb3e2`
- wrapper_fix: `a307bf1db5448eccd72a1d7857f7661c6330d5ad`

## W-000004 SignatureDrift

- Risk: High
- Score: 15.0
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
- wrapper_fix_hit: `4.0`
- multi_version_consistency: `2.0`
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

## W-000033 FieldDrift

- Risk: High
- Score: 15.0
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
- wrapper_fix_hit: `4.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/device.rs:41 `None` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/device.rs:44 `None` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/device.rs:55 `None` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/device.rs:57 `None` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/device.rs:63 `Device::get_device` unsafe=0
- safe API `Device::get_device`
- safe API `Device::as_raw`
- .binddrift/worktrees/v6.13/rust/kernel/device.rs:36 `/// A `Device` instance represents a valid `struct device` created by the C portion of the kernel.`
- .binddrift/worktrees/v6.13/rust/kernel/device.rs:37 `///`
- .binddrift/worktrees/v6.13/rust/kernel/device.rs:38 `/// Instances of this type are always reference-counted, that is, a call to `get_device` ensures`
- .binddrift/worktrees/v6.13/rust/kernel/device.rs:41 `AREF`
- .binddrift/worktrees/v6.13/rust/kernel/device.rs:41 `AREF`
- .binddrift/worktrees/v6.13/rust/kernel/device.rs:41 `AREF`
- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`
- wrapper_fix: `4d320e30ee04c25c660eca2bb33e846ebb71a79a`

## W-000038 FieldDrift

- Risk: High
- Score: 15.0
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
- wrapper_fix_hit: `4.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/block/mq/operations.rs:123 `commit_rqs_callback` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/operations.rs:173 `complete_callback` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/operations.rs:178 `complete_callback` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/operations.rs:205 `complete_callback` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/request.rs:56 `None` unsafe=0
- safe API `Request<T>::start_unchecked`
- safe API `Request<T>::wrapper_ptr`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/operations.rs:118 `/// implemented, and there is no way to exercise this code path.`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/operations.rs:119 `///`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/operations.rs:120 `/// # Safety`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/request.rs:72 `NONNULL_MAPPING`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/request.rs:100 `RESULT_RETURN`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/request.rs:56 `OPAQUE`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/request.rs:59 `AREF`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/request.rs:68 `AREF`
- wrapper_fix: `28e848386b92645f93b9f2fdba5882c3ca7fb3e2`
- wrapper_fix: `a307bf1db5448eccd72a1d7857f7661c6330d5ad`

## W-000014 FieldDrift

- Risk: High
- Score: 15.0
- Symbol: pci_dev
- Explanation: pci_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 11usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': 'match_driver', 'type': 'bool_'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 5usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pri_cap', 'type': 'u16_'}, {'name': 'pri_reqs_alloc', 'type': 'u32_'}, {'name': '_bitfield_align_5', 'type': '[u8; 0]'}, {'name': '_bitfield_5', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.14/rust/kernel/pci.rs:58 `None` unsafe=0
- .binddrift/worktrees/v6.14/rust/kernel/pci.rs:86 `None` unsafe=0
- .binddrift/worktrees/v6.14/rust/kernel/pci.rs:359 `None` unsafe=0
- .binddrift/worktrees/v6.14/rust/kernel/pci.rs:364 `Device::from_dev` unsafe=0
- .binddrift/worktrees/v6.14/rust/kernel/pci.rs:367 `as_raw` unsafe=1
- safe API `Device::from_dev`
- .binddrift/worktrees/v6.14/rust/kernel/pci.rs:354 `/// Create a PCI Device instance from an existing `device::Device`.`
- .binddrift/worktrees/v6.14/rust/kernel/pci.rs:355 `///`
- .binddrift/worktrees/v6.14/rust/kernel/pci.rs:356 `/// # Safety`
- .binddrift/worktrees/v6.14/rust/kernel/pci.rs:358 `AREF`
- .binddrift/worktrees/v6.14/rust/kernel/pci.rs:360 `AREF`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`

## W-000015 FieldDrift

- Risk: High
- Score: 15.0
- Symbol: platform_device
- Explanation: platform_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'id_auto', 'type': 'bool_'}, {'name': 'dev', 'type': 'device'}, {'name': 'platform_dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'num_resources', 'type': 'u32_'}, {'name': 'resource', 'type': '*mut resource'}, {'name': 'id_entry', 'type': '*const platform_device_id'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'mfd_cell', 'type': '*mut mfd_cell'}, {'name': 'archdata', 'type': 'pdev_archdata'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.14/rust/kernel/error.rs:323 `From<core::convert::Infallible>::to_result` unsafe=0
- .binddrift/worktrees/v6.14/rust/kernel/platform.rs:56 `None` unsafe=0
- .binddrift/worktrees/v6.14/rust/kernel/platform.rs:77 `probe_callback` unsafe=0
- .binddrift/worktrees/v6.14/rust/kernel/platform.rs:184 `None` unsafe=0
- .binddrift/worktrees/v6.14/rust/kernel/platform.rs:189 `from_dev` unsafe=0
- safe API `From<core::convert::Infallible>::to_result`
- .binddrift/worktrees/v6.14/rust/kernel/error.rs:318 `///`
- .binddrift/worktrees/v6.14/rust/kernel/error.rs:319 `/// ```ignore`
- .binddrift/worktrees/v6.14/rust/kernel/error.rs:320 `/// # use kernel::from_result;`
- .binddrift/worktrees/v6.14/rust/kernel/platform.rs:185 `AREF`
- wrapper_fix: `ef4dc4cc7001e9cce8a3b556362171648be9ad92`
- wrapper_fix: `4d320e30ee04c25c660eca2bb33e846ebb71a79a`
- wrapper_fix: `0242623384c767b1156b61b67894b4ecf6682b8b`

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

## W-000180 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: queue_work_on
- Explanation: queue_work_on changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['cpu', 'system_wq', 'work'], 'return_type': 'return'}`
- New: `{'params': ['cpu', 'system_percpu_wq', 'work'], 'return_type': 'return'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`
- multi_version_consistency: `2.0`

### Rust Evidence

- .binddrift/worktrees/v6.18/rust/kernel/workqueue.rs:276 `print_now` unsafe=0
- .binddrift/worktrees/v6.18/rust/kernel/workqueue.rs:281 `print_now` unsafe=0
- .binddrift/worktrees/v6.18/rust/kernel/workqueue.rs:286 `print_now` unsafe=1
- .binddrift/worktrees/v6.18/rust/kernel/workqueue.rs:273 `// SAFETY: We only return `false` if the `work_struct` is already in a workqueue. The other`
- wrapper_fix: `d4d791d4aac041fde6eeba0a8f9201d728b52373`

## W-000001 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: REFCOUNT_INIT
- Explanation: REFCOUNT_INIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:156 `Arc<T>::try_new` unsafe=1
- safe API `Arc<T>::try_new`
- .binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:151 `/// Constructs a new reference counted instance of `T`.`
- .binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:155 `// SAFETY: There are no safety requirements for this FFI call.`
- .binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:152 `RESULT_RETURN`
- weak lifetime name .binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:156 `LIFETIME_NAMING_PATTERN`
- wrapper_fix: `bb38f35b35f9de0cebc4d62ea73482454e38cef3`
- wrapper_fix: `076acb647c1f448177d8b3b0e4f33de959713d7d`
- wrapper_fix: `9ba1aaf25ab7dadb910348b6857865e87b4c5689`

## W-000001 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: errname
- Explanation: errname changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.5/rust/kernel/error.rs:144 `Error::name` unsafe=1
- safe API `Error::name`
- safe API `Error::name`
- .binddrift/worktrees/v6.5/rust/kernel/error.rs:140 `/// Returns a string representing the error, if one exists.`
- .binddrift/worktrees/v6.5/rust/kernel/error.rs:143 `// SAFETY: Just an FFI call, there are no extra safety requirements.`
- .binddrift/worktrees/v6.5/rust/kernel/error.rs:148 `// SAFETY: The string returned by `errname` is static and `NUL`-terminated.`
- .binddrift/worktrees/v6.5/rust/kernel/error.rs:142 `OPTION_RETURN`
- wrapper_fix: `d2e3115d717197cb2bc020dd1f06b06538474ac3`
- wrapper_fix: `e9759c5b9ea555d09f426c70c880e9522e9b0576`

## W-000003 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: mdiobus_write
- Explanation: mdiobus_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.8/rust/kernel/net/phy.rs:202 `Device::write` unsafe=1
- safe API `Device::write`
- .binddrift/worktrees/v6.8/rust/kernel/net/phy.rs:198 `// SAFETY: `phydev` is pointing to a valid object by the type invariant of `Self`.`
- .binddrift/worktrees/v6.8/rust/kernel/net/phy.rs:201 `TO_RESULT_MAPPING`
- wrapper_fix: `b2e47002b2350f57bfa8fe1c231e9fbb6baef78b`

## W-000003 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: device_add_disk
- Explanation: device_add_disk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.11/rust/kernel/block/mq/gen_disk.rs:160 `GenDiskBuilder::capacity_sectors` unsafe=1
- .binddrift/worktrees/v6.11/rust/kernel/block/mq/gen_disk.rs:179 `None` unsafe=0
- safe API `GenDiskBuilder::capacity_sectors`
- .binddrift/worktrees/v6.11/rust/kernel/block/mq/gen_disk.rs:157 `// SAFETY: `gendisk` points to a valid and initialized instance of`
- .binddrift/worktrees/v6.11/rust/kernel/block/mq/gen_disk.rs:174 `///`
- .binddrift/worktrees/v6.11/rust/kernel/block/mq/gen_disk.rs:175 `/// # Invariants`
- .binddrift/worktrees/v6.11/rust/kernel/block/mq/gen_disk.rs:156 `TO_RESULT_MAPPING`
- wrapper_fix: `0c5928deada15a8d075516e6e0d9ee19011bb000`

## W-000002 SignatureDrift

- Risk: Medium
- Score: 11.0
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
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/error.rs:295 `From<core::convert::Infallible>::to_result` unsafe=1
- safe API `From<core::convert::Infallible>::to_result`
- .binddrift/worktrees/v6.13/rust/kernel/error.rs:290 `/// ````
- .binddrift/worktrees/v6.13/rust/kernel/error.rs:291 `ERR_PTR_MAPPING`
- .binddrift/worktrees/v6.13/rust/kernel/error.rs:291 `RESULT_RETURN`
- wrapper_fix: `752417b3f0e7721f1d630f40da22d57e0dae043e`

## W-000003 SignatureDrift

- Risk: Medium
- Score: 11.0
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
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/error.rs:297 `From<core::convert::Infallible>::to_result` unsafe=1
- safe API `From<core::convert::Infallible>::to_result`
- .binddrift/worktrees/v6.13/rust/kernel/error.rs:294 `// SAFETY: The FFI function does not deref the pointer.`
- .binddrift/worktrees/v6.13/rust/kernel/error.rs:296 `// SAFETY: The FFI function does not deref the pointer.`
- .binddrift/worktrees/v6.13/rust/kernel/error.rs:295 `IS_ERR_MAPPING`
- wrapper_fix: `752417b3f0e7721f1d630f40da22d57e0dae043e`

## W-000016 SignatureDrift

- Risk: Medium
- Score: 11.0
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
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/block/mq/gen_disk.rs:160 `GenDiskBuilder::capacity_sectors` unsafe=1
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/gen_disk.rs:179 `None` unsafe=0
- safe API `GenDiskBuilder::capacity_sectors`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/gen_disk.rs:157 `// SAFETY: `gendisk` points to a valid and initialized instance of`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/gen_disk.rs:174 `///`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/gen_disk.rs:175 `/// # Invariants`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/gen_disk.rs:156 `TO_RESULT_MAPPING`
- wrapper_fix: `0c5928deada15a8d075516e6e0d9ee19011bb000`

## W-000017 SignatureDrift

- Risk: Medium
- Score: 11.0
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
- multi_version_consistency: `2.0`
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

## W-000019 SignatureDrift

- Risk: Medium
- Score: 11.0
- Symbol: firmware_request_nowarn
- Explanation: firmware_request_nowarn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'fw', 'type': '*mut *const firmware'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'device', 'type': '*mut device'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'fw', 'type': '*mut *const firmware'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'device', 'type': '*mut device'}], 'return_type': 'ffi::c_int'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:12 `None` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:24 `request_nowarn` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:80 `Firmware::request` unsafe=0
- safe API `Firmware::request`
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:28 `/// Abstraction around a C `struct firmware`.`
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:29 `///`
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:79 `/// Send a request for an optional firmware module. See also`
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:75 `RESULT_RETURN`
- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`

## W-000036 FieldDrift

- Risk: Medium
- Score: 11.0
- Symbol: queue_limits
- Explanation: queue_limits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'core::ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'core::ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'max_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'core::ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'core::ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'core::ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'core::ffi::c_uint'}, {'name': 'io_min', 'type': 'core::ffi::c_uint'}, {'name': 'io_opt', 'type': 'core::ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'core::ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'core::ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'core::ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'core::ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'core::ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'core::ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'core::ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'core::ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'core::ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'core::ffi::c_uint'}, {'name': 'max_segments', 'type': 'core::ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'core::ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'core::ffi::c_ushort'}, {'name': 'max_open_zones', 'type': 'core::ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'core::ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'core::ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'core::ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`
- New: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/block/mq/gen_disk.rs:96 `GenDiskBuilder::capacity_sectors` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/gen_disk.rs:97 `GenDiskBuilder::capacity_sectors` unsafe=1
- safe API `GenDiskBuilder::capacity_sectors`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/gen_disk.rs:96 `// SAFETY: `bindings::queue_limits` contain only fields that are valid when zeroed.`
- .binddrift/worktrees/v6.13/rust/kernel/block/mq/gen_disk.rs:95 `RESULT_RETURN`
- wrapper_fix: `5e3b7009f116f684ac6b93d8924506154f3b1f6d`

## W-000016 FieldDrift

- Risk: Medium
- Score: 11.0
- Symbol: queue_limits
- Explanation: queue_limits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`
- New: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'min_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.14/rust/kernel/block/mq/gen_disk.rs:96 `GenDiskBuilder::capacity_sectors` unsafe=0
- .binddrift/worktrees/v6.14/rust/kernel/block/mq/gen_disk.rs:97 `GenDiskBuilder::capacity_sectors` unsafe=1
- safe API `GenDiskBuilder::capacity_sectors`
- .binddrift/worktrees/v6.14/rust/kernel/block/mq/gen_disk.rs:96 `// SAFETY: `bindings::queue_limits` contain only fields that are valid when zeroed.`
- .binddrift/worktrees/v6.14/rust/kernel/block/mq/gen_disk.rs:95 `RESULT_RETURN`
- wrapper_fix: `5e3b7009f116f684ac6b93d8924506154f3b1f6d`

## W-000005 FieldDrift

- Risk: Medium
- Score: 11.0
- Symbol: queue_limits
- Explanation: queue_limits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'min_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`
- New: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'min_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_write_streams', 'type': 'ffi::c_ushort'}, {'name': 'write_stream_granularity', 'type': 'ffi::c_uint'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.16/rust/kernel/block/mq/gen_disk.rs:96 `GenDiskBuilder::capacity_sectors` unsafe=0
- .binddrift/worktrees/v6.16/rust/kernel/block/mq/gen_disk.rs:97 `GenDiskBuilder::capacity_sectors` unsafe=1
- safe API `GenDiskBuilder::capacity_sectors`
- .binddrift/worktrees/v6.16/rust/kernel/block/mq/gen_disk.rs:96 `// SAFETY: `bindings::queue_limits` contain only fields that are valid when zeroed.`
- .binddrift/worktrees/v6.16/rust/kernel/block/mq/gen_disk.rs:95 `RESULT_RETURN`
- wrapper_fix: `5e3b7009f116f684ac6b93d8924506154f3b1f6d`

## W-000010 FieldDrift

- Risk: Medium
- Score: 11.0
- Symbol: queue_limits
- Explanation: queue_limits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'min_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_write_streams', 'type': 'ffi::c_ushort'}, {'name': 'write_stream_granularity', 'type': 'ffi::c_uint'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`
- New: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'min_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_write_streams', 'type': 'ffi::c_ushort'}, {'name': 'write_stream_granularity', 'type': 'ffi::c_uint'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.17/rust/kernel/block/mq/gen_disk.rs:96 `GenDiskBuilder::capacity_sectors` unsafe=0
- .binddrift/worktrees/v6.17/rust/kernel/block/mq/gen_disk.rs:97 `GenDiskBuilder::capacity_sectors` unsafe=1
- safe API `GenDiskBuilder::capacity_sectors`
- .binddrift/worktrees/v6.17/rust/kernel/block/mq/gen_disk.rs:96 `// SAFETY: `bindings::queue_limits` contain only fields that are valid when zeroed.`
- .binddrift/worktrees/v6.17/rust/kernel/block/mq/gen_disk.rs:95 `RESULT_RETURN`
- wrapper_fix: `5e3b7009f116f684ac6b93d8924506154f3b1f6d`

## W-000002 FieldDrift

- Risk: Medium
- Score: 11.0
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
- multi_version_consistency: `2.0`
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

## W-000001 FieldDrift

- Risk: Medium
- Score: 11.0
- Symbol: device
- Explanation: device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'kobj', 'type': 'kobject'}, {'name': 'parent', 'type': '*mut device'}, {'name': 'p', 'type': '*mut device_private'}, {'name': 'init_name', 'type': '*const ffi::c_char'}, {'name': 'type_', 'type': '*const device_type'}, {'name': 'bus', 'type': '*const bus_type'}, {'name': 'driver', 'type': '*mut device_driver'}, {'name': 'platform_data', 'type': '*mut ffi::c_void'}, {'name': 'driver_data', 'type': '*mut ffi::c_void'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'links', 'type': 'dev_links_info'}, {'name': 'power', 'type': 'dev_pm_info'}, {'name': 'pm_domain', 'type': '*mut dev_pm_domain'}, {'name': 'msi', 'type': 'dev_msi_info'}, {'name': 'dma_mask', 'type': '*mut u64_'}, {'name': 'coherent_dma_mask', 'type': 'u64_'}, {'name': 'bus_dma_limit', 'type': 'u64_'}, {'name': 'dma_range_map', 'type': '*mut bus_dma_region'}, {'name': 'dma_parms', 'type': '*mut device_dma_parameters'}, {'name': 'dma_pools', 'type': 'list_head'}, {'name': 'dma_io_tlb_mem', 'type': '*mut io_tlb_mem'}, {'name': 'archdata', 'type': 'dev_archdata'}, {'name': 'of_node', 'type': '*mut device_node'}, {'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'numa_node', 'type': 'ffi::c_int'}, {'name': 'devt', 'type': 'dev_t'}, {'name': 'id', 'type': 'u32_'}, {'name': 'devres_lock', 'type': 'spinlock_t'}, {'name': 'devres_head', 'type': 'list_head'}, {'name': 'class', 'type': '*const class'}, {'name': 'groups', 'type': '*mut *const attribute_group'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'iommu_group', 'type': '*mut iommu_group'}, {'name': 'iommu', 'type': '*mut dev_iommu'}, {'name': 'physical_location', 'type': '*mut device_physical_location'}, {'name': 'removable', 'type': 'device_removable'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 3usize]'}]`
- New: `[{'name': 'kobj', 'type': 'kobject'}, {'name': 'parent', 'type': '*mut device'}, {'name': 'p', 'type': '*mut device_private'}, {'name': 'init_name', 'type': '*const ffi::c_char'}, {'name': 'type_', 'type': '*const device_type'}, {'name': 'bus', 'type': '*const bus_type'}, {'name': 'driver', 'type': '*mut device_driver'}, {'name': 'platform_data', 'type': '*mut ffi::c_void'}, {'name': 'driver_data', 'type': '*mut ffi::c_void'}, {'name': 'driver_override', 'type': 'device__bindgen_ty_1'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'links', 'type': 'dev_links_info'}, {'name': 'power', 'type': 'dev_pm_info'}, {'name': 'pm_domain', 'type': '*mut dev_pm_domain'}, {'name': 'msi', 'type': 'dev_msi_info'}, {'name': 'dma_mask', 'type': '*mut u64_'}, {'name': 'coherent_dma_mask', 'type': 'u64_'}, {'name': 'bus_dma_limit', 'type': 'u64_'}, {'name': 'dma_range_map', 'type': '*mut bus_dma_region'}, {'name': 'dma_parms', 'type': '*mut device_dma_parameters'}, {'name': 'dma_pools', 'type': 'list_head'}, {'name': 'dma_io_tlb_mem', 'type': '*mut io_tlb_mem'}, {'name': 'archdata', 'type': 'dev_archdata'}, {'name': 'of_node', 'type': '*mut device_node'}, {'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'numa_node', 'type': 'ffi::c_int'}, {'name': 'devt', 'type': 'dev_t'}, {'name': 'id', 'type': 'u32_'}, {'name': 'devres_lock', 'type': 'spinlock_t'}, {'name': 'devres_head', 'type': 'list_head'}, {'name': 'class', 'type': '*const class'}, {'name': 'groups', 'type': '*mut *const attribute_group'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'iommu_group', 'type': '*mut iommu_group'}, {'name': 'iommu', 'type': '*mut dev_iommu'}, {'name': 'physical_location', 'type': '*mut device_physical_location'}, {'name': 'removable', 'type': 'device_removable'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 3usize]'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v7.0/rust/kernel/auxiliary.rs:269 `Device::parent` unsafe=0
- .binddrift/worktrees/v7.0/rust/kernel/device.rs:163 `None` unsafe=0
- .binddrift/worktrees/v7.0/rust/kernel/device.rs:170 `None` unsafe=0
- .binddrift/worktrees/v7.0/rust/kernel/device.rs:181 `None` unsafe=0
- .binddrift/worktrees/v7.0/rust/kernel/device.rs:183 `None` unsafe=0
- safe API `Device::parent`
- safe API `Device<Ctx>::parent`
- safe API `Config<T>::set`
- .binddrift/worktrees/v7.0/rust/kernel/auxiliary.rs:265 `// SAFETY: A `struct auxiliary_device` always has a parent.`
- .binddrift/worktrees/v7.0/rust/kernel/device.rs:158 `/// A `Device` instance represents a valid `struct device` created by the C portion of the kernel.`
- .binddrift/worktrees/v7.0/rust/kernel/device.rs:159 `///`
- .binddrift/worktrees/v7.0/rust/kernel/device.rs:163 `AREF`
- .binddrift/worktrees/v7.0/rust/kernel/device.rs:170 `OPAQUE`
- .binddrift/worktrees/v7.0/rust/kernel/device.rs:183 `AREF`
- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`
- wrapper_fix: `4d320e30ee04c25c660eca2bb33e846ebb71a79a`

## W-000003 FieldDrift

- Risk: Medium
- Score: 11.0
- Symbol: platform_device
- Explanation: platform_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'id_auto', 'type': 'bool_'}, {'name': 'dev', 'type': 'device'}, {'name': 'platform_dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'num_resources', 'type': 'u32_'}, {'name': 'resource', 'type': '*mut resource'}, {'name': 'id_entry', 'type': '*const platform_device_id'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'mfd_cell', 'type': '*mut mfd_cell'}, {'name': 'archdata', 'type': 'pdev_archdata'}]`
- New: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'id_auto', 'type': 'bool_'}, {'name': 'dev', 'type': 'device'}, {'name': 'platform_dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'num_resources', 'type': 'u32_'}, {'name': 'resource', 'type': '*mut resource'}, {'name': 'id_entry', 'type': '*const platform_device_id'}, {'name': 'mfd_cell', 'type': '*mut mfd_cell'}, {'name': 'archdata', 'type': 'pdev_archdata'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v7.0/rust/kernel/error.rs:500 `From<core::convert::Infallible>::to_result` unsafe=0
- .binddrift/worktrees/v7.0/rust/kernel/platform.rs:95 `None` unsafe=0
- .binddrift/worktrees/v7.0/rust/kernel/platform.rs:111 `probe_callback` unsafe=0
- .binddrift/worktrees/v7.0/rust/kernel/platform.rs:257 `None` unsafe=0
- .binddrift/worktrees/v7.0/rust/kernel/platform.rs:262 `None` unsafe=0
- safe API `From<core::convert::Infallible>::to_result`
- .binddrift/worktrees/v7.0/rust/kernel/error.rs:495 `///`
- .binddrift/worktrees/v7.0/rust/kernel/error.rs:496 `/// ```ignore`
- .binddrift/worktrees/v7.0/rust/kernel/error.rs:497 `/// # use kernel::from_result;`
- .binddrift/worktrees/v7.0/rust/kernel/platform.rs:257 `OPAQUE`
- wrapper_fix: `ef4dc4cc7001e9cce8a3b556362171648be9ad92`
- wrapper_fix: `4d320e30ee04c25c660eca2bb33e846ebb71a79a`
- wrapper_fix: `0242623384c767b1156b61b67894b4ecf6682b8b`

## W-000009 FieldDrift

- Risk: Medium
- Score: 11.0
- Symbol: device
- Explanation: device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'kobj', 'type': 'kobject'}, {'name': 'parent', 'type': '*mut device'}, {'name': 'p', 'type': '*mut device_private'}, {'name': 'init_name', 'type': '*const ffi::c_char'}, {'name': 'type_', 'type': '*const device_type'}, {'name': 'bus', 'type': '*const bus_type'}, {'name': 'driver', 'type': '*mut device_driver'}, {'name': 'platform_data', 'type': '*mut ffi::c_void'}, {'name': 'driver_data', 'type': '*mut ffi::c_void'}, {'name': 'driver_override', 'type': 'device__bindgen_ty_1'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'links', 'type': 'dev_links_info'}, {'name': 'power', 'type': 'dev_pm_info'}, {'name': 'pm_domain', 'type': '*mut dev_pm_domain'}, {'name': 'msi', 'type': 'dev_msi_info'}, {'name': 'dma_mask', 'type': '*mut u64_'}, {'name': 'coherent_dma_mask', 'type': 'u64_'}, {'name': 'bus_dma_limit', 'type': 'u64_'}, {'name': 'dma_range_map', 'type': '*mut bus_dma_region'}, {'name': 'dma_parms', 'type': '*mut device_dma_parameters'}, {'name': 'dma_pools', 'type': 'list_head'}, {'name': 'dma_io_tlb_mem', 'type': '*mut io_tlb_mem'}, {'name': 'archdata', 'type': 'dev_archdata'}, {'name': 'of_node', 'type': '*mut device_node'}, {'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'numa_node', 'type': 'ffi::c_int'}, {'name': 'devt', 'type': 'dev_t'}, {'name': 'id', 'type': 'u32_'}, {'name': 'devres_lock', 'type': 'spinlock_t'}, {'name': 'devres_head', 'type': 'list_head'}, {'name': 'class', 'type': '*const class'}, {'name': 'groups', 'type': '*mut *const attribute_group'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'iommu_group', 'type': '*mut iommu_group'}, {'name': 'iommu', 'type': '*mut dev_iommu'}, {'name': 'physical_location', 'type': '*mut device_physical_location'}, {'name': 'removable', 'type': 'device_removable'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 3usize]'}]`
- New: `[{'name': 'kobj', 'type': 'kobject'}, {'name': 'parent', 'type': '*mut device'}, {'name': 'p', 'type': '*mut device_private'}, {'name': 'init_name', 'type': '*const ffi::c_char'}, {'name': 'type_', 'type': '*const device_type'}, {'name': 'bus', 'type': '*const bus_type'}, {'name': 'driver', 'type': '*mut device_driver'}, {'name': 'platform_data', 'type': '*mut ffi::c_void'}, {'name': 'driver_data', 'type': '*mut ffi::c_void'}, {'name': 'driver_override', 'type': 'device__bindgen_ty_1'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'links', 'type': 'dev_links_info'}, {'name': 'power', 'type': 'dev_pm_info'}, {'name': 'pm_domain', 'type': '*mut dev_pm_domain'}, {'name': 'msi', 'type': 'dev_msi_info'}, {'name': 'dma_mask', 'type': '*mut u64_'}, {'name': 'coherent_dma_mask', 'type': 'u64_'}, {'name': 'bus_dma_limit', 'type': 'u64_'}, {'name': 'dma_range_map', 'type': '*mut bus_dma_region'}, {'name': 'dma_parms', 'type': '*mut device_dma_parameters'}, {'name': 'dma_pools', 'type': 'list_head'}, {'name': 'dma_io_tlb_mem', 'type': '*mut io_tlb_mem'}, {'name': 'archdata', 'type': 'dev_archdata'}, {'name': 'of_node', 'type': '*mut device_node'}, {'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'numa_node', 'type': 'ffi::c_int'}, {'name': 'devt', 'type': 'dev_t'}, {'name': 'id', 'type': 'u32_'}, {'name': 'devres_lock', 'type': 'spinlock_t'}, {'name': 'devres_head', 'type': 'list_head'}, {'name': 'class', 'type': '*const class'}, {'name': 'groups', 'type': '*mut *const attribute_group'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'iommu_group', 'type': '*mut iommu_group'}, {'name': 'iommu', 'type': '*mut dev_iommu'}, {'name': 'physical_location', 'type': '*mut device_physical_location'}, {'name': 'removable', 'type': 'device_removable'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'flags', 'type': '[ffi::c_ulong; 1usize]'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/auxiliary.rs:269 `Device::parent` unsafe=0
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/device.rs:163 `None` unsafe=0
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/device.rs:170 `None` unsafe=0
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/device.rs:181 `None` unsafe=0
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/device.rs:183 `None` unsafe=0
- safe API `Device::parent`
- safe API `Device<Ctx>::parent`
- safe API `Config<T>::set`
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/auxiliary.rs:265 `// SAFETY: A `struct auxiliary_device` always has a parent.`
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/device.rs:158 `/// A `Device` instance represents a valid `struct device` created by the C portion of the kernel.`
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/device.rs:159 `///`
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/device.rs:163 `AREF`
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/device.rs:170 `OPAQUE`
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/device.rs:183 `AREF`
- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`
- wrapper_fix: `4d320e30ee04c25c660eca2bb33e846ebb71a79a`

## W-000003 SignatureDrift

- Risk: Medium
- Score: 10.0
- Symbol: faux_device_create
- Explanation: faux_device_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.14/rust/kernel/faux.rs:31 `Registration::new` unsafe=1
- safe API `Registration::new`
- .binddrift/worktrees/v6.14/rust/kernel/faux.rs:26 `/// Create and register a new faux device with the given name.`
- .binddrift/worktrees/v6.14/rust/kernel/faux.rs:28 `// SAFETY:`
- .binddrift/worktrees/v6.14/rust/kernel/faux.rs:27 `RESULT_RETURN`
- weak lifetime name .binddrift/worktrees/v6.14/rust/kernel/faux.rs:31 `LIFETIME_NAMING_PATTERN`
- wrapper_fix: `78418f300d3999f1cf8a9ac71065bf2eca61f4dd`

## W-000017 SignatureDrift

- Risk: Medium
- Score: 10.0
- Symbol: security_release_secctx
- Explanation: security_release_secctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['char *secdata', 'u32 seclen'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct lsm_context *cp'], 'return_type': 'static inline void'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.14/rust/kernel/security.rs:68 `drop` unsafe=1
- .binddrift/worktrees/v6.14/rust/kernel/security.rs:65 `// SAFETY: By the invariant of `Self`, this frees a context that came from a successful`
- weak lifetime name .binddrift/worktrees/v6.14/rust/kernel/security.rs:68 `LIFETIME_NAMING_PATTERN`

## W-000001 SignatureDrift

- Risk: Medium
- Score: 10.0
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
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.17/rust/kernel/device.rs:202 `Device<CoreInternal>::set_drvdata` unsafe=1
- safe API `Device<CoreInternal>::set_drvdata`
- .binddrift/worktrees/v6.17/rust/kernel/device.rs:199 `/// Store a pointer to the bound driver's private data.`
- .binddrift/worktrees/v6.17/rust/kernel/device.rs:201 `// SAFETY: By the type invariants, `self.as_raw()` is a valid pointer to a `struct device`.`
- .binddrift/worktrees/v6.17/rust/kernel/device.rs:205 `/// Take ownership of the private data stored in this [`Device`].`
- .binddrift/worktrees/v6.17/rust/kernel/device.rs:200 `FOREIGN_OWNABLE`
- wrapper_fix: `0242623384c767b1156b61b67894b4ecf6682b8b`

## W-000007 SignatureDrift

- Risk: Medium
- Score: 10.0
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
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.17/rust/kernel/regulator.rs:269 `Regulator<T>::get_voltage` unsafe=1
- safe API `Regulator<T>::get_voltage`
- .binddrift/worktrees/v6.17/rust/kernel/regulator.rs:266 `/// Gets the current voltage of the regulator.`
- .binddrift/worktrees/v6.17/rust/kernel/regulator.rs:268 `// SAFETY: Safe as per the type invariants of `Regulator`.`
- .binddrift/worktrees/v6.17/rust/kernel/regulator.rs:267 `RESULT_RETURN`
- .binddrift/worktrees/v6.17/rust/kernel/regulator.rs:269 `AS_PTR`
- wrapper_fix: `8121353a4bf8e38afee26299419a78ec108e14a6`

## W-000008 SignatureDrift

- Risk: Medium
- Score: 10.0
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
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.17/rust/kernel/regulator.rs:383 `Regulator<T>::is_enabled` unsafe=1
- safe API `Regulator<T>::is_enabled`
- .binddrift/worktrees/v6.17/rust/kernel/regulator.rs:380 `/// Checks if the regulator is enabled.`
- .binddrift/worktrees/v6.17/rust/kernel/regulator.rs:382 `// SAFETY: Safe as per the type invariants of `Regulator`.`
- .binddrift/worktrees/v6.17/rust/kernel/regulator.rs:383 `AS_PTR`
- wrapper_fix: `8121353a4bf8e38afee26299419a78ec108e14a6`

## W-000174 SignatureDrift

- Risk: Medium
- Score: 10.0
- Symbol: clear_bit
- Explanation: clear_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:378 `Bitmap::clear_bit_atomic` unsafe=1
- safe API `Bitmap::clear_bit_atomic`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:376 `// SAFETY: `index` is within bounds and the caller has ensured that`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:381 `/// Copy `src` into this [`Bitmap`] and set any remaining bits to zero.`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:382 `///`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:378 `AS_PTR`
- wrapper_fix: `6cf93a9ed39e9f86c7f69c28078500270e70a695`
- wrapper_fix: `11eca92a2caebcc2b3b65ca290385ff4b0498946`
- wrapper_fix: `6a069876eb1402478900ee0eb7d7fe276bb1f4e3`

## W-000175 SignatureDrift

- Risk: Medium
- Score: 10.0
- Symbol: refcount_dec
- Explanation: refcount_dec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:81 `Refcount::dec` unsafe=1
- safe API `Refcount::dec`
- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:76 `/// Provides release memory ordering, such that prior loads and stores are done`
- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:77 `/// before.`
- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:80 `// SAFETY: `self.as_ptr()` is valid.`
- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:80 `AS_PTR`
- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:81 `AS_PTR`
- wrapper_fix: `bb38f35b35f9de0cebc4d62ea73482454e38cef3`
- wrapper_fix: `9ba1aaf25ab7dadb910348b6857865e87b4c5689`

## W-000176 SignatureDrift

- Risk: Medium
- Score: 10.0
- Symbol: refcount_set
- Explanation: refcount_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:56 `Refcount::set` unsafe=1
- safe API `Refcount::set`
- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:52 `/// Set a refcount's value.`
- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:55 `// SAFETY: `self.as_ptr()` is valid.`
- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:59 `/// Increment a refcount.`
- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:55 `AS_PTR`
- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:56 `AS_PTR`
- wrapper_fix: `bb38f35b35f9de0cebc4d62ea73482454e38cef3`
- wrapper_fix: `9ba1aaf25ab7dadb910348b6857865e87b4c5689`

## W-000179 SignatureDrift

- Risk: Medium
- Score: 10.0
- Symbol: queue_delayed_work_on
- Explanation: queue_delayed_work_on changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['cpu', 'system_wq', 'dwork', 'delay'], 'return_type': 'return'}`
- New: `{'params': ['cpu', 'system_percpu_wq', 'dwork', 'delay'], 'return_type': 'return'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v6.18/rust/kernel/workqueue.rs:309 `print_now` unsafe=0
- .binddrift/worktrees/v6.18/rust/kernel/workqueue.rs:316 `print_now` unsafe=0
- .binddrift/worktrees/v6.18/rust/kernel/workqueue.rs:321 `print_now` unsafe=1
- .binddrift/worktrees/v6.18/rust/kernel/workqueue.rs:306 `// SAFETY: We only return `false` if the `work_struct` is already in a workqueue. The other`

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

## W-000004 SignatureDrift

- Risk: Medium
- Score: 10.0
- Symbol: dma_free_attrs
- Explanation: dma_free_attrs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct device *dev', 'size_t size', 'void *cpu_addr', 'dma_addr_t dma_handle', 'unsigned long attrs'], 'return_type': 'static void'}`
- New: `{'params': ['struct device *dev', 'size_t size', 'void *cpu_addr', 'dma_addr_t dma_handle', 'unsigned long attrs'], 'return_type': 'static inline void'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- .binddrift/worktrees/v7.0/rust/kernel/dma.rs:652 `drop` unsafe=1
- .binddrift/worktrees/v7.0/rust/kernel/dma.rs:648 `// SAFETY: Device pointer is guaranteed as valid by the type invariant on `Device`.`
- weak lifetime name .binddrift/worktrees/v7.0/rust/kernel/dma.rs:652 `LIFETIME_NAMING_PATTERN`

## W-000034 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: firmware
- Explanation: firmware changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'size', 'type': 'usize'}, {'name': 'data', 'type': '*const u8_'}, {'name': 'priv_', 'type': '*mut core::ffi::c_void'}]`
- New: `[{'name': 'size', 'type': 'usize'}, {'name': 'data', 'type': '*const u8_'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:15 `None` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:55 `no_run` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:59 `request_internal` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:60 `request_internal` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:62 `request_internal` unsafe=0
- safe API `Firmware::request_nowarn`
- safe API `Firmware::data`
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:50 `/// let blob = fw.data();`
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:51 `///`
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:52 `/// # Ok(())`
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:58 `RESULT_RETURN`
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:81 `RESULT_RETURN`
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:86 `AS_PTR`
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:100 `FROM_RAW`
- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`

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
- .binddrift/worktrees/v6.13/rust/kernel/rbtree.rs:874 `peek_mut` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/rbtree.rs:890 `get_neighbor_raw` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/rbtree.rs:901 `get_neighbor_raw` unsafe=0
- safe API `RBTreeNodeReservation<K::into_node`
- .binddrift/worktrees/v6.13/rust/kernel/rbtree.rs:327 `// SAFETY: `raw_self` is a valid pointer to the `RBTree` (created from `self` above).`
- .binddrift/worktrees/v6.13/rust/kernel/rbtree.rs:331 `// SAFETY: All links fields we create are in a `Node<K, V>`.`
- .binddrift/worktrees/v6.13/rust/kernel/rbtree.rs:720 `///`
- .binddrift/worktrees/v6.13/rust/kernel/rbtree.rs:915 `AS_PTR`
- wrapper_fix: `8333ff4d0799aafbe4275cddcbaf45e545e4efba`

## W-000177 SignatureDrift

- Risk: Medium
- Score: 9.0
- Symbol: set_bit
- Explanation: set_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&mut self'}, {'name': 'index', 'type': 'usize'}, {'name': 'val', 'type': 'bool) { debug_assert!(index / 8 < self.storage.as_ref().len()'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'nr', 'type': 'ffi::c_ulong'}, {'name': 'addr', 'type': '*mut ffi::c_ulong'}], 'return_type': '()'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:327 `Bitmap::set_bit_atomic` unsafe=1
- safe API `Bitmap::set_bit_atomic`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:325 `// SAFETY: `index` is within bounds and the caller has ensured that`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:330 `/// Clear `index` bit.`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:331 `///`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:327 `AS_PTR`
- wrapper_fix: `6cf93a9ed39e9f86c7f69c28078500270e70a695`
- wrapper_fix: `11eca92a2caebcc2b3b65ca290385ff4b0498946`

## W-000001 SignatureDrift

- Risk: Medium
- Score: 9.0
- Symbol: ERR_PTR
- Explanation: ERR_PTR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.4/rust/kernel/error.rs:114 `Error::to_errno` unsafe=1
- safe API `Error::to_errno`
- .binddrift/worktrees/v6.4/rust/kernel/error.rs:110 `/// Returns the error encoded as a pointer.`
- .binddrift/worktrees/v6.4/rust/kernel/error.rs:113 `// SAFETY: self.0 is a valid error due to its invariant.`
- wrapper_fix: `c7e20faa5fcad7a177cf6c306138010343dd6d3e`
- wrapper_fix: `7bc186731e87482662c4f86da455f435fe838fb6`
- wrapper_fix: `e9759c5b9ea555d09f426c70c880e9522e9b0576`

## W-000002 SignatureDrift

- Risk: Medium
- Score: 9.0
- Symbol: mdiobus_read
- Explanation: mdiobus_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.8/rust/kernel/net/phy.rs:186 `Device::read` unsafe=1
- safe API `Device::read`
- .binddrift/worktrees/v6.8/rust/kernel/net/phy.rs:182 `// SAFETY: `phydev` is pointing to a valid object by the type invariant of `Self`.`
- wrapper_fix: `b2e47002b2350f57bfa8fe1c231e9fbb6baef78b`

## W-000004 SignatureDrift

- Risk: Medium
- Score: 9.0
- Symbol: errno_to_blk_status
- Explanation: errno_to_blk_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.11/rust/kernel/error.rs:132 `Error::to_blk_status` unsafe=1
- safe API `Error::to_blk_status`
- .binddrift/worktrees/v6.11/rust/kernel/error.rs:131 `// SAFETY: `self.0` is a valid error due to its invariant.`
- wrapper_fix: `e9759c5b9ea555d09f426c70c880e9522e9b0576`

## W-000005 SignatureDrift

- Risk: Medium
- Score: 8.0
- Symbol: firmware_request_nowarn
- Explanation: firmware_request_nowarn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.11/rust/kernel/firmware.rs:12 `None` unsafe=0
- .binddrift/worktrees/v6.11/rust/kernel/firmware.rs:24 `request_nowarn` unsafe=0
- .binddrift/worktrees/v6.11/rust/kernel/firmware.rs:80 `Firmware::request` unsafe=0
- safe API `Firmware::request`
- .binddrift/worktrees/v6.11/rust/kernel/firmware.rs:28 `/// Abstraction around a C `struct firmware`.`
- .binddrift/worktrees/v6.11/rust/kernel/firmware.rs:29 `///`
- .binddrift/worktrees/v6.11/rust/kernel/firmware.rs:79 `/// Send a request for an optional firmware module. See also`
- .binddrift/worktrees/v6.11/rust/kernel/firmware.rs:75 `RESULT_RETURN`
- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`

## W-000001 SignatureDrift

- Risk: Medium
- Score: 8.0
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
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/error.rs:159 `Error::to_blk_status` unsafe=1
- safe API `Error::to_blk_status`
- .binddrift/worktrees/v6.13/rust/kernel/error.rs:154 `/// Returns the error encoded as a pointer.`
- .binddrift/worktrees/v6.13/rust/kernel/error.rs:157 `// SAFETY: `self.0` is a valid error due to its invariant.`
- wrapper_fix: `c7e20faa5fcad7a177cf6c306138010343dd6d3e`
- wrapper_fix: `7bc186731e87482662c4f86da455f435fe838fb6`
- wrapper_fix: `e9759c5b9ea555d09f426c70c880e9522e9b0576`

## W-000018 SignatureDrift

- Risk: Medium
- Score: 8.0
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
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/error.rs:151 `Error::to_blk_status` unsafe=1
- safe API `Error::to_blk_status`
- .binddrift/worktrees/v6.13/rust/kernel/error.rs:150 `// SAFETY: `self.0` is a valid error due to its invariant.`
- wrapper_fix: `e9759c5b9ea555d09f426c70c880e9522e9b0576`

## W-000003 SignatureDrift

- Risk: Medium
- Score: 8.0
- Symbol: platform_set_drvdata
- Explanation: platform_set_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.17/rust/kernel/error.rs:450 `From<core::convert::Infallible>::to_result` unsafe=0
- safe API `From<core::convert::Infallible>::to_result`
- .binddrift/worktrees/v6.17/rust/kernel/error.rs:445 `/// unsafe extern "C" fn probe_callback(`
- .binddrift/worktrees/v6.17/rust/kernel/error.rs:446 `///     pdev: *mut bindings::platform_device,`
- .binddrift/worktrees/v6.17/rust/kernel/error.rs:447 `/// ) -> kernel::ffi::c_int {`
- wrapper_fix: `ef4dc4cc7001e9cce8a3b556362171648be9ad92`

## W-000178 FieldDrift

- Risk: Medium
- Score: 8.0
- Symbol: kunit_case
- Explanation: kunit_case changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'run_case', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'generate_params', 'type': '::core::option::Option<'}, {'name': 'attr', 'type': 'kunit_attributes'}, {'name': 'status', 'type': 'kunit_status'}, {'name': 'module_name', 'type': '*mut ffi::c_char'}, {'name': 'log', 'type': '*mut string_stream'}]`
- New: `[{'name': 'run_case', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'generate_params', 'type': '::core::option::Option<'}, {'name': 'attr', 'type': 'kunit_attributes'}, {'name': 'param_init', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit) -> ffi::c_int>'}, {'name': 'param_exit', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'status', 'type': 'kunit_status'}, {'name': 'module_name', 'type': '*mut ffi::c_char'}, {'name': 'log', 'type': '*mut string_stream'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.18/rust/kernel/kunit.rs:202 `TestResult::is_test_result_ok` unsafe=0
- .binddrift/worktrees/v6.18/rust/kernel/kunit.rs:203 `TestResult::is_test_result_ok` unsafe=0
- .binddrift/worktrees/v6.18/rust/kernel/kunit.rs:223 `TestResult::is_test_result_ok` unsafe=0
- .binddrift/worktrees/v6.18/rust/kernel/kunit.rs:224 `kunit_case_null` unsafe=0
- .binddrift/worktrees/v6.18/rust/kernel/kunit.rs:255 `test_fn` unsafe=0
- safe API `TestResult::is_test_result_ok`
- .binddrift/worktrees/v6.18/rust/kernel/kunit.rs:197 `/// Use [`kunit_case_null`] to generate such a delimiter.`
- .binddrift/worktrees/v6.18/rust/kernel/kunit.rs:218 `/// Represents the NULL test case delimiter.`
- .binddrift/worktrees/v6.18/rust/kernel/kunit.rs:219 `///`
- wrapper_fix: `7f87c7a003125d5af5ec7abbbc0ac21b4a4661ae`
- wrapper_fix: `be97f3c82021239476ce32cddde32948c597753e`

## W-000001 FieldDrift

- Risk: Medium
- Score: 8.0
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
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.19/rust/kernel/block/mq/gen_disk.rs:110 `GenDiskBuilder::capacity_sectors` unsafe=0
- .binddrift/worktrees/v6.19/rust/kernel/block/mq/gen_disk.rs:111 `GenDiskBuilder::capacity_sectors` unsafe=1
- safe API `GenDiskBuilder::capacity_sectors`
- .binddrift/worktrees/v6.19/rust/kernel/block/mq/gen_disk.rs:106 `// SAFETY: T::QueueData was created by the call to `into_foreign()` above`
- .binddrift/worktrees/v6.19/rust/kernel/block/mq/gen_disk.rs:110 `// SAFETY: `bindings::queue_limits` contain only fields that are valid when zeroed.`
- wrapper_fix: `5e3b7009f116f684ac6b93d8924506154f3b1f6d`

## W-000022 SignatureDrift

- Risk: Low
- Score: 7.0
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
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:111 `read` unsafe=1
- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:107 `// SAFETY: `phydev` is pointing to a valid object by the type invariant of `Device`.`
- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:113 `TO_RESULT_MAPPING`
- wrapper_fix: `b2e47002b2350f57bfa8fe1c231e9fbb6baef78b`

## W-000023 SignatureDrift

- Risk: Low
- Score: 7.0
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
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:123 `write` unsafe=1
- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:119 `// SAFETY: `phydev` is pointing to a valid object by the type invariant of `Device`.`
- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:122 `TO_RESULT_MAPPING`
- wrapper_fix: `b2e47002b2350f57bfa8fe1c231e9fbb6baef78b`

## W-000024 SignatureDrift

- Risk: Low
- Score: 7.0
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
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:202 `read` unsafe=1
- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:199 `// SAFETY: `phydev` is pointing to a valid object by the type invariant of `Device`.`
- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:197 `RESULT_RETURN`
- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:203 `TO_RESULT_MAPPING`
- wrapper_fix: `b2e47002b2350f57bfa8fe1c231e9fbb6baef78b`

## W-000025 SignatureDrift

- Risk: Low
- Score: 7.0
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
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:212 `write` unsafe=1
- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:209 `// SAFETY: `phydev` is pointing to a valid object by the type invariant of `Device`.`
- .binddrift/worktrees/v6.13/rust/kernel/net/phy/reg.rs:211 `TO_RESULT_MAPPING`
- wrapper_fix: `b2e47002b2350f57bfa8fe1c231e9fbb6baef78b`

## W-000027 SignatureDrift

- Risk: Low
- Score: 7.0
- Symbol: request_firmware
- Explanation: request_firmware changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'fw', 'type': '*mut *const firmware'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'device', 'type': '*mut device'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'fw', 'type': '*mut *const firmware'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'device', 'type': '*mut device'}], 'return_type': 'ffi::c_int'}`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:12 `None` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:20 `request` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:74 `request_internal` unsafe=0
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:69 `// SAFETY: `func` not bailing out with a non-zero error code, guarantees that `fw` is a`
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:74 `/// Send a firmware request and wait for it. See also `bindings::request_firmware`.`
- .binddrift/worktrees/v6.13/rust/kernel/firmware.rs:71 `NONNULL_MAPPING`
- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`

## W-000001 FieldDrift

- Risk: Low
- Score: 7.0
- Symbol: pci_dev
- Explanation: pci_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 11usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': 'match_driver', 'type': 'bool_'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 5usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pri_cap', 'type': 'u16_'}, {'name': 'pri_reqs_alloc', 'type': 'u32_'}, {'name': '_bitfield_align_5', 'type': '[u8; 0]'}, {'name': '_bitfield_5', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`
- New: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'rebar_cap', 'type': 'u16_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 11usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': 'match_driver', 'type': 'bool_'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pri_cap', 'type': 'u16_'}, {'name': 'pri_reqs_alloc', 'type': 'u32_'}, {'name': '_bitfield_align_5', 'type': '[u8; 0]'}, {'name': '_bitfield_5', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.15/rust/kernel/pci.rs:62 `None` unsafe=0
- .binddrift/worktrees/v6.15/rust/kernel/pci.rs:89 `None` unsafe=0
- .binddrift/worktrees/v6.15/rust/kernel/pci.rs:254 `None` unsafe=0
- .binddrift/worktrees/v6.15/rust/kernel/pci.rs:364 `None` unsafe=0
- .binddrift/worktrees/v6.15/rust/kernel/pci.rs:431 `deref` unsafe=0
- .binddrift/worktrees/v6.15/rust/kernel/pci.rs:249 `/// # Invariants`
- .binddrift/worktrees/v6.15/rust/kernel/pci.rs:250 `///`
- .binddrift/worktrees/v6.15/rust/kernel/pci.rs:251 `/// A [`Device`] instance represents a valid `struct device` created by the C portion of the kernel.`
- .binddrift/worktrees/v6.15/rust/kernel/pci.rs:254 `OPAQUE`
- .binddrift/worktrees/v6.15/rust/kernel/pci.rs:431 `OPAQUE`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`

## W-000004 FieldDrift

- Risk: Low
- Score: 7.0
- Symbol: pci_dev
- Explanation: pci_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'rebar_cap', 'type': 'u16_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 11usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': 'match_driver', 'type': 'bool_'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pri_cap', 'type': 'u16_'}, {'name': 'pri_reqs_alloc', 'type': 'u32_'}, {'name': '_bitfield_align_5', 'type': '[u8; 0]'}, {'name': '_bitfield_5', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`
- New: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'rebar_cap', 'type': 'u16_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 11usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pri_cap', 'type': 'u16_'}, {'name': 'pri_reqs_alloc', 'type': 'u32_'}, {'name': '_bitfield_align_5', 'type': '[u8; 0]'}, {'name': '_bitfield_5', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v6.16/rust/kernel/pci.rs:62 `None` unsafe=0
- .binddrift/worktrees/v6.16/rust/kernel/pci.rs:89 `None` unsafe=0
- .binddrift/worktrees/v6.16/rust/kernel/pci.rs:257 `None` unsafe=0
- .binddrift/worktrees/v6.16/rust/kernel/pci.rs:367 `None` unsafe=0
- .binddrift/worktrees/v6.16/rust/kernel/pci.rs:474 `try_from` unsafe=1
- .binddrift/worktrees/v6.16/rust/kernel/pci.rs:252 `/// # Invariants`
- .binddrift/worktrees/v6.16/rust/kernel/pci.rs:253 `///`
- .binddrift/worktrees/v6.16/rust/kernel/pci.rs:254 `/// A [`Device`] instance represents a valid `struct device` created by the C portion of the kernel.`
- .binddrift/worktrees/v6.16/rust/kernel/pci.rs:257 `OPAQUE`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`

## W-000002 FieldDrift

- Risk: Low
- Score: 7.0
- Symbol: pci_dev
- Explanation: pci_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'rebar_cap', 'type': 'u16_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 11usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pri_cap', 'type': 'u16_'}, {'name': 'pri_reqs_alloc', 'type': 'u32_'}, {'name': '_bitfield_align_5', 'type': '[u8; 0]'}, {'name': '_bitfield_5', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`
- New: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'rebar_cap', 'type': 'u16_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'msi_addr_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 11usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pri_cap', 'type': 'u16_'}, {'name': 'pri_reqs_alloc', 'type': 'u32_'}, {'name': '_bitfield_align_5', 'type': '[u8; 0]'}, {'name': '_bitfield_5', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'acs_capabilities', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/v7.0/rust/kernel/pci.rs:101 `None` unsafe=0
- .binddrift/worktrees/v7.0/rust/kernel/pci.rs:123 `None` unsafe=0
- .binddrift/worktrees/v7.0/rust/kernel/pci.rs:339 `None` unsafe=0
- .binddrift/worktrees/v7.0/rust/kernel/pci.rs:345 `None` unsafe=0
- .binddrift/worktrees/v7.0/rust/kernel/pci.rs:466 `None` unsafe=0
- .binddrift/worktrees/v7.0/rust/kernel/pci.rs:124 `// SAFETY: The PCI bus only ever calls the remove callback with a valid pointer to a`
- .binddrift/worktrees/v7.0/rust/kernel/pci.rs:334 `///`
- .binddrift/worktrees/v7.0/rust/kernel/pci.rs:335 `/// A [`Device`] instance represents a valid `struct pci_dev` created by the C portion of the`
- .binddrift/worktrees/v7.0/rust/kernel/pci.rs:339 `OPAQUE`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`

## W-000010 FieldDrift

- Risk: Low
- Score: 7.0
- Symbol: pci_dev
- Explanation: pci_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'rebar_cap', 'type': 'u16_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'msi_addr_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 11usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pri_cap', 'type': 'u16_'}, {'name': 'pri_reqs_alloc', 'type': 'u32_'}, {'name': '_bitfield_align_5', 'type': '[u8; 0]'}, {'name': '_bitfield_5', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'acs_capabilities', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`
- New: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'rebar_cap', 'type': 'u16_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'msi_addr_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 11usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pri_cap', 'type': 'u16_'}, {'name': 'pri_reqs_alloc', 'type': 'u32_'}, {'name': '_bitfield_align_5', 'type': '[u8; 0]'}, {'name': '_bitfield_5', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'acs_capabilities', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/pci.rs:101 `None` unsafe=0
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/pci.rs:123 `None` unsafe=0
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/pci.rs:339 `None` unsafe=0
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/pci.rs:345 `None` unsafe=0
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/pci.rs:466 `None` unsafe=0
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/pci.rs:124 `// SAFETY: The PCI bus only ever calls the remove callback with a valid pointer to a`
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/pci.rs:334 `///`
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/pci.rs:335 `/// A [`Device`] instance represents a valid `struct pci_dev` created by the C portion of the`
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/pci.rs:339 `OPAQUE`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`

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

## W-000002 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: devm_platform_ioremap_resource
- Explanation: devm_platform_ioremap_resource changed across the selected Linux versions.
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

- .binddrift/worktrees/v6.14/rust/kernel/error.rs:283 `From<core::convert::Infallible>::to_result` unsafe=1
- safe API `From<core::convert::Infallible>::to_result`
- .binddrift/worktrees/v6.14/rust/kernel/error.rs:278 `///     pdev: &mut PlatformDevice,`
- .binddrift/worktrees/v6.14/rust/kernel/error.rs:279 `///     index: u32,`
- .binddrift/worktrees/v6.14/rust/kernel/error.rs:280 `/// ) -> Result<*mut kernel::ffi::c_void> {`
- .binddrift/worktrees/v6.14/rust/kernel/error.rs:280 `RESULT_RETURN`
- .binddrift/worktrees/v6.14/rust/kernel/error.rs:283 `ERR_PTR_MAPPING`
- wrapper_fix: `752417b3f0e7721f1d630f40da22d57e0dae043e`
- wrapper_fix: `69d5fbb0159673ea6737204f4d458a220e81a0c9`

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

- .binddrift/worktrees/v6.17/rust/kernel/sync/poll.rs:61 `PollTable<::register_wait` unsafe=1
- safe API `PollTable<::register_wait`
- .binddrift/worktrees/v6.17/rust/kernel/sync/poll.rs:65 `/// A wrapper around [`CondVar`] that makes it usable with [`PollTable`].`
- .binddrift/worktrees/v6.17/rust/kernel/sync/poll.rs:66 `///`
- .binddrift/worktrees/v6.17/rust/kernel/sync/poll.rs:61 `AS_PTR`
- wrapper_fix: `de747bd023c09b5b7f3bf5c952d7b1da77a9caaa`

## W-000173 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: bitmap_copy_and_extend
- Explanation: bitmap_copy_and_extend changed across the selected Linux versions.
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

- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:406 `Bitmap::copy_and_extend` unsafe=1
- safe API `Bitmap::copy_and_extend`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:404 `// SAFETY: access to `self` and `src` is within bounds.`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:408 `AS_PTR`
- wrapper_fix: `0452b4ab2961093f23bb289b0112351b917fb23c`
- wrapper_fix: `11eca92a2caebcc2b3b65ca290385ff4b0498946`

## W-000003 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: gpu_buddy_alloc_blocks
- Explanation: gpu_buddy_alloc_blocks changed across the selected Linux versions.
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

- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/gpu/buddy.rs:469 `GpuBuddy::avail` unsafe=1
- safe API `GpuBuddy::avail`
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/gpu/buddy.rs:466 `// SAFETY: Per the type invariant, `inner` contains an initialized`
- .binddrift/worktrees/HEAD_6d35786de281/rust/kernel/gpu/buddy.rs:468 `TO_RESULT_MAPPING`
- wrapper_fix: `b9616d9721bf8a56d5038e85d2ebbe0ec9d56a94`

## W-000002 SignatureDrift

- Risk: Low
- Score: 5.0
- Symbol: IS_ERR
- Explanation: IS_ERR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.4/rust/kernel/error.rs:223 `From<core::convert::Infallible>::to_result` unsafe=1
- safe API `From<core::convert::Infallible>::to_result`
- .binddrift/worktrees/v6.4/rust/kernel/error.rs:219 `ERR_PTR_MAPPING`
- .binddrift/worktrees/v6.4/rust/kernel/error.rs:219 `RESULT_RETURN`
- wrapper_fix: `752417b3f0e7721f1d630f40da22d57e0dae043e`

## W-000003 SignatureDrift

- Risk: Low
- Score: 5.0
- Symbol: PTR_ERR
- Explanation: PTR_ERR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.4/rust/kernel/error.rs:225 `From<core::convert::Infallible>::to_result` unsafe=1
- safe API `From<core::convert::Infallible>::to_result`
- .binddrift/worktrees/v6.4/rust/kernel/error.rs:222 `// SAFETY: The FFI function does not deref the pointer.`
- wrapper_fix: `752417b3f0e7721f1d630f40da22d57e0dae043e`
