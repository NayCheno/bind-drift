# BindDrift Ranked Warnings

## W-000009 FieldDrift

- Risk: Medium
- Score: 9.0
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
- binding_only_penalty: `-5.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/auxiliary.rs:269 `release` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/device.rs:170 `None` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/device.rs:183 `Device::get_device` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/device.rs:338 `Device<Ctx>::as_raw` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/device.rs:369 `Device<Ctx>::parent` unsafe=0
- safe API `Device::get_device`
- safe API `Device<Ctx>::as_raw`
- safe API `Device<Ctx>::parent`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/auxiliary.rs:265 `// SAFETY: A `struct auxiliary_device` always has a parent.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/device.rs:165 `///`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/device.rs:166 `/// [`AlwaysRefCounted`]: kernel::sync::aref::AlwaysRefCounted`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/device.rs:170 `OPAQUE`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/device.rs:183 `AREF`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/device.rs:185 `FROM_RAW`
- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`
- wrapper_fix: `4d320e30ee04c25c660eca2bb33e846ebb71a79a`

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

- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/gpu/buddy.rs:469 `GpuBuddy::avail` unsafe=1
- safe API `GpuBuddy::avail`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/gpu/buddy.rs:466 `// SAFETY: Per the type invariant, `inner` contains an initialized`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/gpu/buddy.rs:468 `TO_RESULT_MAPPING`
- wrapper_fix: `b9616d9721bf8a56d5038e85d2ebbe0ec9d56a94`

## W-000010 FieldDrift

- Risk: Low
- Score: 5.0
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
- binding_only_penalty: `-5.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/pci.rs:101 `None` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/pci.rs:123 `remove_callback` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/pci.rs:339 `None` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/pci.rs:345 `as_raw` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/pci.rs:466 `None` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/pci.rs:124 `// SAFETY: The PCI bus only ever calls the remove callback with a valid pointer to a`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/pci.rs:334 `///`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/pci.rs:335 `/// A [`Device`] instance represents a valid `struct pci_dev` created by the C portion of the`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/pci.rs:339 `OPAQUE`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`

## W-000008 SignatureDrift

- Risk: Low
- Score: 2.0
- Symbol: gpu_buddy_init
- Explanation: gpu_buddy_init changed across the selected Linux versions.
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

- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/gpu/buddy.rs:345 `new` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/gpu/buddy.rs:342 `// SAFETY: `ptr` points to valid uninitialized memory from the pin-init`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/gpu/buddy.rs:344 `TO_RESULT_MAPPING`
- weak lifetime name /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/gpu/buddy.rs:345 `LIFETIME_NAMING_PATTERN`
- wrapper_fix: `b9616d9721bf8a56d5038e85d2ebbe0ec9d56a94`

## W-000004 SignatureDrift

- Risk: Low
- Score: -1.0
- Symbol: gpu_buddy_block_offset
- Explanation: gpu_buddy_block_offset changed across the selected Linux versions.
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

- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/gpu/buddy.rs:566 `offset` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/gpu/buddy.rs:563 `/// Get the block's raw offset in the buddy address space (without base offset).`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/gpu/buddy.rs:565 `// SAFETY: `self.as_raw()` is valid per the type's invariants.`
- wrapper_fix: `b9616d9721bf8a56d5038e85d2ebbe0ec9d56a94`

## W-000005 SignatureDrift

- Risk: Low
- Score: -1.0
- Symbol: gpu_buddy_block_order
- Explanation: gpu_buddy_block_order changed across the selected Linux versions.
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

- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/gpu/buddy.rs:572 `order` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/gpu/buddy.rs:569 `/// Get the block order.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/gpu/buddy.rs:571 `// SAFETY: `self.as_raw()` is valid per the type's invariants.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/gpu/buddy.rs:576 `// SAFETY: `Block` is a wrapper around `gpu_buddy_block` which can be`
- wrapper_fix: `b9616d9721bf8a56d5038e85d2ebbe0ec9d56a94`

## W-000006 SignatureDrift

- Risk: Low
- Score: -1.0
- Symbol: gpu_buddy_fini
- Explanation: gpu_buddy_fini changed across the selected Linux versions.
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

- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/gpu/buddy.rs:369 `drop` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/gpu/buddy.rs:367 `// SAFETY: Per the type invariant, `inner` contains an initialized`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/gpu/buddy.rs:373 `// SAFETY: `GpuBuddyInner` can be sent between threads.`
- weak lifetime name /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/gpu/buddy.rs:369 `LIFETIME_NAMING_PATTERN`
- wrapper_fix: `b9616d9721bf8a56d5038e85d2ebbe0ec9d56a94`

## W-000007 SignatureDrift

- Risk: Low
- Score: -1.0
- Symbol: gpu_buddy_free_list
- Explanation: gpu_buddy_free_list changed across the selected Linux versions.
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

- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/gpu/buddy.rs:541 `drop` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/gpu/buddy.rs:537 `// SAFETY:`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/gpu/buddy.rs:546 `/// A GPU buddy block.`
- weak lifetime name /home/nya/workspace/bind-drift/.binddrift/worktrees/HEAD_9207d47f966b/rust/kernel/gpu/buddy.rs:541 `LIFETIME_NAMING_PATTERN`
- wrapper_fix: `b9616d9721bf8a56d5038e85d2ebbe0ec9d56a94`

## W-000001 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: dma_resv_lock
- Explanation: dma_resv_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `9b836641d3bfa1ab096ec6263f0fa6880cb9c5ef`

## W-000002 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: dma_resv_unlock
- Explanation: dma_resv_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `9b836641d3bfa1ab096ec6263f0fa6880cb9c5ef`
