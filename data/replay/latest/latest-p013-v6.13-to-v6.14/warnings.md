# BindDrift Ranked Warnings

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

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/security.rs:31 `SecurityCtx::from_secid` unsafe=1
- safe API `SecurityCtx::from_secid`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/security.rs:27 `// SAFETY: `struct lsm_context` can be initialized to all zeros.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/security.rs:30 `// SAFETY: Just a C FFI call. The pointer is valid for writes.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/security.rs:26 `RESULT_RETURN`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/security.rs:31 `TO_RESULT_MAPPING`

## W-000014 FieldDrift

- Risk: High
- Score: 13.0
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
- binding_only_penalty: `-5.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/pci.rs:58 `None` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/pci.rs:86 `None` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/pci.rs:359 `None` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/pci.rs:364 `Device::from_dev` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/pci.rs:367 `as_raw` unsafe=1
- safe API `Device::from_dev`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/pci.rs:354 `/// Create a PCI Device instance from an existing `device::Device`.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/pci.rs:355 `///`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/pci.rs:356 `/// # Safety`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/pci.rs:358 `AREF`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/pci.rs:360 `AREF`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`

## W-000015 FieldDrift

- Risk: High
- Score: 13.0
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
- binding_only_penalty: `-5.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:323 `From<core::convert::Infallible>::to_result` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/platform.rs:56 `None` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/platform.rs:77 `probe_callback` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/platform.rs:184 `None` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/platform.rs:189 `from_dev` unsafe=0
- safe API `From<core::convert::Infallible>::to_result`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:318 `///`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:319 `/// ```ignore`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:320 `/// # use kernel::from_result;`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/platform.rs:185 `AREF`
- wrapper_fix: `ef4dc4cc7001e9cce8a3b556362171648be9ad92`
- wrapper_fix: `4d320e30ee04c25c660eca2bb33e846ebb71a79a`
- wrapper_fix: `0242623384c767b1156b61b67894b4ecf6682b8b`

## W-000016 FieldDrift

- Risk: High
- Score: 13.0
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
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/block/mq/gen_disk.rs:96 `GenDiskBuilder::capacity_sectors` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/block/mq/gen_disk.rs:97 `GenDiskBuilder::capacity_sectors` unsafe=1
- safe API `GenDiskBuilder::capacity_sectors`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/block/mq/gen_disk.rs:96 `// SAFETY: `bindings::queue_limits` contain only fields that are valid when zeroed.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/block/mq/gen_disk.rs:95 `RESULT_RETURN`
- wrapper_fix: `5e3b7009f116f684ac6b93d8924506154f3b1f6d`

## W-000002 SignatureDrift

- Risk: Medium
- Score: 10.0
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
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:283 `From<core::convert::Infallible>::to_result` unsafe=1
- safe API `From<core::convert::Infallible>::to_result`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:278 `///     pdev: &mut PlatformDevice,`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:279 `///     index: u32,`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:280 `/// ) -> Result<*mut kernel::ffi::c_void> {`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:280 `RESULT_RETURN`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:283 `ERR_PTR_MAPPING`
- wrapper_fix: `752417b3f0e7721f1d630f40da22d57e0dae043e`
- wrapper_fix: `69d5fbb0159673ea6737204f4d458a220e81a0c9`

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

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/faux.rs:31 `Registration::new` unsafe=1
- safe API `Registration::new`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/faux.rs:26 `/// Create and register a new faux device with the given name.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/faux.rs:28 `// SAFETY:`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/faux.rs:27 `RESULT_RETURN`
- weak lifetime name /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/faux.rs:31 `LIFETIME_NAMING_PATTERN`
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

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/security.rs:68 `drop` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/security.rs:65 `// SAFETY: By the invariant of `Self`, this frees a context that came from a successful`
- weak lifetime name /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/security.rs:68 `LIFETIME_NAMING_PATTERN`

## W-000008 SignatureDrift

- Risk: Low
- Score: 7.0
- Symbol: pci_enable_device_mem
- Explanation: pci_enable_device_mem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/pci.rs:385 `Device::enable_device_mem` unsafe=1
- safe API `Device::enable_device_mem`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/pci.rs:382 `/// Enable memory resources for this device.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/pci.rs:384 `// SAFETY: `self.as_raw` is guaranteed to be a pointer to a valid `struct pci_dev`.`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`

## W-000011 SignatureDrift

- Risk: Low
- Score: 7.0
- Symbol: pci_set_master
- Explanation: pci_set_master changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/pci.rs:396 `Device::set_master` unsafe=1
- safe API `Device::set_master`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/pci.rs:393 `/// Enable bus-mastering for this device.`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`

## W-000013 SignatureDrift

- Risk: Low
- Score: 7.0
- Symbol: platform_set_drvdata
- Explanation: platform_set_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:327 `From<core::convert::Infallible>::to_result` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/platform.rs:69 `probe_callback` unsafe=1
- safe API `From<core::convert::Infallible>::to_result`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:322 `/// unsafe extern "C" fn probe_callback(`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:323 `///     pdev: *mut bindings::platform_device,`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:324 `/// ) -> kernel::ffi::c_int {`
- wrapper_fix: `ef4dc4cc7001e9cce8a3b556362171648be9ad92`

## W-000001 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: devm_add_action
- Explanation: devm_add_action changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/devres.rs:119 `new` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/devres.rs:123 `new` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/devres.rs:116 `// SAFETY: `devm_add_action` guarantees to call `Self::devres_callback` once `dev` is`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/devres.rs:122 `// SAFETY: We just created another reference to `inner` in order to pass it to`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/devres.rs:125 `FROM_RAW`
- wrapper_fix: `ba268514ea14b44570030e8ed2aef92a38679e85`

## W-000004 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: faux_device_destroy
- Explanation: faux_device_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/faux.rs:55 `drop` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/faux.rs:54 `// SAFETY: `self.0` is a valid registered faux_device via our type invariants.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/faux.rs:59 `// SAFETY: The faux device API is thread-safe as guaranteed by the device core, as long as`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/faux.rs:52 `IMPL_DROP`
- wrapper_fix: `78418f300d3999f1cf8a9ac71065bf2eca61f4dd`

## W-000005 SignatureDrift

- Risk: Low
- Score: -4.0
- Symbol: pci_alloc_irq_vectors
- Explanation: pci_alloc_irq_vectors changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `473b9f331718267815649cd93801da832200db71`

## W-000006 SignatureDrift

- Risk: Low
- Score: -4.0
- Symbol: pci_dev_get
- Explanation: pci_dev_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`

## W-000007 SignatureDrift

- Risk: Low
- Score: -4.0
- Symbol: pci_dev_put
- Explanation: pci_dev_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`

## W-000009 SignatureDrift

- Risk: Low
- Score: -4.0
- Symbol: pci_free_irq_vectors
- Explanation: pci_free_irq_vectors changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `473b9f331718267815649cd93801da832200db71`

## W-000010 SignatureDrift

- Risk: Low
- Score: -4.0
- Symbol: pci_irq_vector
- Explanation: pci_irq_vector changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `473b9f331718267815649cd93801da832200db71`

## W-000012 SignatureDrift

- Risk: Low
- Score: -4.0
- Symbol: platform_device_put
- Explanation: platform_device_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `4d320e30ee04c25c660eca2bb33e846ebb71a79a`
