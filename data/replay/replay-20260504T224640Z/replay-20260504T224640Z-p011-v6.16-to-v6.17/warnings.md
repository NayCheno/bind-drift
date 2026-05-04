# BindDrift Ranked Warnings

## W-000767 SignatureDrift

- Risk: High
- Score: 14.6
- Symbol: regulator_get
- Explanation: regulator_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `20`

## W-000510 SignatureDrift

- Risk: High
- Score: 14.0
- Symbol: dev_get_drvdata
- Explanation: dev_get_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `17`

## W-000765 SignatureDrift

- Risk: High
- Score: 13.4
- Symbol: regulator_disable
- Explanation: regulator_disable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `14`

## W-001213 NullabilityDrift

- Risk: High
- Score: 13.2
- Symbol: regulator_get
- Explanation: regulator_get has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/include/linux/regulator/consumer.h:305 `return NULL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:280 `get_internal` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:278 `// SAFETY: It is safe to call `regulator_get()`, on a device pointer`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:282 `// SAFETY: We can safely trust `inner` to be a pointer to a valid`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:277 `RESULT_RETURN`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:280 `AS_PTR`

## W-000132 SignatureDrift

- Risk: High
- Score: 13.0
- Symbol: acpi_enable
- Explanation: acpi_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `12`

## W-000721 SignatureDrift

- Risk: High
- Score: 13.0
- Symbol: platform_set_drvdata
- Explanation: platform_set_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `12`

## W-001212 NullabilityDrift

- Risk: High
- Score: 13.0
- Symbol: acpi_match_device
- Explanation: acpi_match_device has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/include/linux/acpi.h:953 `return NULL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/driver.rs:249 `acpi_id_info` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/driver.rs:246 `// SAFETY:`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/driver.rs:254 `// SAFETY: `DeviceId` is a `#[repr(transparent)]` wrapper of `struct acpi_device_id``
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/driver.rs:249 `AS_PTR`

## W-000117 SignatureDrift

- Risk: High
- Score: 12.6
- Symbol: acpi_disable
- Explanation: acpi_disable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `10`

## W-000661 SignatureDrift

- Risk: High
- Score: 12.6
- Symbol: ktime_get_real
- Explanation: ktime_get_real changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `10`

## W-000885 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: acpi_device
- Explanation: acpi_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'pld_crc', 'type': 'u32_'}, {'name': 'device_type', 'type': 'ffi::c_int'}, {'name': 'handle', 'type': 'acpi_handle'}, {'name': 'fwnode', 'type': 'fwnode_handle'}, {'name': 'wakeup_list', 'type': 'list_head'}, {'name': 'del_list', 'type': 'list_head'}, {'name': 'status', 'type': 'acpi_device_status'}, {'name': 'flags', 'type': 'acpi_device_flags'}, {'name': 'pnp', 'type': 'acpi_device_pnp'}, {'name': 'power', 'type': 'acpi_device_power'}, {'name': 'wakeup', 'type': 'acpi_device_wakeup'}, {'name': 'performance', 'type': 'acpi_device_perf'}, {'name': 'dir', 'type': 'acpi_device_dir'}, {'name': 'data', 'type': 'acpi_device_data'}, {'name': 'handler', 'type': '*mut acpi_scan_handler'}, {'name': 'hp', 'type': '*mut acpi_hotplug_context'}, {'name': 'swnodes', 'type': '*mut acpi_device_software_nodes'}, {'name': 'driver_gpios', 'type': '*const acpi_gpio_mapping'}, {'name': 'driver_data', 'type': '*mut ffi::c_void'}, {'name': 'dev', 'type': 'device'}, {'name': 'physical_node_count', 'type': 'ffi::c_uint'}, {'name': 'dep_unmet', 'type': 'ffi::c_uint'}, {'name': 'physical_node_list', 'type': 'list_head'}, {'name': 'physical_node_lock', 'type': 'mutex'}, {'name': 'remove', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut acpi_device)>'}]`

### Rust Evidence

- Graph edges: `50`

## W-000887 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: bpf_link
- Explanation: bpf_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'refcnt', 'type': 'atomic64_t'}, {'name': 'id', 'type': 'u32_'}, {'name': 'type_', 'type': 'bpf_link_type'}, {'name': 'ops', 'type': '*const bpf_link_ops'}, {'name': 'prog', 'type': '*mut bpf_prog'}, {'name': 'sleepable', 'type': 'bool_'}, {'name': '__bindgen_anon_1', 'type': 'bpf_link__bindgen_ty_1'}]`
- New: `[{'name': 'refcnt', 'type': 'atomic64_t'}, {'name': 'id', 'type': 'u32_'}, {'name': 'type_', 'type': 'bpf_link_type'}, {'name': 'ops', 'type': '*const bpf_link_ops'}, {'name': 'prog', 'type': '*mut bpf_prog'}, {'name': 'flags', 'type': 'u32_'}, {'name': 'attach_type', 'type': 'bpf_attach_type'}, {'name': '__bindgen_anon_1', 'type': 'bpf_link__bindgen_ty_1'}, {'name': 'sleepable', 'type': 'bool_'}]`

### Rust Evidence

- Graph edges: `41`

## W-000890 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: bpf_map
- Explanation: bpf_map changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'ops', 'type': '*const bpf_map_ops'}, {'name': 'inner_map_meta', 'type': '*mut bpf_map'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'map_type', 'type': 'bpf_map_type'}, {'name': 'key_size', 'type': 'u32_'}, {'name': 'value_size', 'type': 'u32_'}, {'name': 'max_entries', 'type': 'u32_'}, {'name': 'map_extra', 'type': 'u64_'}, {'name': 'map_flags', 'type': 'u32_'}, {'name': 'id', 'type': 'u32_'}, {'name': 'record', 'type': '*mut btf_record'}, {'name': 'numa_node', 'type': 'ffi::c_int'}, {'name': 'btf_key_type_id', 'type': 'u32_'}, {'name': 'btf_value_type_id', 'type': 'u32_'}, {'name': 'btf_vmlinux_value_type_id', 'type': 'u32_'}, {'name': 'btf', 'type': '*mut btf'}, {'name': 'name', 'type': '[ffi::c_char; 16usize]'}, {'name': 'freeze_mutex', 'type': 'mutex'}, {'name': 'refcnt', 'type': 'atomic64_t'}, {'name': 'usercnt', 'type': 'atomic64_t'}, {'name': '__bindgen_anon_1', 'type': 'bpf_map__bindgen_ty_1'}, {'name': 'writecnt', 'type': 'atomic64_t'}, {'name': 'owner', 'type': 'bpf_map__bindgen_ty_2'}, {'name': 'bypass_spec_v1', 'type': 'bool_'}, {'name': 'frozen', 'type': 'bool_'}, {'name': 'free_after_mult_rcu_gp', 'type': 'bool_'}, {'name': 'free_after_rcu_gp', 'type': 'bool_'}, {'name': 'sleepable_refcnt', 'type': 'atomic64_t'}, {'name': 'elem_count', 'type': '*mut s64'}]`
- New: `[{'name': 'ops', 'type': '*const bpf_map_ops'}, {'name': 'inner_map_meta', 'type': '*mut bpf_map'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'map_type', 'type': 'bpf_map_type'}, {'name': 'key_size', 'type': 'u32_'}, {'name': 'value_size', 'type': 'u32_'}, {'name': 'max_entries', 'type': 'u32_'}, {'name': 'map_extra', 'type': 'u64_'}, {'name': 'map_flags', 'type': 'u32_'}, {'name': 'id', 'type': 'u32_'}, {'name': 'record', 'type': '*mut btf_record'}, {'name': 'numa_node', 'type': 'ffi::c_int'}, {'name': 'btf_key_type_id', 'type': 'u32_'}, {'name': 'btf_value_type_id', 'type': 'u32_'}, {'name': 'btf_vmlinux_value_type_id', 'type': 'u32_'}, {'name': 'btf', 'type': '*mut btf'}, {'name': 'name', 'type': '[ffi::c_char; 16usize]'}, {'name': 'freeze_mutex', 'type': 'mutex'}, {'name': 'refcnt', 'type': 'atomic64_t'}, {'name': 'usercnt', 'type': 'atomic64_t'}, {'name': '__bindgen_anon_1', 'type': 'bpf_map__bindgen_ty_1'}, {'name': 'writecnt', 'type': 'atomic64_t'}, {'name': 'owner_lock', 'type': 'spinlock_t'}, {'name': 'owner', 'type': '*mut bpf_map_owner'}, {'name': 'bypass_spec_v1', 'type': 'bool_'}, {'name': 'frozen', 'type': 'bool_'}, {'name': 'free_after_mult_rcu_gp', 'type': 'bool_'}, {'name': 'free_after_rcu_gp', 'type': 'bool_'}, {'name': 'sleepable_refcnt', 'type': 'atomic64_t'}, {'name': 'elem_count', 'type': '*mut s64'}, {'name': 'cookie', 'type': 'u64_'}]`

### Rust Evidence

- Graph edges: `48`

## W-000898 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: drm_file
- Explanation: drm_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'authenticated', 'type': 'bool_'}, {'name': 'stereo_allowed', 'type': 'bool_'}, {'name': 'universal_planes', 'type': 'bool_'}, {'name': 'atomic', 'type': 'bool_'}, {'name': 'aspect_ratio_allowed', 'type': 'bool_'}, {'name': 'writeback_connectors', 'type': 'bool_'}, {'name': 'was_master', 'type': 'bool_'}, {'name': 'is_master', 'type': 'bool_'}, {'name': 'supports_virtualized_cursor_plane', 'type': 'bool_'}, {'name': 'master', 'type': '*mut drm_master'}, {'name': 'master_lookup_lock', 'type': 'spinlock_t'}, {'name': 'pid', 'type': '*mut pid'}, {'name': 'client_id', 'type': 'u64_'}, {'name': 'magic', 'type': 'drm_magic_t'}, {'name': 'lhead', 'type': 'list_head'}, {'name': 'minor', 'type': '*mut drm_minor'}, {'name': 'object_idr', 'type': 'idr'}, {'name': 'table_lock', 'type': 'spinlock_t'}, {'name': 'syncobj_idr', 'type': 'idr'}, {'name': 'syncobj_table_lock', 'type': 'spinlock_t'}, {'name': 'filp', 'type': '*mut file'}, {'name': 'driver_priv', 'type': '*mut ffi::c_void'}, {'name': 'fbs', 'type': 'list_head'}, {'name': 'fbs_lock', 'type': 'mutex'}, {'name': 'blobs', 'type': 'list_head'}, {'name': 'event_wait', 'type': 'wait_queue_head_t'}, {'name': 'pending_event_list', 'type': 'list_head'}, {'name': 'event_list', 'type': 'list_head'}, {'name': 'event_space', 'type': 'ffi::c_int'}, {'name': 'event_read_lock', 'type': 'mutex'}, {'name': 'prime', 'type': 'drm_prime_file_private'}, {'name': 'client_name', 'type': '*const ffi::c_char'}, {'name': 'client_name_lock', 'type': 'mutex'}]`
- New: `[{'name': 'authenticated', 'type': 'bool_'}, {'name': 'stereo_allowed', 'type': 'bool_'}, {'name': 'universal_planes', 'type': 'bool_'}, {'name': 'atomic', 'type': 'bool_'}, {'name': 'aspect_ratio_allowed', 'type': 'bool_'}, {'name': 'writeback_connectors', 'type': 'bool_'}, {'name': 'was_master', 'type': 'bool_'}, {'name': 'is_master', 'type': 'bool_'}, {'name': 'supports_virtualized_cursor_plane', 'type': 'bool_'}, {'name': 'master', 'type': '*mut drm_master'}, {'name': 'master_lookup_lock', 'type': 'spinlock_t'}, {'name': 'pid', 'type': '*mut pid'}, {'name': 'client_id', 'type': 'u64_'}, {'name': 'magic', 'type': 'drm_magic_t'}, {'name': 'lhead', 'type': 'list_head'}, {'name': 'minor', 'type': '*mut drm_minor'}, {'name': 'object_idr', 'type': 'idr'}, {'name': 'table_lock', 'type': 'spinlock_t'}, {'name': 'syncobj_idr', 'type': 'idr'}, {'name': 'syncobj_table_lock', 'type': 'spinlock_t'}, {'name': 'filp', 'type': '*mut file'}, {'name': 'driver_priv', 'type': '*mut ffi::c_void'}, {'name': 'fbs', 'type': 'list_head'}, {'name': 'fbs_lock', 'type': 'mutex'}, {'name': 'blobs', 'type': 'list_head'}, {'name': 'event_wait', 'type': 'wait_queue_head_t'}, {'name': 'pending_event_list', 'type': 'list_head'}, {'name': 'event_list', 'type': 'list_head'}, {'name': 'event_space', 'type': 'ffi::c_int'}, {'name': 'event_read_lock', 'type': 'mutex'}, {'name': 'prime', 'type': 'drm_prime_file_private'}, {'name': 'client_name', 'type': '*const ffi::c_char'}, {'name': 'client_name_lock', 'type': 'mutex'}, {'name': 'debugfs_client', 'type': '*mut dentry'}]`

### Rust Evidence

- Graph edges: `43`

## W-000911 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: phy_device
- Explanation: phy_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mdio', 'type': 'mdio_device'}, {'name': 'drv', 'type': '*const phy_driver'}, {'name': 'devlink', 'type': '*mut device_link'}, {'name': 'phyindex', 'type': 'u32_'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'c45_ids', 'type': 'phy_c45_device_ids'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'rate_matching', 'type': 'ffi::c_int'}, {'name': 'state', 'type': 'phy_state'}, {'name': 'dev_flags', 'type': 'u32_'}, {'name': 'interface', 'type': 'phy_interface_t'}, {'name': 'possible_interfaces', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'speed', 'type': 'ffi::c_int'}, {'name': 'duplex', 'type': 'ffi::c_int'}, {'name': 'port', 'type': 'ffi::c_int'}, {'name': 'pause', 'type': 'ffi::c_int'}, {'name': 'asym_pause', 'type': 'ffi::c_int'}, {'name': 'master_slave_get', 'type': 'u8_'}, {'name': 'master_slave_set', 'type': 'u8_'}, {'name': 'master_slave_state', 'type': 'u8_'}, {'name': 'supported', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'advertising', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'lp_advertising', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'adv_old', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'supported_eee', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'advertising_eee', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'eee_disabled_modes', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'enable_tx_lpi', 'type': 'bool_'}, {'name': 'eee_active', 'type': 'bool_'}, {'name': 'eee_cfg', 'type': 'eee_config'}, {'name': 'host_interfaces', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'leds', 'type': 'list_head'}, {'name': 'irq', 'type': 'ffi::c_int'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'shared', 'type': '*mut phy_package_shared'}, {'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'ehdr', 'type': '*mut ffi::c_void'}, {'name': 'nest', 'type': '*mut nlattr'}, {'name': 'state_queue', 'type': 'delayed_work'}, {'name': 'lock', 'type': 'mutex'}, {'name': 'sfp_bus_attached', 'type': 'bool_'}, {'name': 'sfp_bus', 'type': '*mut sfp_bus'}, {'name': 'phylink', 'type': '*mut phylink'}, {'name': 'attached_dev', 'type': '*mut net_device'}, {'name': 'mii_ts', 'type': '*mut mii_timestamper'}, {'name': 'psec', 'type': '*mut pse_control'}, {'name': 'mdix', 'type': 'u8_'}, {'name': 'mdix_ctrl', 'type': 'u8_'}, {'name': 'pma_extable', 'type': 'ffi::c_int'}, {'name': 'link_down_events', 'type': 'ffi::c_uint'}, {'name': 'adjust_link', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut net_device)>'}]`
- New: `[{'name': 'mdio', 'type': 'mdio_device'}, {'name': 'drv', 'type': '*const phy_driver'}, {'name': 'devlink', 'type': '*mut device_link'}, {'name': 'phyindex', 'type': 'u32_'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'c45_ids', 'type': 'phy_c45_device_ids'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'rate_matching', 'type': 'ffi::c_int'}, {'name': 'state', 'type': 'phy_state'}, {'name': 'dev_flags', 'type': 'u32_'}, {'name': 'interface', 'type': 'phy_interface_t'}, {'name': 'possible_interfaces', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'speed', 'type': 'ffi::c_int'}, {'name': 'duplex', 'type': 'ffi::c_int'}, {'name': 'port', 'type': 'ffi::c_int'}, {'name': 'pause', 'type': 'ffi::c_int'}, {'name': 'asym_pause', 'type': 'ffi::c_int'}, {'name': 'master_slave_get', 'type': 'u8_'}, {'name': 'master_slave_set', 'type': 'u8_'}, {'name': 'master_slave_state', 'type': 'u8_'}, {'name': 'supported', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'advertising', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'lp_advertising', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'adv_old', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'supported_eee', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'advertising_eee', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'eee_disabled_modes', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'enable_tx_lpi', 'type': 'bool_'}, {'name': 'eee_active', 'type': 'bool_'}, {'name': 'eee_cfg', 'type': 'eee_config'}, {'name': 'host_interfaces', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'leds', 'type': 'list_head'}, {'name': 'irq', 'type': 'ffi::c_int'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'ehdr', 'type': '*mut ffi::c_void'}, {'name': 'nest', 'type': '*mut nlattr'}, {'name': 'state_queue', 'type': 'delayed_work'}, {'name': 'lock', 'type': 'mutex'}, {'name': 'sfp_bus_attached', 'type': 'bool_'}, {'name': 'sfp_bus', 'type': '*mut sfp_bus'}, {'name': 'phylink', 'type': '*mut phylink'}, {'name': 'attached_dev', 'type': '*mut net_device'}, {'name': 'mii_ts', 'type': '*mut mii_timestamper'}, {'name': 'psec', 'type': '*mut pse_control'}, {'name': 'mdix', 'type': 'u8_'}, {'name': 'mdix_ctrl', 'type': 'u8_'}, {'name': 'pma_extable', 'type': 'ffi::c_int'}, {'name': 'link_down_events', 'type': 'ffi::c_uint'}, {'name': 'adjust_link', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut net_device)>'}]`

### Rust Evidence

- Graph edges: `50`

## W-000912 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: pid
- Explanation: pid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'count', 'type': 'refcount_t'}, {'name': 'level', 'type': 'ffi::c_uint'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'stashed', 'type': '*mut dentry'}, {'name': 'ino', 'type': 'u64_'}, {'name': 'pidfs_node', 'type': 'rb_node'}, {'name': 'tasks', 'type': '[hlist_head; 4usize]'}, {'name': 'inodes', 'type': 'hlist_head'}, {'name': 'wait_pidfd', 'type': 'wait_queue_head_t'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'numbers', 'type': '__IncompleteArrayField<upid>'}]`
- New: `[{'name': 'count', 'type': 'refcount_t'}, {'name': 'level', 'type': 'ffi::c_uint'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': '__bindgen_anon_1', 'type': 'pid__bindgen_ty_1'}, {'name': 'tasks', 'type': '[hlist_head; 4usize]'}, {'name': 'inodes', 'type': 'hlist_head'}, {'name': 'wait_pidfd', 'type': 'wait_queue_head_t'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'numbers', 'type': '__IncompleteArrayField<upid>'}]`

### Rust Evidence

- Graph edges: `30`

## W-000511 SignatureDrift

- Risk: High
- Score: 12.4
- Symbol: dev_set_drvdata
- Explanation: dev_set_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `9`

## W-000665 SignatureDrift

- Risk: High
- Score: 12.4
- Symbol: link
- Explanation: link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(14usize, 1u8) as u32) } } #[inline] pub fn set_link(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(15usize, 1u8) as u32) } } #[inline] pub fn set_link(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `9`

## W-000263 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: acpi_match_device
- Explanation: acpi_match_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000648 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: is_of_node
- Explanation: is_of_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000768 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: regulator_get_voltage
- Explanation: regulator_get_voltage changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000771 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: regulator_set_voltage
- Explanation: regulator_set_voltage changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000685 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: might_resched
- Explanation: might_resched changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000766 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: regulator_enable
- Explanation: regulator_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000770 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: regulator_put
- Explanation: regulator_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000781 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: resource_size
- Explanation: resource_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000893 FieldDrift

- Risk: High
- Score: 12.0
- Symbol: cgroup_subsys
- Explanation: cgroup_subsys changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'css_alloc', 'type': '::core::option::Option<'}, {'name': 'css_offline', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_released', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_free', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_reset', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_killed', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_rstat_flush', 'type': '::core::option::Option<'}, {'name': 'css_extra_stat_show', 'type': '::core::option::Option<'}, {'name': 'css_local_stat_show', 'type': '::core::option::Option<'}, {'name': 'cancel_attach', 'type': '::core::option::Option<unsafe extern "C" fn(tset: *mut cgroup_taskset)>'}, {'name': 'attach', 'type': '::core::option::Option<unsafe extern "C" fn(tset: *mut cgroup_taskset)>'}, {'name': 'post_attach', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'can_fork', 'type': '::core::option::Option<'}, {'name': 'fork', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'bind', 'type': '::core::option::Option<unsafe extern "C" fn(root_css: *mut cgroup_subsys_state)>'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'legacy_name', 'type': '*const ffi::c_char'}, {'name': 'root', 'type': '*mut cgroup_root'}, {'name': 'css_idr', 'type': 'idr'}, {'name': 'cfts', 'type': 'list_head'}, {'name': 'dfl_cftypes', 'type': '*mut cftype'}, {'name': 'legacy_cftypes', 'type': '*mut cftype'}, {'name': 'depends_on', 'type': 'ffi::c_uint'}, {'name': 'rstat_ss_lock', 'type': 'spinlock_t'}, {'name': 'rstat_ss_cpu_lock', 'type': '*mut raw_spinlock_t'}]`
- New: `[{'name': 'css_alloc', 'type': '::core::option::Option<'}, {'name': 'css_offline', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_released', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_free', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_reset', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_killed', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_rstat_flush', 'type': '::core::option::Option<'}, {'name': 'css_extra_stat_show', 'type': '::core::option::Option<'}, {'name': 'css_local_stat_show', 'type': '::core::option::Option<'}, {'name': 'cancel_attach', 'type': '::core::option::Option<unsafe extern "C" fn(tset: *mut cgroup_taskset)>'}, {'name': 'attach', 'type': '::core::option::Option<unsafe extern "C" fn(tset: *mut cgroup_taskset)>'}, {'name': 'post_attach', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'can_fork', 'type': '::core::option::Option<'}, {'name': 'fork', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'bind', 'type': '::core::option::Option<unsafe extern "C" fn(root_css: *mut cgroup_subsys_state)>'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'legacy_name', 'type': '*const ffi::c_char'}, {'name': 'root', 'type': '*mut cgroup_root'}, {'name': 'css_idr', 'type': 'idr'}, {'name': 'cfts', 'type': 'list_head'}, {'name': 'dfl_cftypes', 'type': '*mut cftype'}, {'name': 'legacy_cftypes', 'type': '*mut cftype'}, {'name': 'depends_on', 'type': 'ffi::c_uint'}, {'name': 'rstat_ss_lock', 'type': 'spinlock_t'}, {'name': 'lhead', 'type': '*mut llist_head'}]`

### Rust Evidence

- Graph edges: `17`

## W-000414 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: acpi_table_parse
- Explanation: acpi_table_parse changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000512 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: devm_add_action_or_reset
- Explanation: devm_add_action_or_reset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000517 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: dma_set_mask_and_coherent
- Explanation: dma_set_mask_and_coherent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000638 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: ioremap_np
- Explanation: ioremap_np changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000657 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: ksys_sync_helper
- Explanation: ksys_sync_helper changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000658 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: ktime_get_boottime
- Explanation: ktime_get_boottime changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000660 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: ktime_get_clocktai
- Explanation: ktime_get_clocktai changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000745 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: poll_wait
- Explanation: poll_wait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000769 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: regulator_is_enabled
- Explanation: regulator_is_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000844 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: valid
- Explanation: valid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000461 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: autoneg
- Explanation: autoneg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(13usize, 1u8) as u32) } } #[inline] pub fn set_autoneg(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(14usize, 1u8) as u32) } } #[inline] pub fn set_autoneg(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `5`

## W-000583 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: folio_mapping
- Explanation: folio_mapping changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000607 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: fwnode_handle_put
- Explanation: fwnode_handle_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000663 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: ktime_to_us
- Explanation: ktime_to_us changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000924 FieldDrift

- Risk: High
- Score: 11.6
- Symbol: task_struct
- Explanation: task_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'ffi::c_uint'}, {'name': 'saved_state', 'type': 'ffi::c_uint'}, {'name': 'stack', 'type': '*mut ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'ptrace', 'type': 'ffi::c_uint'}, {'name': 'on_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_cpu', 'type': 'ffi::c_int'}, {'name': 'on_rq', 'type': 'ffi::c_int'}, {'name': 'prio', 'type': 'ffi::c_int'}, {'name': 'static_prio', 'type': 'ffi::c_int'}, {'name': 'normal_prio', 'type': 'ffi::c_int'}, {'name': 'rt_priority', 'type': 'ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'dl_server', 'type': '*mut sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'ffi::c_uint'}, {'name': 'policy', 'type': 'ffi::c_uint'}, {'name': 'max_allowed_capacity', 'type': 'ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut ffi::c_void'}, {'name': 'migration_disabled', 'type': 'ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'rcu_tasks_exit_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_exit_list', 'type': 'list_head'}, {'name': 'trc_reader_nesting', 'type': 'ffi::c_int'}, {'name': 'trc_ipi_to_cpu', 'type': 'ffi::c_int'}, {'name': 'trc_reader_special', 'type': 'rcu_special'}, {'name': 'trc_holdout_list', 'type': 'list_head'}, {'name': 'trc_blkd_node', 'type': 'list_head'}, {'name': 'trc_blkd_cpu', 'type': 'ffi::c_int'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'faults_disabled_mapping', 'type': '*mut address_space'}, {'name': 'exit_state', 'type': 'ffi::c_int'}, {'name': 'exit_code', 'type': 'ffi::c_int'}, {'name': 'exit_signal', 'type': 'ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'ffi::c_int'}, {'name': 'jobctl', 'type': 'ffi::c_ulong'}, {'name': 'personality', 'type': 'ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'worker_private', 'type': '*mut ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'journal_info', 'type': '*mut ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'ffi::c_uint'}, {'name': 'perf_recursion', 'type': '[u8_; 4usize]'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'perf_ctx_data', 'type': '*mut perf_ctx_data'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'ffi::c_short'}, {'name': 'il_weight', 'type': 'u8_'}, {'name': 'pref_node_fork', 'type': 'ffi::c_short'}, {'name': 'rseq', 'type': '*mut rseq'}, {'name': 'rseq_len', 'type': 'u32_'}, {'name': 'rseq_sig', 'type': 'u32_'}, {'name': 'rseq_event_mask', 'type': 'ffi::c_ulong'}, {'name': 'mm_cid', 'type': 'ffi::c_int'}, {'name': 'last_mm_cid', 'type': 'ffi::c_int'}, {'name': 'migrate_from_cpu', 'type': 'ffi::c_int'}, {'name': 'mm_cid_active', 'type': 'ffi::c_int'}, {'name': 'cid_work', 'type': 'callback_head'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'bpf_net_context', 'type': '*mut bpf_net_context'}, {'name': 'mce_vaddr', 'type': '*mut ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': 'thread', 'type': 'thread_struct'}]`
- New: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'ffi::c_uint'}, {'name': 'saved_state', 'type': 'ffi::c_uint'}, {'name': 'stack', 'type': '*mut ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'ptrace', 'type': 'ffi::c_uint'}, {'name': 'on_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_cpu', 'type': 'ffi::c_int'}, {'name': 'on_rq', 'type': 'ffi::c_int'}, {'name': 'prio', 'type': 'ffi::c_int'}, {'name': 'static_prio', 'type': 'ffi::c_int'}, {'name': 'normal_prio', 'type': 'ffi::c_int'}, {'name': 'rt_priority', 'type': 'ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'dl_server', 'type': '*mut sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': '__bindgen_padding_1', 'type': 'u64'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'ffi::c_uint'}, {'name': 'policy', 'type': 'ffi::c_uint'}, {'name': 'max_allowed_capacity', 'type': 'ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut ffi::c_void'}, {'name': 'migration_disabled', 'type': 'ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'rcu_tasks_exit_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_exit_list', 'type': 'list_head'}, {'name': 'trc_reader_nesting', 'type': 'ffi::c_int'}, {'name': 'trc_ipi_to_cpu', 'type': 'ffi::c_int'}, {'name': 'trc_reader_special', 'type': 'rcu_special'}, {'name': 'trc_holdout_list', 'type': 'list_head'}, {'name': 'trc_blkd_node', 'type': 'list_head'}, {'name': 'trc_blkd_cpu', 'type': 'ffi::c_int'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'faults_disabled_mapping', 'type': '*mut address_space'}, {'name': 'exit_state', 'type': 'ffi::c_int'}, {'name': 'exit_code', 'type': 'ffi::c_int'}, {'name': 'exit_signal', 'type': 'ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'ffi::c_int'}, {'name': 'jobctl', 'type': 'ffi::c_ulong'}, {'name': 'personality', 'type': 'ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'worker_private', 'type': '*mut ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'blocked_on', 'type': '*mut mutex'}, {'name': 'journal_info', 'type': '*mut ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'ffi::c_uint'}, {'name': 'perf_recursion', 'type': '[u8_; 4usize]'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'perf_ctx_data', 'type': '*mut perf_ctx_data'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'ffi::c_short'}, {'name': 'il_weight', 'type': 'u8_'}, {'name': 'pref_node_fork', 'type': 'ffi::c_short'}, {'name': 'rseq', 'type': '*mut rseq'}, {'name': 'rseq_len', 'type': 'u32_'}, {'name': 'rseq_sig', 'type': 'u32_'}, {'name': 'rseq_event_mask', 'type': 'ffi::c_ulong'}, {'name': 'mm_cid', 'type': 'ffi::c_int'}, {'name': 'last_mm_cid', 'type': 'ffi::c_int'}, {'name': 'migrate_from_cpu', 'type': 'ffi::c_int'}, {'name': 'mm_cid_active', 'type': 'ffi::c_int'}, {'name': 'cid_work', 'type': 'callback_head'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'bpf_net_context', 'type': '*mut bpf_net_context'}, {'name': 'mce_vaddr', 'type': '*mut ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': 'thread', 'type': 'thread_struct'}]`

### Rust Evidence

- Graph edges: `15`

## W-000553 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: filemap_fdatawrite
- Explanation: filemap_fdatawrite changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000605 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: fsleep
- Explanation: fsleep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000662 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: ktime_to_ms
- Explanation: ktime_to_ms changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000671 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: lru_add_drain
- Explanation: lru_add_drain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000773 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: release_region
- Explanation: release_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000001 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: WARN_ON
- Explanation: WARN_ON changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000015 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: __folio_lock
- Explanation: __folio_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000103 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: acpi_device_fix_up_power
- Explanation: acpi_device_fix_up_power changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000109 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: acpi_device_notify
- Explanation: acpi_device_notify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000139 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: acpi_enter_sleep_state
- Explanation: acpi_enter_sleep_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000143 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: acpi_evaluate_dsm
- Explanation: acpi_evaluate_dsm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000196 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: acpi_get_subsystem_id
- Explanation: acpi_get_subsystem_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000198 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: acpi_get_table
- Explanation: acpi_get_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000201 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: acpi_get_timer
- Explanation: acpi_get_timer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000356 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: acpi_read
- Explanation: acpi_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000407 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: acpi_subsys_suspend
- Explanation: acpi_subsys_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000440 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: acpi_write
- Explanation: acpi_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000558 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: filemap_get_folios
- Explanation: filemap_get_folios changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000620 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: hibernate
- Explanation: hibernate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000736 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: pm_suspend
- Explanation: pm_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000772 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: release_mem_region
- Explanation: release_mem_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-001164 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: acpi_evaluate_dsm
- Explanation: acpi_evaluate_dsm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['acpi_handle handle', 'const guid_t *guid', 'u64 rev', 'u64 func', 'union acpi_object *argv4'], 'return_type': 'union acpi_object *'}`
- New: `{'params': ['acpi_handle handle', 'const guid_t *guid', 'u64 rev', 'u64 func', 'union acpi_object *argv4'], 'return_type': 'static inline union acpi_object *'}`

### Rust Evidence

- Graph edges: `3`

## W-001214 ErrorDrift

- Risk: High
- Score: 11.2
- Symbol: regulator_get_voltage
- Explanation: regulator_get_voltage has ERROR_CODE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/include/linux/regulator/consumer.h:504 `return -EINVAL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:269 `Regulator<T>::get_voltage` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:266 `/// Gets the current voltage of the regulator.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:268 `// SAFETY: Safe as per the type invariants of `Regulator`.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:267 `RESULT_RETURN`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.17/rust/kernel/regulator.rs:269 `AS_PTR`

## W-000050 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_bus_get_status
- Explanation: acpi_bus_get_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000066 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_create_platform_device
- Explanation: acpi_create_platform_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000073 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_dev_for_each_child
- Explanation: acpi_dev_for_each_child changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000078 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_dev_get_first_match_dev
- Explanation: acpi_dev_get_first_match_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000101 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_dev_uid_to_integer
- Explanation: acpi_dev_uid_to_integer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000106 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_device_get_match_data
- Explanation: acpi_device_get_match_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000108 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_device_modalias
- Explanation: acpi_device_modalias changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000115 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_device_uevent_modalias
- Explanation: acpi_device_uevent_modalias changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000119 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_disable_event
- Explanation: acpi_disable_event changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000124 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_dma_get_range
- Explanation: acpi_dma_get_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000135 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_enable_event
- Explanation: acpi_enable_event changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000147 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_evaluate_object
- Explanation: acpi_evaluate_object changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000153 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_exception
- Explanation: acpi_exception changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000166 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_get_data
- Explanation: acpi_get_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000172 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_get_first_physical_node
- Explanation: acpi_get_first_physical_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000179 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_get_local_address
- Explanation: acpi_get_local_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000185 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_get_next_subnode
- Explanation: acpi_get_next_subnode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000190 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_get_pci_dev
- Explanation: acpi_get_pci_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000193 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_get_processor_handle
- Explanation: acpi_get_processor_handle changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000223 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_install_address_space_handler
- Explanation: acpi_install_address_space_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000233 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_install_interface
- Explanation: acpi_install_interface changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000239 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_install_table
- Explanation: acpi_install_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000252 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_leave_sleep_state
- Explanation: acpi_leave_sleep_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000254 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_load_table
- Explanation: acpi_load_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000262 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_match_acpi_device
- Explanation: acpi_match_acpi_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000275 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_nvs_nosave
- Explanation: acpi_nvs_nosave changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000313 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_os_signal
- Explanation: acpi_os_signal changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000335 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_parse_spcr
- Explanation: acpi_parse_spcr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000347 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_pm_set_device_wakeup
- Explanation: acpi_pm_set_device_wakeup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000351 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_processor_evaluate_cst
- Explanation: acpi_processor_evaluate_cst changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000359 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_reconfig_notifier_register
- Explanation: acpi_reconfig_notifier_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000360 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_reconfig_notifier_unregister
- Explanation: acpi_reconfig_notifier_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000364 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_register_lps0_dev
- Explanation: acpi_register_lps0_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000379 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_reset
- Explanation: acpi_reset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000380 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_resource_consumer
- Explanation: acpi_resource_consumer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000391 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_set_gpe
- Explanation: acpi_set_gpe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000410 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_subsystem_init
- Explanation: acpi_subsystem_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000412 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_table_init
- Explanation: acpi_table_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000416 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_table_parse_entries
- Explanation: acpi_table_parse_entries changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000422 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_terminate
- Explanation: acpi_terminate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000446 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: alloc_workqueue
- Explanation: alloc_workqueue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `2`

## W-000551 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: filemap_fdatawait_range
- Explanation: filemap_fdatawait_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000554 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: filemap_fdatawrite_range
- Explanation: filemap_fdatawrite_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000573 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: folio_add_lru
- Explanation: folio_add_lru changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000587 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: folio_wait_bit
- Explanation: folio_wait_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000589 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: folio_wait_private_2
- Explanation: folio_wait_private_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000592 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: folio_wait_writeback
- Explanation: folio_wait_writeback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000634 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: invalidate_inode_pages2
- Explanation: invalidate_inode_pages2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000670 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: lpit_read_residency_count_address
- Explanation: lpit_read_residency_count_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000673 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: lru_add_drain_cpu
- Explanation: lru_add_drain_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000755 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: read_cache_page
- Explanation: read_cache_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000780 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: reserved
- Explanation: reserved changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000847 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vmf_insert_mixed
- Explanation: vmf_insert_mixed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'addr', 'type': 'ffi::c_ulong'}, {'name': 'pfn', 'type': 'pfn_t'}], 'return_type': 'vm_fault_t'}`
- New: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'addr', 'type': 'ffi::c_ulong'}, {'name': 'pfn', 'type': 'ffi::c_ulong'}], 'return_type': 'vm_fault_t'}`

### Rust Evidence

- Graph edges: `2`

## W-000914 FieldDrift

- Risk: High
- Score: 11.0
- Symbol: queue_limits
- Explanation: queue_limits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'min_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_write_streams', 'type': 'ffi::c_ushort'}, {'name': 'write_stream_granularity', 'type': 'ffi::c_uint'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`
- New: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'min_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_write_streams', 'type': 'ffi::c_ushort'}, {'name': 'write_stream_granularity', 'type': 'ffi::c_uint'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`

### Rust Evidence

- Graph edges: `12`

## W-001158 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_dev_get_first_match_dev
- Explanation: acpi_dev_get_first_match_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const char *hid', 'const char *uid', 's64 hrv'], 'return_type': 'struct acpi_device *'}`
- New: `{'params': ['const char *hid', 'const char *uid', 's64 hrv'], 'return_type': 'static inline struct acpi_device *'}`

### Rust Evidence

- Graph edges: `2`

## W-001160 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_dev_uid_to_integer
- Explanation: acpi_dev_uid_to_integer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct acpi_device *adev', 'u64 *integer'], 'return_type': 'int'}`
- New: `{'params': ['struct acpi_device *adev', 'u64 *integer'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `2`

## W-001162 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: acpi_dma_get_range
- Explanation: acpi_dma_get_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct device *dev', 'const struct bus_dma_region **map'], 'return_type': 'int'}`
- New: `{'params': ['struct device *dev', 'const struct bus_dma_region **map'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `2`

## W-001192 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: generic_file_mmap
- Explanation: generic_file_mmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct file *', 'struct vm_area_struct *'], 'return_type': 'extern int'}`
- New: `{'params': ['struct file *', 'struct vm_area_struct *'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `2`

## W-001193 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: generic_file_readonly_mmap
- Explanation: generic_file_readonly_mmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct file *', 'struct vm_area_struct *'], 'return_type': 'extern int'}`
- New: `{'params': ['struct file *', 'struct vm_area_struct *'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `2`

## W-000002 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __acpi_acquire_global_lock
- Explanation: __acpi_acquire_global_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000003 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __acpi_bus_register_driver
- Explanation: __acpi_bus_register_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000004 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __acpi_map_table
- Explanation: __acpi_map_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000005 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __acpi_node_get_property_reference
- Explanation: __acpi_node_get_property_reference changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000006 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __acpi_probe_device_table
- Explanation: __acpi_probe_device_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000007 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __acpi_release_global_lock
- Explanation: __acpi_release_global_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000008 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __acpi_unmap_table
- Explanation: __acpi_unmap_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000009 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __filemap_add_folio
- Explanation: __filemap_add_folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000010 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __filemap_fdatawrite_range
- Explanation: __filemap_fdatawrite_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000011 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __filemap_get_folio
- Explanation: __filemap_get_folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000012 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __filemap_remove_folio
- Explanation: __filemap_remove_folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000013 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __filemap_set_wb_err
- Explanation: __filemap_set_wb_err changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000014 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __folio_cancel_dirty
- Explanation: __folio_cancel_dirty changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000016 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __folio_lock_killable
- Explanation: __folio_lock_killable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000017 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __folio_lock_or_retry
- Explanation: __folio_lock_or_retry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000018 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __folio_mark_dirty
- Explanation: __folio_mark_dirty changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000019 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __refrigerator
- Explanation: __refrigerator changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000020 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __register_one_node
- Explanation: __register_one_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000021 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __swap_count
- Explanation: __swap_count changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000022 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __thaw_task
- Explanation: __thaw_task changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000023 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __trace_set_need_resched
- Explanation: __trace_set_need_resched changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000024 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: _install_special_mapping
- Explanation: _install_special_mapping changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'addr', 'type': 'ffi::c_ulong'}, {'name': 'len', 'type': 'ffi::c_ulong'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'spec', 'type': '*const vm_special_mapping'}], 'return_type': '*mut vm_area_struct'}`
- New: `{'params': [{'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'addr', 'type': 'ffi::c_ulong'}, {'name': 'len', 'type': 'ffi::c_ulong'}, {'name': 'vm_flags', 'type': 'vm_flags_t'}, {'name': 'spec', 'type': '*const vm_special_mapping'}], 'return_type': '*mut vm_area_struct'}`

### Rust Evidence

- Graph edges: `1`

## W-000025 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_acquire_global_lock
- Explanation: acpi_acquire_global_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000026 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_acquire_mutex
- Explanation: acpi_acquire_mutex changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000027 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_add_pm_notifier
- Explanation: acpi_add_pm_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000028 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_any_fixed_event_status_set
- Explanation: acpi_any_fixed_event_status_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000029 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_any_gpe_status_set
- Explanation: acpi_any_gpe_status_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000030 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_arch_init
- Explanation: acpi_arch_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000031 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_ata_match
- Explanation: acpi_ata_match changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000032 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_attach_data
- Explanation: acpi_attach_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000033 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_bay_match
- Explanation: acpi_bay_match changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000034 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_bind_one
- Explanation: acpi_bind_one changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000035 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_bios_error
- Explanation: acpi_bios_error changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000036 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_bios_exception
- Explanation: acpi_bios_exception changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000037 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_bios_warning
- Explanation: acpi_bios_warning changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000038 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_blacklisted
- Explanation: acpi_blacklisted changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000039 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_boot_init
- Explanation: acpi_boot_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000040 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_boot_table_init
- Explanation: acpi_boot_table_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000041 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_boot_table_prepare
- Explanation: acpi_boot_table_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000042 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_buffer_to_resource
- Explanation: acpi_buffer_to_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000043 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_bus_attach_private_data
- Explanation: acpi_bus_attach_private_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000044 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_bus_can_wakeup
- Explanation: acpi_bus_can_wakeup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000045 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_bus_detach_private_data
- Explanation: acpi_bus_detach_private_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000046 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_bus_for_each_dev
- Explanation: acpi_bus_for_each_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000047 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_bus_generate_netlink_event
- Explanation: acpi_bus_generate_netlink_event changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000048 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_bus_get_ejd
- Explanation: acpi_bus_get_ejd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000049 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_bus_get_private_data
- Explanation: acpi_bus_get_private_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000051 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_bus_get_status_handle
- Explanation: acpi_bus_get_status_handle changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000052 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_bus_init_power
- Explanation: acpi_bus_init_power changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000053 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_bus_power_manageable
- Explanation: acpi_bus_power_manageable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000054 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_bus_private_data_handler
- Explanation: acpi_bus_private_data_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000055 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_bus_scan
- Explanation: acpi_bus_scan changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000056 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_bus_set_power
- Explanation: acpi_bus_set_power changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000057 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_bus_trim
- Explanation: acpi_bus_trim changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000058 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_bus_unregister_driver
- Explanation: acpi_bus_unregister_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000059 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_bus_update_power
- Explanation: acpi_bus_update_power changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000060 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_check_address_range
- Explanation: acpi_check_address_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000061 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_check_dsm
- Explanation: acpi_check_dsm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000062 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_check_region
- Explanation: acpi_check_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000063 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_check_resource_conflict
- Explanation: acpi_check_resource_conflict changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000064 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_clear_event
- Explanation: acpi_clear_event changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000065 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_clear_gpe
- Explanation: acpi_clear_gpe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000067 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_data_add_props
- Explanation: acpi_data_add_props changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000068 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_debug_trace
- Explanation: acpi_debug_trace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000069 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_decode_pld_buffer
- Explanation: acpi_decode_pld_buffer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000070 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_detach_data
- Explanation: acpi_detach_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000071 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_clear_dependencies
- Explanation: acpi_dev_clear_dependencies changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000072 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_filter_resource_type
- Explanation: acpi_dev_filter_resource_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000074 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_for_each_child_reverse
- Explanation: acpi_dev_for_each_child_reverse changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000075 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_found
- Explanation: acpi_dev_found changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000076 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_free_resource_list
- Explanation: acpi_dev_free_resource_list changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000077 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_get_dma_resources
- Explanation: acpi_dev_get_dma_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000079 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_get_irq_type
- Explanation: acpi_dev_get_irq_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000080 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_get_memory_resources
- Explanation: acpi_dev_get_memory_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000081 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_get_next_consumer_dev
- Explanation: acpi_dev_get_next_consumer_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000082 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_get_next_match_dev
- Explanation: acpi_dev_get_next_match_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000083 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_get_property
- Explanation: acpi_dev_get_property changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000084 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_get_resources
- Explanation: acpi_dev_get_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000085 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_install_notify_handler
- Explanation: acpi_dev_install_notify_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000086 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_irq_flags
- Explanation: acpi_dev_irq_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000087 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_pm_attach
- Explanation: acpi_dev_pm_attach changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000088 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_power_state_for_wake
- Explanation: acpi_dev_power_state_for_wake changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000089 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_power_up_children_with_adr
- Explanation: acpi_dev_power_up_children_with_adr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000090 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_present
- Explanation: acpi_dev_present changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000091 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_ready_for_enumeration
- Explanation: acpi_dev_ready_for_enumeration changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000092 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_remove_notify_handler
- Explanation: acpi_dev_remove_notify_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000093 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_resource_address_space
- Explanation: acpi_dev_resource_address_space changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000094 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_resource_ext_address_space
- Explanation: acpi_dev_resource_ext_address_space changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000095 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_resource_interrupt
- Explanation: acpi_dev_resource_interrupt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000096 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_resource_io
- Explanation: acpi_dev_resource_io changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000097 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_resource_memory
- Explanation: acpi_dev_resource_memory changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000098 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_resume
- Explanation: acpi_dev_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000099 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_state_d0
- Explanation: acpi_dev_state_d0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000100 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_suspend
- Explanation: acpi_dev_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000102 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_device_dep
- Explanation: acpi_device_dep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000104 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_device_fix_up_power_children
- Explanation: acpi_device_fix_up_power_children changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000105 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_device_fix_up_power_extended
- Explanation: acpi_device_fix_up_power_extended changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000107 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_device_hid
- Explanation: acpi_device_hid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000110 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_device_notify_remove
- Explanation: acpi_device_notify_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000111 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_device_override_status
- Explanation: acpi_device_override_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000112 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_device_power_add_dependent
- Explanation: acpi_device_power_add_dependent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000113 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_device_power_remove_dependent
- Explanation: acpi_device_power_remove_dependent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000114 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_device_set_power
- Explanation: acpi_device_set_power changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000116 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_device_update_power
- Explanation: acpi_device_update_power changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000118 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_disable_all_gpes
- Explanation: acpi_disable_all_gpes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000120 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_disable_gpe
- Explanation: acpi_disable_gpe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000121 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_disable_wakeup_device_power
- Explanation: acpi_disable_wakeup_device_power changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000122 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dispatch_gpe
- Explanation: acpi_dispatch_gpe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000123 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dma_configure_id
- Explanation: acpi_dma_configure_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000125 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dma_supported
- Explanation: acpi_dma_supported changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000126 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dock_match
- Explanation: acpi_dock_match changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000127 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_driver_match_device
- Explanation: acpi_driver_match_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000128 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_duplicate_processor_id
- Explanation: acpi_duplicate_processor_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000129 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_early_init
- Explanation: acpi_early_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000130 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_ec_mark_gpe_for_wake
- Explanation: acpi_ec_mark_gpe_for_wake changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000131 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_ec_set_gpe_wake_mask
- Explanation: acpi_ec_set_gpe_wake_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000133 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_enable_all_runtime_gpes
- Explanation: acpi_enable_all_runtime_gpes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000134 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_enable_all_wakeup_gpes
- Explanation: acpi_enable_all_wakeup_gpes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000136 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_enable_gpe
- Explanation: acpi_enable_gpe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000137 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_enable_subsystem
- Explanation: acpi_enable_subsystem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000138 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_enable_wakeup_device_power
- Explanation: acpi_enable_wakeup_device_power changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000140 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_enter_sleep_state_prep
- Explanation: acpi_enter_sleep_state_prep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000141 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_enter_sleep_state_s4bios
- Explanation: acpi_enter_sleep_state_s4bios changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000142 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_error
- Explanation: acpi_error changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000144 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_evaluate_ej0
- Explanation: acpi_evaluate_ej0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000145 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_evaluate_integer
- Explanation: acpi_evaluate_integer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000146 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_evaluate_lck
- Explanation: acpi_evaluate_lck changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000148 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_evaluate_object_typed
- Explanation: acpi_evaluate_object_typed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000149 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_evaluate_ost
- Explanation: acpi_evaluate_ost changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000150 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_evaluate_reference
- Explanation: acpi_evaluate_reference changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000151 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_evaluate_reg
- Explanation: acpi_evaluate_reg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000152 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_evaluation_failure_warn
- Explanation: acpi_evaluation_failure_warn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000154 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_execute_reg_methods
- Explanation: acpi_execute_reg_methods changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000155 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_execute_simple_method
- Explanation: acpi_execute_simple_method changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000156 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_extract_package
- Explanation: acpi_extract_package changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000157 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_fetch_acpi_dev
- Explanation: acpi_fetch_acpi_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000158 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_find_child_by_adr
- Explanation: acpi_find_child_by_adr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000159 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_find_child_device
- Explanation: acpi_find_child_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000160 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_find_root_pointer
- Explanation: acpi_find_root_pointer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000161 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_finish_gpe
- Explanation: acpi_finish_gpe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000162 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_format_exception
- Explanation: acpi_format_exception changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000163 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_generic_reduced_hw_init
- Explanation: acpi_generic_reduced_hw_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000164 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_acpi_dev
- Explanation: acpi_get_acpi_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000165 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_current_resources
- Explanation: acpi_get_current_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000167 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_data_full
- Explanation: acpi_get_data_full changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000168 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_devices
- Explanation: acpi_get_devices changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000169 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_dma_attr
- Explanation: acpi_get_dma_attr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000170 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_event_resources
- Explanation: acpi_get_event_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000171 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_event_status
- Explanation: acpi_get_event_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000173 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_gpe_device
- Explanation: acpi_get_gpe_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000174 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_gpe_status
- Explanation: acpi_get_gpe_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000175 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_gsi_dispatcher
- Explanation: acpi_get_gsi_dispatcher changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000176 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_handle
- Explanation: acpi_get_handle changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000177 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_ioapic_id
- Explanation: acpi_get_ioapic_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000178 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_irq_routing_table
- Explanation: acpi_get_irq_routing_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000180 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_local_u64_address
- Explanation: acpi_get_local_u64_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000181 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_lps0_constraint
- Explanation: acpi_get_lps0_constraint changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000182 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_madt_revision
- Explanation: acpi_get_madt_revision changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000183 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_name
- Explanation: acpi_get_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000184 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_next_object
- Explanation: acpi_get_next_object changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000186 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_node
- Explanation: acpi_get_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000187 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_object_info
- Explanation: acpi_get_object_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000188 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_override_irq
- Explanation: acpi_get_override_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000189 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_parent
- Explanation: acpi_get_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000191 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_physical_device_location
- Explanation: acpi_get_physical_device_location changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000192 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_possible_resources
- Explanation: acpi_get_possible_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000194 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_sleep_type_data
- Explanation: acpi_get_sleep_type_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000195 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_statistics
- Explanation: acpi_get_statistics changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000197 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_system_info
- Explanation: acpi_get_system_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000199 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_table_by_index
- Explanation: acpi_get_table_by_index changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000200 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_table_header
- Explanation: acpi_get_table_header changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000202 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_timer_duration
- Explanation: acpi_get_timer_duration changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000203 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_timer_resolution
- Explanation: acpi_get_timer_resolution changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000204 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_type
- Explanation: acpi_get_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000205 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_vendor_resource
- Explanation: acpi_get_vendor_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000206 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_wakeup_address
- Explanation: acpi_get_wakeup_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000207 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_gsi_to_irq
- Explanation: acpi_gsi_to_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000208 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_handle_list_equal
- Explanation: acpi_handle_list_equal changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000209 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_handle_list_free
- Explanation: acpi_handle_list_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000210 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_handle_list_replace
- Explanation: acpi_handle_list_replace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000211 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_handle_path
- Explanation: acpi_handle_path changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000212 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_handle_printk
- Explanation: acpi_handle_printk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000213 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_has_method
- Explanation: acpi_has_method changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000214 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_hw_disable_all_gpes
- Explanation: acpi_hw_disable_all_gpes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000215 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_hw_enable_all_wakeup_gpes
- Explanation: acpi_hw_enable_all_wakeup_gpes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000216 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_info
- Explanation: acpi_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000217 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_init_pcc
- Explanation: acpi_init_pcc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000218 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_initialize_debugger
- Explanation: acpi_initialize_debugger changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000219 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_initialize_hp_context
- Explanation: acpi_initialize_hp_context changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000220 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_initialize_objects
- Explanation: acpi_initialize_objects changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000221 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_initialize_subsystem
- Explanation: acpi_initialize_subsystem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000222 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_initialize_tables
- Explanation: acpi_initialize_tables changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000224 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_install_address_space_handler_no_reg
- Explanation: acpi_install_address_space_handler_no_reg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000225 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_install_cmos_rtc_space_handler
- Explanation: acpi_install_cmos_rtc_space_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000226 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_install_exception_handler
- Explanation: acpi_install_exception_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000227 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_install_fixed_event_handler
- Explanation: acpi_install_fixed_event_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000228 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_install_global_event_handler
- Explanation: acpi_install_global_event_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000229 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_install_gpe_block
- Explanation: acpi_install_gpe_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000230 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_install_gpe_handler
- Explanation: acpi_install_gpe_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000231 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_install_gpe_raw_handler
- Explanation: acpi_install_gpe_raw_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000232 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_install_initialization_handler
- Explanation: acpi_install_initialization_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000234 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_install_interface_handler
- Explanation: acpi_install_interface_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000235 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_install_method
- Explanation: acpi_install_method changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000236 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_install_notify_handler
- Explanation: acpi_install_notify_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000237 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_install_physical_table
- Explanation: acpi_install_physical_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000238 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_install_sci_handler
- Explanation: acpi_install_sci_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000240 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_install_table_handler
- Explanation: acpi_install_table_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000241 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_ioapic_add
- Explanation: acpi_ioapic_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000242 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_ioapic_registered
- Explanation: acpi_ioapic_registered changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000243 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_iommu_fwspec_init
- Explanation: acpi_iommu_fwspec_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000244 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_irq_create_hierarchy
- Explanation: acpi_irq_create_hierarchy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000245 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_irq_penalty_init
- Explanation: acpi_irq_penalty_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000246 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_irq_stats_init
- Explanation: acpi_irq_stats_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000247 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_is_pnp_device
- Explanation: acpi_is_pnp_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000248 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_is_root_bridge
- Explanation: acpi_is_root_bridge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000249 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_is_video_device
- Explanation: acpi_is_video_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000250 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_isa_irq_available
- Explanation: acpi_isa_irq_available changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000251 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_isa_irq_to_gsi
- Explanation: acpi_isa_irq_to_gsi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000253 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_leave_sleep_state_prep
- Explanation: acpi_leave_sleep_state_prep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000255 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_load_tables
- Explanation: acpi_load_tables changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000256 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_locate_initial_tables
- Explanation: acpi_locate_initial_tables changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000257 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_lock_hp_context
- Explanation: acpi_lock_hp_context changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000258 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_map_cpu
- Explanation: acpi_map_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000259 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_map_pxm_to_node
- Explanation: acpi_map_pxm_to_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000260 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_mark_gpe_for_wake
- Explanation: acpi_mark_gpe_for_wake changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000261 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_mask_gpe
- Explanation: acpi_mask_gpe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000264 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_match_device_ids
- Explanation: acpi_match_device_ids changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000265 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_match_platform_list
- Explanation: acpi_match_platform_list changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000266 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_mps_check
- Explanation: acpi_mps_check changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000267 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_mrrm_max_mem_region
- Explanation: acpi_mrrm_max_mem_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000268 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_node_backed_by_real_pxm
- Explanation: acpi_node_backed_by_real_pxm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000269 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_node_prop_get
- Explanation: acpi_node_prop_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000270 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_notifier_call_chain
- Explanation: acpi_notifier_call_chain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000271 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_numa_init
- Explanation: acpi_numa_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000272 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_numa_processor_affinity_init
- Explanation: acpi_numa_processor_affinity_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000273 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_numa_x2apic_affinity_init
- Explanation: acpi_numa_x2apic_affinity_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000274 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_nvs_for_each_region
- Explanation: acpi_nvs_for_each_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000276 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_nvs_nosave_s3
- Explanation: acpi_nvs_nosave_s3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000277 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_nvs_register
- Explanation: acpi_nvs_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000278 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_old_suspend_ordering
- Explanation: acpi_old_suspend_ordering changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000279 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_acquire_lock
- Explanation: acpi_os_acquire_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000280 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_create_cache
- Explanation: acpi_os_create_cache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000281 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_create_semaphore
- Explanation: acpi_os_create_semaphore changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000282 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_delete_cache
- Explanation: acpi_os_delete_cache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000283 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_delete_lock
- Explanation: acpi_os_delete_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000284 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_delete_semaphore
- Explanation: acpi_os_delete_semaphore changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000285 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_enter_sleep
- Explanation: acpi_os_enter_sleep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000286 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_execute
- Explanation: acpi_os_execute changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000287 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_get_iomem
- Explanation: acpi_os_get_iomem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000288 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_get_line
- Explanation: acpi_os_get_line changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000289 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_get_physical_address
- Explanation: acpi_os_get_physical_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000290 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_get_root_pointer
- Explanation: acpi_os_get_root_pointer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000291 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_get_timer
- Explanation: acpi_os_get_timer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000292 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_initialize
- Explanation: acpi_os_initialize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000293 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_install_interrupt_handler
- Explanation: acpi_os_install_interrupt_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000294 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_map_generic_address
- Explanation: acpi_os_map_generic_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000295 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_map_iomem
- Explanation: acpi_os_map_iomem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000296 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_map_memory
- Explanation: acpi_os_map_memory changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000297 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_notify_command_complete
- Explanation: acpi_os_notify_command_complete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000298 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_physical_table_override
- Explanation: acpi_os_physical_table_override changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000299 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_predefined_override
- Explanation: acpi_os_predefined_override changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000300 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_prepare_extended_sleep
- Explanation: acpi_os_prepare_extended_sleep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000301 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_prepare_sleep
- Explanation: acpi_os_prepare_sleep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000302 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_printf
- Explanation: acpi_os_printf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000303 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_purge_cache
- Explanation: acpi_os_purge_cache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000304 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_read_iomem
- Explanation: acpi_os_read_iomem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000305 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_read_memory
- Explanation: acpi_os_read_memory changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000306 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_read_pci_configuration
- Explanation: acpi_os_read_pci_configuration changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000307 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_read_port
- Explanation: acpi_os_read_port changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000308 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_release_lock
- Explanation: acpi_os_release_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000309 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_release_object
- Explanation: acpi_os_release_object changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000310 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_remove_interrupt_handler
- Explanation: acpi_os_remove_interrupt_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000311 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_set_prepare_extended_sleep
- Explanation: acpi_os_set_prepare_extended_sleep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000312 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_set_prepare_sleep
- Explanation: acpi_os_set_prepare_sleep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000314 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_signal_semaphore
- Explanation: acpi_os_signal_semaphore changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000315 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_sleep
- Explanation: acpi_os_sleep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000316 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_stall
- Explanation: acpi_os_stall changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000317 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_table_override
- Explanation: acpi_os_table_override changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000318 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_terminate
- Explanation: acpi_os_terminate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000319 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_trace_point
- Explanation: acpi_os_trace_point changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000320 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_unmap_generic_address
- Explanation: acpi_os_unmap_generic_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000321 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_unmap_iomem
- Explanation: acpi_os_unmap_iomem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000322 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_unmap_memory
- Explanation: acpi_os_unmap_memory changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000323 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_vprintf
- Explanation: acpi_os_vprintf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000324 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_wait_command_ready
- Explanation: acpi_os_wait_command_ready changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000325 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_wait_events_complete
- Explanation: acpi_os_wait_events_complete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000326 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_wait_semaphore
- Explanation: acpi_os_wait_semaphore changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000327 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_write_memory
- Explanation: acpi_os_write_memory changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000328 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_write_pci_configuration
- Explanation: acpi_os_write_pci_configuration changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000329 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_os_write_port
- Explanation: acpi_os_write_port changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000330 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_osi_is_win8
- Explanation: acpi_osi_is_win8 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000331 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_osi_setup
- Explanation: acpi_osi_setup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000332 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_parse_entries_array
- Explanation: acpi_parse_entries_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000333 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_parse_mcfg
- Explanation: acpi_parse_mcfg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000334 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_parse_mp_wake
- Explanation: acpi_parse_mp_wake changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000336 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_pci_find_root
- Explanation: acpi_pci_find_root changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000337 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_pci_irq_disable
- Explanation: acpi_pci_irq_disable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000338 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_pci_irq_enable
- Explanation: acpi_pci_irq_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000339 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_pci_irq_lookup
- Explanation: acpi_pci_irq_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000340 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_pci_link_allocate_irq
- Explanation: acpi_pci_link_allocate_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000341 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_pci_link_free_irq
- Explanation: acpi_pci_link_free_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000342 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_penalize_isa_irq
- Explanation: acpi_penalize_isa_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000343 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_penalize_sci_irq
- Explanation: acpi_penalize_sci_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000344 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_pic_sci_set_trigger
- Explanation: acpi_pic_sci_set_trigger changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000345 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_pm_device_can_wakeup
- Explanation: acpi_pm_device_can_wakeup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000346 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_pm_device_sleep_state
- Explanation: acpi_pm_device_sleep_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000348 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_pm_wakeup_event
- Explanation: acpi_pm_wakeup_event changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000349 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_power_state_string
- Explanation: acpi_power_state_string changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000350 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_processor_claim_cst_control
- Explanation: acpi_processor_claim_cst_control changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000352 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_purge_cached_objects
- Explanation: acpi_purge_cached_objects changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000353 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_put_table
- Explanation: acpi_put_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000354 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_quirk_skip_acpi_ac_and_battery
- Explanation: acpi_quirk_skip_acpi_ac_and_battery changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000355 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_quirk_skip_serdev_enumeration
- Explanation: acpi_quirk_skip_serdev_enumeration changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000357 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_read_bit_register
- Explanation: acpi_read_bit_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000358 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_reallocate_root_table
- Explanation: acpi_reallocate_root_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000361 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_reduced_hardware
- Explanation: acpi_reduced_hardware changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000362 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_register_gsi
- Explanation: acpi_register_gsi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000363 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_register_ioapic
- Explanation: acpi_register_ioapic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000365 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_register_wakeup_handler
- Explanation: acpi_register_wakeup_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000366 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_release_global_lock
- Explanation: acpi_release_global_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000367 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_release_mutex
- Explanation: acpi_release_mutex changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000368 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_remove_address_space_handler
- Explanation: acpi_remove_address_space_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000369 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_remove_cmos_rtc_space_handler
- Explanation: acpi_remove_cmos_rtc_space_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000370 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_remove_fixed_event_handler
- Explanation: acpi_remove_fixed_event_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000371 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_remove_gpe_block
- Explanation: acpi_remove_gpe_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000372 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_remove_gpe_handler
- Explanation: acpi_remove_gpe_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000373 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_remove_interface
- Explanation: acpi_remove_interface changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000374 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_remove_notify_handler
- Explanation: acpi_remove_notify_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000375 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_remove_pm_notifier
- Explanation: acpi_remove_pm_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000376 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_remove_sci_handler
- Explanation: acpi_remove_sci_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000377 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_remove_table_handler
- Explanation: acpi_remove_table_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000378 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_reserve_initial_tables
- Explanation: acpi_reserve_initial_tables changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000381 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_resource_to_address64
- Explanation: acpi_resource_to_address64 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000382 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_resources_are_enforced
- Explanation: acpi_resources_are_enforced changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000383 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_run_osc
- Explanation: acpi_run_osc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000384 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_scan_add_dep
- Explanation: acpi_scan_add_dep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000385 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_scan_add_handler
- Explanation: acpi_scan_add_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000386 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_scan_lock_acquire
- Explanation: acpi_scan_lock_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000387 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_scan_lock_release
- Explanation: acpi_scan_lock_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000388 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_set_current_resources
- Explanation: acpi_set_current_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000389 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_set_debugger_thread_id
- Explanation: acpi_set_debugger_thread_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000390 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_set_firmware_waking_vector
- Explanation: acpi_set_firmware_waking_vector changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000392 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_set_gpe_wake_mask
- Explanation: acpi_set_gpe_wake_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000393 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_set_gsi_to_irq_fallback
- Explanation: acpi_set_gsi_to_irq_fallback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000394 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_set_irq_model
- Explanation: acpi_set_irq_model changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000395 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_set_modalias
- Explanation: acpi_set_modalias changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000396 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_setup_gpe_for_wake
- Explanation: acpi_setup_gpe_for_wake changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000397 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_sleep_no_blacklist
- Explanation: acpi_sleep_no_blacklist changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000398 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_sleep_state_supported
- Explanation: acpi_sleep_state_supported changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000399 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_storage_d3
- Explanation: acpi_storage_d3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000400 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_subsys_complete
- Explanation: acpi_subsys_complete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000401 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_subsys_freeze
- Explanation: acpi_subsys_freeze changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000402 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_subsys_poweroff
- Explanation: acpi_subsys_poweroff changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000403 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_subsys_prepare
- Explanation: acpi_subsys_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000404 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_subsys_restore_early
- Explanation: acpi_subsys_restore_early changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000405 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_subsys_runtime_resume
- Explanation: acpi_subsys_runtime_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000406 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_subsys_runtime_suspend
- Explanation: acpi_subsys_runtime_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000408 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_subsys_suspend_late
- Explanation: acpi_subsys_suspend_late changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000409 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_subsys_suspend_noirq
- Explanation: acpi_subsys_suspend_noirq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000411 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_subsystem_status
- Explanation: acpi_subsystem_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000413 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_table_init_complete
- Explanation: acpi_table_init_complete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000415 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_table_parse_cedt
- Explanation: acpi_table_parse_cedt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000417 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_table_parse_entries_array
- Explanation: acpi_table_parse_entries_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000418 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_table_parse_madt
- Explanation: acpi_table_parse_madt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000419 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_table_print_madt_entry
- Explanation: acpi_table_print_madt_entry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000420 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_table_upgrade
- Explanation: acpi_table_upgrade changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000421 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_target_system_state
- Explanation: acpi_target_system_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000423 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_terminate_debugger
- Explanation: acpi_terminate_debugger changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000424 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_unbind_one
- Explanation: acpi_unbind_one changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000425 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_unload_parent_table
- Explanation: acpi_unload_parent_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000426 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_unload_table
- Explanation: acpi_unload_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000427 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_unlock_hp_context
- Explanation: acpi_unlock_hp_context changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000428 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_unmap_cpu
- Explanation: acpi_unmap_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000429 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_unregister_gsi
- Explanation: acpi_unregister_gsi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000430 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_unregister_ioapic
- Explanation: acpi_unregister_ioapic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000431 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_unregister_lps0_dev
- Explanation: acpi_unregister_lps0_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000432 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_unregister_wakeup_handler
- Explanation: acpi_unregister_wakeup_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000433 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_update_all_gpes
- Explanation: acpi_update_all_gpes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000434 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_update_interfaces
- Explanation: acpi_update_interfaces changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000435 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_wait_for_acpi_ipmi
- Explanation: acpi_wait_for_acpi_ipmi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000436 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_walk_namespace
- Explanation: acpi_walk_namespace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000437 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_walk_resource_buffer
- Explanation: acpi_walk_resource_buffer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000438 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_walk_resources
- Explanation: acpi_walk_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000439 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_warning
- Explanation: acpi_warning changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000441 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_write_bit_register
- Explanation: acpi_write_bit_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000442 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: add_swap_count_continuation
- Explanation: add_swap_count_continuation changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000443 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: add_swap_extent
- Explanation: add_swap_extent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000444 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: add_to_page_cache_lru
- Explanation: add_to_page_cache_lru changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000445 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: add_wait_queue_priority_exclusive
- Explanation: add_wait_queue_priority_exclusive changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000447 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_workqueue_attrs
- Explanation: alloc_workqueue_attrs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000448 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_workqueue_attrs_noprof
- Explanation: alloc_workqueue_attrs_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000449 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_workqueue_noprof
- Explanation: alloc_workqueue_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000450 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_acpi_add_auto_dep
- Explanation: arch_acpi_add_auto_dep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000451 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_hibernation_header_restore
- Explanation: arch_hibernation_header_restore changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000452 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_hibernation_header_save
- Explanation: arch_hibernation_header_save changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000453 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_post_acpi_subsys_init
- Explanation: arch_post_acpi_subsys_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000454 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_reserve_mem_area
- Explanation: arch_reserve_mem_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000455 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_resume_nosmt
- Explanation: arch_resume_nosmt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000456 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_sort_irqchip_probe
- Explanation: arch_sort_irqchip_probe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000457 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_suspend_disable_irqs
- Explanation: arch_suspend_disable_irqs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000458 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_suspend_enable_irqs
- Explanation: arch_suspend_enable_irqs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000459 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_sync_kernel_mappings
- Explanation: arch_sync_kernel_mappings changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000460 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: asm_acpi_mp_play_dead
- Explanation: asm_acpi_mp_play_dead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000462 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: autoneg_complete
- Explanation: autoneg_complete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(15usize, 1u8) as u32) } } #[inline] pub fn set_autoneg_complete(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(16usize, 1u8) as u32) } } #[inline] pub fn set_autoneg_complete(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000465 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: backing_file_user_path
- Explanation: backing_file_user_path changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'f', 'type': '*mut file'}], 'return_type': '*mut path'}`
- New: `{'params': [{'name': 'f', 'type': '*const file'}], 'return_type': '*mut path'}`

### Rust Evidence

- Graph edges: `1`

## W-000466 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: backlight
- Explanation: backlight changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000467 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bad_srat
- Explanation: bad_srat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000468 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: balloon_set_new_target
- Explanation: balloon_set_new_target changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000469 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: battery_present
- Explanation: battery_present changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000470 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_num_online_queues
- Explanation: blk_mq_num_online_queues changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000471 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_num_possible_queues
- Explanation: blk_mq_num_possible_queues changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000472 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_bprintf_prepare
- Explanation: bpf_bprintf_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'fmt', 'type': '*mut ffi::c_char'}, {'name': 'fmt_size', 'type': 'u32_'}, {'name': 'raw_args', 'type': '*const u64_'}, {'name': 'num_args', 'type': 'u32_'}, {'name': 'data', 'type': '*mut bpf_bprintf_data'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'fmt', 'type': '*const ffi::c_char'}, {'name': 'fmt_size', 'type': 'u32_'}, {'name': 'raw_args', 'type': '*const u64_'}, {'name': 'num_args', 'type': 'u32_'}, {'name': 'data', 'type': '*mut bpf_bprintf_data'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000473 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_jit_bypass_spec_v1
- Explanation: bpf_jit_bypass_spec_v1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000474 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_jit_bypass_spec_v4
- Explanation: bpf_jit_bypass_spec_v4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000475 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_prog_find_from_stack
- Explanation: bpf_prog_find_from_stack changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000476 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_prog_get_file_line
- Explanation: bpf_prog_get_file_line changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000477 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_prog_stream_free
- Explanation: bpf_prog_stream_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000478 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_prog_stream_init
- Explanation: bpf_prog_stream_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000479 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_prog_stream_read
- Explanation: bpf_prog_stream_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000480 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_put_buffers
- Explanation: bpf_put_buffers changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000481 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_stream_stage_commit
- Explanation: bpf_stream_stage_commit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000482 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_stream_stage_dump_stack
- Explanation: bpf_stream_stage_dump_stack changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000483 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_stream_stage_free
- Explanation: bpf_stream_stage_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000484 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_stream_stage_init
- Explanation: bpf_stream_stage_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000485 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_stream_stage_printk
- Explanation: bpf_stream_stage_printk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000486 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_try_get_buffers
- Explanation: bpf_try_get_buffers changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000487 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: broken_intx_masking
- Explanation: broken_intx_masking changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(30usize, 1u8) as u32) } } #[inline] pub fn set_broken_intx_masking(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(31usize, 1u8) as u32) } } #[inline] pub fn set_broken_intx_masking(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000488 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_type_is_i32
- Explanation: btf_type_is_i32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000489 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_type_is_i64
- Explanation: btf_type_is_i64 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000490 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_type_is_primitive
- Explanation: btf_type_is_primitive changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000491 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bus_address
- Explanation: bus_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000494 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cca_seen
- Explanation: cca_seen changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000495 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cdat_table_parse
- Explanation: cdat_table_parse changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000496 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_freezing
- Explanation: cgroup_freezing changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000497 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: check_move_unevictable_folios
- Explanation: check_move_unevictable_folios changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000498 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: clear_page_dirty_for_io
- Explanation: clear_page_dirty_for_io changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000499 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: clear_pfnblock_bit
- Explanation: clear_pfnblock_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000500 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: coherent_dma
- Explanation: coherent_dma changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000501 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: count_swap_pages
- Explanation: count_swap_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000502 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_attack_vector_mitigated
- Explanation: cpu_attack_vector_mitigated changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000503 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_show_vmscape
- Explanation: cpu_show_vmscape changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000505 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_splice_alias_ops
- Explanation: d_splice_alias_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000506 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: default_timestamp
- Explanation: default_timestamp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(19usize, 1u8) as u32) } } #[inline] pub fn set_default_timestamp(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(20usize, 1u8) as u32) } } #[inline] pub fn set_default_timestamp(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000507 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: delete_from_page_cache_batch
- Explanation: delete_from_page_cache_batch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000508 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: demand_offline
- Explanation: demand_offline changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000509 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: detach_power_off
- Explanation: detach_power_off changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000513 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: disable_srat
- Explanation: disable_srat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000514 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_fence_driver_name
- Explanation: dma_fence_driver_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000515 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_fence_init64
- Explanation: dma_fence_init64 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000516 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_fence_timeline_name
- Explanation: dma_fence_timeline_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000518 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dpm_save_failed_dev
- Explanation: dpm_save_failed_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000519 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dpm_save_failed_step
- Explanation: dpm_save_failed_step changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000520 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_debugfs_bridge_params
- Explanation: drm_debugfs_bridge_params changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000521 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_debugfs_dev_init
- Explanation: drm_debugfs_dev_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'dev', 'type': '*mut drm_device'}, {'name': 'root', 'type': '*mut dentry'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'dev', 'type': '*mut drm_device'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000522 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_debugfs_init_root
- Explanation: drm_debugfs_init_root changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000523 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_debugfs_remove_root
- Explanation: drm_debugfs_remove_root changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000524 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_dev_wedged_event
- Explanation: drm_dev_wedged_event changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'dev', 'type': '*mut drm_device'}, {'name': 'method', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'dev', 'type': '*mut drm_device'}, {'name': 'method', 'type': 'ffi::c_ulong'}, {'name': 'info', 'type': '*mut drm_wedge_task_info'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000525 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_is_prime_exported_dma_buf
- Explanation: drm_gem_is_prime_exported_dma_buf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000526 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_lru_scan
- Explanation: drm_gem_lru_scan changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'lru', 'type': '*mut drm_gem_lru'}, {'name': 'nr_to_scan', 'type': 'ffi::c_uint'}, {'name': 'remaining', 'type': '*mut ffi::c_ulong'}, {'name': 'shrink', 'type': '::core::option::Option<unsafe extern "C" fn(obj: *mut drm_gem_object'}], 'return_type': 'bool_>, ) -> ffi::c_ulong'}`
- New: `{'params': [{'name': 'lru', 'type': '*mut drm_gem_lru'}, {'name': 'nr_to_scan', 'type': 'ffi::c_uint'}, {'name': 'remaining', 'type': '*mut ffi::c_ulong'}, {'name': 'shrink', 'type': '::core::option::Option< unsafe extern "C" fn(obj: *mut drm_gem_object, ticket: *mut ww_acquire_ctx'}], 'return_type': 'bool_, >, ticket: *mut ww_acquire_ctx, ) -> ffi::c_ulong'}`

### Rust Evidence

- Graph edges: `1`

## W-000527 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dsw_present
- Explanation: dsw_present changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000528 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dynamic_status
- Explanation: dynamic_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000529 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: early_acpi_boot_init
- Explanation: early_acpi_boot_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000530 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ec_get_handle
- Explanation: ec_get_handle changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000531 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ec_read
- Explanation: ec_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000532 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ec_transaction
- Explanation: ec_transaction changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000533 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ec_write
- Explanation: ec_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000534 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ejectable
- Explanation: ejectable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000535 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: enabled
- Explanation: enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000536 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: end_page_writeback
- Explanation: end_page_writeback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000537 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: enumeration_by_parent
- Explanation: enumeration_by_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000538 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: exit_swap_address_space
- Explanation: exit_swap_address_space changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000539 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: explicit_get
- Explanation: explicit_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000540 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: explicit_set
- Explanation: explicit_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000541 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: external_facing
- Explanation: external_facing changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(29usize, 1u8) as u32) } } #[inline] pub fn set_external_facing(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(30usize, 1u8) as u32) } } #[inline] pub fn set_external_facing(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000542 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fault_in_readable
- Explanation: fault_in_readable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000543 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fault_in_safe_writeable
- Explanation: fault_in_safe_writeable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000544 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fault_in_subpage_writeable
- Explanation: fault_in_subpage_writeable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000545 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fault_in_writeable
- Explanation: fault_in_writeable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000546 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fc_mount_longterm
- Explanation: fc_mount_longterm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000547 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_add_folio
- Explanation: filemap_add_folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000548 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_alloc_folio_noprof
- Explanation: filemap_alloc_folio_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000549 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_check_errors
- Explanation: filemap_check_errors changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000550 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_fdatawait_keep_errors
- Explanation: filemap_fdatawait_keep_errors changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000552 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_fdatawait_range_keep_errors
- Explanation: filemap_fdatawait_range_keep_errors changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000555 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_fdatawrite_wbc
- Explanation: filemap_fdatawrite_wbc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000556 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_flush
- Explanation: filemap_flush changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000557 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_get_entry
- Explanation: filemap_get_entry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000559 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_get_folios_contig
- Explanation: filemap_get_folios_contig changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000560 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_get_folios_tag
- Explanation: filemap_get_folios_tag changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000561 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_invalidate_inode
- Explanation: filemap_invalidate_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000562 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_invalidate_pages
- Explanation: filemap_invalidate_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000563 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_migrate_folio
- Explanation: filemap_migrate_folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000564 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_range_has_page
- Explanation: filemap_range_has_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000565 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_range_has_writeback
- Explanation: filemap_range_has_writeback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000566 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_release_folio
- Explanation: filemap_release_folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000567 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_remove_folio
- Explanation: filemap_remove_folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000568 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_write_and_wait_range
- Explanation: filemap_write_and_wait_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000569 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: find_first_swap
- Explanation: find_first_swap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000570 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: find_random_bit
- Explanation: find_random_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000571 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fix_pxm_node_maps
- Explanation: fix_pxm_node_maps changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000572 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_account_cleaned
- Explanation: folio_account_cleaned changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000574 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_add_lru_vma
- Explanation: folio_add_lru_vma changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000575 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_alloc_swap
- Explanation: folio_alloc_swap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000576 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_clear_dirty_for_io
- Explanation: folio_clear_dirty_for_io changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000577 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_deactivate
- Explanation: folio_deactivate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000578 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_end_private_2
- Explanation: folio_end_private_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000579 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_end_read
- Explanation: folio_end_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000580 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_end_writeback
- Explanation: folio_end_writeback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000581 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_free_swap
- Explanation: folio_free_swap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000582 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_invalidate
- Explanation: folio_invalidate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000584 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_mark_accessed
- Explanation: folio_mark_accessed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000585 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_mark_lazyfree
- Explanation: folio_mark_lazyfree changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000586 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_unlock
- Explanation: folio_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000588 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_wait_bit_killable
- Explanation: folio_wait_bit_killable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000590 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_wait_private_2_killable
- Explanation: folio_wait_private_2_killable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000591 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_wait_stable
- Explanation: folio_wait_stable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000593 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_wait_writeback_killable
- Explanation: folio_wait_writeback_killable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000595 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: for_sync
- Explanation: for_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(5usize, 1u8) as u32) } } #[inline] pub fn set_for_sync(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(4usize, 1u8) as u32) } } #[inline] pub fn set_for_sync(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000596 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_folio_and_swap_cache
- Explanation: free_folio_and_swap_cache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000597 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_pages_and_swap_cache
- Explanation: free_pages_and_swap_cache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000598 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_swap_and_cache_nr
- Explanation: free_swap_and_cache_nr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000599 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_swap_cache
- Explanation: free_swap_cache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000600 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: freeze_kernel_threads
- Explanation: freeze_kernel_threads changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000601 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: freeze_processes
- Explanation: freeze_processes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000602 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: freeze_task
- Explanation: freeze_task changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000603 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: freezing_slow_path
- Explanation: freezing_slow_path changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000604 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: frozen
- Explanation: frozen changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(38usize, 1u8) as u32) } } #[inline] pub fn set_frozen(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': 'p', 'type': '*mut task_struct'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000606 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: functional
- Explanation: functional changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000608 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_file_mmap_prepare
- Explanation: generic_file_mmap_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000609 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_file_readonly_mmap_prepare
- Explanation: generic_file_readonly_mmap_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000610 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_swapfile_activate
- Explanation: generic_swapfile_activate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000611 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_dev_from_fwnode
- Explanation: get_dev_from_fwnode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000612 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_pfnblock_bit
- Explanation: get_pfnblock_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000614 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_pfnblock_migratetype
- Explanation: get_pfnblock_migratetype changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000615 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_safe_page
- Explanation: get_safe_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000616 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_swap_device
- Explanation: get_swap_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000617 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_swap_page_of_type
- Explanation: get_swap_page_of_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000618 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hardware_id
- Explanation: hardware_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000619 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hash_pointers_finalize
- Explanation: hash_pointers_finalize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000621 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hibernate_quiet_exec
- Explanation: hibernate_quiet_exec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000622 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hibernate_resume_nonboot_cpu_disable
- Explanation: hibernate_resume_nonboot_cpu_disable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000623 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hibernation_available
- Explanation: hibernation_available changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000624 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hibernation_set_ops
- Explanation: hibernation_set_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000625 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: honor_deps
- Explanation: honor_deps changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000626 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hotplug_notify
- Explanation: hotplug_notify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000627 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ignore_parent
- Explanation: ignore_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000628 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: init_cpu_to_node
- Explanation: init_cpu_to_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000629 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: init_gi_nodes
- Explanation: init_gi_nodes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000630 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: init_swap_address_space
- Explanation: init_swap_address_space changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000631 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: initialized
- Explanation: initialized changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(0usize, 1u8) as u32) } } #[inline] pub fn set_initialized(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u32_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(5usize, 1u8) as u32) } } #[inline] pub fn set_initialized(&mut self, val: u32_) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000632 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inrush_current
- Explanation: inrush_current changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000633 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: interrupts
- Explanation: interrupts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(16usize, 1u8) as u32) } } #[inline] pub fn set_interrupts(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(17usize, 1u8) as u32) } } #[inline] pub fn set_interrupts(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000635 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: invalidate_inode_pages2_range
- Explanation: invalidate_inode_pages2_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000636 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: invalidate_mapping_pages
- Explanation: invalidate_mapping_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000637 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: io_window_1k
- Explanation: io_window_1k changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(31usize, 1u8) as u32) } } #[inline] pub fn set_io_window_1k(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(32usize, 1u8) as u32) } } #[inline] pub fn set_io_window_1k(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000639 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_managed
- Explanation: irq_managed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(32usize, 1u8) as u32) } } #[inline] pub fn set_irq_managed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(33usize, 1u8) as u32) } } #[inline] pub fn set_irq_managed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000640 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_rerun
- Explanation: irq_rerun changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(18usize, 1u8) as u32) } } #[inline] pub fn set_irq_rerun(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(19usize, 1u8) as u32) } } #[inline] pub fn set_irq_rerun(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000641 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_suspended
- Explanation: irq_suspended changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(17usize, 1u8) as u32) } } #[inline] pub fn set_irq_suspended(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(18usize, 1u8) as u32) } } #[inline] pub fn set_irq_suspended(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000642 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_acpi_data_node
- Explanation: is_acpi_data_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000643 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_acpi_device_node
- Explanation: is_acpi_device_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000644 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_dock_device
- Explanation: is_dock_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000645 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_dock_station
- Explanation: is_dock_station changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000646 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_genphy_driven
- Explanation: is_genphy_driven changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000647 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_hibernate_resume_dev
- Explanation: is_hibernate_resume_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000649 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_pciehp
- Explanation: is_pciehp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000650 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_probed
- Explanation: is_probed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(34usize, 1u8) as u32) } } #[inline] pub fn set_is_probed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(35usize, 1u8) as u32) } } #[inline] pub fn set_is_probed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000651 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_thunderbolt
- Explanation: is_thunderbolt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(27usize, 1u8) as u32) } } #[inline] pub fn set_is_thunderbolt(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(28usize, 1u8) as u32) } } #[inline] pub fn set_is_thunderbolt(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000652 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kiocb_invalidate_pages
- Explanation: kiocb_invalidate_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000653 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kiocb_invalidate_post_direct_write
- Explanation: kiocb_invalidate_post_direct_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000654 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kiocb_write_and_wait
- Explanation: kiocb_write_and_wait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000655 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kswapd_run
- Explanation: kswapd_run changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000656 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kswapd_stop
- Explanation: kswapd_stop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000659 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ktime_get_clock_ts64
- Explanation: ktime_get_clock_ts64 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000664 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_attach_mm
- Explanation: kunit_attach_mm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000666 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: link_active_reporting
- Explanation: link_active_reporting changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(35usize, 1u8) as u32) } } #[inline] pub fn set_link_active_reporting(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(36usize, 1u8) as u32) } } #[inline] pub fn set_link_active_reporting(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000667 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lock_next_vma
- Explanation: lock_next_vma changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000668 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lock_system_sleep
- Explanation: lock_system_sleep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000669 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: locked_recursive_removal
- Explanation: locked_recursive_removal changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000672 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lru_add_drain_all
- Explanation: lru_add_drain_all changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000674 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lru_add_drain_cpu_zone
- Explanation: lru_add_drain_cpu_zone changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000675 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lru_cache_disable
- Explanation: lru_cache_disable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000676 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lru_note_cost_refault
- Explanation: lru_note_cost_refault changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000677 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lru_note_cost_unlock_irq
- Explanation: lru_note_cost_unlock_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000678 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mapping_read_folio_gfp
- Explanation: mapping_read_folio_gfp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000679 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mapping_seek_hole_data
- Explanation: mapping_seek_hole_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000680 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mark_page_accessed
- Explanation: mark_page_accessed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000681 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: match_driver
- Explanation: match_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000683 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mem_cgroup_shrink_node
- Explanation: mem_cgroup_shrink_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000686 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mprotect_fixup
- Explanation: mprotect_fixup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'vmi', 'type': '*mut vma_iterator'}, {'name': 'tlb', 'type': '*mut mmu_gather'}, {'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'pprev', 'type': '*mut *mut vm_area_struct'}, {'name': 'start', 'type': 'ffi::c_ulong'}, {'name': 'end', 'type': 'ffi::c_ulong'}, {'name': 'newflags', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'vmi', 'type': '*mut vma_iterator'}, {'name': 'tlb', 'type': '*mut mmu_gather'}, {'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'pprev', 'type': '*mut *mut vm_area_struct'}, {'name': 'start', 'type': 'ffi::c_ulong'}, {'name': 'end', 'type': 'ffi::c_ulong'}, {'name': 'newflags', 'type': 'vm_flags_t'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000687 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_bitfield_1
- Explanation: new_bitfield_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'is_c45', 'type': 'ffi::c_uint'}, {'name': 'is_internal', 'type': 'ffi::c_uint'}, {'name': 'is_pseudo_fixed_link', 'type': 'ffi::c_uint'}, {'name': 'is_gigabit_capable', 'type': 'ffi::c_uint'}, {'name': 'has_fixups', 'type': 'ffi::c_uint'}, {'name': 'suspended', 'type': 'ffi::c_uint'}, {'name': 'suspended_by_mdio_bus', 'type': 'ffi::c_uint'}, {'name': 'sysfs_links', 'type': 'ffi::c_uint'}, {'name': 'loopback_enabled', 'type': 'ffi::c_uint'}, {'name': 'downshifted_rate', 'type': 'ffi::c_uint'}, {'name': 'is_on_sfp_module', 'type': 'ffi::c_uint'}, {'name': 'mac_managed_pm', 'type': 'ffi::c_uint'}, {'name': 'wol_enabled', 'type': 'ffi::c_uint'}, {'name': 'autoneg', 'type': 'ffi::c_uint'}, {'name': 'link', 'type': 'ffi::c_uint'}, {'name': 'autoneg_complete', 'type': 'ffi::c_uint'}, {'name': 'interrupts', 'type': 'ffi::c_uint'}, {'name': 'irq_suspended', 'type': 'ffi::c_uint'}, {'name': 'irq_rerun', 'type': 'ffi::c_uint'}, {'name': 'default_timestamp', 'type': 'ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`
- New: `{'params': [{'name': 'is_c45', 'type': 'ffi::c_uint'}, {'name': 'is_internal', 'type': 'ffi::c_uint'}, {'name': 'is_pseudo_fixed_link', 'type': 'ffi::c_uint'}, {'name': 'is_gigabit_capable', 'type': 'ffi::c_uint'}, {'name': 'has_fixups', 'type': 'ffi::c_uint'}, {'name': 'suspended', 'type': 'ffi::c_uint'}, {'name': 'suspended_by_mdio_bus', 'type': 'ffi::c_uint'}, {'name': 'sysfs_links', 'type': 'ffi::c_uint'}, {'name': 'loopback_enabled', 'type': 'ffi::c_uint'}, {'name': 'downshifted_rate', 'type': 'ffi::c_uint'}, {'name': 'is_on_sfp_module', 'type': 'ffi::c_uint'}, {'name': 'mac_managed_pm', 'type': 'ffi::c_uint'}, {'name': 'wol_enabled', 'type': 'ffi::c_uint'}, {'name': 'is_genphy_driven', 'type': 'ffi::c_uint'}, {'name': 'autoneg', 'type': 'ffi::c_uint'}, {'name': 'link', 'type': 'ffi::c_uint'}, {'name': 'autoneg_complete', 'type': 'ffi::c_uint'}, {'name': 'interrupts', 'type': 'ffi::c_uint'}, {'name': 'irq_suspended', 'type': 'ffi::c_uint'}, {'name': 'irq_rerun', 'type': 'ffi::c_uint'}, {'name': 'default_timestamp', 'type': 'ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`

### Rust Evidence

- Graph edges: `1`

## W-000688 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_bitfield_4
- Explanation: new_bitfield_4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'transparent', 'type': 'ffi::c_uint'}, {'name': 'io_window', 'type': 'ffi::c_uint'}, {'name': 'pref_window', 'type': 'ffi::c_uint'}, {'name': 'pref_64_window', 'type': 'ffi::c_uint'}, {'name': 'multifunction', 'type': 'ffi::c_uint'}, {'name': 'is_busmaster', 'type': 'ffi::c_uint'}, {'name': 'no_msi', 'type': 'ffi::c_uint'}, {'name': 'no_64bit_msi', 'type': 'ffi::c_uint'}, {'name': 'block_cfg_access', 'type': 'ffi::c_uint'}, {'name': 'broken_parity_status', 'type': 'ffi::c_uint'}, {'name': 'irq_reroute_variant', 'type': 'ffi::c_uint'}, {'name': 'msi_enabled', 'type': 'ffi::c_uint'}, {'name': 'msix_enabled', 'type': 'ffi::c_uint'}, {'name': 'ari_enabled', 'type': 'ffi::c_uint'}, {'name': 'ats_enabled', 'type': 'ffi::c_uint'}, {'name': 'pasid_enabled', 'type': 'ffi::c_uint'}, {'name': 'pri_enabled', 'type': 'ffi::c_uint'}, {'name': 'tph_enabled', 'type': 'ffi::c_uint'}, {'name': 'is_managed', 'type': 'ffi::c_uint'}, {'name': 'is_msi_managed', 'type': 'ffi::c_uint'}, {'name': 'needs_freset', 'type': 'ffi::c_uint'}, {'name': 'state_saved', 'type': 'ffi::c_uint'}, {'name': 'is_physfn', 'type': 'ffi::c_uint'}, {'name': 'is_virtfn', 'type': 'ffi::c_uint'}, {'name': 'is_hotplug_bridge', 'type': 'ffi::c_uint'}, {'name': 'shpc_managed', 'type': 'ffi::c_uint'}, {'name': 'is_thunderbolt', 'type': 'ffi::c_uint'}, {'name': 'untrusted', 'type': 'ffi::c_uint'}, {'name': 'external_facing', 'type': 'ffi::c_uint'}, {'name': 'broken_intx_masking', 'type': 'ffi::c_uint'}, {'name': 'io_window_1k', 'type': 'ffi::c_uint'}, {'name': 'irq_managed', 'type': 'ffi::c_uint'}, {'name': 'non_compliant_bars', 'type': 'ffi::c_uint'}, {'name': 'is_probed', 'type': 'ffi::c_uint'}, {'name': 'link_active_reporting', 'type': 'ffi::c_uint'}, {'name': 'no_vf_scan', 'type': 'ffi::c_uint'}, {'name': 'no_command_memory', 'type': 'ffi::c_uint'}, {'name': 'rom_bar_overlap', 'type': 'ffi::c_uint'}, {'name': 'rom_attr_enabled', 'type': 'ffi::c_uint'}, {'name': 'non_mappable_bars', 'type': 'ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`
- New: `{'params': [{'name': 'transparent', 'type': 'ffi::c_uint'}, {'name': 'io_window', 'type': 'ffi::c_uint'}, {'name': 'pref_window', 'type': 'ffi::c_uint'}, {'name': 'pref_64_window', 'type': 'ffi::c_uint'}, {'name': 'multifunction', 'type': 'ffi::c_uint'}, {'name': 'is_busmaster', 'type': 'ffi::c_uint'}, {'name': 'no_msi', 'type': 'ffi::c_uint'}, {'name': 'no_64bit_msi', 'type': 'ffi::c_uint'}, {'name': 'block_cfg_access', 'type': 'ffi::c_uint'}, {'name': 'broken_parity_status', 'type': 'ffi::c_uint'}, {'name': 'irq_reroute_variant', 'type': 'ffi::c_uint'}, {'name': 'msi_enabled', 'type': 'ffi::c_uint'}, {'name': 'msix_enabled', 'type': 'ffi::c_uint'}, {'name': 'ari_enabled', 'type': 'ffi::c_uint'}, {'name': 'ats_enabled', 'type': 'ffi::c_uint'}, {'name': 'pasid_enabled', 'type': 'ffi::c_uint'}, {'name': 'pri_enabled', 'type': 'ffi::c_uint'}, {'name': 'tph_enabled', 'type': 'ffi::c_uint'}, {'name': 'is_managed', 'type': 'ffi::c_uint'}, {'name': 'is_msi_managed', 'type': 'ffi::c_uint'}, {'name': 'needs_freset', 'type': 'ffi::c_uint'}, {'name': 'state_saved', 'type': 'ffi::c_uint'}, {'name': 'is_physfn', 'type': 'ffi::c_uint'}, {'name': 'is_virtfn', 'type': 'ffi::c_uint'}, {'name': 'is_hotplug_bridge', 'type': 'ffi::c_uint'}, {'name': 'is_pciehp', 'type': 'ffi::c_uint'}, {'name': 'shpc_managed', 'type': 'ffi::c_uint'}, {'name': 'is_thunderbolt', 'type': 'ffi::c_uint'}, {'name': 'untrusted', 'type': 'ffi::c_uint'}, {'name': 'external_facing', 'type': 'ffi::c_uint'}, {'name': 'broken_intx_masking', 'type': 'ffi::c_uint'}, {'name': 'io_window_1k', 'type': 'ffi::c_uint'}, {'name': 'irq_managed', 'type': 'ffi::c_uint'}, {'name': 'non_compliant_bars', 'type': 'ffi::c_uint'}, {'name': 'is_probed', 'type': 'ffi::c_uint'}, {'name': 'link_active_reporting', 'type': 'ffi::c_uint'}, {'name': 'no_vf_scan', 'type': 'ffi::c_uint'}, {'name': 'no_command_memory', 'type': 'ffi::c_uint'}, {'name': 'rom_bar_overlap', 'type': 'ffi::c_uint'}, {'name': 'rom_attr_enabled', 'type': 'ffi::c_uint'}, {'name': 'non_mappable_bars', 'type': 'ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`

### Rust Evidence

- Graph edges: `1`

## W-000689 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_cgroup_owner
- Explanation: no_cgroup_owner changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(7usize, 1u8) as u32) } } #[inline] pub fn set_no_cgroup_owner(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(6usize, 1u8) as u32) } } #[inline] pub fn set_no_cgroup_owner(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000690 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_command_memory
- Explanation: no_command_memory changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(37usize, 1u8) as u32) } } #[inline] pub fn set_no_command_memory(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(38usize, 1u8) as u32) } } #[inline] pub fn set_no_command_memory(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000692 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_vf_scan
- Explanation: no_vf_scan changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(36usize, 1u8) as u32) } } #[inline] pub fn set_no_vf_scan(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(37usize, 1u8) as u32) } } #[inline] pub fn set_no_vf_scan(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000693 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: node_to_pxm
- Explanation: node_to_pxm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000694 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: non_compliant_bars
- Explanation: non_compliant_bars changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(33usize, 1u8) as u32) } } #[inline] pub fn set_non_compliant_bars(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(34usize, 1u8) as u32) } } #[inline] pub fn set_non_compliant_bars(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000695 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: non_mappable_bars
- Explanation: non_mappable_bars changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(40usize, 1u8) as u32) } } #[inline] pub fn set_non_mappable_bars(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(41usize, 1u8) as u32) } } #[inline] pub fn set_non_mappable_bars(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000696 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: noop_dirty_folio
- Explanation: noop_dirty_folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000697 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: notifier_present
- Explanation: notifier_present changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000698 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: numa_add_cpu
- Explanation: numa_add_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000699 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: numa_clear_node
- Explanation: numa_clear_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000700 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: numa_cpu_node
- Explanation: numa_cpu_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000701 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: numa_remove_cpu
- Explanation: numa_remove_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000702 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: numa_set_node
- Explanation: numa_set_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000703 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: of_compatible_ok
- Explanation: of_compatible_ok changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000705 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: page_cache_async_ra
- Explanation: page_cache_async_ra changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000706 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: page_cache_next_miss
- Explanation: page_cache_next_miss changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000707 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: page_cache_prev_miss
- Explanation: page_cache_prev_miss changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000708 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: page_cache_ra_unbounded
- Explanation: page_cache_ra_unbounded changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000709 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: page_cache_sync_ra
- Explanation: page_cache_sync_ra changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000710 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pagecache_get_page
- Explanation: pagecache_get_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000711 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_acpi_crs_quirks
- Explanation: pci_acpi_crs_quirks changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000712 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_acpi_scan_root
- Explanation: pci_acpi_scan_root changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000715 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pfn_is_nosave
- Explanation: pfn_is_nosave changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000718 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_get_internal_delay
- Explanation: phy_get_internal_delay changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'dev', 'type': '*mut device'}, {'name': 'delay_values', 'type': '*const ffi::c_int'}, {'name': 'size', 'type': 'ffi::c_int'}, {'name': 'is_rx', 'type': 'bool_'}], 'return_type': 's32'}`
- New: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'delay_values', 'type': '*const ffi::c_int'}, {'name': 'size', 'type': 'ffi::c_int'}, {'name': 'is_rx', 'type': 'bool_'}], 'return_type': 's32'}`

### Rust Evidence

- Graph edges: `1`

## W-000720 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_id
- Explanation: platform_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000722 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_debug_messages_should_print
- Explanation: pm_debug_messages_should_print changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000723 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_get_wakeup_count
- Explanation: pm_get_wakeup_count changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000724 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_hibernate_is_recovering
- Explanation: pm_hibernate_is_recovering changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000725 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_prepare_console
- Explanation: pm_prepare_console changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000726 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_print_active_wakeup_sources
- Explanation: pm_print_active_wakeup_sources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000727 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_report_hw_sleep_time
- Explanation: pm_report_hw_sleep_time changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000728 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_report_max_hw_sleep
- Explanation: pm_report_max_hw_sleep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000729 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_restore_console
- Explanation: pm_restore_console changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000730 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_restore_gfp_mask
- Explanation: pm_restore_gfp_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000731 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_restrict_gfp_mask
- Explanation: pm_restrict_gfp_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000732 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_save_wakeup_count
- Explanation: pm_save_wakeup_count changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000733 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_set_vt_switch
- Explanation: pm_set_vt_switch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000734 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_sleep_transition_in_progress
- Explanation: pm_sleep_transition_in_progress changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000735 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_states_init
- Explanation: pm_states_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000737 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_suspend_default_s2idle
- Explanation: pm_suspend_default_s2idle changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000738 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_system_cancel_wakeup
- Explanation: pm_system_cancel_wakeup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000739 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_system_irq_wakeup
- Explanation: pm_system_irq_wakeup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000740 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_system_wakeup
- Explanation: pm_system_wakeup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000741 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_wakep_autosleep_enabled
- Explanation: pm_wakep_autosleep_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000742 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_wakeup_clear
- Explanation: pm_wakeup_clear changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000743 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_wakeup_irq
- Explanation: pm_wakeup_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000744 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_wakeup_pending
- Explanation: pm_wakeup_pending changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000746 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: power_manageable
- Explanation: power_manageable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000747 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: power_removed
- Explanation: power_removed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000748 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: power_resources
- Explanation: power_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000749 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: present
- Explanation: present changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000750 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: put_online
- Explanation: put_online changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000751 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: put_swap_folio
- Explanation: put_swap_folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000752 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pxm_to_node
- Explanation: pxm_to_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000753 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: range_cyclic
- Explanation: range_cyclic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(4usize, 1u8) as u32) } } #[inline] pub fn set_range_cyclic(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(3usize, 1u8) as u32) } } #[inline] pub fn set_range_cyclic(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000754 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: read_cache_folio
- Explanation: read_cache_folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000756 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: read_cache_page_gfp
- Explanation: read_cache_page_gfp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000757 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: readahead_expand
- Explanation: readahead_expand changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000758 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: reclaim_register_node
- Explanation: reclaim_register_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000759 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: reclaim_unregister_node
- Explanation: reclaim_unregister_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000760 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: register_acpi_bus_type
- Explanation: register_acpi_bus_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000761 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: register_acpi_notifier
- Explanation: register_acpi_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000762 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: register_nosave_region
- Explanation: register_nosave_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000763 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: register_one_node
- Explanation: register_one_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000764 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: register_pm_notifier
- Explanation: register_pm_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000774 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: removable
- Explanation: removable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000775 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: remove_mapping
- Explanation: remove_mapping changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000776 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: replace_page_cache_folio
- Explanation: replace_page_cache_folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000777 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: request_mem_region
- Explanation: request_mem_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000778 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: request_muxed_region
- Explanation: request_muxed_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000779 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: request_region
- Explanation: request_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000782 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: restore_processor_state
- Explanation: restore_processor_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000783 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rom_attr_enabled
- Explanation: rom_attr_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(39usize, 1u8) as u32) } } #[inline] pub fn set_rom_attr_enabled(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(40usize, 1u8) as u32) } } #[inline] pub fn set_rom_attr_enabled(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000784 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rom_bar_overlap
- Explanation: rom_bar_overlap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(38usize, 1u8) as u32) } } #[inline] pub fn set_rom_bar_overlap(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(39usize, 1u8) as u32) } } #[inline] pub fn set_rom_bar_overlap(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000785 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rxfh_per_ctx_fields
- Explanation: rxfh_per_ctx_fields changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000786 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: s2idle_set_ops
- Explanation: s2idle_set_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000787 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: s2idle_wake
- Explanation: s2idle_wake changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000788 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: save_processor_state
- Explanation: save_processor_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000790 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_file_getattr
- Explanation: security_inode_file_getattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000791 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_file_setattr
- Explanation: security_inode_file_setattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000792 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_default_d_op
- Explanation: set_default_d_op changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000793 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_freezable
- Explanation: set_freezable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000794 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_pfnblock_bit
- Explanation: set_pfnblock_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000796 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: show_in_ui
- Explanation: show_in_ui changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000797 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: shpc_managed
- Explanation: shpc_managed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(26usize, 1u8) as u32) } } #[inline] pub fn set_shpc_managed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(27usize, 1u8) as u32) } } #[inline] pub fn set_shpc_managed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000798 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: shrink_all_memory
- Explanation: shrink_all_memory changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000799 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: si_swapinfo
- Explanation: si_swapinfo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000800 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_start_creating
- Explanation: simple_start_creating changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000801 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_write_begin
- Explanation: simple_write_begin changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'file', 'type': '*mut file'}, {'name': 'mapping', 'type': '*mut address_space'}, {'name': 'pos', 'type': 'loff_t'}, {'name': 'len', 'type': 'ffi::c_uint'}, {'name': 'foliop', 'type': '*mut *mut folio'}, {'name': 'fsdata', 'type': '*mut *mut ffi::c_void'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'iocb', 'type': '*const kiocb'}, {'name': 'mapping', 'type': '*mut address_space'}, {'name': 'pos', 'type': 'loff_t'}, {'name': 'len', 'type': 'ffi::c_uint'}, {'name': 'foliop', 'type': '*mut *mut folio'}, {'name': 'fsdata', 'type': '*mut *mut ffi::c_void'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000802 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_copy_datagram_from_iter_full
- Explanation: skb_copy_datagram_from_iter_full changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000803 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_splice_from_iter
- Explanation: skb_splice_from_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'iter', 'type': '*mut iov_iter'}, {'name': 'maxsize', 'type': 'isize'}, {'name': 'gfp', 'type': 'gfp_t'}], 'return_type': 'isize'}`
- New: `{'params': [{'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'iter', 'type': '*mut iov_iter'}, {'name': 'maxsize', 'type': 'isize'}], 'return_type': 'isize'}`

### Rust Evidence

- Graph edges: `1`

## W-000804 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: snapshot_page
- Explanation: snapshot_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000805 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: srat_disabled
- Explanation: srat_disabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000806 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: strict_midlayer
- Explanation: strict_midlayer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000807 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: suspend_set_ops
- Explanation: suspend_set_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000808 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: suspend_valid_only_mem
- Explanation: suspend_valid_only_mem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000809 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: swap_duplicate
- Explanation: swap_duplicate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000810 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: swap_entry_swapped
- Explanation: swap_entry_swapped changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000811 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: swap_folio_sector
- Explanation: swap_folio_sector changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000812 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: swap_free_nr
- Explanation: swap_free_nr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000813 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: swap_setup
- Explanation: swap_setup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000814 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: swap_shmem_alloc
- Explanation: swap_shmem_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000815 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: swap_type_of
- Explanation: swap_type_of changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000816 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: swapcache_prepare
- Explanation: swapcache_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000817 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: swapdev_block
- Explanation: swapdev_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000818 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: swp_swap_info
- Explanation: swp_swap_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000819 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: swp_swapcount
- Explanation: swp_swapcount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000820 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: swsusp_arch_resume
- Explanation: swsusp_arch_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000821 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: swsusp_arch_suspend
- Explanation: swsusp_arch_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000822 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: swsusp_page_is_forbidden
- Explanation: swsusp_page_is_forbidden changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000823 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: swsusp_save
- Explanation: swsusp_save changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000824 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: swsusp_set_page_free
- Explanation: swsusp_set_page_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000825 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: swsusp_unset_page_free
- Explanation: swsusp_unset_page_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000827 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: system_entering_hibernation
- Explanation: system_entering_hibernation changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000828 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: thaw_kernel_threads
- Explanation: thaw_kernel_threads changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000829 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: thaw_processes
- Explanation: thaw_processes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000830 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: thermal_acpi_active_trip_temp
- Explanation: thermal_acpi_active_trip_temp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000831 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: thermal_acpi_critical_trip_temp
- Explanation: thermal_acpi_critical_trip_temp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000832 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: thermal_acpi_hot_trip_temp
- Explanation: thermal_acpi_hot_trip_temp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000833 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: thermal_acpi_passive_trip_temp
- Explanation: thermal_acpi_passive_trip_temp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000834 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: topology_get_primary_thread
- Explanation: topology_get_primary_thread changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000835 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: try_to_free_mem_cgroup_pages
- Explanation: try_to_free_mem_cgroup_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000836 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: try_to_free_pages
- Explanation: try_to_free_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000837 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unlock_page
- Explanation: unlock_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000838 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unlock_system_sleep
- Explanation: unlock_system_sleep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000839 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unpinned_netfs_wb
- Explanation: unpinned_netfs_wb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(6usize, 1u8) as u32) } } #[inline] pub fn set_unpinned_netfs_wb(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(5usize, 1u8) as u32) } } #[inline] pub fn set_unpinned_netfs_wb(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000840 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unregister_acpi_bus_type
- Explanation: unregister_acpi_bus_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000841 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unregister_acpi_notifier
- Explanation: unregister_acpi_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000842 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unregister_pm_notifier
- Explanation: unregister_pm_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000843 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: untrusted
- Explanation: untrusted changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(28usize, 1u8) as u32) } } #[inline] pub fn set_untrusted(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(29usize, 1u8) as u32) } } #[inline] pub fn set_untrusted(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000845 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: visited
- Explanation: visited changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000846 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_get_page_prot
- Explanation: vm_get_page_prot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'vm_flags', 'type': 'ffi::c_ulong'}], 'return_type': 'pgprot_t'}`
- New: `{'params': [{'name': 'vm_flags', 'type': 'vm_flags_t'}], 'return_type': 'pgprot_t'}`

### Rust Evidence

- Graph edges: `1`

## W-000848 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmf_insert_mixed_mkwrite
- Explanation: vmf_insert_mixed_mkwrite changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'addr', 'type': 'ffi::c_ulong'}, {'name': 'pfn', 'type': 'pfn_t'}], 'return_type': 'vm_fault_t'}`
- New: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'addr', 'type': 'ffi::c_ulong'}, {'name': 'pfn', 'type': 'ffi::c_ulong'}], 'return_type': 'vm_fault_t'}`

### Rust Evidence

- Graph edges: `1`

## W-000849 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmf_insert_pfn_pmd
- Explanation: vmf_insert_pfn_pmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'vmf', 'type': '*mut vm_fault'}, {'name': 'pfn', 'type': 'pfn_t'}, {'name': 'write', 'type': 'bool_'}], 'return_type': 'vm_fault_t'}`
- New: `{'params': [{'name': 'vmf', 'type': '*mut vm_fault'}, {'name': 'pfn', 'type': 'ffi::c_ulong'}, {'name': 'write', 'type': 'bool_'}], 'return_type': 'vm_fault_t'}`

### Rust Evidence

- Graph edges: `1`

## W-000850 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmf_insert_pfn_pud
- Explanation: vmf_insert_pfn_pud changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'vmf', 'type': '*mut vm_fault'}, {'name': 'pfn', 'type': 'pfn_t'}, {'name': 'write', 'type': 'bool_'}], 'return_type': 'vm_fault_t'}`
- New: `{'params': [{'name': 'vmf', 'type': '*mut vm_fault'}, {'name': 'pfn', 'type': 'ffi::c_ulong'}, {'name': 'write', 'type': 'bool_'}], 'return_type': 'vm_fault_t'}`

### Rust Evidence

- Graph edges: `1`

## W-000851 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vpanic
- Explanation: vpanic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000852 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vprintk_deferred
- Explanation: vprintk_deferred changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000853 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wait_on_page_writeback
- Explanation: wait_on_page_writeback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000854 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wbinvd_on_all_cpus
- Explanation: wbinvd_on_all_cpus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'ffi::c_int'}`
- New: `{'params': [], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000855 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wbinvd_on_cpus_mask
- Explanation: wbinvd_on_cpus_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000856 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wbnoinvd_on_all_cpus
- Explanation: wbnoinvd_on_all_cpus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000857 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wbnoinvd_on_cpus_mask
- Explanation: wbnoinvd_on_cpus_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000858 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wmi_evaluate_method
- Explanation: wmi_evaluate_method changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000859 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wmi_get_acpi_device_uid
- Explanation: wmi_get_acpi_device_uid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000860 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wmi_has_guid
- Explanation: wmi_has_guid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000861 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wmi_install_notify_handler
- Explanation: wmi_install_notify_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000862 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wmi_instance_count
- Explanation: wmi_instance_count changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000863 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wmi_query_block
- Explanation: wmi_query_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000864 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wmi_remove_notify_handler
- Explanation: wmi_remove_notify_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000865 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wmi_set_block
- Explanation: wmi_set_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000867 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: workingset_activation
- Explanation: workingset_activation changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000868 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: workingset_age_nonresident
- Explanation: workingset_age_nonresident changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000869 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: workingset_eviction
- Explanation: workingset_eviction changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000870 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: workingset_refault
- Explanation: workingset_refault changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000871 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: workingset_test_recent
- Explanation: workingset_test_recent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000872 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: write_inode_now
- Explanation: write_inode_now changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000873 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: x86_acpi_numa_init
- Explanation: x86_acpi_numa_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000874 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: x86_default_get_root_pointer
- Explanation: x86_default_get_root_pointer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000875 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: x86_default_set_root_pointer
- Explanation: x86_default_set_root_pointer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000876 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xen_alloc_ballooned_pages
- Explanation: xen_alloc_ballooned_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000877 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xen_arch_register_cpu
- Explanation: xen_arch_register_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000878 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xen_arch_unregister_cpu
- Explanation: xen_arch_unregister_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000879 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xen_biovec_phys_mergeable
- Explanation: xen_biovec_phys_mergeable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000880 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xen_free_ballooned_pages
- Explanation: xen_free_ballooned_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000881 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xen_get_lazy_mode
- Explanation: xen_get_lazy_mode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000882 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xen_prepare_pvh
- Explanation: xen_prepare_pvh changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000883 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xen_pv_evtchn_do_upcall
- Explanation: xen_pv_evtchn_do_upcall changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000884 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: zone_reclaimable_pages
- Explanation: zone_reclaimable_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001156 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_check_dsm
- Explanation: acpi_check_dsm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['acpi_handle handle', 'const guid_t *guid', 'u64 rev', 'u64 funcs'], 'return_type': 'bool'}`
- New: `{'params': ['acpi_handle handle', 'const guid_t *guid', 'u64 rev', 'u64 funcs'], 'return_type': 'static inline bool'}`

### Rust Evidence

- Graph edges: `1`

## W-001157 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_found
- Explanation: acpi_dev_found changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const char *hid'], 'return_type': 'bool'}`
- New: `{'params': ['const char *hid'], 'return_type': 'static inline bool'}`

### Rust Evidence

- Graph edges: `1`

## W-001159 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dev_present
- Explanation: acpi_dev_present changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const char *hid', 'const char *uid', 's64 hrv'], 'return_type': 'bool'}`
- New: `{'params': ['const char *hid', 'const char *uid', 's64 hrv'], 'return_type': 'static inline bool'}`

### Rust Evidence

- Graph edges: `1`

## W-001161 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dma_configure_id
- Explanation: acpi_dma_configure_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['dev', 'attr', 'NULL'], 'return_type': 'return'}`
- New: `{'params': ['struct device *dev', 'enum dev_dma_attr attr', 'const u32 *input_id'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `1`

## W-001163 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_dma_supported
- Explanation: acpi_dma_supported changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct acpi_device *adev'], 'return_type': 'bool'}`
- New: `{'params': ['const struct acpi_device *adev'], 'return_type': 'static inline bool'}`

### Rust Evidence

- Graph edges: `1`

## W-001165 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_dma_attr
- Explanation: acpi_get_dma_attr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct acpi_device *adev'], 'return_type': 'enum dev_dma_attr'}`
- New: `{'params': ['struct acpi_device *adev'], 'return_type': 'static inline enum dev_dma_attr'}`

### Rust Evidence

- Graph edges: `1`

## W-001166 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_map_pxm_to_node
- Explanation: acpi_map_pxm_to_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['int'], 'return_type': 'extern int'}`
- New: `{'params': ['int pxm'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `1`

## W-001167 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_reduced_hardware
- Explanation: acpi_reduced_hardware changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'bool'}`
- New: `{'params': [], 'return_type': 'static inline bool'}`

### Rust Evidence

- Graph edges: `1`

## W-001170 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dl_task_check_affinity
- Explanation: dl_task_check_affinity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct task_struct *p', 'const struct cpumask *mask'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct task_struct *p', 'const struct cpumask *mask'], 'return_type': 'extern int'}`

### Rust Evidence

- Graph edges: `1`

## W-001171 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_set_cpus_allowed
- Explanation: do_set_cpus_allowed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct task_struct *p', 'const struct cpumask *new_mask'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct task_struct *p', 'const struct cpumask *new_mask'], 'return_type': 'extern void'}`

### Rust Evidence

- Graph edges: `1`

## W-001174 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_debugfs_dev_init
- Explanation: drm_debugfs_dev_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_device *dev', 'struct dentry *root'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct drm_device *dev'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `1`

## W-001175 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_dev_wedged_event
- Explanation: drm_dev_wedged_event changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_device *dev', 'unsigned long method'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_device *dev', 'unsigned long method', 'struct drm_wedge_task_info *info'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-001185 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_lru_scan
- Explanation: drm_gem_lru_scan changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_gem_lru *lru', 'unsigned int nr_to_scan', 'unsigned long *remaining', 'bool (*shrink)(struct drm_gem_object *obj)'], 'return_type': 'unsigned long'}`
- New: `{'params': ['struct drm_gem_lru *lru', 'unsigned int nr_to_scan', 'unsigned long *remaining', 'bool (*shrink)(struct drm_gem_object *obj, struct ww_acquire_ctx *ticket)', 'struct ww_acquire_ctx *ticket'], 'return_type': 'unsigned long'}`

### Rust Evidence

- Graph edges: `1`

## W-001189 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dup_user_cpus_ptr
- Explanation: dup_user_cpus_ptr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct task_struct *dst', 'struct task_struct *src', 'int node'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct task_struct *dst', 'struct task_struct *src', 'int node'], 'return_type': 'extern int'}`

### Rust Evidence

- Graph edges: `1`

## W-001194 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_acpi_data_node
- Explanation: is_acpi_data_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct fwnode_handle *fwnode'], 'return_type': 'bool'}`
- New: `{'params': ['const struct fwnode_handle *fwnode'], 'return_type': 'static inline bool'}`

### Rust Evidence

- Graph edges: `1`

## W-001195 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_acpi_device_node
- Explanation: is_acpi_device_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct fwnode_handle *fwnode'], 'return_type': 'bool'}`
- New: `{'params': ['const struct fwnode_handle *fwnode'], 'return_type': 'static inline bool'}`

### Rust Evidence

- Graph edges: `1`

## W-001196 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kick_process
- Explanation: kick_process changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct task_struct *tsk'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct task_struct *tsk'], 'return_type': 'extern void'}`

### Rust Evidence

- Graph edges: `1`

## W-001198 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_get_internal_delay
- Explanation: phy_get_internal_delay changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct phy_device *phydev', 'struct device *dev', 'const int *delay_values', 'int size', 'bool is_rx'], 'return_type': 's32'}`
- New: `{'params': ['struct phy_device *phydev', 'const int *delay_values', 'int size', 'bool is_rx'], 'return_type': 's32'}`

### Rust Evidence

- Graph edges: `1`

## W-001199 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: release_user_cpus_ptr
- Explanation: release_user_cpus_ptr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct task_struct *p'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct task_struct *p'], 'return_type': 'extern void'}`

### Rust Evidence

- Graph edges: `1`

## W-001200 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sched_domains_mutex_lock
- Explanation: sched_domains_mutex_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'static inline void'}`
- New: `{'params': [], 'return_type': 'extern void'}`

### Rust Evidence

- Graph edges: `1`

## W-001201 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sched_domains_mutex_unlock
- Explanation: sched_domains_mutex_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'static inline void'}`
- New: `{'params': [], 'return_type': 'extern void'}`

### Rust Evidence

- Graph edges: `1`

## W-001203 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_cpus_allowed_ptr
- Explanation: set_cpus_allowed_ptr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct task_struct *p', 'const struct cpumask *new_mask'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct task_struct *p', 'const struct cpumask *new_mask'], 'return_type': 'extern int'}`

### Rust Evidence

- Graph edges: `1`

## W-001210 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_write_begin
- Explanation: simple_write_begin changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct file *file', 'struct address_space *mapping', 'loff_t pos', 'unsigned len', 'struct folio **foliop', 'void **fsdata'], 'return_type': 'extern int'}`
- New: `{'params': ['const struct kiocb *iocb', 'struct address_space *mapping', 'loff_t pos', 'unsigned len', 'struct folio **foliop', 'void **fsdata'], 'return_type': 'extern int'}`

### Rust Evidence

- Graph edges: `1`

## W-000888 FieldDrift

- Risk: High
- Score: 10.6
- Symbol: bpf_link_info__bindgen_ty_1__bindgen_ty_1
- Explanation: bpf_link_info__bindgen_ty_1__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'tp_name', 'type': '__u64'}, {'name': 'tp_name_len', 'type': '__u32'}]`
- New: `[{'name': 'tp_name', 'type': '__u64'}, {'name': 'tp_name_len', 'type': '__u32'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': 'cookie', 'type': '__u64'}]`

### Rust Evidence

- Graph edges: `10`

## W-001187 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: drm_helper_mode_fill_fb_struct
- Explanation: drm_helper_mode_fill_fb_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_device *dev', 'struct drm_framebuffer *fb', 'const struct drm_mode_fb_cmd2 *mode_cmd'], 'return_type': 'void'}`
- New: `{'params': ['struct drm_device *dev', 'struct drm_framebuffer *fb', 'const struct drm_format_info *info', 'const struct drm_mode_fb_cmd2 *mode_cmd'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000907 FieldDrift

- Risk: High
- Score: 10.0
- Symbol: net_iov
- Explanation: net_iov changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'type_', 'type': 'net_iov_type'}, {'name': 'pp_magic', 'type': 'ffi::c_ulong'}, {'name': 'pp', 'type': '*mut page_pool'}, {'name': 'owner', 'type': '*mut net_iov_area'}, {'name': 'dma_addr', 'type': 'ffi::c_ulong'}, {'name': 'pp_ref_count', 'type': 'atomic_long_t'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'net_iov__bindgen_ty_1'}, {'name': 'owner', 'type': '*mut net_iov_area'}, {'name': 'type_', 'type': 'net_iov_type'}]`

### Rust Evidence

- Graph edges: `7`

## W-000905 FieldDrift

- Risk: Medium
- Score: 9.8
- Symbol: mii_bus
- Explanation: mii_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'owner', 'type': '*mut module'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'id', 'type': '[ffi::c_char; 61usize]'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'read', 'type': '::core::option::Option<'}, {'name': 'write', 'type': '::core::option::Option<'}, {'name': 'read_c45', 'type': '::core::option::Option<'}, {'name': 'write_c45', 'type': '::core::option::Option<'}, {'name': 'reset', 'type': '::core::option::Option<unsafe extern "C" fn(bus: *mut mii_bus) -> ffi::c_int>'}, {'name': 'stats', 'type': '[mdio_bus_stats; 32usize]'}, {'name': 'mdio_lock', 'type': 'mutex'}, {'name': 'parent', 'type': '*mut device'}, {'name': 'state', 'type': 'mii_bus__bindgen_ty_1'}, {'name': 'dev', 'type': 'device'}, {'name': 'mdio_map', 'type': '[*mut mdio_device; 32usize]'}, {'name': 'phy_mask', 'type': 'u32_'}, {'name': 'phy_ignore_ta_mask', 'type': 'u32_'}, {'name': 'irq', 'type': '[ffi::c_int; 32usize]'}, {'name': 'reset_delay_us', 'type': 'ffi::c_int'}, {'name': 'reset_post_delay_us', 'type': 'ffi::c_int'}, {'name': 'reset_gpiod', 'type': '*mut gpio_desc'}, {'name': 'shared_lock', 'type': 'mutex'}, {'name': 'shared', 'type': '[*mut phy_package_shared; 32usize]'}]`
- New: `[{'name': 'owner', 'type': '*mut module'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'id', 'type': '[ffi::c_char; 61usize]'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'read', 'type': '::core::option::Option<'}, {'name': 'write', 'type': '::core::option::Option<'}, {'name': 'read_c45', 'type': '::core::option::Option<'}, {'name': 'write_c45', 'type': '::core::option::Option<'}, {'name': 'reset', 'type': '::core::option::Option<unsafe extern "C" fn(bus: *mut mii_bus) -> ffi::c_int>'}, {'name': 'stats', 'type': '[mdio_bus_stats; 32usize]'}, {'name': 'mdio_lock', 'type': 'mutex'}, {'name': 'parent', 'type': '*mut device'}, {'name': 'state', 'type': 'mii_bus__bindgen_ty_1'}, {'name': 'dev', 'type': 'device'}, {'name': 'mdio_map', 'type': '[*mut mdio_device; 32usize]'}, {'name': 'phy_mask', 'type': 'u32_'}, {'name': 'phy_ignore_ta_mask', 'type': 'u32_'}, {'name': 'irq', 'type': '[ffi::c_int; 32usize]'}, {'name': 'reset_delay_us', 'type': 'ffi::c_int'}, {'name': 'reset_post_delay_us', 'type': 'ffi::c_int'}, {'name': 'reset_gpiod', 'type': '*mut gpio_desc'}, {'name': 'shared_lock', 'type': 'mutex'}]`

### Rust Evidence

- Graph edges: `6`

## W-000463 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: auxiliary_get_drvdata
- Explanation: auxiliary_get_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000464 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: auxiliary_set_drvdata
- Explanation: auxiliary_set_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000492 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: cap_mmap_file
- Explanation: cap_mmap_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000493 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: cap_rss_ctx_supported
- Explanation: cap_rss_ctx_supported changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000504 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: d_set_d_op
- Explanation: d_set_d_op changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000594 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: for_reclaim
- Explanation: for_reclaim changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000613 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: get_pfnblock_flags_mask
- Explanation: get_pfnblock_flags_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000682 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mdio_device_bus_match
- Explanation: mdio_device_bus_match changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000684 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: memory_failure_queue_kick
- Explanation: memory_failure_queue_kick changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000691 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: no_hash_pointers_enable
- Explanation: no_hash_pointers_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000704 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: of_led_get
- Explanation: of_led_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000713 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: pci_get_drvdata
- Explanation: pci_get_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000714 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: pci_set_drvdata
- Explanation: pci_set_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000716 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_driver_is_genphy
- Explanation: phy_driver_is_genphy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000717 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_driver_is_genphy_10g
- Explanation: phy_driver_is_genphy_10g changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000719 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: platform_get_drvdata
- Explanation: platform_get_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000789 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sbitmap_get_shallow
- Explanation: sbitmap_get_shallow changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000795 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: set_pfnblock_flags_mask
- Explanation: set_pfnblock_flags_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000826 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sysctl_max_threads
- Explanation: sysctl_max_threads changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000866 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: work_on_cpu_safe_key
- Explanation: work_on_cpu_safe_key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000886 FieldDrift

- Risk: Medium
- Score: 9.6
- Symbol: blk_integrity
- Explanation: blk_integrity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'flags', 'type': 'ffi::c_uchar'}, {'name': 'csum_type', 'type': 'blk_integrity_checksum'}, {'name': 'tuple_size', 'type': 'ffi::c_uchar'}, {'name': 'pi_offset', 'type': 'ffi::c_uchar'}, {'name': 'interval_exp', 'type': 'ffi::c_uchar'}, {'name': 'tag_size', 'type': 'ffi::c_uchar'}]`
- New: `[{'name': 'flags', 'type': 'ffi::c_uchar'}, {'name': 'csum_type', 'type': 'blk_integrity_checksum'}, {'name': 'metadata_size', 'type': 'ffi::c_uchar'}, {'name': 'pi_offset', 'type': 'ffi::c_uchar'}, {'name': 'interval_exp', 'type': 'ffi::c_uchar'}, {'name': 'tag_size', 'type': 'ffi::c_uchar'}, {'name': 'pi_tuple_size', 'type': 'ffi::c_uchar'}]`

### Rust Evidence

- Graph edges: `5`

## W-001168 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: bitmap_weight
- Explanation: bitmap_weight changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['cpumask_bits(srcp)', 'small_cpumask_bits'], 'return_type': 'return'}`
- New: `{'params': ['intf', 'PHY_INTERFACE_MODE_MAX'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001169 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_engine_alloc_init_and_set
- Explanation: crypto_engine_alloc_init_and_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct device *dev', 'bool retry_support', 'int (*cbk_do_batch)(struct crypto_engine *engine)', 'bool rt', 'int qlen'], 'return_type': 'struct crypto_engine *'}`
- New: `{'params': ['struct device *dev', 'bool retry_support', 'bool rt', 'int qlen'], 'return_type': 'struct crypto_engine *'}`

### Rust Evidence

- Graph edges: `0`

## W-001172 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_bridge_detect
- Explanation: drm_bridge_detect changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_bridge *bridge'], 'return_type': 'enum drm_connector_status'}`
- New: `{'params': ['struct drm_bridge *bridge', 'struct drm_connector *connector'], 'return_type': 'enum drm_connector_status'}`

### Rust Evidence

- Graph edges: `0`

## W-001173 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_connector_hdmi_audio_init
- Explanation: drm_connector_hdmi_audio_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_connector *connector', 'struct device *hdmi_codec_dev', 'const struct drm_connector_hdmi_audio_funcs *funcs', 'unsigned int max_i2s_playback_channels', 'bool spdif_playback', 'int sound_dai_port'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_connector *connector', 'struct device *hdmi_codec_dev', 'const struct drm_connector_hdmi_audio_funcs *funcs', 'unsigned int max_i2s_playback_channels', 'u64 i2s_formats', 'bool spdif_playback', 'int sound_dai_port'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-001176 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_edp_backlight_enable
- Explanation: drm_edp_backlight_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_dp_aux *aux', 'const struct drm_edp_backlight_info *bl', 'u16 level'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_dp_aux *aux', 'const struct drm_edp_backlight_info *bl', 'u32 level'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-001177 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_edp_backlight_init
- Explanation: drm_edp_backlight_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_dp_aux *aux', 'struct drm_edp_backlight_info *bl', 'u16 driver_pwm_freq_hz', 'const u8 edp_dpcd[EDP_DISPLAY_CTL_CAP_SIZE]', 'u16 *current_level', 'u8 *current_mode'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_dp_aux *aux', 'struct drm_edp_backlight_info *bl', 'u32 max_luminance', 'u16 driver_pwm_freq_hz', 'const u8 edp_dpcd[EDP_DISPLAY_CTL_CAP_SIZE]', 'u32 *current_level', 'u8 *current_mode', 'bool need_luminance'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-001178 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_edp_backlight_set_level
- Explanation: drm_edp_backlight_set_level changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_dp_aux *aux', 'const struct drm_edp_backlight_info *bl', 'u16 level'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_dp_aux *aux', 'const struct drm_edp_backlight_info *bl', 'u32 level'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-001179 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_fb_xrgb8888_to_rgb565
- Explanation: drm_fb_xrgb8888_to_rgb565 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct iosys_map *dst', 'const unsigned int *dst_pitch', 'const struct iosys_map *src', 'const struct drm_framebuffer *fb', 'const struct drm_rect *clip', 'struct drm_format_conv_state *state', 'bool swab'], 'return_type': 'void'}`
- New: `{'params': ['struct iosys_map *dst', 'const unsigned int *dst_pitch', 'const struct iosys_map *src', 'const struct drm_framebuffer *fb', 'const struct drm_rect *clip', 'struct drm_format_conv_state *state'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001180 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_gem_fb_afbc_init
- Explanation: drm_gem_fb_afbc_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_device *dev', 'const struct drm_mode_fb_cmd2 *mode_cmd', 'struct drm_afbc_framebuffer *afbc_fb'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_device *dev', 'const struct drm_format_info *info', 'const struct drm_mode_fb_cmd2 *mode_cmd', 'struct drm_afbc_framebuffer *afbc_fb'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-001181 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_gem_fb_create
- Explanation: drm_gem_fb_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_device *dev', 'struct drm_file *file', 'const struct drm_mode_fb_cmd2 *mode_cmd'], 'return_type': 'struct drm_framebuffer *'}`
- New: `{'params': ['struct drm_device *dev', 'struct drm_file *file', 'const struct drm_format_info *info', 'const struct drm_mode_fb_cmd2 *mode_cmd'], 'return_type': 'struct drm_framebuffer *'}`

### Rust Evidence

- Graph edges: `0`

## W-001182 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_gem_fb_create_with_dirty
- Explanation: drm_gem_fb_create_with_dirty changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_device *dev', 'struct drm_file *file', 'const struct drm_mode_fb_cmd2 *mode_cmd'], 'return_type': 'struct drm_framebuffer *'}`
- New: `{'params': ['struct drm_device *dev', 'struct drm_file *file', 'const struct drm_format_info *info', 'const struct drm_mode_fb_cmd2 *mode_cmd'], 'return_type': 'struct drm_framebuffer *'}`

### Rust Evidence

- Graph edges: `0`

## W-001183 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_gem_fb_create_with_funcs
- Explanation: drm_gem_fb_create_with_funcs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_device *dev', 'struct drm_file *file', 'const struct drm_mode_fb_cmd2 *mode_cmd', 'const struct drm_framebuffer_funcs *funcs'], 'return_type': 'struct drm_framebuffer *'}`
- New: `{'params': ['struct drm_device *dev', 'struct drm_file *file', 'const struct drm_format_info *info', 'const struct drm_mode_fb_cmd2 *mode_cmd', 'const struct drm_framebuffer_funcs *funcs'], 'return_type': 'struct drm_framebuffer *'}`

### Rust Evidence

- Graph edges: `0`

## W-001184 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_gem_fb_init_with_funcs
- Explanation: drm_gem_fb_init_with_funcs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_device *dev', 'struct drm_framebuffer *fb', 'struct drm_file *file', 'const struct drm_mode_fb_cmd2 *mode_cmd', 'const struct drm_framebuffer_funcs *funcs'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_device *dev', 'struct drm_framebuffer *fb', 'struct drm_file *file', 'const struct drm_format_info *info', 'const struct drm_mode_fb_cmd2 *mode_cmd', 'const struct drm_framebuffer_funcs *funcs'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-001186 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_get_format_info
- Explanation: drm_get_format_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_device *dev', 'const struct drm_mode_fb_cmd2 *mode_cmd'], 'return_type': 'const struct drm_format_info *'}`
- New: `{'params': ['struct drm_device *dev', 'u32 pixel_format', 'u64 modifier'], 'return_type': 'const struct drm_format_info *'}`

### Rust Evidence

- Graph edges: `0`

## W-001188 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_sched_job_init
- Explanation: drm_sched_job_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_sched_job *job', 'struct drm_sched_entity *entity', 'u32 credits', 'void *owner'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_sched_job *job', 'struct drm_sched_entity *entity', 'u32 credits', 'void *owner', 'u64 drm_client_id'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-001190 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: file_user_inode
- Explanation: file_user_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct file *f'], 'return_type': 'static inline const struct inode *'}`
- New: `{'params': ['const struct file *f'], 'return_type': 'static inline const struct inode *'}`

### Rust Evidence

- Graph edges: `0`

## W-001191 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: file_user_path
- Explanation: file_user_path changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct file *f'], 'return_type': 'static inline const struct path *'}`
- New: `{'params': ['const struct file *f'], 'return_type': 'static inline const struct path *'}`

### Rust Evidence

- Graph edges: `0`

## W-001197 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_driver_is_genphy
- Explanation: phy_driver_is_genphy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct phy_device *phydev'], 'return_type': 'bool'}`
- New: `{'params': ['struct phy_device *phydev'], 'return_type': 'static inline bool'}`

### Rust Evidence

- Graph edges: `0`

## W-001202 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: scheduler_ipi
- Explanation: scheduler_ipi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'static inline void'}`
- New: `{'params': [], 'return_type': 'static __always_inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-001204 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sha1_init
- Explanation: sha1_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['__u32 *buf'], 'return_type': 'void'}`
- New: `{'params': ['struct sha1_ctx *ctx'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001205 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sha224_final
- Explanation: sha224_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct sha256_state *sctx', 'u8 out[SHA224_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['struct sha224_ctx *ctx', 'u8 out[SHA224_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001206 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sha224_init
- Explanation: sha224_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct sha256_state *sctx'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct sha224_ctx *ctx'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001207 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sha256_final
- Explanation: sha256_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct sha256_state *sctx', 'u8 out[SHA256_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['struct sha256_ctx *ctx', 'u8 out[SHA256_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001208 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sha256_init
- Explanation: sha256_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct sha256_state *sctx'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct sha256_ctx *ctx'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001209 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sha256_update
- Explanation: sha256_update changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct sha256_state *sctx', 'const u8 *data', 'size_t len'], 'return_type': 'void'}`
- New: `{'params': ['struct sha256_ctx *ctx', 'const u8 *data', 'size_t len'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-001211 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ttm_bo_lru_cursor_init
- Explanation: ttm_bo_lru_cursor_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct ttm_bo_lru_cursor *curs', 'struct ttm_resource_manager *man', 'struct ttm_operation_ctx *ctx'], 'return_type': 'struct ttm_bo_lru_cursor *'}`
- New: `{'params': ['struct ttm_bo_lru_cursor *curs', 'struct ttm_resource_manager *man', 'struct ttm_lru_walk_arg *arg'], 'return_type': 'struct ttm_bo_lru_cursor *'}`

### Rust Evidence

- Graph edges: `0`

## W-000908 FieldDrift

- Risk: Medium
- Score: 9.4
- Symbol: pci_host_bridge
- Explanation: pci_host_bridge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'dev', 'type': 'device'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'ops', 'type': '*mut pci_ops'}, {'name': 'child_ops', 'type': '*mut pci_ops'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'busnr', 'type': 'ffi::c_int'}, {'name': 'domain_nr', 'type': 'ffi::c_int'}, {'name': 'windows', 'type': 'list_head'}, {'name': 'dma_ranges', 'type': 'list_head'}, {'name': 'map_irq', 'type': '::core::option::Option<'}, {'name': 'release_fn', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut pci_host_bridge)>'}, {'name': 'enable_device', 'type': '::core::option::Option<'}, {'name': 'disable_device', 'type': '::core::option::Option<'}, {'name': 'release_data', 'type': '*mut ffi::c_void'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'align_resource', 'type': '::core::option::Option<'}, {'name': '__bindgen_padding_0', 'type': '[u64; 5usize]'}, {'name': 'private', 'type': '__IncompleteArrayField<ffi::c_ulong>'}]`
- New: `[{'name': 'dev', 'type': 'device'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'ops', 'type': '*mut pci_ops'}, {'name': 'child_ops', 'type': '*mut pci_ops'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'busnr', 'type': 'ffi::c_int'}, {'name': 'domain_nr', 'type': 'ffi::c_int'}, {'name': 'windows', 'type': 'list_head'}, {'name': 'dma_ranges', 'type': 'list_head'}, {'name': 'map_irq', 'type': '::core::option::Option<'}, {'name': 'release_fn', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut pci_host_bridge)>'}, {'name': 'enable_device', 'type': '::core::option::Option<'}, {'name': 'disable_device', 'type': '::core::option::Option<'}, {'name': 'release_data', 'type': '*mut ffi::c_void'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'align_resource', 'type': '::core::option::Option<'}, {'name': '__bindgen_padding_0', 'type': '[u64; 4usize]'}, {'name': 'private', 'type': '__IncompleteArrayField<ffi::c_ulong>'}]`

### Rust Evidence

- Graph edges: `4`

## W-000904 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: kunit_try_catch
- Explanation: kunit_try_catch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bindgen_opaque_blob', 'type': '[u64; 5usize]'}]`
- New: `[{'name': '_bindgen_opaque_blob', 'type': '[u64; 6usize]'}]`

### Rust Evidence

- Graph edges: `3`

## W-000902 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: file_ra_state
- Explanation: file_ra_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'start', 'type': 'ffi::c_ulong'}, {'name': 'size', 'type': 'ffi::c_uint'}, {'name': 'async_size', 'type': 'ffi::c_uint'}, {'name': 'ra_pages', 'type': 'ffi::c_uint'}, {'name': 'mmap_miss', 'type': 'ffi::c_uint'}, {'name': 'prev_pos', 'type': 'loff_t'}]`
- New: `[{'name': 'start', 'type': 'ffi::c_ulong'}, {'name': 'size', 'type': 'ffi::c_uint'}, {'name': 'async_size', 'type': 'ffi::c_uint'}, {'name': 'ra_pages', 'type': 'ffi::c_uint'}, {'name': 'order', 'type': 'ffi::c_ushort'}, {'name': 'mmap_miss', 'type': 'ffi::c_ushort'}, {'name': 'prev_pos', 'type': 'loff_t'}]`

### Rust Evidence

- Graph edges: `2`

## W-000906 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: mm_struct__bindgen_ty_1
- Explanation: mm_struct__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'mm_struct__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mm_mt', 'type': 'maple_tree'}, {'name': 'mmap_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'task_size', 'type': 'ffi::c_ulong'}, {'name': 'pgd', 'type': '*mut pgd_t'}, {'name': 'membarrier_state', 'type': 'atomic_t'}, {'name': 'mm_users', 'type': 'atomic_t'}, {'name': 'pcpu_cid', 'type': '*mut mm_cid'}, {'name': 'mm_cid_next_scan', 'type': 'ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_uint'}, {'name': 'max_nr_cid', 'type': 'atomic_t'}, {'name': 'cpus_allowed_lock', 'type': 'raw_spinlock_t'}, {'name': 'pgtables_bytes', 'type': 'atomic_long_t'}, {'name': 'map_count', 'type': 'ffi::c_int'}, {'name': 'page_table_lock', 'type': 'spinlock_t'}, {'name': 'mmap_lock', 'type': 'rw_semaphore'}, {'name': 'mmlist', 'type': 'list_head'}, {'name': 'vma_writer_wait', 'type': 'rcuwait'}, {'name': 'mm_lock_seq', 'type': 'seqcount_t'}, {'name': 'hiwater_rss', 'type': 'ffi::c_ulong'}, {'name': 'hiwater_vm', 'type': 'ffi::c_ulong'}, {'name': 'total_vm', 'type': 'ffi::c_ulong'}, {'name': 'locked_vm', 'type': 'ffi::c_ulong'}, {'name': 'pinned_vm', 'type': 'atomic64_t'}, {'name': 'data_vm', 'type': 'ffi::c_ulong'}, {'name': 'exec_vm', 'type': 'ffi::c_ulong'}, {'name': 'stack_vm', 'type': 'ffi::c_ulong'}, {'name': 'def_flags', 'type': 'ffi::c_ulong'}, {'name': 'write_protect_seq', 'type': 'seqcount_t'}, {'name': 'arg_lock', 'type': 'spinlock_t'}, {'name': 'start_code', 'type': 'ffi::c_ulong'}, {'name': 'end_code', 'type': 'ffi::c_ulong'}, {'name': 'start_data', 'type': 'ffi::c_ulong'}, {'name': 'end_data', 'type': 'ffi::c_ulong'}, {'name': 'start_brk', 'type': 'ffi::c_ulong'}, {'name': 'brk', 'type': 'ffi::c_ulong'}, {'name': 'start_stack', 'type': 'ffi::c_ulong'}, {'name': 'arg_start', 'type': 'ffi::c_ulong'}, {'name': 'arg_end', 'type': 'ffi::c_ulong'}, {'name': 'env_start', 'type': 'ffi::c_ulong'}, {'name': 'env_end', 'type': 'ffi::c_ulong'}, {'name': 'saved_auxv', 'type': '[ffi::c_ulong; 52usize]'}, {'name': 'rss_stat', 'type': '[percpu_counter; 4usize]'}, {'name': 'binfmt', 'type': '*mut linux_binfmt'}, {'name': 'context', 'type': 'mm_context_t'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'ioctx_lock', 'type': 'spinlock_t'}, {'name': 'ioctx_table', 'type': '*mut kioctx_table'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'exe_file', 'type': '*mut file'}, {'name': 'notifier_subscriptions', 'type': '*mut mmu_notifier_subscriptions'}, {'name': 'tlb_flush_pending', 'type': 'atomic_t'}, {'name': 'tlb_flush_batched', 'type': 'atomic_t'}, {'name': 'uprobes_state', 'type': 'uprobes_state'}, {'name': 'hugetlb_usage', 'type': 'atomic_long_t'}, {'name': 'async_put_work', 'type': 'work_struct'}, {'name': 'iommu_mm', 'type': '*mut iommu_mm_data'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'mm_struct__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mm_mt', 'type': 'maple_tree'}, {'name': 'mmap_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'task_size', 'type': 'ffi::c_ulong'}, {'name': 'pgd', 'type': '*mut pgd_t'}, {'name': 'membarrier_state', 'type': 'atomic_t'}, {'name': 'mm_users', 'type': 'atomic_t'}, {'name': 'pcpu_cid', 'type': '*mut mm_cid'}, {'name': 'mm_cid_next_scan', 'type': 'ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_uint'}, {'name': 'max_nr_cid', 'type': 'atomic_t'}, {'name': 'cpus_allowed_lock', 'type': 'raw_spinlock_t'}, {'name': 'pgtables_bytes', 'type': 'atomic_long_t'}, {'name': 'map_count', 'type': 'ffi::c_int'}, {'name': 'page_table_lock', 'type': 'spinlock_t'}, {'name': 'mmap_lock', 'type': 'rw_semaphore'}, {'name': 'mmlist', 'type': 'list_head'}, {'name': 'vma_writer_wait', 'type': 'rcuwait'}, {'name': 'mm_lock_seq', 'type': 'seqcount_t'}, {'name': 'futex_hash_lock', 'type': 'mutex'}, {'name': 'futex_phash', 'type': '*mut futex_private_hash'}, {'name': 'futex_phash_new', 'type': '*mut futex_private_hash'}, {'name': 'futex_batches', 'type': 'ffi::c_ulong'}, {'name': 'futex_rcu', 'type': 'callback_head'}, {'name': 'futex_atomic', 'type': 'atomic_long_t'}, {'name': 'futex_ref', 'type': '*mut ffi::c_uint'}, {'name': 'hiwater_rss', 'type': 'ffi::c_ulong'}, {'name': 'hiwater_vm', 'type': 'ffi::c_ulong'}, {'name': 'total_vm', 'type': 'ffi::c_ulong'}, {'name': 'locked_vm', 'type': 'ffi::c_ulong'}, {'name': 'pinned_vm', 'type': 'atomic64_t'}, {'name': 'data_vm', 'type': 'ffi::c_ulong'}, {'name': 'exec_vm', 'type': 'ffi::c_ulong'}, {'name': 'stack_vm', 'type': 'ffi::c_ulong'}, {'name': 'def_flags', 'type': 'vm_flags_t'}, {'name': 'write_protect_seq', 'type': 'seqcount_t'}, {'name': 'arg_lock', 'type': 'spinlock_t'}, {'name': 'start_code', 'type': 'ffi::c_ulong'}, {'name': 'end_code', 'type': 'ffi::c_ulong'}, {'name': 'start_data', 'type': 'ffi::c_ulong'}, {'name': 'end_data', 'type': 'ffi::c_ulong'}, {'name': 'start_brk', 'type': 'ffi::c_ulong'}, {'name': 'brk', 'type': 'ffi::c_ulong'}, {'name': 'start_stack', 'type': 'ffi::c_ulong'}, {'name': 'arg_start', 'type': 'ffi::c_ulong'}, {'name': 'arg_end', 'type': 'ffi::c_ulong'}, {'name': 'env_start', 'type': 'ffi::c_ulong'}, {'name': 'env_end', 'type': 'ffi::c_ulong'}, {'name': 'saved_auxv', 'type': '[ffi::c_ulong; 52usize]'}, {'name': 'rss_stat', 'type': '[percpu_counter; 4usize]'}, {'name': 'binfmt', 'type': '*mut linux_binfmt'}, {'name': 'context', 'type': 'mm_context_t'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'ioctx_lock', 'type': 'spinlock_t'}, {'name': 'ioctx_table', 'type': '*mut kioctx_table'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'exe_file', 'type': '*mut file'}, {'name': 'notifier_subscriptions', 'type': '*mut mmu_notifier_subscriptions'}, {'name': 'tlb_flush_pending', 'type': 'atomic_t'}, {'name': 'tlb_flush_batched', 'type': 'atomic_t'}, {'name': 'uprobes_state', 'type': 'uprobes_state'}, {'name': 'hugetlb_usage', 'type': 'atomic_long_t'}, {'name': 'async_put_work', 'type': 'work_struct'}, {'name': 'iommu_mm', 'type': '*mut iommu_mm_data'}]`

### Rust Evidence

- Graph edges: `2`

## W-000889 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bpf_link_info__bindgen_ty_1__bindgen_ty_2
- Explanation: bpf_link_info__bindgen_ty_1__bindgen_ty_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'attach_type', 'type': '__u32'}, {'name': 'target_obj_id', 'type': '__u32'}, {'name': 'target_btf_id', 'type': '__u32'}]`
- New: `[{'name': 'attach_type', 'type': '__u32'}, {'name': 'target_obj_id', 'type': '__u32'}, {'name': 'target_btf_id', 'type': '__u32'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': 'cookie', 'type': '__u64'}]`

### Rust Evidence

- Graph edges: `1`

## W-000891 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bpf_prog_aux
- Explanation: bpf_prog_aux changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'refcnt', 'type': 'atomic64_t'}, {'name': 'used_map_cnt', 'type': 'u32_'}, {'name': 'used_btf_cnt', 'type': 'u32_'}, {'name': 'max_ctx_offset', 'type': 'u32_'}, {'name': 'max_pkt_offset', 'type': 'u32_'}, {'name': 'max_tp_access', 'type': 'u32_'}, {'name': 'stack_depth', 'type': 'u32_'}, {'name': 'id', 'type': 'u32_'}, {'name': 'func_cnt', 'type': 'u32_'}, {'name': 'real_func_cnt', 'type': 'u32_'}, {'name': 'func_idx', 'type': 'u32_'}, {'name': 'attach_btf_id', 'type': 'u32_'}, {'name': 'attach_st_ops_member_off', 'type': 'u32_'}, {'name': 'ctx_arg_info_size', 'type': 'u32_'}, {'name': 'max_rdonly_access', 'type': 'u32_'}, {'name': 'max_rdwr_access', 'type': 'u32_'}, {'name': 'attach_btf', 'type': '*mut btf'}, {'name': 'ctx_arg_info', 'type': '*mut bpf_ctx_arg_aux'}, {'name': 'priv_stack_ptr', 'type': '*mut ffi::c_void'}, {'name': 'dst_mutex', 'type': 'mutex'}, {'name': 'dst_prog', 'type': '*mut bpf_prog'}, {'name': 'dst_trampoline', 'type': '*mut bpf_trampoline'}, {'name': 'saved_dst_prog_type', 'type': 'bpf_prog_type'}, {'name': 'saved_dst_attach_type', 'type': 'bpf_attach_type'}, {'name': 'verifier_zext', 'type': 'bool_'}, {'name': 'dev_bound', 'type': 'bool_'}, {'name': 'offload_requested', 'type': 'bool_'}, {'name': 'attach_btf_trace', 'type': 'bool_'}, {'name': 'attach_tracing_prog', 'type': 'bool_'}, {'name': 'func_proto_unreliable', 'type': 'bool_'}, {'name': 'tail_call_reachable', 'type': 'bool_'}, {'name': 'xdp_has_frags', 'type': 'bool_'}, {'name': 'exception_cb', 'type': 'bool_'}, {'name': 'exception_boundary', 'type': 'bool_'}, {'name': 'is_extended', 'type': 'bool_'}, {'name': 'jits_use_priv_stack', 'type': 'bool_'}, {'name': 'priv_stack_requested', 'type': 'bool_'}, {'name': 'changes_pkt_data', 'type': 'bool_'}, {'name': 'might_sleep', 'type': 'bool_'}, {'name': 'prog_array_member_cnt', 'type': 'u64_'}, {'name': 'ext_mutex', 'type': 'mutex'}, {'name': 'arena', 'type': '*mut bpf_arena'}, {'name': 'recursion_detected', 'type': '::core::option::Option<unsafe extern "C" fn(prog: *mut bpf_prog)>'}, {'name': 'attach_func_proto', 'type': '*const btf_type'}, {'name': 'attach_func_name', 'type': '*const ffi::c_char'}, {'name': 'func', 'type': '*mut *mut bpf_prog'}, {'name': 'jit_data', 'type': '*mut ffi::c_void'}, {'name': 'poke_tab', 'type': '*mut bpf_jit_poke_descriptor'}, {'name': 'kfunc_tab', 'type': '*mut bpf_kfunc_desc_tab'}, {'name': 'kfunc_btf_tab', 'type': '*mut bpf_kfunc_btf_tab'}, {'name': 'size_poke_tab', 'type': 'u32_'}, {'name': 'ksym', 'type': 'bpf_ksym'}, {'name': 'ops', 'type': '*const bpf_prog_ops'}, {'name': 'st_ops', 'type': '*const bpf_struct_ops'}, {'name': 'used_maps', 'type': '*mut *mut bpf_map'}, {'name': 'used_maps_mutex', 'type': 'mutex'}, {'name': 'used_btfs', 'type': '*mut btf_mod_pair'}, {'name': 'prog', 'type': '*mut bpf_prog'}, {'name': 'user', 'type': '*mut user_struct'}, {'name': 'load_time', 'type': 'u64_'}, {'name': 'verified_insns', 'type': 'u32_'}, {'name': 'cgroup_atype', 'type': 'ffi::c_int'}, {'name': 'cgroup_storage', 'type': '[*mut bpf_map; 2usize]'}, {'name': 'name', 'type': '[ffi::c_char; 16usize]'}, {'name': 'bpf_exception_cb', 'type': '::core::option::Option<'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'token', 'type': '*mut bpf_token'}, {'name': 'offload', 'type': '*mut bpf_prog_offload'}, {'name': 'btf', 'type': '*mut btf'}, {'name': 'func_info', 'type': '*mut bpf_func_info'}, {'name': 'func_info_aux', 'type': '*mut bpf_func_info_aux'}, {'name': 'linfo', 'type': '*mut bpf_line_info'}, {'name': 'jited_linfo', 'type': '*mut *mut ffi::c_void'}, {'name': 'func_info_cnt', 'type': 'u32_'}, {'name': 'nr_linfo', 'type': 'u32_'}, {'name': 'linfo_idx', 'type': 'u32_'}, {'name': 'mod_', 'type': '*mut module'}, {'name': 'num_exentries', 'type': 'u32_'}, {'name': 'extable', 'type': '*mut exception_table_entry'}, {'name': '__bindgen_anon_1', 'type': 'bpf_prog_aux__bindgen_ty_1'}]`
- New: `[{'name': 'refcnt', 'type': 'atomic64_t'}, {'name': 'used_map_cnt', 'type': 'u32_'}, {'name': 'used_btf_cnt', 'type': 'u32_'}, {'name': 'max_ctx_offset', 'type': 'u32_'}, {'name': 'max_pkt_offset', 'type': 'u32_'}, {'name': 'max_tp_access', 'type': 'u32_'}, {'name': 'stack_depth', 'type': 'u32_'}, {'name': 'id', 'type': 'u32_'}, {'name': 'func_cnt', 'type': 'u32_'}, {'name': 'real_func_cnt', 'type': 'u32_'}, {'name': 'func_idx', 'type': 'u32_'}, {'name': 'attach_btf_id', 'type': 'u32_'}, {'name': 'attach_st_ops_member_off', 'type': 'u32_'}, {'name': 'ctx_arg_info_size', 'type': 'u32_'}, {'name': 'max_rdonly_access', 'type': 'u32_'}, {'name': 'max_rdwr_access', 'type': 'u32_'}, {'name': 'attach_btf', 'type': '*mut btf'}, {'name': 'ctx_arg_info', 'type': '*mut bpf_ctx_arg_aux'}, {'name': 'priv_stack_ptr', 'type': '*mut ffi::c_void'}, {'name': 'dst_mutex', 'type': 'mutex'}, {'name': 'dst_prog', 'type': '*mut bpf_prog'}, {'name': 'dst_trampoline', 'type': '*mut bpf_trampoline'}, {'name': 'saved_dst_prog_type', 'type': 'bpf_prog_type'}, {'name': 'saved_dst_attach_type', 'type': 'bpf_attach_type'}, {'name': 'verifier_zext', 'type': 'bool_'}, {'name': 'dev_bound', 'type': 'bool_'}, {'name': 'offload_requested', 'type': 'bool_'}, {'name': 'attach_btf_trace', 'type': 'bool_'}, {'name': 'attach_tracing_prog', 'type': 'bool_'}, {'name': 'func_proto_unreliable', 'type': 'bool_'}, {'name': 'tail_call_reachable', 'type': 'bool_'}, {'name': 'xdp_has_frags', 'type': 'bool_'}, {'name': 'exception_cb', 'type': 'bool_'}, {'name': 'exception_boundary', 'type': 'bool_'}, {'name': 'is_extended', 'type': 'bool_'}, {'name': 'jits_use_priv_stack', 'type': 'bool_'}, {'name': 'priv_stack_requested', 'type': 'bool_'}, {'name': 'changes_pkt_data', 'type': 'bool_'}, {'name': 'might_sleep', 'type': 'bool_'}, {'name': 'prog_array_member_cnt', 'type': 'u64_'}, {'name': 'ext_mutex', 'type': 'mutex'}, {'name': 'arena', 'type': '*mut bpf_arena'}, {'name': 'recursion_detected', 'type': '::core::option::Option<unsafe extern "C" fn(prog: *mut bpf_prog)>'}, {'name': 'attach_func_proto', 'type': '*const btf_type'}, {'name': 'attach_func_name', 'type': '*const ffi::c_char'}, {'name': 'func', 'type': '*mut *mut bpf_prog'}, {'name': 'jit_data', 'type': '*mut ffi::c_void'}, {'name': 'poke_tab', 'type': '*mut bpf_jit_poke_descriptor'}, {'name': 'kfunc_tab', 'type': '*mut bpf_kfunc_desc_tab'}, {'name': 'kfunc_btf_tab', 'type': '*mut bpf_kfunc_btf_tab'}, {'name': 'size_poke_tab', 'type': 'u32_'}, {'name': 'ksym', 'type': 'bpf_ksym'}, {'name': 'ops', 'type': '*const bpf_prog_ops'}, {'name': 'st_ops', 'type': '*const bpf_struct_ops'}, {'name': 'used_maps', 'type': '*mut *mut bpf_map'}, {'name': 'used_maps_mutex', 'type': 'mutex'}, {'name': 'used_btfs', 'type': '*mut btf_mod_pair'}, {'name': 'prog', 'type': '*mut bpf_prog'}, {'name': 'user', 'type': '*mut user_struct'}, {'name': 'load_time', 'type': 'u64_'}, {'name': 'verified_insns', 'type': 'u32_'}, {'name': 'cgroup_atype', 'type': 'ffi::c_int'}, {'name': 'cgroup_storage', 'type': '[*mut bpf_map; 2usize]'}, {'name': 'name', 'type': '[ffi::c_char; 16usize]'}, {'name': 'bpf_exception_cb', 'type': '::core::option::Option<'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'token', 'type': '*mut bpf_token'}, {'name': 'offload', 'type': '*mut bpf_prog_offload'}, {'name': 'btf', 'type': '*mut btf'}, {'name': 'func_info', 'type': '*mut bpf_func_info'}, {'name': 'func_info_aux', 'type': '*mut bpf_func_info_aux'}, {'name': 'linfo', 'type': '*mut bpf_line_info'}, {'name': 'jited_linfo', 'type': '*mut *mut ffi::c_void'}, {'name': 'func_info_cnt', 'type': 'u32_'}, {'name': 'nr_linfo', 'type': 'u32_'}, {'name': 'linfo_idx', 'type': 'u32_'}, {'name': 'mod_', 'type': '*mut module'}, {'name': 'num_exentries', 'type': 'u32_'}, {'name': 'extable', 'type': '*mut exception_table_entry'}, {'name': '__bindgen_anon_1', 'type': 'bpf_prog_aux__bindgen_ty_1'}, {'name': 'stream', 'type': '[bpf_stream; 2usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000892 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bpf_tracing_link
- Explanation: bpf_tracing_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'link', 'type': 'bpf_tramp_link'}, {'name': 'attach_type', 'type': 'bpf_attach_type'}, {'name': 'trampoline', 'type': '*mut bpf_trampoline'}, {'name': 'tgt_prog', 'type': '*mut bpf_prog'}]`
- New: `[{'name': 'link', 'type': 'bpf_tramp_link'}, {'name': 'trampoline', 'type': '*mut bpf_trampoline'}, {'name': 'tgt_prog', 'type': '*mut bpf_prog'}]`

### Rust Evidence

- Graph edges: `1`

## W-000894 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: codetag_iterator
- Explanation: codetag_iterator changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'cttype', 'type': '*mut codetag_type'}, {'name': 'cmod', 'type': '*mut codetag_module'}, {'name': 'mod_id', 'type': 'ffi::c_ulong'}, {'name': 'ct', 'type': '*mut codetag'}]`
- New: `[{'name': 'cttype', 'type': '*mut codetag_type'}, {'name': 'cmod', 'type': '*mut codetag_module'}, {'name': 'mod_id', 'type': 'ffi::c_ulong'}, {'name': 'ct', 'type': '*mut codetag'}, {'name': 'mod_seq', 'type': 'ffi::c_ulong'}]`

### Rust Evidence

- Graph edges: `1`

## W-000895 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: css_rstat_cpu
- Explanation: css_rstat_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'updated_children', 'type': '*mut cgroup_subsys_state'}, {'name': 'updated_next', 'type': '*mut cgroup_subsys_state'}]`
- New: `[{'name': 'updated_children', 'type': '*mut cgroup_subsys_state'}, {'name': 'updated_next', 'type': '*mut cgroup_subsys_state'}, {'name': 'lnode', 'type': 'llist_node'}, {'name': 'owner', 'type': '*mut cgroup_subsys_state'}]`

### Rust Evidence

- Graph edges: `1`

## W-000896 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: dev_pm_info
- Explanation: dev_pm_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'power_state', 'type': 'pm_message_t'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'driver_flags', 'type': 'u32_'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'entry', 'type': 'list_head'}, {'name': 'completion', 'type': 'completion'}, {'name': 'wakeup', 'type': '*mut wakeup_source'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'suspend_timer', 'type': 'hrtimer'}, {'name': 'timer_expires', 'type': 'u64_'}, {'name': 'work', 'type': 'work_struct'}, {'name': 'wait_queue', 'type': 'wait_queue_head_t'}, {'name': 'wakeirq', 'type': '*mut wake_irq'}, {'name': 'usage_count', 'type': 'atomic_t'}, {'name': 'child_count', 'type': 'atomic_t'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'links_count', 'type': 'ffi::c_uint'}, {'name': 'request', 'type': 'rpm_request'}, {'name': 'runtime_status', 'type': 'rpm_status'}, {'name': 'last_status', 'type': 'rpm_status'}, {'name': 'runtime_error', 'type': 'ffi::c_int'}, {'name': 'autosuspend_delay', 'type': 'ffi::c_int'}, {'name': 'last_busy', 'type': 'u64_'}, {'name': 'active_time', 'type': 'u64_'}, {'name': 'suspended_time', 'type': 'u64_'}, {'name': 'accounting_timestamp', 'type': 'u64_'}, {'name': 'subsys_data', 'type': '*mut pm_subsys_data'}, {'name': 'qos', 'type': '*mut dev_pm_qos'}]`
- New: `[{'name': 'power_state', 'type': 'pm_message_t'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'driver_flags', 'type': 'u32_'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'entry', 'type': 'list_head'}, {'name': 'completion', 'type': 'completion'}, {'name': 'wakeup', 'type': '*mut wakeup_source'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'suspend_timer', 'type': 'hrtimer'}, {'name': 'timer_expires', 'type': 'u64_'}, {'name': 'work', 'type': 'work_struct'}, {'name': 'wait_queue', 'type': 'wait_queue_head_t'}, {'name': 'wakeirq', 'type': '*mut wake_irq'}, {'name': 'usage_count', 'type': 'atomic_t'}, {'name': 'child_count', 'type': 'atomic_t'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'links_count', 'type': 'ffi::c_uint'}, {'name': 'request', 'type': 'rpm_request'}, {'name': 'runtime_status', 'type': 'rpm_status'}, {'name': 'last_status', 'type': 'rpm_status'}, {'name': 'runtime_error', 'type': 'ffi::c_int'}, {'name': 'autosuspend_delay', 'type': 'ffi::c_int'}, {'name': 'last_busy', 'type': 'u64_'}, {'name': 'active_time', 'type': 'u64_'}, {'name': 'suspended_time', 'type': 'u64_'}, {'name': 'accounting_timestamp', 'type': 'u64_'}, {'name': 'subsys_data', 'type': '*mut pm_subsys_data'}, {'name': 'qos', 'type': '*mut dev_pm_qos'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 7usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000897 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: dma_fence_ops
- Explanation: dma_fence_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'use_64bit_seqno', 'type': 'bool_'}, {'name': 'signaled', 'type': '::core::option::Option<unsafe extern "C" fn(fence: *mut dma_fence) -> bool_>'}, {'name': 'wait', 'type': '::core::option::Option<'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(fence: *mut dma_fence)>'}]`
- New: `[{'name': 'signaled', 'type': '::core::option::Option<unsafe extern "C" fn(fence: *mut dma_fence) -> bool_>'}, {'name': 'wait', 'type': '::core::option::Option<'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(fence: *mut dma_fence)>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000899 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: ethtool_ops
- Explanation: ethtool_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'rxfh_indir_space', 'type': 'u32_'}, {'name': 'rxfh_key_space', 'type': 'u16_'}, {'name': 'rxfh_priv_size', 'type': 'u16_'}, {'name': 'rxfh_max_num_contexts', 'type': 'u32_'}, {'name': 'supported_coalesce_params', 'type': 'u32_'}, {'name': 'supported_ring_params', 'type': 'u32_'}, {'name': 'supported_hwtstamp_qualifiers', 'type': 'u32_'}, {'name': 'get_drvinfo', 'type': '::core::option::Option<'}, {'name': 'get_regs', 'type': '::core::option::Option<'}, {'name': 'get_wol', 'type': '::core::option::Option<'}, {'name': 'set_wol', 'type': '::core::option::Option<'}, {'name': 'get_msglevel', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'get_link', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'get_link_ext_state', 'type': '::core::option::Option<'}, {'name': 'get_link_ext_stats', 'type': '::core::option::Option<'}, {'name': 'get_eeprom', 'type': '::core::option::Option<'}, {'name': 'set_eeprom', 'type': '::core::option::Option<'}, {'name': 'get_coalesce', 'type': '::core::option::Option<'}, {'name': 'set_coalesce', 'type': '::core::option::Option<'}, {'name': 'get_ringparam', 'type': '::core::option::Option<'}, {'name': 'set_ringparam', 'type': '::core::option::Option<'}, {'name': 'get_pause_stats', 'type': '::core::option::Option<'}, {'name': 'get_pauseparam', 'type': '::core::option::Option<'}, {'name': 'set_pauseparam', 'type': '::core::option::Option<'}, {'name': 'self_test', 'type': '::core::option::Option<'}, {'name': 'get_strings', 'type': '::core::option::Option<'}, {'name': 'set_phys_id', 'type': '::core::option::Option<'}, {'name': 'get_ethtool_stats', 'type': '::core::option::Option<'}, {'name': 'begin', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> ffi::c_int>'}, {'name': 'complete', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device)>'}, {'name': 'get_priv_flags', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'set_priv_flags', 'type': '::core::option::Option<'}, {'name': 'get_sset_count', 'type': '::core::option::Option<'}, {'name': 'get_rxnfc', 'type': '::core::option::Option<'}, {'name': 'set_rxnfc', 'type': '::core::option::Option<'}, {'name': 'flash_device', 'type': '::core::option::Option<'}, {'name': 'reset', 'type': '::core::option::Option<'}, {'name': 'get_rxfh', 'type': '::core::option::Option<'}, {'name': 'set_rxfh', 'type': '::core::option::Option<'}, {'name': 'create_rxfh_context', 'type': '::core::option::Option<'}, {'name': 'modify_rxfh_context', 'type': '::core::option::Option<'}, {'name': 'remove_rxfh_context', 'type': '::core::option::Option<'}, {'name': 'get_channels', 'type': '::core::option::Option<'}, {'name': 'set_channels', 'type': '::core::option::Option<'}, {'name': 'get_dump_flag', 'type': '::core::option::Option<'}, {'name': 'get_dump_data', 'type': '::core::option::Option<'}, {'name': 'set_dump', 'type': '::core::option::Option<'}, {'name': 'get_ts_info', 'type': '::core::option::Option<'}, {'name': 'get_ts_stats', 'type': '::core::option::Option<'}, {'name': 'get_module_info', 'type': '::core::option::Option<'}, {'name': 'get_module_eeprom', 'type': '::core::option::Option<'}, {'name': 'get_eee', 'type': '::core::option::Option<'}, {'name': 'set_eee', 'type': '::core::option::Option<'}, {'name': 'get_tunable', 'type': '::core::option::Option<'}, {'name': 'set_tunable', 'type': '::core::option::Option<'}, {'name': 'get_per_queue_coalesce', 'type': '::core::option::Option<'}, {'name': 'set_per_queue_coalesce', 'type': '::core::option::Option<'}, {'name': 'get_link_ksettings', 'type': '::core::option::Option<'}, {'name': 'set_link_ksettings', 'type': '::core::option::Option<'}, {'name': 'get_fec_stats', 'type': '::core::option::Option<'}, {'name': 'get_fecparam', 'type': '::core::option::Option<'}, {'name': 'set_fecparam', 'type': '::core::option::Option<'}, {'name': 'get_ethtool_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_phy_tunable', 'type': '::core::option::Option<'}, {'name': 'set_phy_tunable', 'type': '::core::option::Option<'}, {'name': 'get_module_eeprom_by_page', 'type': '::core::option::Option<'}, {'name': 'set_module_eeprom_by_page', 'type': '::core::option::Option<'}, {'name': 'get_eth_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_eth_mac_stats', 'type': '::core::option::Option<'}, {'name': 'get_eth_ctrl_stats', 'type': '::core::option::Option<'}, {'name': 'get_rmon_stats', 'type': '::core::option::Option<'}, {'name': 'get_module_power_mode', 'type': '::core::option::Option<'}, {'name': 'set_module_power_mode', 'type': '::core::option::Option<'}, {'name': 'get_mm', 'type': '::core::option::Option<'}, {'name': 'set_mm', 'type': '::core::option::Option<'}, {'name': 'get_mm_stats', 'type': '::core::option::Option<'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'rxfh_indir_space', 'type': 'u32_'}, {'name': 'rxfh_key_space', 'type': 'u16_'}, {'name': 'rxfh_priv_size', 'type': 'u16_'}, {'name': 'rxfh_max_num_contexts', 'type': 'u32_'}, {'name': 'supported_coalesce_params', 'type': 'u32_'}, {'name': 'supported_ring_params', 'type': 'u32_'}, {'name': 'supported_hwtstamp_qualifiers', 'type': 'u32_'}, {'name': 'get_drvinfo', 'type': '::core::option::Option<'}, {'name': 'get_regs', 'type': '::core::option::Option<'}, {'name': 'get_wol', 'type': '::core::option::Option<'}, {'name': 'set_wol', 'type': '::core::option::Option<'}, {'name': 'get_msglevel', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'get_link', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'get_link_ext_state', 'type': '::core::option::Option<'}, {'name': 'get_link_ext_stats', 'type': '::core::option::Option<'}, {'name': 'get_eeprom', 'type': '::core::option::Option<'}, {'name': 'set_eeprom', 'type': '::core::option::Option<'}, {'name': 'get_coalesce', 'type': '::core::option::Option<'}, {'name': 'set_coalesce', 'type': '::core::option::Option<'}, {'name': 'get_ringparam', 'type': '::core::option::Option<'}, {'name': 'set_ringparam', 'type': '::core::option::Option<'}, {'name': 'get_pause_stats', 'type': '::core::option::Option<'}, {'name': 'get_pauseparam', 'type': '::core::option::Option<'}, {'name': 'set_pauseparam', 'type': '::core::option::Option<'}, {'name': 'self_test', 'type': '::core::option::Option<'}, {'name': 'get_strings', 'type': '::core::option::Option<'}, {'name': 'set_phys_id', 'type': '::core::option::Option<'}, {'name': 'get_ethtool_stats', 'type': '::core::option::Option<'}, {'name': 'begin', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> ffi::c_int>'}, {'name': 'complete', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device)>'}, {'name': 'get_priv_flags', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'set_priv_flags', 'type': '::core::option::Option<'}, {'name': 'get_sset_count', 'type': '::core::option::Option<'}, {'name': 'get_rxnfc', 'type': '::core::option::Option<'}, {'name': 'set_rxnfc', 'type': '::core::option::Option<'}, {'name': 'flash_device', 'type': '::core::option::Option<'}, {'name': 'reset', 'type': '::core::option::Option<'}, {'name': 'get_rxfh', 'type': '::core::option::Option<'}, {'name': 'set_rxfh', 'type': '::core::option::Option<'}, {'name': 'get_rxfh_fields', 'type': '::core::option::Option<'}, {'name': 'set_rxfh_fields', 'type': '::core::option::Option<'}, {'name': 'create_rxfh_context', 'type': '::core::option::Option<'}, {'name': 'modify_rxfh_context', 'type': '::core::option::Option<'}, {'name': 'remove_rxfh_context', 'type': '::core::option::Option<'}, {'name': 'get_channels', 'type': '::core::option::Option<'}, {'name': 'set_channels', 'type': '::core::option::Option<'}, {'name': 'get_dump_flag', 'type': '::core::option::Option<'}, {'name': 'get_dump_data', 'type': '::core::option::Option<'}, {'name': 'set_dump', 'type': '::core::option::Option<'}, {'name': 'get_ts_info', 'type': '::core::option::Option<'}, {'name': 'get_ts_stats', 'type': '::core::option::Option<'}, {'name': 'get_module_info', 'type': '::core::option::Option<'}, {'name': 'get_module_eeprom', 'type': '::core::option::Option<'}, {'name': 'get_eee', 'type': '::core::option::Option<'}, {'name': 'set_eee', 'type': '::core::option::Option<'}, {'name': 'get_tunable', 'type': '::core::option::Option<'}, {'name': 'set_tunable', 'type': '::core::option::Option<'}, {'name': 'get_per_queue_coalesce', 'type': '::core::option::Option<'}, {'name': 'set_per_queue_coalesce', 'type': '::core::option::Option<'}, {'name': 'get_link_ksettings', 'type': '::core::option::Option<'}, {'name': 'set_link_ksettings', 'type': '::core::option::Option<'}, {'name': 'get_fec_stats', 'type': '::core::option::Option<'}, {'name': 'get_fecparam', 'type': '::core::option::Option<'}, {'name': 'set_fecparam', 'type': '::core::option::Option<'}, {'name': 'get_ethtool_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_phy_tunable', 'type': '::core::option::Option<'}, {'name': 'set_phy_tunable', 'type': '::core::option::Option<'}, {'name': 'get_module_eeprom_by_page', 'type': '::core::option::Option<'}, {'name': 'set_module_eeprom_by_page', 'type': '::core::option::Option<'}, {'name': 'get_eth_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_eth_mac_stats', 'type': '::core::option::Option<'}, {'name': 'get_eth_ctrl_stats', 'type': '::core::option::Option<'}, {'name': 'get_rmon_stats', 'type': '::core::option::Option<'}, {'name': 'get_module_power_mode', 'type': '::core::option::Option<'}, {'name': 'set_module_power_mode', 'type': '::core::option::Option<'}, {'name': 'get_mm', 'type': '::core::option::Option<'}, {'name': 'set_mm', 'type': '::core::option::Option<'}, {'name': 'get_mm_stats', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-000900 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: ethtool_rmon_stats__bindgen_ty_1__bindgen_ty_1
- Explanation: ethtool_rmon_stats__bindgen_ty_1__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'undersize_pkts', 'type': 'u64_'}, {'name': 'oversize_pkts', 'type': 'u64_'}, {'name': 'fragments', 'type': 'u64_'}, {'name': 'jabbers', 'type': 'u64_'}, {'name': 'hist', 'type': '[u64_; 10usize]'}, {'name': 'hist_tx', 'type': '[u64_; 10usize]'}]`
- New: `[{'name': 'undersize_pkts', 'type': 'u64_'}, {'name': 'oversize_pkts', 'type': 'u64_'}, {'name': 'fragments', 'type': 'u64_'}, {'name': 'jabbers', 'type': 'u64_'}, {'name': 'hist', 'type': '[u64_; 11usize]'}, {'name': 'hist_tx', 'type': '[u64_; 11usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000901 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: ethtool_rmon_stats__bindgen_ty_1__bindgen_ty_2
- Explanation: ethtool_rmon_stats__bindgen_ty_1__bindgen_ty_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'undersize_pkts', 'type': 'u64_'}, {'name': 'oversize_pkts', 'type': 'u64_'}, {'name': 'fragments', 'type': 'u64_'}, {'name': 'jabbers', 'type': 'u64_'}, {'name': 'hist', 'type': '[u64_; 10usize]'}, {'name': 'hist_tx', 'type': '[u64_; 10usize]'}]`
- New: `[{'name': 'undersize_pkts', 'type': 'u64_'}, {'name': 'oversize_pkts', 'type': 'u64_'}, {'name': 'fragments', 'type': 'u64_'}, {'name': 'jabbers', 'type': 'u64_'}, {'name': 'hist', 'type': '[u64_; 11usize]'}, {'name': 'hist_tx', 'type': '[u64_; 11usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000903 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: kernel_ethtool_ts_info
- Explanation: kernel_ethtool_ts_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'cmd', 'type': 'u32_'}, {'name': 'so_timestamping', 'type': 'u32_'}, {'name': 'phc_index', 'type': 'ffi::c_int'}, {'name': 'phc_qualifier', 'type': 'hwtstamp_provider_qualifier'}, {'name': 'phc_source', 'type': 'hwtstamp_source'}, {'name': 'phc_phyindex', 'type': 'ffi::c_int'}, {'name': 'tx_types', 'type': 'hwtstamp_tx_types'}, {'name': 'rx_filters', 'type': 'hwtstamp_rx_filters'}]`
- New: `[{'name': 'cmd', 'type': 'u32_'}, {'name': 'so_timestamping', 'type': 'u32_'}, {'name': 'phc_index', 'type': 'ffi::c_int'}, {'name': 'phc_qualifier', 'type': 'hwtstamp_provider_qualifier'}, {'name': 'phc_source', 'type': 'hwtstamp_source'}, {'name': 'phc_phyindex', 'type': 'ffi::c_int'}, {'name': 'tx_types', 'type': 'u32_'}, {'name': 'rx_filters', 'type': 'u32_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000909 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: per_cpu_nodestat
- Explanation: per_cpu_nodestat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'stat_threshold', 'type': 's8'}, {'name': 'vm_node_stat_diff', 'type': '[s8; 48usize]'}]`
- New: `[{'name': 'stat_threshold', 'type': 's8'}, {'name': 'vm_node_stat_diff', 'type': '[s8; 47usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000910 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: pglist_data
- Explanation: pglist_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'node_zones', 'type': '[zone; 4usize]'}, {'name': 'node_zonelists', 'type': '[zonelist; 2usize]'}, {'name': 'nr_zones', 'type': 'ffi::c_int'}, {'name': 'node_start_pfn', 'type': 'ffi::c_ulong'}, {'name': 'node_present_pages', 'type': 'ffi::c_ulong'}, {'name': 'node_spanned_pages', 'type': 'ffi::c_ulong'}, {'name': 'node_id', 'type': 'ffi::c_int'}, {'name': 'kswapd_wait', 'type': 'wait_queue_head_t'}, {'name': 'pfmemalloc_wait', 'type': 'wait_queue_head_t'}, {'name': 'reclaim_wait', 'type': '[wait_queue_head_t; 4usize]'}, {'name': 'nr_writeback_throttled', 'type': 'atomic_t'}, {'name': 'nr_reclaim_start', 'type': 'ffi::c_ulong'}, {'name': 'kswapd', 'type': '*mut task_struct'}, {'name': 'kswapd_order', 'type': 'ffi::c_int'}, {'name': 'kswapd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kswapd_failures', 'type': 'ffi::c_int'}, {'name': 'kcompactd_max_order', 'type': 'ffi::c_int'}, {'name': 'kcompactd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kcompactd_wait', 'type': 'wait_queue_head_t'}, {'name': 'kcompactd', 'type': '*mut task_struct'}, {'name': 'proactive_compact_trigger', 'type': 'bool_'}, {'name': 'totalreserve_pages', 'type': 'ffi::c_ulong'}, {'name': 'min_unmapped_pages', 'type': 'ffi::c_ulong'}, {'name': 'min_slab_pages', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': '__lruvec', 'type': 'lruvec'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_padding_1', 'type': '[u64; 6usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'per_cpu_nodestats', 'type': '*mut per_cpu_nodestat'}, {'name': 'vm_stat', 'type': '[atomic_long_t; 48usize]'}, {'name': 'memtier', 'type': '*mut memory_tier'}]`
- New: `[{'name': 'node_zones', 'type': '[zone; 4usize]'}, {'name': 'node_zonelists', 'type': '[zonelist; 2usize]'}, {'name': 'nr_zones', 'type': 'ffi::c_int'}, {'name': 'node_start_pfn', 'type': 'ffi::c_ulong'}, {'name': 'node_present_pages', 'type': 'ffi::c_ulong'}, {'name': 'node_spanned_pages', 'type': 'ffi::c_ulong'}, {'name': 'node_id', 'type': 'ffi::c_int'}, {'name': 'kswapd_wait', 'type': 'wait_queue_head_t'}, {'name': 'pfmemalloc_wait', 'type': 'wait_queue_head_t'}, {'name': 'reclaim_wait', 'type': '[wait_queue_head_t; 4usize]'}, {'name': 'nr_writeback_throttled', 'type': 'atomic_t'}, {'name': 'nr_reclaim_start', 'type': 'ffi::c_ulong'}, {'name': 'kswapd', 'type': '*mut task_struct'}, {'name': 'kswapd_order', 'type': 'ffi::c_int'}, {'name': 'kswapd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kswapd_failures', 'type': 'ffi::c_int'}, {'name': 'kcompactd_max_order', 'type': 'ffi::c_int'}, {'name': 'kcompactd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kcompactd_wait', 'type': 'wait_queue_head_t'}, {'name': 'kcompactd', 'type': '*mut task_struct'}, {'name': 'proactive_compact_trigger', 'type': 'bool_'}, {'name': 'totalreserve_pages', 'type': 'ffi::c_ulong'}, {'name': 'min_unmapped_pages', 'type': 'ffi::c_ulong'}, {'name': 'min_slab_pages', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': '__lruvec', 'type': 'lruvec'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_padding_1', 'type': '[u64; 6usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'per_cpu_nodestats', 'type': '*mut per_cpu_nodestat'}, {'name': 'vm_stat', 'type': '[atomic_long_t; 47usize]'}, {'name': 'memtier', 'type': '*mut memory_tier'}]`

### Rust Evidence

- Graph edges: `1`

## W-000913 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: proc_dir_entry
- Explanation: proc_dir_entry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[]`

### Rust Evidence

- Graph edges: `1`

## W-000915 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: readahead_control
- Explanation: readahead_control changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'file', 'type': '*mut file'}, {'name': 'mapping', 'type': '*mut address_space'}, {'name': 'ra', 'type': '*mut file_ra_state'}, {'name': '_index', 'type': 'ffi::c_ulong'}, {'name': '_nr_pages', 'type': 'ffi::c_uint'}, {'name': '_batch_count', 'type': 'ffi::c_uint'}, {'name': 'dropbehind', 'type': 'bool_'}, {'name': '_workingset', 'type': 'bool_'}, {'name': '_pflags', 'type': 'ffi::c_ulong'}]`

### Rust Evidence

- Graph edges: `1`

## W-000916 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: reclaim_state
- Explanation: reclaim_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'reclaimed', 'type': 'ffi::c_ulong'}]`

### Rust Evidence

- Graph edges: `1`

## W-000917 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: renamedata
- Explanation: renamedata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'old_mnt_idmap', 'type': '*mut mnt_idmap'}, {'name': 'old_dir', 'type': '*mut inode'}, {'name': 'old_dentry', 'type': '*mut dentry'}, {'name': 'new_mnt_idmap', 'type': '*mut mnt_idmap'}, {'name': 'new_dir', 'type': '*mut inode'}, {'name': 'new_dentry', 'type': '*mut dentry'}, {'name': 'delegated_inode', 'type': '*mut *mut inode'}, {'name': 'flags', 'type': 'ffi::c_uint'}]`
- New: `[{'name': 'old_mnt_idmap', 'type': '*mut mnt_idmap'}, {'name': 'old_parent', 'type': '*mut dentry'}, {'name': 'old_dentry', 'type': '*mut dentry'}, {'name': 'new_mnt_idmap', 'type': '*mut mnt_idmap'}, {'name': 'new_parent', 'type': '*mut dentry'}, {'name': 'new_dentry', 'type': '*mut dentry'}, {'name': 'delegated_inode', 'type': '*mut *mut inode'}, {'name': 'flags', 'type': 'ffi::c_uint'}]`

### Rust Evidence

- Graph edges: `1`

## W-000918 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: sched_dl_entity
- Explanation: sched_dl_entity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'rb_node', 'type': 'rb_node'}, {'name': 'dl_runtime', 'type': 'u64_'}, {'name': 'dl_deadline', 'type': 'u64_'}, {'name': 'dl_period', 'type': 'u64_'}, {'name': 'dl_bw', 'type': 'u64_'}, {'name': 'dl_density', 'type': 'u64_'}, {'name': 'runtime', 'type': 's64'}, {'name': 'deadline', 'type': 'u64_'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'dl_timer', 'type': 'hrtimer'}, {'name': 'inactive_timer', 'type': 'hrtimer'}, {'name': 'rq', 'type': '*mut rq'}, {'name': 'server_has_tasks', 'type': 'dl_server_has_tasks_f'}, {'name': 'server_pick_task', 'type': 'dl_server_pick_f'}, {'name': 'pi_se', 'type': '*mut sched_dl_entity'}]`
- New: `[{'name': 'rb_node', 'type': 'rb_node'}, {'name': 'dl_runtime', 'type': 'u64_'}, {'name': 'dl_deadline', 'type': 'u64_'}, {'name': 'dl_period', 'type': 'u64_'}, {'name': 'dl_bw', 'type': 'u64_'}, {'name': 'dl_density', 'type': 'u64_'}, {'name': 'runtime', 'type': 's64'}, {'name': 'deadline', 'type': 'u64_'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'dl_timer', 'type': 'hrtimer'}, {'name': 'inactive_timer', 'type': 'hrtimer'}, {'name': 'rq', 'type': '*mut rq'}, {'name': 'server_pick_task', 'type': 'dl_server_pick_f'}, {'name': 'pi_se', 'type': '*mut sched_dl_entity'}]`

### Rust Evidence

- Graph edges: `1`

## W-000919 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: sched_domain_topology_level
- Explanation: sched_domain_topology_level changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mask', 'type': 'sched_domain_mask_f'}, {'name': 'sd_flags', 'type': 'sched_domain_flags_f'}, {'name': 'flags', 'type': 'ffi::c_int'}, {'name': 'numa_level', 'type': 'ffi::c_int'}, {'name': 'data', 'type': 'sd_data'}, {'name': 'name', 'type': '*mut ffi::c_char'}]`
- New: `[{'name': 'mask', 'type': 'sched_domain_mask_f'}, {'name': 'sd_flags', 'type': 'sched_domain_flags_f'}, {'name': 'numa_level', 'type': 'ffi::c_int'}, {'name': 'data', 'type': 'sd_data'}, {'name': 'name', 'type': '*mut ffi::c_char'}]`

### Rust Evidence

- Graph edges: `1`

## W-000920 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: sched_entity
- Explanation: sched_entity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'load', 'type': 'load_weight'}, {'name': 'run_node', 'type': 'rb_node'}, {'name': 'deadline', 'type': 'u64_'}, {'name': 'min_vruntime', 'type': 'u64_'}, {'name': 'min_slice', 'type': 'u64_'}, {'name': 'group_node', 'type': 'list_head'}, {'name': 'on_rq', 'type': 'ffi::c_uchar'}, {'name': 'sched_delayed', 'type': 'ffi::c_uchar'}, {'name': 'rel_deadline', 'type': 'ffi::c_uchar'}, {'name': 'custom_slice', 'type': 'ffi::c_uchar'}, {'name': 'exec_start', 'type': 'u64_'}, {'name': 'sum_exec_runtime', 'type': 'u64_'}, {'name': 'prev_sum_exec_runtime', 'type': 'u64_'}, {'name': 'vruntime', 'type': 'u64_'}, {'name': 'vlag', 'type': 's64'}, {'name': 'slice', 'type': 'u64_'}, {'name': 'nr_migrations', 'type': 'u64_'}, {'name': 'depth', 'type': 'ffi::c_int'}, {'name': 'parent', 'type': '*mut sched_entity'}, {'name': 'cfs_rq', 'type': '*mut cfs_rq'}, {'name': 'my_q', 'type': '*mut cfs_rq'}, {'name': 'runnable_weight', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': 'u64'}, {'name': 'avg', 'type': 'sched_avg'}]`
- New: `[{'name': 'load', 'type': 'load_weight'}, {'name': 'run_node', 'type': 'rb_node'}, {'name': 'deadline', 'type': 'u64_'}, {'name': 'min_vruntime', 'type': 'u64_'}, {'name': 'min_slice', 'type': 'u64_'}, {'name': 'group_node', 'type': 'list_head'}, {'name': 'on_rq', 'type': 'ffi::c_uchar'}, {'name': 'sched_delayed', 'type': 'ffi::c_uchar'}, {'name': 'rel_deadline', 'type': 'ffi::c_uchar'}, {'name': 'custom_slice', 'type': 'ffi::c_uchar'}, {'name': 'exec_start', 'type': 'u64_'}, {'name': 'sum_exec_runtime', 'type': 'u64_'}, {'name': 'prev_sum_exec_runtime', 'type': 'u64_'}, {'name': 'vruntime', 'type': 'u64_'}, {'name': '__bindgen_anon_1', 'type': 'sched_entity__bindgen_ty_1'}, {'name': 'slice', 'type': 'u64_'}, {'name': 'nr_migrations', 'type': 'u64_'}, {'name': 'depth', 'type': 'ffi::c_int'}, {'name': 'parent', 'type': '*mut sched_entity'}, {'name': 'cfs_rq', 'type': '*mut cfs_rq'}, {'name': 'my_q', 'type': '*mut cfs_rq'}, {'name': 'runnable_weight', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': 'u64'}, {'name': 'avg', 'type': 'sched_avg'}]`

### Rust Evidence

- Graph edges: `1`

## W-000921 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: super_block
- Explanation: super_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 's_list', 'type': 'list_head'}, {'name': 's_dev', 'type': 'dev_t'}, {'name': 's_blocksize_bits', 'type': 'ffi::c_uchar'}, {'name': 's_blocksize', 'type': 'ffi::c_ulong'}, {'name': 's_maxbytes', 'type': 'loff_t'}, {'name': 's_type', 'type': '*mut file_system_type'}, {'name': 's_op', 'type': '*const super_operations'}, {'name': 'dq_op', 'type': '*const dquot_operations'}, {'name': 's_qcop', 'type': '*const quotactl_ops'}, {'name': 's_export_op', 'type': '*const export_operations'}, {'name': 's_flags', 'type': 'ffi::c_ulong'}, {'name': 's_iflags', 'type': 'ffi::c_ulong'}, {'name': 's_magic', 'type': 'ffi::c_ulong'}, {'name': 's_root', 'type': '*mut dentry'}, {'name': 's_umount', 'type': 'rw_semaphore'}, {'name': 's_count', 'type': 'ffi::c_int'}, {'name': 's_active', 'type': 'atomic_t'}, {'name': 's_security', 'type': '*mut ffi::c_void'}, {'name': 's_xattr', 'type': '*const *mut xattr_handler'}, {'name': 's_roots', 'type': 'hlist_bl_head'}, {'name': 's_mounts', 'type': 'list_head'}, {'name': 's_bdev', 'type': '*mut block_device'}, {'name': 's_bdev_file', 'type': '*mut file'}, {'name': 's_bdi', 'type': '*mut backing_dev_info'}, {'name': 's_mtd', 'type': '*mut mtd_info'}, {'name': 's_instances', 'type': 'hlist_node'}, {'name': 's_quota_types', 'type': 'ffi::c_uint'}, {'name': 's_dquot', 'type': 'quota_info'}, {'name': 's_writers', 'type': 'sb_writers'}, {'name': 's_fs_info', 'type': '*mut ffi::c_void'}, {'name': 's_time_gran', 'type': 'u32_'}, {'name': 's_time_min', 'type': 'time64_t'}, {'name': 's_time_max', 'type': 'time64_t'}, {'name': 's_fsnotify_mask', 'type': 'u32_'}, {'name': 's_fsnotify_info', 'type': '*mut fsnotify_sb_info'}, {'name': 's_id', 'type': '[ffi::c_char; 32usize]'}, {'name': 's_uuid', 'type': 'uuid_t'}, {'name': 's_uuid_len', 'type': 'u8_'}, {'name': 's_sysfs_name', 'type': '[ffi::c_char; 37usize]'}, {'name': 's_max_links', 'type': 'ffi::c_uint'}, {'name': 's_vfs_rename_mutex', 'type': 'mutex'}, {'name': 's_subtype', 'type': '*const ffi::c_char'}, {'name': 's_d_op', 'type': '*const dentry_operations'}, {'name': 's_shrink', 'type': '*mut shrinker'}, {'name': 's_remove_count', 'type': 'atomic_long_t'}, {'name': 's_readonly_remount', 'type': 'ffi::c_int'}, {'name': 's_wb_err', 'type': 'errseq_t'}, {'name': 's_dio_done_wq', 'type': '*mut workqueue_struct'}, {'name': 's_pins', 'type': 'hlist_head'}, {'name': 's_user_ns', 'type': '*mut user_namespace'}, {'name': 's_dentry_lru', 'type': 'list_lru'}, {'name': 's_inode_lru', 'type': 'list_lru'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 's_sync_lock', 'type': 'mutex'}, {'name': 's_stack_depth', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': '[u32; 15usize]'}, {'name': 's_inode_list_lock', 'type': 'spinlock_t'}, {'name': 's_inodes', 'type': 'list_head'}, {'name': 's_inode_wblist_lock', 'type': 'spinlock_t'}, {'name': 's_inodes_wb', 'type': 'list_head'}]`
- New: `[{'name': 's_list', 'type': 'list_head'}, {'name': 's_dev', 'type': 'dev_t'}, {'name': 's_blocksize_bits', 'type': 'ffi::c_uchar'}, {'name': 's_blocksize', 'type': 'ffi::c_ulong'}, {'name': 's_maxbytes', 'type': 'loff_t'}, {'name': 's_type', 'type': '*mut file_system_type'}, {'name': 's_op', 'type': '*const super_operations'}, {'name': 'dq_op', 'type': '*const dquot_operations'}, {'name': 's_qcop', 'type': '*const quotactl_ops'}, {'name': 's_export_op', 'type': '*const export_operations'}, {'name': 's_flags', 'type': 'ffi::c_ulong'}, {'name': 's_iflags', 'type': 'ffi::c_ulong'}, {'name': 's_magic', 'type': 'ffi::c_ulong'}, {'name': 's_root', 'type': '*mut dentry'}, {'name': 's_umount', 'type': 'rw_semaphore'}, {'name': 's_count', 'type': 'ffi::c_int'}, {'name': 's_active', 'type': 'atomic_t'}, {'name': 's_security', 'type': '*mut ffi::c_void'}, {'name': 's_xattr', 'type': '*const *mut xattr_handler'}, {'name': 's_roots', 'type': 'hlist_bl_head'}, {'name': 's_mounts', 'type': 'list_head'}, {'name': 's_bdev', 'type': '*mut block_device'}, {'name': 's_bdev_file', 'type': '*mut file'}, {'name': 's_bdi', 'type': '*mut backing_dev_info'}, {'name': 's_mtd', 'type': '*mut mtd_info'}, {'name': 's_instances', 'type': 'hlist_node'}, {'name': 's_quota_types', 'type': 'ffi::c_uint'}, {'name': 's_dquot', 'type': 'quota_info'}, {'name': 's_writers', 'type': 'sb_writers'}, {'name': 's_fs_info', 'type': '*mut ffi::c_void'}, {'name': 's_time_gran', 'type': 'u32_'}, {'name': 's_time_min', 'type': 'time64_t'}, {'name': 's_time_max', 'type': 'time64_t'}, {'name': 's_fsnotify_mask', 'type': 'u32_'}, {'name': 's_fsnotify_info', 'type': '*mut fsnotify_sb_info'}, {'name': 's_id', 'type': '[ffi::c_char; 32usize]'}, {'name': 's_uuid', 'type': 'uuid_t'}, {'name': 's_uuid_len', 'type': 'u8_'}, {'name': 's_sysfs_name', 'type': '[ffi::c_char; 37usize]'}, {'name': 's_max_links', 'type': 'ffi::c_uint'}, {'name': 's_d_flags', 'type': 'ffi::c_uint'}, {'name': 's_vfs_rename_mutex', 'type': 'mutex'}, {'name': 's_subtype', 'type': '*const ffi::c_char'}, {'name': '__s_d_op', 'type': '*const dentry_operations'}, {'name': 's_shrink', 'type': '*mut shrinker'}, {'name': 's_remove_count', 'type': 'atomic_long_t'}, {'name': 's_readonly_remount', 'type': 'ffi::c_int'}, {'name': 's_wb_err', 'type': 'errseq_t'}, {'name': 's_dio_done_wq', 'type': '*mut workqueue_struct'}, {'name': 's_pins', 'type': 'hlist_head'}, {'name': 's_user_ns', 'type': '*mut user_namespace'}, {'name': 's_dentry_lru', 'type': 'list_lru'}, {'name': 's_inode_lru', 'type': 'list_lru'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 's_sync_lock', 'type': 'mutex'}, {'name': 's_stack_depth', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': '[u32; 15usize]'}, {'name': 's_inode_list_lock', 'type': 'spinlock_t'}, {'name': 's_inodes', 'type': 'list_head'}, {'name': 's_inode_wblist_lock', 'type': 'spinlock_t'}, {'name': 's_inodes_wb', 'type': 'list_head'}]`

### Rust Evidence

- Graph edges: `1`

## W-000922 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: super_operations
- Explanation: super_operations changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'destroy_inode', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut inode)>'}, {'name': 'free_inode', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut inode)>'}, {'name': 'write_inode', 'type': '::core::option::Option<'}, {'name': 'drop_inode', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut inode) -> ffi::c_int>'}, {'name': 'evict_inode', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut inode)>'}, {'name': 'put_super', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut super_block)>'}, {'name': 'sync_fs', 'type': '::core::option::Option<'}, {'name': 'freeze_super', 'type': '::core::option::Option<'}, {'name': 'thaw_super', 'type': '::core::option::Option<'}, {'name': 'statfs', 'type': '::core::option::Option<'}, {'name': 'remount_fs', 'type': '::core::option::Option<'}, {'name': 'umount_begin', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut super_block)>'}, {'name': 'show_options', 'type': '::core::option::Option<'}, {'name': 'show_devname', 'type': '::core::option::Option<'}, {'name': 'show_path', 'type': '::core::option::Option<'}, {'name': 'show_stats', 'type': '::core::option::Option<'}, {'name': 'quota_read', 'type': '::core::option::Option<'}, {'name': 'quota_write', 'type': '::core::option::Option<'}, {'name': 'nr_cached_objects', 'type': '::core::option::Option<'}, {'name': 'free_cached_objects', 'type': '::core::option::Option<'}, {'name': 'shutdown', 'type': '::core::option::Option<unsafe extern "C" fn(sb: *mut super_block)>'}]`
- New: `[{'name': 'destroy_inode', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut inode)>'}, {'name': 'free_inode', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut inode)>'}, {'name': 'write_inode', 'type': '::core::option::Option<'}, {'name': 'drop_inode', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut inode) -> ffi::c_int>'}, {'name': 'evict_inode', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut inode)>'}, {'name': 'put_super', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut super_block)>'}, {'name': 'sync_fs', 'type': '::core::option::Option<'}, {'name': 'freeze_super', 'type': '::core::option::Option<'}, {'name': 'thaw_super', 'type': '::core::option::Option<'}, {'name': 'statfs', 'type': '::core::option::Option<'}, {'name': 'remount_fs', 'type': '::core::option::Option<'}, {'name': 'umount_begin', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut super_block)>'}, {'name': 'show_options', 'type': '::core::option::Option<'}, {'name': 'show_devname', 'type': '::core::option::Option<'}, {'name': 'show_path', 'type': '::core::option::Option<'}, {'name': 'show_stats', 'type': '::core::option::Option<'}, {'name': 'quota_read', 'type': '::core::option::Option<'}, {'name': 'quota_write', 'type': '::core::option::Option<'}, {'name': 'nr_cached_objects', 'type': '::core::option::Option<'}, {'name': 'free_cached_objects', 'type': '::core::option::Option<'}, {'name': 'remove_bdev', 'type': '::core::option::Option<'}, {'name': 'shutdown', 'type': '::core::option::Option<unsafe extern "C" fn(sb: *mut super_block)>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000923 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: swap_info_struct
- Explanation: swap_info_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'users', 'type': 'percpu_ref'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'prio', 'type': 'ffi::c_short'}, {'name': 'list', 'type': 'plist_node'}, {'name': 'type_', 'type': 'ffi::c_schar'}, {'name': 'max', 'type': 'ffi::c_uint'}, {'name': 'swap_map', 'type': '*mut ffi::c_uchar'}, {'name': 'zeromap', 'type': '*mut ffi::c_ulong'}, {'name': 'cluster_info', 'type': '*mut swap_cluster_info'}, {'name': 'free_clusters', 'type': 'list_head'}, {'name': 'full_clusters', 'type': 'list_head'}, {'name': 'nonfull_clusters', 'type': '[list_head; 1usize]'}, {'name': 'frag_clusters', 'type': '[list_head; 1usize]'}, {'name': 'frag_cluster_nr', 'type': '[atomic_long_t; 1usize]'}, {'name': 'pages', 'type': 'ffi::c_uint'}, {'name': 'inuse_pages', 'type': 'atomic_long_t'}, {'name': 'global_cluster', 'type': '*mut swap_sequential_cluster'}, {'name': 'global_cluster_lock', 'type': 'spinlock_t'}, {'name': 'swap_extent_root', 'type': 'rb_root'}, {'name': 'bdev', 'type': '*mut block_device'}, {'name': 'swap_file', 'type': '*mut file'}, {'name': 'comp', 'type': 'completion'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'cont_lock', 'type': 'spinlock_t'}, {'name': 'discard_work', 'type': 'work_struct'}, {'name': 'reclaim_work', 'type': 'work_struct'}, {'name': 'discard_clusters', 'type': 'list_head'}, {'name': 'avail_lists', 'type': '__IncompleteArrayField<plist_node>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000925 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: wait_page_queue
- Explanation: wait_page_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[{'name': 'folio', 'type': '*mut folio'}, {'name': 'bit_nr', 'type': 'ffi::c_int'}, {'name': 'wait', 'type': 'wait_queue_entry_t'}]`

### Rust Evidence

- Graph edges: `1`

## W-000926 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: writeback_control
- Explanation: writeback_control changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'nr_to_write', 'type': 'ffi::c_long'}, {'name': 'pages_skipped', 'type': 'ffi::c_long'}, {'name': 'range_start', 'type': 'loff_t'}, {'name': 'range_end', 'type': 'loff_t'}, {'name': 'sync_mode', 'type': 'writeback_sync_modes'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'swap_plug', 'type': '*mut *mut swap_iocb'}, {'name': 'list', 'type': '*mut list_head'}, {'name': 'fbatch', 'type': 'folio_batch'}, {'name': 'index', 'type': 'ffi::c_ulong'}, {'name': 'saved_err', 'type': 'ffi::c_int'}]`
- New: `[{'name': 'nr_to_write', 'type': 'ffi::c_long'}, {'name': 'pages_skipped', 'type': 'ffi::c_long'}, {'name': 'range_start', 'type': 'loff_t'}, {'name': 'range_end', 'type': 'loff_t'}, {'name': 'sync_mode', 'type': 'writeback_sync_modes'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'fbatch', 'type': 'folio_batch'}, {'name': 'index', 'type': 'ffi::c_ulong'}, {'name': 'saved_err', 'type': 'ffi::c_int'}]`

### Rust Evidence

- Graph edges: `1`

## W-001046 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: node_stat_item_NR_SHMEM
- Explanation: node_stat_item_NR_SHMEM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `23`
- New: `22`

### Rust Evidence

- Graph edges: `3`

## W-000991 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: cpuhp_state_CPUHP_BP_PREPARE_DYN
- Explanation: cpuhp_state_CPUHP_BP_PREPARE_DYN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `63`
- New: `62`

### Rust Evidence

- Graph edges: `2`

## W-001063 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: req_op_REQ_OP_ZONE_RESET
- Explanation: req_op_REQ_OP_ZONE_RESET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `13`
- New: `15`

### Rust Evidence

- Graph edges: `2`

## W-000927 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ETHTOOL_A_PSE_MAX
- Explanation: ETHTOOL_A_PSE_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `13`
- New: `16`

### Rust Evidence

- Graph edges: `1`

## W-000928 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ETHTOOL_A_RSS_MAX
- Explanation: ETHTOOL_A_RSS_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `7`
- New: `8`

### Rust Evidence

- Graph edges: `1`

## W-000929 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ETHTOOL_MSG_KERNEL_MAX
- Explanation: ETHTOOL_MSG_KERNEL_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `53`

### Rust Evidence

- Graph edges: `1`

## W-000930 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ETHTOOL_MSG_USER_MAX
- Explanation: ETHTOOL_MSG_USER_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `47`
- New: `50`

### Rust Evidence

- Graph edges: `1`

## W-000931 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ETHTOOL_RMON_HIST_MAX
- Explanation: ETHTOOL_RMON_HIST_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `11`

### Rust Evidence

- Graph edges: `1`

## W-000932 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: IA32_NR_syscalls
- Explanation: IA32_NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `468`
- New: `470`

### Rust Evidence

- Graph edges: `1`

## W-000933 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: NR_syscalls
- Explanation: NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `468`
- New: `470`

### Rust Evidence

- Graph edges: `1`

## W-000934 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: QUEUE_FLAG_MAX
- Explanation: QUEUE_FLAG_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `15`
- New: `16`

### Rust Evidence

- Graph edges: `1`

## W-000935 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: SD_NUMA
- Explanation: SD_NUMA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16384`
- New: `8192`

### Rust Evidence

- Graph edges: `1`

## W-000936 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: SRCU_READ_FLAVOR_ALL
- Explanation: SRCU_READ_FLAVOR_ALL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `15`
- New: `11`

### Rust Evidence

- Graph edges: `1`

## W-000937 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: SRCU_READ_FLAVOR_SLOWGP
- Explanation: SRCU_READ_FLAVOR_SLOWGP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `12`
- New: `8`

### Rust Evidence

- Graph edges: `1`

## W-000938 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __ETHTOOL_A_PSE_CNT
- Explanation: __ETHTOOL_A_PSE_CNT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `14`
- New: `17`

### Rust Evidence

- Graph edges: `1`

## W-000939 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __ETHTOOL_A_RSS_CNT
- Explanation: __ETHTOOL_A_RSS_CNT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `9`

### Rust Evidence

- Graph edges: `1`

## W-000940 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __ETHTOOL_MSG_KERNEL_CNT
- Explanation: __ETHTOOL_MSG_KERNEL_CNT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `49`
- New: `54`

### Rust Evidence

- Graph edges: `1`

## W-000941 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __ETHTOOL_MSG_USER_CNT
- Explanation: __ETHTOOL_MSG_USER_CNT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `51`

### Rust Evidence

- Graph edges: `1`

## W-000942 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __NET_IPV6_MAX
- Explanation: __NET_IPV6_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `29`
- New: `30`

### Rust Evidence

- Graph edges: `1`

## W-000943 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __NR_ia32_syscalls
- Explanation: __NR_ia32_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `468`
- New: `470`

### Rust Evidence

- Graph edges: `1`

## W-000944 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __NR_syscalls
- Explanation: __NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `468`
- New: `470`

### Rust Evidence

- Graph edges: `1`

## W-000945 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __SD_FLAG_CNT
- Explanation: __SD_FLAG_CNT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `15`
- New: `14`

### Rust Evidence

- Graph edges: `1`

## W-000946 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __SD_NUMA
- Explanation: __SD_NUMA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `14`
- New: `13`

### Rust Evidence

- Graph edges: `1`

## W-000947 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_cmd___MAX_BPF_CMD
- Explanation: bpf_cmd___MAX_BPF_CMD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `37`
- New: `38`

### Rust Evidence

- Graph edges: `1`

## W-000948 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM64_DEBUG_MONITORS_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM64_DEBUG_MONITORS_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `110`
- New: `109`

### Rust Evidence

- Graph edges: `1`

## W-000949 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARMADA_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARMADA_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `124`
- New: `123`

### Rust Evidence

- Graph edges: `1`

## W-000950 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_EVTSTRM_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_EVTSTRM_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `118`
- New: `117`

### Rust Evidence

- Graph edges: `1`

## W-000951 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `117`
- New: `116`

### Rust Evidence

- Graph edges: `1`

## W-000952 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_CACHE_B15_RAC_DEAD
- Explanation: cpuhp_state_CPUHP_AP_ARM_CACHE_B15_RAC_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `34`
- New: `33`

### Rust Evidence

- Graph edges: `1`

## W-000953 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_GLOBAL_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_GLOBAL_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `119`
- New: `118`

### Rust Evidence

- Graph edges: `1`

## W-000954 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_L2X0_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_L2X0_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `115`
- New: `114`

### Rust Evidence

- Graph edges: `1`

## W-000955 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_MVEBU_COHERENCY
- Explanation: cpuhp_state_CPUHP_AP_ARM_MVEBU_COHERENCY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `104`
- New: `103`

### Rust Evidence

- Graph edges: `1`

## W-000956 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_TWD_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_TWD_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `121`
- New: `120`

### Rust Evidence

- Graph edges: `1`

## W-000957 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_VFP_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_VFP_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `109`
- New: `108`

### Rust Evidence

- Graph edges: `1`

## W-000958 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_CACHECTRL_STARTING
- Explanation: cpuhp_state_CPUHP_AP_CACHECTRL_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `88`
- New: `87`

### Rust Evidence

- Graph edges: `1`

## W-000959 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_CPU_PM_STARTING
- Explanation: cpuhp_state_CPUHP_AP_CPU_PM_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `91`
- New: `90`

### Rust Evidence

- Graph edges: `1`

## W-000960 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_DTPM_CPU_DEAD
- Explanation: cpuhp_state_CPUHP_AP_DTPM_CPU_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `36`
- New: `35`

### Rust Evidence

- Graph edges: `1`

## W-000961 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_EXYNOS4_MCT_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_EXYNOS4_MCT_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `116`
- New: `115`

### Rust Evidence

- Graph edges: `1`

## W-000962 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IDLE_DEAD
- Explanation: cpuhp_state_CPUHP_AP_IDLE_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `86`
- New: `85`

### Rust Evidence

- Graph edges: `1`

## W-000963 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_APPLE_AIC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_APPLE_AIC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `94`
- New: `93`

### Rust Evidence

- Graph edges: `1`

## W-000964 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_ARMADA_XP_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_ARMADA_XP_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `95`
- New: `94`

### Rust Evidence

- Graph edges: `1`

## W-000965 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_AVECINTC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_AVECINTC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `99`
- New: `98`

### Rust Evidence

- Graph edges: `1`

## W-000966 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_BCM2836_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_BCM2836_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `96`
- New: `95`

### Rust Evidence

- Graph edges: `1`

## W-000967 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_EIOINTC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_EIOINTC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `98`
- New: `97`

### Rust Evidence

- Graph edges: `1`

## W-000968 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_GIC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_GIC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `92`
- New: `91`

### Rust Evidence

- Graph edges: `1`

## W-000969 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_HIP04_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_HIP04_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `93`
- New: `92`

### Rust Evidence

- Graph edges: `1`

## W-000970 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_MIPS_GIC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_MIPS_GIC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `97`
- New: `96`

### Rust Evidence

- Graph edges: `1`

## W-000971 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_RISCV_IMSIC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_RISCV_IMSIC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `102`
- New: `101`

### Rust Evidence

- Graph edges: `1`

## W-000972 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_RISCV_SBI_IPI_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_RISCV_SBI_IPI_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `103`
- New: `102`

### Rust Evidence

- Graph edges: `1`

## W-000973 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_SIFIVE_PLIC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_SIFIVE_PLIC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `100`
- New: `99`

### Rust Evidence

- Graph edges: `1`

## W-000974 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_JCORE_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_JCORE_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `120`
- New: `119`

### Rust Evidence

- Graph edges: `1`

## W-000975 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_OFFLINE
- Explanation: cpuhp_state_CPUHP_AP_OFFLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `87`
- New: `86`

### Rust Evidence

- Graph edges: `1`

## W-000976 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_ACPI_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_ACPI_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `112`
- New: `111`

### Rust Evidence

- Graph edges: `1`

## W-000977 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HW_BREAKPOINT_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HW_BREAKPOINT_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `111`
- New: `110`

### Rust Evidence

- Graph edges: `1`

## W-000978 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `113`
- New: `112`

### Rust Evidence

- Graph edges: `1`

## W-000979 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_RISCV_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_RISCV_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `114`
- New: `113`

### Rust Evidence

- Graph edges: `1`

## W-000980 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_IBS_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_IBS_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `107`
- New: `106`

### Rust Evidence

- Graph edges: `1`

## W-000981 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `105`
- New: `104`

### Rust Evidence

- Graph edges: `1`

## W-000982 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `106`
- New: `105`

### Rust Evidence

- Graph edges: `1`

## W-000983 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_XTENSA_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_XTENSA_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `108`
- New: `107`

### Rust Evidence

- Graph edges: `1`

## W-000984 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_QCOM_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_QCOM_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `122`
- New: `121`

### Rust Evidence

- Graph edges: `1`

## W-000985 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_RCUTREE_DYING
- Explanation: cpuhp_state_CPUHP_AP_RCUTREE_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `90`
- New: `89`

### Rust Evidence

- Graph edges: `1`

## W-000986 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_SCHED_STARTING
- Explanation: cpuhp_state_CPUHP_AP_SCHED_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `89`
- New: `88`

### Rust Evidence

- Graph edges: `1`

## W-000987 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_TEGRA_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_TEGRA_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `123`
- New: `122`

### Rust Evidence

- Graph edges: `1`

## W-000988 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_ARM_BL_PREPARE
- Explanation: cpuhp_state_CPUHP_ARM_BL_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `55`
- New: `54`

### Rust Evidence

- Graph edges: `1`

## W-000989 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_ARM_SHMOBILE_SCU_PREPARE
- Explanation: cpuhp_state_CPUHP_ARM_SHMOBILE_SCU_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `51`
- New: `50`

### Rust Evidence

- Graph edges: `1`

## W-000990 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_BP_KICK_AP
- Explanation: cpuhp_state_CPUHP_BP_KICK_AP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `84`
- New: `83`

### Rust Evidence

- Graph edges: `1`

## W-000992 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_BP_PREPARE_DYN_END
- Explanation: cpuhp_state_CPUHP_BP_PREPARE_DYN_END changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `83`
- New: `82`

### Rust Evidence

- Graph edges: `1`

## W-000993 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_BRINGUP_CPU
- Explanation: cpuhp_state_CPUHP_BRINGUP_CPU changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `85`
- New: `84`

### Rust Evidence

- Graph edges: `1`

## W-000994 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_CPUIDLE_COUPLED_PREPARE
- Explanation: cpuhp_state_CPUHP_CPUIDLE_COUPLED_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `46`
- New: `45`

### Rust Evidence

- Graph edges: `1`

## W-000995 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_HRTIMERS_PREPARE
- Explanation: cpuhp_state_CPUHP_HRTIMERS_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `40`
- New: `39`

### Rust Evidence

- Graph edges: `1`

## W-000996 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_IOMMU_IOVA_DEAD
- Explanation: cpuhp_state_CPUHP_IOMMU_IOVA_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `33`
- New: `32`

### Rust Evidence

- Graph edges: `1`

## W-000997 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_KVM_PPC_BOOK3S_PREPARE
- Explanation: cpuhp_state_CPUHP_KVM_PPC_BOOK3S_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `58`
- New: `57`

### Rust Evidence

- Graph edges: `1`

## W-000998 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_MD_RAID5_PREPARE
- Explanation: cpuhp_state_CPUHP_MD_RAID5_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `44`
- New: `43`

### Rust Evidence

- Graph edges: `1`

## W-000999 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_MIPS_SOC_PREPARE
- Explanation: cpuhp_state_CPUHP_MIPS_SOC_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `62`
- New: `61`

### Rust Evidence

- Graph edges: `1`

## W-001000 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_MM_ZSWP_POOL_PREPARE
- Explanation: cpuhp_state_CPUHP_MM_ZSWP_POOL_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `57`
- New: `56`

### Rust Evidence

- Graph edges: `1`

## W-001001 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_NET_IUCV_PREPARE
- Explanation: cpuhp_state_CPUHP_NET_IUCV_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `54`
- New: `53`

### Rust Evidence

- Graph edges: `1`

## W-001002 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_PADATA_DEAD
- Explanation: cpuhp_state_CPUHP_PADATA_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `35`
- New: `34`

### Rust Evidence

- Graph edges: `1`

## W-001003 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_POWERPC_MMU_CTX_PREPARE
- Explanation: cpuhp_state_CPUHP_POWERPC_MMU_CTX_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `47`

### Rust Evidence

- Graph edges: `1`

## W-001004 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_POWERPC_PMAC_PREPARE
- Explanation: cpuhp_state_CPUHP_POWERPC_PMAC_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `47`
- New: `46`

### Rust Evidence

- Graph edges: `1`

## W-001005 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_POWER_NUMA_PREPARE
- Explanation: cpuhp_state_CPUHP_POWER_NUMA_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `39`
- New: `38`

### Rust Evidence

- Graph edges: `1`

## W-001006 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_RANDOM_PREPARE
- Explanation: cpuhp_state_CPUHP_RANDOM_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `37`
- New: `36`

### Rust Evidence

- Graph edges: `1`

## W-001007 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_RCUTREE_PREP
- Explanation: cpuhp_state_CPUHP_RCUTREE_PREP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `45`
- New: `44`

### Rust Evidence

- Graph edges: `1`

## W-001008 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_RELAY_PREPARE
- Explanation: cpuhp_state_CPUHP_RELAY_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `43`
- New: `42`

### Rust Evidence

- Graph edges: `1`

## W-001009 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_SH_SH3X_PREPARE
- Explanation: cpuhp_state_CPUHP_SH_SH3X_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `52`
- New: `51`

### Rust Evidence

- Graph edges: `1`

## W-001010 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_SMPCFD_PREPARE
- Explanation: cpuhp_state_CPUHP_SMPCFD_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `42`
- New: `41`

### Rust Evidence

- Graph edges: `1`

## W-001011 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_TIMERS_PREPARE
- Explanation: cpuhp_state_CPUHP_TIMERS_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `60`
- New: `59`

### Rust Evidence

- Graph edges: `1`

## W-001012 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_TMIGR_PREPARE
- Explanation: cpuhp_state_CPUHP_TMIGR_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `61`
- New: `60`

### Rust Evidence

- Graph edges: `1`

## W-001013 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_TOPOLOGY_PREPARE
- Explanation: cpuhp_state_CPUHP_TOPOLOGY_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `53`
- New: `52`

### Rust Evidence

- Graph edges: `1`

## W-001014 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_TRACE_RB_PREPARE
- Explanation: cpuhp_state_CPUHP_TRACE_RB_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `56`
- New: `55`

### Rust Evidence

- Graph edges: `1`

## W-001015 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_WORKQUEUE_PREP
- Explanation: cpuhp_state_CPUHP_WORKQUEUE_PREP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `38`
- New: `37`

### Rust Evidence

- Graph edges: `1`

## W-001016 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_X2APIC_PREPARE
- Explanation: cpuhp_state_CPUHP_X2APIC_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `41`
- New: `40`

### Rust Evidence

- Graph edges: `1`

## W-001017 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_XEN_EVTCHN_PREPARE
- Explanation: cpuhp_state_CPUHP_XEN_EVTCHN_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `50`
- New: `49`

### Rust Evidence

- Graph edges: `1`

## W-001018 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_XEN_PREPARE
- Explanation: cpuhp_state_CPUHP_XEN_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `49`
- New: `48`

### Rust Evidence

- Graph edges: `1`

## W-001019 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_ZCOMP_PREPARE
- Explanation: cpuhp_state_CPUHP_ZCOMP_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `59`
- New: `58`

### Rust Evidence

- Graph edges: `1`

## W-001020 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: dma_fence_flag_bits_DMA_FENCE_FLAG_ENABLE_SIGNAL_BIT
- Explanation: dma_fence_flag_bits_DMA_FENCE_FLAG_ENABLE_SIGNAL_BIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `2`
- New: `3`

### Rust Evidence

- Graph edges: `1`

## W-001021 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: dma_fence_flag_bits_DMA_FENCE_FLAG_SIGNALED_BIT
- Explanation: dma_fence_flag_bits_DMA_FENCE_FLAG_SIGNALED_BIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0`
- New: `1`

### Rust Evidence

- Graph edges: `1`

## W-001022 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: dma_fence_flag_bits_DMA_FENCE_FLAG_TIMESTAMP_BIT
- Explanation: dma_fence_flag_bits_DMA_FENCE_FLAG_TIMESTAMP_BIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `1`
- New: `2`

### Rust Evidence

- Graph edges: `1`

## W-001023 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: dma_fence_flag_bits_DMA_FENCE_FLAG_USER_BITS
- Explanation: dma_fence_flag_bits_DMA_FENCE_FLAG_USER_BITS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `3`
- New: `4`

### Rust Evidence

- Graph edges: `1`

## W-001024 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_KMEM
- Explanation: memcg_stat_item_MEMCG_KMEM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `52`
- New: `51`

### Rust Evidence

- Graph edges: `1`

## W-001025 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_NR_STAT
- Explanation: memcg_stat_item_MEMCG_NR_STAT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `55`
- New: `54`

### Rust Evidence

- Graph edges: `1`

## W-001026 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_PERCPU_B
- Explanation: memcg_stat_item_MEMCG_PERCPU_B changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `50`
- New: `49`

### Rust Evidence

- Graph edges: `1`

## W-001027 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_SOCK
- Explanation: memcg_stat_item_MEMCG_SOCK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `49`
- New: `48`

### Rust Evidence

- Graph edges: `1`

## W-001028 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_SWAP
- Explanation: memcg_stat_item_MEMCG_SWAP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `47`

### Rust Evidence

- Graph edges: `1`

## W-001029 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_VMALLOC
- Explanation: memcg_stat_item_MEMCG_VMALLOC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `51`
- New: `50`

### Rust Evidence

- Graph edges: `1`

## W-001030 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_ZSWAPPED
- Explanation: memcg_stat_item_MEMCG_ZSWAPPED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `54`
- New: `53`

### Rust Evidence

- Graph edges: `1`

## W-001031 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_ZSWAP_B
- Explanation: memcg_stat_item_MEMCG_ZSWAP_B changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `53`
- New: `52`

### Rust Evidence

- Graph edges: `1`

## W-001032 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: mount_flags_MNT_INTERNAL_FLAGS
- Explanation: mount_flags_MNT_INTERNAL_FLAGS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `125850112`
- New: `58737152`

### Rust Evidence

- Graph edges: `1`

## W-001033 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_ANON_THPS
- Explanation: node_stat_item_NR_ANON_THPS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `28`
- New: `27`

### Rust Evidence

- Graph edges: `1`

## W-001034 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_BALLOON_PAGES
- Explanation: node_stat_item_NR_BALLOON_PAGES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `47`
- New: `46`

### Rust Evidence

- Graph edges: `1`

## W-001035 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_DIRTIED
- Explanation: node_stat_item_NR_DIRTIED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `31`
- New: `30`

### Rust Evidence

- Graph edges: `1`

## W-001036 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_FILE_PMDMAPPED
- Explanation: node_stat_item_NR_FILE_PMDMAPPED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `27`
- New: `26`

### Rust Evidence

- Graph edges: `1`

## W-001037 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_FILE_THPS
- Explanation: node_stat_item_NR_FILE_THPS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `26`
- New: `25`

### Rust Evidence

- Graph edges: `1`

## W-001038 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_FOLL_PIN_ACQUIRED
- Explanation: node_stat_item_NR_FOLL_PIN_ACQUIRED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `35`
- New: `34`

### Rust Evidence

- Graph edges: `1`

## W-001039 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_FOLL_PIN_RELEASED
- Explanation: node_stat_item_NR_FOLL_PIN_RELEASED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `36`
- New: `35`

### Rust Evidence

- Graph edges: `1`

## W-001040 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_HUGETLB
- Explanation: node_stat_item_NR_HUGETLB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `46`
- New: `45`

### Rust Evidence

- Graph edges: `1`

## W-001041 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_IOMMU_PAGES
- Explanation: node_stat_item_NR_IOMMU_PAGES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `40`
- New: `39`

### Rust Evidence

- Graph edges: `1`

## W-001042 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_KERNEL_MISC_RECLAIMABLE
- Explanation: node_stat_item_NR_KERNEL_MISC_RECLAIMABLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `34`
- New: `33`

### Rust Evidence

- Graph edges: `1`

## W-001043 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_KERNEL_STACK_KB
- Explanation: node_stat_item_NR_KERNEL_STACK_KB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `37`
- New: `36`

### Rust Evidence

- Graph edges: `1`

## W-001044 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_PAGETABLE
- Explanation: node_stat_item_NR_PAGETABLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `38`
- New: `37`

### Rust Evidence

- Graph edges: `1`

## W-001045 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_SECONDARY_PAGETABLE
- Explanation: node_stat_item_NR_SECONDARY_PAGETABLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `39`
- New: `38`

### Rust Evidence

- Graph edges: `1`

## W-001047 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_SHMEM_PMDMAPPED
- Explanation: node_stat_item_NR_SHMEM_PMDMAPPED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `25`
- New: `24`

### Rust Evidence

- Graph edges: `1`

## W-001048 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_SHMEM_THPS
- Explanation: node_stat_item_NR_SHMEM_THPS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `24`
- New: `23`

### Rust Evidence

- Graph edges: `1`

## W-001049 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_SWAPCACHE
- Explanation: node_stat_item_NR_SWAPCACHE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `41`
- New: `40`

### Rust Evidence

- Graph edges: `1`

## W-001050 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_THROTTLED_WRITTEN
- Explanation: node_stat_item_NR_THROTTLED_WRITTEN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `33`
- New: `32`

### Rust Evidence

- Graph edges: `1`

## W-001051 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_VMSCAN_IMMEDIATE
- Explanation: node_stat_item_NR_VMSCAN_IMMEDIATE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `30`
- New: `29`

### Rust Evidence

- Graph edges: `1`

## W-001052 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_VMSCAN_WRITE
- Explanation: node_stat_item_NR_VMSCAN_WRITE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `29`
- New: `28`

### Rust Evidence

- Graph edges: `1`

## W-001053 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_VM_NODE_STAT_ITEMS
- Explanation: node_stat_item_NR_VM_NODE_STAT_ITEMS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `47`

### Rust Evidence

- Graph edges: `1`

## W-001054 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_WRITTEN
- Explanation: node_stat_item_NR_WRITTEN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `32`
- New: `31`

### Rust Evidence

- Graph edges: `1`

## W-001055 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_PGDEMOTE_DIRECT
- Explanation: node_stat_item_PGDEMOTE_DIRECT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `43`
- New: `42`

### Rust Evidence

- Graph edges: `1`

## W-001056 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_PGDEMOTE_KHUGEPAGED
- Explanation: node_stat_item_PGDEMOTE_KHUGEPAGED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `44`
- New: `43`

### Rust Evidence

- Graph edges: `1`

## W-001057 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_PGDEMOTE_KSWAPD
- Explanation: node_stat_item_PGDEMOTE_KSWAPD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `42`
- New: `41`

### Rust Evidence

- Graph edges: `1`

## W-001058 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_PGDEMOTE_PROACTIVE
- Explanation: node_stat_item_PGDEMOTE_PROACTIVE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `45`
- New: `44`

### Rust Evidence

- Graph edges: `1`

## W-001059 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: phy_interface_t_PHY_INTERFACE_MODE_MAX
- Explanation: phy_interface_t_PHY_INTERFACE_MODE_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `34`
- New: `38`

### Rust Evidence

- Graph edges: `1`

## W-001060 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: req_flag_bits___REQ_NOUNMAP
- Explanation: req_flag_bits___REQ_NOUNMAP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `28`
- New: `29`

### Rust Evidence

- Graph edges: `1`

## W-001061 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: req_flag_bits___REQ_NR_BITS
- Explanation: req_flag_bits___REQ_NR_BITS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `29`
- New: `30`

### Rust Evidence

- Graph edges: `1`

## W-001062 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: req_op_REQ_OP_ZONE_FINISH
- Explanation: req_op_REQ_OP_ZONE_FINISH changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `12`
- New: `13`

### Rust Evidence

- Graph edges: `1`

## W-001064 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: req_op_REQ_OP_ZONE_RESET_ALL
- Explanation: req_op_REQ_OP_ZONE_RESET_ALL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `15`
- New: `17`

### Rust Evidence

- Graph edges: `1`

## W-001065 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_ARP_PVLAN_DISABLE
- Explanation: skb_drop_reason_SKB_DROP_REASON_ARP_PVLAN_DISABLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `116`
- New: `117`

### Rust Evidence

- Graph edges: `1`

## W-001066 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_BPF_CGROUP_EGRESS
- Explanation: skb_drop_reason_SKB_DROP_REASON_BPF_CGROUP_EGRESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `54`
- New: `55`

### Rust Evidence

- Graph edges: `1`

## W-001067 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_BRIDGE_INGRESS_STP_STATE
- Explanation: skb_drop_reason_SKB_DROP_REASON_BRIDGE_INGRESS_STP_STATE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `118`
- New: `119`

### Rust Evidence

- Graph edges: `1`

## W-001068 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_CAKE_FLOOD
- Explanation: skb_drop_reason_SKB_DROP_REASON_CAKE_FLOOD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `66`
- New: `67`

### Rust Evidence

- Graph edges: `1`

## W-001069 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_CPU_BACKLOG
- Explanation: skb_drop_reason_SKB_DROP_REASON_CPU_BACKLOG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `70`
- New: `71`

### Rust Evidence

- Graph edges: `1`

## W-001070 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_DEV_HDR
- Explanation: skb_drop_reason_SKB_DROP_REASON_DEV_HDR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `77`
- New: `78`

### Rust Evidence

- Graph edges: `1`

## W-001071 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_DEV_READY
- Explanation: skb_drop_reason_SKB_DROP_REASON_DEV_READY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `78`
- New: `79`

### Rust Evidence

- Graph edges: `1`

## W-001072 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_DUP_FRAG
- Explanation: skb_drop_reason_SKB_DROP_REASON_DUP_FRAG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `93`
- New: `94`

### Rust Evidence

- Graph edges: `1`

## W-001073 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FQ_BAND_LIMIT
- Explanation: skb_drop_reason_SKB_DROP_REASON_FQ_BAND_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `67`
- New: `68`

### Rust Evidence

- Graph edges: `1`

## W-001074 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FQ_FLOW_LIMIT
- Explanation: skb_drop_reason_SKB_DROP_REASON_FQ_FLOW_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `69`
- New: `70`

### Rust Evidence

- Graph edges: `1`

## W-001075 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FQ_HORIZON_LIMIT
- Explanation: skb_drop_reason_SKB_DROP_REASON_FQ_HORIZON_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `68`
- New: `69`

### Rust Evidence

- Graph edges: `1`

## W-001076 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FRAG_REASM_TIMEOUT
- Explanation: skb_drop_reason_SKB_DROP_REASON_FRAG_REASM_TIMEOUT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `94`
- New: `95`

### Rust Evidence

- Graph edges: `1`

## W-001077 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FRAG_TOO_FAR
- Explanation: skb_drop_reason_SKB_DROP_REASON_FRAG_TOO_FAR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `95`
- New: `96`

### Rust Evidence

- Graph edges: `1`

## W-001078 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FULL_RING
- Explanation: skb_drop_reason_SKB_DROP_REASON_FULL_RING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `79`
- New: `80`

### Rust Evidence

- Graph edges: `1`

## W-001079 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_HDR_TRUNC
- Explanation: skb_drop_reason_SKB_DROP_REASON_HDR_TRUNC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `81`
- New: `82`

### Rust Evidence

- Graph edges: `1`

## W-001080 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_ICMP_CSUM
- Explanation: skb_drop_reason_SKB_DROP_REASON_ICMP_CSUM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `84`
- New: `85`

### Rust Evidence

- Graph edges: `1`

## W-001081 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_INVALID_PROTO
- Explanation: skb_drop_reason_SKB_DROP_REASON_INVALID_PROTO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `85`
- New: `86`

### Rust Evidence

- Graph edges: `1`

## W-001082 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6DISABLED
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6DISABLED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `55`
- New: `56`

### Rust Evidence

- Graph edges: `1`

## W-001083 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_BAD_EXTHDR
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_BAD_EXTHDR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `97`
- New: `98`

### Rust Evidence

- Graph edges: `1`

## W-001084 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_CODE
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_CODE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `100`
- New: `101`

### Rust Evidence

- Graph edges: `1`

## W-001085 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_OPTIONS
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_OPTIONS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `101`
- New: `102`

### Rust Evidence

- Graph edges: `1`

## W-001086 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_FRAG
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_FRAG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `98`
- New: `99`

### Rust Evidence

- Graph edges: `1`

## W-001087 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_HOP_LIMIT
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_HOP_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `99`
- New: `100`

### Rust Evidence

- Graph edges: `1`

## W-001088 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_NS_OTHERHOST
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_NS_OTHERHOST changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `102`
- New: `103`

### Rust Evidence

- Graph edges: `1`

## W-001089 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INADDRERRORS
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INADDRERRORS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `86`
- New: `87`

### Rust Evidence

- Graph edges: `1`

## W-001090 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INNOROUTES
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INNOROUTES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `87`
- New: `88`

### Rust Evidence

- Graph edges: `1`

## W-001091 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_DEST
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_DEST changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `91`
- New: `92`

### Rust Evidence

- Graph edges: `1`

## W-001092 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_SOURCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_SOURCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `89`
- New: `90`

### Rust Evidence

- Graph edges: `1`

## W-001093 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_LOCALNET
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_LOCALNET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `90`
- New: `91`

### Rust Evidence

- Graph edges: `1`

## W-001094 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_LOCAL_SOURCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_LOCAL_SOURCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `88`
- New: `89`

### Rust Evidence

- Graph edges: `1`

## W-001095 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_OUTNOROUTES
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_OUTNOROUTES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `53`
- New: `54`

### Rust Evidence

- Graph edges: `1`

## W-001096 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_TUNNEL_ECN
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_TUNNEL_ECN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `113`
- New: `114`

### Rust Evidence

- Graph edges: `1`

## W-001097 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_LOCAL_MAC
- Explanation: skb_drop_reason_SKB_DROP_REASON_LOCAL_MAC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `115`
- New: `116`

### Rust Evidence

- Graph edges: `1`

## W-001098 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_MAC_IEEE_MAC_CONTROL
- Explanation: skb_drop_reason_SKB_DROP_REASON_MAC_IEEE_MAC_CONTROL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `117`
- New: `118`

### Rust Evidence

- Graph edges: `1`

## W-001099 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_MAC_INVALID_SOURCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_MAC_INVALID_SOURCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `110`
- New: `111`

### Rust Evidence

- Graph edges: `1`

## W-001100 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_MAX
- Explanation: skb_drop_reason_SKB_DROP_REASON_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `119`
- New: `125`

### Rust Evidence

- Graph edges: `1`

## W-001101 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NEIGH_CREATEFAIL
- Explanation: skb_drop_reason_SKB_DROP_REASON_NEIGH_CREATEFAIL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `56`
- New: `57`

### Rust Evidence

- Graph edges: `1`

## W-001102 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NEIGH_DEAD
- Explanation: skb_drop_reason_SKB_DROP_REASON_NEIGH_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `59`
- New: `60`

### Rust Evidence

- Graph edges: `1`

## W-001103 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NEIGH_FAILED
- Explanation: skb_drop_reason_SKB_DROP_REASON_NEIGH_FAILED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `57`
- New: `58`

### Rust Evidence

- Graph edges: `1`

## W-001104 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NEIGH_HH_FILLFAIL
- Explanation: skb_drop_reason_SKB_DROP_REASON_NEIGH_HH_FILLFAIL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `60`
- New: `61`

### Rust Evidence

- Graph edges: `1`

## W-001105 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NEIGH_QUEUEFULL
- Explanation: skb_drop_reason_SKB_DROP_REASON_NEIGH_QUEUEFULL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `58`
- New: `59`

### Rust Evidence

- Graph edges: `1`

## W-001106 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NOMEM
- Explanation: skb_drop_reason_SKB_DROP_REASON_NOMEM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `80`
- New: `81`

### Rust Evidence

- Graph edges: `1`

## W-001107 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NO_TX_TARGET
- Explanation: skb_drop_reason_SKB_DROP_REASON_NO_TX_TARGET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `112`
- New: `113`

### Rust Evidence

- Graph edges: `1`

## W-001108 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_PACKET_SOCK_ERROR
- Explanation: skb_drop_reason_SKB_DROP_REASON_PACKET_SOCK_ERROR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `105`
- New: `106`

### Rust Evidence

- Graph edges: `1`

## W-001109 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_PKT_TOO_BIG
- Explanation: skb_drop_reason_SKB_DROP_REASON_PKT_TOO_BIG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `92`
- New: `93`

### Rust Evidence

- Graph edges: `1`

## W-001110 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_QDISC_CONGESTED
- Explanation: skb_drop_reason_SKB_DROP_REASON_QDISC_CONGESTED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `65`
- New: `66`

### Rust Evidence

- Graph edges: `1`

## W-001111 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_QDISC_DROP
- Explanation: skb_drop_reason_SKB_DROP_REASON_QDISC_DROP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `63`
- New: `64`

### Rust Evidence

- Graph edges: `1`

## W-001112 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_QDISC_OVERLIMIT
- Explanation: skb_drop_reason_SKB_DROP_REASON_QDISC_OVERLIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `64`
- New: `65`

### Rust Evidence

- Graph edges: `1`

## W-001113 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_QUEUE_PURGE
- Explanation: skb_drop_reason_SKB_DROP_REASON_QUEUE_PURGE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `103`
- New: `104`

### Rust Evidence

- Graph edges: `1`

## W-001114 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SECURITY_HOOK
- Explanation: skb_drop_reason_SKB_DROP_REASON_SECURITY_HOOK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `62`
- New: `63`

### Rust Evidence

- Graph edges: `1`

## W-001115 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SKB_CSUM
- Explanation: skb_drop_reason_SKB_DROP_REASON_SKB_CSUM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `74`
- New: `75`

### Rust Evidence

- Graph edges: `1`

## W-001116 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SKB_GSO_SEG
- Explanation: skb_drop_reason_SKB_DROP_REASON_SKB_GSO_SEG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `75`
- New: `76`

### Rust Evidence

- Graph edges: `1`

## W-001117 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SKB_UCOPY_FAULT
- Explanation: skb_drop_reason_SKB_DROP_REASON_SKB_UCOPY_FAULT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `76`
- New: `77`

### Rust Evidence

- Graph edges: `1`

## W-001118 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TAP_FILTER
- Explanation: skb_drop_reason_SKB_DROP_REASON_TAP_FILTER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `82`
- New: `83`

### Rust Evidence

- Graph edges: `1`

## W-001119 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TAP_TXFILTER
- Explanation: skb_drop_reason_SKB_DROP_REASON_TAP_TXFILTER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `83`
- New: `84`

### Rust Evidence

- Graph edges: `1`

## W-001120 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_ACK_UNSENT_DATA
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_ACK_UNSENT_DATA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `50`
- New: `51`

### Rust Evidence

- Graph edges: `1`

## W-001121 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_CLOSE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_CLOSE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `46`
- New: `47`

### Rust Evidence

- Graph edges: `1`

## W-001122 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_FASTOPEN
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_FASTOPEN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `47`
- New: `48`

### Rust Evidence

- Graph edges: `1`

## W-001123 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_ACK_SEQUENCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_ACK_SEQUENCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `43`
- New: `44`

### Rust Evidence

- Graph edges: `1`

## W-001124 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_SYN
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_SYN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `45`
- New: `46`

### Rust Evidence

- Graph edges: `1`

## W-001125 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_MINTTL
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_MINTTL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `96`
- New: `97`

### Rust Evidence

- Graph edges: `1`

## W-001126 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OFO_DROP
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OFO_DROP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `52`
- New: `53`

### Rust Evidence

- Graph edges: `1`

## W-001127 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OFO_QUEUE_PRUNE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OFO_QUEUE_PRUNE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `51`
- New: `52`

### Rust Evidence

- Graph edges: `1`

## W-001128 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OLD_ACK
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OLD_ACK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `49`

### Rust Evidence

- Graph edges: `1`

## W-001129 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_RESET
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_RESET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `44`
- New: `45`

### Rust Evidence

- Graph edges: `1`

## W-001130 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_TOO_OLD_ACK
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_TOO_OLD_ACK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `49`
- New: `50`

### Rust Evidence

- Graph edges: `1`

## W-001131 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_CHAIN_NOTFOUND
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_CHAIN_NOTFOUND changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `106`
- New: `107`

### Rust Evidence

- Graph edges: `1`

## W-001132 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_COOKIE_ERROR
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_COOKIE_ERROR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `104`
- New: `105`

### Rust Evidence

- Graph edges: `1`

## W-001133 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_EGRESS
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_EGRESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `61`
- New: `62`

### Rust Evidence

- Graph edges: `1`

## W-001134 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_INGRESS
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_INGRESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `72`
- New: `73`

### Rust Evidence

- Graph edges: `1`

## W-001135 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_RECLASSIFY_LOOP
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_RECLASSIFY_LOOP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `107`
- New: `108`

### Rust Evidence

- Graph edges: `1`

## W-001136 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TUNNEL_TXINFO
- Explanation: skb_drop_reason_SKB_DROP_REASON_TUNNEL_TXINFO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `114`
- New: `115`

### Rust Evidence

- Graph edges: `1`

## W-001137 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_UNHANDLED_PROTO
- Explanation: skb_drop_reason_SKB_DROP_REASON_UNHANDLED_PROTO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `73`
- New: `74`

### Rust Evidence

- Graph edges: `1`

## W-001138 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_VXLAN_ENTRY_EXISTS
- Explanation: skb_drop_reason_SKB_DROP_REASON_VXLAN_ENTRY_EXISTS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `111`
- New: `112`

### Rust Evidence

- Graph edges: `1`

## W-001139 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_VXLAN_INVALID_HDR
- Explanation: skb_drop_reason_SKB_DROP_REASON_VXLAN_INVALID_HDR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `108`
- New: `109`

### Rust Evidence

- Graph edges: `1`

## W-001140 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_VXLAN_VNI_NOT_FOUND
- Explanation: skb_drop_reason_SKB_DROP_REASON_VXLAN_VNI_NOT_FOUND changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `109`
- New: `110`

### Rust Evidence

- Graph edges: `1`

## W-001141 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_XDP
- Explanation: skb_drop_reason_SKB_DROP_REASON_XDP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `71`
- New: `72`

### Rust Evidence

- Graph edges: `1`

## W-001151 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ETHTOOL_RMON_HIST_MAX
- Explanation: ETHTOOL_RMON_HIST_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `11`

### Rust Evidence

- Graph edges: `1`

## W-001153 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: USER_HZ
- Explanation: USER_HZ changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `100		/* some user interfaces are */`
- New: `__USER_HZ	/* some user interfaces are */`

### Rust Evidence

- Graph edges: `1`

## W-001142 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: ACPI_PROBE_TABLE
- Explanation: ACPI_PROBE_TABLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: ``
- New: `__##name##_acpi_probe_table`

### Rust Evidence

- Graph edges: `0`

## W-001143 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_32K
- Explanation: CLKID_AO_32K changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `11`
- New: `23`

### Rust Evidence

- Graph edges: `0`

## W-001144 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_32K_DIV
- Explanation: CLKID_AO_32K_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `9`
- New: `21`

### Rust Evidence

- Graph edges: `0`

## W-001145 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_32K_PRE
- Explanation: CLKID_AO_32K_PRE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `20`

### Rust Evidence

- Graph edges: `0`

## W-001146 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_32K_SEL
- Explanation: CLKID_AO_32K_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `22`

### Rust Evidence

- Graph edges: `0`

## W-001147 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_CLK81
- Explanation: CLKID_AO_CLK81 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `13`
- New: `15`

### Rust Evidence

- Graph edges: `0`

## W-001148 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_CTS_OSCIN
- Explanation: CLKID_AO_CTS_OSCIN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `7`
- New: `19`

### Rust Evidence

- Graph edges: `0`

## W-001149 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_CTS_RTC_OSCIN
- Explanation: CLKID_AO_CTS_RTC_OSCIN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `12`
- New: `28`

### Rust Evidence

- Graph edges: `0`

## W-001150 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_UART2
- Explanation: CLKID_AO_UART2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `4`
- New: `6`

### Rust Evidence

- Graph edges: `0`

## W-001152 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: HASH_MAX_DESCSIZE
- Explanation: HASH_MAX_DESCSIZE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `(sizeof(struct shash_desc) + 360)`
- New: `(sizeof(struct shash_desc) + 361)`

### Rust Evidence

- Graph edges: `0`

## W-001154 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: acpi_dev_hid_uid_match
- Explanation: acpi_dev_hid_uid_match changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `\`
- New: `(adev && false)`

### Rust Evidence

- Graph edges: `0`

## W-001155 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: acpi_dev_uid_match
- Explanation: acpi_dev_uid_match changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `\`
- New: `(adev && false)`

### Rust Evidence

- Graph edges: `0`
