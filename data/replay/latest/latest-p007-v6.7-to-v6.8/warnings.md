# BindDrift Ranked Warnings

## W-000003 SignatureDrift

- Risk: Low
- Score: 6.0
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
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.8/rust/kernel/net/phy.rs:202 `Device::write` unsafe=1
- safe API `Device::write`
- .binddrift/worktrees/v6.8/rust/kernel/net/phy.rs:198 `// SAFETY: `phydev` is pointing to a valid object by the type invariant of `Self`.`
- .binddrift/worktrees/v6.8/rust/kernel/net/phy.rs:201 `TO_RESULT_MAPPING`
- wrapper_fix: `b2e47002b2350f57bfa8fe1c231e9fbb6baef78b`

## W-000002 SignatureDrift

- Risk: Low
- Score: 3.0
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
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.8/rust/kernel/net/phy.rs:186 `Device::read` unsafe=1
- safe API `Device::read`
- .binddrift/worktrees/v6.8/rust/kernel/net/phy.rs:182 `// SAFETY: `phydev` is pointing to a valid object by the type invariant of `Self`.`
- wrapper_fix: `b2e47002b2350f57bfa8fe1c231e9fbb6baef78b`

## W-000007 FieldDrift

- Risk: Low
- Score: -5.0
- Symbol: device
- Explanation: device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'kobj', 'type': 'kobject'}, {'name': 'parent', 'type': '*mut device'}, {'name': 'p', 'type': '*mut device_private'}, {'name': 'init_name', 'type': '*const core::ffi::c_char'}, {'name': 'type_', 'type': '*const device_type'}, {'name': 'bus', 'type': '*const bus_type'}, {'name': 'driver', 'type': '*mut device_driver'}, {'name': 'platform_data', 'type': '*mut core::ffi::c_void'}, {'name': 'driver_data', 'type': '*mut core::ffi::c_void'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'links', 'type': 'dev_links_info'}, {'name': 'power', 'type': 'dev_pm_info'}, {'name': 'pm_domain', 'type': '*mut dev_pm_domain'}, {'name': 'msi', 'type': 'dev_msi_info'}, {'name': 'dma_ops', 'type': '*mut dma_map_ops'}, {'name': 'dma_mask', 'type': '*mut u64_'}, {'name': 'coherent_dma_mask', 'type': 'u64_'}, {'name': 'bus_dma_limit', 'type': 'u64_'}, {'name': 'dma_range_map', 'type': '*mut bus_dma_region'}, {'name': 'dma_parms', 'type': '*mut device_dma_parameters'}, {'name': 'dma_pools', 'type': 'list_head'}, {'name': 'dma_io_tlb_mem', 'type': '*mut io_tlb_mem'}, {'name': 'archdata', 'type': 'dev_archdata'}, {'name': 'of_node', 'type': '*mut device_node'}, {'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'numa_node', 'type': 'core::ffi::c_int'}, {'name': 'devt', 'type': 'dev_t'}, {'name': 'id', 'type': 'u32_'}, {'name': 'devres_lock', 'type': 'spinlock_t'}, {'name': 'devres_head', 'type': 'list_head'}, {'name': 'class', 'type': '*const class'}, {'name': 'groups', 'type': '*mut *const attribute_group'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'iommu_group', 'type': '*mut iommu_group'}, {'name': 'iommu', 'type': '*mut dev_iommu'}, {'name': 'physical_location', 'type': '*mut device_physical_location'}, {'name': 'removable', 'type': 'device_removable'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 3usize]'}]`

### Score Breakdown

- binding_only_penalty: `-5.0`

### Rust Evidence

- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`
- wrapper_fix: `4d320e30ee04c25c660eca2bb33e846ebb71a79a`

## W-000001 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: get_device
- Explanation: get_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `4d320e30ee04c25c660eca2bb33e846ebb71a79a`
- wrapper_fix: `6fe9e919c144f1296d38e2abb10c7ac4320aa7fa`

## W-000004 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: phy_read_mmd
- Explanation: phy_read_mmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `b2e47002b2350f57bfa8fe1c231e9fbb6baef78b`

## W-000005 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: phy_write_mmd
- Explanation: phy_write_mmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `b2e47002b2350f57bfa8fe1c231e9fbb6baef78b`

## W-000006 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: put_device
- Explanation: put_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `6fe9e919c144f1296d38e2abb10c7ac4320aa7fa`
