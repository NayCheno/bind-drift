# BindDrift Ranked Warnings

## W-000200 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: file
- Explanation: file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'f_ref', 'type': 'file_ref_t'}, {'name': 'f_lock', 'type': 'spinlock_t'}, {'name': 'f_mode', 'type': 'fmode_t'}, {'name': 'f_op', 'type': '*const file_operations'}, {'name': 'f_mapping', 'type': '*mut address_space'}, {'name': 'private_data', 'type': '*mut ffi::c_void'}, {'name': 'f_inode', 'type': '*mut inode'}, {'name': 'f_flags', 'type': 'ffi::c_uint'}, {'name': 'f_iocb_flags', 'type': 'ffi::c_uint'}, {'name': 'f_cred', 'type': '*const cred'}, {'name': 'f_path', 'type': 'path'}, {'name': '__bindgen_anon_1', 'type': 'file__bindgen_ty_1'}, {'name': 'f_pos', 'type': 'loff_t'}, {'name': 'f_security', 'type': '*mut ffi::c_void'}, {'name': 'f_owner', 'type': '*mut fown_struct'}, {'name': 'f_wb_err', 'type': 'errseq_t'}, {'name': 'f_sb_err', 'type': 'errseq_t'}, {'name': 'f_ep', 'type': '*mut hlist_head'}, {'name': '__bindgen_anon_2', 'type': 'file__bindgen_ty_2'}]`
- New: `[{'name': 'f_lock', 'type': 'spinlock_t'}, {'name': 'f_mode', 'type': 'fmode_t'}, {'name': 'f_op', 'type': '*const file_operations'}, {'name': 'f_mapping', 'type': '*mut address_space'}, {'name': 'private_data', 'type': '*mut ffi::c_void'}, {'name': 'f_inode', 'type': '*mut inode'}, {'name': 'f_flags', 'type': 'ffi::c_uint'}, {'name': 'f_iocb_flags', 'type': 'ffi::c_uint'}, {'name': 'f_cred', 'type': '*const cred'}, {'name': 'f_owner', 'type': '*mut fown_struct'}, {'name': 'f_path', 'type': 'path'}, {'name': '__bindgen_anon_1', 'type': 'file__bindgen_ty_1'}, {'name': 'f_pos', 'type': 'loff_t'}, {'name': 'f_security', 'type': '*mut ffi::c_void'}, {'name': 'f_wb_err', 'type': 'errseq_t'}, {'name': 'f_sb_err', 'type': 'errseq_t'}, {'name': 'f_ep', 'type': '*mut hlist_head'}, {'name': '__bindgen_anon_2', 'type': 'file__bindgen_ty_2'}, {'name': 'f_ref', 'type': 'file_ref_t'}]`

### Rust Evidence

- Graph edges: `50`

## W-000201 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: folio
- Explanation: folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'folio__bindgen_ty_1'}, {'name': '__bindgen_anon_2', 'type': 'folio__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'folio__bindgen_ty_3'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'folio__bindgen_ty_1'}, {'name': '__bindgen_anon_2', 'type': 'folio__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'folio__bindgen_ty_3'}, {'name': '__bindgen_anon_4', 'type': 'folio__bindgen_ty_4'}]`

### Rust Evidence

- Graph edges: `29`

## W-000211 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: module
- Explanation: module changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'state', 'type': 'module_state'}, {'name': 'list', 'type': 'list_head'}, {'name': 'name', 'type': '[ffi::c_char; 56usize]'}, {'name': 'mkobj', 'type': 'module_kobject'}, {'name': 'modinfo_attrs', 'type': '*mut module_attribute'}, {'name': 'version', 'type': '*const ffi::c_char'}, {'name': 'srcversion', 'type': '*const ffi::c_char'}, {'name': 'holders_dir', 'type': '*mut kobject'}, {'name': 'syms', 'type': '*mut kernel_symbol'}, {'name': 'crcs', 'type': '*const u32_'}, {'name': 'num_syms', 'type': 'ffi::c_uint'}, {'name': 'param_lock', 'type': 'mutex'}, {'name': 'kp', 'type': '*mut kernel_param'}, {'name': 'num_kp', 'type': 'ffi::c_uint'}, {'name': 'num_gpl_syms', 'type': 'ffi::c_uint'}, {'name': 'gpl_syms', 'type': '*const kernel_symbol'}, {'name': 'gpl_crcs', 'type': '*const u32_'}, {'name': 'using_gplonly_symbols', 'type': 'bool_'}, {'name': 'async_probe_requested', 'type': 'bool_'}, {'name': 'num_exentries', 'type': 'ffi::c_uint'}, {'name': 'extable', 'type': '*mut exception_table_entry'}, {'name': 'init', 'type': '::core::option::Option<unsafe extern "C" fn() -> ffi::c_int>'}, {'name': 'mem', 'type': '[module_memory; 7usize]'}, {'name': 'arch', 'type': 'mod_arch_specific'}, {'name': 'taints', 'type': 'ffi::c_ulong'}, {'name': 'num_bugs', 'type': 'ffi::c_uint'}, {'name': 'bug_list', 'type': 'list_head'}, {'name': 'bug_table', 'type': '*mut bug_entry'}, {'name': 'kallsyms', 'type': '*mut mod_kallsyms'}, {'name': 'core_kallsyms', 'type': 'mod_kallsyms'}, {'name': 'sect_attrs', 'type': '*mut module_sect_attrs'}, {'name': 'notes_attrs', 'type': '*mut module_notes_attrs'}, {'name': 'args', 'type': '*mut ffi::c_char'}, {'name': 'percpu', 'type': '*mut ffi::c_void'}, {'name': 'percpu_size', 'type': 'ffi::c_uint'}, {'name': 'noinstr_text_start', 'type': '*mut ffi::c_void'}, {'name': 'noinstr_text_size', 'type': 'ffi::c_uint'}, {'name': 'num_tracepoints', 'type': 'ffi::c_uint'}, {'name': 'tracepoints_ptrs', 'type': '*const ffi::c_int'}, {'name': 'num_srcu_structs', 'type': 'ffi::c_uint'}, {'name': 'srcu_struct_ptrs', 'type': '*mut *mut srcu_struct'}, {'name': 'jump_entries', 'type': '*mut jump_entry'}, {'name': 'num_jump_entries', 'type': 'ffi::c_uint'}, {'name': 'num_trace_bprintk_fmt', 'type': 'ffi::c_uint'}, {'name': 'trace_bprintk_fmt_start', 'type': '*mut *const ffi::c_char'}, {'name': 'trace_events', 'type': '*mut *mut trace_event_call'}, {'name': 'num_trace_events', 'type': 'ffi::c_uint'}, {'name': 'trace_evals', 'type': '*mut *mut trace_eval_map'}, {'name': 'num_trace_evals', 'type': 'ffi::c_uint'}, {'name': 'kprobes_text_start', 'type': '*mut ffi::c_void'}, {'name': 'kprobes_text_size', 'type': 'ffi::c_uint'}, {'name': 'kprobe_blacklist', 'type': '*mut ffi::c_ulong'}, {'name': 'num_kprobe_blacklist', 'type': 'ffi::c_uint'}, {'name': 'num_static_call_sites', 'type': 'ffi::c_int'}, {'name': 'static_call_sites', 'type': '*mut static_call_site'}, {'name': 'source_list', 'type': 'list_head'}, {'name': 'target_list', 'type': 'list_head'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'refcnt', 'type': 'atomic_t'}]`
- New: `[{'name': 'state', 'type': 'module_state'}, {'name': 'list', 'type': 'list_head'}, {'name': 'name', 'type': '[ffi::c_char; 56usize]'}, {'name': 'mkobj', 'type': 'module_kobject'}, {'name': 'modinfo_attrs', 'type': '*mut module_attribute'}, {'name': 'version', 'type': '*const ffi::c_char'}, {'name': 'srcversion', 'type': '*const ffi::c_char'}, {'name': 'holders_dir', 'type': '*mut kobject'}, {'name': 'syms', 'type': '*mut kernel_symbol'}, {'name': 'crcs', 'type': '*const u32_'}, {'name': 'num_syms', 'type': 'ffi::c_uint'}, {'name': 'param_lock', 'type': 'mutex'}, {'name': 'kp', 'type': '*mut kernel_param'}, {'name': 'num_kp', 'type': 'ffi::c_uint'}, {'name': 'num_gpl_syms', 'type': 'ffi::c_uint'}, {'name': 'gpl_syms', 'type': '*const kernel_symbol'}, {'name': 'gpl_crcs', 'type': '*const u32_'}, {'name': 'using_gplonly_symbols', 'type': 'bool_'}, {'name': 'async_probe_requested', 'type': 'bool_'}, {'name': 'num_exentries', 'type': 'ffi::c_uint'}, {'name': 'extable', 'type': '*mut exception_table_entry'}, {'name': 'init', 'type': '::core::option::Option<unsafe extern "C" fn() -> ffi::c_int>'}, {'name': 'mem', 'type': '[module_memory; 7usize]'}, {'name': 'arch', 'type': 'mod_arch_specific'}, {'name': 'taints', 'type': 'ffi::c_ulong'}, {'name': 'num_bugs', 'type': 'ffi::c_uint'}, {'name': 'bug_list', 'type': 'list_head'}, {'name': 'bug_table', 'type': '*mut bug_entry'}, {'name': 'kallsyms', 'type': '*mut mod_kallsyms'}, {'name': 'core_kallsyms', 'type': 'mod_kallsyms'}, {'name': 'sect_attrs', 'type': '*mut module_sect_attrs'}, {'name': 'notes_attrs', 'type': '*mut module_notes_attrs'}, {'name': 'args', 'type': '*mut ffi::c_char'}, {'name': 'percpu', 'type': '*mut ffi::c_void'}, {'name': 'percpu_size', 'type': 'ffi::c_uint'}, {'name': 'noinstr_text_start', 'type': '*mut ffi::c_void'}, {'name': 'noinstr_text_size', 'type': 'ffi::c_uint'}, {'name': 'num_tracepoints', 'type': 'ffi::c_uint'}, {'name': 'tracepoints_ptrs', 'type': '*const ffi::c_int'}, {'name': 'num_srcu_structs', 'type': 'ffi::c_uint'}, {'name': 'srcu_struct_ptrs', 'type': '*mut *mut srcu_struct'}, {'name': 'jump_entries', 'type': '*mut jump_entry'}, {'name': 'num_jump_entries', 'type': 'ffi::c_uint'}, {'name': 'num_trace_bprintk_fmt', 'type': 'ffi::c_uint'}, {'name': 'trace_bprintk_fmt_start', 'type': '*mut *const ffi::c_char'}, {'name': 'trace_events', 'type': '*mut *mut trace_event_call'}, {'name': 'num_trace_events', 'type': 'ffi::c_uint'}, {'name': 'trace_evals', 'type': '*mut *mut trace_eval_map'}, {'name': 'num_trace_evals', 'type': 'ffi::c_uint'}, {'name': 'kprobes_text_start', 'type': '*mut ffi::c_void'}, {'name': 'kprobes_text_size', 'type': 'ffi::c_uint'}, {'name': 'kprobe_blacklist', 'type': '*mut ffi::c_ulong'}, {'name': 'num_kprobe_blacklist', 'type': 'ffi::c_uint'}, {'name': 'num_static_call_sites', 'type': 'ffi::c_int'}, {'name': 'static_call_sites', 'type': '*mut static_call_site'}, {'name': 'source_list', 'type': 'list_head'}, {'name': 'target_list', 'type': 'list_head'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'refcnt', 'type': 'atomic_t'}, {'name': 'its_num_pages', 'type': 'ffi::c_int'}, {'name': 'its_page_array', 'type': '*mut *mut ffi::c_void'}]`

### Rust Evidence

- Graph edges: `42`

## W-000217 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: pci_dev
- Explanation: pci_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 11usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': 'match_driver', 'type': 'bool_'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 5usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pri_cap', 'type': 'u16_'}, {'name': 'pri_reqs_alloc', 'type': 'u32_'}, {'name': '_bitfield_align_5', 'type': '[u8; 0]'}, {'name': '_bitfield_5', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`
- New: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'rebar_cap', 'type': 'u16_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 11usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': 'match_driver', 'type': 'bool_'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pri_cap', 'type': 'u16_'}, {'name': 'pri_reqs_alloc', 'type': 'u32_'}, {'name': '_bitfield_align_5', 'type': '[u8; 0]'}, {'name': '_bitfield_5', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`

### Rust Evidence

- Graph edges: `50`

## W-000221 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: phy_device
- Explanation: phy_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mdio', 'type': 'mdio_device'}, {'name': 'drv', 'type': '*const phy_driver'}, {'name': 'devlink', 'type': '*mut device_link'}, {'name': 'phyindex', 'type': 'u32_'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'c45_ids', 'type': 'phy_c45_device_ids'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'rate_matching', 'type': 'ffi::c_int'}, {'name': 'state', 'type': 'phy_state'}, {'name': 'dev_flags', 'type': 'u32_'}, {'name': 'interface', 'type': 'phy_interface_t'}, {'name': 'possible_interfaces', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'speed', 'type': 'ffi::c_int'}, {'name': 'duplex', 'type': 'ffi::c_int'}, {'name': 'port', 'type': 'ffi::c_int'}, {'name': 'pause', 'type': 'ffi::c_int'}, {'name': 'asym_pause', 'type': 'ffi::c_int'}, {'name': 'master_slave_get', 'type': 'u8_'}, {'name': 'master_slave_set', 'type': 'u8_'}, {'name': 'master_slave_state', 'type': 'u8_'}, {'name': 'supported', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'advertising', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'lp_advertising', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'adv_old', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'supported_eee', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'advertising_eee', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'eee_broken_modes', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'enable_tx_lpi', 'type': 'bool_'}, {'name': 'eee_active', 'type': 'bool_'}, {'name': 'eee_cfg', 'type': 'eee_config'}, {'name': 'host_interfaces', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'leds', 'type': 'list_head'}, {'name': 'irq', 'type': 'ffi::c_int'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'shared', 'type': '*mut phy_package_shared'}, {'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'ehdr', 'type': '*mut ffi::c_void'}, {'name': 'nest', 'type': '*mut nlattr'}, {'name': 'state_queue', 'type': 'delayed_work'}, {'name': 'lock', 'type': 'mutex'}, {'name': 'sfp_bus_attached', 'type': 'bool_'}, {'name': 'sfp_bus', 'type': '*mut sfp_bus'}, {'name': 'phylink', 'type': '*mut phylink'}, {'name': 'attached_dev', 'type': '*mut net_device'}, {'name': 'mii_ts', 'type': '*mut mii_timestamper'}, {'name': 'psec', 'type': '*mut pse_control'}, {'name': 'mdix', 'type': 'u8_'}, {'name': 'mdix_ctrl', 'type': 'u8_'}, {'name': 'pma_extable', 'type': 'ffi::c_int'}, {'name': 'link_down_events', 'type': 'ffi::c_uint'}, {'name': 'adjust_link', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut net_device)>'}]`
- New: `[{'name': 'mdio', 'type': 'mdio_device'}, {'name': 'drv', 'type': '*const phy_driver'}, {'name': 'devlink', 'type': '*mut device_link'}, {'name': 'phyindex', 'type': 'u32_'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'c45_ids', 'type': 'phy_c45_device_ids'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'rate_matching', 'type': 'ffi::c_int'}, {'name': 'state', 'type': 'phy_state'}, {'name': 'dev_flags', 'type': 'u32_'}, {'name': 'interface', 'type': 'phy_interface_t'}, {'name': 'possible_interfaces', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'speed', 'type': 'ffi::c_int'}, {'name': 'duplex', 'type': 'ffi::c_int'}, {'name': 'port', 'type': 'ffi::c_int'}, {'name': 'pause', 'type': 'ffi::c_int'}, {'name': 'asym_pause', 'type': 'ffi::c_int'}, {'name': 'master_slave_get', 'type': 'u8_'}, {'name': 'master_slave_set', 'type': 'u8_'}, {'name': 'master_slave_state', 'type': 'u8_'}, {'name': 'supported', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'advertising', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'lp_advertising', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'adv_old', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'supported_eee', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'advertising_eee', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'eee_disabled_modes', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'enable_tx_lpi', 'type': 'bool_'}, {'name': 'eee_active', 'type': 'bool_'}, {'name': 'eee_cfg', 'type': 'eee_config'}, {'name': 'host_interfaces', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'leds', 'type': 'list_head'}, {'name': 'irq', 'type': 'ffi::c_int'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'shared', 'type': '*mut phy_package_shared'}, {'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'ehdr', 'type': '*mut ffi::c_void'}, {'name': 'nest', 'type': '*mut nlattr'}, {'name': 'state_queue', 'type': 'delayed_work'}, {'name': 'lock', 'type': 'mutex'}, {'name': 'sfp_bus_attached', 'type': 'bool_'}, {'name': 'sfp_bus', 'type': '*mut sfp_bus'}, {'name': 'phylink', 'type': '*mut phylink'}, {'name': 'attached_dev', 'type': '*mut net_device'}, {'name': 'mii_ts', 'type': '*mut mii_timestamper'}, {'name': 'psec', 'type': '*mut pse_control'}, {'name': 'mdix', 'type': 'u8_'}, {'name': 'mdix_ctrl', 'type': 'u8_'}, {'name': 'pma_extable', 'type': 'ffi::c_int'}, {'name': 'link_down_events', 'type': 'ffi::c_uint'}, {'name': 'adjust_link', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut net_device)>'}]`

### Rust Evidence

- Graph edges: `50`

## W-000237 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: zone
- Explanation: zone changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_watermark', 'type': '[ffi::c_ulong; 4usize]'}, {'name': 'watermark_boost', 'type': 'ffi::c_ulong'}, {'name': 'nr_reserved_highatomic', 'type': 'ffi::c_ulong'}, {'name': 'nr_free_highatomic', 'type': 'ffi::c_ulong'}, {'name': 'lowmem_reserve', 'type': '[ffi::c_long; 4usize]'}, {'name': 'node', 'type': 'ffi::c_int'}, {'name': 'zone_pgdat', 'type': '*mut pglist_data'}, {'name': 'per_cpu_pageset', 'type': '*mut per_cpu_pages'}, {'name': 'per_cpu_zonestats', 'type': '*mut per_cpu_zonestat'}, {'name': 'pageset_high_min', 'type': 'ffi::c_int'}, {'name': 'pageset_high_max', 'type': 'ffi::c_int'}, {'name': 'pageset_batch', 'type': 'ffi::c_int'}, {'name': 'zone_start_pfn', 'type': 'ffi::c_ulong'}, {'name': 'managed_pages', 'type': 'atomic_long_t'}, {'name': 'spanned_pages', 'type': 'ffi::c_ulong'}, {'name': 'present_pages', 'type': 'ffi::c_ulong'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'initialized', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': 'u64'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': 'free_area', 'type': '[free_area; 11usize]'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': '__bindgen_padding_1', 'type': '[u64; 3usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'percpu_drift_mark', 'type': 'ffi::c_ulong'}, {'name': 'compact_cached_free_pfn', 'type': 'ffi::c_ulong'}, {'name': 'compact_cached_migrate_pfn', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'compact_init_migrate_pfn', 'type': 'ffi::c_ulong'}, {'name': 'compact_init_free_pfn', 'type': 'ffi::c_ulong'}, {'name': 'compact_considered', 'type': 'ffi::c_uint'}, {'name': 'compact_defer_shift', 'type': 'ffi::c_uint'}, {'name': 'compact_order_failed', 'type': 'ffi::c_int'}, {'name': 'compact_blockskip_flush', 'type': 'bool_'}, {'name': 'contiguous', 'type': 'bool_'}, {'name': '__bindgen_padding_2', 'type': '[u64; 0usize]'}, {'name': '_pad3_', 'type': 'cacheline_padding'}, {'name': 'vm_stat', 'type': '[atomic_long_t; 10usize]'}, {'name': 'vm_numa_event', 'type': '[atomic_long_t; 6usize]'}]`
- New: `[{'name': '_watermark', 'type': '[ffi::c_ulong; 4usize]'}, {'name': 'watermark_boost', 'type': 'ffi::c_ulong'}, {'name': 'nr_reserved_highatomic', 'type': 'ffi::c_ulong'}, {'name': 'nr_free_highatomic', 'type': 'ffi::c_ulong'}, {'name': 'lowmem_reserve', 'type': '[ffi::c_long; 4usize]'}, {'name': 'node', 'type': 'ffi::c_int'}, {'name': 'zone_pgdat', 'type': '*mut pglist_data'}, {'name': 'per_cpu_pageset', 'type': '*mut per_cpu_pages'}, {'name': 'per_cpu_zonestats', 'type': '*mut per_cpu_zonestat'}, {'name': 'pageset_high_min', 'type': 'ffi::c_int'}, {'name': 'pageset_high_max', 'type': 'ffi::c_int'}, {'name': 'pageset_batch', 'type': 'ffi::c_int'}, {'name': 'zone_start_pfn', 'type': 'ffi::c_ulong'}, {'name': 'managed_pages', 'type': 'atomic_long_t'}, {'name': 'spanned_pages', 'type': 'ffi::c_ulong'}, {'name': 'present_pages', 'type': 'ffi::c_ulong'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'initialized', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': 'u64'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': 'free_area', 'type': '[free_area; 11usize]'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'trylock_free_pages', 'type': 'llist_head'}, {'name': '__bindgen_padding_1', 'type': '[u64; 2usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'percpu_drift_mark', 'type': 'ffi::c_ulong'}, {'name': 'compact_cached_free_pfn', 'type': 'ffi::c_ulong'}, {'name': 'compact_cached_migrate_pfn', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'compact_init_migrate_pfn', 'type': 'ffi::c_ulong'}, {'name': 'compact_init_free_pfn', 'type': 'ffi::c_ulong'}, {'name': 'compact_considered', 'type': 'ffi::c_uint'}, {'name': 'compact_defer_shift', 'type': 'ffi::c_uint'}, {'name': 'compact_order_failed', 'type': 'ffi::c_int'}, {'name': 'compact_blockskip_flush', 'type': 'bool_'}, {'name': 'contiguous', 'type': 'bool_'}, {'name': '__bindgen_padding_2', 'type': '[u64; 0usize]'}, {'name': '_pad3_', 'type': 'cacheline_padding'}, {'name': 'vm_stat', 'type': '[atomic_long_t; 11usize]'}, {'name': 'vm_numa_event', 'type': '[atomic_long_t; 6usize]'}]`

### Rust Evidence

- Graph edges: `38`

## W-000610 NullabilityDrift

- Risk: High
- Score: 12.6
- Symbol: dma_alloc_attrs
- Explanation: dma_alloc_attrs has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.15/include/linux/dma-mapping.h:192 `return NULL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.15/rust/kernel/dma.rs:171 `test` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.15/rust/kernel/dma.rs:169 `// SAFETY: Device pointer is guaranteed as valid by the type invariant on `Device`.`

## W-000230 FieldDrift

- Risk: High
- Score: 12.4
- Symbol: taskstats
- Explanation: taskstats changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'version', 'type': '__u16'}, {'name': 'ac_exitcode', 'type': '__u32'}, {'name': 'ac_flag', 'type': '__u8'}, {'name': 'ac_nice', 'type': '__u8'}, {'name': 'cpu_count', 'type': '__u64'}, {'name': 'cpu_delay_total', 'type': '__u64'}, {'name': 'cpu_delay_max', 'type': '__u64'}, {'name': 'cpu_delay_min', 'type': '__u64'}, {'name': 'blkio_count', 'type': '__u64'}, {'name': 'blkio_delay_total', 'type': '__u64'}, {'name': 'blkio_delay_max', 'type': '__u64'}, {'name': 'blkio_delay_min', 'type': '__u64'}, {'name': 'swapin_count', 'type': '__u64'}, {'name': 'swapin_delay_total', 'type': '__u64'}, {'name': 'swapin_delay_max', 'type': '__u64'}, {'name': 'swapin_delay_min', 'type': '__u64'}, {'name': 'cpu_run_real_total', 'type': '__u64'}, {'name': 'cpu_run_virtual_total', 'type': '__u64'}, {'name': 'ac_comm', 'type': '[ffi::c_char; 32usize]'}, {'name': 'ac_sched', 'type': '__u8'}, {'name': 'ac_pad', 'type': '[__u8; 3usize]'}, {'name': '__bindgen_padding_0', 'type': 'u32'}, {'name': 'ac_uid', 'type': '__u32'}, {'name': 'ac_gid', 'type': '__u32'}, {'name': 'ac_pid', 'type': '__u32'}, {'name': 'ac_ppid', 'type': '__u32'}, {'name': 'ac_btime', 'type': '__u32'}, {'name': 'ac_etime', 'type': '__u64'}, {'name': 'ac_utime', 'type': '__u64'}, {'name': 'ac_stime', 'type': '__u64'}, {'name': 'ac_minflt', 'type': '__u64'}, {'name': 'ac_majflt', 'type': '__u64'}, {'name': 'coremem', 'type': '__u64'}, {'name': 'virtmem', 'type': '__u64'}, {'name': 'hiwater_rss', 'type': '__u64'}, {'name': 'hiwater_vm', 'type': '__u64'}, {'name': 'read_char', 'type': '__u64'}, {'name': 'write_char', 'type': '__u64'}, {'name': 'read_syscalls', 'type': '__u64'}, {'name': 'write_syscalls', 'type': '__u64'}, {'name': 'read_bytes', 'type': '__u64'}, {'name': 'write_bytes', 'type': '__u64'}, {'name': 'cancelled_write_bytes', 'type': '__u64'}, {'name': 'nvcsw', 'type': '__u64'}, {'name': 'nivcsw', 'type': '__u64'}, {'name': 'ac_utimescaled', 'type': '__u64'}, {'name': 'ac_stimescaled', 'type': '__u64'}, {'name': 'cpu_scaled_run_real_total', 'type': '__u64'}, {'name': 'freepages_count', 'type': '__u64'}, {'name': 'freepages_delay_total', 'type': '__u64'}, {'name': 'freepages_delay_max', 'type': '__u64'}, {'name': 'freepages_delay_min', 'type': '__u64'}, {'name': 'thrashing_count', 'type': '__u64'}, {'name': 'thrashing_delay_total', 'type': '__u64'}, {'name': 'thrashing_delay_max', 'type': '__u64'}, {'name': 'thrashing_delay_min', 'type': '__u64'}, {'name': 'ac_btime64', 'type': '__u64'}, {'name': 'compact_count', 'type': '__u64'}, {'name': 'compact_delay_total', 'type': '__u64'}, {'name': 'compact_delay_max', 'type': '__u64'}, {'name': 'compact_delay_min', 'type': '__u64'}, {'name': 'ac_tgid', 'type': '__u32'}, {'name': 'ac_tgetime', 'type': '__u64'}, {'name': 'ac_exe_dev', 'type': '__u64'}, {'name': 'ac_exe_inode', 'type': '__u64'}, {'name': 'wpcopy_count', 'type': '__u64'}, {'name': 'wpcopy_delay_total', 'type': '__u64'}, {'name': 'wpcopy_delay_max', 'type': '__u64'}, {'name': 'wpcopy_delay_min', 'type': '__u64'}, {'name': 'irq_count', 'type': '__u64'}, {'name': 'irq_delay_total', 'type': '__u64'}, {'name': 'irq_delay_max', 'type': '__u64'}, {'name': 'irq_delay_min', 'type': '__u64'}]`
- New: `[{'name': 'version', 'type': '__u16'}, {'name': 'ac_exitcode', 'type': '__u32'}, {'name': 'ac_flag', 'type': '__u8'}, {'name': 'ac_nice', 'type': '__u8'}, {'name': 'cpu_count', 'type': '__u64'}, {'name': 'cpu_delay_total', 'type': '__u64'}, {'name': 'blkio_count', 'type': '__u64'}, {'name': 'blkio_delay_total', 'type': '__u64'}, {'name': 'swapin_count', 'type': '__u64'}, {'name': 'swapin_delay_total', 'type': '__u64'}, {'name': 'cpu_run_real_total', 'type': '__u64'}, {'name': 'cpu_run_virtual_total', 'type': '__u64'}, {'name': 'ac_comm', 'type': '[ffi::c_char; 32usize]'}, {'name': 'ac_sched', 'type': '__u8'}, {'name': 'ac_pad', 'type': '[__u8; 3usize]'}, {'name': '__bindgen_padding_0', 'type': 'u32'}, {'name': 'ac_uid', 'type': '__u32'}, {'name': 'ac_gid', 'type': '__u32'}, {'name': 'ac_pid', 'type': '__u32'}, {'name': 'ac_ppid', 'type': '__u32'}, {'name': 'ac_btime', 'type': '__u32'}, {'name': 'ac_etime', 'type': '__u64'}, {'name': 'ac_utime', 'type': '__u64'}, {'name': 'ac_stime', 'type': '__u64'}, {'name': 'ac_minflt', 'type': '__u64'}, {'name': 'ac_majflt', 'type': '__u64'}, {'name': 'coremem', 'type': '__u64'}, {'name': 'virtmem', 'type': '__u64'}, {'name': 'hiwater_rss', 'type': '__u64'}, {'name': 'hiwater_vm', 'type': '__u64'}, {'name': 'read_char', 'type': '__u64'}, {'name': 'write_char', 'type': '__u64'}, {'name': 'read_syscalls', 'type': '__u64'}, {'name': 'write_syscalls', 'type': '__u64'}, {'name': 'read_bytes', 'type': '__u64'}, {'name': 'write_bytes', 'type': '__u64'}, {'name': 'cancelled_write_bytes', 'type': '__u64'}, {'name': 'nvcsw', 'type': '__u64'}, {'name': 'nivcsw', 'type': '__u64'}, {'name': 'ac_utimescaled', 'type': '__u64'}, {'name': 'ac_stimescaled', 'type': '__u64'}, {'name': 'cpu_scaled_run_real_total', 'type': '__u64'}, {'name': 'freepages_count', 'type': '__u64'}, {'name': 'freepages_delay_total', 'type': '__u64'}, {'name': 'thrashing_count', 'type': '__u64'}, {'name': 'thrashing_delay_total', 'type': '__u64'}, {'name': 'ac_btime64', 'type': '__u64'}, {'name': 'compact_count', 'type': '__u64'}, {'name': 'compact_delay_total', 'type': '__u64'}, {'name': 'ac_tgid', 'type': '__u32'}, {'name': 'ac_tgetime', 'type': '__u64'}, {'name': 'ac_exe_dev', 'type': '__u64'}, {'name': 'ac_exe_inode', 'type': '__u64'}, {'name': 'wpcopy_count', 'type': '__u64'}, {'name': 'wpcopy_delay_total', 'type': '__u64'}, {'name': 'irq_count', 'type': '__u64'}, {'name': 'irq_delay_total', 'type': '__u64'}, {'name': 'cpu_delay_max', 'type': '__u64'}, {'name': 'cpu_delay_min', 'type': '__u64'}, {'name': 'blkio_delay_max', 'type': '__u64'}, {'name': 'blkio_delay_min', 'type': '__u64'}, {'name': 'swapin_delay_max', 'type': '__u64'}, {'name': 'swapin_delay_min', 'type': '__u64'}, {'name': 'freepages_delay_max', 'type': '__u64'}, {'name': 'freepages_delay_min', 'type': '__u64'}, {'name': 'thrashing_delay_max', 'type': '__u64'}, {'name': 'thrashing_delay_min', 'type': '__u64'}, {'name': 'compact_delay_max', 'type': '__u64'}, {'name': 'compact_delay_min', 'type': '__u64'}, {'name': 'wpcopy_delay_max', 'type': '__u64'}, {'name': 'wpcopy_delay_min', 'type': '__u64'}, {'name': 'irq_delay_max', 'type': '__u64'}, {'name': 'irq_delay_min', 'type': '__u64'}]`

### Rust Evidence

- Graph edges: `19`

## W-000569 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: kmap_local_page
- Explanation: kmap_local_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['scatterwalk_page(walk)) + offset_in_page(walk->offset'], 'return_type': 'return'}`
- New: `{'params': ['page'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `8`

## W-000100 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: lockdep_unregister_key
- Explanation: lockdep_unregister_key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000198 FieldDrift

- Risk: High
- Score: 12.0
- Symbol: cgroup_subsys
- Explanation: cgroup_subsys changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'css_alloc', 'type': '::core::option::Option<'}, {'name': 'css_offline', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_released', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_free', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_reset', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_rstat_flush', 'type': '::core::option::Option<'}, {'name': 'css_extra_stat_show', 'type': '::core::option::Option<'}, {'name': 'css_local_stat_show', 'type': '::core::option::Option<'}, {'name': 'cancel_attach', 'type': '::core::option::Option<unsafe extern "C" fn(tset: *mut cgroup_taskset)>'}, {'name': 'attach', 'type': '::core::option::Option<unsafe extern "C" fn(tset: *mut cgroup_taskset)>'}, {'name': 'post_attach', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'can_fork', 'type': '::core::option::Option<'}, {'name': 'fork', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'bind', 'type': '::core::option::Option<unsafe extern "C" fn(root_css: *mut cgroup_subsys_state)>'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'legacy_name', 'type': '*const ffi::c_char'}, {'name': 'root', 'type': '*mut cgroup_root'}, {'name': 'css_idr', 'type': 'idr'}, {'name': 'cfts', 'type': 'list_head'}, {'name': 'dfl_cftypes', 'type': '*mut cftype'}, {'name': 'legacy_cftypes', 'type': '*mut cftype'}, {'name': 'depends_on', 'type': 'ffi::c_uint'}]`
- New: `[{'name': 'css_alloc', 'type': '::core::option::Option<'}, {'name': 'css_offline', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_released', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_free', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_reset', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_killed', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_rstat_flush', 'type': '::core::option::Option<'}, {'name': 'css_extra_stat_show', 'type': '::core::option::Option<'}, {'name': 'css_local_stat_show', 'type': '::core::option::Option<'}, {'name': 'cancel_attach', 'type': '::core::option::Option<unsafe extern "C" fn(tset: *mut cgroup_taskset)>'}, {'name': 'attach', 'type': '::core::option::Option<unsafe extern "C" fn(tset: *mut cgroup_taskset)>'}, {'name': 'post_attach', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'can_fork', 'type': '::core::option::Option<'}, {'name': 'fork', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'bind', 'type': '::core::option::Option<unsafe extern "C" fn(root_css: *mut cgroup_subsys_state)>'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'legacy_name', 'type': '*const ffi::c_char'}, {'name': 'root', 'type': '*mut cgroup_root'}, {'name': 'css_idr', 'type': 'idr'}, {'name': 'cfts', 'type': 'list_head'}, {'name': 'dfl_cftypes', 'type': '*mut cftype'}, {'name': 'legacy_cftypes', 'type': '*mut cftype'}, {'name': 'depends_on', 'type': 'ffi::c_uint'}]`

### Rust Evidence

- Graph edges: `17`

## W-000208 FieldDrift

- Risk: High
- Score: 12.0
- Symbol: kernfs_node
- Explanation: kernfs_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'count', 'type': 'atomic_t'}, {'name': 'active', 'type': 'atomic_t'}, {'name': 'parent', 'type': '*mut kernfs_node'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'rb', 'type': 'rb_node'}, {'name': 'ns', 'type': '*const ffi::c_void'}, {'name': 'hash', 'type': 'ffi::c_uint'}, {'name': 'flags', 'type': 'ffi::c_ushort'}, {'name': 'mode', 'type': 'umode_t'}, {'name': '__bindgen_anon_1', 'type': 'kernfs_node__bindgen_ty_1'}, {'name': 'id', 'type': 'u64_'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'iattr', 'type': '*mut kernfs_iattrs'}, {'name': 'rcu', 'type': 'callback_head'}]`
- New: `[{'name': 'count', 'type': 'atomic_t'}, {'name': 'active', 'type': 'atomic_t'}, {'name': '__parent', 'type': '*mut kernfs_node'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'rb', 'type': 'rb_node'}, {'name': 'ns', 'type': '*const ffi::c_void'}, {'name': 'hash', 'type': 'ffi::c_uint'}, {'name': 'flags', 'type': 'ffi::c_ushort'}, {'name': 'mode', 'type': 'umode_t'}, {'name': '__bindgen_anon_1', 'type': 'kernfs_node__bindgen_ty_1'}, {'name': 'id', 'type': 'u64_'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'iattr', 'type': '*mut kernfs_iattrs'}, {'name': 'rcu', 'type': 'callback_head'}]`

### Rust Evidence

- Graph edges: `17`

## W-000570 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: mdiobus_read
- Explanation: mdiobus_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['phydev->mdio.bus', 'addr', 'regnum'], 'return_type': 'return'}`
- New: `{'params': ['phydev->mdio.bus', 'phydev->mdio.addr', 'regnum'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `6`

## W-000571 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: mdiobus_write
- Explanation: mdiobus_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['phydev->mdio.bus', 'addr', 'regnum', 'val'], 'return_type': 'return'}`
- New: `{'params': ['phydev->mdio.bus', 'phydev->mdio.addr', 'regnum', 'val'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `6`

## W-000099 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: lockdep_register_key
- Explanation: lockdep_register_key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000229 FieldDrift

- Risk: High
- Score: 11.6
- Symbol: task_struct
- Explanation: task_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'ffi::c_uint'}, {'name': 'saved_state', 'type': 'ffi::c_uint'}, {'name': 'stack', 'type': '*mut ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'ptrace', 'type': 'ffi::c_uint'}, {'name': 'on_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_cpu', 'type': 'ffi::c_int'}, {'name': 'on_rq', 'type': 'ffi::c_int'}, {'name': 'prio', 'type': 'ffi::c_int'}, {'name': 'static_prio', 'type': 'ffi::c_int'}, {'name': 'normal_prio', 'type': 'ffi::c_int'}, {'name': 'rt_priority', 'type': 'ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'dl_server', 'type': '*mut sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'ffi::c_uint'}, {'name': 'policy', 'type': 'ffi::c_uint'}, {'name': 'max_allowed_capacity', 'type': 'ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut ffi::c_void'}, {'name': 'migration_disabled', 'type': 'ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'rcu_tasks_exit_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_exit_list', 'type': 'list_head'}, {'name': 'trc_reader_nesting', 'type': 'ffi::c_int'}, {'name': 'trc_ipi_to_cpu', 'type': 'ffi::c_int'}, {'name': 'trc_reader_special', 'type': 'rcu_special'}, {'name': 'trc_holdout_list', 'type': 'list_head'}, {'name': 'trc_blkd_node', 'type': 'list_head'}, {'name': 'trc_blkd_cpu', 'type': 'ffi::c_int'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'faults_disabled_mapping', 'type': '*mut address_space'}, {'name': 'exit_state', 'type': 'ffi::c_int'}, {'name': 'exit_code', 'type': 'ffi::c_int'}, {'name': 'exit_signal', 'type': 'ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'ffi::c_int'}, {'name': 'jobctl', 'type': 'ffi::c_ulong'}, {'name': 'personality', 'type': 'ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'worker_private', 'type': '*mut ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'journal_info', 'type': '*mut ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'ffi::c_uint'}, {'name': 'perf_recursion', 'type': '[u8_; 4usize]'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'ffi::c_short'}, {'name': 'il_weight', 'type': 'u8_'}, {'name': 'pref_node_fork', 'type': 'ffi::c_short'}, {'name': 'rseq', 'type': '*mut rseq'}, {'name': 'rseq_len', 'type': 'u32_'}, {'name': 'rseq_sig', 'type': 'u32_'}, {'name': 'rseq_event_mask', 'type': 'ffi::c_ulong'}, {'name': 'mm_cid', 'type': 'ffi::c_int'}, {'name': 'last_mm_cid', 'type': 'ffi::c_int'}, {'name': 'migrate_from_cpu', 'type': 'ffi::c_int'}, {'name': 'mm_cid_active', 'type': 'ffi::c_int'}, {'name': 'cid_work', 'type': 'callback_head'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'bpf_net_context', 'type': '*mut bpf_net_context'}, {'name': 'mce_vaddr', 'type': '*mut ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': '__bindgen_padding_1', 'type': '[u64; 5usize]'}, {'name': 'thread', 'type': 'thread_struct'}]`
- New: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'ffi::c_uint'}, {'name': 'saved_state', 'type': 'ffi::c_uint'}, {'name': 'stack', 'type': '*mut ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'ptrace', 'type': 'ffi::c_uint'}, {'name': 'on_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_cpu', 'type': 'ffi::c_int'}, {'name': 'on_rq', 'type': 'ffi::c_int'}, {'name': 'prio', 'type': 'ffi::c_int'}, {'name': 'static_prio', 'type': 'ffi::c_int'}, {'name': 'normal_prio', 'type': 'ffi::c_int'}, {'name': 'rt_priority', 'type': 'ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'dl_server', 'type': '*mut sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'ffi::c_uint'}, {'name': 'policy', 'type': 'ffi::c_uint'}, {'name': 'max_allowed_capacity', 'type': 'ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut ffi::c_void'}, {'name': 'migration_disabled', 'type': 'ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'rcu_tasks_exit_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_exit_list', 'type': 'list_head'}, {'name': 'trc_reader_nesting', 'type': 'ffi::c_int'}, {'name': 'trc_ipi_to_cpu', 'type': 'ffi::c_int'}, {'name': 'trc_reader_special', 'type': 'rcu_special'}, {'name': 'trc_holdout_list', 'type': 'list_head'}, {'name': 'trc_blkd_node', 'type': 'list_head'}, {'name': 'trc_blkd_cpu', 'type': 'ffi::c_int'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'faults_disabled_mapping', 'type': '*mut address_space'}, {'name': 'exit_state', 'type': 'ffi::c_int'}, {'name': 'exit_code', 'type': 'ffi::c_int'}, {'name': 'exit_signal', 'type': 'ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'ffi::c_int'}, {'name': 'jobctl', 'type': 'ffi::c_ulong'}, {'name': 'personality', 'type': 'ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'worker_private', 'type': '*mut ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'journal_info', 'type': '*mut ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'ffi::c_uint'}, {'name': 'perf_recursion', 'type': '[u8_; 4usize]'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'perf_ctx_data', 'type': '*mut perf_ctx_data'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'ffi::c_short'}, {'name': 'il_weight', 'type': 'u8_'}, {'name': 'pref_node_fork', 'type': 'ffi::c_short'}, {'name': 'rseq', 'type': '*mut rseq'}, {'name': 'rseq_len', 'type': 'u32_'}, {'name': 'rseq_sig', 'type': 'u32_'}, {'name': 'rseq_event_mask', 'type': 'ffi::c_ulong'}, {'name': 'mm_cid', 'type': 'ffi::c_int'}, {'name': 'last_mm_cid', 'type': 'ffi::c_int'}, {'name': 'migrate_from_cpu', 'type': 'ffi::c_int'}, {'name': 'mm_cid_active', 'type': 'ffi::c_int'}, {'name': 'cid_work', 'type': 'callback_head'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'bpf_net_context', 'type': '*mut bpf_net_context'}, {'name': 'mce_vaddr', 'type': '*mut ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': '__bindgen_padding_1', 'type': '[u64; 3usize]'}, {'name': 'thread', 'type': 'thread_struct'}]`

### Rust Evidence

- Graph edges: `15`

## W-000073 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: getname
- Explanation: getname changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `4`

## W-000560 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: getname
- Explanation: getname changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['name'], 'return_type': 'return'}`
- New: `{'params': ['const char __user *name'], 'return_type': 'static inline struct filename *'}`

### Rust Evidence

- Graph edges: `4`

## W-000044 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: cpu_wants_rethunk
- Explanation: cpu_wants_rethunk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000136 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: phy_register_fixup
- Explanation: phy_register_fixup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `2`

## W-000153 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: sched_domains_mutex_lock
- Explanation: sched_domains_mutex_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000187 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: xas_try_split
- Explanation: xas_try_split changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000002 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __blk_rq_map_sg
- Explanation: __blk_rq_map_sg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'q', 'type': '*mut request_queue'}, {'name': 'rq', 'type': '*mut request'}, {'name': 'sglist', 'type': '*mut scatterlist'}, {'name': 'last_sg', 'type': '*mut *mut scatterlist'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'rq', 'type': '*mut request'}, {'name': 'sglist', 'type': '*mut scatterlist'}, {'name': 'last_sg', 'type': '*mut *mut scatterlist'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000003 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __ioread64_hi_lo
- Explanation: __ioread64_hi_lo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000004 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __ioread64_lo_hi
- Explanation: __ioread64_lo_hi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000005 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __ioread64be_hi_lo
- Explanation: __ioread64be_hi_lo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000006 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __ioread64be_lo_hi
- Explanation: __ioread64be_lo_hi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000007 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __iowrite64_hi_lo
- Explanation: __iowrite64_hi_lo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000008 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __iowrite64_lo_hi
- Explanation: __iowrite64_lo_hi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000009 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __iowrite64be_hi_lo
- Explanation: __iowrite64be_hi_lo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000010 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __iowrite64be_lo_hi
- Explanation: __iowrite64be_lo_hi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000015 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __trace_set_current_state
- Explanation: __trace_set_current_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000017 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __vma_start_write
- Explanation: __vma_start_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000018 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_cpumask_var
- Explanation: alloc_cpumask_var changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000019 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_inode
- Explanation: alloc_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000020 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: apply_alternatives
- Explanation: apply_alternatives changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'start', 'type': '*mut alt_instr'}, {'name': 'end', 'type': '*mut alt_instr'}, {'name': 'mod_', 'type': '*mut module'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'start', 'type': '*mut alt_instr'}, {'name': 'end', 'type': '*mut alt_instr'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000021 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: apply_fineibt
- Explanation: apply_fineibt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'start_retpoline', 'type': '*mut s32'}, {'name': 'end_retpoine', 'type': '*mut s32'}, {'name': 'start_cfi', 'type': '*mut s32'}, {'name': 'end_cfi', 'type': '*mut s32'}, {'name': 'mod_', 'type': '*mut module'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'start_retpoline', 'type': '*mut s32'}, {'name': 'end_retpoine', 'type': '*mut s32'}, {'name': 'start_cfi', 'type': '*mut s32'}, {'name': 'end_cfi', 'type': '*mut s32'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000022 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: apply_retpolines
- Explanation: apply_retpolines changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'start', 'type': '*mut s32'}, {'name': 'end', 'type': '*mut s32'}, {'name': 'mod_', 'type': '*mut module'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'start', 'type': '*mut s32'}, {'name': 'end', 'type': '*mut s32'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000023 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: apply_returns
- Explanation: apply_returns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'start', 'type': '*mut s32'}, {'name': 'end', 'type': '*mut s32'}, {'name': 'mod_', 'type': '*mut module'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'start', 'type': '*mut s32'}, {'name': 'end', 'type': '*mut s32'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000024 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: apply_seal_endbr
- Explanation: apply_seal_endbr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'start', 'type': '*mut s32'}, {'name': 'end', 'type': '*mut s32'}, {'name': 'mod_', 'type': '*mut module'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'start', 'type': '*mut s32'}, {'name': 'end', 'type': '*mut s32'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000025 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_memremap_wb
- Explanation: arch_memremap_wb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000026 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_mm_preinit
- Explanation: arch_mm_preinit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000028 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bdev_statx
- Explanation: bdev_statx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut path'}, {'name': 'arg2', 'type': '*mut kstat'}, {'name': 'arg3', 'type': 'u32_'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'path', 'type': '*const path'}, {'name': 'stat', 'type': '*mut kstat'}, {'name': 'request_mask', 'type': 'u32_'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000029 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bdev_validate_blocksize
- Explanation: bdev_validate_blocksize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000032 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_get_perf_event_read_value_proto
- Explanation: bpf_get_perf_event_read_value_proto changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000033 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_prog_ctx_arg_info_init
- Explanation: bpf_prog_ctx_arg_info_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000034 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_link_lanes_supported
- Explanation: cap_link_lanes_supported changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u32_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(0usize, 1u8) as u32) } } #[inline] pub fn set_cap_link_lanes_supported(&mut self, val: u32_) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u32_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(8usize, 1u8) as u32) } } #[inline] pub fn set_cap_link_lanes_supported(&mut self, val: u32_) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000035 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_rss_ctx_supported
- Explanation: cap_rss_ctx_supported changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u32_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(1usize, 1u8) as u32) } } #[inline] pub fn set_cap_rss_ctx_supported(&mut self, val: u32_) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u32_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(9usize, 1u8) as u32) } } #[inline] pub fn set_cap_rss_ctx_supported(&mut self, val: u32_) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000036 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_rss_rxnfc_adds
- Explanation: cap_rss_rxnfc_adds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u32_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(4usize, 1u8) as u32) } } #[inline] pub fn set_cap_rss_rxnfc_adds(&mut self, val: u32_) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u32_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(11usize, 1u8) as u32) } } #[inline] pub fn set_cap_rss_rxnfc_adds(&mut self, val: u32_) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000038 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_add_cftypes
- Explanation: cgroup_add_cftypes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000041 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: change_pid
- Explanation: change_pid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'task', 'type': '*mut task_struct'}, {'name': 'arg1', 'type': 'pid_type'}, {'name': 'pid', 'type': '*mut pid'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'pids', 'type': '*mut *mut pid'}, {'name': 'task', 'type': '*mut task_struct'}, {'name': 'arg1', 'type': 'pid_type'}, {'name': 'pid', 'type': '*mut pid'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000042 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: check_cpufeature_deps
- Explanation: check_cpufeature_deps changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000043 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_show_indirect_target_selection
- Explanation: cpu_show_indirect_target_selection changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000045 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_wants_rethunk_at
- Explanation: cpu_wants_rethunk_at changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000046 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpumask_clear_cpu
- Explanation: cpumask_clear_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000047 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpumask_copy
- Explanation: cpumask_copy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000049 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpumask_set_cpu
- Explanation: cpumask_set_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000050 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpumask_setall
- Explanation: cpumask_setall changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000051 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpumask_weight
- Explanation: cpumask_weight changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000053 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: detach_pid
- Explanation: detach_pid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'task', 'type': '*mut task_struct'}, {'name': 'arg1', 'type': 'pid_type'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'pids', 'type': '*mut *mut pid'}, {'name': 'task', 'type': '*mut task_struct'}, {'name': 'arg1', 'type': 'pid_type'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000054 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_add_of_node
- Explanation: device_add_of_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000055 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_remove_of_node
- Explanation: device_remove_of_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000060 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_sys_open
- Explanation: do_sys_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'dfd', 'type': 'ffi::c_int'}, {'name': 'filename', 'type': '*const ffi::c_char'}, {'name': 'flags', 'type': 'ffi::c_int'}, {'name': 'mode', 'type': 'umode_t'}], 'return_type': 'ffi::c_long'}`
- New: `{'params': [{'name': 'dfd', 'type': 'ffi::c_int'}, {'name': 'filename', 'type': '*const ffi::c_char'}, {'name': 'flags', 'type': 'ffi::c_int'}, {'name': 'mode', 'type': 'umode_t'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000063 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: flit_mode
- Explanation: flit_mode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000064 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_cpumask_var
- Explanation: free_cpumask_var changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000065 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_pages_nolock
- Explanation: free_pages_nolock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000066 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_pids
- Explanation: free_pids changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000067 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_eee_is_active
- Explanation: genphy_c45_eee_is_active changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'adv', 'type': '*mut ffi::c_ulong'}, {'name': 'lp', 'type': '*mut ffi::c_ulong'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'lp', 'type': '*mut ffi::c_ulong'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000068 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_loopback
- Explanation: genphy_c45_loopback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'enable', 'type': 'bool_'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'enable', 'type': 'bool_'}, {'name': 'speed', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000070 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_loopback
- Explanation: genphy_loopback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'enable', 'type': 'bool_'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'enable', 'type': 'bool_'}, {'name': 'speed', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000071 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_dump_page
- Explanation: get_dump_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'addr', 'type': 'ffi::c_ulong'}], 'return_type': '*mut page'}`
- New: `{'params': [{'name': 'addr', 'type': 'ffi::c_ulong'}, {'name': 'locked', 'type': '*mut ffi::c_int'}], 'return_type': '*mut page'}`

### Rust Evidence

- Graph edges: `1`

## W-000074 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: has_capability
- Explanation: has_capability changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000076 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ida_find_first_range
- Explanation: ida_find_first_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000077 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: identify_secondary_cpu
- Explanation: identify_secondary_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut cpuinfo_x86'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'cpu', 'type': 'ffi::c_uint'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000084 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ioremap_prot
- Explanation: ioremap_prot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'offset', 'type': 'resource_size_t'}, {'name': 'size', 'type': 'ffi::c_ulong'}, {'name': 'prot_val', 'type': 'ffi::c_ulong'}], 'return_type': '*mut ffi::c_void'}`
- New: `{'params': [{'name': 'offset', 'type': 'resource_size_t'}, {'name': 'size', 'type': 'ffi::c_ulong'}, {'name': 'prot', 'type': 'pgprot_t'}], 'return_type': '*mut ffi::c_void'}`

### Rust Evidence

- Graph edges: `1`

## W-000091 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_endbr
- Explanation: is_endbr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000092 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: its_fini_mod
- Explanation: its_fini_mod changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000093 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: its_free_mod
- Explanation: its_free_mod changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000094 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: its_init_mod
- Explanation: its_init_mod changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000095 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: its_return_thunk
- Explanation: its_return_thunk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000096 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: its_static_thunk
- Explanation: its_static_thunk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000097 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_path_from_node
- Explanation: kernfs_path_from_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'root_kn', 'type': '*mut kernfs_node'}, {'name': 'kn', 'type': '*mut kernfs_node'}, {'name': 'buf', 'type': '*mut ffi::c_char'}, {'name': 'buflen', 'type': 'usize'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'kn_to', 'type': '*mut kernfs_node'}, {'name': 'kn_from', 'type': '*mut kernfs_node'}, {'name': 'buf', 'type': '*mut ffi::c_char'}, {'name': 'buflen', 'type': 'usize'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000098 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_root_flags
- Explanation: kernfs_root_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000101 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lookup_or_create_module_kobject
- Explanation: lookup_or_create_module_kobject changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000102 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: module_for_each_mod
- Explanation: module_for_each_mod changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000104 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: must_resume
- Explanation: must_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_2.get(4usize, 1u8) as u8) } } #[inline] pub fn set_must_resume(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_2.get(5usize, 1u8) as u8) } } #[inline] pub fn set_must_resume(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000105 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mutex_get_owner
- Explanation: mutex_get_owner changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000106 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mwait_play_dead
- Explanation: mwait_play_dead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000107 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: napi_skb_cache_get_bulk
- Explanation: napi_skb_cache_get_bulk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000108 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: nearest_node_nodemask
- Explanation: nearest_node_nodemask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000109 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_bitfield_4
- Explanation: new_bitfield_4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'transparent', 'type': 'ffi::c_uint'}, {'name': 'io_window', 'type': 'ffi::c_uint'}, {'name': 'pref_window', 'type': 'ffi::c_uint'}, {'name': 'pref_64_window', 'type': 'ffi::c_uint'}, {'name': 'multifunction', 'type': 'ffi::c_uint'}, {'name': 'is_busmaster', 'type': 'ffi::c_uint'}, {'name': 'no_msi', 'type': 'ffi::c_uint'}, {'name': 'no_64bit_msi', 'type': 'ffi::c_uint'}, {'name': 'block_cfg_access', 'type': 'ffi::c_uint'}, {'name': 'broken_parity_status', 'type': 'ffi::c_uint'}, {'name': 'irq_reroute_variant', 'type': 'ffi::c_uint'}, {'name': 'msi_enabled', 'type': 'ffi::c_uint'}, {'name': 'msix_enabled', 'type': 'ffi::c_uint'}, {'name': 'ari_enabled', 'type': 'ffi::c_uint'}, {'name': 'ats_enabled', 'type': 'ffi::c_uint'}, {'name': 'pasid_enabled', 'type': 'ffi::c_uint'}, {'name': 'pri_enabled', 'type': 'ffi::c_uint'}, {'name': 'tph_enabled', 'type': 'ffi::c_uint'}, {'name': 'is_managed', 'type': 'ffi::c_uint'}, {'name': 'is_msi_managed', 'type': 'ffi::c_uint'}, {'name': 'needs_freset', 'type': 'ffi::c_uint'}, {'name': 'state_saved', 'type': 'ffi::c_uint'}, {'name': 'is_physfn', 'type': 'ffi::c_uint'}, {'name': 'is_virtfn', 'type': 'ffi::c_uint'}, {'name': 'is_hotplug_bridge', 'type': 'ffi::c_uint'}, {'name': 'shpc_managed', 'type': 'ffi::c_uint'}, {'name': 'is_thunderbolt', 'type': 'ffi::c_uint'}, {'name': 'untrusted', 'type': 'ffi::c_uint'}, {'name': 'external_facing', 'type': 'ffi::c_uint'}, {'name': 'broken_intx_masking', 'type': 'ffi::c_uint'}, {'name': 'io_window_1k', 'type': 'ffi::c_uint'}, {'name': 'irq_managed', 'type': 'ffi::c_uint'}, {'name': 'non_compliant_bars', 'type': 'ffi::c_uint'}, {'name': 'is_probed', 'type': 'ffi::c_uint'}, {'name': 'link_active_reporting', 'type': 'ffi::c_uint'}, {'name': 'no_vf_scan', 'type': 'ffi::c_uint'}, {'name': 'no_command_memory', 'type': 'ffi::c_uint'}, {'name': 'rom_bar_overlap', 'type': 'ffi::c_uint'}, {'name': 'rom_attr_enabled', 'type': 'ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`
- New: `{'params': [{'name': 'transparent', 'type': 'ffi::c_uint'}, {'name': 'io_window', 'type': 'ffi::c_uint'}, {'name': 'pref_window', 'type': 'ffi::c_uint'}, {'name': 'pref_64_window', 'type': 'ffi::c_uint'}, {'name': 'multifunction', 'type': 'ffi::c_uint'}, {'name': 'is_busmaster', 'type': 'ffi::c_uint'}, {'name': 'no_msi', 'type': 'ffi::c_uint'}, {'name': 'no_64bit_msi', 'type': 'ffi::c_uint'}, {'name': 'block_cfg_access', 'type': 'ffi::c_uint'}, {'name': 'broken_parity_status', 'type': 'ffi::c_uint'}, {'name': 'irq_reroute_variant', 'type': 'ffi::c_uint'}, {'name': 'msi_enabled', 'type': 'ffi::c_uint'}, {'name': 'msix_enabled', 'type': 'ffi::c_uint'}, {'name': 'ari_enabled', 'type': 'ffi::c_uint'}, {'name': 'ats_enabled', 'type': 'ffi::c_uint'}, {'name': 'pasid_enabled', 'type': 'ffi::c_uint'}, {'name': 'pri_enabled', 'type': 'ffi::c_uint'}, {'name': 'tph_enabled', 'type': 'ffi::c_uint'}, {'name': 'is_managed', 'type': 'ffi::c_uint'}, {'name': 'is_msi_managed', 'type': 'ffi::c_uint'}, {'name': 'needs_freset', 'type': 'ffi::c_uint'}, {'name': 'state_saved', 'type': 'ffi::c_uint'}, {'name': 'is_physfn', 'type': 'ffi::c_uint'}, {'name': 'is_virtfn', 'type': 'ffi::c_uint'}, {'name': 'is_hotplug_bridge', 'type': 'ffi::c_uint'}, {'name': 'shpc_managed', 'type': 'ffi::c_uint'}, {'name': 'is_thunderbolt', 'type': 'ffi::c_uint'}, {'name': 'untrusted', 'type': 'ffi::c_uint'}, {'name': 'external_facing', 'type': 'ffi::c_uint'}, {'name': 'broken_intx_masking', 'type': 'ffi::c_uint'}, {'name': 'io_window_1k', 'type': 'ffi::c_uint'}, {'name': 'irq_managed', 'type': 'ffi::c_uint'}, {'name': 'non_compliant_bars', 'type': 'ffi::c_uint'}, {'name': 'is_probed', 'type': 'ffi::c_uint'}, {'name': 'link_active_reporting', 'type': 'ffi::c_uint'}, {'name': 'no_vf_scan', 'type': 'ffi::c_uint'}, {'name': 'no_command_memory', 'type': 'ffi::c_uint'}, {'name': 'rom_bar_overlap', 'type': 'ffi::c_uint'}, {'name': 'rom_attr_enabled', 'type': 'ffi::c_uint'}, {'name': 'non_mappable_bars', 'type': 'ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`

### Rust Evidence

- Graph edges: `1`

## W-000111 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: non_mappable_bars
- Explanation: non_mappable_bars changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000128 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_get_tx_amplitude_gain
- Explanation: phy_get_tx_amplitude_gain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000130 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_loopback
- Explanation: phy_loopback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'enable', 'type': 'bool_'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'enable', 'type': 'bool_'}, {'name': 'speed', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000142 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: posixtimer_create_prctl
- Explanation: posixtimer_create_prctl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000143 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pr_flush
- Explanation: pr_flush changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000144 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: preempt_model_str
- Explanation: preempt_model_str changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000145 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: prep_compound_page
- Explanation: prep_compound_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000148 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: reserve_mem_release_by_name
- Explanation: reserve_mem_release_by_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000149 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: resilient_queued_spin_lock_slowpath
- Explanation: resilient_queued_spin_lock_slowpath changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000150 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: resilient_tas_spin_lock
- Explanation: resilient_tas_spin_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000151 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rust_fmt_argument
- Explanation: rust_fmt_argument changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000152 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rxfh_per_ctx_key
- Explanation: rxfh_per_ctx_key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u32_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(3usize, 1u8) as u32) } } #[inline] pub fn set_rxfh_per_ctx_key(&mut self, val: u32_) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u32_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(10usize, 1u8) as u32) } } #[inline] pub fn set_rxfh_per_ctx_key(&mut self, val: u32_) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000154 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sched_domains_mutex_unlock
- Explanation: sched_domains_mutex_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000155 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: section_map_size
- Explanation: section_map_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000156 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_perf_event_open
- Explanation: security_perf_event_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'attr', 'type': '*mut perf_event_attr'}, {'name': 'type_', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'type_', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000157 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_uring_allowed
- Explanation: security_uring_allowed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000159 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_strntoul
- Explanation: simple_strntoul changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000160 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_flow_get_ports
- Explanation: skb_flow_get_ports changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000161 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: smart_suspend
- Explanation: smart_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000163 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sparse_init_early_section
- Explanation: sparse_init_early_section changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000164 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sparse_vmemmap_init_nid_early
- Explanation: sparse_vmemmap_init_nid_early changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000165 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sparse_vmemmap_init_nid_late
- Explanation: sparse_vmemmap_init_nid_late changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000166 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: supported_input_xfrm
- Explanation: supported_input_xfrm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000168 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: timer_create_restore_ids
- Explanation: timer_create_restore_ids changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000169 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: track_pfn_copy
- Explanation: track_pfn_copy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'dst_vma', 'type': '*mut vm_area_struct'}, {'name': 'src_vma', 'type': '*mut vm_area_struct'}, {'name': 'pfn', 'type': '*mut ffi::c_ulong'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000170 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: try_alloc_pages_noprof
- Explanation: try_alloc_pages_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000171 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: untrack_pfn_copy
- Explanation: untrack_pfn_copy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000172 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_ioctl
- Explanation: vfs_ioctl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'file', 'type': '*mut file'}, {'name': 'cmd', 'type': 'ffi::c_uint'}, {'name': 'arg', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_long'}`
- New: `{'params': [{'name': 'file', 'type': '*mut file'}, {'name': 'cmd', 'type': 'ffi::c_uint'}, {'name': 'arg', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000173 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_mkdir
- Explanation: vfs_mkdir changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut mnt_idmap'}, {'name': 'arg2', 'type': '*mut inode'}, {'name': 'arg3', 'type': '*mut dentry'}, {'name': 'arg4', 'type': 'umode_t'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*mut mnt_idmap'}, {'name': 'arg2', 'type': '*mut inode'}, {'name': 'arg3', 'type': '*mut dentry'}, {'name': 'arg4', 'type': 'umode_t'}], 'return_type': '*mut dentry'}`

### Rust Evidence

- Graph edges: `1`

## W-000174 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_pressure_ratio
- Explanation: vfs_pressure_ratio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000175 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_truncate
- Explanation: vfs_truncate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*const path'}, {'name': 'arg2', 'type': 'loff_t'}], 'return_type': 'ffi::c_long'}`
- New: `{'params': [{'name': 'arg1', 'type': '*const path'}, {'name': 'arg2', 'type': 'loff_t'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000176 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_mark_detached
- Explanation: vma_mark_detached changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000177 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmemmap_populate_hvo
- Explanation: vmemmap_populate_hvo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000178 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmemmap_pte_populate
- Explanation: vmemmap_pte_populate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'pmd', 'type': '*mut pmd_t'}, {'name': 'addr', 'type': 'ffi::c_ulong'}, {'name': 'node', 'type': 'ffi::c_int'}, {'name': 'altmap', 'type': '*mut vmem_altmap'}, {'name': 'reuse', 'type': '*mut page'}], 'return_type': '*mut pte_t'}`
- New: `{'params': [{'name': 'pmd', 'type': '*mut pmd_t'}, {'name': 'addr', 'type': 'ffi::c_ulong'}, {'name': 'node', 'type': 'ffi::c_int'}, {'name': 'altmap', 'type': '*mut vmem_altmap'}, {'name': 'ptpfn', 'type': 'ffi::c_ulong'}, {'name': 'flags', 'type': 'ffi::c_ulong'}], 'return_type': '*mut pte_t'}`

### Rust Evidence

- Graph edges: `1`

## W-000179 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmemmap_undo_hvo
- Explanation: vmemmap_undo_hvo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000180 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmemmap_wrprotect_hvo
- Explanation: vmemmap_wrprotect_hvo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000181 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmf_insert_folio_pmd
- Explanation: vmf_insert_folio_pmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000182 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmf_insert_folio_pud
- Explanation: vmf_insert_folio_pud changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000183 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmf_insert_page_mkwrite
- Explanation: vmf_insert_page_mkwrite changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000185 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: work_in_progress
- Explanation: work_in_progress changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000186 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: write_ibpb
- Explanation: write_ibpb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000188 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xas_try_split_min_order
- Explanation: xas_try_split_min_order changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000189 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: zalloc_cpumask_var
- Explanation: zalloc_cpumask_var changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000543 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __blk_rq_map_sg
- Explanation: __blk_rq_map_sg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['q', 'rq', 'sglist', '&last_sg'], 'return_type': 'return'}`
- New: `{'params': ['rq', 'sglist', '&last_sg'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `1`

## W-000544 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mdiobus_read
- Explanation: __mdiobus_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['phydev->mdio.bus', 'addr', 'regnum'], 'return_type': 'return'}`
- New: `{'params': ['phydev->mdio.bus', 'phydev->mdio.addr', 'regnum'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `1`

## W-000545 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mdiobus_write
- Explanation: __mdiobus_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['phydev->mdio.bus', 'addr', 'regnum', 'val'], 'return_type': 'return'}`
- New: `{'params': ['phydev->mdio.bus', 'phydev->mdio.addr', 'regnum', 'val'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `1`

## W-000547 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acomp_request_free
- Explanation: acomp_request_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct acomp_req *req'], 'return_type': 'void'}`
- New: `{'params': ['struct acomp_req *req'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `1`

## W-000548 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bdev_statx
- Explanation: bdev_statx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct path *path', 'struct kstat *stat', 'u32 request_mask'], 'return_type': 'static inline void'}`
- New: `{'params': ['const struct path *path', 'struct kstat *stat', 'u32 request_mask'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `1`

## W-000552 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_sys_open
- Explanation: do_sys_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['int dfd', 'const char __user *filename', 'int flags', 'umode_t mode'], 'return_type': 'extern long'}`
- New: `{'params': ['int dfd', 'const char __user *filename', 'int flags', 'umode_t mode'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000557 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_eee_is_active
- Explanation: genphy_c45_eee_is_active changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct phy_device *phydev', 'unsigned long *adv', 'unsigned long *lp'], 'return_type': 'int'}`
- New: `{'params': ['struct phy_device *phydev', 'unsigned long *lp'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000558 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_loopback
- Explanation: genphy_c45_loopback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct phy_device *phydev', 'bool enable'], 'return_type': 'int'}`
- New: `{'params': ['struct phy_device *phydev', 'bool enable', 'int speed'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000559 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_loopback
- Explanation: genphy_loopback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct phy_device *phydev', 'bool enable'], 'return_type': 'int'}`
- New: `{'params': ['struct phy_device *phydev', 'bool enable', 'int speed'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000561 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: getname_flags
- Explanation: getname_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const char __user *', 'int'], 'return_type': 'extern struct filename *'}`
- New: `{'params': ['name', '0'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `1`

## W-000566 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ioremap_prot
- Explanation: ioremap_prot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['addr', 'size', '_PAGE_IOREMAP'], 'return_type': 'return'}`
- New: `{'params': ['addr', 'size', '__pgprot(_PAGE_IOREMAP)'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `1`

## W-000573 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_loopback
- Explanation: phy_loopback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct phy_device *phydev', 'bool enable'], 'return_type': 'int'}`
- New: `{'params': ['struct phy_device *phydev', 'bool enable', 'int speed'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000598 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_perf_event_open
- Explanation: security_perf_event_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct perf_event_attr *attr', 'int type'], 'return_type': 'static inline int'}`
- New: `{'params': ['int type'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `1`

## W-000607 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_ioctl
- Explanation: vfs_ioctl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct file *file', 'unsigned int cmd', 'unsigned long arg'], 'return_type': 'extern long'}`
- New: `{'params': ['struct file *file', 'unsigned int cmd', 'unsigned long arg'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000608 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_mkdir
- Explanation: vfs_mkdir changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mnt_idmap *', 'struct inode *', 'struct dentry *', 'umode_t'], 'return_type': 'int'}`
- New: `{'params': ['struct mnt_idmap *', 'struct inode *', 'struct dentry *', 'umode_t'], 'return_type': 'struct dentry *'}`

### Rust Evidence

- Graph edges: `1`

## W-000609 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_truncate
- Explanation: vfs_truncate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct path *', 'loff_t'], 'return_type': 'extern long'}`
- New: `{'params': ['const struct path *', 'loff_t'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000553 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: drm_atomic_helper_damage_merged
- Explanation: drm_atomic_helper_damage_merged changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct drm_plane_state *old_state', 'struct drm_plane_state *state', 'struct drm_rect *rect'], 'return_type': 'bool'}`
- New: `{'params': ['const struct drm_plane_state *old_state', 'const struct drm_plane_state *state', 'struct drm_rect *rect'], 'return_type': 'bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000575 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_iounmap
- Explanation: rust_helper_iounmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['volatile void __iomem *addr'], 'return_type': 'void'}`
- New: `{'params': ['void __iomem *addr'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000576 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_readb
- Explanation: rust_helper_readb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const volatile void __iomem *addr'], 'return_type': 'u8'}`
- New: `{'params': ['const void __iomem *addr'], 'return_type': 'u8'}`

### Rust Evidence

- Graph edges: `0`

## W-000577 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_readb_relaxed
- Explanation: rust_helper_readb_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const volatile void __iomem *addr'], 'return_type': 'u8'}`
- New: `{'params': ['const void __iomem *addr'], 'return_type': 'u8'}`

### Rust Evidence

- Graph edges: `0`

## W-000578 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_readl
- Explanation: rust_helper_readl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const volatile void __iomem *addr'], 'return_type': 'u32'}`
- New: `{'params': ['const void __iomem *addr'], 'return_type': 'u32'}`

### Rust Evidence

- Graph edges: `0`

## W-000579 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_readl_relaxed
- Explanation: rust_helper_readl_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const volatile void __iomem *addr'], 'return_type': 'u32'}`
- New: `{'params': ['const void __iomem *addr'], 'return_type': 'u32'}`

### Rust Evidence

- Graph edges: `0`

## W-000580 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_readq
- Explanation: rust_helper_readq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const volatile void __iomem *addr'], 'return_type': 'u64'}`
- New: `{'params': ['const void __iomem *addr'], 'return_type': 'u64'}`

### Rust Evidence

- Graph edges: `0`

## W-000581 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_readq_relaxed
- Explanation: rust_helper_readq_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const volatile void __iomem *addr'], 'return_type': 'u64'}`
- New: `{'params': ['const void __iomem *addr'], 'return_type': 'u64'}`

### Rust Evidence

- Graph edges: `0`

## W-000582 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_readw
- Explanation: rust_helper_readw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const volatile void __iomem *addr'], 'return_type': 'u16'}`
- New: `{'params': ['const void __iomem *addr'], 'return_type': 'u16'}`

### Rust Evidence

- Graph edges: `0`

## W-000583 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_readw_relaxed
- Explanation: rust_helper_readw_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const volatile void __iomem *addr'], 'return_type': 'u16'}`
- New: `{'params': ['const void __iomem *addr'], 'return_type': 'u16'}`

### Rust Evidence

- Graph edges: `0`

## W-000584 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_writeb
- Explanation: rust_helper_writeb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u8 value', 'volatile void __iomem *addr'], 'return_type': 'void'}`
- New: `{'params': ['u8 value', 'void __iomem *addr'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000585 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_writeb_relaxed
- Explanation: rust_helper_writeb_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u8 value', 'volatile void __iomem *addr'], 'return_type': 'void'}`
- New: `{'params': ['u8 value', 'void __iomem *addr'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000586 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_writel
- Explanation: rust_helper_writel changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u32 value', 'volatile void __iomem *addr'], 'return_type': 'void'}`
- New: `{'params': ['u32 value', 'void __iomem *addr'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000587 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_writel_relaxed
- Explanation: rust_helper_writel_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u32 value', 'volatile void __iomem *addr'], 'return_type': 'void'}`
- New: `{'params': ['u32 value', 'void __iomem *addr'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000588 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_writeq
- Explanation: rust_helper_writeq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u64 value', 'volatile void __iomem *addr'], 'return_type': 'void'}`
- New: `{'params': ['u64 value', 'void __iomem *addr'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000589 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_writeq_relaxed
- Explanation: rust_helper_writeq_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u64 value', 'volatile void __iomem *addr'], 'return_type': 'void'}`
- New: `{'params': ['u64 value', 'void __iomem *addr'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000590 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_writew
- Explanation: rust_helper_writew changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u16 value', 'volatile void __iomem *addr'], 'return_type': 'void'}`
- New: `{'params': ['u16 value', 'void __iomem *addr'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000591 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_writew_relaxed
- Explanation: rust_helper_writew_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u16 value', 'volatile void __iomem *addr'], 'return_type': 'void'}`
- New: `{'params': ['u16 value', 'void __iomem *addr'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000216 FieldDrift

- Risk: High
- Score: 10.4
- Symbol: page_counter
- Explanation: page_counter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'usage', 'type': 'atomic_long_t'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': 'emin', 'type': 'ffi::c_ulong'}, {'name': 'min_usage', 'type': 'atomic_long_t'}, {'name': 'children_min_usage', 'type': 'atomic_long_t'}, {'name': 'elow', 'type': 'ffi::c_ulong'}, {'name': 'low_usage', 'type': 'atomic_long_t'}, {'name': 'children_low_usage', 'type': 'atomic_long_t'}, {'name': 'watermark', 'type': 'ffi::c_ulong'}, {'name': 'local_watermark', 'type': 'ffi::c_ulong'}, {'name': 'failcnt', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_padding_1', 'type': '[u64; 7usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'protection_support', 'type': 'bool_'}, {'name': 'min', 'type': 'ffi::c_ulong'}, {'name': 'low', 'type': 'ffi::c_ulong'}, {'name': 'high', 'type': 'ffi::c_ulong'}, {'name': 'max', 'type': 'ffi::c_ulong'}, {'name': 'parent', 'type': '*mut page_counter'}]`
- New: `[{'name': 'usage', 'type': 'atomic_long_t'}, {'name': 'failcnt', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': '[u64; 6usize]'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': 'emin', 'type': 'ffi::c_ulong'}, {'name': 'min_usage', 'type': 'atomic_long_t'}, {'name': 'children_min_usage', 'type': 'atomic_long_t'}, {'name': 'elow', 'type': 'ffi::c_ulong'}, {'name': 'low_usage', 'type': 'atomic_long_t'}, {'name': 'children_low_usage', 'type': 'atomic_long_t'}, {'name': 'watermark', 'type': 'ffi::c_ulong'}, {'name': 'local_watermark', 'type': 'ffi::c_ulong'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'protection_support', 'type': 'bool_'}, {'name': 'track_failcnt', 'type': 'bool_'}, {'name': 'min', 'type': 'ffi::c_ulong'}, {'name': 'low', 'type': 'ffi::c_ulong'}, {'name': 'high', 'type': 'ffi::c_ulong'}, {'name': 'max', 'type': 'ffi::c_ulong'}, {'name': 'parent', 'type': '*mut page_counter'}]`

### Rust Evidence

- Graph edges: `9`

## W-000232 FieldDrift

- Risk: High
- Score: 10.0
- Symbol: uprobe_task
- Explanation: uprobe_task changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'state', 'type': 'uprobe_task_state'}, {'name': 'depth', 'type': 'ffi::c_uint'}, {'name': 'return_instances', 'type': '*mut return_instance'}, {'name': 'ri_pool', 'type': '*mut return_instance'}, {'name': 'ri_timer', 'type': 'timer_list'}, {'name': 'ri_seqcount', 'type': 'seqcount_t'}, {'name': '__bindgen_anon_1', 'type': 'uprobe_task__bindgen_ty_1'}, {'name': 'active_uprobe', 'type': '*mut uprobe'}, {'name': 'xol_vaddr', 'type': 'ffi::c_ulong'}, {'name': 'auprobe', 'type': '*mut arch_uprobe'}]`
- New: `[{'name': 'state', 'type': 'uprobe_task_state'}, {'name': 'depth', 'type': 'ffi::c_uint'}, {'name': 'return_instances', 'type': '*mut return_instance'}, {'name': 'ri_pool', 'type': '*mut return_instance'}, {'name': 'ri_timer', 'type': 'timer_list'}, {'name': 'ri_seqcount', 'type': 'seqcount_t'}, {'name': '__bindgen_anon_1', 'type': 'uprobe_task__bindgen_ty_1'}, {'name': 'active_uprobe', 'type': '*mut uprobe'}, {'name': 'xol_vaddr', 'type': 'ffi::c_ulong'}, {'name': 'signal_denied', 'type': 'bool_'}, {'name': 'auprobe', 'type': '*mut arch_uprobe'}]`

### Rust Evidence

- Graph edges: `7`

## W-000001 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: KSTK_ESP
- Explanation: KSTK_ESP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000011 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __module_writable_address
- Explanation: __module_writable_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000012 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __phy_package_read_mmd
- Explanation: __phy_package_read_mmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000013 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __phy_package_write_mmd
- Explanation: __phy_package_write_mmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000014 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __skb_flow_get_ports
- Explanation: __skb_flow_get_ports changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000016 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __vm_area_free
- Explanation: __vm_area_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000027 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: async_in_progress
- Explanation: async_in_progress changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000030 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: blkdev_get_no_open
- Explanation: blkdev_get_no_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000031 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: blkdev_put_no_open
- Explanation: blkdev_put_no_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000037 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: cap_rss_sym_xor_supported
- Explanation: cap_rss_sym_xor_supported changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000039 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: cgroup_rstat_flush_hold
- Explanation: cgroup_rstat_flush_hold changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000040 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: cgroup_rstat_flush_release
- Explanation: cgroup_rstat_flush_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000048 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: cpumask_next_wrap
- Explanation: cpumask_next_wrap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000052 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: d_exact_alias
- Explanation: d_exact_alias changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000056 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: devm_of_phy_package_join
- Explanation: devm_of_phy_package_join changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000057 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: devm_phy_package_join
- Explanation: devm_phy_package_join changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000058 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: dirtytime_interval_handler
- Explanation: dirtytime_interval_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000059 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: do_arch_prctl_common
- Explanation: do_arch_prctl_common changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000061 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drop_caches_sysctl_handler
- Explanation: drop_caches_sysctl_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000062 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: entry_ibpb
- Explanation: entry_ibpb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000069 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: genphy_c45_read_eee_adv
- Explanation: genphy_c45_read_eee_adv changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000072 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: get_ucounts
- Explanation: get_ucounts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000075 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: hrtimer_init
- Explanation: hrtimer_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000078 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ioread64
- Explanation: ioread64 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000079 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ioread64_hi_lo
- Explanation: ioread64_hi_lo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000080 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ioread64_lo_hi
- Explanation: ioread64_lo_hi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000081 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ioread64be
- Explanation: ioread64be changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000082 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ioread64be_hi_lo
- Explanation: ioread64be_hi_lo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000083 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ioread64be_lo_hi
- Explanation: ioread64be_lo_hi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000085 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: iowrite64
- Explanation: iowrite64 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000086 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: iowrite64_hi_lo
- Explanation: iowrite64_hi_lo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000087 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: iowrite64_lo_hi
- Explanation: iowrite64_lo_hi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000088 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: iowrite64be
- Explanation: iowrite64be changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000089 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: iowrite64be_hi_lo
- Explanation: iowrite64be_hi_lo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000090 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: iowrite64be_lo_hi
- Explanation: iowrite64be_lo_hi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000103 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mount_single
- Explanation: mount_single changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000110 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: new_inode_pseudo
- Explanation: new_inode_pseudo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000112 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: of_phy_package_join
- Explanation: of_phy_package_join changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000113 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: of_set_phy_eee_broken
- Explanation: of_set_phy_eee_broken changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000114 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: of_set_phy_supported
- Explanation: of_set_phy_supported changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000115 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: of_set_phy_timing_role
- Explanation: of_set_phy_timing_role changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000116 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: overcommit_kbytes_handler
- Explanation: overcommit_kbytes_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000117 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: overcommit_policy_handler
- Explanation: overcommit_policy_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000118 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: overcommit_ratio_handler
- Explanation: overcommit_ratio_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000119 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: paravirt_disable_iospace
- Explanation: paravirt_disable_iospace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000120 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: partition_sched_domains_locked
- Explanation: partition_sched_domains_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000121 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: pci_hp_create_module_link
- Explanation: pci_hp_create_module_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000122 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: pci_hp_remove_module_link
- Explanation: pci_hp_remove_module_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000123 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: pci_reassign_bridge_resources
- Explanation: pci_reassign_bridge_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000124 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: pci_reassign_resource
- Explanation: pci_reassign_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000125 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: pci_rescan_bus_bridge_resize
- Explanation: pci_rescan_bus_bridge_resize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000126 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: pci_setup_bridge
- Explanation: pci_setup_bridge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000127 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_check_downshift
- Explanation: phy_check_downshift changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000129 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_lookup_setting
- Explanation: phy_lookup_setting changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000131 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_package_join
- Explanation: phy_package_join changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000132 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_package_leave
- Explanation: phy_package_leave changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000133 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_package_read_mmd
- Explanation: phy_package_read_mmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000134 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_package_write_mmd
- Explanation: phy_package_write_mmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000135 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_queue_state_machine
- Explanation: phy_queue_state_machine changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000137 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_speed_down_core
- Explanation: phy_speed_down_core changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000138 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_speeds
- Explanation: phy_speeds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000139 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_supported_speeds
- Explanation: phy_supported_speeds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000140 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: pm_generic_freeze_late
- Explanation: pm_generic_freeze_late changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000141 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: pm_generic_thaw_early
- Explanation: pm_generic_thaw_early changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000146 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: rcu_init_tasks_generic
- Explanation: rcu_init_tasks_generic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000147 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: register_page_bootmem_memmap
- Explanation: register_page_bootmem_memmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000158 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: set_active
- Explanation: set_active changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000162 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: smp_store_cpu_info
- Explanation: smp_store_cpu_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000167 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sysctl_vm_numa_stat_handler
- Explanation: sysctl_vm_numa_stat_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000184 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vmstat_refresh
- Explanation: vmstat_refresh changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000190 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: zone_watermark_ok_safe
- Explanation: zone_watermark_ok_safe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000542 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __arch_update_vsyscall
- Explanation: __arch_update_vsyscall changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct vdso_data *vdata'], 'return_type': 'static __always_inline void'}`
- New: `{'params': ['struct vdso_time_data *vdata'], 'return_type': 'static __always_inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-000546 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __tlb_remove_page_size
- Explanation: __tlb_remove_page_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['tlb', 'page', 'delay_rmap', 'PAGE_SIZE'], 'return_type': 'return'}`
- New: `{'params': ['struct mmu_gather *tlb', 'struct page *page', 'bool delay_rmap', 'int page_size'], 'return_type': 'extern bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000549 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: blk_rq_map_sg
- Explanation: blk_rq_map_sg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct request_queue *q', 'struct request *rq', 'struct scatterlist *sglist'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct request *rq', 'struct scatterlist *sglist'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `0`

## W-000550 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_acomp_compress
- Explanation: crypto_acomp_compress changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct acomp_req *req'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct acomp_req *req'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000551 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_acomp_decompress
- Explanation: crypto_acomp_decompress changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct acomp_req *req'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct acomp_req *req'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000554 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_hdmi_connector_mode_valid
- Explanation: drm_hdmi_connector_mode_valid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_connector *connector', 'struct drm_display_mode *mode'], 'return_type': 'enum drm_mode_status'}`
- New: `{'params': ['struct drm_connector *connector', 'const struct drm_display_mode *mode'], 'return_type': 'enum drm_mode_status'}`

### Rust Evidence

- Graph edges: `0`

## W-000555 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_lspcon_set_mode
- Explanation: drm_lspcon_set_mode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct drm_device *dev', 'struct i2c_adapter *adapter', 'enum drm_lspcon_mode reqd_mode'], 'return_type': 'int'}`
- New: `{'params': ['const struct drm_device *dev', 'struct i2c_adapter *adapter', 'enum drm_lspcon_mode reqd_mode', 'int time_out'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000556 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_sched_init
- Explanation: drm_sched_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_gpu_scheduler *sched', 'const struct drm_sched_backend_ops *ops', 'struct workqueue_struct *submit_wq', 'u32 num_rqs', 'u32 credit_limit', 'unsigned int hang_limit', 'long timeout', 'struct workqueue_struct *timeout_wq', 'atomic_t *score', 'const char *name', 'struct device *dev'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_gpu_scheduler *sched', 'const struct drm_sched_init_args *args'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000562 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: hv_do_fast_hypercall8
- Explanation: hv_do_fast_hypercall8 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u16 control', 'u64 input8'], 'return_type': 'extern u64'}`
- New: `{'params': ['u16 control', 'u64 input8'], 'return_type': 'u64'}`

### Rust Evidence

- Graph edges: `0`

## W-000563 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: hv_do_hypercall
- Explanation: hv_do_hypercall changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u64 control', 'void *inputaddr', 'void *outputaddr'], 'return_type': 'extern u64'}`
- New: `{'params': ['u64 control', 'void *inputaddr', 'void *outputaddr'], 'return_type': 'u64'}`

### Rust Evidence

- Graph edges: `0`

## W-000564 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ioread64
- Explanation: ioread64 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const void __iomem *'], 'return_type': 'extern u64'}`
- New: `{'params': ['const volatile void __iomem *addr'], 'return_type': 'static inline u64'}`

### Rust Evidence

- Graph edges: `0`

## W-000565 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ioread64be
- Explanation: ioread64be changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const void __iomem *'], 'return_type': 'extern u64'}`
- New: `{'params': ['const volatile void __iomem *addr'], 'return_type': 'static inline u64'}`

### Rust Evidence

- Graph edges: `0`

## W-000567 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: iowrite64
- Explanation: iowrite64 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u64', 'void __iomem *'], 'return_type': 'extern void'}`
- New: `{'params': ['u64 value', 'volatile void __iomem *addr'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-000568 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: iowrite64be
- Explanation: iowrite64be changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u64', 'void __iomem *'], 'return_type': 'extern void'}`
- New: `{'params': ['u64 value', 'volatile void __iomem *addr'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-000572 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: new_inode_pseudo
- Explanation: new_inode_pseudo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct super_block *sb'], 'return_type': 'extern struct inode *'}`
- New: `{'params': ['struct super_block *sb'], 'return_type': 'static inline struct inode *'}`

### Rust Evidence

- Graph edges: `0`

## W-000574 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: read_word_at_a_time
- Explanation: read_word_at_a_time changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const void *addr'], 'return_type': 'static __no_kasan_or_inline unsigned long'}`
- New: `{'params': ['const void *addr'], 'return_type': 'static __no_sanitize_or_inline unsigned long'}`

### Rust Evidence

- Graph edges: `0`

## W-000592 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: scatterwalk_map
- Explanation: scatterwalk_map changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct scatter_walk *walk'], 'return_type': 'static inline void *'}`
- New: `{'params': ['struct scatter_walk *walk'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-000593 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: scatterwalk_map_and_copy
- Explanation: scatterwalk_map_and_copy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['void *buf', 'struct scatterlist *sg', 'unsigned int start', 'unsigned int nbytes', 'int out'], 'return_type': 'void'}`
- New: `{'params': ['void *buf', 'struct scatterlist *sg', 'unsigned int start', 'unsigned int nbytes', 'int out'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-000594 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: scatterwalk_unmap
- Explanation: scatterwalk_unmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['void *vaddr'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct scatter_walk *walk'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-000595 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: security_bpf
- Explanation: security_bpf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['int cmd', 'union bpf_attr *attr', 'unsigned int size'], 'return_type': 'static inline int'}`
- New: `{'params': ['int cmd', 'union bpf_attr *attr', 'unsigned int size', 'bool kernel'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `0`

## W-000596 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: security_bpf_map_create
- Explanation: security_bpf_map_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct bpf_map *map', 'union bpf_attr *attr', 'struct bpf_token *token'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct bpf_map *map', 'union bpf_attr *attr', 'struct bpf_token *token', 'bool kernel'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `0`

## W-000597 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: security_bpf_prog_load
- Explanation: security_bpf_prog_load changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct bpf_prog *prog', 'union bpf_attr *attr', 'struct bpf_token *token'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct bpf_prog *prog', 'union bpf_attr *attr', 'struct bpf_token *token', 'bool kernel'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `0`

## W-000599 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: skcipher_walk_aead_decrypt
- Explanation: skcipher_walk_aead_decrypt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct skcipher_walk *walk', 'struct aead_request *req', 'bool atomic'], 'return_type': 'int'}`
- New: `{'params': ['struct skcipher_walk *__restrict walk', 'struct aead_request *__restrict req', 'bool atomic'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000600 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: skcipher_walk_aead_encrypt
- Explanation: skcipher_walk_aead_encrypt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct skcipher_walk *walk', 'struct aead_request *req', 'bool atomic'], 'return_type': 'int'}`
- New: `{'params': ['struct skcipher_walk *__restrict walk', 'struct aead_request *__restrict req', 'bool atomic'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000601 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: skcipher_walk_virt
- Explanation: skcipher_walk_virt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct skcipher_walk *walk', 'struct skcipher_request *req', 'bool atomic'], 'return_type': 'int'}`
- New: `{'params': ['struct skcipher_walk *__restrict walk', 'struct skcipher_request *__restrict req', 'bool atomic'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000602 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: test_and_clear_bit
- Explanation: test_and_clear_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['nr ^ BITOP_LE_SWIZZLE', 'addr'], 'return_type': 'return'}`
- New: `{'params': ['cpumask_check(cpu)', 'cpumask_bits(cpumask)'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-000603 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: test_and_set_bit
- Explanation: test_and_set_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['nr ^ BITOP_LE_SWIZZLE', 'addr'], 'return_type': 'return'}`
- New: `{'params': ['cpumask_check(cpu)', 'cpumask_bits(cpumask)'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-000604 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: test_bit
- Explanation: test_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['DRM_MM_NODE_ALLOCATED_BIT', '&node->flags'], 'return_type': 'return'}`
- New: `{'params': ['cpumask_check(cpu)', 'cpumask_bits((cpumask))'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-000605 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: tlb_remove_ptdesc
- Explanation: tlb_remove_ptdesc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mmu_gather *tlb', 'void *pt'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct mmu_gather *tlb', 'struct ptdesc *pt'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-000606 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ttm_resource_manager_first
- Explanation: ttm_resource_manager_first changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct ttm_resource_manager *man', 'struct ttm_resource_cursor *cursor'], 'return_type': 'struct ttm_resource *'}`
- New: `{'params': ['struct ttm_resource_cursor *cursor'], 'return_type': 'struct ttm_resource *'}`

### Rust Evidence

- Graph edges: `0`

## W-000207 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: k_itimer
- Explanation: k_itimer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'list', 'type': 'hlist_node'}, {'name': 'ignored_list', 'type': 'hlist_node'}, {'name': 't_hash', 'type': 'hlist_node'}, {'name': 'it_lock', 'type': 'spinlock_t'}, {'name': 'kclock', 'type': '*mut k_clock'}, {'name': 'it_clock', 'type': 'clockid_t'}, {'name': 'it_id', 'type': 'timer_t'}, {'name': 'it_status', 'type': 'ffi::c_int'}, {'name': 'it_sig_periodic', 'type': 'bool_'}, {'name': 'it_overrun', 'type': 's64'}, {'name': 'it_overrun_last', 'type': 's64'}, {'name': 'it_signal_seq', 'type': 'ffi::c_uint'}, {'name': 'it_sigqueue_seq', 'type': 'ffi::c_uint'}, {'name': 'it_sigev_notify', 'type': 'ffi::c_int'}, {'name': 'it_pid_type', 'type': 'pid_type'}, {'name': 'it_interval', 'type': 'ktime_t'}, {'name': 'it_signal', 'type': '*mut signal_struct'}, {'name': '__bindgen_anon_1', 'type': 'k_itimer__bindgen_ty_1'}, {'name': 'sigq', 'type': 'sigqueue'}, {'name': 'rcuref', 'type': 'rcuref_t'}, {'name': 'it', 'type': 'k_itimer__bindgen_ty_2'}, {'name': 'rcu', 'type': 'callback_head'}]`
- New: `[{'name': 't_hash', 'type': 'hlist_node'}, {'name': 'list', 'type': 'hlist_node'}, {'name': 'it_id', 'type': 'timer_t'}, {'name': 'it_clock', 'type': 'clockid_t'}, {'name': 'it_sigev_notify', 'type': 'ffi::c_int'}, {'name': 'it_pid_type', 'type': 'pid_type'}, {'name': 'it_signal', 'type': '*mut signal_struct'}, {'name': 'kclock', 'type': '*mut k_clock'}, {'name': 'it_lock', 'type': 'spinlock_t'}, {'name': 'it_status', 'type': 'ffi::c_int'}, {'name': 'it_sig_periodic', 'type': 'bool_'}, {'name': 'it_overrun', 'type': 's64'}, {'name': 'it_overrun_last', 'type': 's64'}, {'name': 'it_signal_seq', 'type': 'ffi::c_uint'}, {'name': 'it_sigqueue_seq', 'type': 'ffi::c_uint'}, {'name': 'it_interval', 'type': 'ktime_t'}, {'name': 'ignored_list', 'type': 'hlist_node'}, {'name': '__bindgen_anon_1', 'type': 'k_itimer__bindgen_ty_1'}, {'name': 'sigq', 'type': 'sigqueue'}, {'name': 'rcuref', 'type': 'rcuref_t'}, {'name': 'it', 'type': 'k_itimer__bindgen_ty_2'}, {'name': 'rcu', 'type': 'callback_head'}]`

### Rust Evidence

- Graph edges: `3`

## W-000213 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: net_iov
- Explanation: net_iov changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__unused_padding', 'type': 'ffi::c_ulong'}, {'name': 'pp_magic', 'type': 'ffi::c_ulong'}, {'name': 'pp', 'type': '*mut page_pool'}, {'name': 'owner', 'type': '*mut dmabuf_genpool_chunk_owner'}, {'name': 'dma_addr', 'type': 'ffi::c_ulong'}, {'name': 'pp_ref_count', 'type': 'atomic_long_t'}]`
- New: `[{'name': '__unused_padding', 'type': 'ffi::c_ulong'}, {'name': 'pp_magic', 'type': 'ffi::c_ulong'}, {'name': 'pp', 'type': '*mut page_pool'}, {'name': 'owner', 'type': '*mut net_iov_area'}, {'name': 'dma_addr', 'type': 'ffi::c_ulong'}, {'name': 'pp_ref_count', 'type': 'atomic_long_t'}]`

### Rust Evidence

- Graph edges: `3`

## W-000234 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: vm_area_struct
- Explanation: vm_area_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'vm_area_struct__bindgen_ty_1'}, {'name': 'vm_mm', 'type': '*mut mm_struct'}, {'name': 'vm_page_prot', 'type': 'pgprot_t'}, {'name': '__bindgen_anon_2', 'type': 'vm_area_struct__bindgen_ty_2'}, {'name': 'detached', 'type': 'bool_'}, {'name': 'vm_lock_seq', 'type': 'ffi::c_uint'}, {'name': 'vm_lock', 'type': '*mut vma_lock'}, {'name': 'shared', 'type': 'vm_area_struct__bindgen_ty_3'}, {'name': 'anon_vma_chain', 'type': 'list_head'}, {'name': 'anon_vma', 'type': '*mut anon_vma'}, {'name': 'vm_ops', 'type': '*const vm_operations_struct'}, {'name': 'vm_pgoff', 'type': 'ffi::c_ulong'}, {'name': 'vm_file', 'type': '*mut file'}, {'name': 'vm_private_data', 'type': '*mut ffi::c_void'}, {'name': 'swap_readahead_info', 'type': 'atomic_long_t'}, {'name': 'vm_policy', 'type': '*mut mempolicy'}, {'name': 'vm_userfaultfd_ctx', 'type': 'vm_userfaultfd_ctx'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'vm_area_struct__bindgen_ty_1'}, {'name': 'vm_mm', 'type': '*mut mm_struct'}, {'name': 'vm_page_prot', 'type': 'pgprot_t'}, {'name': '__bindgen_anon_2', 'type': 'vm_area_struct__bindgen_ty_2'}, {'name': 'vm_lock_seq', 'type': 'ffi::c_uint'}, {'name': 'anon_vma_chain', 'type': 'list_head'}, {'name': 'anon_vma', 'type': '*mut anon_vma'}, {'name': 'vm_ops', 'type': '*const vm_operations_struct'}, {'name': 'vm_pgoff', 'type': 'ffi::c_ulong'}, {'name': 'vm_file', 'type': '*mut file'}, {'name': 'vm_private_data', 'type': '*mut ffi::c_void'}, {'name': 'swap_readahead_info', 'type': 'atomic_long_t'}, {'name': 'vm_policy', 'type': '*mut mempolicy'}, {'name': '__bindgen_padding_0', 'type': '[u32; 2usize]'}, {'name': 'vm_refcnt', 'type': 'refcount_t'}, {'name': 'shared', 'type': 'vm_area_struct__bindgen_ty_3'}, {'name': 'vm_userfaultfd_ctx', 'type': 'vm_userfaultfd_ctx'}]`

### Rust Evidence

- Graph edges: `3`

## W-000202 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: folio__bindgen_ty_1__bindgen_ty_1
- Explanation: folio__bindgen_ty_1__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'folio__bindgen_ty_1__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mapping', 'type': '*mut address_space'}, {'name': 'index', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_2', 'type': 'folio__bindgen_ty_1__bindgen_ty_1__bindgen_ty_2'}, {'name': '_mapcount', 'type': 'atomic_t'}, {'name': '_refcount', 'type': 'atomic_t'}]`
- New: `[{'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'folio__bindgen_ty_1__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mapping', 'type': '*mut address_space'}, {'name': '__bindgen_anon_2', 'type': 'folio__bindgen_ty_1__bindgen_ty_1__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'folio__bindgen_ty_1__bindgen_ty_1__bindgen_ty_3'}, {'name': '_mapcount', 'type': 'atomic_t'}, {'name': '_refcount', 'type': 'atomic_t'}]`

### Rust Evidence

- Graph edges: `2`

## W-000203 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: folio__bindgen_ty_2__bindgen_ty_1
- Explanation: folio__bindgen_ty_2__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_flags_1', 'type': 'ffi::c_ulong'}, {'name': '_head_1', 'type': 'ffi::c_ulong'}, {'name': '_large_mapcount', 'type': 'atomic_t'}, {'name': '_entire_mapcount', 'type': 'atomic_t'}, {'name': '_nr_pages_mapped', 'type': 'atomic_t'}, {'name': '_pincount', 'type': 'atomic_t'}, {'name': '_folio_nr_pages', 'type': 'ffi::c_uint'}]`
- New: `[{'name': '_flags_1', 'type': 'ffi::c_ulong'}, {'name': '_head_1', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'folio__bindgen_ty_2__bindgen_ty_1__bindgen_ty_1'}, {'name': '_mapcount_1', 'type': 'atomic_t'}, {'name': '_refcount_1', 'type': 'atomic_t'}]`

### Rust Evidence

- Graph edges: `2`

## W-000210 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: mm_struct__bindgen_ty_1
- Explanation: mm_struct__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'mm_struct__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mm_mt', 'type': 'maple_tree'}, {'name': 'mmap_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'task_size', 'type': 'ffi::c_ulong'}, {'name': 'pgd', 'type': '*mut pgd_t'}, {'name': 'membarrier_state', 'type': 'atomic_t'}, {'name': 'mm_users', 'type': 'atomic_t'}, {'name': 'pcpu_cid', 'type': '*mut mm_cid'}, {'name': 'mm_cid_next_scan', 'type': 'ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_uint'}, {'name': 'max_nr_cid', 'type': 'atomic_t'}, {'name': 'cpus_allowed_lock', 'type': 'raw_spinlock_t'}, {'name': 'pgtables_bytes', 'type': 'atomic_long_t'}, {'name': 'map_count', 'type': 'ffi::c_int'}, {'name': 'page_table_lock', 'type': 'spinlock_t'}, {'name': 'mmap_lock', 'type': 'rw_semaphore'}, {'name': 'mmlist', 'type': 'list_head'}, {'name': 'mm_lock_seq', 'type': 'seqcount_t'}, {'name': 'hiwater_rss', 'type': 'ffi::c_ulong'}, {'name': 'hiwater_vm', 'type': 'ffi::c_ulong'}, {'name': 'total_vm', 'type': 'ffi::c_ulong'}, {'name': 'locked_vm', 'type': 'ffi::c_ulong'}, {'name': 'pinned_vm', 'type': 'atomic64_t'}, {'name': 'data_vm', 'type': 'ffi::c_ulong'}, {'name': 'exec_vm', 'type': 'ffi::c_ulong'}, {'name': 'stack_vm', 'type': 'ffi::c_ulong'}, {'name': 'def_flags', 'type': 'ffi::c_ulong'}, {'name': 'write_protect_seq', 'type': 'seqcount_t'}, {'name': 'arg_lock', 'type': 'spinlock_t'}, {'name': 'start_code', 'type': 'ffi::c_ulong'}, {'name': 'end_code', 'type': 'ffi::c_ulong'}, {'name': 'start_data', 'type': 'ffi::c_ulong'}, {'name': 'end_data', 'type': 'ffi::c_ulong'}, {'name': 'start_brk', 'type': 'ffi::c_ulong'}, {'name': 'brk', 'type': 'ffi::c_ulong'}, {'name': 'start_stack', 'type': 'ffi::c_ulong'}, {'name': 'arg_start', 'type': 'ffi::c_ulong'}, {'name': 'arg_end', 'type': 'ffi::c_ulong'}, {'name': 'env_start', 'type': 'ffi::c_ulong'}, {'name': 'env_end', 'type': 'ffi::c_ulong'}, {'name': 'saved_auxv', 'type': '[ffi::c_ulong; 52usize]'}, {'name': 'rss_stat', 'type': '[percpu_counter; 4usize]'}, {'name': 'binfmt', 'type': '*mut linux_binfmt'}, {'name': 'context', 'type': 'mm_context_t'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'ioctx_lock', 'type': 'spinlock_t'}, {'name': 'ioctx_table', 'type': '*mut kioctx_table'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'exe_file', 'type': '*mut file'}, {'name': 'notifier_subscriptions', 'type': '*mut mmu_notifier_subscriptions'}, {'name': 'tlb_flush_pending', 'type': 'atomic_t'}, {'name': 'tlb_flush_batched', 'type': 'atomic_t'}, {'name': 'uprobes_state', 'type': 'uprobes_state'}, {'name': 'hugetlb_usage', 'type': 'atomic_long_t'}, {'name': 'async_put_work', 'type': 'work_struct'}, {'name': 'iommu_mm', 'type': '*mut iommu_mm_data'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'mm_struct__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mm_mt', 'type': 'maple_tree'}, {'name': 'mmap_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'task_size', 'type': 'ffi::c_ulong'}, {'name': 'pgd', 'type': '*mut pgd_t'}, {'name': 'membarrier_state', 'type': 'atomic_t'}, {'name': 'mm_users', 'type': 'atomic_t'}, {'name': 'pcpu_cid', 'type': '*mut mm_cid'}, {'name': 'mm_cid_next_scan', 'type': 'ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_uint'}, {'name': 'max_nr_cid', 'type': 'atomic_t'}, {'name': 'cpus_allowed_lock', 'type': 'raw_spinlock_t'}, {'name': 'pgtables_bytes', 'type': 'atomic_long_t'}, {'name': 'map_count', 'type': 'ffi::c_int'}, {'name': 'page_table_lock', 'type': 'spinlock_t'}, {'name': 'mmap_lock', 'type': 'rw_semaphore'}, {'name': 'mmlist', 'type': 'list_head'}, {'name': 'vma_writer_wait', 'type': 'rcuwait'}, {'name': 'mm_lock_seq', 'type': 'seqcount_t'}, {'name': 'hiwater_rss', 'type': 'ffi::c_ulong'}, {'name': 'hiwater_vm', 'type': 'ffi::c_ulong'}, {'name': 'total_vm', 'type': 'ffi::c_ulong'}, {'name': 'locked_vm', 'type': 'ffi::c_ulong'}, {'name': 'pinned_vm', 'type': 'atomic64_t'}, {'name': 'data_vm', 'type': 'ffi::c_ulong'}, {'name': 'exec_vm', 'type': 'ffi::c_ulong'}, {'name': 'stack_vm', 'type': 'ffi::c_ulong'}, {'name': 'def_flags', 'type': 'ffi::c_ulong'}, {'name': 'write_protect_seq', 'type': 'seqcount_t'}, {'name': 'arg_lock', 'type': 'spinlock_t'}, {'name': 'start_code', 'type': 'ffi::c_ulong'}, {'name': 'end_code', 'type': 'ffi::c_ulong'}, {'name': 'start_data', 'type': 'ffi::c_ulong'}, {'name': 'end_data', 'type': 'ffi::c_ulong'}, {'name': 'start_brk', 'type': 'ffi::c_ulong'}, {'name': 'brk', 'type': 'ffi::c_ulong'}, {'name': 'start_stack', 'type': 'ffi::c_ulong'}, {'name': 'arg_start', 'type': 'ffi::c_ulong'}, {'name': 'arg_end', 'type': 'ffi::c_ulong'}, {'name': 'env_start', 'type': 'ffi::c_ulong'}, {'name': 'env_end', 'type': 'ffi::c_ulong'}, {'name': 'saved_auxv', 'type': '[ffi::c_ulong; 52usize]'}, {'name': 'rss_stat', 'type': '[percpu_counter; 4usize]'}, {'name': 'binfmt', 'type': '*mut linux_binfmt'}, {'name': 'context', 'type': 'mm_context_t'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'ioctx_lock', 'type': 'spinlock_t'}, {'name': 'ioctx_table', 'type': '*mut kioctx_table'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'exe_file', 'type': '*mut file'}, {'name': 'notifier_subscriptions', 'type': '*mut mmu_notifier_subscriptions'}, {'name': 'tlb_flush_pending', 'type': 'atomic_t'}, {'name': 'tlb_flush_batched', 'type': 'atomic_t'}, {'name': 'uprobes_state', 'type': 'uprobes_state'}, {'name': 'hugetlb_usage', 'type': 'atomic_long_t'}, {'name': 'async_put_work', 'type': 'work_struct'}, {'name': 'iommu_mm', 'type': '*mut iommu_mm_data'}]`

### Rust Evidence

- Graph edges: `2`

## W-000191 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: arch_tlbflush_unmap_batch
- Explanation: arch_tlbflush_unmap_batch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'cpumask', 'type': 'cpumask'}]`
- New: `[{'name': 'cpumask', 'type': 'cpumask'}, {'name': 'unmapped_pages', 'type': 'bool_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000192 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bpf_attr__bindgen_ty_8
- Explanation: bpf_attr__bindgen_ty_8 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'bpf_attr__bindgen_ty_8__bindgen_ty_1'}, {'name': 'next_id', 'type': '__u32'}, {'name': 'open_flags', 'type': '__u32'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'bpf_attr__bindgen_ty_8__bindgen_ty_1'}, {'name': 'next_id', 'type': '__u32'}, {'name': 'open_flags', 'type': '__u32'}, {'name': 'fd_by_id_token_fd', 'type': '__s32'}]`

### Rust Evidence

- Graph edges: `1`

## W-000193 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bpf_ctx_arg_aux
- Explanation: bpf_ctx_arg_aux changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'offset', 'type': 'u32_'}, {'name': 'reg_type', 'type': 'bpf_reg_type'}, {'name': 'btf', 'type': '*mut btf'}, {'name': 'btf_id', 'type': 'u32_'}]`
- New: `[{'name': 'offset', 'type': 'u32_'}, {'name': 'reg_type', 'type': 'bpf_reg_type'}, {'name': 'btf', 'type': '*mut btf'}, {'name': 'btf_id', 'type': 'u32_'}, {'name': 'ref_obj_id', 'type': 'u32_'}, {'name': 'refcounted', 'type': 'bool_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000194 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bpf_insn_access_aux__bindgen_ty_1__bindgen_ty_1
- Explanation: bpf_insn_access_aux__bindgen_ty_1__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'btf', 'type': '*mut btf'}, {'name': 'btf_id', 'type': 'u32_'}]`
- New: `[{'name': 'btf', 'type': '*mut btf'}, {'name': 'btf_id', 'type': 'u32_'}, {'name': 'ref_obj_id', 'type': 'u32_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000195 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bpf_prog_aux
- Explanation: bpf_prog_aux changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'refcnt', 'type': 'atomic64_t'}, {'name': 'used_map_cnt', 'type': 'u32_'}, {'name': 'used_btf_cnt', 'type': 'u32_'}, {'name': 'max_ctx_offset', 'type': 'u32_'}, {'name': 'max_pkt_offset', 'type': 'u32_'}, {'name': 'max_tp_access', 'type': 'u32_'}, {'name': 'stack_depth', 'type': 'u32_'}, {'name': 'id', 'type': 'u32_'}, {'name': 'func_cnt', 'type': 'u32_'}, {'name': 'real_func_cnt', 'type': 'u32_'}, {'name': 'func_idx', 'type': 'u32_'}, {'name': 'attach_btf_id', 'type': 'u32_'}, {'name': 'ctx_arg_info_size', 'type': 'u32_'}, {'name': 'max_rdonly_access', 'type': 'u32_'}, {'name': 'max_rdwr_access', 'type': 'u32_'}, {'name': 'attach_btf', 'type': '*mut btf'}, {'name': 'ctx_arg_info', 'type': '*const bpf_ctx_arg_aux'}, {'name': 'priv_stack_ptr', 'type': '*mut ffi::c_void'}, {'name': 'dst_mutex', 'type': 'mutex'}, {'name': 'dst_prog', 'type': '*mut bpf_prog'}, {'name': 'dst_trampoline', 'type': '*mut bpf_trampoline'}, {'name': 'saved_dst_prog_type', 'type': 'bpf_prog_type'}, {'name': 'saved_dst_attach_type', 'type': 'bpf_attach_type'}, {'name': 'verifier_zext', 'type': 'bool_'}, {'name': 'dev_bound', 'type': 'bool_'}, {'name': 'offload_requested', 'type': 'bool_'}, {'name': 'attach_btf_trace', 'type': 'bool_'}, {'name': 'attach_tracing_prog', 'type': 'bool_'}, {'name': 'func_proto_unreliable', 'type': 'bool_'}, {'name': 'tail_call_reachable', 'type': 'bool_'}, {'name': 'xdp_has_frags', 'type': 'bool_'}, {'name': 'exception_cb', 'type': 'bool_'}, {'name': 'exception_boundary', 'type': 'bool_'}, {'name': 'is_extended', 'type': 'bool_'}, {'name': 'jits_use_priv_stack', 'type': 'bool_'}, {'name': 'priv_stack_requested', 'type': 'bool_'}, {'name': 'changes_pkt_data', 'type': 'bool_'}, {'name': 'prog_array_member_cnt', 'type': 'u64_'}, {'name': 'ext_mutex', 'type': 'mutex'}, {'name': 'arena', 'type': '*mut bpf_arena'}, {'name': 'recursion_detected', 'type': '::core::option::Option<unsafe extern "C" fn(prog: *mut bpf_prog)>'}, {'name': 'attach_func_proto', 'type': '*const btf_type'}, {'name': 'attach_func_name', 'type': '*const ffi::c_char'}, {'name': 'func', 'type': '*mut *mut bpf_prog'}, {'name': 'jit_data', 'type': '*mut ffi::c_void'}, {'name': 'poke_tab', 'type': '*mut bpf_jit_poke_descriptor'}, {'name': 'kfunc_tab', 'type': '*mut bpf_kfunc_desc_tab'}, {'name': 'kfunc_btf_tab', 'type': '*mut bpf_kfunc_btf_tab'}, {'name': 'size_poke_tab', 'type': 'u32_'}, {'name': 'ksym', 'type': 'bpf_ksym'}, {'name': 'ops', 'type': '*const bpf_prog_ops'}, {'name': 'used_maps', 'type': '*mut *mut bpf_map'}, {'name': 'used_maps_mutex', 'type': 'mutex'}, {'name': 'used_btfs', 'type': '*mut btf_mod_pair'}, {'name': 'prog', 'type': '*mut bpf_prog'}, {'name': 'user', 'type': '*mut user_struct'}, {'name': 'load_time', 'type': 'u64_'}, {'name': 'verified_insns', 'type': 'u32_'}, {'name': 'cgroup_atype', 'type': 'ffi::c_int'}, {'name': 'cgroup_storage', 'type': '[*mut bpf_map; 2usize]'}, {'name': 'name', 'type': '[ffi::c_char; 16usize]'}, {'name': 'bpf_exception_cb', 'type': '::core::option::Option<'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'token', 'type': '*mut bpf_token'}, {'name': 'offload', 'type': '*mut bpf_prog_offload'}, {'name': 'btf', 'type': '*mut btf'}, {'name': 'func_info', 'type': '*mut bpf_func_info'}, {'name': 'func_info_aux', 'type': '*mut bpf_func_info_aux'}, {'name': 'linfo', 'type': '*mut bpf_line_info'}, {'name': 'jited_linfo', 'type': '*mut *mut ffi::c_void'}, {'name': 'func_info_cnt', 'type': 'u32_'}, {'name': 'nr_linfo', 'type': 'u32_'}, {'name': 'linfo_idx', 'type': 'u32_'}, {'name': 'mod_', 'type': '*mut module'}, {'name': 'num_exentries', 'type': 'u32_'}, {'name': 'extable', 'type': '*mut exception_table_entry'}, {'name': '__bindgen_anon_1', 'type': 'bpf_prog_aux__bindgen_ty_1'}]`
- New: `[{'name': 'refcnt', 'type': 'atomic64_t'}, {'name': 'used_map_cnt', 'type': 'u32_'}, {'name': 'used_btf_cnt', 'type': 'u32_'}, {'name': 'max_ctx_offset', 'type': 'u32_'}, {'name': 'max_pkt_offset', 'type': 'u32_'}, {'name': 'max_tp_access', 'type': 'u32_'}, {'name': 'stack_depth', 'type': 'u32_'}, {'name': 'id', 'type': 'u32_'}, {'name': 'func_cnt', 'type': 'u32_'}, {'name': 'real_func_cnt', 'type': 'u32_'}, {'name': 'func_idx', 'type': 'u32_'}, {'name': 'attach_btf_id', 'type': 'u32_'}, {'name': 'attach_st_ops_member_off', 'type': 'u32_'}, {'name': 'ctx_arg_info_size', 'type': 'u32_'}, {'name': 'max_rdonly_access', 'type': 'u32_'}, {'name': 'max_rdwr_access', 'type': 'u32_'}, {'name': 'attach_btf', 'type': '*mut btf'}, {'name': 'ctx_arg_info', 'type': '*mut bpf_ctx_arg_aux'}, {'name': 'priv_stack_ptr', 'type': '*mut ffi::c_void'}, {'name': 'dst_mutex', 'type': 'mutex'}, {'name': 'dst_prog', 'type': '*mut bpf_prog'}, {'name': 'dst_trampoline', 'type': '*mut bpf_trampoline'}, {'name': 'saved_dst_prog_type', 'type': 'bpf_prog_type'}, {'name': 'saved_dst_attach_type', 'type': 'bpf_attach_type'}, {'name': 'verifier_zext', 'type': 'bool_'}, {'name': 'dev_bound', 'type': 'bool_'}, {'name': 'offload_requested', 'type': 'bool_'}, {'name': 'attach_btf_trace', 'type': 'bool_'}, {'name': 'attach_tracing_prog', 'type': 'bool_'}, {'name': 'func_proto_unreliable', 'type': 'bool_'}, {'name': 'tail_call_reachable', 'type': 'bool_'}, {'name': 'xdp_has_frags', 'type': 'bool_'}, {'name': 'exception_cb', 'type': 'bool_'}, {'name': 'exception_boundary', 'type': 'bool_'}, {'name': 'is_extended', 'type': 'bool_'}, {'name': 'jits_use_priv_stack', 'type': 'bool_'}, {'name': 'priv_stack_requested', 'type': 'bool_'}, {'name': 'changes_pkt_data', 'type': 'bool_'}, {'name': 'might_sleep', 'type': 'bool_'}, {'name': 'prog_array_member_cnt', 'type': 'u64_'}, {'name': 'ext_mutex', 'type': 'mutex'}, {'name': 'arena', 'type': '*mut bpf_arena'}, {'name': 'recursion_detected', 'type': '::core::option::Option<unsafe extern "C" fn(prog: *mut bpf_prog)>'}, {'name': 'attach_func_proto', 'type': '*const btf_type'}, {'name': 'attach_func_name', 'type': '*const ffi::c_char'}, {'name': 'func', 'type': '*mut *mut bpf_prog'}, {'name': 'jit_data', 'type': '*mut ffi::c_void'}, {'name': 'poke_tab', 'type': '*mut bpf_jit_poke_descriptor'}, {'name': 'kfunc_tab', 'type': '*mut bpf_kfunc_desc_tab'}, {'name': 'kfunc_btf_tab', 'type': '*mut bpf_kfunc_btf_tab'}, {'name': 'size_poke_tab', 'type': 'u32_'}, {'name': 'ksym', 'type': 'bpf_ksym'}, {'name': 'ops', 'type': '*const bpf_prog_ops'}, {'name': 'st_ops', 'type': '*const bpf_struct_ops'}, {'name': 'used_maps', 'type': '*mut *mut bpf_map'}, {'name': 'used_maps_mutex', 'type': 'mutex'}, {'name': 'used_btfs', 'type': '*mut btf_mod_pair'}, {'name': 'prog', 'type': '*mut bpf_prog'}, {'name': 'user', 'type': '*mut user_struct'}, {'name': 'load_time', 'type': 'u64_'}, {'name': 'verified_insns', 'type': 'u32_'}, {'name': 'cgroup_atype', 'type': 'ffi::c_int'}, {'name': 'cgroup_storage', 'type': '[*mut bpf_map; 2usize]'}, {'name': 'name', 'type': '[ffi::c_char; 16usize]'}, {'name': 'bpf_exception_cb', 'type': '::core::option::Option<'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'token', 'type': '*mut bpf_token'}, {'name': 'offload', 'type': '*mut bpf_prog_offload'}, {'name': 'btf', 'type': '*mut btf'}, {'name': 'func_info', 'type': '*mut bpf_func_info'}, {'name': 'func_info_aux', 'type': '*mut bpf_func_info_aux'}, {'name': 'linfo', 'type': '*mut bpf_line_info'}, {'name': 'jited_linfo', 'type': '*mut *mut ffi::c_void'}, {'name': 'func_info_cnt', 'type': 'u32_'}, {'name': 'nr_linfo', 'type': 'u32_'}, {'name': 'linfo_idx', 'type': 'u32_'}, {'name': 'mod_', 'type': '*mut module'}, {'name': 'num_exentries', 'type': 'u32_'}, {'name': 'extable', 'type': '*mut exception_table_entry'}, {'name': '__bindgen_anon_1', 'type': 'bpf_prog_aux__bindgen_ty_1'}]`

### Rust Evidence

- Graph edges: `1`

## W-000196 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: btf_record
- Explanation: btf_record changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'cnt', 'type': 'u32_'}, {'name': 'field_mask', 'type': 'u32_'}, {'name': 'spin_lock_off', 'type': 'ffi::c_int'}, {'name': 'timer_off', 'type': 'ffi::c_int'}, {'name': 'wq_off', 'type': 'ffi::c_int'}, {'name': 'refcount_off', 'type': 'ffi::c_int'}, {'name': 'fields', 'type': '__IncompleteArrayField<btf_field>'}]`
- New: `[{'name': 'cnt', 'type': 'u32_'}, {'name': 'field_mask', 'type': 'u32_'}, {'name': 'spin_lock_off', 'type': 'ffi::c_int'}, {'name': 'res_spin_lock_off', 'type': 'ffi::c_int'}, {'name': 'timer_off', 'type': 'ffi::c_int'}, {'name': 'wq_off', 'type': 'ffi::c_int'}, {'name': 'refcount_off', 'type': 'ffi::c_int'}, {'name': 'fields', 'type': '__IncompleteArrayField<btf_field>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000197 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: callthunk_sites
- Explanation: callthunk_sites changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'call_start', 'type': '*mut s32'}, {'name': 'call_end', 'type': '*mut s32'}, {'name': 'alt_start', 'type': '*mut alt_instr'}, {'name': 'alt_end', 'type': '*mut alt_instr'}]`
- New: `[{'name': 'call_start', 'type': '*mut s32'}, {'name': 'call_end', 'type': '*mut s32'}]`

### Rust Evidence

- Graph edges: `1`

## W-000199 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: ethtool_ops
- Explanation: ethtool_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rxfh_indir_space', 'type': 'u32_'}, {'name': 'rxfh_key_space', 'type': 'u16_'}, {'name': 'rxfh_priv_size', 'type': 'u16_'}, {'name': 'rxfh_max_num_contexts', 'type': 'u32_'}, {'name': 'supported_coalesce_params', 'type': 'u32_'}, {'name': 'supported_ring_params', 'type': 'u32_'}, {'name': 'supported_hwtstamp_qualifiers', 'type': 'u32_'}, {'name': 'get_drvinfo', 'type': '::core::option::Option<'}, {'name': 'get_regs', 'type': '::core::option::Option<'}, {'name': 'get_wol', 'type': '::core::option::Option<'}, {'name': 'set_wol', 'type': '::core::option::Option<'}, {'name': 'get_msglevel', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'get_link', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'get_link_ext_state', 'type': '::core::option::Option<'}, {'name': 'get_link_ext_stats', 'type': '::core::option::Option<'}, {'name': 'get_eeprom', 'type': '::core::option::Option<'}, {'name': 'set_eeprom', 'type': '::core::option::Option<'}, {'name': 'get_coalesce', 'type': '::core::option::Option<'}, {'name': 'set_coalesce', 'type': '::core::option::Option<'}, {'name': 'get_ringparam', 'type': '::core::option::Option<'}, {'name': 'set_ringparam', 'type': '::core::option::Option<'}, {'name': 'get_pause_stats', 'type': '::core::option::Option<'}, {'name': 'get_pauseparam', 'type': '::core::option::Option<'}, {'name': 'set_pauseparam', 'type': '::core::option::Option<'}, {'name': 'self_test', 'type': '::core::option::Option<'}, {'name': 'get_strings', 'type': '::core::option::Option<'}, {'name': 'set_phys_id', 'type': '::core::option::Option<'}, {'name': 'get_ethtool_stats', 'type': '::core::option::Option<'}, {'name': 'begin', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> ffi::c_int>'}, {'name': 'complete', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device)>'}, {'name': 'get_priv_flags', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'set_priv_flags', 'type': '::core::option::Option<'}, {'name': 'get_sset_count', 'type': '::core::option::Option<'}, {'name': 'get_rxnfc', 'type': '::core::option::Option<'}, {'name': 'set_rxnfc', 'type': '::core::option::Option<'}, {'name': 'flash_device', 'type': '::core::option::Option<'}, {'name': 'reset', 'type': '::core::option::Option<'}, {'name': 'get_rxfh', 'type': '::core::option::Option<'}, {'name': 'set_rxfh', 'type': '::core::option::Option<'}, {'name': 'create_rxfh_context', 'type': '::core::option::Option<'}, {'name': 'modify_rxfh_context', 'type': '::core::option::Option<'}, {'name': 'remove_rxfh_context', 'type': '::core::option::Option<'}, {'name': 'get_channels', 'type': '::core::option::Option<'}, {'name': 'set_channels', 'type': '::core::option::Option<'}, {'name': 'get_dump_flag', 'type': '::core::option::Option<'}, {'name': 'get_dump_data', 'type': '::core::option::Option<'}, {'name': 'set_dump', 'type': '::core::option::Option<'}, {'name': 'get_ts_info', 'type': '::core::option::Option<'}, {'name': 'get_ts_stats', 'type': '::core::option::Option<'}, {'name': 'get_module_info', 'type': '::core::option::Option<'}, {'name': 'get_module_eeprom', 'type': '::core::option::Option<'}, {'name': 'get_eee', 'type': '::core::option::Option<'}, {'name': 'set_eee', 'type': '::core::option::Option<'}, {'name': 'get_tunable', 'type': '::core::option::Option<'}, {'name': 'set_tunable', 'type': '::core::option::Option<'}, {'name': 'get_per_queue_coalesce', 'type': '::core::option::Option<'}, {'name': 'set_per_queue_coalesce', 'type': '::core::option::Option<'}, {'name': 'get_link_ksettings', 'type': '::core::option::Option<'}, {'name': 'set_link_ksettings', 'type': '::core::option::Option<'}, {'name': 'get_fec_stats', 'type': '::core::option::Option<'}, {'name': 'get_fecparam', 'type': '::core::option::Option<'}, {'name': 'set_fecparam', 'type': '::core::option::Option<'}, {'name': 'get_ethtool_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_phy_tunable', 'type': '::core::option::Option<'}, {'name': 'set_phy_tunable', 'type': '::core::option::Option<'}, {'name': 'get_module_eeprom_by_page', 'type': '::core::option::Option<'}, {'name': 'set_module_eeprom_by_page', 'type': '::core::option::Option<'}, {'name': 'get_eth_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_eth_mac_stats', 'type': '::core::option::Option<'}, {'name': 'get_eth_ctrl_stats', 'type': '::core::option::Option<'}, {'name': 'get_rmon_stats', 'type': '::core::option::Option<'}, {'name': 'get_module_power_mode', 'type': '::core::option::Option<'}, {'name': 'set_module_power_mode', 'type': '::core::option::Option<'}, {'name': 'get_mm', 'type': '::core::option::Option<'}, {'name': 'set_mm', 'type': '::core::option::Option<'}, {'name': 'get_mm_stats', 'type': '::core::option::Option<'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'rxfh_indir_space', 'type': 'u32_'}, {'name': 'rxfh_key_space', 'type': 'u16_'}, {'name': 'rxfh_priv_size', 'type': 'u16_'}, {'name': 'rxfh_max_num_contexts', 'type': 'u32_'}, {'name': 'supported_coalesce_params', 'type': 'u32_'}, {'name': 'supported_ring_params', 'type': 'u32_'}, {'name': 'supported_hwtstamp_qualifiers', 'type': 'u32_'}, {'name': 'get_drvinfo', 'type': '::core::option::Option<'}, {'name': 'get_regs', 'type': '::core::option::Option<'}, {'name': 'get_wol', 'type': '::core::option::Option<'}, {'name': 'set_wol', 'type': '::core::option::Option<'}, {'name': 'get_msglevel', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'get_link', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'get_link_ext_state', 'type': '::core::option::Option<'}, {'name': 'get_link_ext_stats', 'type': '::core::option::Option<'}, {'name': 'get_eeprom', 'type': '::core::option::Option<'}, {'name': 'set_eeprom', 'type': '::core::option::Option<'}, {'name': 'get_coalesce', 'type': '::core::option::Option<'}, {'name': 'set_coalesce', 'type': '::core::option::Option<'}, {'name': 'get_ringparam', 'type': '::core::option::Option<'}, {'name': 'set_ringparam', 'type': '::core::option::Option<'}, {'name': 'get_pause_stats', 'type': '::core::option::Option<'}, {'name': 'get_pauseparam', 'type': '::core::option::Option<'}, {'name': 'set_pauseparam', 'type': '::core::option::Option<'}, {'name': 'self_test', 'type': '::core::option::Option<'}, {'name': 'get_strings', 'type': '::core::option::Option<'}, {'name': 'set_phys_id', 'type': '::core::option::Option<'}, {'name': 'get_ethtool_stats', 'type': '::core::option::Option<'}, {'name': 'begin', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> ffi::c_int>'}, {'name': 'complete', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device)>'}, {'name': 'get_priv_flags', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'set_priv_flags', 'type': '::core::option::Option<'}, {'name': 'get_sset_count', 'type': '::core::option::Option<'}, {'name': 'get_rxnfc', 'type': '::core::option::Option<'}, {'name': 'set_rxnfc', 'type': '::core::option::Option<'}, {'name': 'flash_device', 'type': '::core::option::Option<'}, {'name': 'reset', 'type': '::core::option::Option<'}, {'name': 'get_rxfh', 'type': '::core::option::Option<'}, {'name': 'set_rxfh', 'type': '::core::option::Option<'}, {'name': 'create_rxfh_context', 'type': '::core::option::Option<'}, {'name': 'modify_rxfh_context', 'type': '::core::option::Option<'}, {'name': 'remove_rxfh_context', 'type': '::core::option::Option<'}, {'name': 'get_channels', 'type': '::core::option::Option<'}, {'name': 'set_channels', 'type': '::core::option::Option<'}, {'name': 'get_dump_flag', 'type': '::core::option::Option<'}, {'name': 'get_dump_data', 'type': '::core::option::Option<'}, {'name': 'set_dump', 'type': '::core::option::Option<'}, {'name': 'get_ts_info', 'type': '::core::option::Option<'}, {'name': 'get_ts_stats', 'type': '::core::option::Option<'}, {'name': 'get_module_info', 'type': '::core::option::Option<'}, {'name': 'get_module_eeprom', 'type': '::core::option::Option<'}, {'name': 'get_eee', 'type': '::core::option::Option<'}, {'name': 'set_eee', 'type': '::core::option::Option<'}, {'name': 'get_tunable', 'type': '::core::option::Option<'}, {'name': 'set_tunable', 'type': '::core::option::Option<'}, {'name': 'get_per_queue_coalesce', 'type': '::core::option::Option<'}, {'name': 'set_per_queue_coalesce', 'type': '::core::option::Option<'}, {'name': 'get_link_ksettings', 'type': '::core::option::Option<'}, {'name': 'set_link_ksettings', 'type': '::core::option::Option<'}, {'name': 'get_fec_stats', 'type': '::core::option::Option<'}, {'name': 'get_fecparam', 'type': '::core::option::Option<'}, {'name': 'set_fecparam', 'type': '::core::option::Option<'}, {'name': 'get_ethtool_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_phy_tunable', 'type': '::core::option::Option<'}, {'name': 'set_phy_tunable', 'type': '::core::option::Option<'}, {'name': 'get_module_eeprom_by_page', 'type': '::core::option::Option<'}, {'name': 'set_module_eeprom_by_page', 'type': '::core::option::Option<'}, {'name': 'get_eth_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_eth_mac_stats', 'type': '::core::option::Option<'}, {'name': 'get_eth_ctrl_stats', 'type': '::core::option::Option<'}, {'name': 'get_rmon_stats', 'type': '::core::option::Option<'}, {'name': 'get_module_power_mode', 'type': '::core::option::Option<'}, {'name': 'set_module_power_mode', 'type': '::core::option::Option<'}, {'name': 'get_mm', 'type': '::core::option::Option<'}, {'name': 'set_mm', 'type': '::core::option::Option<'}, {'name': 'get_mm_stats', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-000204 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: folio__bindgen_ty_3__bindgen_ty_1
- Explanation: folio__bindgen_ty_3__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_flags_2', 'type': 'ffi::c_ulong'}, {'name': '_head_2', 'type': 'ffi::c_ulong'}, {'name': '_hugetlb_subpool', 'type': '*mut ffi::c_void'}, {'name': '_hugetlb_cgroup', 'type': '*mut ffi::c_void'}, {'name': '_hugetlb_cgroup_rsvd', 'type': '*mut ffi::c_void'}, {'name': '_hugetlb_hwpoison', 'type': '*mut ffi::c_void'}]`
- New: `[{'name': '_flags_2', 'type': 'ffi::c_ulong'}, {'name': '_head_2', 'type': 'ffi::c_ulong'}, {'name': '_deferred_list', 'type': 'list_head'}]`

### Rust Evidence

- Graph edges: `1`

## W-000205 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: follow_pfnmap_args
- Explanation: follow_pfnmap_args changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'address', 'type': 'ffi::c_ulong'}, {'name': 'lock', 'type': '*mut spinlock_t'}, {'name': 'ptep', 'type': '*mut pte_t'}, {'name': 'pfn', 'type': 'ffi::c_ulong'}, {'name': 'pgprot', 'type': 'pgprot_t'}, {'name': 'writable', 'type': 'bool_'}, {'name': 'special', 'type': 'bool_'}]`
- New: `[{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'address', 'type': 'ffi::c_ulong'}, {'name': 'lock', 'type': '*mut spinlock_t'}, {'name': 'ptep', 'type': '*mut pte_t'}, {'name': 'pfn', 'type': 'ffi::c_ulong'}, {'name': 'addr_mask', 'type': 'ffi::c_ulong'}, {'name': 'pgprot', 'type': 'pgprot_t'}, {'name': 'writable', 'type': 'bool_'}, {'name': 'special', 'type': 'bool_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000206 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: fwnode_reference_args
- Explanation: fwnode_reference_args changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'nargs', 'type': 'ffi::c_uint'}, {'name': 'args', 'type': '[u64_; 8usize]'}]`
- New: `[{'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'nargs', 'type': 'ffi::c_uint'}, {'name': 'args', 'type': '[u64_; 16usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000209 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: mm_context_t
- Explanation: mm_context_t changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'ctx_id', 'type': 'u64_'}, {'name': 'tlb_gen', 'type': 'atomic64_t'}, {'name': 'next_trim_cpumask', 'type': 'ffi::c_ulong'}, {'name': 'ldt_usr_sem', 'type': 'rw_semaphore'}, {'name': 'ldt', 'type': '*mut ldt_struct'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'lock', 'type': 'mutex'}, {'name': 'vdso', 'type': '*mut ffi::c_void'}, {'name': 'vdso_image', 'type': '*const vdso_image'}, {'name': 'perf_rdpmc_allowed', 'type': 'atomic_t'}, {'name': 'pkey_allocation_map', 'type': 'u16_'}, {'name': 'execute_only_pkey', 'type': 's16'}]`
- New: `[{'name': 'ctx_id', 'type': 'u64_'}, {'name': 'tlb_gen', 'type': 'atomic64_t'}, {'name': 'next_trim_cpumask', 'type': 'ffi::c_ulong'}, {'name': 'ldt_usr_sem', 'type': 'rw_semaphore'}, {'name': 'ldt', 'type': '*mut ldt_struct'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'lock', 'type': 'mutex'}, {'name': 'vdso', 'type': '*mut ffi::c_void'}, {'name': 'vdso_image', 'type': '*const vdso_image'}, {'name': 'perf_rdpmc_allowed', 'type': 'atomic_t'}, {'name': 'pkey_allocation_map', 'type': 'u16_'}, {'name': 'execute_only_pkey', 'type': 's16'}, {'name': 'global_asid', 'type': 'u16_'}, {'name': 'asid_transition', 'type': 'bool_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000212 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: module_memory
- Explanation: module_memory changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'base', 'type': '*mut ffi::c_void'}, {'name': 'rw_copy', 'type': '*mut ffi::c_void'}, {'name': 'is_rox', 'type': 'bool_'}, {'name': 'size', 'type': 'ffi::c_uint'}, {'name': 'mtn', 'type': 'mod_tree_node'}]`
- New: `[{'name': 'base', 'type': '*mut ffi::c_void'}, {'name': 'is_rox', 'type': 'bool_'}, {'name': 'size', 'type': 'ffi::c_uint'}, {'name': 'mtn', 'type': 'mod_tree_node'}]`

### Rust Evidence

- Graph edges: `1`

## W-000214 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: node_cache_attrs
- Explanation: node_cache_attrs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'indexing', 'type': 'cache_indexing'}, {'name': 'write_policy', 'type': 'cache_write_policy'}, {'name': 'size', 'type': 'u64_'}, {'name': 'line_size', 'type': 'u16_'}, {'name': 'level', 'type': 'u8_'}]`
- New: `[{'name': 'indexing', 'type': 'cache_indexing'}, {'name': 'write_policy', 'type': 'cache_write_policy'}, {'name': 'size', 'type': 'u64_'}, {'name': 'line_size', 'type': 'u16_'}, {'name': 'level', 'type': 'u8_'}, {'name': 'address_mode', 'type': 'u16_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000215 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: page__bindgen_ty_1__bindgen_ty_4
- Explanation: page__bindgen_ty_1__bindgen_ty_4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'pgmap', 'type': '*mut dev_pagemap'}, {'name': 'zone_device_data', 'type': '*mut ffi::c_void'}]`
- New: `[{'name': '_unused_pgmap_compound_head', 'type': '*mut ffi::c_void'}, {'name': 'zone_device_data', 'type': '*mut ffi::c_void'}]`

### Rust Evidence

- Graph edges: `1`

## W-000218 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: per_cpu_nodestat
- Explanation: per_cpu_nodestat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'stat_threshold', 'type': 's8'}, {'name': 'vm_node_stat_diff', 'type': '[s8; 46usize]'}]`
- New: `[{'name': 'stat_threshold', 'type': 's8'}, {'name': 'vm_node_stat_diff', 'type': '[s8; 48usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000219 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: per_cpu_zonestat
- Explanation: per_cpu_zonestat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'vm_stat_diff', 'type': '[s8; 10usize]'}, {'name': 'stat_threshold', 'type': 's8'}, {'name': 'vm_numa_event', 'type': '[ffi::c_ulong; 6usize]'}]`
- New: `[{'name': 'vm_stat_diff', 'type': '[s8; 11usize]'}, {'name': 'stat_threshold', 'type': 's8'}, {'name': 'vm_numa_event', 'type': '[ffi::c_ulong; 6usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000220 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: pglist_data
- Explanation: pglist_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'node_zones', 'type': '[zone; 4usize]'}, {'name': 'node_zonelists', 'type': '[zonelist; 2usize]'}, {'name': 'nr_zones', 'type': 'ffi::c_int'}, {'name': 'node_start_pfn', 'type': 'ffi::c_ulong'}, {'name': 'node_present_pages', 'type': 'ffi::c_ulong'}, {'name': 'node_spanned_pages', 'type': 'ffi::c_ulong'}, {'name': 'node_id', 'type': 'ffi::c_int'}, {'name': 'kswapd_wait', 'type': 'wait_queue_head_t'}, {'name': 'pfmemalloc_wait', 'type': 'wait_queue_head_t'}, {'name': 'reclaim_wait', 'type': '[wait_queue_head_t; 4usize]'}, {'name': 'nr_writeback_throttled', 'type': 'atomic_t'}, {'name': 'nr_reclaim_start', 'type': 'ffi::c_ulong'}, {'name': 'kswapd', 'type': '*mut task_struct'}, {'name': 'kswapd_order', 'type': 'ffi::c_int'}, {'name': 'kswapd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kswapd_failures', 'type': 'ffi::c_int'}, {'name': 'kcompactd_max_order', 'type': 'ffi::c_int'}, {'name': 'kcompactd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kcompactd_wait', 'type': 'wait_queue_head_t'}, {'name': 'kcompactd', 'type': '*mut task_struct'}, {'name': 'proactive_compact_trigger', 'type': 'bool_'}, {'name': 'totalreserve_pages', 'type': 'ffi::c_ulong'}, {'name': 'min_unmapped_pages', 'type': 'ffi::c_ulong'}, {'name': 'min_slab_pages', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': '__lruvec', 'type': 'lruvec'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_padding_1', 'type': '[u64; 6usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'per_cpu_nodestats', 'type': '*mut per_cpu_nodestat'}, {'name': 'vm_stat', 'type': '[atomic_long_t; 46usize]'}, {'name': 'memtier', 'type': '*mut memory_tier'}]`
- New: `[{'name': 'node_zones', 'type': '[zone; 4usize]'}, {'name': 'node_zonelists', 'type': '[zonelist; 2usize]'}, {'name': 'nr_zones', 'type': 'ffi::c_int'}, {'name': 'node_start_pfn', 'type': 'ffi::c_ulong'}, {'name': 'node_present_pages', 'type': 'ffi::c_ulong'}, {'name': 'node_spanned_pages', 'type': 'ffi::c_ulong'}, {'name': 'node_id', 'type': 'ffi::c_int'}, {'name': 'kswapd_wait', 'type': 'wait_queue_head_t'}, {'name': 'pfmemalloc_wait', 'type': 'wait_queue_head_t'}, {'name': 'reclaim_wait', 'type': '[wait_queue_head_t; 4usize]'}, {'name': 'nr_writeback_throttled', 'type': 'atomic_t'}, {'name': 'nr_reclaim_start', 'type': 'ffi::c_ulong'}, {'name': 'kswapd', 'type': '*mut task_struct'}, {'name': 'kswapd_order', 'type': 'ffi::c_int'}, {'name': 'kswapd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kswapd_failures', 'type': 'ffi::c_int'}, {'name': 'kcompactd_max_order', 'type': 'ffi::c_int'}, {'name': 'kcompactd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kcompactd_wait', 'type': 'wait_queue_head_t'}, {'name': 'kcompactd', 'type': '*mut task_struct'}, {'name': 'proactive_compact_trigger', 'type': 'bool_'}, {'name': 'totalreserve_pages', 'type': 'ffi::c_ulong'}, {'name': 'min_unmapped_pages', 'type': 'ffi::c_ulong'}, {'name': 'min_slab_pages', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': '__lruvec', 'type': 'lruvec'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_padding_1', 'type': '[u64; 6usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'per_cpu_nodestats', 'type': '*mut per_cpu_nodestat'}, {'name': 'vm_stat', 'type': '[atomic_long_t; 48usize]'}, {'name': 'memtier', 'type': '*mut memory_tier'}]`

### Rust Evidence

- Graph edges: `1`

## W-000222 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: phy_package_shared
- Explanation: phy_package_shared changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'base_addr', 'type': 'u8_'}, {'name': 'np', 'type': '*mut device_node'}, {'name': 'refcnt', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'priv_size', 'type': 'usize'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}]`
- New: `[{'name': '_address', 'type': 'u8'}]`

### Rust Evidence

- Graph edges: `1`

## W-000223 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: pv_irq_ops
- Explanation: pv_irq_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'safe_halt', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'halt', 'type': '::core::option::Option<unsafe extern "C" fn()>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000224 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: request_queue
- Explanation: request_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'queuedata', 'type': '*mut ffi::c_void'}, {'name': 'elevator', 'type': '*mut elevator_queue'}, {'name': 'mq_ops', 'type': '*const blk_mq_ops'}, {'name': 'queue_ctx', 'type': '*mut blk_mq_ctx'}, {'name': 'queue_flags', 'type': 'ffi::c_ulong'}, {'name': 'rq_timeout', 'type': 'ffi::c_uint'}, {'name': 'queue_depth', 'type': 'ffi::c_uint'}, {'name': 'refs', 'type': 'refcount_t'}, {'name': 'nr_hw_queues', 'type': 'ffi::c_uint'}, {'name': 'hctx_table', 'type': 'xarray'}, {'name': 'q_usage_counter', 'type': 'percpu_ref'}, {'name': 'io_lock_cls_key', 'type': 'lock_class_key'}, {'name': 'io_lockdep_map', 'type': 'lockdep_map'}, {'name': 'q_lock_cls_key', 'type': 'lock_class_key'}, {'name': 'q_lockdep_map', 'type': 'lockdep_map'}, {'name': 'last_merge', 'type': '*mut request'}, {'name': 'queue_lock', 'type': 'spinlock_t'}, {'name': 'quiesce_depth', 'type': 'ffi::c_int'}, {'name': 'disk', 'type': '*mut gendisk'}, {'name': 'mq_kobj', 'type': '*mut kobject'}, {'name': 'limits', 'type': 'queue_limits'}, {'name': 'dev', 'type': '*mut device'}, {'name': 'rpm_status', 'type': 'rpm_status'}, {'name': 'pm_only', 'type': 'atomic_t'}, {'name': 'stats', 'type': '*mut blk_queue_stats'}, {'name': 'rq_qos', 'type': '*mut rq_qos'}, {'name': 'rq_qos_mutex', 'type': 'mutex'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'nr_requests', 'type': 'ffi::c_ulong'}, {'name': 'timeout', 'type': 'timer_list'}, {'name': 'timeout_work', 'type': 'work_struct'}, {'name': 'nr_active_requests_shared_tags', 'type': 'atomic_t'}, {'name': 'sched_shared_tags', 'type': '*mut blk_mq_tags'}, {'name': 'icq_list', 'type': 'list_head'}, {'name': 'blkcg_pols', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'root_blkg', 'type': '*mut blkcg_gq'}, {'name': 'blkg_list', 'type': 'list_head'}, {'name': 'blkcg_mutex', 'type': 'mutex'}, {'name': 'node', 'type': 'ffi::c_int'}, {'name': 'requeue_lock', 'type': 'spinlock_t'}, {'name': 'requeue_list', 'type': 'list_head'}, {'name': 'requeue_work', 'type': 'delayed_work'}, {'name': 'blk_trace', 'type': '*mut blk_trace'}, {'name': 'fq', 'type': '*mut blk_flush_queue'}, {'name': 'flush_list', 'type': 'list_head'}, {'name': 'sysfs_lock', 'type': 'mutex'}, {'name': 'limits_lock', 'type': 'mutex'}, {'name': 'unused_hctx_list', 'type': 'list_head'}, {'name': 'unused_hctx_lock', 'type': 'spinlock_t'}, {'name': 'mq_freeze_depth', 'type': 'ffi::c_int'}, {'name': 'callback_head', 'type': 'callback_head'}, {'name': 'mq_freeze_wq', 'type': 'wait_queue_head_t'}, {'name': 'mq_freeze_lock', 'type': 'mutex'}, {'name': 'tag_set', 'type': '*mut blk_mq_tag_set'}, {'name': 'tag_set_list', 'type': 'list_head'}, {'name': 'debugfs_dir', 'type': '*mut dentry'}, {'name': 'sched_debugfs_dir', 'type': '*mut dentry'}, {'name': 'rqos_debugfs_dir', 'type': '*mut dentry'}, {'name': 'debugfs_mutex', 'type': 'mutex'}]`
- New: `[{'name': 'queuedata', 'type': '*mut ffi::c_void'}, {'name': 'elevator', 'type': '*mut elevator_queue'}, {'name': 'mq_ops', 'type': '*const blk_mq_ops'}, {'name': 'queue_ctx', 'type': '*mut blk_mq_ctx'}, {'name': 'queue_flags', 'type': 'ffi::c_ulong'}, {'name': 'rq_timeout', 'type': 'ffi::c_uint'}, {'name': 'queue_depth', 'type': 'ffi::c_uint'}, {'name': 'refs', 'type': 'refcount_t'}, {'name': 'nr_hw_queues', 'type': 'ffi::c_uint'}, {'name': 'hctx_table', 'type': 'xarray'}, {'name': 'q_usage_counter', 'type': 'percpu_ref'}, {'name': 'io_lock_cls_key', 'type': 'lock_class_key'}, {'name': 'io_lockdep_map', 'type': 'lockdep_map'}, {'name': 'q_lock_cls_key', 'type': 'lock_class_key'}, {'name': 'q_lockdep_map', 'type': 'lockdep_map'}, {'name': 'last_merge', 'type': '*mut request'}, {'name': 'queue_lock', 'type': 'spinlock_t'}, {'name': 'quiesce_depth', 'type': 'ffi::c_int'}, {'name': 'disk', 'type': '*mut gendisk'}, {'name': 'mq_kobj', 'type': '*mut kobject'}, {'name': 'limits', 'type': 'queue_limits'}, {'name': 'dev', 'type': '*mut device'}, {'name': 'rpm_status', 'type': 'rpm_status'}, {'name': 'pm_only', 'type': 'atomic_t'}, {'name': 'stats', 'type': '*mut blk_queue_stats'}, {'name': 'rq_qos', 'type': '*mut rq_qos'}, {'name': 'rq_qos_mutex', 'type': 'mutex'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'nr_requests', 'type': 'ffi::c_ulong'}, {'name': 'timeout', 'type': 'timer_list'}, {'name': 'timeout_work', 'type': 'work_struct'}, {'name': 'nr_active_requests_shared_tags', 'type': 'atomic_t'}, {'name': 'sched_shared_tags', 'type': '*mut blk_mq_tags'}, {'name': 'icq_list', 'type': 'list_head'}, {'name': 'blkcg_pols', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'root_blkg', 'type': '*mut blkcg_gq'}, {'name': 'blkg_list', 'type': 'list_head'}, {'name': 'blkcg_mutex', 'type': 'mutex'}, {'name': 'node', 'type': 'ffi::c_int'}, {'name': 'requeue_lock', 'type': 'spinlock_t'}, {'name': 'requeue_list', 'type': 'list_head'}, {'name': 'requeue_work', 'type': 'delayed_work'}, {'name': 'blk_trace', 'type': '*mut blk_trace'}, {'name': 'fq', 'type': '*mut blk_flush_queue'}, {'name': 'flush_list', 'type': 'list_head'}, {'name': 'elevator_lock', 'type': 'mutex'}, {'name': 'sysfs_lock', 'type': 'mutex'}, {'name': 'limits_lock', 'type': 'mutex'}, {'name': 'unused_hctx_list', 'type': 'list_head'}, {'name': 'unused_hctx_lock', 'type': 'spinlock_t'}, {'name': 'mq_freeze_depth', 'type': 'ffi::c_int'}, {'name': 'callback_head', 'type': 'callback_head'}, {'name': 'mq_freeze_wq', 'type': 'wait_queue_head_t'}, {'name': 'mq_freeze_lock', 'type': 'mutex'}, {'name': 'tag_set', 'type': '*mut blk_mq_tag_set'}, {'name': 'tag_set_list', 'type': 'list_head'}, {'name': 'debugfs_dir', 'type': '*mut dentry'}, {'name': 'sched_debugfs_dir', 'type': '*mut dentry'}, {'name': 'rqos_debugfs_dir', 'type': '*mut dentry'}, {'name': 'debugfs_mutex', 'type': 'mutex'}]`

### Rust Evidence

- Graph edges: `1`

## W-000225 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: signal_struct
- Explanation: signal_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'sigcnt', 'type': 'refcount_t'}, {'name': 'live', 'type': 'atomic_t'}, {'name': 'nr_threads', 'type': 'ffi::c_int'}, {'name': 'quick_threads', 'type': 'ffi::c_int'}, {'name': 'thread_head', 'type': 'list_head'}, {'name': 'wait_chldexit', 'type': 'wait_queue_head_t'}, {'name': 'curr_target', 'type': '*mut task_struct'}, {'name': 'shared_pending', 'type': 'sigpending'}, {'name': 'multiprocess', 'type': 'hlist_head'}, {'name': 'group_exit_code', 'type': 'ffi::c_int'}, {'name': 'notify_count', 'type': 'ffi::c_int'}, {'name': 'group_exec_task', 'type': '*mut task_struct'}, {'name': 'group_stop_count', 'type': 'ffi::c_int'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'core_state', 'type': '*mut core_state'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'next_posix_timer_id', 'type': 'ffi::c_uint'}, {'name': 'posix_timers', 'type': 'hlist_head'}, {'name': 'ignored_posix_timers', 'type': 'hlist_head'}, {'name': 'real_timer', 'type': 'hrtimer'}, {'name': 'it_real_incr', 'type': 'ktime_t'}, {'name': 'it', 'type': '[cpu_itimer; 2usize]'}, {'name': 'cputimer', 'type': 'thread_group_cputimer'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'pids', 'type': '[*mut pid; 4usize]'}, {'name': 'tty_old_pgrp', 'type': '*mut pid'}, {'name': 'leader', 'type': 'ffi::c_int'}, {'name': 'tty', 'type': '*mut tty_struct'}, {'name': 'stats_lock', 'type': 'seqlock_t'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'cutime', 'type': 'u64_'}, {'name': 'cstime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'cgtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'ffi::c_ulong'}, {'name': 'cnvcsw', 'type': 'ffi::c_ulong'}, {'name': 'cnivcsw', 'type': 'ffi::c_ulong'}, {'name': 'min_flt', 'type': 'ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'ffi::c_ulong'}, {'name': 'cmin_flt', 'type': 'ffi::c_ulong'}, {'name': 'cmaj_flt', 'type': 'ffi::c_ulong'}, {'name': 'inblock', 'type': 'ffi::c_ulong'}, {'name': 'oublock', 'type': 'ffi::c_ulong'}, {'name': 'cinblock', 'type': 'ffi::c_ulong'}, {'name': 'coublock', 'type': 'ffi::c_ulong'}, {'name': 'maxrss', 'type': 'ffi::c_ulong'}, {'name': 'cmaxrss', 'type': 'ffi::c_ulong'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'sum_sched_runtime', 'type': 'ffi::c_ulonglong'}, {'name': 'rlim', 'type': '[rlimit; 16usize]'}, {'name': 'pacct', 'type': 'pacct_struct'}, {'name': 'stats', 'type': '*mut taskstats'}, {'name': 'audit_tty', 'type': 'ffi::c_uint'}, {'name': 'tty_audit_buf', 'type': '*mut tty_audit_buf'}, {'name': 'oom_flag_origin', 'type': 'bool_'}, {'name': 'oom_score_adj', 'type': 'ffi::c_short'}, {'name': 'oom_score_adj_min', 'type': 'ffi::c_short'}, {'name': 'oom_mm', 'type': '*mut mm_struct'}, {'name': 'cred_guard_mutex', 'type': 'mutex'}, {'name': 'exec_update_lock', 'type': 'rw_semaphore'}]`
- New: `[{'name': 'sigcnt', 'type': 'refcount_t'}, {'name': 'live', 'type': 'atomic_t'}, {'name': 'nr_threads', 'type': 'ffi::c_int'}, {'name': 'quick_threads', 'type': 'ffi::c_int'}, {'name': 'thread_head', 'type': 'list_head'}, {'name': 'wait_chldexit', 'type': 'wait_queue_head_t'}, {'name': 'curr_target', 'type': '*mut task_struct'}, {'name': 'shared_pending', 'type': 'sigpending'}, {'name': 'multiprocess', 'type': 'hlist_head'}, {'name': 'group_exit_code', 'type': 'ffi::c_int'}, {'name': 'notify_count', 'type': 'ffi::c_int'}, {'name': 'group_exec_task', 'type': '*mut task_struct'}, {'name': 'group_stop_count', 'type': 'ffi::c_int'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'core_state', 'type': '*mut core_state'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'next_posix_timer_id', 'type': 'atomic_t'}, {'name': 'posix_timers', 'type': 'hlist_head'}, {'name': 'ignored_posix_timers', 'type': 'hlist_head'}, {'name': 'real_timer', 'type': 'hrtimer'}, {'name': 'it_real_incr', 'type': 'ktime_t'}, {'name': 'it', 'type': '[cpu_itimer; 2usize]'}, {'name': 'cputimer', 'type': 'thread_group_cputimer'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'pids', 'type': '[*mut pid; 4usize]'}, {'name': 'tty_old_pgrp', 'type': '*mut pid'}, {'name': 'leader', 'type': 'ffi::c_int'}, {'name': 'tty', 'type': '*mut tty_struct'}, {'name': 'stats_lock', 'type': 'seqlock_t'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'cutime', 'type': 'u64_'}, {'name': 'cstime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'cgtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'ffi::c_ulong'}, {'name': 'cnvcsw', 'type': 'ffi::c_ulong'}, {'name': 'cnivcsw', 'type': 'ffi::c_ulong'}, {'name': 'min_flt', 'type': 'ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'ffi::c_ulong'}, {'name': 'cmin_flt', 'type': 'ffi::c_ulong'}, {'name': 'cmaj_flt', 'type': 'ffi::c_ulong'}, {'name': 'inblock', 'type': 'ffi::c_ulong'}, {'name': 'oublock', 'type': 'ffi::c_ulong'}, {'name': 'cinblock', 'type': 'ffi::c_ulong'}, {'name': 'coublock', 'type': 'ffi::c_ulong'}, {'name': 'maxrss', 'type': 'ffi::c_ulong'}, {'name': 'cmaxrss', 'type': 'ffi::c_ulong'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'sum_sched_runtime', 'type': 'ffi::c_ulonglong'}, {'name': 'rlim', 'type': '[rlimit; 16usize]'}, {'name': 'pacct', 'type': 'pacct_struct'}, {'name': 'stats', 'type': '*mut taskstats'}, {'name': 'audit_tty', 'type': 'ffi::c_uint'}, {'name': 'tty_audit_buf', 'type': '*mut tty_audit_buf'}, {'name': 'oom_flag_origin', 'type': 'bool_'}, {'name': 'oom_score_adj', 'type': 'ffi::c_short'}, {'name': 'oom_score_adj_min', 'type': 'ffi::c_short'}, {'name': 'oom_mm', 'type': '*mut mm_struct'}, {'name': 'cred_guard_mutex', 'type': 'mutex'}, {'name': 'exec_update_lock', 'type': 'rw_semaphore'}]`

### Rust Evidence

- Graph edges: `1`

## W-000226 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: software_node_ref_args
- Explanation: software_node_ref_args changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'node', 'type': '*const software_node'}, {'name': 'nargs', 'type': 'ffi::c_uint'}, {'name': 'args', 'type': '[u64_; 8usize]'}]`
- New: `[{'name': 'node', 'type': '*const software_node'}, {'name': 'nargs', 'type': 'ffi::c_uint'}, {'name': 'args', 'type': '[u64_; 16usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000227 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: srcu_data
- Explanation: srcu_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'srcu_lock_count', 'type': '[atomic_long_t; 2usize]'}, {'name': 'srcu_unlock_count', 'type': '[atomic_long_t; 2usize]'}, {'name': 'srcu_reader_flavor', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': '[u32; 7usize]'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'srcu_cblist', 'type': 'rcu_segcblist'}, {'name': 'srcu_gp_seq_needed', 'type': 'ffi::c_ulong'}, {'name': 'srcu_gp_seq_needed_exp', 'type': 'ffi::c_ulong'}, {'name': 'srcu_cblist_invoking', 'type': 'bool_'}, {'name': 'delay_work', 'type': 'timer_list'}, {'name': 'work', 'type': 'work_struct'}, {'name': 'srcu_barrier_head', 'type': 'callback_head'}, {'name': 'mynode', 'type': '*mut srcu_node'}, {'name': 'grpmask', 'type': 'ffi::c_ulong'}, {'name': 'cpu', 'type': 'ffi::c_int'}, {'name': 'ssp', 'type': '*mut srcu_struct'}]`
- New: `[{'name': 'srcu_ctrs', 'type': '[srcu_ctr; 2usize]'}, {'name': 'srcu_reader_flavor', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': '[u32; 7usize]'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'srcu_cblist', 'type': 'rcu_segcblist'}, {'name': 'srcu_gp_seq_needed', 'type': 'ffi::c_ulong'}, {'name': 'srcu_gp_seq_needed_exp', 'type': 'ffi::c_ulong'}, {'name': 'srcu_cblist_invoking', 'type': 'bool_'}, {'name': 'delay_work', 'type': 'timer_list'}, {'name': 'work', 'type': 'work_struct'}, {'name': 'srcu_barrier_head', 'type': 'callback_head'}, {'name': 'mynode', 'type': '*mut srcu_node'}, {'name': 'grpmask', 'type': 'ffi::c_ulong'}, {'name': 'cpu', 'type': 'ffi::c_int'}, {'name': 'ssp', 'type': '*mut srcu_struct'}]`

### Rust Evidence

- Graph edges: `1`

## W-000228 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: srcu_struct
- Explanation: srcu_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'srcu_idx', 'type': 'ffi::c_uint'}, {'name': 'sda', 'type': '*mut srcu_data'}, {'name': 'dep_map', 'type': 'lockdep_map'}, {'name': 'srcu_sup', 'type': '*mut srcu_usage'}]`
- New: `[{'name': 'srcu_ctrp', 'type': '*mut srcu_ctr'}, {'name': 'sda', 'type': '*mut srcu_data'}, {'name': 'dep_map', 'type': 'lockdep_map'}, {'name': 'srcu_sup', 'type': '*mut srcu_usage'}]`

### Rust Evidence

- Graph edges: `1`

## W-000231 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: ucounts
- Explanation: ucounts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'node', 'type': 'hlist_node'}, {'name': 'ns', 'type': '*mut user_namespace'}, {'name': 'uid', 'type': 'kuid_t'}, {'name': 'count', 'type': 'atomic_t'}, {'name': 'ucount', 'type': '[atomic_long_t; 10usize]'}, {'name': 'rlimit', 'type': '[atomic_long_t; 4usize]'}]`
- New: `[{'name': 'node', 'type': 'hlist_nulls_node'}, {'name': 'ns', 'type': '*mut user_namespace'}, {'name': 'uid', 'type': 'kuid_t'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'count', 'type': 'rcuref_t'}, {'name': 'ucount', 'type': '[atomic_long_t; 10usize]'}, {'name': 'rlimit', 'type': '[atomic_long_t; 4usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000233 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vdso_image
- Explanation: vdso_image changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'data', 'type': '*mut ffi::c_void'}, {'name': 'size', 'type': 'ffi::c_ulong'}, {'name': 'alt', 'type': 'ffi::c_ulong'}, {'name': 'alt_len', 'type': 'ffi::c_ulong'}, {'name': 'extable_base', 'type': 'ffi::c_ulong'}, {'name': 'extable_len', 'type': 'ffi::c_ulong'}, {'name': 'extable', 'type': '*const ffi::c_void'}, {'name': 'sym_vvar_start', 'type': 'ffi::c_long'}, {'name': 'sym_vvar_page', 'type': 'ffi::c_long'}, {'name': 'sym_pvclock_page', 'type': 'ffi::c_long'}, {'name': 'sym_hvclock_page', 'type': 'ffi::c_long'}, {'name': 'sym_timens_page', 'type': 'ffi::c_long'}, {'name': 'sym_VDSO32_NOTE_MASK', 'type': 'ffi::c_long'}, {'name': 'sym___kernel_sigreturn', 'type': 'ffi::c_long'}, {'name': 'sym___kernel_rt_sigreturn', 'type': 'ffi::c_long'}, {'name': 'sym___kernel_vsyscall', 'type': 'ffi::c_long'}, {'name': 'sym_int80_landing_pad', 'type': 'ffi::c_long'}, {'name': 'sym_vdso32_sigreturn_landing_pad', 'type': 'ffi::c_long'}, {'name': 'sym_vdso32_rt_sigreturn_landing_pad', 'type': 'ffi::c_long'}]`
- New: `[{'name': 'data', 'type': '*mut ffi::c_void'}, {'name': 'size', 'type': 'ffi::c_ulong'}, {'name': 'alt', 'type': 'ffi::c_ulong'}, {'name': 'alt_len', 'type': 'ffi::c_ulong'}, {'name': 'extable_base', 'type': 'ffi::c_ulong'}, {'name': 'extable_len', 'type': 'ffi::c_ulong'}, {'name': 'extable', 'type': '*const ffi::c_void'}, {'name': 'sym_VDSO32_NOTE_MASK', 'type': 'ffi::c_long'}, {'name': 'sym___kernel_sigreturn', 'type': 'ffi::c_long'}, {'name': 'sym___kernel_rt_sigreturn', 'type': 'ffi::c_long'}, {'name': 'sym___kernel_vsyscall', 'type': 'ffi::c_long'}, {'name': 'sym_int80_landing_pad', 'type': 'ffi::c_long'}, {'name': 'sym_vdso32_sigreturn_landing_pad', 'type': 'ffi::c_long'}, {'name': 'sym_vdso32_rt_sigreturn_landing_pad', 'type': 'ffi::c_long'}]`

### Rust Evidence

- Graph edges: `1`

## W-000235 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vm_event_state
- Explanation: vm_event_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'event', 'type': '[ffi::c_ulong; 82usize]'}]`
- New: `[{'name': 'event', 'type': '[ffi::c_ulong; 86usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000236 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: x86_cpu_id
- Explanation: x86_cpu_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'vendor', 'type': '__u16'}, {'name': 'family', 'type': '__u16'}, {'name': 'model', 'type': '__u16'}, {'name': 'steppings', 'type': '__u16'}, {'name': 'feature', 'type': '__u16'}, {'name': 'flags', 'type': '__u16'}, {'name': 'driver_data', 'type': 'kernel_ulong_t'}]`
- New: `[{'name': 'vendor', 'type': '__u16'}, {'name': 'family', 'type': '__u16'}, {'name': 'model', 'type': '__u16'}, {'name': 'steppings', 'type': '__u16'}, {'name': 'feature', 'type': '__u16'}, {'name': 'flags', 'type': '__u16'}, {'name': 'type_', 'type': '__u8'}, {'name': 'driver_data', 'type': 'kernel_ulong_t'}]`

### Rust Evidence

- Graph edges: `1`

## W-000541 MacroConstDrift

- Risk: Medium
- Score: 8.6
- Symbol: init_wait
- Explanation: init_wait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `\`
- New: `init_wait_func(wait, autoremove_wake_function)`

### Rust Evidence

- Graph edges: `5`

## W-000306 MacroConstDrift

- Risk: Medium
- Score: 8.4
- Symbol: cpuhp_state_CPUHP_AP_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `146`
- New: `145`

### Rust Evidence

- Graph edges: `4`

## W-000238 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: BUG_UD1
- Explanation: BUG_UD1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `65534`
- New: `65533`

### Rust Evidence

- Graph edges: `2`

## W-000241 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: LOCK_PREFIX
- Explanation: LOCK_PREFIX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `b".pushsection .smp_locks,\"a\"\n.balign 4\n.long 671f - .\n.popsection\n671:\n\tlock`
- New: `b".pushsection .smp_locks,\"a\"\n.balign 4\n.long 671f - .\n.popsection\n671:\n\tlock \0"`

### Rust Evidence

- Graph edges: `2`

## W-000307 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: cpuhp_state_CPUHP_AP_ONLINE_DYN
- Explanation: cpuhp_state_CPUHP_AP_ONLINE_DYN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `195`
- New: `194`

### Rust Evidence

- Graph edges: `2`

## W-000370 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: cpuhp_state_CPUHP_BP_PREPARE_DYN
- Explanation: cpuhp_state_CPUHP_BP_PREPARE_DYN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `65`
- New: `64`

### Rust Evidence

- Graph edges: `2`

## W-000482 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: vm_event_item_HTLB_BUDDY_PGALLOC
- Explanation: vm_event_item_HTLB_BUDDY_PGALLOC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `62`
- New: `64`

### Rust Evidence

- Graph edges: `2`

## W-000503 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: vm_event_item_PGSCAN_DIRECT
- Explanation: vm_event_item_PGSCAN_DIRECT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `29`
- New: `30`

### Rust Evidence

- Graph edges: `2`

## W-000513 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: vm_event_item_SWAP_RA
- Explanation: vm_event_item_SWAP_RA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `71`
- New: `73`

### Rust Evidence

- Graph edges: `2`

## W-000239 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: BUG_UD2
- Explanation: BUG_UD2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `65533`
- New: `65534`

### Rust Evidence

- Graph edges: `1`

## W-000240 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: IA32_NR_syscalls
- Explanation: IA32_NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `467`
- New: `468`

### Rust Evidence

- Graph edges: `1`

## W-000242 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: MAX_DA_NAME_LEN
- Explanation: MAX_DA_NAME_LEN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `24`
- New: `32`

### Rust Evidence

- Graph edges: `1`

## W-000243 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: NETIF_F_FCOE_CRC_BIT
- Explanation: NETIF_F_FCOE_CRC_BIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `35`
- New: `36`

### Rust Evidence

- Graph edges: `1`

## W-000244 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: NETIF_F_GSO_LAST
- Explanation: NETIF_F_GSO_LAST changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `34`
- New: `35`

### Rust Evidence

- Graph edges: `1`

## W-000245 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: NETIF_F_SCTP_CRC_BIT
- Explanation: NETIF_F_SCTP_CRC_BIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `36`
- New: `37`

### Rust Evidence

- Graph edges: `1`

## W-000246 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: NR_FWNODE_REFERENCE_ARGS
- Explanation: NR_FWNODE_REFERENCE_ARGS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `16`

### Rust Evidence

- Graph edges: `1`

## W-000247 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: NR_syscalls
- Explanation: NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `467`
- New: `468`

### Rust Evidence

- Graph edges: `1`

## W-000248 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: PCI_REBAR_CAP_SIZES
- Explanation: PCI_REBAR_CAP_SIZES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16777200`
- New: `4294967280`

### Rust Evidence

- Graph edges: `1`

## W-000249 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: SECTION_MAP_LAST_BIT
- Explanation: SECTION_MAP_LAST_BIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `4`
- New: `5`

### Rust Evidence

- Graph edges: `1`

## W-000250 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: SOF_TIMESTAMPING_LAST
- Explanation: SOF_TIMESTAMPING_LAST changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `131072`
- New: `262144`

### Rust Evidence

- Graph edges: `1`

## W-000251 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: SOF_TIMESTAMPING_MASK
- Explanation: SOF_TIMESTAMPING_MASK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `262143`
- New: `524287`

### Rust Evidence

- Graph edges: `1`

## W-000252 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: SRCU_READ_FLAVOR_ALL
- Explanation: SRCU_READ_FLAVOR_ALL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `7`
- New: `15`

### Rust Evidence

- Graph edges: `1`

## W-000253 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TAINT_FLAGS_COUNT
- Explanation: TAINT_FLAGS_COUNT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `19`
- New: `20`

### Rust Evidence

- Graph edges: `1`

## W-000254 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TAINT_FLAGS_MAX
- Explanation: TAINT_FLAGS_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `524287`
- New: `1048575`

### Rust Evidence

- Graph edges: `1`

## W-000255 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TASKSTATS_VERSION
- Explanation: TASKSTATS_VERSION changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `15`
- New: `16`

### Rust Evidence

- Graph edges: `1`

## W-000256 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __NR_ia32_syscalls
- Explanation: __NR_ia32_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `467`
- New: `468`

### Rust Evidence

- Graph edges: `1`

## W-000257 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __NR_syscalls
- Explanation: __NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `467`
- New: `468`

### Rust Evidence

- Graph edges: `1`

## W-000258 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ACTIVE
- Explanation: cpuhp_state_CPUHP_AP_ACTIVE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `238`
- New: `237`

### Rust Evidence

- Graph edges: `1`

## W-000259 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARC_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARC_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `128`
- New: `127`

### Rust Evidence

- Graph edges: `1`

## W-000260 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM64_DEBUG_MONITORS_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM64_DEBUG_MONITORS_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `112`
- New: `111`

### Rust Evidence

- Graph edges: `1`

## W-000261 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM64_ISNDEP_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM64_ISNDEP_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `140`
- New: `139`

### Rust Evidence

- Graph edges: `1`

## W-000262 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARMADA_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARMADA_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `126`
- New: `125`

### Rust Evidence

- Graph edges: `1`

## W-000263 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_EVTSTRM_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_EVTSTRM_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `120`
- New: `119`

### Rust Evidence

- Graph edges: `1`

## W-000264 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `119`
- New: `118`

### Rust Evidence

- Graph edges: `1`

## W-000265 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_CACHE_B15_RAC_DYING
- Explanation: cpuhp_state_CPUHP_AP_ARM_CACHE_B15_RAC_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `145`
- New: `144`

### Rust Evidence

- Graph edges: `1`

## W-000266 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_CORESIGHT_CTI_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_CORESIGHT_CTI_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `139`
- New: `138`

### Rust Evidence

- Graph edges: `1`

## W-000267 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_CORESIGHT_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_CORESIGHT_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `138`
- New: `137`

### Rust Evidence

- Graph edges: `1`

## W-000268 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_GLOBAL_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_GLOBAL_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `121`
- New: `120`

### Rust Evidence

- Graph edges: `1`

## W-000269 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_L2X0_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_L2X0_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `117`
- New: `116`

### Rust Evidence

- Graph edges: `1`

## W-000270 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_MVEBU_COHERENCY
- Explanation: cpuhp_state_CPUHP_AP_ARM_MVEBU_COHERENCY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `106`
- New: `105`

### Rust Evidence

- Graph edges: `1`

## W-000271 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_MVEBU_SYNC_CLOCKS
- Explanation: cpuhp_state_CPUHP_AP_ARM_MVEBU_SYNC_CLOCKS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `155`
- New: `154`

### Rust Evidence

- Graph edges: `1`

## W-000272 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_TWD_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_TWD_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `123`
- New: `122`

### Rust Evidence

- Graph edges: `1`

## W-000273 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_VFP_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_VFP_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `111`
- New: `110`

### Rust Evidence

- Graph edges: `1`

## W-000274 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_XEN_RUNSTATE_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_XEN_RUNSTATE_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `137`
- New: `136`

### Rust Evidence

- Graph edges: `1`

## W-000275 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_XEN_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_XEN_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `136`
- New: `135`

### Rust Evidence

- Graph edges: `1`

## W-000276 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_BASE_CACHEINFO_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_BASE_CACHEINFO_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `194`
- New: `193`

### Rust Evidence

- Graph edges: `1`

## W-000277 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_BLK_MQ_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_BLK_MQ_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `154`
- New: `153`

### Rust Evidence

- Graph edges: `1`

## W-000278 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_CACHECTRL_STARTING
- Explanation: cpuhp_state_CPUHP_AP_CACHECTRL_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `90`
- New: `89`

### Rust Evidence

- Graph edges: `1`

## W-000279 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_CLINT_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_CLINT_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `131`
- New: `130`

### Rust Evidence

- Graph edges: `1`

## W-000280 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_CPU_PM_STARTING
- Explanation: cpuhp_state_CPUHP_AP_CPU_PM_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `93`
- New: `92`

### Rust Evidence

- Graph edges: `1`

## W-000281 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_CSKY_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_CSKY_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `132`
- New: `131`

### Rust Evidence

- Graph edges: `1`

## W-000282 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_DUMMY_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_DUMMY_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `135`
- New: `134`

### Rust Evidence

- Graph edges: `1`

## W-000283 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_EXYNOS4_MCT_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_EXYNOS4_MCT_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `118`
- New: `117`

### Rust Evidence

- Graph edges: `1`

## W-000284 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_HRTIMERS_DYING
- Explanation: cpuhp_state_CPUHP_AP_HRTIMERS_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `142`
- New: `141`

### Rust Evidence

- Graph edges: `1`

## W-000285 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_HYPERV_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_HYPERV_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `149`
- New: `148`

### Rust Evidence

- Graph edges: `1`

## W-000286 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_HYPERV_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_HYPERV_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `134`
- New: `133`

### Rust Evidence

- Graph edges: `1`

## W-000287 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IDLE_DEAD
- Explanation: cpuhp_state_CPUHP_AP_IDLE_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `88`
- New: `87`

### Rust Evidence

- Graph edges: `1`

## W-000288 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_AFFINITY_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_IRQ_AFFINITY_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `153`
- New: `152`

### Rust Evidence

- Graph edges: `1`

## W-000289 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_APPLE_AIC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_APPLE_AIC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `96`
- New: `95`

### Rust Evidence

- Graph edges: `1`

## W-000290 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_ARMADA_XP_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_ARMADA_XP_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `97`
- New: `96`

### Rust Evidence

- Graph edges: `1`

## W-000291 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_AVECINTC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_AVECINTC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `101`
- New: `100`

### Rust Evidence

- Graph edges: `1`

## W-000292 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_BCM2836_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_BCM2836_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `98`
- New: `97`

### Rust Evidence

- Graph edges: `1`

## W-000293 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_EIOINTC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_EIOINTC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `100`
- New: `99`

### Rust Evidence

- Graph edges: `1`

## W-000294 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_GIC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_GIC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `94`
- New: `93`

### Rust Evidence

- Graph edges: `1`

## W-000295 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_HIP04_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_HIP04_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `95`
- New: `94`

### Rust Evidence

- Graph edges: `1`

## W-000296 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_MIPS_GIC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_MIPS_GIC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `99`
- New: `98`

### Rust Evidence

- Graph edges: `1`

## W-000297 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_RISCV_IMSIC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_RISCV_IMSIC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `104`
- New: `103`

### Rust Evidence

- Graph edges: `1`

## W-000298 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_RISCV_SBI_IPI_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_RISCV_SBI_IPI_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `105`
- New: `104`

### Rust Evidence

- Graph edges: `1`

## W-000299 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_SIFIVE_PLIC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_SIFIVE_PLIC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `102`
- New: `101`

### Rust Evidence

- Graph edges: `1`

## W-000300 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_THEAD_ACLINT_SSWI_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_THEAD_ACLINT_SSWI_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `103`
- New: `102`

### Rust Evidence

- Graph edges: `1`

## W-000301 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_JCORE_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_JCORE_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `122`
- New: `121`

### Rust Evidence

- Graph edges: `1`

## W-000302 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_KTHREADS_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_KTHREADS_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `193`
- New: `192`

### Rust Evidence

- Graph edges: `1`

## W-000303 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_KVM_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_KVM_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `150`
- New: `149`

### Rust Evidence

- Graph edges: `1`

## W-000304 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_MIPS_GIC_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_MIPS_GIC_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `127`
- New: `126`

### Rust Evidence

- Graph edges: `1`

## W-000305 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_OFFLINE
- Explanation: cpuhp_state_CPUHP_AP_OFFLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `89`
- New: `88`

### Rust Evidence

- Graph edges: `1`

## W-000308 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ONLINE_DYN_END
- Explanation: cpuhp_state_CPUHP_AP_ONLINE_DYN_END changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `235`
- New: `234`

### Rust Evidence

- Graph edges: `1`

## W-000309 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ONLINE_IDLE
- Explanation: cpuhp_state_CPUHP_AP_ONLINE_IDLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `148`
- New: `147`

### Rust Evidence

- Graph edges: `1`

## W-000310 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_ACPI_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_ACPI_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `114`
- New: `113`

### Rust Evidence

- Graph edges: `1`

## W-000311 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_APM_XGENE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_APM_XGENE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `177`
- New: `176`

### Rust Evidence

- Graph edges: `1`

## W-000312 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_CAVIUM_TX2_UNCORE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_CAVIUM_TX2_UNCORE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `178`
- New: `177`

### Rust Evidence

- Graph edges: `1`

## W-000313 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_CCI_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_CCI_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `164`
- New: `163`

### Rust Evidence

- Graph edges: `1`

## W-000314 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_CCN_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_CCN_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `165`
- New: `164`

### Rust Evidence

- Graph edges: `1`

## W-000315 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_CPA_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_CPA_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `166`
- New: `165`

### Rust Evidence

- Graph edges: `1`

## W-000316 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_DDRC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_DDRC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `167`
- New: `166`

### Rust Evidence

- Graph edges: `1`

## W-000317 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_HHA_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_HHA_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `168`
- New: `167`

### Rust Evidence

- Graph edges: `1`

## W-000318 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_L3_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_L3_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `169`
- New: `168`

### Rust Evidence

- Graph edges: `1`

## W-000319 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PA_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PA_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `170`
- New: `169`

### Rust Evidence

- Graph edges: `1`

## W-000320 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PCIE_PMU_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PCIE_PMU_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `172`
- New: `171`

### Rust Evidence

- Graph edges: `1`

## W-000321 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_SLLC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_SLLC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `171`
- New: `170`

### Rust Evidence

- Graph edges: `1`

## W-000322 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HNS3_PMU_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HNS3_PMU_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `173`
- New: `172`

### Rust Evidence

- Graph edges: `1`

## W-000323 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HW_BREAKPOINT_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HW_BREAKPOINT_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `113`
- New: `112`

### Rust Evidence

- Graph edges: `1`

## W-000324 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_L2X0_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_L2X0_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `174`
- New: `173`

### Rust Evidence

- Graph edges: `1`

## W-000325 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_MARVELL_CN10K_DDR_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_MARVELL_CN10K_DDR_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `179`
- New: `178`

### Rust Evidence

- Graph edges: `1`

## W-000326 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_MRVL_PEM_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_MRVL_PEM_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `180`
- New: `179`

### Rust Evidence

- Graph edges: `1`

## W-000327 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L2_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L2_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `175`
- New: `174`

### Rust Evidence

- Graph edges: `1`

## W-000328 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L3_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L3_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `176`
- New: `175`

### Rust Evidence

- Graph edges: `1`

## W-000329 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `115`
- New: `114`

### Rust Evidence

- Graph edges: `1`

## W-000330 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_CSKY_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_CSKY_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `187`
- New: `186`

### Rust Evidence

- Graph edges: `1`

## W-000331 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `157`
- New: `156`

### Rust Evidence

- Graph edges: `1`

## W-000332 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_CORE_IMC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_CORE_IMC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `182`
- New: `181`

### Rust Evidence

- Graph edges: `1`

## W-000333 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_HV_24x7_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_HV_24x7_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `185`
- New: `184`

### Rust Evidence

- Graph edges: `1`

## W-000334 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_HV_GPCI_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_HV_GPCI_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `186`
- New: `185`

### Rust Evidence

- Graph edges: `1`

## W-000335 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_NEST_IMC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_NEST_IMC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `181`
- New: `180`

### Rust Evidence

- Graph edges: `1`

## W-000336 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_THREAD_IMC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_THREAD_IMC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `183`
- New: `182`

### Rust Evidence

- Graph edges: `1`

## W-000337 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_TRACE_IMC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_TRACE_IMC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `184`
- New: `183`

### Rust Evidence

- Graph edges: `1`

## W-000338 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_RISCV_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_RISCV_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `116`
- New: `115`

### Rust Evidence

- Graph edges: `1`

## W-000339 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_S390_CF_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_S390_CF_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `162`
- New: `161`

### Rust Evidence

- Graph edges: `1`

## W-000340 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_S390_SF_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_S390_SF_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `163`
- New: `162`

### Rust Evidence

- Graph edges: `1`

## W-000341 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_IBS_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_IBS_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `109`
- New: `108`

### Rust Evidence

- Graph edges: `1`

## W-000342 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_POWER_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_POWER_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `161`
- New: `160`

### Rust Evidence

- Graph edges: `1`

## W-000343 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `160`
- New: `159`

### Rust Evidence

- Graph edges: `1`

## W-000344 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `107`
- New: `106`

### Rust Evidence

- Graph edges: `1`

## W-000345 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `158`
- New: `157`

### Rust Evidence

- Graph edges: `1`

## W-000346 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `108`
- New: `107`

### Rust Evidence

- Graph edges: `1`

## W-000347 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_UNCORE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_UNCORE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `159`
- New: `158`

### Rust Evidence

- Graph edges: `1`

## W-000348 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_XTENSA_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_XTENSA_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `110`
- New: `109`

### Rust Evidence

- Graph edges: `1`

## W-000349 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_QCOM_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_QCOM_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `124`
- New: `123`

### Rust Evidence

- Graph edges: `1`

## W-000350 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_RANDOM_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_RANDOM_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `191`
- New: `190`

### Rust Evidence

- Graph edges: `1`

## W-000351 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_RCUTREE_DYING
- Explanation: cpuhp_state_CPUHP_AP_RCUTREE_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `92`
- New: `91`

### Rust Evidence

- Graph edges: `1`

## W-000352 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_RCUTREE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_RCUTREE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `192`
- New: `191`

### Rust Evidence

- Graph edges: `1`

## W-000353 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_REALTEK_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_REALTEK_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `129`
- New: `128`

### Rust Evidence

- Graph edges: `1`

## W-000354 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_RISCV_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_RISCV_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `130`
- New: `129`

### Rust Evidence

- Graph edges: `1`

## W-000355 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_SCHED_STARTING
- Explanation: cpuhp_state_CPUHP_AP_SCHED_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `91`
- New: `90`

### Rust Evidence

- Graph edges: `1`

## W-000356 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_SCHED_WAIT_EMPTY
- Explanation: cpuhp_state_CPUHP_AP_SCHED_WAIT_EMPTY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `151`
- New: `150`

### Rust Evidence

- Graph edges: `1`

## W-000357 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_SMPBOOT_THREADS
- Explanation: cpuhp_state_CPUHP_AP_SMPBOOT_THREADS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `152`
- New: `151`

### Rust Evidence

- Graph edges: `1`

## W-000358 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_SMPCFD_DYING
- Explanation: cpuhp_state_CPUHP_AP_SMPCFD_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `141`
- New: `140`

### Rust Evidence

- Graph edges: `1`

## W-000359 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_TEGRA_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_TEGRA_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `125`
- New: `124`

### Rust Evidence

- Graph edges: `1`

## W-000360 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_TICK_DYING
- Explanation: cpuhp_state_CPUHP_AP_TICK_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `143`
- New: `142`

### Rust Evidence

- Graph edges: `1`

## W-000361 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_TI_GP_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_TI_GP_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `133`
- New: `132`

### Rust Evidence

- Graph edges: `1`

## W-000362 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_TMIGR_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_TMIGR_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `188`
- New: `187`

### Rust Evidence

- Graph edges: `1`

## W-000363 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_WATCHDOG_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_WATCHDOG_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `189`
- New: `188`

### Rust Evidence

- Graph edges: `1`

## W-000364 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_WORKQUEUE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_WORKQUEUE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `190`
- New: `189`

### Rust Evidence

- Graph edges: `1`

## W-000365 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_X86_HPET_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_X86_HPET_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `236`
- New: `235`

### Rust Evidence

- Graph edges: `1`

## W-000366 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_X86_INTEL_EPB_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_X86_INTEL_EPB_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `156`
- New: `155`

### Rust Evidence

- Graph edges: `1`

## W-000367 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_X86_KVM_CLK_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_X86_KVM_CLK_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `237`
- New: `236`

### Rust Evidence

- Graph edges: `1`

## W-000368 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_X86_TBOOT_DYING
- Explanation: cpuhp_state_CPUHP_AP_X86_TBOOT_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `144`
- New: `143`

### Rust Evidence

- Graph edges: `1`

## W-000369 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_BP_KICK_AP
- Explanation: cpuhp_state_CPUHP_BP_KICK_AP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `86`
- New: `85`

### Rust Evidence

- Graph edges: `1`

## W-000371 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_BP_PREPARE_DYN_END
- Explanation: cpuhp_state_CPUHP_BP_PREPARE_DYN_END changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `85`
- New: `84`

### Rust Evidence

- Graph edges: `1`

## W-000372 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_BRINGUP_CPU
- Explanation: cpuhp_state_CPUHP_BRINGUP_CPU changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `87`
- New: `86`

### Rust Evidence

- Graph edges: `1`

## W-000373 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_KVM_PPC_BOOK3S_PREPARE
- Explanation: cpuhp_state_CPUHP_KVM_PPC_BOOK3S_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `60`
- New: `59`

### Rust Evidence

- Graph edges: `1`

## W-000374 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_MIPS_SOC_PREPARE
- Explanation: cpuhp_state_CPUHP_MIPS_SOC_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `64`
- New: `63`

### Rust Evidence

- Graph edges: `1`

## W-000375 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_MM_ZSWP_POOL_PREPARE
- Explanation: cpuhp_state_CPUHP_MM_ZSWP_POOL_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `59`
- New: `58`

### Rust Evidence

- Graph edges: `1`

## W-000376 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_ONLINE
- Explanation: cpuhp_state_CPUHP_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `239`
- New: `238`

### Rust Evidence

- Graph edges: `1`

## W-000377 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_TEARDOWN_CPU
- Explanation: cpuhp_state_CPUHP_TEARDOWN_CPU changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `147`
- New: `146`

### Rust Evidence

- Graph edges: `1`

## W-000378 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_TIMERS_PREPARE
- Explanation: cpuhp_state_CPUHP_TIMERS_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `62`
- New: `61`

### Rust Evidence

- Graph edges: `1`

## W-000379 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_TMIGR_PREPARE
- Explanation: cpuhp_state_CPUHP_TMIGR_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `63`
- New: `62`

### Rust Evidence

- Graph edges: `1`

## W-000380 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_ZCOMP_PREPARE
- Explanation: cpuhp_state_CPUHP_ZCOMP_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `61`
- New: `60`

### Rust Evidence

- Graph edges: `1`

## W-000381 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ethtool_link_mode_bit_indices___ETHTOOL_LINK_MODE_MASK_NBITS
- Explanation: ethtool_link_mode_bit_indices___ETHTOOL_LINK_MODE_MASK_NBITS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `103`
- New: `121`

### Rust Evidence

- Graph edges: `1`

## W-000382 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: mds_mitigations_MDS_MITIGATION_FULL
- Explanation: mds_mitigations_MDS_MITIGATION_FULL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `1`
- New: `2`

### Rust Evidence

- Graph edges: `1`

## W-000383 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: mds_mitigations_MDS_MITIGATION_VMWERV
- Explanation: mds_mitigations_MDS_MITIGATION_VMWERV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `2`
- New: `3`

### Rust Evidence

- Graph edges: `1`

## W-000384 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_KMEM
- Explanation: memcg_stat_item_MEMCG_KMEM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `50`
- New: `52`

### Rust Evidence

- Graph edges: `1`

## W-000385 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_NR_STAT
- Explanation: memcg_stat_item_MEMCG_NR_STAT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `53`
- New: `55`

### Rust Evidence

- Graph edges: `1`

## W-000386 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_PERCPU_B
- Explanation: memcg_stat_item_MEMCG_PERCPU_B changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `50`

### Rust Evidence

- Graph edges: `1`

## W-000387 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_SOCK
- Explanation: memcg_stat_item_MEMCG_SOCK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `47`
- New: `49`

### Rust Evidence

- Graph edges: `1`

## W-000388 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_SWAP
- Explanation: memcg_stat_item_MEMCG_SWAP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `46`
- New: `48`

### Rust Evidence

- Graph edges: `1`

## W-000389 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_VMALLOC
- Explanation: memcg_stat_item_MEMCG_VMALLOC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `49`
- New: `51`

### Rust Evidence

- Graph edges: `1`

## W-000390 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_ZSWAPPED
- Explanation: memcg_stat_item_MEMCG_ZSWAPPED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `52`
- New: `54`

### Rust Evidence

- Graph edges: `1`

## W-000391 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_ZSWAP_B
- Explanation: memcg_stat_item_MEMCG_ZSWAP_B changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `51`
- New: `53`

### Rust Evidence

- Graph edges: `1`

## W-000392 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_HUGETLB
- Explanation: node_stat_item_NR_HUGETLB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `45`
- New: `46`

### Rust Evidence

- Graph edges: `1`

## W-000393 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_VM_NODE_STAT_ITEMS
- Explanation: node_stat_item_NR_VM_NODE_STAT_ITEMS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `46`
- New: `48`

### Rust Evidence

- Graph edges: `1`

## W-000394 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_ARP_PVLAN_DISABLE
- Explanation: skb_drop_reason_SKB_DROP_REASON_ARP_PVLAN_DISABLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `112`
- New: `114`

### Rust Evidence

- Graph edges: `1`

## W-000395 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_BPF_CGROUP_EGRESS
- Explanation: skb_drop_reason_SKB_DROP_REASON_BPF_CGROUP_EGRESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `51`
- New: `53`

### Rust Evidence

- Graph edges: `1`

## W-000396 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_BRIDGE_INGRESS_STP_STATE
- Explanation: skb_drop_reason_SKB_DROP_REASON_BRIDGE_INGRESS_STP_STATE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `114`
- New: `116`

### Rust Evidence

- Graph edges: `1`

## W-000397 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_CAKE_FLOOD
- Explanation: skb_drop_reason_SKB_DROP_REASON_CAKE_FLOOD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `62`
- New: `64`

### Rust Evidence

- Graph edges: `1`

## W-000398 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_CPU_BACKLOG
- Explanation: skb_drop_reason_SKB_DROP_REASON_CPU_BACKLOG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `66`
- New: `68`

### Rust Evidence

- Graph edges: `1`

## W-000399 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_DEV_HDR
- Explanation: skb_drop_reason_SKB_DROP_REASON_DEV_HDR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `73`
- New: `75`

### Rust Evidence

- Graph edges: `1`

## W-000400 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_DEV_READY
- Explanation: skb_drop_reason_SKB_DROP_REASON_DEV_READY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `74`
- New: `76`

### Rust Evidence

- Graph edges: `1`

## W-000401 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_DUP_FRAG
- Explanation: skb_drop_reason_SKB_DROP_REASON_DUP_FRAG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `89`
- New: `91`

### Rust Evidence

- Graph edges: `1`

## W-000402 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FQ_BAND_LIMIT
- Explanation: skb_drop_reason_SKB_DROP_REASON_FQ_BAND_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `63`
- New: `65`

### Rust Evidence

- Graph edges: `1`

## W-000403 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FQ_FLOW_LIMIT
- Explanation: skb_drop_reason_SKB_DROP_REASON_FQ_FLOW_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `65`
- New: `67`

### Rust Evidence

- Graph edges: `1`

## W-000404 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FQ_HORIZON_LIMIT
- Explanation: skb_drop_reason_SKB_DROP_REASON_FQ_HORIZON_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `64`
- New: `66`

### Rust Evidence

- Graph edges: `1`

## W-000405 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FRAG_REASM_TIMEOUT
- Explanation: skb_drop_reason_SKB_DROP_REASON_FRAG_REASM_TIMEOUT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `90`
- New: `92`

### Rust Evidence

- Graph edges: `1`

## W-000406 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FRAG_TOO_FAR
- Explanation: skb_drop_reason_SKB_DROP_REASON_FRAG_TOO_FAR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `91`
- New: `93`

### Rust Evidence

- Graph edges: `1`

## W-000407 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FULL_RING
- Explanation: skb_drop_reason_SKB_DROP_REASON_FULL_RING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `75`
- New: `77`

### Rust Evidence

- Graph edges: `1`

## W-000408 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_HDR_TRUNC
- Explanation: skb_drop_reason_SKB_DROP_REASON_HDR_TRUNC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `77`
- New: `79`

### Rust Evidence

- Graph edges: `1`

## W-000409 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_ICMP_CSUM
- Explanation: skb_drop_reason_SKB_DROP_REASON_ICMP_CSUM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `80`
- New: `82`

### Rust Evidence

- Graph edges: `1`

## W-000410 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_INVALID_PROTO
- Explanation: skb_drop_reason_SKB_DROP_REASON_INVALID_PROTO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `81`
- New: `83`

### Rust Evidence

- Graph edges: `1`

## W-000411 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6DISABLED
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6DISABLED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `52`
- New: `54`

### Rust Evidence

- Graph edges: `1`

## W-000412 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_BAD_EXTHDR
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_BAD_EXTHDR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `93`
- New: `95`

### Rust Evidence

- Graph edges: `1`

## W-000413 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_CODE
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_CODE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `96`
- New: `98`

### Rust Evidence

- Graph edges: `1`

## W-000414 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_OPTIONS
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_OPTIONS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `97`
- New: `99`

### Rust Evidence

- Graph edges: `1`

## W-000415 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_FRAG
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_FRAG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `94`
- New: `96`

### Rust Evidence

- Graph edges: `1`

## W-000416 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_HOP_LIMIT
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_HOP_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `95`
- New: `97`

### Rust Evidence

- Graph edges: `1`

## W-000417 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_NS_OTHERHOST
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_NS_OTHERHOST changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `98`
- New: `100`

### Rust Evidence

- Graph edges: `1`

## W-000418 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INADDRERRORS
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INADDRERRORS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `82`
- New: `84`

### Rust Evidence

- Graph edges: `1`

## W-000419 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INNOROUTES
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INNOROUTES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `83`
- New: `85`

### Rust Evidence

- Graph edges: `1`

## W-000420 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_DEST
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_DEST changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `87`
- New: `89`

### Rust Evidence

- Graph edges: `1`

## W-000421 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_SOURCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_SOURCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `85`
- New: `87`

### Rust Evidence

- Graph edges: `1`

## W-000422 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_LOCALNET
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_LOCALNET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `86`
- New: `88`

### Rust Evidence

- Graph edges: `1`

## W-000423 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_LOCAL_SOURCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_LOCAL_SOURCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `84`
- New: `86`

### Rust Evidence

- Graph edges: `1`

## W-000424 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_OUTNOROUTES
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_OUTNOROUTES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `50`
- New: `52`

### Rust Evidence

- Graph edges: `1`

## W-000425 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_TUNNEL_ECN
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_TUNNEL_ECN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `109`
- New: `111`

### Rust Evidence

- Graph edges: `1`

## W-000426 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_LOCAL_MAC
- Explanation: skb_drop_reason_SKB_DROP_REASON_LOCAL_MAC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `111`
- New: `113`

### Rust Evidence

- Graph edges: `1`

## W-000427 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_MAC_IEEE_MAC_CONTROL
- Explanation: skb_drop_reason_SKB_DROP_REASON_MAC_IEEE_MAC_CONTROL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `113`
- New: `115`

### Rust Evidence

- Graph edges: `1`

## W-000428 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_MAC_INVALID_SOURCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_MAC_INVALID_SOURCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `106`
- New: `108`

### Rust Evidence

- Graph edges: `1`

## W-000429 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_MAX
- Explanation: skb_drop_reason_SKB_DROP_REASON_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `115`
- New: `117`

### Rust Evidence

- Graph edges: `1`

## W-000430 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NEIGH_CREATEFAIL
- Explanation: skb_drop_reason_SKB_DROP_REASON_NEIGH_CREATEFAIL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `53`
- New: `55`

### Rust Evidence

- Graph edges: `1`

## W-000431 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NEIGH_DEAD
- Explanation: skb_drop_reason_SKB_DROP_REASON_NEIGH_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `56`
- New: `58`

### Rust Evidence

- Graph edges: `1`

## W-000432 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NEIGH_FAILED
- Explanation: skb_drop_reason_SKB_DROP_REASON_NEIGH_FAILED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `54`
- New: `56`

### Rust Evidence

- Graph edges: `1`

## W-000433 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NEIGH_QUEUEFULL
- Explanation: skb_drop_reason_SKB_DROP_REASON_NEIGH_QUEUEFULL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `55`
- New: `57`

### Rust Evidence

- Graph edges: `1`

## W-000434 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NOMEM
- Explanation: skb_drop_reason_SKB_DROP_REASON_NOMEM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `76`
- New: `78`

### Rust Evidence

- Graph edges: `1`

## W-000435 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NO_TX_TARGET
- Explanation: skb_drop_reason_SKB_DROP_REASON_NO_TX_TARGET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `108`
- New: `110`

### Rust Evidence

- Graph edges: `1`

## W-000436 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_PACKET_SOCK_ERROR
- Explanation: skb_drop_reason_SKB_DROP_REASON_PACKET_SOCK_ERROR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `101`
- New: `103`

### Rust Evidence

- Graph edges: `1`

## W-000437 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_PKT_TOO_BIG
- Explanation: skb_drop_reason_SKB_DROP_REASON_PKT_TOO_BIG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `88`
- New: `90`

### Rust Evidence

- Graph edges: `1`

## W-000438 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_QDISC_CONGESTED
- Explanation: skb_drop_reason_SKB_DROP_REASON_QDISC_CONGESTED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `61`
- New: `63`

### Rust Evidence

- Graph edges: `1`

## W-000439 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_QDISC_DROP
- Explanation: skb_drop_reason_SKB_DROP_REASON_QDISC_DROP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `59`
- New: `61`

### Rust Evidence

- Graph edges: `1`

## W-000440 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_QDISC_OVERLIMIT
- Explanation: skb_drop_reason_SKB_DROP_REASON_QDISC_OVERLIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `60`
- New: `62`

### Rust Evidence

- Graph edges: `1`

## W-000441 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_QUEUE_PURGE
- Explanation: skb_drop_reason_SKB_DROP_REASON_QUEUE_PURGE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `99`
- New: `101`

### Rust Evidence

- Graph edges: `1`

## W-000442 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SECURITY_HOOK
- Explanation: skb_drop_reason_SKB_DROP_REASON_SECURITY_HOOK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `58`
- New: `60`

### Rust Evidence

- Graph edges: `1`

## W-000443 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SKB_CSUM
- Explanation: skb_drop_reason_SKB_DROP_REASON_SKB_CSUM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `70`
- New: `72`

### Rust Evidence

- Graph edges: `1`

## W-000444 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SKB_GSO_SEG
- Explanation: skb_drop_reason_SKB_DROP_REASON_SKB_GSO_SEG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `71`
- New: `73`

### Rust Evidence

- Graph edges: `1`

## W-000445 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SKB_UCOPY_FAULT
- Explanation: skb_drop_reason_SKB_DROP_REASON_SKB_UCOPY_FAULT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `72`
- New: `74`

### Rust Evidence

- Graph edges: `1`

## W-000446 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TAP_FILTER
- Explanation: skb_drop_reason_SKB_DROP_REASON_TAP_FILTER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `78`
- New: `80`

### Rust Evidence

- Graph edges: `1`

## W-000447 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TAP_TXFILTER
- Explanation: skb_drop_reason_SKB_DROP_REASON_TAP_TXFILTER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `79`
- New: `81`

### Rust Evidence

- Graph edges: `1`

## W-000448 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_ACK_UNSENT_DATA
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_ACK_UNSENT_DATA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `47`
- New: `49`

### Rust Evidence

- Graph edges: `1`

## W-000449 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_CLOSE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_CLOSE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `43`
- New: `45`

### Rust Evidence

- Graph edges: `1`

## W-000450 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_FASTOPEN
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_FASTOPEN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `44`
- New: `46`

### Rust Evidence

- Graph edges: `1`

## W-000451 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_ACK_SEQUENCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_ACK_SEQUENCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `40`
- New: `42`

### Rust Evidence

- Graph edges: `1`

## W-000452 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_SEQUENCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_SEQUENCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `39`
- New: `41`

### Rust Evidence

- Graph edges: `1`

## W-000453 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_SYN
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_SYN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `42`
- New: `44`

### Rust Evidence

- Graph edges: `1`

## W-000454 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_MINTTL
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_MINTTL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `92`
- New: `94`

### Rust Evidence

- Graph edges: `1`

## W-000455 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OFO_DROP
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OFO_DROP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `49`
- New: `51`

### Rust Evidence

- Graph edges: `1`

## W-000456 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OFO_QUEUE_PRUNE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OFO_QUEUE_PRUNE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `50`

### Rust Evidence

- Graph edges: `1`

## W-000457 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OLD_ACK
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OLD_ACK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `45`
- New: `47`

### Rust Evidence

- Graph edges: `1`

## W-000458 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OLD_SEQUENCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OLD_SEQUENCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `38`
- New: `40`

### Rust Evidence

- Graph edges: `1`

## W-000459 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_RESET
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_RESET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `41`
- New: `43`

### Rust Evidence

- Graph edges: `1`

## W-000460 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_TOO_OLD_ACK
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_TOO_OLD_ACK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `46`
- New: `48`

### Rust Evidence

- Graph edges: `1`

## W-000461 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_CHAIN_NOTFOUND
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_CHAIN_NOTFOUND changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `102`
- New: `104`

### Rust Evidence

- Graph edges: `1`

## W-000462 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_COOKIE_ERROR
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_COOKIE_ERROR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `100`
- New: `102`

### Rust Evidence

- Graph edges: `1`

## W-000463 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_EGRESS
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_EGRESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `57`
- New: `59`

### Rust Evidence

- Graph edges: `1`

## W-000464 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_INGRESS
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_INGRESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `68`
- New: `70`

### Rust Evidence

- Graph edges: `1`

## W-000465 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_RECLASSIFY_LOOP
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_RECLASSIFY_LOOP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `103`
- New: `105`

### Rust Evidence

- Graph edges: `1`

## W-000466 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TUNNEL_TXINFO
- Explanation: skb_drop_reason_SKB_DROP_REASON_TUNNEL_TXINFO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `110`
- New: `112`

### Rust Evidence

- Graph edges: `1`

## W-000467 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_UNHANDLED_PROTO
- Explanation: skb_drop_reason_SKB_DROP_REASON_UNHANDLED_PROTO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `69`
- New: `71`

### Rust Evidence

- Graph edges: `1`

## W-000468 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_VXLAN_ENTRY_EXISTS
- Explanation: skb_drop_reason_SKB_DROP_REASON_VXLAN_ENTRY_EXISTS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `107`
- New: `109`

### Rust Evidence

- Graph edges: `1`

## W-000469 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_VXLAN_INVALID_HDR
- Explanation: skb_drop_reason_SKB_DROP_REASON_VXLAN_INVALID_HDR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `104`
- New: `106`

### Rust Evidence

- Graph edges: `1`

## W-000470 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_VXLAN_VNI_NOT_FOUND
- Explanation: skb_drop_reason_SKB_DROP_REASON_VXLAN_VNI_NOT_FOUND changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `105`
- New: `107`

### Rust Evidence

- Graph edges: `1`

## W-000471 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_XDP
- Explanation: skb_drop_reason_SKB_DROP_REASON_XDP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `67`
- New: `69`

### Rust Evidence

- Graph edges: `1`

## W-000472 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_COMPACTFAIL
- Explanation: vm_event_item_COMPACTFAIL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `57`
- New: `59`

### Rust Evidence

- Graph edges: `1`

## W-000473 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_COMPACTFREE_SCANNED
- Explanation: vm_event_item_COMPACTFREE_SCANNED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `54`
- New: `56`

### Rust Evidence

- Graph edges: `1`

## W-000474 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_COMPACTISOLATED
- Explanation: vm_event_item_COMPACTISOLATED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `55`
- New: `57`

### Rust Evidence

- Graph edges: `1`

## W-000475 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_COMPACTMIGRATE_SCANNED
- Explanation: vm_event_item_COMPACTMIGRATE_SCANNED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `53`
- New: `55`

### Rust Evidence

- Graph edges: `1`

## W-000476 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_COMPACTSTALL
- Explanation: vm_event_item_COMPACTSTALL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `56`
- New: `58`

### Rust Evidence

- Graph edges: `1`

## W-000477 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_COMPACTSUCCESS
- Explanation: vm_event_item_COMPACTSUCCESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `58`
- New: `60`

### Rust Evidence

- Graph edges: `1`

## W-000478 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_DIRECT_MAP_LEVEL2_SPLIT
- Explanation: vm_event_item_DIRECT_MAP_LEVEL2_SPLIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `75`
- New: `77`

### Rust Evidence

- Graph edges: `1`

## W-000479 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_DIRECT_MAP_LEVEL3_SPLIT
- Explanation: vm_event_item_DIRECT_MAP_LEVEL3_SPLIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `76`
- New: `78`

### Rust Evidence

- Graph edges: `1`

## W-000480 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_DROP_PAGECACHE
- Explanation: vm_event_item_DROP_PAGECACHE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `45`
- New: `47`

### Rust Evidence

- Graph edges: `1`

## W-000481 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_DROP_SLAB
- Explanation: vm_event_item_DROP_SLAB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `46`
- New: `48`

### Rust Evidence

- Graph edges: `1`

## W-000483 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_HTLB_BUDDY_PGALLOC_FAIL
- Explanation: vm_event_item_HTLB_BUDDY_PGALLOC_FAIL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `63`
- New: `65`

### Rust Evidence

- Graph edges: `1`

## W-000484 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KCOMPACTD_FREE_SCANNED
- Explanation: vm_event_item_KCOMPACTD_FREE_SCANNED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `61`
- New: `63`

### Rust Evidence

- Graph edges: `1`

## W-000485 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KCOMPACTD_MIGRATE_SCANNED
- Explanation: vm_event_item_KCOMPACTD_MIGRATE_SCANNED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `60`
- New: `62`

### Rust Evidence

- Graph edges: `1`

## W-000486 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KCOMPACTD_WAKE
- Explanation: vm_event_item_KCOMPACTD_WAKE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `59`
- New: `61`

### Rust Evidence

- Graph edges: `1`

## W-000487 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KSTACK_16K
- Explanation: vm_event_item_KSTACK_16K changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `81`
- New: `85`

### Rust Evidence

- Graph edges: `1`

## W-000488 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KSTACK_1K
- Explanation: vm_event_item_KSTACK_1K changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `77`
- New: `81`

### Rust Evidence

- Graph edges: `1`

## W-000489 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KSTACK_2K
- Explanation: vm_event_item_KSTACK_2K changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `78`
- New: `82`

### Rust Evidence

- Graph edges: `1`

## W-000490 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KSTACK_4K
- Explanation: vm_event_item_KSTACK_4K changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `79`
- New: `83`

### Rust Evidence

- Graph edges: `1`

## W-000491 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KSTACK_8K
- Explanation: vm_event_item_KSTACK_8K changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `80`
- New: `84`

### Rust Evidence

- Graph edges: `1`

## W-000492 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KSWAPD_HIGH_WMARK_HIT_QUICKLY
- Explanation: vm_event_item_KSWAPD_HIGH_WMARK_HIT_QUICKLY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `42`
- New: `44`

### Rust Evidence

- Graph edges: `1`

## W-000493 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KSWAPD_INODESTEAL
- Explanation: vm_event_item_KSWAPD_INODESTEAL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `40`
- New: `42`

### Rust Evidence

- Graph edges: `1`

## W-000494 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KSWAPD_LOW_WMARK_HIT_QUICKLY
- Explanation: vm_event_item_KSWAPD_LOW_WMARK_HIT_QUICKLY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `41`
- New: `43`

### Rust Evidence

- Graph edges: `1`

## W-000495 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_NR_VM_EVENT_ITEMS
- Explanation: vm_event_item_NR_VM_EVENT_ITEMS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `82`
- New: `86`

### Rust Evidence

- Graph edges: `1`

## W-000496 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_OOM_KILL
- Explanation: vm_event_item_OOM_KILL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `47`
- New: `49`

### Rust Evidence

- Graph edges: `1`

## W-000497 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PAGEOUTRUN
- Explanation: vm_event_item_PAGEOUTRUN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `43`
- New: `45`

### Rust Evidence

- Graph edges: `1`

## W-000498 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGINODESTEAL
- Explanation: vm_event_item_PGINODESTEAL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `38`
- New: `40`

### Rust Evidence

- Graph edges: `1`

## W-000499 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGMIGRATE_FAIL
- Explanation: vm_event_item_PGMIGRATE_FAIL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `49`
- New: `51`

### Rust Evidence

- Graph edges: `1`

## W-000500 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGMIGRATE_SUCCESS
- Explanation: vm_event_item_PGMIGRATE_SUCCESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `50`

### Rust Evidence

- Graph edges: `1`

## W-000501 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGROTATED
- Explanation: vm_event_item_PGROTATED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `44`
- New: `46`

### Rust Evidence

- Graph edges: `1`

## W-000502 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGSCAN_ANON
- Explanation: vm_event_item_PGSCAN_ANON changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `32`
- New: `34`

### Rust Evidence

- Graph edges: `1`

## W-000504 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGSCAN_DIRECT_THROTTLE
- Explanation: vm_event_item_PGSCAN_DIRECT_THROTTLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `31`
- New: `33`

### Rust Evidence

- Graph edges: `1`

## W-000505 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGSCAN_FILE
- Explanation: vm_event_item_PGSCAN_FILE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `33`
- New: `35`

### Rust Evidence

- Graph edges: `1`

## W-000506 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGSCAN_KHUGEPAGED
- Explanation: vm_event_item_PGSCAN_KHUGEPAGED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `30`
- New: `31`

### Rust Evidence

- Graph edges: `1`

## W-000507 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGSCAN_KSWAPD
- Explanation: vm_event_item_PGSCAN_KSWAPD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `28`
- New: `29`

### Rust Evidence

- Graph edges: `1`

## W-000508 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGSCAN_ZONE_RECLAIM_FAILED
- Explanation: vm_event_item_PGSCAN_ZONE_RECLAIM_FAILED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `37`
- New: `39`

### Rust Evidence

- Graph edges: `1`

## W-000509 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGSCAN_ZONE_RECLAIM_SUCCESS
- Explanation: vm_event_item_PGSCAN_ZONE_RECLAIM_SUCCESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `36`
- New: `38`

### Rust Evidence

- Graph edges: `1`

## W-000510 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGSTEAL_ANON
- Explanation: vm_event_item_PGSTEAL_ANON changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `34`
- New: `36`

### Rust Evidence

- Graph edges: `1`

## W-000511 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGSTEAL_FILE
- Explanation: vm_event_item_PGSTEAL_FILE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `35`
- New: `37`

### Rust Evidence

- Graph edges: `1`

## W-000512 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_SLABS_SCANNED
- Explanation: vm_event_item_SLABS_SCANNED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `39`
- New: `41`

### Rust Evidence

- Graph edges: `1`

## W-000514 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_SWAP_RA_HIT
- Explanation: vm_event_item_SWAP_RA_HIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `72`
- New: `74`

### Rust Evidence

- Graph edges: `1`

## W-000515 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_SWPIN_ZERO
- Explanation: vm_event_item_SWPIN_ZERO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `73`
- New: `75`

### Rust Evidence

- Graph edges: `1`

## W-000516 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_SWPOUT_ZERO
- Explanation: vm_event_item_SWPOUT_ZERO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `74`
- New: `76`

### Rust Evidence

- Graph edges: `1`

## W-000517 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_THP_MIGRATION_FAIL
- Explanation: vm_event_item_THP_MIGRATION_FAIL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `51`
- New: `53`

### Rust Evidence

- Graph edges: `1`

## W-000518 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_THP_MIGRATION_SPLIT
- Explanation: vm_event_item_THP_MIGRATION_SPLIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `52`
- New: `54`

### Rust Evidence

- Graph edges: `1`

## W-000519 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_THP_MIGRATION_SUCCESS
- Explanation: vm_event_item_THP_MIGRATION_SUCCESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `50`
- New: `52`

### Rust Evidence

- Graph edges: `1`

## W-000520 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_UNEVICTABLE_PGCLEARED
- Explanation: vm_event_item_UNEVICTABLE_PGCLEARED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `69`
- New: `71`

### Rust Evidence

- Graph edges: `1`

## W-000521 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_UNEVICTABLE_PGCULLED
- Explanation: vm_event_item_UNEVICTABLE_PGCULLED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `64`
- New: `66`

### Rust Evidence

- Graph edges: `1`

## W-000522 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_UNEVICTABLE_PGMLOCKED
- Explanation: vm_event_item_UNEVICTABLE_PGMLOCKED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `67`
- New: `69`

### Rust Evidence

- Graph edges: `1`

## W-000523 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_UNEVICTABLE_PGMUNLOCKED
- Explanation: vm_event_item_UNEVICTABLE_PGMUNLOCKED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `68`
- New: `70`

### Rust Evidence

- Graph edges: `1`

## W-000524 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_UNEVICTABLE_PGRESCUED
- Explanation: vm_event_item_UNEVICTABLE_PGRESCUED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `66`
- New: `68`

### Rust Evidence

- Graph edges: `1`

## W-000525 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_UNEVICTABLE_PGSCANNED
- Explanation: vm_event_item_UNEVICTABLE_PGSCANNED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `65`
- New: `67`

### Rust Evidence

- Graph edges: `1`

## W-000526 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_UNEVICTABLE_PGSTRANDED
- Explanation: vm_event_item_UNEVICTABLE_PGSTRANDED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `70`
- New: `72`

### Rust Evidence

- Graph edges: `1`

## W-000527 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: zone_stat_item_NR_BOUNCE
- Explanation: zone_stat_item_NR_BOUNCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `9`

### Rust Evidence

- Graph edges: `1`

## W-000528 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: zone_stat_item_NR_FREE_CMA_PAGES
- Explanation: zone_stat_item_NR_FREE_CMA_PAGES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `9`
- New: `10`

### Rust Evidence

- Graph edges: `1`

## W-000529 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: zone_stat_item_NR_MLOCK
- Explanation: zone_stat_item_NR_MLOCK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `7`
- New: `8`

### Rust Evidence

- Graph edges: `1`

## W-000530 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: zone_stat_item_NR_VM_ZONE_STAT_ITEMS
- Explanation: zone_stat_item_NR_VM_ZONE_STAT_ITEMS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `11`

### Rust Evidence

- Graph edges: `1`

## W-000531 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: zone_stat_item_NR_ZONE_ACTIVE_ANON
- Explanation: zone_stat_item_NR_ZONE_ACTIVE_ANON changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `2`
- New: `3`

### Rust Evidence

- Graph edges: `1`

## W-000532 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: zone_stat_item_NR_ZONE_ACTIVE_FILE
- Explanation: zone_stat_item_NR_ZONE_ACTIVE_FILE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `4`
- New: `5`

### Rust Evidence

- Graph edges: `1`

## W-000533 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: zone_stat_item_NR_ZONE_INACTIVE_ANON
- Explanation: zone_stat_item_NR_ZONE_INACTIVE_ANON changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `1`
- New: `2`

### Rust Evidence

- Graph edges: `1`

## W-000534 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: zone_stat_item_NR_ZONE_INACTIVE_FILE
- Explanation: zone_stat_item_NR_ZONE_INACTIVE_FILE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `3`
- New: `4`

### Rust Evidence

- Graph edges: `1`

## W-000535 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: zone_stat_item_NR_ZONE_LRU_BASE
- Explanation: zone_stat_item_NR_ZONE_LRU_BASE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `1`
- New: `2`

### Rust Evidence

- Graph edges: `1`

## W-000536 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: zone_stat_item_NR_ZONE_UNEVICTABLE
- Explanation: zone_stat_item_NR_ZONE_UNEVICTABLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `6`

### Rust Evidence

- Graph edges: `1`

## W-000537 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: zone_stat_item_NR_ZONE_WRITE_PENDING
- Explanation: zone_stat_item_NR_ZONE_WRITE_PENDING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `6`
- New: `7`

### Rust Evidence

- Graph edges: `1`

## W-000539 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: FOP_DONTCACHE
- Explanation: FOP_DONTCACHE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `((__force fop_flags_t)(1 << 7))`
- New: `0 /* ((__force fop_flags_t)(1 << 7)) */`

### Rust Evidence

- Graph edges: `1`

## W-000538 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: EDP_DISPLAY_CTL_CAP_SIZE
- Explanation: EDP_DISPLAY_CTL_CAP_SIZE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `3`
- New: `5`

### Rust Evidence

- Graph edges: `0`

## W-000540 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: TTM_TT_FLAG_PRIV_POPULATED
- Explanation: TTM_TT_FLAG_PRIV_POPULATED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `BIT(5)`
- New: `BIT(6)`

### Rust Evidence

- Graph edges: `0`
