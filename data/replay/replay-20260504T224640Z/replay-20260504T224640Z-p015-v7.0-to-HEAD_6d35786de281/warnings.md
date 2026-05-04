# BindDrift Ranked Warnings

## W-000001 SignatureDrift

- Risk: High
- Score: 14.6
- Symbol: INIT_LIST_HEAD
- Explanation: INIT_LIST_HEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `21`

## W-000181 SignatureDrift

- Risk: High
- Score: 14.4
- Symbol: vm_mmap
- Explanation: vm_mmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut file'}, {'name': 'arg2', 'type': 'ffi::c_ulong'}, {'name': 'arg3', 'type': 'ffi::c_ulong'}, {'name': 'arg4', 'type': 'ffi::c_ulong'}, {'name': 'arg5', 'type': 'ffi::c_ulong'}, {'name': 'arg6', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_ulong'}`
- New: `{'params': [{'name': 'file', 'type': '*mut file'}, {'name': 'addr', 'type': 'ffi::c_ulong'}, {'name': 'len', 'type': 'ffi::c_ulong'}, {'name': 'prot', 'type': 'ffi::c_ulong'}, {'name': 'flag', 'type': 'ffi::c_ulong'}, {'name': 'offset', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_ulong'}`

### Rust Evidence

- Graph edges: `19`

## W-000707 SignatureDrift

- Risk: High
- Score: 14.4
- Symbol: vm_mmap
- Explanation: vm_mmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct file *', 'unsigned long', 'unsigned long', 'unsigned long', 'unsigned long', 'unsigned long'], 'return_type': 'extern unsigned long __must_check'}`
- New: `{'params': ['struct file *file', 'unsigned long addr', 'unsigned long len', 'unsigned long prot', 'unsigned long flag', 'unsigned long offset'], 'return_type': 'unsigned long __must_check'}`

### Rust Evidence

- Graph edges: `19`

## W-000689 SignatureDrift

- Risk: High
- Score: 14.0
- Symbol: resource_size_t
- Explanation: resource_size_t changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['*resource_alignf)(void *data, const struct resource *res, resource_size_t size, resource_size_t align'], 'return_type': 'typedef'}`
- New: `{'params': ['*resource_alignf)(void *data, const struct resource *res, const struct resource *empty_res, resource_size_t size, resource_size_t align'], 'return_type': 'typedef'}`

### Rust Evidence

- Graph edges: `17`

## W-000134 SignatureDrift

- Risk: High
- Score: 13.2
- Symbol: list_add_tail
- Explanation: list_add_tail changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `13`

## W-000195 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: cgroup
- Explanation: cgroup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'self_', 'type': 'cgroup_subsys_state'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'level', 'type': 'ffi::c_int'}, {'name': 'max_depth', 'type': 'ffi::c_int'}, {'name': 'nr_descendants', 'type': 'ffi::c_int'}, {'name': 'nr_dying_descendants', 'type': 'ffi::c_int'}, {'name': 'max_descendants', 'type': 'ffi::c_int'}, {'name': 'nr_populated_csets', 'type': 'ffi::c_int'}, {'name': 'nr_populated_domain_children', 'type': 'ffi::c_int'}, {'name': 'nr_populated_threaded_children', 'type': 'ffi::c_int'}, {'name': 'nr_threaded_children', 'type': 'ffi::c_int'}, {'name': 'kill_seq', 'type': 'ffi::c_uint'}, {'name': 'kn', 'type': '*mut kernfs_node'}, {'name': 'procs_file', 'type': 'cgroup_file'}, {'name': 'events_file', 'type': 'cgroup_file'}, {'name': 'psi_files', 'type': '__IncompleteArrayField<cgroup_file>'}, {'name': 'subtree_control', 'type': 'u32_'}, {'name': 'subtree_ss_mask', 'type': 'u32_'}, {'name': 'old_subtree_control', 'type': 'u32_'}, {'name': 'old_subtree_ss_mask', 'type': 'u32_'}, {'name': 'subsys', 'type': '[*mut cgroup_subsys_state; 14usize]'}, {'name': 'nr_dying_subsys', 'type': '[ffi::c_int; 14usize]'}, {'name': 'root', 'type': '*mut cgroup_root'}, {'name': 'cset_links', 'type': 'list_head'}, {'name': 'e_csets', 'type': '[list_head; 14usize]'}, {'name': 'dom_cgrp', 'type': '*mut cgroup'}, {'name': 'old_dom_cgrp', 'type': '*mut cgroup'}, {'name': 'rstat_base_cpu', 'type': '*mut cgroup_rstat_base_cpu'}, {'name': '_pad_', 'type': 'cacheline_padding'}, {'name': 'last_bstat', 'type': 'cgroup_base_stat'}, {'name': 'bstat', 'type': 'cgroup_base_stat'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'pidlists', 'type': 'list_head'}, {'name': 'pidlist_mutex', 'type': 'mutex'}, {'name': 'offline_waitq', 'type': 'wait_queue_head_t'}, {'name': 'dying_populated_waitq', 'type': 'wait_queue_head_t'}, {'name': 'release_agent_work', 'type': 'work_struct'}, {'name': 'psi', 'type': '*mut psi_group'}, {'name': 'bpf', 'type': 'cgroup_bpf'}, {'name': 'freezer', 'type': 'cgroup_freezer_state'}, {'name': '__bindgen_anon_1', 'type': 'cgroup__bindgen_ty_1'}]`
- New: `[{'name': 'self_', 'type': 'cgroup_subsys_state'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'level', 'type': 'ffi::c_int'}, {'name': 'max_depth', 'type': 'ffi::c_int'}, {'name': 'nr_descendants', 'type': 'ffi::c_int'}, {'name': 'nr_dying_descendants', 'type': 'ffi::c_int'}, {'name': 'max_descendants', 'type': 'ffi::c_int'}, {'name': 'nr_populated_csets', 'type': 'ffi::c_int'}, {'name': 'nr_populated_domain_children', 'type': 'ffi::c_int'}, {'name': 'nr_populated_threaded_children', 'type': 'ffi::c_int'}, {'name': 'nr_threaded_children', 'type': 'ffi::c_int'}, {'name': 'kill_seq', 'type': 'ffi::c_uint'}, {'name': 'kn', 'type': '*mut kernfs_node'}, {'name': 'procs_file', 'type': 'cgroup_file'}, {'name': 'events_file', 'type': 'cgroup_file'}, {'name': 'psi_files', 'type': '__IncompleteArrayField<cgroup_file>'}, {'name': 'subtree_control', 'type': 'u32_'}, {'name': 'subtree_ss_mask', 'type': 'u32_'}, {'name': 'old_subtree_control', 'type': 'u32_'}, {'name': 'old_subtree_ss_mask', 'type': 'u32_'}, {'name': 'subsys', 'type': '[*mut cgroup_subsys_state; 14usize]'}, {'name': 'nr_dying_subsys', 'type': '[ffi::c_int; 14usize]'}, {'name': 'root', 'type': '*mut cgroup_root'}, {'name': 'cset_links', 'type': 'list_head'}, {'name': 'e_csets', 'type': '[list_head; 14usize]'}, {'name': 'dom_cgrp', 'type': '*mut cgroup'}, {'name': 'old_dom_cgrp', 'type': '*mut cgroup'}, {'name': 'rstat_base_cpu', 'type': '*mut cgroup_rstat_base_cpu'}, {'name': '__bindgen_padding_0', 'type': '[u64; 6usize]'}, {'name': '_pad_', 'type': 'cacheline_padding'}, {'name': 'last_bstat', 'type': 'cgroup_base_stat'}, {'name': 'bstat', 'type': 'cgroup_base_stat'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'pidlists', 'type': 'list_head'}, {'name': 'pidlist_mutex', 'type': 'mutex'}, {'name': 'offline_waitq', 'type': 'wait_queue_head_t'}, {'name': 'dying_populated_waitq', 'type': 'wait_queue_head_t'}, {'name': 'release_agent_work', 'type': 'work_struct'}, {'name': 'psi', 'type': '*mut psi_group'}, {'name': 'bpf', 'type': 'cgroup_bpf'}, {'name': 'freezer', 'type': 'cgroup_freezer_state'}, {'name': '__bindgen_anon_1', 'type': 'cgroup__bindgen_ty_1'}]`

### Rust Evidence

- Graph edges: `50`

## W-000197 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: class
- Explanation: class changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'class_groups', 'type': '*mut *const attribute_group'}, {'name': 'dev_groups', 'type': '*mut *const attribute_group'}, {'name': 'dev_uevent', 'type': '::core::option::Option<'}, {'name': 'devnode', 'type': '::core::option::Option<'}, {'name': 'class_release', 'type': '::core::option::Option<unsafe extern "C" fn(class: *const class)>'}, {'name': 'dev_release', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'shutdown_pre', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'ns_type', 'type': '*const kobj_ns_type_operations'}, {'name': 'get_ownership', 'type': '::core::option::Option<'}, {'name': 'pm', 'type': '*const dev_pm_ops'}]`
- New: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'class_groups', 'type': '*const *const attribute_group'}, {'name': 'dev_groups', 'type': '*const *const attribute_group'}, {'name': 'dev_uevent', 'type': '::core::option::Option<'}, {'name': 'devnode', 'type': '::core::option::Option<'}, {'name': 'class_release', 'type': '::core::option::Option<unsafe extern "C" fn(class: *const class)>'}, {'name': 'dev_release', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'shutdown_pre', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'ns_type', 'type': '*const kobj_ns_type_operations'}, {'name': 'get_ownership', 'type': '::core::option::Option<'}, {'name': 'pm', 'type': '*const dev_pm_ops'}]`

### Rust Evidence

- Graph edges: `50`

## W-000198 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: cpufreq_policy
- Explanation: cpufreq_policy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'cpus', 'type': 'cpumask_var_t'}, {'name': 'related_cpus', 'type': 'cpumask_var_t'}, {'name': 'real_cpus', 'type': 'cpumask_var_t'}, {'name': 'shared_type', 'type': 'ffi::c_uint'}, {'name': 'cpu', 'type': 'ffi::c_uint'}, {'name': 'clk', 'type': '*mut clk'}, {'name': 'cpuinfo', 'type': 'cpufreq_cpuinfo'}, {'name': 'min', 'type': 'ffi::c_uint'}, {'name': 'max', 'type': 'ffi::c_uint'}, {'name': 'cur', 'type': 'ffi::c_uint'}, {'name': 'suspend_freq', 'type': 'ffi::c_uint'}, {'name': 'policy', 'type': 'ffi::c_uint'}, {'name': 'last_policy', 'type': 'ffi::c_uint'}, {'name': 'governor', 'type': '*mut cpufreq_governor'}, {'name': 'governor_data', 'type': '*mut ffi::c_void'}, {'name': 'last_governor', 'type': '[ffi::c_char; 16usize]'}, {'name': 'update', 'type': 'work_struct'}, {'name': 'constraints', 'type': 'freq_constraints'}, {'name': 'min_freq_req', 'type': '*mut freq_qos_request'}, {'name': 'max_freq_req', 'type': '*mut freq_qos_request'}, {'name': 'freq_table', 'type': '*mut cpufreq_frequency_table'}, {'name': 'freq_table_sorted', 'type': 'cpufreq_table_sorting'}, {'name': 'policy_list', 'type': 'list_head'}, {'name': 'kobj', 'type': 'kobject'}, {'name': 'kobj_unregister', 'type': 'completion'}, {'name': 'rwsem', 'type': 'rw_semaphore'}, {'name': 'fast_switch_possible', 'type': 'bool_'}, {'name': 'fast_switch_enabled', 'type': 'bool_'}, {'name': 'strict_target', 'type': 'bool_'}, {'name': 'efficiencies_available', 'type': 'bool_'}, {'name': 'transition_delay_us', 'type': 'ffi::c_uint'}, {'name': 'dvfs_possible_from_any_cpu', 'type': 'bool_'}, {'name': 'boost_enabled', 'type': 'bool_'}, {'name': 'boost_supported', 'type': 'bool_'}, {'name': 'cached_target_freq', 'type': 'ffi::c_uint'}, {'name': 'cached_resolved_idx', 'type': 'ffi::c_uint'}, {'name': 'transition_ongoing', 'type': 'bool_'}, {'name': 'transition_lock', 'type': 'spinlock_t'}, {'name': 'transition_wait', 'type': 'wait_queue_head_t'}, {'name': 'transition_task', 'type': '*mut task_struct'}, {'name': 'stats', 'type': '*mut cpufreq_stats'}, {'name': 'driver_data', 'type': '*mut ffi::c_void'}, {'name': 'cdev', 'type': '*mut thermal_cooling_device'}, {'name': 'nb_min', 'type': 'notifier_block'}, {'name': 'nb_max', 'type': 'notifier_block'}]`
- New: `[{'name': 'cpus', 'type': 'cpumask_var_t'}, {'name': 'related_cpus', 'type': 'cpumask_var_t'}, {'name': 'real_cpus', 'type': 'cpumask_var_t'}, {'name': 'shared_type', 'type': 'ffi::c_uint'}, {'name': 'cpu', 'type': 'ffi::c_uint'}, {'name': 'clk', 'type': '*mut clk'}, {'name': 'cpuinfo', 'type': 'cpufreq_cpuinfo'}, {'name': 'min', 'type': 'ffi::c_uint'}, {'name': 'max', 'type': 'ffi::c_uint'}, {'name': 'cur', 'type': 'ffi::c_uint'}, {'name': 'suspend_freq', 'type': 'ffi::c_uint'}, {'name': 'policy', 'type': 'ffi::c_uint'}, {'name': 'last_policy', 'type': 'ffi::c_uint'}, {'name': 'governor', 'type': '*mut cpufreq_governor'}, {'name': 'governor_data', 'type': '*mut ffi::c_void'}, {'name': 'last_governor', 'type': '[ffi::c_char; 16usize]'}, {'name': 'update', 'type': 'work_struct'}, {'name': 'constraints', 'type': 'freq_constraints'}, {'name': 'min_freq_req', 'type': 'freq_qos_request'}, {'name': 'max_freq_req', 'type': 'freq_qos_request'}, {'name': 'boost_freq_req', 'type': 'freq_qos_request'}, {'name': 'freq_table', 'type': '*mut cpufreq_frequency_table'}, {'name': 'freq_table_sorted', 'type': 'cpufreq_table_sorting'}, {'name': 'policy_list', 'type': 'list_head'}, {'name': 'kobj', 'type': 'kobject'}, {'name': 'kobj_unregister', 'type': 'completion'}, {'name': 'rwsem', 'type': 'rw_semaphore'}, {'name': 'fast_switch_possible', 'type': 'bool_'}, {'name': 'fast_switch_enabled', 'type': 'bool_'}, {'name': 'strict_target', 'type': 'bool_'}, {'name': 'efficiencies_available', 'type': 'bool_'}, {'name': 'transition_delay_us', 'type': 'ffi::c_uint'}, {'name': 'dvfs_possible_from_any_cpu', 'type': 'bool_'}, {'name': 'boost_enabled', 'type': 'bool_'}, {'name': 'boost_supported', 'type': 'bool_'}, {'name': 'cached_target_freq', 'type': 'ffi::c_uint'}, {'name': 'cached_resolved_idx', 'type': 'ffi::c_uint'}, {'name': 'transition_ongoing', 'type': 'bool_'}, {'name': 'transition_lock', 'type': 'spinlock_t'}, {'name': 'transition_wait', 'type': 'wait_queue_head_t'}, {'name': 'transition_task', 'type': '*mut task_struct'}, {'name': 'stats', 'type': '*mut cpufreq_stats'}, {'name': 'driver_data', 'type': '*mut ffi::c_void'}, {'name': 'cdev', 'type': '*mut thermal_cooling_device'}, {'name': 'nb_min', 'type': 'notifier_block'}, {'name': 'nb_max', 'type': 'notifier_block'}]`

### Rust Evidence

- Graph edges: `50`

## W-000200 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: dentry
- Explanation: dentry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'd_flags', 'type': 'ffi::c_uint'}, {'name': 'd_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'd_hash', 'type': 'hlist_bl_node'}, {'name': 'd_parent', 'type': '*mut dentry'}, {'name': '__bindgen_anon_1', 'type': 'dentry__bindgen_ty_1'}, {'name': 'd_inode', 'type': '*mut inode'}, {'name': 'd_shortname', 'type': 'shortname_store'}, {'name': 'd_op', 'type': '*const dentry_operations'}, {'name': 'd_sb', 'type': '*mut super_block'}, {'name': 'd_time', 'type': 'ffi::c_ulong'}, {'name': 'd_fsdata', 'type': '*mut ffi::c_void'}, {'name': 'd_lockref', 'type': 'lockref'}, {'name': '__bindgen_anon_2', 'type': 'dentry__bindgen_ty_2'}, {'name': 'd_sib', 'type': 'hlist_node'}, {'name': 'd_children', 'type': 'hlist_head'}, {'name': 'd_u', 'type': 'dentry__bindgen_ty_3'}]`
- New: `[{'name': 'd_flags', 'type': 'ffi::c_uint'}, {'name': 'd_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'd_hash', 'type': 'hlist_bl_node'}, {'name': 'd_parent', 'type': '*mut dentry'}, {'name': '__bindgen_anon_1', 'type': 'dentry__bindgen_ty_1'}, {'name': 'd_inode', 'type': '*mut inode'}, {'name': 'd_shortname', 'type': 'shortname_store'}, {'name': 'd_op', 'type': '*const dentry_operations'}, {'name': 'd_sb', 'type': '*mut super_block'}, {'name': 'd_time', 'type': 'ffi::c_ulong'}, {'name': 'd_fsdata', 'type': '*mut ffi::c_void'}, {'name': 'd_lockref', 'type': 'lockref'}, {'name': '__bindgen_anon_2', 'type': 'dentry__bindgen_ty_2'}, {'name': 'd_sib', 'type': 'hlist_node'}, {'name': 'd_children', 'type': 'hlist_head'}, {'name': '__bindgen_anon_3', 'type': 'dentry__bindgen_ty_3'}]`

### Rust Evidence

- Graph edges: `50`

## W-000201 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: device
- Explanation: device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'kobj', 'type': 'kobject'}, {'name': 'parent', 'type': '*mut device'}, {'name': 'p', 'type': '*mut device_private'}, {'name': 'init_name', 'type': '*const ffi::c_char'}, {'name': 'type_', 'type': '*const device_type'}, {'name': 'bus', 'type': '*const bus_type'}, {'name': 'driver', 'type': '*mut device_driver'}, {'name': 'platform_data', 'type': '*mut ffi::c_void'}, {'name': 'driver_data', 'type': '*mut ffi::c_void'}, {'name': 'driver_override', 'type': 'device__bindgen_ty_1'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'links', 'type': 'dev_links_info'}, {'name': 'power', 'type': 'dev_pm_info'}, {'name': 'pm_domain', 'type': '*mut dev_pm_domain'}, {'name': 'msi', 'type': 'dev_msi_info'}, {'name': 'dma_mask', 'type': '*mut u64_'}, {'name': 'coherent_dma_mask', 'type': 'u64_'}, {'name': 'bus_dma_limit', 'type': 'u64_'}, {'name': 'dma_range_map', 'type': '*mut bus_dma_region'}, {'name': 'dma_parms', 'type': '*mut device_dma_parameters'}, {'name': 'dma_pools', 'type': 'list_head'}, {'name': 'dma_io_tlb_mem', 'type': '*mut io_tlb_mem'}, {'name': 'archdata', 'type': 'dev_archdata'}, {'name': 'of_node', 'type': '*mut device_node'}, {'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'numa_node', 'type': 'ffi::c_int'}, {'name': 'devt', 'type': 'dev_t'}, {'name': 'id', 'type': 'u32_'}, {'name': 'devres_lock', 'type': 'spinlock_t'}, {'name': 'devres_head', 'type': 'list_head'}, {'name': 'class', 'type': '*const class'}, {'name': 'groups', 'type': '*mut *const attribute_group'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'iommu_group', 'type': '*mut iommu_group'}, {'name': 'iommu', 'type': '*mut dev_iommu'}, {'name': 'physical_location', 'type': '*mut device_physical_location'}, {'name': 'removable', 'type': 'device_removable'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 3usize]'}]`
- New: `[{'name': 'kobj', 'type': 'kobject'}, {'name': 'parent', 'type': '*mut device'}, {'name': 'p', 'type': '*mut device_private'}, {'name': 'init_name', 'type': '*const ffi::c_char'}, {'name': 'type_', 'type': '*const device_type'}, {'name': 'bus', 'type': '*const bus_type'}, {'name': 'driver', 'type': '*mut device_driver'}, {'name': 'platform_data', 'type': '*mut ffi::c_void'}, {'name': 'driver_data', 'type': '*mut ffi::c_void'}, {'name': 'driver_override', 'type': 'device__bindgen_ty_1'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'links', 'type': 'dev_links_info'}, {'name': 'power', 'type': 'dev_pm_info'}, {'name': 'pm_domain', 'type': '*mut dev_pm_domain'}, {'name': 'msi', 'type': 'dev_msi_info'}, {'name': 'dma_mask', 'type': '*mut u64_'}, {'name': 'coherent_dma_mask', 'type': 'u64_'}, {'name': 'bus_dma_limit', 'type': 'u64_'}, {'name': 'dma_range_map', 'type': '*mut bus_dma_region'}, {'name': 'dma_parms', 'type': '*mut device_dma_parameters'}, {'name': 'dma_pools', 'type': 'list_head'}, {'name': 'dma_io_tlb_mem', 'type': '*mut io_tlb_mem'}, {'name': 'archdata', 'type': 'dev_archdata'}, {'name': 'of_node', 'type': '*mut device_node'}, {'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'numa_node', 'type': 'ffi::c_int'}, {'name': 'devt', 'type': 'dev_t'}, {'name': 'id', 'type': 'u32_'}, {'name': 'devres_lock', 'type': 'spinlock_t'}, {'name': 'devres_head', 'type': 'list_head'}, {'name': 'class', 'type': '*const class'}, {'name': 'groups', 'type': '*mut *const attribute_group'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'iommu_group', 'type': '*mut iommu_group'}, {'name': 'iommu', 'type': '*mut dev_iommu'}, {'name': 'physical_location', 'type': '*mut device_physical_location'}, {'name': 'removable', 'type': 'device_removable'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'flags', 'type': '[ffi::c_ulong; 1usize]'}]`

### Rust Evidence

- Graph edges: `50`

## W-000203 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: dma_fence
- Explanation: dma_fence changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'lock', 'type': '*mut spinlock_t'}, {'name': 'ops', 'type': '*const dma_fence_ops'}, {'name': '__bindgen_anon_1', 'type': 'dma_fence__bindgen_ty_1'}, {'name': 'context', 'type': 'u64_'}, {'name': 'seqno', 'type': 'u64_'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'refcount', 'type': 'kref'}, {'name': 'error', 'type': 'ffi::c_int'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'dma_fence__bindgen_ty_1'}, {'name': 'ops', 'type': '*const dma_fence_ops'}, {'name': '__bindgen_anon_2', 'type': 'dma_fence__bindgen_ty_2'}, {'name': 'context', 'type': 'u64_'}, {'name': 'seqno', 'type': 'u64_'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'refcount', 'type': 'kref'}, {'name': 'error', 'type': 'ffi::c_int'}]`

### Rust Evidence

- Graph edges: `34`

## W-000209 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: fwnode_handle
- Explanation: fwnode_handle changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'secondary', 'type': '*mut fwnode_handle'}, {'name': 'ops', 'type': '*const fwnode_operations'}, {'name': 'dev', 'type': '*mut device'}, {'name': 'suppliers', 'type': 'list_head'}, {'name': 'consumers', 'type': 'list_head'}, {'name': 'flags', 'type': 'u8_'}]`
- New: `[{'name': 'secondary', 'type': '*mut fwnode_handle'}, {'name': 'ops', 'type': '*const fwnode_operations'}, {'name': 'dev', 'type': '*mut device'}, {'name': 'suppliers', 'type': 'list_head'}, {'name': 'consumers', 'type': 'list_head'}, {'name': 'flags', 'type': 'ffi::c_ulong'}]`

### Rust Evidence

- Graph edges: `28`

## W-000210 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: hrtimer
- Explanation: hrtimer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'node', 'type': 'timerqueue_node'}, {'name': '_softexpires', 'type': 'ktime_t'}, {'name': 'base', 'type': '*mut hrtimer_clock_base'}, {'name': 'state', 'type': 'u8_'}, {'name': 'is_rel', 'type': 'u8_'}, {'name': 'is_soft', 'type': 'u8_'}, {'name': 'is_hard', 'type': 'u8_'}]`
- New: `[{'name': 'node', 'type': 'timerqueue_linked_node'}, {'name': 'base', 'type': '*mut hrtimer_clock_base'}, {'name': 'is_queued', 'type': 'bool_'}, {'name': 'is_rel', 'type': 'bool_'}, {'name': 'is_soft', 'type': 'bool_'}, {'name': 'is_hard', 'type': 'bool_'}, {'name': 'is_lazy', 'type': 'bool_'}, {'name': '_softexpires', 'type': 'ktime_t'}]`

### Rust Evidence

- Graph edges: `50`

## W-000213 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: inode
- Explanation: inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'i_mode', 'type': 'umode_t'}, {'name': 'i_opflags', 'type': 'ffi::c_ushort'}, {'name': 'i_flags', 'type': 'ffi::c_uint'}, {'name': 'i_acl', 'type': '*mut posix_acl'}, {'name': 'i_default_acl', 'type': '*mut posix_acl'}, {'name': 'i_uid', 'type': 'kuid_t'}, {'name': 'i_gid', 'type': 'kgid_t'}, {'name': 'i_op', 'type': '*const inode_operations'}, {'name': 'i_sb', 'type': '*mut super_block'}, {'name': 'i_mapping', 'type': '*mut address_space'}, {'name': 'i_security', 'type': '*mut ffi::c_void'}, {'name': 'i_ino', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'inode__bindgen_ty_1'}, {'name': 'i_rdev', 'type': 'dev_t'}, {'name': 'i_size', 'type': 'loff_t'}, {'name': 'i_atime_sec', 'type': 'time64_t'}, {'name': 'i_mtime_sec', 'type': 'time64_t'}, {'name': 'i_ctime_sec', 'type': 'time64_t'}, {'name': 'i_atime_nsec', 'type': 'u32_'}, {'name': 'i_mtime_nsec', 'type': 'u32_'}, {'name': 'i_ctime_nsec', 'type': 'u32_'}, {'name': 'i_generation', 'type': 'u32_'}, {'name': 'i_lock', 'type': 'spinlock_t'}, {'name': 'i_bytes', 'type': 'ffi::c_ushort'}, {'name': 'i_blkbits', 'type': 'u8_'}, {'name': 'i_write_hint', 'type': 'rw_hint'}, {'name': 'i_blocks', 'type': 'blkcnt_t'}, {'name': 'i_state', 'type': 'inode_state_flags'}, {'name': 'i_rwsem', 'type': 'rw_semaphore'}, {'name': 'dirtied_when', 'type': 'ffi::c_ulong'}, {'name': 'dirtied_time_when', 'type': 'ffi::c_ulong'}, {'name': 'i_hash', 'type': 'hlist_node'}, {'name': 'i_io_list', 'type': 'list_head'}, {'name': 'i_lru', 'type': 'list_head'}, {'name': 'i_sb_list', 'type': 'list_head'}, {'name': 'i_wb_list', 'type': 'list_head'}, {'name': '__bindgen_anon_2', 'type': 'inode__bindgen_ty_2'}, {'name': 'i_version', 'type': 'atomic64_t'}, {'name': 'i_sequence', 'type': 'atomic64_t'}, {'name': 'i_count', 'type': 'atomic_t'}, {'name': 'i_dio_count', 'type': 'atomic_t'}, {'name': 'i_writecount', 'type': 'atomic_t'}, {'name': 'i_readcount', 'type': 'atomic_t'}, {'name': '__bindgen_anon_3', 'type': 'inode__bindgen_ty_3'}, {'name': 'i_flctx', 'type': '*mut file_lock_context'}, {'name': 'i_data', 'type': 'address_space'}, {'name': '__bindgen_anon_4', 'type': 'inode__bindgen_ty_4'}, {'name': '__bindgen_anon_5', 'type': 'inode__bindgen_ty_5'}, {'name': 'i_fsnotify_mask', 'type': '__u32'}, {'name': 'i_fsnotify_marks', 'type': '*mut fsnotify_mark_connector'}, {'name': 'i_private', 'type': '*mut ffi::c_void'}]`
- New: `[{'name': 'i_mode', 'type': 'umode_t'}, {'name': 'i_opflags', 'type': 'ffi::c_ushort'}, {'name': 'i_flags', 'type': 'ffi::c_uint'}, {'name': 'i_acl', 'type': '*mut posix_acl'}, {'name': 'i_default_acl', 'type': '*mut posix_acl'}, {'name': 'i_uid', 'type': 'kuid_t'}, {'name': 'i_gid', 'type': 'kgid_t'}, {'name': 'i_op', 'type': '*const inode_operations'}, {'name': 'i_sb', 'type': '*mut super_block'}, {'name': 'i_mapping', 'type': '*mut address_space'}, {'name': 'i_security', 'type': '*mut ffi::c_void'}, {'name': 'i_ino', 'type': 'u64_'}, {'name': '__bindgen_anon_1', 'type': 'inode__bindgen_ty_1'}, {'name': 'i_rdev', 'type': 'dev_t'}, {'name': 'i_size', 'type': 'loff_t'}, {'name': 'i_atime_sec', 'type': 'time64_t'}, {'name': 'i_mtime_sec', 'type': 'time64_t'}, {'name': 'i_ctime_sec', 'type': 'time64_t'}, {'name': 'i_atime_nsec', 'type': 'u32_'}, {'name': 'i_mtime_nsec', 'type': 'u32_'}, {'name': 'i_ctime_nsec', 'type': 'u32_'}, {'name': 'i_generation', 'type': 'u32_'}, {'name': 'i_lock', 'type': 'spinlock_t'}, {'name': 'i_bytes', 'type': 'ffi::c_ushort'}, {'name': 'i_blkbits', 'type': 'u8_'}, {'name': 'i_write_hint', 'type': 'rw_hint'}, {'name': 'i_blocks', 'type': 'blkcnt_t'}, {'name': 'i_state', 'type': 'inode_state_flags'}, {'name': 'i_rwsem', 'type': 'rw_semaphore'}, {'name': 'dirtied_when', 'type': 'ffi::c_ulong'}, {'name': 'dirtied_time_when', 'type': 'ffi::c_ulong'}, {'name': 'i_hash', 'type': 'hlist_node'}, {'name': 'i_io_list', 'type': 'list_head'}, {'name': 'i_lru', 'type': 'list_head'}, {'name': 'i_sb_list', 'type': 'list_head'}, {'name': 'i_wb_list', 'type': 'list_head'}, {'name': '__bindgen_anon_2', 'type': 'inode__bindgen_ty_2'}, {'name': 'i_version', 'type': 'atomic64_t'}, {'name': 'i_sequence', 'type': 'atomic64_t'}, {'name': 'i_count', 'type': 'atomic_t'}, {'name': 'i_dio_count', 'type': 'atomic_t'}, {'name': 'i_writecount', 'type': 'atomic_t'}, {'name': 'i_readcount', 'type': 'atomic_t'}, {'name': '__bindgen_anon_3', 'type': 'inode__bindgen_ty_3'}, {'name': 'i_flctx', 'type': '*mut file_lock_context'}, {'name': 'i_data', 'type': 'address_space'}, {'name': '__bindgen_anon_4', 'type': 'inode__bindgen_ty_4'}, {'name': '__bindgen_anon_5', 'type': 'inode__bindgen_ty_5'}, {'name': 'i_fsnotify_mask', 'type': '__u32'}, {'name': 'i_fsnotify_marks', 'type': '*mut fsnotify_mark_connector'}, {'name': 'i_private', 'type': '*mut ffi::c_void'}]`

### Rust Evidence

- Graph edges: `50`

## W-000214 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: iommu_domain
- Explanation: iommu_domain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'type_', 'type': 'ffi::c_uint'}, {'name': 'cookie_type', 'type': 'iommu_domain_cookie_type'}, {'name': 'ops', 'type': '*const iommu_domain_ops'}, {'name': 'dirty_ops', 'type': '*const iommu_dirty_ops'}, {'name': 'owner', 'type': '*const iommu_ops'}, {'name': 'pgsize_bitmap', 'type': 'ffi::c_ulong'}, {'name': 'geometry', 'type': 'iommu_domain_geometry'}, {'name': '__bindgen_anon_1', 'type': 'iommu_domain__bindgen_ty_1'}]`
- New: `[{'name': 'type_', 'type': 'ffi::c_uint'}, {'name': 'cookie_type', 'type': 'iommu_domain_cookie_type'}, {'name': 'is_iommupt', 'type': 'bool_'}, {'name': 'ops', 'type': '*const iommu_domain_ops'}, {'name': 'dirty_ops', 'type': '*const iommu_dirty_ops'}, {'name': 'owner', 'type': '*const iommu_ops'}, {'name': 'pgsize_bitmap', 'type': 'ffi::c_ulong'}, {'name': 'geometry', 'type': 'iommu_domain_geometry'}, {'name': '__bindgen_anon_1', 'type': 'iommu_domain__bindgen_ty_1'}]`

### Rust Evidence

- Graph edges: `21`

## W-000220 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: module
- Explanation: module changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'state', 'type': 'module_state'}, {'name': 'list', 'type': 'list_head'}, {'name': 'name', 'type': '[ffi::c_char; 56usize]'}, {'name': 'mkobj', 'type': 'module_kobject'}, {'name': 'modinfo_attrs', 'type': '*mut module_attribute'}, {'name': 'version', 'type': '*const ffi::c_char'}, {'name': 'srcversion', 'type': '*const ffi::c_char'}, {'name': 'holders_dir', 'type': '*mut kobject'}, {'name': 'syms', 'type': '*mut kernel_symbol'}, {'name': 'crcs', 'type': '*const u32_'}, {'name': 'num_syms', 'type': 'ffi::c_uint'}, {'name': 'param_lock', 'type': 'mutex'}, {'name': 'kp', 'type': '*mut kernel_param'}, {'name': 'num_kp', 'type': 'ffi::c_uint'}, {'name': 'num_gpl_syms', 'type': 'ffi::c_uint'}, {'name': 'gpl_syms', 'type': '*const kernel_symbol'}, {'name': 'gpl_crcs', 'type': '*const u32_'}, {'name': 'using_gplonly_symbols', 'type': 'bool_'}, {'name': 'async_probe_requested', 'type': 'bool_'}, {'name': 'num_exentries', 'type': 'ffi::c_uint'}, {'name': 'extable', 'type': '*mut exception_table_entry'}, {'name': 'init', 'type': '::core::option::Option<unsafe extern "C" fn() -> ffi::c_int>'}, {'name': 'mem', 'type': '[module_memory; 7usize]'}, {'name': 'arch', 'type': 'mod_arch_specific'}, {'name': 'taints', 'type': 'ffi::c_ulong'}, {'name': 'num_bugs', 'type': 'ffi::c_uint'}, {'name': 'bug_list', 'type': 'list_head'}, {'name': 'bug_table', 'type': '*mut bug_entry'}, {'name': 'kallsyms', 'type': '*mut mod_kallsyms'}, {'name': 'core_kallsyms', 'type': 'mod_kallsyms'}, {'name': 'sect_attrs', 'type': '*mut module_sect_attrs'}, {'name': 'notes_attrs', 'type': '*mut module_notes_attrs'}, {'name': 'args', 'type': '*mut ffi::c_char'}, {'name': 'percpu', 'type': '*mut ffi::c_void'}, {'name': 'percpu_size', 'type': 'ffi::c_uint'}, {'name': 'noinstr_text_start', 'type': '*mut ffi::c_void'}, {'name': 'noinstr_text_size', 'type': 'ffi::c_uint'}, {'name': 'num_tracepoints', 'type': 'ffi::c_uint'}, {'name': 'tracepoints_ptrs', 'type': '*const ffi::c_int'}, {'name': 'num_srcu_structs', 'type': 'ffi::c_uint'}, {'name': 'srcu_struct_ptrs', 'type': '*mut *mut srcu_struct'}, {'name': 'jump_entries', 'type': '*mut jump_entry'}, {'name': 'num_jump_entries', 'type': 'ffi::c_uint'}, {'name': 'num_trace_bprintk_fmt', 'type': 'ffi::c_uint'}, {'name': 'trace_bprintk_fmt_start', 'type': '*mut *const ffi::c_char'}, {'name': 'trace_events', 'type': '*mut *mut trace_event_call'}, {'name': 'num_trace_events', 'type': 'ffi::c_uint'}, {'name': 'trace_evals', 'type': '*mut *mut trace_eval_map'}, {'name': 'num_trace_evals', 'type': 'ffi::c_uint'}, {'name': 'kprobes_text_start', 'type': '*mut ffi::c_void'}, {'name': 'kprobes_text_size', 'type': 'ffi::c_uint'}, {'name': 'kprobe_blacklist', 'type': '*mut ffi::c_ulong'}, {'name': 'num_kprobe_blacklist', 'type': 'ffi::c_uint'}, {'name': 'num_static_call_sites', 'type': 'ffi::c_int'}, {'name': 'static_call_sites', 'type': '*mut static_call_site'}, {'name': 'source_list', 'type': 'list_head'}, {'name': 'target_list', 'type': 'list_head'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'refcnt', 'type': 'atomic_t'}]`
- New: `[{'name': 'state', 'type': 'module_state'}, {'name': 'list', 'type': 'list_head'}, {'name': 'name', 'type': '[ffi::c_char; 56usize]'}, {'name': 'mkobj', 'type': 'module_kobject'}, {'name': 'modinfo_attrs', 'type': '*mut module_attribute'}, {'name': 'version', 'type': '*const ffi::c_char'}, {'name': 'srcversion', 'type': '*const ffi::c_char'}, {'name': 'imported_namespaces', 'type': '*const ffi::c_char'}, {'name': 'holders_dir', 'type': '*mut kobject'}, {'name': 'syms', 'type': '*mut kernel_symbol'}, {'name': 'crcs', 'type': '*const u32_'}, {'name': 'flagstab', 'type': '*const u8_'}, {'name': 'num_syms', 'type': 'ffi::c_uint'}, {'name': 'param_lock', 'type': 'mutex'}, {'name': 'kp', 'type': '*mut kernel_param'}, {'name': 'num_kp', 'type': 'ffi::c_uint'}, {'name': 'using_gplonly_symbols', 'type': 'bool_'}, {'name': 'async_probe_requested', 'type': 'bool_'}, {'name': 'num_exentries', 'type': 'ffi::c_uint'}, {'name': 'extable', 'type': '*mut exception_table_entry'}, {'name': 'init', 'type': '::core::option::Option<unsafe extern "C" fn() -> ffi::c_int>'}, {'name': '__bindgen_padding_0', 'type': 'u64'}, {'name': 'mem', 'type': '[module_memory; 7usize]'}, {'name': 'arch', 'type': 'mod_arch_specific'}, {'name': 'taints', 'type': 'ffi::c_ulong'}, {'name': 'num_bugs', 'type': 'ffi::c_uint'}, {'name': 'bug_list', 'type': 'list_head'}, {'name': 'bug_table', 'type': '*mut bug_entry'}, {'name': 'kallsyms', 'type': '*mut mod_kallsyms'}, {'name': 'core_kallsyms', 'type': 'mod_kallsyms'}, {'name': 'sect_attrs', 'type': '*mut module_sect_attrs'}, {'name': 'notes_attrs', 'type': '*mut module_notes_attrs'}, {'name': 'args', 'type': '*mut ffi::c_char'}, {'name': 'percpu', 'type': '*mut ffi::c_void'}, {'name': 'percpu_size', 'type': 'ffi::c_uint'}, {'name': 'noinstr_text_start', 'type': '*mut ffi::c_void'}, {'name': 'noinstr_text_size', 'type': 'ffi::c_uint'}, {'name': 'num_tracepoints', 'type': 'ffi::c_uint'}, {'name': 'tracepoints_ptrs', 'type': '*const ffi::c_int'}, {'name': 'num_srcu_structs', 'type': 'ffi::c_uint'}, {'name': 'srcu_struct_ptrs', 'type': '*mut *mut srcu_struct'}, {'name': 'jump_entries', 'type': '*mut jump_entry'}, {'name': 'num_jump_entries', 'type': 'ffi::c_uint'}, {'name': 'num_trace_bprintk_fmt', 'type': 'ffi::c_uint'}, {'name': 'trace_bprintk_fmt_start', 'type': '*mut *const ffi::c_char'}, {'name': 'trace_events', 'type': '*mut *mut trace_event_call'}, {'name': 'num_trace_events', 'type': 'ffi::c_uint'}, {'name': 'trace_evals', 'type': '*mut *mut trace_eval_map'}, {'name': 'num_trace_evals', 'type': 'ffi::c_uint'}, {'name': 'kprobes_text_start', 'type': '*mut ffi::c_void'}, {'name': 'kprobes_text_size', 'type': 'ffi::c_uint'}, {'name': 'kprobe_blacklist', 'type': '*mut ffi::c_ulong'}, {'name': 'num_kprobe_blacklist', 'type': 'ffi::c_uint'}, {'name': 'num_static_call_sites', 'type': 'ffi::c_int'}, {'name': 'static_call_sites', 'type': '*mut static_call_site'}, {'name': 'source_list', 'type': 'list_head'}, {'name': 'target_list', 'type': 'list_head'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'refcnt', 'type': 'atomic_t'}]`

### Rust Evidence

- Graph edges: `44`

## W-000221 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: mutex
- Explanation: mutex changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'owner', 'type': 'atomic_long_t'}, {'name': 'wait_lock', 'type': 'raw_spinlock_t'}, {'name': 'osq', 'type': 'optimistic_spin_queue'}, {'name': 'wait_list', 'type': 'list_head'}]`
- New: `[{'name': 'owner', 'type': 'atomic_long_t'}, {'name': 'wait_lock', 'type': 'raw_spinlock_t'}, {'name': 'osq', 'type': 'optimistic_spin_queue'}, {'name': 'first_waiter', 'type': '*mut mutex_waiter'}]`

### Rust Evidence

- Graph edges: `37`

## W-000225 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: pci_dev
- Explanation: pci_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'rebar_cap', 'type': 'u16_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'msi_addr_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 11usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pri_cap', 'type': 'u16_'}, {'name': 'pri_reqs_alloc', 'type': 'u32_'}, {'name': '_bitfield_align_5', 'type': '[u8; 0]'}, {'name': '_bitfield_5', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'acs_capabilities', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`
- New: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'rebar_cap', 'type': 'u16_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'msi_addr_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 11usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pri_cap', 'type': 'u16_'}, {'name': 'pri_reqs_alloc', 'type': 'u32_'}, {'name': '_bitfield_align_5', 'type': '[u8; 0]'}, {'name': '_bitfield_5', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'acs_capabilities', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`

### Rust Evidence

- Graph edges: `50`

## W-000229 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: phy_device
- Explanation: phy_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mdio', 'type': 'mdio_device'}, {'name': 'drv', 'type': '*const phy_driver'}, {'name': 'devlink', 'type': '*mut device_link'}, {'name': 'phyindex', 'type': 'u32_'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'c45_ids', 'type': 'phy_c45_device_ids'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'rate_matching', 'type': 'ffi::c_int'}, {'name': 'state', 'type': 'phy_state'}, {'name': 'dev_flags', 'type': 'u32_'}, {'name': 'interface', 'type': 'phy_interface_t'}, {'name': 'possible_interfaces', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'speed', 'type': 'ffi::c_int'}, {'name': 'duplex', 'type': 'ffi::c_int'}, {'name': 'port', 'type': 'ffi::c_int'}, {'name': 'master_slave_get', 'type': 'u8_'}, {'name': 'master_slave_set', 'type': 'u8_'}, {'name': 'master_slave_state', 'type': 'u8_'}, {'name': 'supported', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'advertising', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'lp_advertising', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'adv_old', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'supported_eee', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'advertising_eee', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'eee_disabled_modes', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'enable_tx_lpi', 'type': 'bool_'}, {'name': 'eee_active', 'type': 'bool_'}, {'name': 'eee_cfg', 'type': 'eee_config'}, {'name': 'host_interfaces', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'leds', 'type': 'list_head'}, {'name': 'irq', 'type': 'ffi::c_int'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'ehdr', 'type': '*mut ffi::c_void'}, {'name': 'nest', 'type': '*mut nlattr'}, {'name': 'state_queue', 'type': 'delayed_work'}, {'name': 'lock', 'type': 'mutex'}, {'name': 'sfp_bus_attached', 'type': 'bool_'}, {'name': 'sfp_bus', 'type': '*mut sfp_bus'}, {'name': 'phylink', 'type': '*mut phylink'}, {'name': 'attached_dev', 'type': '*mut net_device'}, {'name': 'mii_ts', 'type': '*mut mii_timestamper'}, {'name': 'psec', 'type': '*mut pse_control'}, {'name': 'ports', 'type': 'list_head'}, {'name': 'n_ports', 'type': 'ffi::c_int'}, {'name': 'max_n_ports', 'type': 'ffi::c_int'}, {'name': 'mdix', 'type': 'u8_'}, {'name': 'mdix_ctrl', 'type': 'u8_'}, {'name': 'pma_extable', 'type': 'ffi::c_int'}, {'name': 'link_down_events', 'type': 'ffi::c_uint'}, {'name': 'adjust_link', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut net_device)>'}, {'name': 'oatc14_sqi_capability', 'type': 'phy_oatc14_sqi_capability'}]`
- New: `[{'name': 'mdio', 'type': 'mdio_device'}, {'name': 'drv', 'type': '*const phy_driver'}, {'name': 'devlink', 'type': '*mut device_link'}, {'name': 'phyindex', 'type': 'u32_'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'c45_ids', 'type': 'phy_c45_device_ids'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'rate_matching', 'type': 'ffi::c_int'}, {'name': 'state', 'type': 'phy_state'}, {'name': 'dev_flags', 'type': 'u32_'}, {'name': 'interface', 'type': 'phy_interface_t'}, {'name': 'possible_interfaces', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'speed', 'type': 'ffi::c_int'}, {'name': 'duplex', 'type': 'ffi::c_int'}, {'name': 'port', 'type': 'ffi::c_int'}, {'name': 'master_slave_get', 'type': 'u8_'}, {'name': 'master_slave_set', 'type': 'u8_'}, {'name': 'master_slave_state', 'type': 'u8_'}, {'name': 'supported', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'advertising', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'lp_advertising', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'adv_old', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'supported_eee', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'advertising_eee', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'eee_disabled_modes', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'enable_tx_lpi', 'type': 'bool_'}, {'name': 'eee_active', 'type': 'bool_'}, {'name': 'autonomous_eee_disabled', 'type': 'bool_'}, {'name': 'eee_cfg', 'type': 'eee_config'}, {'name': 'host_interfaces', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'leds', 'type': 'list_head'}, {'name': 'irq', 'type': 'ffi::c_int'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'shared', 'type': '*mut phy_package_shared'}, {'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'ehdr', 'type': '*mut ffi::c_void'}, {'name': 'nest', 'type': '*mut nlattr'}, {'name': 'state_queue', 'type': 'delayed_work'}, {'name': 'lock', 'type': 'mutex'}, {'name': 'sfp_bus_attached', 'type': 'bool_'}, {'name': 'sfp_bus', 'type': '*mut sfp_bus'}, {'name': 'phylink', 'type': '*mut phylink'}, {'name': 'attached_dev', 'type': '*mut net_device'}, {'name': 'mii_ts', 'type': '*mut mii_timestamper'}, {'name': 'psec', 'type': '*mut pse_control'}, {'name': 'ports', 'type': 'list_head'}, {'name': 'n_ports', 'type': 'ffi::c_int'}, {'name': 'max_n_ports', 'type': 'ffi::c_int'}, {'name': 'mdix', 'type': 'u8_'}, {'name': 'mdix_ctrl', 'type': 'u8_'}, {'name': 'pma_extable', 'type': 'ffi::c_int'}, {'name': 'link_down_events', 'type': 'ffi::c_uint'}, {'name': 'adjust_link', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut net_device)>'}, {'name': 'oatc14_sqi_capability', 'type': 'phy_oatc14_sqi_capability'}]`

### Rust Evidence

- Graph edges: `50`

## W-000250 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: zone
- Explanation: zone changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_watermark', 'type': '[ffi::c_ulong; 4usize]'}, {'name': 'watermark_boost', 'type': 'ffi::c_ulong'}, {'name': 'nr_reserved_highatomic', 'type': 'ffi::c_ulong'}, {'name': 'nr_free_highatomic', 'type': 'ffi::c_ulong'}, {'name': 'lowmem_reserve', 'type': '[ffi::c_long; 4usize]'}, {'name': 'node', 'type': 'ffi::c_int'}, {'name': 'zone_pgdat', 'type': '*mut pglist_data'}, {'name': 'per_cpu_pageset', 'type': '*mut per_cpu_pages'}, {'name': 'per_cpu_zonestats', 'type': '*mut per_cpu_zonestat'}, {'name': 'pageset_high_min', 'type': 'ffi::c_int'}, {'name': 'pageset_high_max', 'type': 'ffi::c_int'}, {'name': 'pageset_batch', 'type': 'ffi::c_int'}, {'name': 'zone_start_pfn', 'type': 'ffi::c_ulong'}, {'name': 'managed_pages', 'type': 'atomic_long_t'}, {'name': 'spanned_pages', 'type': 'ffi::c_ulong'}, {'name': 'present_pages', 'type': 'ffi::c_ulong'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'initialized', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': 'u64'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': 'free_area', 'type': '[free_area; 11usize]'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'trylock_free_pages', 'type': 'llist_head'}, {'name': '__bindgen_padding_1', 'type': '[u64; 2usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'percpu_drift_mark', 'type': 'ffi::c_ulong'}, {'name': 'compact_cached_free_pfn', 'type': 'ffi::c_ulong'}, {'name': 'compact_cached_migrate_pfn', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'compact_init_migrate_pfn', 'type': 'ffi::c_ulong'}, {'name': 'compact_init_free_pfn', 'type': 'ffi::c_ulong'}, {'name': 'compact_considered', 'type': 'ffi::c_uint'}, {'name': 'compact_defer_shift', 'type': 'ffi::c_uint'}, {'name': 'compact_order_failed', 'type': 'ffi::c_int'}, {'name': 'compact_blockskip_flush', 'type': 'bool_'}, {'name': 'contiguous', 'type': 'bool_'}, {'name': '__bindgen_padding_2', 'type': '[u64; 0usize]'}, {'name': '_pad3_', 'type': 'cacheline_padding'}, {'name': 'vm_stat', 'type': '[atomic_long_t; 10usize]'}, {'name': 'vm_numa_event', 'type': '[atomic_long_t; 6usize]'}]`
- New: `[{'name': '_watermark', 'type': '[ffi::c_ulong; 4usize]'}, {'name': 'watermark_boost', 'type': 'ffi::c_ulong'}, {'name': 'nr_reserved_highatomic', 'type': 'ffi::c_ulong'}, {'name': 'nr_free_highatomic', 'type': 'ffi::c_ulong'}, {'name': 'lowmem_reserve', 'type': '[ffi::c_long; 4usize]'}, {'name': 'node', 'type': 'ffi::c_int'}, {'name': 'zone_pgdat', 'type': '*mut pglist_data'}, {'name': 'per_cpu_pageset', 'type': '*mut per_cpu_pages'}, {'name': 'per_cpu_zonestats', 'type': '*mut per_cpu_zonestat'}, {'name': 'pageset_high_min', 'type': 'ffi::c_int'}, {'name': 'pageset_high_max', 'type': 'ffi::c_int'}, {'name': 'pageset_batch', 'type': 'ffi::c_int'}, {'name': 'zone_start_pfn', 'type': 'ffi::c_ulong'}, {'name': 'managed_pages', 'type': 'atomic_long_t'}, {'name': 'spanned_pages', 'type': 'ffi::c_ulong'}, {'name': 'present_pages', 'type': 'ffi::c_ulong'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'initialized', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': 'u64'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': 'free_area', 'type': '[free_area; 11usize]'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'trylock_free_pages', 'type': 'llist_head'}, {'name': '__bindgen_padding_1', 'type': '[u64; 2usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'percpu_drift_mark', 'type': 'ffi::c_ulong'}, {'name': 'compact_cached_free_pfn', 'type': 'ffi::c_ulong'}, {'name': 'compact_cached_migrate_pfn', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'compact_init_migrate_pfn', 'type': 'ffi::c_ulong'}, {'name': 'compact_init_free_pfn', 'type': 'ffi::c_ulong'}, {'name': 'compact_considered', 'type': 'ffi::c_uint'}, {'name': 'compact_defer_shift', 'type': 'ffi::c_uint'}, {'name': 'compact_order_failed', 'type': 'ffi::c_int'}, {'name': 'compact_blockskip_flush', 'type': 'bool_'}, {'name': 'contiguous', 'type': 'bool_'}, {'name': '__bindgen_padding_2', 'type': '[u64; 0usize]'}, {'name': '_pad3_', 'type': 'cacheline_padding'}, {'name': 'vm_stat', 'type': '[atomic_long_t; 10usize]'}, {'name': 'vm_numa_event', 'type': '[atomic_long_t; 6usize]'}, {'name': 'vmemmap_tails', 'type': '[*mut page; 16usize]'}]`

### Rust Evidence

- Graph edges: `38`

## W-000074 SignatureDrift

- Risk: High
- Score: 12.4
- Symbol: drm_gem_shmem_init
- Explanation: drm_gem_shmem_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `9`

## W-000192 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: zap_vma_range
- Explanation: zap_vma_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000061 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: devres_node_remove
- Explanation: devres_node_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000077 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: drm_gem_shmem_object_free
- Explanation: drm_gem_shmem_object_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000055 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: dev_name
- Explanation: dev_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000059 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: devres_node_add
- Explanation: devres_node_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000060 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: devres_node_init
- Explanation: devres_node_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000062 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: devres_set_node_dbginfo
- Explanation: devres_set_node_dbginfo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000109 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: gpu_buddy_block_order
- Explanation: gpu_buddy_block_order changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000693 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: rust_helper_clk_get
- Explanation: rust_helper_clk_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct device *dev', 'const char *id'], 'return_type': 'struct clk *'}`
- New: `{'params': ['struct device *dev', 'const char *id'], 'return_type': '__rust_helper struct clk *'}`

### Rust Evidence

- Graph edges: `1`

## W-000698 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: rust_helper_clk_put
- Explanation: rust_helper_clk_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct clk *clk'], 'return_type': 'void'}`
- New: `{'params': ['struct clk *clk'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `1`

## W-000067 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: dma_resv_lock
- Explanation: dma_resv_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000092 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: drm_gem_shmem_release
- Explanation: drm_gem_shmem_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000107 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: gpu_buddy_alloc_blocks
- Explanation: gpu_buddy_alloc_blocks changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000108 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: gpu_buddy_block_offset
- Explanation: gpu_buddy_block_offset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000112 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: gpu_buddy_fini
- Explanation: gpu_buddy_fini changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000114 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: gpu_buddy_free_list
- Explanation: gpu_buddy_free_list changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000115 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: gpu_buddy_init
- Explanation: gpu_buddy_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000243 FieldDrift

- Risk: High
- Score: 11.6
- Symbol: task_struct
- Explanation: task_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'ffi::c_uint'}, {'name': 'saved_state', 'type': 'ffi::c_uint'}, {'name': 'stack', 'type': '*mut ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'ptrace', 'type': 'ffi::c_uint'}, {'name': 'on_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_cpu', 'type': 'ffi::c_int'}, {'name': 'on_rq', 'type': 'ffi::c_int'}, {'name': 'prio', 'type': 'ffi::c_int'}, {'name': 'static_prio', 'type': 'ffi::c_int'}, {'name': 'normal_prio', 'type': 'ffi::c_int'}, {'name': 'rt_priority', 'type': 'ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'dl_server', 'type': '*mut sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': '__bindgen_padding_1', 'type': 'u64'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'ffi::c_uint'}, {'name': 'policy', 'type': 'ffi::c_uint'}, {'name': 'max_allowed_capacity', 'type': 'ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut ffi::c_void'}, {'name': 'migration_disabled', 'type': 'ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'rcu_tasks_exit_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_exit_list', 'type': 'list_head'}, {'name': 'trc_reader_nesting', 'type': 'ffi::c_int'}, {'name': 'trc_reader_scp', 'type': '*mut srcu_ctr'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'exit_state', 'type': 'ffi::c_int'}, {'name': 'exit_code', 'type': 'ffi::c_int'}, {'name': 'exit_signal', 'type': 'ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'ffi::c_int'}, {'name': 'jobctl', 'type': 'ffi::c_ulong'}, {'name': 'personality', 'type': 'ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'worker_private', 'type': '*mut ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'io_uring_restrict', 'type': '*mut io_restriction'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'blocked_on', 'type': '*mut mutex'}, {'name': 'journal_info', 'type': '*mut ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'ffi::c_uint'}, {'name': 'perf_recursion', 'type': '[u8_; 4usize]'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'perf_ctx_data', 'type': '*mut perf_ctx_data'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'ffi::c_short'}, {'name': 'il_weight', 'type': 'u8_'}, {'name': 'pref_node_fork', 'type': 'ffi::c_short'}, {'name': 'rseq', 'type': 'rseq_data'}, {'name': 'mm_cid', 'type': 'sched_mm_cid'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'bpf_net_context', 'type': '*mut bpf_net_context'}, {'name': 'mce_vaddr', 'type': '*mut ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': 'unwind_info', 'type': 'unwind_task_info'}, {'name': 'thread', 'type': 'thread_struct'}]`
- New: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'ffi::c_uint'}, {'name': 'saved_state', 'type': 'ffi::c_uint'}, {'name': 'stack', 'type': '*mut ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'ptrace', 'type': 'ffi::c_uint'}, {'name': 'on_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_cpu', 'type': 'ffi::c_int'}, {'name': 'on_rq', 'type': 'ffi::c_int'}, {'name': 'prio', 'type': 'ffi::c_int'}, {'name': 'static_prio', 'type': 'ffi::c_int'}, {'name': 'normal_prio', 'type': 'ffi::c_int'}, {'name': 'rt_priority', 'type': 'ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'dl_server', 'type': '*mut sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': '__bindgen_padding_1', 'type': '[u64; 5usize]'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'ffi::c_uint'}, {'name': 'policy', 'type': 'ffi::c_uint'}, {'name': 'max_allowed_capacity', 'type': 'ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut ffi::c_void'}, {'name': 'migration_disabled', 'type': 'ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'rcu_tasks_exit_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_exit_list', 'type': 'list_head'}, {'name': 'trc_reader_nesting', 'type': 'ffi::c_int'}, {'name': 'trc_reader_scp', 'type': '*mut srcu_ctr'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'exit_state', 'type': 'ffi::c_int'}, {'name': 'exit_code', 'type': 'ffi::c_int'}, {'name': 'exit_signal', 'type': 'ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'ffi::c_int'}, {'name': 'jobctl', 'type': 'ffi::c_ulong'}, {'name': 'personality', 'type': 'ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'worker_private', 'type': '*mut ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'io_uring_restrict', 'type': '*mut io_restriction'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'blocked_on', 'type': '*mut mutex'}, {'name': 'blocked_lock', 'type': 'raw_spinlock_t'}, {'name': 'journal_info', 'type': '*mut ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'ffi::c_uint'}, {'name': 'perf_recursion', 'type': '[u8_; 4usize]'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'perf_ctx_data', 'type': '*mut perf_ctx_data'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'ffi::c_short'}, {'name': 'il_weight', 'type': 'u8_'}, {'name': 'pref_node_fork', 'type': 'ffi::c_short'}, {'name': 'rseq', 'type': 'rseq_data'}, {'name': 'mm_cid', 'type': 'sched_mm_cid'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'bpf_net_context', 'type': '*mut bpf_net_context'}, {'name': 'mce_vaddr', 'type': '*mut ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': 'unwind_info', 'type': 'unwind_task_info'}, {'name': 'thread', 'type': 'thread_struct'}]`

### Rust Evidence

- Graph edges: `15`

## W-000027 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic_ptr_try_cmpxchg
- Explanation: atomic_ptr_try_cmpxchg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000031 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic_ptr_xchg
- Explanation: atomic_ptr_xchg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000154 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: phy_attach
- Explanation: phy_attach changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `4`

## W-000629 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: default_llseek
- Explanation: default_llseek changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct file *file', 'loff_t offset', 'int whence'], 'return_type': 'extern loff_t'}`
- New: `{'params': ['struct file *file', 'loff_t offset', 'int whence'], 'return_type': 'loff_t'}`

### Rust Evidence

- Graph edges: `4`

## W-000682 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: memcpy
- Explanation: memcpy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['dst', 'src', 'len'], 'return_type': 'else'}`
- New: `{'params': ['dst', 'src->vaddr + src_offset', 'len'], 'return_type': 'else'}`

### Rust Evidence

- Graph edges: `4`

## W-000081 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: drm_gem_shmem_object_print_info
- Explanation: drm_gem_shmem_object_print_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000124 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: ilookup
- Explanation: ilookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'sb', 'type': '*mut super_block'}, {'name': 'ino', 'type': 'ffi::c_ulong'}], 'return_type': '*mut inode'}`
- New: `{'params': [{'name': 'sb', 'type': '*mut super_block'}, {'name': 'ino', 'type': 'u64_'}], 'return_type': '*mut inode'}`

### Rust Evidence

- Graph edges: `3`

## W-000178 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: type_
- Explanation: type_ changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u16_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(8usize, 5u8) as u16) } } #[inline] pub fn set_type(&mut self, val: u16_) { unsafe { let val: u16 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u64_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(48usize, 4u8) as u64) } } #[inline] pub fn set_type(&mut self, val: u64_) { unsafe { let val: u64 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `3`

## W-000669 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: ilookup
- Explanation: ilookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct super_block *sb', 'unsigned long ino'], 'return_type': 'extern struct inode *'}`
- New: `{'params': ['struct super_block *sb', 'u64 ino'], 'return_type': 'struct inode *'}`

### Rust Evidence

- Graph edges: `3`

## W-000023 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: atomic_ptr_read
- Explanation: atomic_ptr_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000025 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: atomic_ptr_set
- Explanation: atomic_ptr_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000036 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: backing_file_security
- Explanation: backing_file_security changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000070 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: drm_gem_shmem_dumb_create
- Explanation: drm_gem_shmem_dumb_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000078 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: drm_gem_shmem_object_get_sg_table
- Explanation: drm_gem_shmem_object_get_sg_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000079 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: drm_gem_shmem_object_mmap
- Explanation: drm_gem_shmem_object_mmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000080 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: drm_gem_shmem_object_pin
- Explanation: drm_gem_shmem_object_pin changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000082 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: drm_gem_shmem_object_unpin
- Explanation: drm_gem_shmem_object_unpin changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000083 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: drm_gem_shmem_object_vmap
- Explanation: drm_gem_shmem_object_vmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000084 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: drm_gem_shmem_object_vunmap
- Explanation: drm_gem_shmem_object_vunmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000085 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: drm_gem_shmem_pin
- Explanation: drm_gem_shmem_pin changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000088 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: drm_gem_shmem_prime_import_sg_table
- Explanation: drm_gem_shmem_prime_import_sg_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000093 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: drm_gem_shmem_unpin
- Explanation: drm_gem_shmem_unpin changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000120 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: iget5_locked
- Explanation: iget5_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut super_block'}, {'name': 'arg2', 'type': 'ffi::c_ulong'}, {'name': 'test', 'type': '::core::option::Option< unsafe extern "C" fn(arg1: *mut inode, arg2: *mut ffi::c_void'}], 'return_type': 'ffi::c_int, >, set: ::core::option::Option< unsafe extern "C" fn(arg1: *mut inode, arg2: *mut ffi::c_void) -> ffi::c_int, >, arg3: *mut ffi::c_void, ) -> *mut inode'}`
- New: `{'params': [{'name': 'sb', 'type': '*mut super_block'}, {'name': 'hashval', 'type': 'u64_'}, {'name': 'test', 'type': '::core::option::Option< unsafe extern "C" fn(arg1: *mut inode, arg2: *mut ffi::c_void'}], 'return_type': 'ffi::c_int, >, set: ::core::option::Option< unsafe extern "C" fn(arg1: *mut inode, arg2: *mut ffi::c_void) -> ffi::c_int, >, data: *mut ffi::c_void, ) -> *mut inode'}`

### Rust Evidence

- Graph edges: `2`

## W-000125 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: ilookup5
- Explanation: ilookup5 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'sb', 'type': '*mut super_block'}, {'name': 'hashval', 'type': 'ffi::c_ulong'}, {'name': 'test', 'type': '::core::option::Option< unsafe extern "C" fn(arg1: *mut inode, arg2: *mut ffi::c_void'}], 'return_type': 'ffi::c_int, >, data: *mut ffi::c_void, ) -> *mut inode'}`
- New: `{'params': [{'name': 'sb', 'type': '*mut super_block'}, {'name': 'hashval', 'type': 'u64_'}, {'name': 'test', 'type': '::core::option::Option< unsafe extern "C" fn(arg1: *mut inode, arg2: *mut ffi::c_void'}], 'return_type': 'ffi::c_int, >, data: *mut ffi::c_void, ) -> *mut inode'}`

### Rust Evidence

- Graph edges: `2`

## W-000131 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: insert_inode_locked
- Explanation: insert_inode_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut inode'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'inode', 'type': '*mut inode'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `2`

## W-000165 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: simple_fsync
- Explanation: simple_fsync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000665 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: iget5_locked
- Explanation: iget5_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct super_block *', 'unsigned long', 'int (*test)(struct inode *, void *)', 'int (*set)(struct inode *, void *)', 'void *'], 'return_type': 'struct inode *'}`
- New: `{'params': ['struct super_block *sb', 'u64 hashval', 'int (*test)(struct inode *, void *)', 'int (*set)(struct inode *, void *)', 'void *data'], 'return_type': 'struct inode *'}`

### Rust Evidence

- Graph edges: `2`

## W-000670 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: ilookup5
- Explanation: ilookup5 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct super_block *sb', 'unsigned long hashval', 'int (*test)(struct inode *, void *)', 'void *data'], 'return_type': 'extern struct inode *'}`
- New: `{'params': ['struct super_block *sb', 'u64 hashval', 'int (*test)(struct inode *, void *)', 'void *data'], 'return_type': 'struct inode *'}`

### Rust Evidence

- Graph edges: `2`

## W-000678 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: insert_inode_locked
- Explanation: insert_inode_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct inode *'], 'return_type': 'extern int'}`
- New: `{'params': ['struct inode *inode'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `2`

## W-000683 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: memset
- Explanation: memset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['dst', '0xff', 'len'], 'return_type': 'else'}`
- New: `{'params': ['dst->vaddr + offset', 'value', 'len'], 'return_type': 'else'}`

### Rust Evidence

- Graph edges: `2`

## W-000002 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __bitmap_weighted_xor
- Explanation: __bitmap_weighted_xor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000003 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __compat_vma_mmap
- Explanation: __compat_vma_mmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'f_op', 'type': '*const file_operations'}, {'name': 'file', 'type': '*mut file'}, {'name': 'vma', 'type': '*mut vm_area_struct'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'desc', 'type': '*mut vm_area_desc'}, {'name': 'vma', 'type': '*mut vm_area_struct'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000007 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __folio_batch_release
- Explanation: __folio_batch_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'pvec', 'type': '*mut folio_batch'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'fbatch', 'type': '*mut folio_batch'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000009 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __hrtimer_rearm_deferred
- Explanation: __hrtimer_rearm_deferred changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000010 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __insert_inode_hash
- Explanation: __insert_inode_hash changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut inode'}, {'name': 'hashval', 'type': 'ffi::c_ulong'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'inode', 'type': '*mut inode'}, {'name': 'hashval', 'type': 'u64_'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000011 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mmu_notifier_clear_flush_young
- Explanation: __mmu_notifier_clear_flush_young changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'start', 'type': 'ffi::c_ulong'}, {'name': 'end', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'start', 'type': 'ffi::c_ulong'}, {'name': 'end', 'type': 'ffi::c_ulong'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000012 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mmu_notifier_clear_young
- Explanation: __mmu_notifier_clear_young changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'start', 'type': 'ffi::c_ulong'}, {'name': 'end', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'start', 'type': 'ffi::c_ulong'}, {'name': 'end', 'type': 'ffi::c_ulong'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000013 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mmu_notifier_test_young
- Explanation: __mmu_notifier_test_young changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'address', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'address', 'type': 'ffi::c_ulong'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000014 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __rb_erase_color
- Explanation: __rb_erase_color changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000015 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __rb_insert_augmented
- Explanation: __rb_insert_augmented changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000016 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __remove_inode_hash
- Explanation: __remove_inode_hash changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut inode'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'inode', 'type': '*mut inode'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000017 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_get_cpu_uid
- Explanation: acpi_get_cpu_uid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000019 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_notifier_call_chain
- Explanation: acpi_notifier_call_chain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut acpi_device'}, {'name': 'arg2', 'type': 'u32_'}, {'name': 'arg3', 'type': 'u32_'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'device_class', 'type': '*const ffi::c_char'}, {'name': 'bus_id', 'type': '*const ffi::c_char'}, {'name': 'type_', 'type': 'u32_'}, {'name': 'data', 'type': 'u32_'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000022 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_setup_zero_pages
- Explanation: arch_setup_zero_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000024 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_ptr_read_acquire
- Explanation: atomic_ptr_read_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000026 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_ptr_set_release
- Explanation: atomic_ptr_set_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000028 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_ptr_try_cmpxchg_acquire
- Explanation: atomic_ptr_try_cmpxchg_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000029 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_ptr_try_cmpxchg_relaxed
- Explanation: atomic_ptr_try_cmpxchg_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000030 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_ptr_try_cmpxchg_release
- Explanation: atomic_ptr_try_cmpxchg_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000032 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_ptr_xchg_acquire
- Explanation: atomic_ptr_xchg_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000033 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_ptr_xchg_relaxed
- Explanation: atomic_ptr_xchg_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000034 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_ptr_xchg_release
- Explanation: atomic_ptr_xchg_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000035 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: autoreap
- Explanation: autoreap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000037 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: backing_file_set_security
- Explanation: backing_file_set_security changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000038 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_alloc_bioset
- Explanation: bio_alloc_bioset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'bdev', 'type': '*mut block_device'}, {'name': 'nr_vecs', 'type': 'ffi::c_ushort'}, {'name': 'opf', 'type': 'blk_opf_t'}, {'name': 'gfp_mask', 'type': 'gfp_t'}, {'name': 'bs', 'type': '*mut bio_set'}], 'return_type': '*mut bio'}`
- New: `{'params': [{'name': 'bdev', 'type': '*mut block_device'}, {'name': 'nr_vecs', 'type': 'ffi::c_ushort'}, {'name': 'opf', 'type': 'blk_opf_t'}, {'name': 'gfp', 'type': 'gfp_t'}, {'name': 'bs', 'type': '*mut bio_set'}], 'return_type': '*mut bio'}`

### Rust Evidence

- Graph edges: `1`

## W-000039 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_await
- Explanation: bio_await changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000040 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_iov_iter_bounce
- Explanation: bio_iov_iter_bounce changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'bio', 'type': '*mut bio'}, {'name': 'iter', 'type': '*mut iov_iter'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'bio', 'type': '*mut bio'}, {'name': 'iter', 'type': '*mut iov_iter'}, {'name': 'maxlen', 'type': 'usize'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000041 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_find_linfo
- Explanation: bpf_find_linfo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000042 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_get_linfo_file_line
- Explanation: bpf_get_linfo_file_line changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000043 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: call_depth_return_thunk
- Explanation: call_depth_return_thunk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000044 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: callthunks_patch_builtin_calls
- Explanation: callthunks_patch_builtin_calls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000045 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: callthunks_patch_module_calls
- Explanation: callthunks_patch_module_calls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000046 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: callthunks_translate_call_dest
- Explanation: callthunks_translate_call_dest changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000047 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_on_dfl
- Explanation: cgroup_on_dfl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000048 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: compat_set_desc_from_vma
- Explanation: compat_set_desc_from_vma changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000049 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_to_nontemporal
- Explanation: copy_to_nontemporal changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000050 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_user_flushcache
- Explanation: copy_user_flushcache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000051 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_driver_adjust_perf
- Explanation: cpufreq_driver_adjust_perf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'cpu', 'type': 'ffi::c_uint'}, {'name': 'min_perf', 'type': 'ffi::c_ulong'}, {'name': 'target_perf', 'type': 'ffi::c_ulong'}, {'name': 'capacity', 'type': 'ffi::c_ulong'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'policy', 'type': '*mut cpufreq_policy'}, {'name': 'min_perf', 'type': 'ffi::c_ulong'}, {'name': 'target_perf', 'type': 'ffi::c_ulong'}, {'name': 'capacity', 'type': 'ffi::c_ulong'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000052 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_mark_tmpfile_name
- Explanation: d_mark_tmpfile_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000054 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_is_auxiliary
- Explanation: dev_is_auxiliary changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000056 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_add_groups
- Explanation: device_add_groups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'dev', 'type': '*mut device'}, {'name': 'groups', 'type': '*mut *const attribute_group'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'dev', 'type': '*mut device'}, {'name': 'groups', 'type': '*const *const attribute_group'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000057 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_remove_groups
- Explanation: device_remove_groups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'dev', 'type': '*mut device'}, {'name': 'groups', 'type': '*mut *const attribute_group'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'dev', 'type': '*mut device'}, {'name': 'groups', 'type': '*const *const attribute_group'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000058 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_alloc_workqueue
- Explanation: devm_alloc_workqueue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000063 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: discard_new_inode
- Explanation: discard_new_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut inode'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'inode', 'type': '*mut inode'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000064 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_buf_attach_revocable
- Explanation: dma_buf_attach_revocable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000065 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_buf_invalidate_mappings
- Explanation: dma_buf_invalidate_mappings changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000068 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_resv_unlock
- Explanation: dma_resv_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000069 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_shmem_create
- Explanation: drm_gem_shmem_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000071 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_shmem_free
- Explanation: drm_gem_shmem_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000072 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_shmem_get_pages_sgt
- Explanation: drm_gem_shmem_get_pages_sgt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000073 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_shmem_get_sg_table
- Explanation: drm_gem_shmem_get_sg_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000075 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_shmem_madvise_locked
- Explanation: drm_gem_shmem_madvise_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000076 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_shmem_mmap
- Explanation: drm_gem_shmem_mmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000086 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_shmem_pin_locked
- Explanation: drm_gem_shmem_pin_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000087 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_shmem_prime_import_no_map
- Explanation: drm_gem_shmem_prime_import_no_map changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000089 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_shmem_print_info
- Explanation: drm_gem_shmem_print_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000090 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_shmem_purge_locked
- Explanation: drm_gem_shmem_purge_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000091 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_shmem_put_pages_locked
- Explanation: drm_gem_shmem_put_pages_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000094 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_shmem_unpin_locked
- Explanation: drm_gem_shmem_unpin_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000095 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_shmem_vmap_locked
- Explanation: drm_gem_shmem_vmap_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000096 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_shmem_vunmap_locked
- Explanation: drm_gem_shmem_vunmap_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000097 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: enter_lazy_tlb
- Explanation: enter_lazy_tlb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000098 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_rxfh_ctxs_can_resize
- Explanation: ethtool_rxfh_ctxs_can_resize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000099 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_rxfh_ctxs_resize
- Explanation: ethtool_rxfh_ctxs_resize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000100 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_rxfh_indir_can_resize
- Explanation: ethtool_rxfh_indir_can_resize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000101 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_rxfh_indir_lost
- Explanation: ethtool_rxfh_indir_lost changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000102 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_rxfh_indir_resize
- Explanation: ethtool_rxfh_indir_resize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000103 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: find_inode_by_ino_rcu
- Explanation: find_inode_by_ino_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut super_block'}, {'name': 'arg2', 'type': 'ffi::c_ulong'}], 'return_type': '*mut inode'}`
- New: `{'params': [{'name': 'sb', 'type': '*mut super_block'}, {'name': 'ino', 'type': 'u64_'}], 'return_type': '*mut inode'}`

### Rust Evidence

- Graph edges: `1`

## W-000104 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: find_inode_nowait
- Explanation: find_inode_nowait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut super_block'}, {'name': 'arg2', 'type': 'ffi::c_ulong'}, {'name': 'match_', 'type': '::core::option::Option< unsafe extern "C" fn( arg1: *mut inode, arg2: ffi::c_ulong, arg3: *mut ffi::c_void,'}], 'return_type': 'ffi::c_int, >, data: *mut ffi::c_void, ) -> *mut inode'}`
- New: `{'params': [{'name': 'sb', 'type': '*mut super_block'}, {'name': 'hashval', 'type': 'u64_'}, {'name': 'match_', 'type': '::core::option::Option< unsafe extern "C" fn( arg1: *mut inode, arg2: u64_, arg3: *mut ffi::c_void,'}], 'return_type': 'ffi::c_int, >, data: *mut ffi::c_void, ) -> *mut inode'}`

### Rust Evidence

- Graph edges: `1`

## W-000105 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: find_inode_rcu
- Explanation: find_inode_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut super_block'}, {'name': 'arg2', 'type': 'ffi::c_ulong'}, {'name': 'arg3', 'type': '::core::option::Option< unsafe extern "C" fn(arg1: *mut inode, arg2: *mut ffi::c_void'}], 'return_type': 'ffi::c_int, >, arg4: *mut ffi::c_void, ) -> *mut inode'}`
- New: `{'params': [{'name': 'sb', 'type': '*mut super_block'}, {'name': 'hashval', 'type': 'u64_'}, {'name': 'test', 'type': '::core::option::Option< unsafe extern "C" fn(arg1: *mut inode, arg2: *mut ffi::c_void'}], 'return_type': 'ffi::c_int, >, data: *mut ffi::c_void, ) -> *mut inode'}`

### Rust Evidence

- Graph edges: `1`

## W-000110 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpu_buddy_block_print
- Explanation: gpu_buddy_block_print changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000111 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpu_buddy_block_trim
- Explanation: gpu_buddy_block_trim changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000113 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpu_buddy_free_block
- Explanation: gpu_buddy_free_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000116 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpu_buddy_print
- Explanation: gpu_buddy_print changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000117 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpu_buddy_reset_clear
- Explanation: gpu_buddy_reset_clear changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000121 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iget5_locked_rcu
- Explanation: iget5_locked_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut super_block'}, {'name': 'arg2', 'type': 'ffi::c_ulong'}, {'name': 'test', 'type': '::core::option::Option< unsafe extern "C" fn(arg1: *mut inode, arg2: *mut ffi::c_void'}], 'return_type': 'ffi::c_int, >, set: ::core::option::Option< unsafe extern "C" fn(arg1: *mut inode, arg2: *mut ffi::c_void) -> ffi::c_int, >, arg3: *mut ffi::c_void, ) -> *mut inode'}`
- New: `{'params': [{'name': 'sb', 'type': '*mut super_block'}, {'name': 'hashval', 'type': 'u64_'}, {'name': 'test', 'type': '::core::option::Option< unsafe extern "C" fn(arg1: *mut inode, arg2: *mut ffi::c_void'}], 'return_type': 'ffi::c_int, >, set: ::core::option::Option< unsafe extern "C" fn(arg1: *mut inode, arg2: *mut ffi::c_void) -> ffi::c_int, >, data: *mut ffi::c_void, ) -> *mut inode'}`

### Rust Evidence

- Graph edges: `1`

## W-000122 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iget_locked
- Explanation: iget_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut super_block'}, {'name': 'arg2', 'type': 'ffi::c_ulong'}], 'return_type': '*mut inode'}`
- New: `{'params': [{'name': 'sb', 'type': '*mut super_block'}, {'name': 'ino', 'type': 'u64_'}], 'return_type': '*mut inode'}`

### Rust Evidence

- Graph edges: `1`

## W-000123 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: igrab
- Explanation: igrab changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut inode'}], 'return_type': '*mut inode'}`
- New: `{'params': [{'name': 'inode', 'type': '*mut inode'}], 'return_type': '*mut inode'}`

### Rust Evidence

- Graph edges: `1`

## W-000126 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ilookup5_nowait
- Explanation: ilookup5_nowait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'sb', 'type': '*mut super_block'}, {'name': 'hashval', 'type': 'ffi::c_ulong'}, {'name': 'test', 'type': '::core::option::Option< unsafe extern "C" fn(arg1: *mut inode, arg2: *mut ffi::c_void'}], 'return_type': 'ffi::c_int, >, data: *mut ffi::c_void, isnew: *mut bool_, ) -> *mut inode'}`
- New: `{'params': [{'name': 'sb', 'type': '*mut super_block'}, {'name': 'hashval', 'type': 'u64_'}, {'name': 'test', 'type': '::core::option::Option< unsafe extern "C" fn(arg1: *mut inode, arg2: *mut ffi::c_void'}], 'return_type': 'ffi::c_int, >, data: *mut ffi::c_void, isnew: *mut bool_, ) -> *mut inode'}`

### Rust Evidence

- Graph edges: `1`

## W-000128 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_init_always_gfp
- Explanation: inode_init_always_gfp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut super_block'}, {'name': 'arg2', 'type': '*mut inode'}, {'name': 'arg3', 'type': 'gfp_t'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'sb', 'type': '*mut super_block'}, {'name': 'inode', 'type': '*mut inode'}, {'name': 'gfp', 'type': 'gfp_t'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000129 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_init_once
- Explanation: inode_init_once changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut inode'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'inode', 'type': '*mut inode'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000130 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_insert5
- Explanation: inode_insert5 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'inode', 'type': '*mut inode'}, {'name': 'hashval', 'type': 'ffi::c_ulong'}, {'name': 'test', 'type': '::core::option::Option< unsafe extern "C" fn(arg1: *mut inode, arg2: *mut ffi::c_void'}], 'return_type': 'ffi::c_int, >, set: ::core::option::Option< unsafe extern "C" fn(arg1: *mut inode, arg2: *mut ffi::c_void) -> ffi::c_int, >, data: *mut ffi::c_void, ) -> *mut inode'}`
- New: `{'params': [{'name': 'inode', 'type': '*mut inode'}, {'name': 'hashval', 'type': 'u64_'}, {'name': 'test', 'type': '::core::option::Option< unsafe extern "C" fn(arg1: *mut inode, arg2: *mut ffi::c_void'}], 'return_type': 'ffi::c_int, >, set: ::core::option::Option< unsafe extern "C" fn(arg1: *mut inode, arg2: *mut ffi::c_void) -> ffi::c_int, >, data: *mut ffi::c_void, ) -> *mut inode'}`

### Rust Evidence

- Graph edges: `1`

## W-000132 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: insert_inode_locked4
- Explanation: insert_inode_locked4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut inode'}, {'name': 'arg2', 'type': 'ffi::c_ulong'}, {'name': 'test', 'type': '::core::option::Option< unsafe extern "C" fn(arg1: *mut inode, arg2: *mut ffi::c_void'}], 'return_type': 'ffi::c_int, >, arg3: *mut ffi::c_void, ) -> ffi::c_int'}`
- New: `{'params': [{'name': 'inode', 'type': '*mut inode'}, {'name': 'hashval', 'type': 'u64_'}, {'name': 'test', 'type': '::core::option::Option< unsafe extern "C" fn(arg1: *mut inode, arg2: *mut ffi::c_void'}], 'return_type': 'ffi::c_int, >, data: *mut ffi::c_void, ) -> ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000133 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iunique
- Explanation: iunique changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut super_block'}, {'name': 'arg2', 'type': 'ino_t'}], 'return_type': 'ino_t'}`
- New: `{'params': [{'name': 'sb', 'type': '*mut super_block'}, {'name': 'max_reserved', 'type': 'ino_t'}], 'return_type': 'ino_t'}`

### Rust Evidence

- Graph edges: `1`

## W-000135 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lruvec_lru_size
- Explanation: lruvec_lru_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000136 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: map_anon_folio_pte_nopf
- Explanation: map_anon_folio_pte_nopf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000137 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: map_kernel_pages_complete
- Explanation: map_kernel_pages_complete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000138 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: map_kernel_pages_prepare
- Explanation: map_kernel_pages_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000139 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: map_wc
- Explanation: map_wc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000143 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmap_action_complete
- Explanation: mmap_action_complete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'action', 'type': '*mut mmap_action'}, {'name': 'vma', 'type': '*mut vm_area_struct'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'action', 'type': '*mut mmap_action'}, {'name': 'is_compat', 'type': 'bool_'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000144 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmap_action_prepare
- Explanation: mmap_action_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'action', 'type': '*mut mmap_action'}, {'name': 'desc', 'type': '*mut vm_area_desc'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'desc', 'type': '*mut vm_area_desc'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000145 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: module_destroy_params
- Explanation: module_destroy_params changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000147 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: online
- Explanation: online changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000148 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pages_mark_accessed_on_put
- Explanation: pages_mark_accessed_on_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000149 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pages_mark_dirty_on_put
- Explanation: pages_mark_dirty_on_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000150 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_set_copystring
- Explanation: param_set_copystring changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'val', 'type': '*const ffi::c_char'}, {'name': 'arg1', 'type': '*const kernel_param'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'val', 'type': '*const ffi::c_char'}, {'name': 'kp', 'type': '*const kernel_param'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000151 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: parse_args
- Explanation: parse_args changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'args', 'type': '*mut ffi::c_char'}, {'name': 'params', 'type': '*const kernel_param'}, {'name': 'num', 'type': 'ffi::c_uint'}, {'name': 'level_min', 'type': 's16'}, {'name': 'level_max', 'type': 's16'}, {'name': 'arg', 'type': '*mut ffi::c_void'}, {'name': 'unknown', 'type': 'parse_unknown_fn'}], 'return_type': '*mut ffi::c_char'}`
- New: `{'params': [{'name': 'doing', 'type': '*const ffi::c_char'}, {'name': 'args', 'type': '*mut ffi::c_char'}, {'name': 'params', 'type': '*const kernel_param'}, {'name': 'num', 'type': 'ffi::c_uint'}, {'name': 'min_level', 'type': 's16'}, {'name': 'max_level', 'type': 's16'}, {'name': 'arg', 'type': '*mut ffi::c_void'}, {'name': 'unknown', 'type': 'parse_unknown_fn'}], 'return_type': '*mut ffi::c_char'}`

### Rust Evidence

- Graph edges: `1`

## W-000152 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_align_resource
- Explanation: pci_align_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000153 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_align_resource
- Explanation: pcibios_align_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut ffi::c_void'}, {'name': 'arg2', 'type': '*const resource'}, {'name': 'arg3', 'type': 'resource_size_t'}, {'name': 'arg4', 'type': 'resource_size_t'}], 'return_type': 'resource_size_t'}`
- New: `{'params': [{'name': 'data', 'type': '*mut ffi::c_void'}, {'name': 'res', 'type': '*const resource'}, {'name': 'empty_res', 'type': '*const resource'}, {'name': 'size', 'type': 'resource_size_t'}, {'name': 'align', 'type': 'resource_size_t'}], 'return_type': 'resource_size_t'}`

### Rust Evidence

- Graph edges: `1`

## W-000155 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pmdp_clear_flush_young
- Explanation: pmdp_clear_flush_young changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'address', 'type': 'ffi::c_ulong'}, {'name': 'pmdp', 'type': '*mut pmd_t'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'address', 'type': 'ffi::c_ulong'}, {'name': 'pmdp', 'type': '*mut pmd_t'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000156 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pmdp_test_and_clear_young
- Explanation: pmdp_test_and_clear_young changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'addr', 'type': 'ffi::c_ulong'}, {'name': 'pmdp', 'type': '*mut pmd_t'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'addr', 'type': 'ffi::c_ulong'}, {'name': 'pmdp', 'type': '*mut pmd_t'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000157 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ptep_clear_flush_young
- Explanation: ptep_clear_flush_young changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'address', 'type': 'ffi::c_ulong'}, {'name': 'ptep', 'type': '*mut pte_t'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'address', 'type': 'ffi::c_ulong'}, {'name': 'ptep', 'type': '*mut pte_t'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000158 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ptep_test_and_clear_young
- Explanation: ptep_test_and_clear_young changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'addr', 'type': 'ffi::c_ulong'}, {'name': 'ptep', 'type': '*mut pte_t'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'addr', 'type': 'ffi::c_ulong'}, {'name': 'ptep', 'type': '*mut pte_t'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000159 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pudp_test_and_clear_young
- Explanation: pudp_test_and_clear_young changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'addr', 'type': 'ffi::c_ulong'}, {'name': 'pudp', 'type': '*mut pud_t'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'addr', 'type': 'ffi::c_ulong'}, {'name': 'pudp', 'type': '*mut pud_t'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000160 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rb_erase_linked
- Explanation: rb_erase_linked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000162 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_backing_file_alloc
- Explanation: security_backing_file_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000163 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_backing_file_free
- Explanation: security_backing_file_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000164 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_mmap_backing_file
- Explanation: security_mmap_backing_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000166 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_fsync_noflush
- Explanation: simple_fsync_noflush changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000168 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: soc_attr_read_machine
- Explanation: soc_attr_read_machine changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000170 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: software_node_init
- Explanation: software_node_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000172 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_create_groups
- Explanation: sysfs_create_groups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'kobj', 'type': '*mut kobject'}, {'name': 'groups', 'type': '*mut *const attribute_group'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'kobj', 'type': '*mut kobject'}, {'name': 'groups', 'type': '*const *const attribute_group'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000173 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_groups_change_owner
- Explanation: sysfs_groups_change_owner changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'kobj', 'type': '*mut kobject'}, {'name': 'groups', 'type': '*mut *const attribute_group'}, {'name': 'kuid', 'type': 'kuid_t'}, {'name': 'kgid', 'type': 'kgid_t'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'kobj', 'type': '*mut kobject'}, {'name': 'groups', 'type': '*const *const attribute_group'}, {'name': 'kuid', 'type': 'kuid_t'}, {'name': 'kgid', 'type': 'kgid_t'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000174 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_remove_groups
- Explanation: sysfs_remove_groups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'kobj', 'type': '*mut kobject'}, {'name': 'groups', 'type': '*mut *const attribute_group'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'kobj', 'type': '*mut kobject'}, {'name': 'groups', 'type': '*const *const attribute_group'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000175 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_update_groups
- Explanation: sysfs_update_groups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'kobj', 'type': '*mut kobject'}, {'name': 'groups', 'type': '*mut *const attribute_group'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'kobj', 'type': '*mut kobject'}, {'name': 'groups', 'type': '*const *const attribute_group'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000176 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: timer_create_restore_ids
- Explanation: timer_create_restore_ids changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(2usize, 1u8) as u32) } } #[inline] pub fn set_timer_create_restore_ids(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(3usize, 1u8) as u32) } } #[inline] pub fn set_timer_create_restore_ids(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000177 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: timerqueue_linked_add
- Explanation: timerqueue_linked_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000179 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unlock_new_inode
- Explanation: unlock_new_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut inode'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'inode', 'type': '*mut inode'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000180 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_brk_flags
- Explanation: vm_brk_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': 'ffi::c_ulong'}, {'name': 'arg2', 'type': 'ffi::c_ulong'}, {'name': 'arg3', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'addr', 'type': 'ffi::c_ulong'}, {'name': 'request', 'type': 'ffi::c_ulong'}, {'name': 'is_exec', 'type': 'bool_'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000182 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_mmap_shadow_stack
- Explanation: vm_mmap_shadow_stack changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000183 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_munmap
- Explanation: vm_munmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': 'ffi::c_ulong'}, {'name': 'arg2', 'type': 'usize'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'start', 'type': 'ffi::c_ulong'}, {'name': 'len', 'type': 'usize'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000184 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_mmu_pagesize
- Explanation: vma_mmu_pagesize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000185 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmemmap_populate_hvo
- Explanation: vmemmap_populate_hvo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'start', 'type': 'ffi::c_ulong'}, {'name': 'end', 'type': 'ffi::c_ulong'}, {'name': 'node', 'type': 'ffi::c_int'}, {'name': 'headsize', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'start', 'type': 'ffi::c_ulong'}, {'name': 'end', 'type': 'ffi::c_ulong'}, {'name': 'order', 'type': 'ffi::c_uint'}, {'name': 'zone', 'type': '*mut zone'}, {'name': 'headsize', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000187 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: x86_call_depth_emit_accounting
- Explanation: x86_call_depth_emit_accounting changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000188 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: zap_huge_pmd
- Explanation: zap_huge_pmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'tlb', 'type': '*mut mmu_gather'}, {'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'pmd', 'type': '*mut pmd_t'}, {'name': 'addr', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'tlb', 'type': '*mut mmu_gather'}, {'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'pmd', 'type': '*mut pmd_t'}, {'name': 'addr', 'type': 'ffi::c_ulong'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000190 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: zap_special_vma_range
- Explanation: zap_special_vma_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000614 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __compat_vma_mmap
- Explanation: __compat_vma_mmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct file_operations *f_op', 'struct file *file', 'struct vm_area_struct *vma'], 'return_type': 'int'}`
- New: `{'params': ['struct vm_area_desc *desc', 'struct vm_area_struct *vma'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000615 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __insert_inode_hash
- Explanation: __insert_inode_hash changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct inode *', 'unsigned long hashval'], 'return_type': 'extern void'}`
- New: `{'params': ['struct inode *inode', 'u64 hashval'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-000621 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __refcount_sub_and_test
- Explanation: __refcount_sub_and_test changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['int i', 'refcount_t *r', 'int *oldp'], 'return_type': 'static inline __must_check __signed_wrap bool'}`
- New: `{'params': ['int i', 'refcount_t *r', 'int *oldp'], 'return_type': 'static inline __must_check bool'}`

### Rust Evidence

- Graph edges: `1`

## W-000622 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __remove_inode_hash
- Explanation: __remove_inode_hash changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct inode *'], 'return_type': 'extern void'}`
- New: `{'params': ['struct inode *inode'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-000624 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_notifier_call_chain
- Explanation: acpi_notifier_call_chain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct acpi_device *', 'u32', 'u32'], 'return_type': 'extern int'}`
- New: `{'params': ['const char *device_class', 'const char *bus_id', 'u32 type', 'u32 data'], 'return_type': 'extern int'}`

### Rust Evidence

- Graph edges: `1`

## W-000625 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: address_space_init_once
- Explanation: address_space_init_once changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct address_space *mapping'], 'return_type': 'extern void'}`
- New: `{'params': ['struct address_space *mapping'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-000627 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_driver_adjust_perf
- Explanation: cpufreq_driver_adjust_perf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned int cpu', 'unsigned long min_perf', 'unsigned long target_perf', 'unsigned long capacity'], 'return_type': 'void'}`
- New: `{'params': ['struct cpufreq_policy *policy', 'unsigned long min_perf', 'unsigned long target_perf', 'unsigned long capacity'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-000628 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_mark_dontcache
- Explanation: d_mark_dontcache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct inode *inode'], 'return_type': 'extern void'}`
- New: `{'params': ['struct inode *inode'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-000630 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: discard_new_inode
- Explanation: discard_new_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct inode *'], 'return_type': 'extern void'}`
- New: `{'params': ['struct inode *inode'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-000659 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: evict_inodes
- Explanation: evict_inodes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct super_block *sb'], 'return_type': 'extern void'}`
- New: `{'params': ['struct super_block *sb'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-000660 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: find_inode_by_ino_rcu
- Explanation: find_inode_by_ino_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct super_block *', 'unsigned long'], 'return_type': 'extern struct inode *'}`
- New: `{'params': ['struct super_block *sb', 'u64 ino'], 'return_type': 'struct inode *'}`

### Rust Evidence

- Graph edges: `1`

## W-000661 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: find_inode_nowait
- Explanation: find_inode_nowait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct super_block *', 'unsigned long', 'int (*match)(struct inode *, unsigned long, void *)', 'void *data'], 'return_type': 'extern struct inode *'}`
- New: `{'params': ['struct super_block *sb', 'u64 hashval', 'int (*match)(struct inode *, u64, void *)', 'void *data'], 'return_type': 'struct inode *'}`

### Rust Evidence

- Graph edges: `1`

## W-000662 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: find_inode_rcu
- Explanation: find_inode_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct super_block *', 'unsigned long', 'int (*)(struct inode *, void *)', 'void *'], 'return_type': 'extern struct inode *'}`
- New: `{'params': ['struct super_block *sb', 'u64 hashval', 'int (*test)(struct inode *, void *)', 'void *data'], 'return_type': 'struct inode *'}`

### Rust Evidence

- Graph edges: `1`

## W-000663 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_next_ino
- Explanation: get_next_ino changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'extern unsigned int'}`
- New: `{'params': [], 'return_type': 'unsigned int'}`

### Rust Evidence

- Graph edges: `1`

## W-000666 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iget5_locked_rcu
- Explanation: iget5_locked_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct super_block *', 'unsigned long', 'int (*test)(struct inode *, void *)', 'int (*set)(struct inode *, void *)', 'void *'], 'return_type': 'struct inode *'}`
- New: `{'params': ['struct super_block *sb', 'u64 hashval', 'int (*test)(struct inode *, void *)', 'int (*set)(struct inode *, void *)', 'void *data'], 'return_type': 'struct inode *'}`

### Rust Evidence

- Graph edges: `1`

## W-000667 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iget_locked
- Explanation: iget_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct super_block *', 'unsigned long'], 'return_type': 'extern struct inode *'}`
- New: `{'params': ['struct super_block *sb', 'u64 ino'], 'return_type': 'struct inode *'}`

### Rust Evidence

- Graph edges: `1`

## W-000668 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: igrab
- Explanation: igrab changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct inode *'], 'return_type': 'extern struct inode *'}`
- New: `{'params': ['struct inode *inode'], 'return_type': 'struct inode *'}`

### Rust Evidence

- Graph edges: `1`

## W-000671 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ilookup5_nowait
- Explanation: ilookup5_nowait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct super_block *sb', 'unsigned long hashval', 'int (*test)(struct inode *, void *)', 'void *data', 'bool *isnew'], 'return_type': 'extern struct inode *'}`
- New: `{'params': ['struct super_block *sb', 'u64 hashval', 'int (*test)(struct inode *, void *)', 'void *data', 'bool *isnew'], 'return_type': 'struct inode *'}`

### Rust Evidence

- Graph edges: `1`

## W-000672 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_init_once
- Explanation: inode_init_once changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct inode *'], 'return_type': 'extern void'}`
- New: `{'params': ['struct inode *inode'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-000673 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_insert5
- Explanation: inode_insert5 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct inode *inode', 'unsigned long hashval', 'int (*test)(struct inode *, void *)', 'int (*set)(struct inode *, void *)', 'void *data'], 'return_type': 'extern struct inode *'}`
- New: `{'params': ['struct inode *inode', 'u64 hashval', 'int (*test)(struct inode *, void *)', 'int (*set)(struct inode *, void *)', 'void *data'], 'return_type': 'struct inode *'}`

### Rust Evidence

- Graph edges: `1`

## W-000674 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_just_drop
- Explanation: inode_just_drop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct inode *inode'], 'return_type': 'extern int'}`
- New: `{'params': ['struct inode *inode'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000675 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_lru_list_add
- Explanation: inode_lru_list_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct inode *inode'], 'return_type': 'extern void'}`
- New: `{'params': ['struct inode *inode'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-000676 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_needs_sync
- Explanation: inode_needs_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct inode *inode'], 'return_type': 'extern int'}`
- New: `{'params': ['struct inode *inode'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000677 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_sb_list_add
- Explanation: inode_sb_list_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct inode *inode'], 'return_type': 'extern void'}`
- New: `{'params': ['struct inode *inode'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-000679 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: insert_inode_locked4
- Explanation: insert_inode_locked4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct inode *', 'unsigned long', 'int (*test)(struct inode *, void *)', 'void *'], 'return_type': 'extern int'}`
- New: `{'params': ['struct inode *inode', 'u64 hashval', 'int (*test)(struct inode *, void *)', 'void *data'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000680 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iunique
- Explanation: iunique changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct super_block *', 'ino_t'], 'return_type': 'extern ino_t'}`
- New: `{'params': ['struct super_block *sb', 'ino_t max_reserved'], 'return_type': 'ino_t'}`

### Rust Evidence

- Graph edges: `1`

## W-000684 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmap_action_complete
- Explanation: mmap_action_complete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mmap_action *action', 'struct vm_area_struct *vma'], 'return_type': 'int'}`
- New: `{'params': ['struct vm_area_struct *vma', 'struct mmap_action *action', 'bool is_compat'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000685 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmap_action_prepare
- Explanation: mmap_action_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mmap_action *action', 'struct vm_area_desc *desc'], 'return_type': 'void'}`
- New: `{'params': ['struct vm_area_desc *desc'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000686 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_enable_ptm
- Explanation: pci_enable_ptm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct pci_dev *dev', 'u8 *granularity'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct pci_dev *dev'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `1`

## W-000687 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_align_resource
- Explanation: pcibios_align_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['void *', 'const struct resource *', 'resource_size_t', 'resource_size_t'], 'return_type': 'resource_size_t'}`
- New: `{'params': ['void *data', 'const struct resource *res', 'const struct resource *empty_res', 'resource_size_t size', 'resource_size_t align'], 'return_type': 'resource_size_t'}`

### Rust Evidence

- Graph edges: `1`

## W-000704 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unlock_new_inode
- Explanation: unlock_new_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct inode *'], 'return_type': 'extern void'}`
- New: `{'params': ['struct inode *inode'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-000705 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_llseek
- Explanation: vfs_llseek changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct file *file', 'loff_t offset', 'int whence'], 'return_type': 'extern loff_t'}`
- New: `{'params': ['struct file *file', 'loff_t offset', 'int whence'], 'return_type': 'loff_t'}`

### Rust Evidence

- Graph edges: `1`

## W-000706 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_brk_flags
- Explanation: vm_brk_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned long', 'unsigned long', 'unsigned long'], 'return_type': 'extern int __must_check'}`
- New: `{'params': ['unsigned long addr', 'unsigned long request', 'bool is_exec'], 'return_type': 'int __must_check'}`

### Rust Evidence

- Graph edges: `1`

## W-000708 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_munmap
- Explanation: vm_munmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned long', 'size_t'], 'return_type': 'extern int'}`
- New: `{'params': ['unsigned long start', 'size_t len'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000716 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmemmap_populate_hvo
- Explanation: vmemmap_populate_hvo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned long start', 'unsigned long end', 'int node', 'unsigned long headsize'], 'return_type': 'int'}`
- New: `{'params': ['unsigned long start', 'unsigned long end', 'unsigned int order', 'struct zone *zone', 'unsigned long headsize'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000204 FieldDrift

- Risk: High
- Score: 10.6
- Symbol: drm_mode_config
- Explanation: drm_mode_config changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mutex', 'type': 'mutex'}, {'name': 'connection_mutex', 'type': 'drm_modeset_lock'}, {'name': 'acquire_ctx', 'type': '*mut drm_modeset_acquire_ctx'}, {'name': 'idr_mutex', 'type': 'mutex'}, {'name': 'object_idr', 'type': 'idr'}, {'name': 'tile_idr', 'type': 'idr'}, {'name': 'fb_lock', 'type': 'mutex'}, {'name': 'num_fb', 'type': 'ffi::c_int'}, {'name': 'fb_list', 'type': 'list_head'}, {'name': 'connector_list_lock', 'type': 'spinlock_t'}, {'name': 'num_connector', 'type': 'ffi::c_int'}, {'name': 'connector_ida', 'type': 'ida'}, {'name': 'connector_list', 'type': 'list_head'}, {'name': 'connector_free_list', 'type': 'llist_head'}, {'name': 'connector_free_work', 'type': 'work_struct'}, {'name': 'num_encoder', 'type': 'ffi::c_int'}, {'name': 'encoder_list', 'type': 'list_head'}, {'name': 'num_total_plane', 'type': 'ffi::c_int'}, {'name': 'plane_list', 'type': 'list_head'}, {'name': 'panic_lock', 'type': 'raw_spinlock'}, {'name': 'num_colorop', 'type': 'ffi::c_int'}, {'name': 'colorop_list', 'type': 'list_head'}, {'name': 'num_crtc', 'type': 'ffi::c_int'}, {'name': 'crtc_list', 'type': 'list_head'}, {'name': 'property_list', 'type': 'list_head'}, {'name': 'privobj_list', 'type': 'list_head'}, {'name': 'min_width', 'type': 'ffi::c_uint'}, {'name': 'min_height', 'type': 'ffi::c_uint'}, {'name': 'max_width', 'type': 'ffi::c_uint'}, {'name': 'max_height', 'type': 'ffi::c_uint'}, {'name': 'funcs', 'type': '*const drm_mode_config_funcs'}, {'name': 'poll_enabled', 'type': 'bool_'}, {'name': 'poll_running', 'type': 'bool_'}, {'name': 'delayed_event', 'type': 'bool_'}, {'name': 'output_poll_work', 'type': 'delayed_work'}, {'name': 'blob_lock', 'type': 'mutex'}, {'name': 'property_blob_list', 'type': 'list_head'}, {'name': 'edid_property', 'type': '*mut drm_property'}, {'name': 'dpms_property', 'type': '*mut drm_property'}, {'name': 'path_property', 'type': '*mut drm_property'}, {'name': 'tile_property', 'type': '*mut drm_property'}, {'name': 'link_status_property', 'type': '*mut drm_property'}, {'name': 'plane_type_property', 'type': '*mut drm_property'}, {'name': 'prop_src_x', 'type': '*mut drm_property'}, {'name': 'prop_src_y', 'type': '*mut drm_property'}, {'name': 'prop_src_w', 'type': '*mut drm_property'}, {'name': 'prop_src_h', 'type': '*mut drm_property'}, {'name': 'prop_crtc_x', 'type': '*mut drm_property'}, {'name': 'prop_crtc_y', 'type': '*mut drm_property'}, {'name': 'prop_crtc_w', 'type': '*mut drm_property'}, {'name': 'prop_crtc_h', 'type': '*mut drm_property'}, {'name': 'prop_fb_id', 'type': '*mut drm_property'}, {'name': 'prop_in_fence_fd', 'type': '*mut drm_property'}, {'name': 'prop_out_fence_ptr', 'type': '*mut drm_property'}, {'name': 'prop_crtc_id', 'type': '*mut drm_property'}, {'name': 'prop_fb_damage_clips', 'type': '*mut drm_property'}, {'name': 'prop_active', 'type': '*mut drm_property'}, {'name': 'prop_mode_id', 'type': '*mut drm_property'}, {'name': 'prop_vrr_enabled', 'type': '*mut drm_property'}, {'name': 'dvi_i_subconnector_property', 'type': '*mut drm_property'}, {'name': 'dvi_i_select_subconnector_property', 'type': '*mut drm_property'}, {'name': 'dp_subconnector_property', 'type': '*mut drm_property'}, {'name': 'tv_subconnector_property', 'type': '*mut drm_property'}, {'name': 'tv_select_subconnector_property', 'type': '*mut drm_property'}, {'name': 'legacy_tv_mode_property', 'type': '*mut drm_property'}, {'name': 'tv_mode_property', 'type': '*mut drm_property'}, {'name': 'tv_left_margin_property', 'type': '*mut drm_property'}, {'name': 'tv_right_margin_property', 'type': '*mut drm_property'}, {'name': 'tv_top_margin_property', 'type': '*mut drm_property'}, {'name': 'tv_bottom_margin_property', 'type': '*mut drm_property'}, {'name': 'tv_brightness_property', 'type': '*mut drm_property'}, {'name': 'tv_contrast_property', 'type': '*mut drm_property'}, {'name': 'tv_flicker_reduction_property', 'type': '*mut drm_property'}, {'name': 'tv_overscan_property', 'type': '*mut drm_property'}, {'name': 'tv_saturation_property', 'type': '*mut drm_property'}, {'name': 'tv_hue_property', 'type': '*mut drm_property'}, {'name': 'scaling_mode_property', 'type': '*mut drm_property'}, {'name': 'aspect_ratio_property', 'type': '*mut drm_property'}, {'name': 'content_type_property', 'type': '*mut drm_property'}, {'name': 'degamma_lut_property', 'type': '*mut drm_property'}, {'name': 'degamma_lut_size_property', 'type': '*mut drm_property'}, {'name': 'ctm_property', 'type': '*mut drm_property'}, {'name': 'gamma_lut_property', 'type': '*mut drm_property'}, {'name': 'gamma_lut_size_property', 'type': '*mut drm_property'}, {'name': 'suggested_x_property', 'type': '*mut drm_property'}, {'name': 'suggested_y_property', 'type': '*mut drm_property'}, {'name': 'non_desktop_property', 'type': '*mut drm_property'}, {'name': 'panel_orientation_property', 'type': '*mut drm_property'}, {'name': 'writeback_fb_id_property', 'type': '*mut drm_property'}, {'name': 'writeback_pixel_formats_property', 'type': '*mut drm_property'}, {'name': 'writeback_out_fence_ptr_property', 'type': '*mut drm_property'}, {'name': 'hdr_output_metadata_property', 'type': '*mut drm_property'}, {'name': 'content_protection_property', 'type': '*mut drm_property'}, {'name': 'hdcp_content_type_property', 'type': '*mut drm_property'}, {'name': 'preferred_depth', 'type': 'u32'}, {'name': 'prefer_shadow', 'type': 'u32'}, {'name': 'quirk_addfb_prefer_xbgr_30bpp', 'type': 'bool_'}, {'name': 'quirk_addfb_prefer_host_byte_order', 'type': 'bool_'}, {'name': 'async_page_flip', 'type': 'bool_'}, {'name': 'fb_modifiers_not_supported', 'type': 'bool_'}, {'name': 'normalize_zpos', 'type': 'bool_'}, {'name': 'modifiers_property', 'type': '*mut drm_property'}, {'name': 'async_modifiers_property', 'type': '*mut drm_property'}, {'name': 'size_hints_property', 'type': '*mut drm_property'}, {'name': 'cursor_width', 'type': 'u32'}, {'name': 'cursor_height', 'type': 'u32'}, {'name': 'suspend_state', 'type': '*mut drm_atomic_state'}, {'name': 'helper_private', 'type': '*mut drm_mode_config_helper_funcs'}]`
- New: `[{'name': 'mutex', 'type': 'mutex'}, {'name': 'connection_mutex', 'type': 'drm_modeset_lock'}, {'name': 'acquire_ctx', 'type': '*mut drm_modeset_acquire_ctx'}, {'name': 'idr_mutex', 'type': 'mutex'}, {'name': 'object_idr', 'type': 'idr'}, {'name': 'tile_idr', 'type': 'idr'}, {'name': 'fb_lock', 'type': 'mutex'}, {'name': 'num_fb', 'type': 'ffi::c_int'}, {'name': 'fb_list', 'type': 'list_head'}, {'name': 'connector_list_lock', 'type': 'spinlock_t'}, {'name': 'num_connector', 'type': 'ffi::c_int'}, {'name': 'connector_ida', 'type': 'ida'}, {'name': 'connector_list', 'type': 'list_head'}, {'name': 'connector_free_list', 'type': 'llist_head'}, {'name': 'connector_free_work', 'type': 'work_struct'}, {'name': 'num_encoder', 'type': 'ffi::c_int'}, {'name': 'encoder_list', 'type': 'list_head'}, {'name': 'num_total_plane', 'type': 'ffi::c_int'}, {'name': 'plane_list', 'type': 'list_head'}, {'name': 'panic_lock', 'type': 'raw_spinlock'}, {'name': 'num_colorop', 'type': 'ffi::c_int'}, {'name': 'colorop_list', 'type': 'list_head'}, {'name': 'num_crtc', 'type': 'ffi::c_int'}, {'name': 'crtc_list', 'type': 'list_head'}, {'name': 'property_list', 'type': 'list_head'}, {'name': 'privobj_list', 'type': 'list_head'}, {'name': 'min_width', 'type': 'ffi::c_uint'}, {'name': 'min_height', 'type': 'ffi::c_uint'}, {'name': 'max_width', 'type': 'ffi::c_uint'}, {'name': 'max_height', 'type': 'ffi::c_uint'}, {'name': 'funcs', 'type': '*const drm_mode_config_funcs'}, {'name': 'poll_enabled', 'type': 'bool_'}, {'name': 'poll_running', 'type': 'bool_'}, {'name': 'delayed_event', 'type': 'bool_'}, {'name': 'output_poll_work', 'type': 'delayed_work'}, {'name': 'blob_lock', 'type': 'mutex'}, {'name': 'property_blob_list', 'type': 'list_head'}, {'name': 'edid_property', 'type': '*mut drm_property'}, {'name': 'dpms_property', 'type': '*mut drm_property'}, {'name': 'path_property', 'type': '*mut drm_property'}, {'name': 'tile_property', 'type': '*mut drm_property'}, {'name': 'panel_type_property', 'type': '*mut drm_property'}, {'name': 'link_status_property', 'type': '*mut drm_property'}, {'name': 'plane_type_property', 'type': '*mut drm_property'}, {'name': 'prop_src_x', 'type': '*mut drm_property'}, {'name': 'prop_src_y', 'type': '*mut drm_property'}, {'name': 'prop_src_w', 'type': '*mut drm_property'}, {'name': 'prop_src_h', 'type': '*mut drm_property'}, {'name': 'prop_crtc_x', 'type': '*mut drm_property'}, {'name': 'prop_crtc_y', 'type': '*mut drm_property'}, {'name': 'prop_crtc_w', 'type': '*mut drm_property'}, {'name': 'prop_crtc_h', 'type': '*mut drm_property'}, {'name': 'prop_fb_id', 'type': '*mut drm_property'}, {'name': 'prop_in_fence_fd', 'type': '*mut drm_property'}, {'name': 'prop_out_fence_ptr', 'type': '*mut drm_property'}, {'name': 'prop_crtc_id', 'type': '*mut drm_property'}, {'name': 'prop_fb_damage_clips', 'type': '*mut drm_property'}, {'name': 'prop_active', 'type': '*mut drm_property'}, {'name': 'prop_mode_id', 'type': '*mut drm_property'}, {'name': 'prop_vrr_enabled', 'type': '*mut drm_property'}, {'name': 'dvi_i_subconnector_property', 'type': '*mut drm_property'}, {'name': 'dvi_i_select_subconnector_property', 'type': '*mut drm_property'}, {'name': 'dp_subconnector_property', 'type': '*mut drm_property'}, {'name': 'tv_subconnector_property', 'type': '*mut drm_property'}, {'name': 'tv_select_subconnector_property', 'type': '*mut drm_property'}, {'name': 'legacy_tv_mode_property', 'type': '*mut drm_property'}, {'name': 'tv_mode_property', 'type': '*mut drm_property'}, {'name': 'tv_left_margin_property', 'type': '*mut drm_property'}, {'name': 'tv_right_margin_property', 'type': '*mut drm_property'}, {'name': 'tv_top_margin_property', 'type': '*mut drm_property'}, {'name': 'tv_bottom_margin_property', 'type': '*mut drm_property'}, {'name': 'tv_brightness_property', 'type': '*mut drm_property'}, {'name': 'tv_contrast_property', 'type': '*mut drm_property'}, {'name': 'tv_flicker_reduction_property', 'type': '*mut drm_property'}, {'name': 'tv_overscan_property', 'type': '*mut drm_property'}, {'name': 'tv_saturation_property', 'type': '*mut drm_property'}, {'name': 'tv_hue_property', 'type': '*mut drm_property'}, {'name': 'scaling_mode_property', 'type': '*mut drm_property'}, {'name': 'aspect_ratio_property', 'type': '*mut drm_property'}, {'name': 'content_type_property', 'type': '*mut drm_property'}, {'name': 'degamma_lut_property', 'type': '*mut drm_property'}, {'name': 'degamma_lut_size_property', 'type': '*mut drm_property'}, {'name': 'ctm_property', 'type': '*mut drm_property'}, {'name': 'gamma_lut_property', 'type': '*mut drm_property'}, {'name': 'gamma_lut_size_property', 'type': '*mut drm_property'}, {'name': 'background_color_property', 'type': '*mut drm_property'}, {'name': 'suggested_x_property', 'type': '*mut drm_property'}, {'name': 'suggested_y_property', 'type': '*mut drm_property'}, {'name': 'non_desktop_property', 'type': '*mut drm_property'}, {'name': 'panel_orientation_property', 'type': '*mut drm_property'}, {'name': 'writeback_fb_id_property', 'type': '*mut drm_property'}, {'name': 'writeback_pixel_formats_property', 'type': '*mut drm_property'}, {'name': 'writeback_out_fence_ptr_property', 'type': '*mut drm_property'}, {'name': 'hdr_output_metadata_property', 'type': '*mut drm_property'}, {'name': 'content_protection_property', 'type': '*mut drm_property'}, {'name': 'hdcp_content_type_property', 'type': '*mut drm_property'}, {'name': 'preferred_depth', 'type': 'u32'}, {'name': 'prefer_shadow', 'type': 'u32'}, {'name': 'quirk_addfb_prefer_xbgr_30bpp', 'type': 'bool_'}, {'name': 'quirk_addfb_prefer_host_byte_order', 'type': 'bool_'}, {'name': 'async_page_flip', 'type': 'bool_'}, {'name': 'fb_modifiers_not_supported', 'type': 'bool_'}, {'name': 'normalize_zpos', 'type': 'bool_'}, {'name': 'modifiers_property', 'type': '*mut drm_property'}, {'name': 'async_modifiers_property', 'type': '*mut drm_property'}, {'name': 'size_hints_property', 'type': '*mut drm_property'}, {'name': 'cursor_width', 'type': 'u32'}, {'name': 'cursor_height', 'type': 'u32'}, {'name': 'suspend_state', 'type': '*mut drm_atomic_state'}, {'name': 'helper_private', 'type': '*mut drm_mode_config_helper_funcs'}]`

### Rust Evidence

- Graph edges: `5`

## W-000634 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: drm_fb_helper_blank
- Explanation: drm_fb_helper_blank changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['int blank', 'struct fb_info *info'], 'return_type': 'static inline int'}`
- New: `{'params': ['int blank', 'struct fb_info *info'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000635 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: drm_fb_helper_check_var
- Explanation: drm_fb_helper_check_var changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct fb_var_screeninfo *var', 'struct fb_info *info'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct fb_var_screeninfo *var', 'struct fb_info *info'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000636 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: drm_fb_helper_deferred_io
- Explanation: drm_fb_helper_deferred_io changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct fb_info *info', 'struct list_head *pagelist'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct fb_info *info', 'struct list_head *pagereflist'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000637 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: drm_fb_helper_fill_info
- Explanation: drm_fb_helper_fill_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct fb_info *info', 'struct drm_fb_helper *fb_helper', 'struct drm_fb_helper_surface_size *sizes'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct fb_info *info', 'struct drm_fb_helper *fb_helper', 'struct drm_fb_helper_surface_size *sizes'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000638 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: drm_fb_helper_fini
- Explanation: drm_fb_helper_fini changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_fb_helper *helper'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct drm_fb_helper *helper'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000639 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: drm_fb_helper_hotplug_event
- Explanation: drm_fb_helper_hotplug_event changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_fb_helper *fb_helper'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct drm_fb_helper *fb_helper'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000640 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: drm_fb_helper_init
- Explanation: drm_fb_helper_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_device *dev', 'struct drm_fb_helper *helper'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct drm_device *dev', 'struct drm_fb_helper *helper'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000641 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: drm_fb_helper_initial_config
- Explanation: drm_fb_helper_initial_config changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_fb_helper *fb_helper'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct drm_fb_helper *fb_helper'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000642 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: drm_fb_helper_ioctl
- Explanation: drm_fb_helper_ioctl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct fb_info *info', 'unsigned int cmd', 'unsigned long arg'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct fb_info *info', 'unsigned int cmd', 'unsigned long arg'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000643 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: drm_fb_helper_pan_display
- Explanation: drm_fb_helper_pan_display changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct fb_var_screeninfo *var', 'struct fb_info *info'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct fb_var_screeninfo *var', 'struct fb_info *info'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000644 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: drm_fb_helper_prepare
- Explanation: drm_fb_helper_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_device *dev', 'struct drm_fb_helper *helper', 'unsigned int preferred_bpp', 'const struct drm_fb_helper_funcs *funcs'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct drm_device *dev', 'struct drm_fb_helper *helper', 'unsigned int preferred_bpp', 'const struct drm_fb_helper_funcs *funcs'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000645 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: drm_fb_helper_restore_fbdev_mode_unlocked
- Explanation: drm_fb_helper_restore_fbdev_mode_unlocked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_fb_helper *fb_helper'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct drm_fb_helper *fb_helper', 'bool force'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000646 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: drm_fb_helper_set_par
- Explanation: drm_fb_helper_set_par changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct fb_info *info'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct fb_info *info'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000647 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: drm_fb_helper_set_suspend
- Explanation: drm_fb_helper_set_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_fb_helper *fb_helper', 'bool suspend'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct drm_fb_helper *fb_helper', 'bool suspend'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000648 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: drm_fb_helper_set_suspend_unlocked
- Explanation: drm_fb_helper_set_suspend_unlocked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_fb_helper *fb_helper', 'bool suspend'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct drm_fb_helper *fb_helper', 'bool suspend'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000649 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: drm_fb_helper_setcmap
- Explanation: drm_fb_helper_setcmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct fb_cmap *cmap', 'struct fb_info *info'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct fb_cmap *cmap', 'struct fb_info *info'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000650 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: drm_fb_helper_unprepare
- Explanation: drm_fb_helper_unprepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_fb_helper *fb_helper'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct drm_fb_helper *fb_helper'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000651 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: drm_fb_helper_unregister_info
- Explanation: drm_fb_helper_unregister_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_fb_helper *fb_helper'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct drm_fb_helper *fb_helper'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000690 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_clk_disable
- Explanation: rust_helper_clk_disable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct clk *clk'], 'return_type': 'void'}`
- New: `{'params': ['struct clk *clk'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000691 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_clk_disable_unprepare
- Explanation: rust_helper_clk_disable_unprepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct clk *clk'], 'return_type': 'void'}`
- New: `{'params': ['struct clk *clk'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000692 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_clk_enable
- Explanation: rust_helper_clk_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct clk *clk'], 'return_type': 'int'}`
- New: `{'params': ['struct clk *clk'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000694 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_clk_get_optional
- Explanation: rust_helper_clk_get_optional changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct device *dev', 'const char *id'], 'return_type': 'struct clk *'}`
- New: `{'params': ['struct device *dev', 'const char *id'], 'return_type': '__rust_helper struct clk *'}`

### Rust Evidence

- Graph edges: `0`

## W-000695 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_clk_get_rate
- Explanation: rust_helper_clk_get_rate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct clk *clk'], 'return_type': 'unsigned long'}`
- New: `{'params': ['struct clk *clk'], 'return_type': '__rust_helper unsigned long'}`

### Rust Evidence

- Graph edges: `0`

## W-000696 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_clk_prepare
- Explanation: rust_helper_clk_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct clk *clk'], 'return_type': 'int'}`
- New: `{'params': ['struct clk *clk'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000697 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_clk_prepare_enable
- Explanation: rust_helper_clk_prepare_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct clk *clk'], 'return_type': 'int'}`
- New: `{'params': ['struct clk *clk'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000699 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_clk_set_rate
- Explanation: rust_helper_clk_set_rate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct clk *clk', 'unsigned long rate'], 'return_type': 'int'}`
- New: `{'params': ['struct clk *clk', 'unsigned long rate'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000700 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_clk_unprepare
- Explanation: rust_helper_clk_unprepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct clk *clk'], 'return_type': 'void'}`
- New: `{'params': ['struct clk *clk'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000701 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_static_key_count
- Explanation: rust_helper_static_key_count changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct static_key *key'], 'return_type': 'int'}`
- New: `{'params': ['struct static_key *key'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000199 FieldDrift

- Risk: High
- Score: 10.2
- Symbol: cpuinfo_x86
- Explanation: cpuinfo_x86 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'cpuinfo_x86__bindgen_ty_1'}, {'name': 'x86_stepping', 'type': '__u8'}, {'name': 'x86_tlbsize', 'type': 'ffi::c_int'}, {'name': 'vmx_capability', 'type': '[__u32; 5usize]'}, {'name': 'x86_virt_bits', 'type': '__u8'}, {'name': 'x86_phys_bits', 'type': '__u8'}, {'name': 'extended_cpuid_level', 'type': '__u32'}, {'name': 'cpuid_level', 'type': 'ffi::c_int'}, {'name': '__bindgen_anon_2', 'type': 'cpuinfo_x86__bindgen_ty_2'}, {'name': 'x86_vendor_id', 'type': '[ffi::c_char; 16usize]'}, {'name': 'x86_model_id', 'type': '[ffi::c_char; 64usize]'}, {'name': 'topo', 'type': 'cpuinfo_topology'}, {'name': 'x86_cache_size', 'type': 'ffi::c_uint'}, {'name': 'x86_cache_alignment', 'type': 'ffi::c_int'}, {'name': 'x86_cache_max_rmid', 'type': 'ffi::c_int'}, {'name': 'x86_cache_occ_scale', 'type': 'ffi::c_int'}, {'name': 'x86_cache_mbm_width_offset', 'type': 'ffi::c_int'}, {'name': 'x86_power', 'type': 'ffi::c_int'}, {'name': 'loops_per_jiffy', 'type': 'ffi::c_ulong'}, {'name': 'ppin', 'type': 'u64_'}, {'name': 'x86_clflush_size', 'type': 'u16_'}, {'name': 'booted_cores', 'type': 'u16_'}, {'name': 'cpu_index', 'type': 'u16_'}, {'name': 'smt_active', 'type': 'bool_'}, {'name': 'microcode', 'type': 'u32_'}, {'name': 'x86_cache_bits', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': 'u16'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'cpuinfo_x86__bindgen_ty_1'}, {'name': 'x86_stepping', 'type': '__u8'}, {'name': '__bindgen_anon_2', 'type': 'cpuinfo_x86__bindgen_ty_2'}, {'name': 'x86_tlbsize', 'type': 'ffi::c_int'}, {'name': 'vmx_capability', 'type': '[__u32; 5usize]'}, {'name': 'x86_virt_bits', 'type': '__u8'}, {'name': 'x86_phys_bits', 'type': '__u8'}, {'name': 'extended_cpuid_level', 'type': '__u32'}, {'name': 'cpuid_level', 'type': 'ffi::c_int'}, {'name': '__bindgen_anon_3', 'type': 'cpuinfo_x86__bindgen_ty_3'}, {'name': 'x86_vendor_id', 'type': '[ffi::c_char; 16usize]'}, {'name': 'x86_model_id', 'type': '[ffi::c_char; 64usize]'}, {'name': 'topo', 'type': 'cpuinfo_topology'}, {'name': 'x86_cache_size', 'type': 'ffi::c_uint'}, {'name': 'x86_cache_alignment', 'type': 'ffi::c_int'}, {'name': 'x86_cache_max_rmid', 'type': 'ffi::c_int'}, {'name': 'x86_cache_occ_scale', 'type': 'ffi::c_int'}, {'name': 'x86_cache_mbm_width_offset', 'type': 'ffi::c_int'}, {'name': 'x86_power', 'type': 'ffi::c_int'}, {'name': 'loops_per_jiffy', 'type': 'ffi::c_ulong'}, {'name': 'ppin', 'type': 'u64_'}, {'name': 'x86_clflush_size', 'type': 'u16_'}, {'name': 'booted_cores', 'type': 'u16_'}, {'name': 'cpu_index', 'type': 'u16_'}, {'name': 'smt_active', 'type': 'bool_'}, {'name': 'microcode', 'type': 'u32_'}, {'name': 'x86_cache_bits', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': 'u16'}]`

### Rust Evidence

- Graph edges: `8`

## W-000217 FieldDrift

- Risk: Medium
- Score: 9.8
- Symbol: mii_bus
- Explanation: mii_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'owner', 'type': '*mut module'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'id', 'type': '[ffi::c_char; 61usize]'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'read', 'type': '::core::option::Option<'}, {'name': 'write', 'type': '::core::option::Option<'}, {'name': 'read_c45', 'type': '::core::option::Option<'}, {'name': 'write_c45', 'type': '::core::option::Option<'}, {'name': 'reset', 'type': '::core::option::Option<unsafe extern "C" fn(bus: *mut mii_bus) -> ffi::c_int>'}, {'name': 'stats', 'type': '[mdio_bus_stats; 32usize]'}, {'name': 'mdio_lock', 'type': 'mutex'}, {'name': 'parent', 'type': '*mut device'}, {'name': 'state', 'type': 'mii_bus__bindgen_ty_1'}, {'name': 'dev', 'type': 'device'}, {'name': 'mdio_map', 'type': '[*mut mdio_device; 32usize]'}, {'name': 'phy_mask', 'type': 'u32_'}, {'name': 'phy_ignore_ta_mask', 'type': 'u32_'}, {'name': 'irq', 'type': '[ffi::c_int; 32usize]'}, {'name': 'reset_delay_us', 'type': 'ffi::c_int'}, {'name': 'reset_post_delay_us', 'type': 'ffi::c_int'}, {'name': 'reset_gpiod', 'type': '*mut gpio_desc'}, {'name': 'shared_lock', 'type': 'mutex'}]`
- New: `[{'name': 'owner', 'type': '*mut module'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'id', 'type': '[ffi::c_char; 61usize]'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'read', 'type': '::core::option::Option<'}, {'name': 'write', 'type': '::core::option::Option<'}, {'name': 'read_c45', 'type': '::core::option::Option<'}, {'name': 'write_c45', 'type': '::core::option::Option<'}, {'name': 'reset', 'type': '::core::option::Option<unsafe extern "C" fn(bus: *mut mii_bus) -> ffi::c_int>'}, {'name': 'stats', 'type': '[mdio_bus_stats; 32usize]'}, {'name': 'mdio_lock', 'type': 'mutex'}, {'name': 'parent', 'type': '*mut device'}, {'name': 'state', 'type': 'mii_bus__bindgen_ty_1'}, {'name': 'dev', 'type': 'device'}, {'name': 'mdio_map', 'type': '[*mut mdio_device; 32usize]'}, {'name': 'phy_mask', 'type': 'u32_'}, {'name': 'phy_ignore_ta_mask', 'type': 'u32_'}, {'name': 'irq', 'type': '[ffi::c_int; 32usize]'}, {'name': 'reset_delay_us', 'type': 'ffi::c_int'}, {'name': 'reset_post_delay_us', 'type': 'ffi::c_int'}, {'name': 'reset_gpiod', 'type': '*mut gpio_desc'}, {'name': 'shared_lock', 'type': 'mutex'}, {'name': 'shared', 'type': '[*mut phy_package_shared; 32usize]'}]`

### Rust Evidence

- Graph edges: `6`

## W-000234 FieldDrift

- Risk: Medium
- Score: 9.8
- Symbol: rhashtable
- Explanation: rhashtable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'tbl', 'type': '*mut bucket_table'}, {'name': 'key_len', 'type': 'ffi::c_uint'}, {'name': 'max_elems', 'type': 'ffi::c_uint'}, {'name': 'p', 'type': 'rhashtable_params'}, {'name': 'rhlist', 'type': 'bool_'}, {'name': 'run_work', 'type': 'work_struct'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'nelems', 'type': 'atomic_t'}]`
- New: `[{'name': 'tbl', 'type': '*mut bucket_table'}, {'name': 'key_len', 'type': 'ffi::c_uint'}, {'name': 'max_elems', 'type': 'ffi::c_uint'}, {'name': 'p', 'type': 'rhashtable_params'}, {'name': 'rhlist', 'type': 'bool_'}, {'name': 'run_work', 'type': 'work_struct'}, {'name': 'run_irq_work', 'type': 'irq_work'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'nelems', 'type': 'atomic_t'}]`

### Rust Evidence

- Graph edges: `6`

## W-000237 FieldDrift

- Risk: Medium
- Score: 9.8
- Symbol: sched_domain
- Explanation: sched_domain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'parent', 'type': '*mut sched_domain'}, {'name': 'child', 'type': '*mut sched_domain'}, {'name': 'groups', 'type': '*mut sched_group'}, {'name': 'min_interval', 'type': 'ffi::c_ulong'}, {'name': 'max_interval', 'type': 'ffi::c_ulong'}, {'name': 'busy_factor', 'type': 'ffi::c_uint'}, {'name': 'imbalance_pct', 'type': 'ffi::c_uint'}, {'name': 'cache_nice_tries', 'type': 'ffi::c_uint'}, {'name': 'imb_numa_nr', 'type': 'ffi::c_uint'}, {'name': 'nohz_idle', 'type': 'ffi::c_int'}, {'name': 'flags', 'type': 'ffi::c_int'}, {'name': 'level', 'type': 'ffi::c_int'}, {'name': 'last_balance', 'type': 'ffi::c_ulong'}, {'name': 'balance_interval', 'type': 'ffi::c_uint'}, {'name': 'nr_balance_failed', 'type': 'ffi::c_uint'}, {'name': 'newidle_call', 'type': 'ffi::c_uint'}, {'name': 'newidle_success', 'type': 'ffi::c_uint'}, {'name': 'newidle_ratio', 'type': 'ffi::c_uint'}, {'name': 'max_newidle_lb_cost', 'type': 'u64_'}, {'name': 'last_decay_max_lb_cost', 'type': 'ffi::c_ulong'}, {'name': 'lb_count', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_failed', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_balanced', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_imbalance_load', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_imbalance_util', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_imbalance_task', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_imbalance_misfit', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_gained', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_hot_gained', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_nobusyg', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_nobusyq', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'alb_count', 'type': 'ffi::c_uint'}, {'name': 'alb_failed', 'type': 'ffi::c_uint'}, {'name': 'alb_pushed', 'type': 'ffi::c_uint'}, {'name': 'sbe_count', 'type': 'ffi::c_uint'}, {'name': 'sbe_balanced', 'type': 'ffi::c_uint'}, {'name': 'sbe_pushed', 'type': 'ffi::c_uint'}, {'name': 'sbf_count', 'type': 'ffi::c_uint'}, {'name': 'sbf_balanced', 'type': 'ffi::c_uint'}, {'name': 'sbf_pushed', 'type': 'ffi::c_uint'}, {'name': 'ttwu_wake_remote', 'type': 'ffi::c_uint'}, {'name': 'ttwu_move_affine', 'type': 'ffi::c_uint'}, {'name': 'ttwu_move_balance', 'type': 'ffi::c_uint'}, {'name': 'name', 'type': '*mut ffi::c_char'}, {'name': '__bindgen_anon_1', 'type': 'sched_domain__bindgen_ty_1'}, {'name': 'shared', 'type': '*mut sched_domain_shared'}, {'name': 'span_weight', 'type': 'ffi::c_uint'}, {'name': 'span', 'type': '__IncompleteArrayField<ffi::c_ulong>'}]`
- New: `[{'name': 'parent', 'type': '*mut sched_domain'}, {'name': 'child', 'type': '*mut sched_domain'}, {'name': 'groups', 'type': '*mut sched_group'}, {'name': 'min_interval', 'type': 'ffi::c_ulong'}, {'name': 'max_interval', 'type': 'ffi::c_ulong'}, {'name': 'busy_factor', 'type': 'ffi::c_uint'}, {'name': 'imbalance_pct', 'type': 'ffi::c_uint'}, {'name': 'cache_nice_tries', 'type': 'ffi::c_uint'}, {'name': 'imb_numa_nr', 'type': 'ffi::c_uint'}, {'name': 'nohz_idle', 'type': 'ffi::c_int'}, {'name': 'flags', 'type': 'ffi::c_int'}, {'name': 'level', 'type': 'ffi::c_int'}, {'name': 'last_balance', 'type': 'ffi::c_ulong'}, {'name': 'balance_interval', 'type': 'ffi::c_uint'}, {'name': 'nr_balance_failed', 'type': 'ffi::c_uint'}, {'name': 'newidle_call', 'type': 'ffi::c_uint'}, {'name': 'newidle_success', 'type': 'ffi::c_uint'}, {'name': 'newidle_ratio', 'type': 'ffi::c_uint'}, {'name': 'newidle_stamp', 'type': 'u64_'}, {'name': 'max_newidle_lb_cost', 'type': 'u64_'}, {'name': 'last_decay_max_lb_cost', 'type': 'ffi::c_ulong'}, {'name': 'lb_count', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_failed', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_balanced', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_imbalance_load', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_imbalance_util', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_imbalance_task', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_imbalance_misfit', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_gained', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_hot_gained', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_nobusyg', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_nobusyq', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'alb_count', 'type': 'ffi::c_uint'}, {'name': 'alb_failed', 'type': 'ffi::c_uint'}, {'name': 'alb_pushed', 'type': 'ffi::c_uint'}, {'name': 'sbe_count', 'type': 'ffi::c_uint'}, {'name': 'sbe_balanced', 'type': 'ffi::c_uint'}, {'name': 'sbe_pushed', 'type': 'ffi::c_uint'}, {'name': 'sbf_count', 'type': 'ffi::c_uint'}, {'name': 'sbf_balanced', 'type': 'ffi::c_uint'}, {'name': 'sbf_pushed', 'type': 'ffi::c_uint'}, {'name': 'ttwu_wake_remote', 'type': 'ffi::c_uint'}, {'name': 'ttwu_move_affine', 'type': 'ffi::c_uint'}, {'name': 'ttwu_move_balance', 'type': 'ffi::c_uint'}, {'name': 'name', 'type': '*mut ffi::c_char'}, {'name': '__bindgen_anon_1', 'type': 'sched_domain__bindgen_ty_1'}, {'name': 'shared', 'type': '*mut sched_domain_shared'}, {'name': 'span_weight', 'type': 'ffi::c_uint'}]`

### Rust Evidence

- Graph edges: `6`

## W-000004 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __copy_user_flushcache
- Explanation: __copy_user_flushcache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000005 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __copy_user_nocache
- Explanation: __copy_user_nocache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000006 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __find_nth_andnot_bit
- Explanation: __find_nth_andnot_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000008 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __generic_file_fsync
- Explanation: __generic_file_fsync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000018 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: acpi_install_cmos_rtc_space_handler
- Explanation: acpi_install_cmos_rtc_space_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000020 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: acpi_remove_cmos_rtc_space_handler
- Explanation: acpi_remove_cmos_rtc_space_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000021 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: add_swap_count_continuation
- Explanation: add_swap_count_continuation changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000053 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: destroy_params
- Explanation: destroy_params changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000066 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: dma_buf_move_notify
- Explanation: dma_buf_move_notify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000106 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: generic_file_fsync
- Explanation: generic_file_fsync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000118 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: hang_detected
- Explanation: hang_detected changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000119 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: hres_active
- Explanation: hres_active changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000127 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: in_hrtirq
- Explanation: in_hrtirq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000140 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: may_expand_vm
- Explanation: may_expand_vm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000141 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mdiobus_register_device
- Explanation: mdiobus_register_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000142 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mdiobus_unregister_device
- Explanation: mdiobus_unregister_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000146 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: no_pci_devices
- Explanation: no_pci_devices changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000161 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: reserve_bootmem_region
- Explanation: reserve_bootmem_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000167 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: skb_add_rx_frag_netmem
- Explanation: skb_add_rx_frag_netmem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000169 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: softirq_activated
- Explanation: softirq_activated changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000171 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: subsection_map_init
- Explanation: subsection_map_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000186 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vmemmap_undo_hvo
- Explanation: vmemmap_undo_hvo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000189 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: zap_page_range_single
- Explanation: zap_page_range_single changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000191 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: zap_vma_ptes
- Explanation: zap_vma_ptes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000222 FieldDrift

- Risk: Medium
- Score: 9.6
- Symbol: net_iov
- Explanation: net_iov changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'net_iov__bindgen_ty_1'}, {'name': 'owner', 'type': '*mut net_iov_area'}, {'name': 'type_', 'type': 'net_iov_type'}]`
- New: `[{'name': 'desc', 'type': 'netmem_desc'}, {'name': 'page_type', 'type': 'ffi::c_uint'}, {'name': 'type_', 'type': 'net_iov_type'}, {'name': 'owner', 'type': '*mut net_iov_area'}]`

### Rust Evidence

- Graph edges: `5`

## W-000616 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __mk_vma_flags
- Explanation: __mk_vma_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['size_t count', 'const vma_flag_t *bits'], 'return_type': 'static inline vma_flags_t'}`
- New: `{'params': ['vma_flags_t flags', 'size_t count', 'const vma_flag_t *bits'], 'return_type': 'static __always_inline vma_flags_t'}`

### Rust Evidence

- Graph edges: `0`

## W-000617 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __refcount_add
- Explanation: __refcount_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['int i', 'refcount_t *r', 'int *oldp'], 'return_type': 'static inline __signed_wrap void'}`
- New: `{'params': ['int i', 'refcount_t *r', 'int *oldp'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-000618 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __refcount_add_not_zero
- Explanation: __refcount_add_not_zero changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['int i', 'refcount_t *r', 'int *oldp'], 'return_type': 'static inline __must_check __signed_wrap bool'}`
- New: `{'params': ['int i', 'refcount_t *r', 'int *oldp'], 'return_type': 'static inline __must_check bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000619 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __refcount_add_not_zero_acquire
- Explanation: __refcount_add_not_zero_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['int i', 'refcount_t *r', 'int *oldp'], 'return_type': 'static inline __must_check __signed_wrap bool'}`
- New: `{'params': ['int i', 'refcount_t *r', 'int *oldp'], 'return_type': 'static inline __must_check bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000620 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __refcount_add_not_zero_limited_acquire
- Explanation: __refcount_add_not_zero_limited_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['int i', 'refcount_t *r', 'int *oldp', 'int limit'], 'return_type': 'static inline __must_check __signed_wrap bool'}`
- New: `{'params': ['int i', 'refcount_t *r', 'int *oldp', 'int limit'], 'return_type': 'static inline __must_check bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000623 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __vma_atomic_valid_flag
- Explanation: __vma_atomic_valid_flag changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct vm_area_struct *vma', 'vma_flag_t bit'], 'return_type': 'static inline bool'}`
- New: `{'params': ['struct vm_area_struct *vma', 'vma_flag_t bit'], 'return_type': 'static __always_inline bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000626 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: bitmap_equal
- Explanation: bitmap_equal changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['cpumask_bits(src1p)', 'cpumask_bits(src2p)', 'small_cpumask_bits'], 'return_type': 'return'}`
- New: `{'params': ['bitmap', 'bitmap_other', 'NUM_VMA_FLAG_BITS'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-000631 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_atomic_private_obj_init
- Explanation: drm_atomic_private_obj_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_device *dev', 'struct drm_private_obj *obj', 'struct drm_private_state *state', 'const struct drm_private_state_funcs *funcs'], 'return_type': 'void'}`
- New: `{'params': ['struct drm_device *dev', 'struct drm_private_obj *obj', 'const struct drm_private_state_funcs *funcs'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000632 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_buddy_block_print
- Explanation: drm_buddy_block_print changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_buddy *mm', 'struct drm_buddy_block *block', 'struct drm_printer *p'], 'return_type': 'void'}`
- New: `{'params': ['struct gpu_buddy *mm', 'struct gpu_buddy_block *block', 'struct drm_printer *p'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000633 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_buddy_print
- Explanation: drm_buddy_print changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_buddy *mm', 'struct drm_printer *p'], 'return_type': 'void'}`
- New: `{'params': ['struct gpu_buddy *mm', 'struct drm_printer *p'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000652 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_hdmi_compute_mode_clock
- Explanation: drm_hdmi_compute_mode_clock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct drm_display_mode *mode', 'unsigned int bpc', 'enum hdmi_colorspace fmt'], 'return_type': 'unsigned long long'}`
- New: `{'params': ['const struct drm_display_mode *mode', 'unsigned int bpc', 'enum drm_output_color_format fmt'], 'return_type': 'unsigned long long'}`

### Rust Evidence

- Graph edges: `0`

## W-000653 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_hdmi_connector_get_output_format_name
- Explanation: drm_hdmi_connector_get_output_format_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['enum hdmi_colorspace fmt'], 'return_type': 'const char *'}`
- New: `{'params': ['enum drm_output_color_format fmt'], 'return_type': 'const char *'}`

### Rust Evidence

- Graph edges: `0`

## W-000654 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_plane_colorop_3dlut_init
- Explanation: drm_plane_colorop_3dlut_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_device *dev', 'struct drm_colorop *colorop', 'struct drm_plane *plane', 'uint32_t lut_size', 'enum drm_colorop_lut3d_interpolation_type interpolation', 'uint32_t flags'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_device *dev', 'struct drm_colorop *colorop', 'struct drm_plane *plane', 'const struct drm_colorop_funcs *funcs', 'uint32_t lut_size', 'enum drm_colorop_lut3d_interpolation_type interpolation', 'uint32_t flags'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000655 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_plane_colorop_ctm_3x4_init
- Explanation: drm_plane_colorop_ctm_3x4_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_device *dev', 'struct drm_colorop *colorop', 'struct drm_plane *plane', 'uint32_t flags'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_device *dev', 'struct drm_colorop *colorop', 'struct drm_plane *plane', 'const struct drm_colorop_funcs *funcs', 'uint32_t flags'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000656 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_plane_colorop_curve_1d_init
- Explanation: drm_plane_colorop_curve_1d_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_device *dev', 'struct drm_colorop *colorop', 'struct drm_plane *plane', 'u64 supported_tfs', 'uint32_t flags'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_device *dev', 'struct drm_colorop *colorop', 'struct drm_plane *plane', 'const struct drm_colorop_funcs *funcs', 'u64 supported_tfs', 'uint32_t flags'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000657 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_plane_colorop_curve_1d_lut_init
- Explanation: drm_plane_colorop_curve_1d_lut_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_device *dev', 'struct drm_colorop *colorop', 'struct drm_plane *plane', 'uint32_t lut_size', 'enum drm_colorop_lut1d_interpolation_type interpolation', 'uint32_t flags'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_device *dev', 'struct drm_colorop *colorop', 'struct drm_plane *plane', 'const struct drm_colorop_funcs *funcs', 'uint32_t lut_size', 'enum drm_colorop_lut1d_interpolation_type interpolation', 'uint32_t flags'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000658 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_plane_colorop_mult_init
- Explanation: drm_plane_colorop_mult_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_device *dev', 'struct drm_colorop *colorop', 'struct drm_plane *plane', 'uint32_t flags'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_device *dev', 'struct drm_colorop *colorop', 'struct drm_plane *plane', 'const struct drm_colorop_funcs *funcs', 'uint32_t flags'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000664 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: hweight_long
- Explanation: hweight_long changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['*src1 & ~(*src2) & BITMAP_LAST_WORD_MASK(nbits)'], 'return_type': 'return'}`
- New: `{'params': ['*bitmap & GENMASK(end - 1, start)'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-000681 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: long
- Explanation: long changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['*pagesize)(struct vm_area_struct * area'], 'return_type': 'unsigned'}`
- New: `{'params': ['*pagesize)(struct vm_area_struct *vma'], 'return_type': 'unsigned'}`

### Rust Evidence

- Graph edges: `0`

## W-000688 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: polyval_preparekey
- Explanation: polyval_preparekey changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct polyval_key *key', 'const u8 raw_key[POLYVAL_BLOCK_SIZE]'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct polyval_key *key', 'const u8 raw_key[POLYVAL_BLOCK_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000702 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sm3_init
- Explanation: sm3_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct sm3_state *sctx'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct sm3_ctx *ctx'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000703 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ttm_backup_copy_page
- Explanation: ttm_backup_copy_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct file *backup', 'struct page *dst', 'pgoff_t handle', 'bool intr'], 'return_type': 'int'}`
- New: `{'params': ['struct file *backup', 'struct page *dst', 'pgoff_t handle', 'bool intr', 'gfp_t additional_gfp'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000709 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vma_desc_clear_flags_mask
- Explanation: vma_desc_clear_flags_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct vm_area_desc *desc', 'vma_flags_t flags'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct vm_area_desc *desc', 'vma_flags_t flags'], 'return_type': 'static __always_inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-000710 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vma_desc_set_flags_mask
- Explanation: vma_desc_set_flags_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct vm_area_desc *desc', 'vma_flags_t flags'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct vm_area_desc *desc', 'vma_flags_t flags'], 'return_type': 'static __always_inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-000711 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vma_flags_test
- Explanation: vma_flags_test changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['flags', 'VMA_MAYSHARE_BIT', 'VMA_MAYOVERLAY_BIT'], 'return_type': 'return'}`
- New: `{'params': ['const vma_flags_t *flags', 'vma_flag_t bit'], 'return_type': 'static __always_inline bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000712 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vma_is_dax
- Explanation: vma_is_dax changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['vma) || (vma->vm_file && (vma->vm_flags & (VM_PFNMAP | VM_MIXEDMAP))'], 'return_type': 'return'}`
- New: `{'params': ['const struct vm_area_struct *vma'], 'return_type': 'static inline bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000713 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vma_set_atomic_flag
- Explanation: vma_set_atomic_flag changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct vm_area_struct *vma', 'vma_flag_t bit'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct vm_area_struct *vma', 'vma_flag_t bit'], 'return_type': 'static __always_inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-000714 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vma_set_flags_mask
- Explanation: vma_set_flags_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct vm_area_struct *vma', 'vma_flags_t flags'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct vm_area_struct *vma', 'vma_flags_t flags'], 'return_type': 'static __always_inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-000715 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vma_test_atomic_flag
- Explanation: vma_test_atomic_flag changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct vm_area_struct *vma', 'vma_flag_t bit'], 'return_type': 'static inline bool'}`
- New: `{'params': ['struct vm_area_struct *vma', 'vma_flag_t bit'], 'return_type': 'static __always_inline bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000717 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ww_mutex_is_locked
- Explanation: ww_mutex_is_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['&lock->mutex'], 'return_type': 'return'}`
- New: `{'params': ['&obj->lock'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-000226 FieldDrift

- Risk: Medium
- Score: 9.4
- Symbol: pci_host_bridge
- Explanation: pci_host_bridge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'dev', 'type': 'device'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'ops', 'type': '*mut pci_ops'}, {'name': 'child_ops', 'type': '*mut pci_ops'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'busnr', 'type': 'ffi::c_int'}, {'name': 'domain_nr', 'type': 'ffi::c_int'}, {'name': 'windows', 'type': 'list_head'}, {'name': 'dma_ranges', 'type': 'list_head'}, {'name': 'map_irq', 'type': '::core::option::Option<'}, {'name': 'release_fn', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut pci_host_bridge)>'}, {'name': 'enable_device', 'type': '::core::option::Option<'}, {'name': 'disable_device', 'type': '::core::option::Option<'}, {'name': 'release_data', 'type': '*mut ffi::c_void'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'align_resource', 'type': '::core::option::Option<'}, {'name': '__bindgen_padding_0', 'type': '[u64; 2usize]'}, {'name': 'private', 'type': '__IncompleteArrayField<ffi::c_ulong>'}]`
- New: `[{'name': 'dev', 'type': 'device'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'ops', 'type': '*mut pci_ops'}, {'name': 'child_ops', 'type': '*mut pci_ops'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'busnr', 'type': 'ffi::c_int'}, {'name': 'domain_nr', 'type': 'ffi::c_int'}, {'name': 'windows', 'type': 'list_head'}, {'name': 'dma_ranges', 'type': 'list_head'}, {'name': 'map_irq', 'type': '::core::option::Option<'}, {'name': 'release_fn', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut pci_host_bridge)>'}, {'name': 'enable_device', 'type': '::core::option::Option<'}, {'name': 'disable_device', 'type': '::core::option::Option<'}, {'name': 'release_data', 'type': '*mut ffi::c_void'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'align_resource', 'type': '::core::option::Option<'}, {'name': 'private', 'type': '__IncompleteArrayField<ffi::c_ulong>'}]`

### Rust Evidence

- Graph edges: `4`

## W-000193 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: address_space
- Explanation: address_space changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'host', 'type': '*mut inode'}, {'name': 'i_pages', 'type': 'xarray'}, {'name': 'invalidate_lock', 'type': 'rw_semaphore'}, {'name': 'gfp_mask', 'type': 'gfp_t'}, {'name': 'i_mmap_writable', 'type': 'atomic_t'}, {'name': 'i_mmap', 'type': 'rb_root_cached'}, {'name': 'nrpages', 'type': 'ffi::c_ulong'}, {'name': 'writeback_index', 'type': 'ffi::c_ulong'}, {'name': 'a_ops', 'type': '*const address_space_operations'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'wb_err', 'type': 'errseq_t'}, {'name': 'i_private_lock', 'type': 'spinlock_t'}, {'name': 'i_private_list', 'type': 'list_head'}, {'name': 'i_mmap_rwsem', 'type': 'rw_semaphore'}, {'name': 'i_private_data', 'type': '*mut ffi::c_void'}]`
- New: `[{'name': 'host', 'type': '*mut inode'}, {'name': 'i_pages', 'type': 'xarray'}, {'name': 'invalidate_lock', 'type': 'rw_semaphore'}, {'name': 'gfp_mask', 'type': 'gfp_t'}, {'name': 'i_mmap_writable', 'type': 'atomic_t'}, {'name': 'i_mmap', 'type': 'rb_root_cached'}, {'name': 'nrpages', 'type': 'ffi::c_ulong'}, {'name': 'writeback_index', 'type': 'ffi::c_ulong'}, {'name': 'a_ops', 'type': '*const address_space_operations'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'wb_err', 'type': 'errseq_t'}, {'name': 'i_private_lock', 'type': 'spinlock_t'}, {'name': 'i_mmap_rwsem', 'type': 'rw_semaphore'}]`

### Rust Evidence

- Graph edges: `3`

## W-000196 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: cgroup_file
- Explanation: cgroup_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'kn', 'type': '*mut kernfs_node'}, {'name': 'notified_at', 'type': 'ffi::c_ulong'}, {'name': 'notify_timer', 'type': 'timer_list'}]`
- New: `[{'name': 'kn', 'type': '*mut kernfs_node'}, {'name': 'notified_at', 'type': 'ffi::c_ulong'}, {'name': 'notify_timer', 'type': 'timer_list'}, {'name': 'lock', 'type': 'spinlock_t'}]`

### Rust Evidence

- Graph edges: `3`

## W-000216 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: kunit_try_catch
- Explanation: kunit_try_catch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bindgen_opaque_blob', 'type': '[u64; 6usize]'}]`
- New: `[{'name': 'test', 'type': '*mut kunit'}, {'name': 'try_result', 'type': 'ffi::c_int'}, {'name': 'try_', 'type': 'kunit_try_catch_func_t'}, {'name': 'catch', 'type': 'kunit_try_catch_func_t'}, {'name': 'timeout', 'type': 'ffi::c_ulong'}, {'name': 'context', 'type': '*mut ffi::c_void'}]`

### Rust Evidence

- Graph edges: `3`

## W-000194 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: btf_header
- Explanation: btf_header changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'magic', 'type': '__u16'}, {'name': 'version', 'type': '__u8'}, {'name': 'flags', 'type': '__u8'}, {'name': 'hdr_len', 'type': '__u32'}, {'name': 'type_off', 'type': '__u32'}, {'name': 'type_len', 'type': '__u32'}, {'name': 'str_off', 'type': '__u32'}, {'name': 'str_len', 'type': '__u32'}]`
- New: `[{'name': 'magic', 'type': '__u16'}, {'name': 'version', 'type': '__u8'}, {'name': 'flags', 'type': '__u8'}, {'name': 'hdr_len', 'type': '__u32'}, {'name': 'type_off', 'type': '__u32'}, {'name': 'type_len', 'type': '__u32'}, {'name': 'str_off', 'type': '__u32'}, {'name': 'str_len', 'type': '__u32'}, {'name': 'layout_off', 'type': '__u32'}, {'name': 'layout_len', 'type': '__u32'}]`

### Rust Evidence

- Graph edges: `2`

## W-000208 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: ethtool_rxfh_context
- Explanation: ethtool_rxfh_context changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'indir_size', 'type': 'u32_'}, {'name': 'key_size', 'type': 'u32_'}, {'name': 'priv_size', 'type': 'u16_'}, {'name': 'hfunc', 'type': 'u8_'}, {'name': 'input_xfrm', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'key_off', 'type': 'u32_'}, {'name': '__bindgen_padding_0', 'type': '[u8; 4usize]'}, {'name': 'data', 'type': '__IncompleteArrayField<u8_>'}]`
- New: `[{'name': 'indir_size', 'type': 'u32_'}, {'name': 'key_size', 'type': 'u32_'}, {'name': 'indir_user_size', 'type': 'u32_'}, {'name': 'priv_size', 'type': 'u16_'}, {'name': 'hfunc', 'type': 'u8_'}, {'name': 'input_xfrm', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'key_off', 'type': 'u32_'}, {'name': 'data', 'type': '__IncompleteArrayField<u8_>'}]`

### Rust Evidence

- Graph edges: `2`

## W-000218 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: mm_struct__bindgen_ty_1
- Explanation: mm_struct__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'mm_struct__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mm_mt', 'type': 'maple_tree'}, {'name': 'mmap_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'task_size', 'type': 'ffi::c_ulong'}, {'name': 'pgd', 'type': '*mut pgd_t'}, {'name': 'membarrier_state', 'type': 'atomic_t'}, {'name': 'mm_users', 'type': 'atomic_t'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': 'mm_cid', 'type': 'mm_mm_cid'}, {'name': 'pgtables_bytes', 'type': 'atomic_long_t'}, {'name': 'map_count', 'type': 'ffi::c_int'}, {'name': 'page_table_lock', 'type': 'spinlock_t'}, {'name': 'mmap_lock', 'type': 'rw_semaphore'}, {'name': 'mmlist', 'type': 'list_head'}, {'name': 'vma_writer_wait', 'type': 'rcuwait'}, {'name': 'mm_lock_seq', 'type': 'seqcount_t'}, {'name': 'futex_hash_lock', 'type': 'mutex'}, {'name': 'futex_phash', 'type': '*mut futex_private_hash'}, {'name': 'futex_phash_new', 'type': '*mut futex_private_hash'}, {'name': 'futex_batches', 'type': 'ffi::c_ulong'}, {'name': 'futex_rcu', 'type': 'callback_head'}, {'name': 'futex_atomic', 'type': 'atomic_long_t'}, {'name': 'futex_ref', 'type': '*mut ffi::c_uint'}, {'name': 'hiwater_rss', 'type': 'ffi::c_ulong'}, {'name': 'hiwater_vm', 'type': 'ffi::c_ulong'}, {'name': 'total_vm', 'type': 'ffi::c_ulong'}, {'name': 'locked_vm', 'type': 'ffi::c_ulong'}, {'name': 'pinned_vm', 'type': 'atomic64_t'}, {'name': 'data_vm', 'type': 'ffi::c_ulong'}, {'name': 'exec_vm', 'type': 'ffi::c_ulong'}, {'name': 'stack_vm', 'type': 'ffi::c_ulong'}, {'name': 'def_flags', 'type': 'vm_flags_t'}, {'name': 'write_protect_seq', 'type': 'seqcount_t'}, {'name': 'arg_lock', 'type': 'spinlock_t'}, {'name': 'start_code', 'type': 'ffi::c_ulong'}, {'name': 'end_code', 'type': 'ffi::c_ulong'}, {'name': 'start_data', 'type': 'ffi::c_ulong'}, {'name': 'end_data', 'type': 'ffi::c_ulong'}, {'name': 'start_brk', 'type': 'ffi::c_ulong'}, {'name': 'brk', 'type': 'ffi::c_ulong'}, {'name': 'start_stack', 'type': 'ffi::c_ulong'}, {'name': 'arg_start', 'type': 'ffi::c_ulong'}, {'name': 'arg_end', 'type': 'ffi::c_ulong'}, {'name': 'env_start', 'type': 'ffi::c_ulong'}, {'name': 'env_end', 'type': 'ffi::c_ulong'}, {'name': 'saved_auxv', 'type': '[ffi::c_ulong; 56usize]'}, {'name': 'rss_stat', 'type': '[percpu_counter; 4usize]'}, {'name': 'binfmt', 'type': '*mut linux_binfmt'}, {'name': 'context', 'type': 'mm_context_t'}, {'name': 'flags', 'type': 'mm_flags_t'}, {'name': 'ioctx_lock', 'type': 'spinlock_t'}, {'name': 'ioctx_table', 'type': '*mut kioctx_table'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'exe_file', 'type': '*mut file'}, {'name': 'notifier_subscriptions', 'type': '*mut mmu_notifier_subscriptions'}, {'name': 'tlb_flush_pending', 'type': 'atomic_t'}, {'name': 'tlb_flush_batched', 'type': 'atomic_t'}, {'name': 'uprobes_state', 'type': 'uprobes_state'}, {'name': 'hugetlb_usage', 'type': 'atomic_long_t'}, {'name': 'async_put_work', 'type': 'work_struct'}, {'name': 'iommu_mm', 'type': '*mut iommu_mm_data'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'mm_struct__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mm_mt', 'type': 'maple_tree'}, {'name': 'mmap_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'task_size', 'type': 'ffi::c_ulong'}, {'name': 'pgd', 'type': '*mut pgd_t'}, {'name': 'membarrier_state', 'type': 'atomic_t'}, {'name': 'mm_users', 'type': 'atomic_t'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': 'mm_cid', 'type': 'mm_mm_cid'}, {'name': 'pgtables_bytes', 'type': 'atomic_long_t'}, {'name': 'map_count', 'type': 'ffi::c_int'}, {'name': 'page_table_lock', 'type': 'spinlock_t'}, {'name': 'mmap_lock', 'type': 'rw_semaphore'}, {'name': 'mmlist', 'type': 'list_head'}, {'name': 'vma_writer_wait', 'type': 'rcuwait'}, {'name': 'mm_lock_seq', 'type': 'seqcount_t'}, {'name': 'futex_hash_lock', 'type': 'mutex'}, {'name': 'futex_phash', 'type': '*mut futex_private_hash'}, {'name': 'futex_phash_new', 'type': '*mut futex_private_hash'}, {'name': 'futex_batches', 'type': 'ffi::c_ulong'}, {'name': 'futex_rcu', 'type': 'callback_head'}, {'name': 'futex_atomic', 'type': 'atomic_long_t'}, {'name': 'futex_ref', 'type': '*mut ffi::c_uint'}, {'name': 'hiwater_rss', 'type': 'ffi::c_ulong'}, {'name': 'hiwater_vm', 'type': 'ffi::c_ulong'}, {'name': 'total_vm', 'type': 'ffi::c_ulong'}, {'name': 'locked_vm', 'type': 'ffi::c_ulong'}, {'name': 'pinned_vm', 'type': 'atomic64_t'}, {'name': 'data_vm', 'type': 'ffi::c_ulong'}, {'name': 'exec_vm', 'type': 'ffi::c_ulong'}, {'name': 'stack_vm', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_2', 'type': 'mm_struct__bindgen_ty_1__bindgen_ty_2'}, {'name': 'write_protect_seq', 'type': 'seqcount_t'}, {'name': 'arg_lock', 'type': 'spinlock_t'}, {'name': 'start_code', 'type': 'ffi::c_ulong'}, {'name': 'end_code', 'type': 'ffi::c_ulong'}, {'name': 'start_data', 'type': 'ffi::c_ulong'}, {'name': 'end_data', 'type': 'ffi::c_ulong'}, {'name': 'start_brk', 'type': 'ffi::c_ulong'}, {'name': 'brk', 'type': 'ffi::c_ulong'}, {'name': 'start_stack', 'type': 'ffi::c_ulong'}, {'name': 'arg_start', 'type': 'ffi::c_ulong'}, {'name': 'arg_end', 'type': 'ffi::c_ulong'}, {'name': 'env_start', 'type': 'ffi::c_ulong'}, {'name': 'env_end', 'type': 'ffi::c_ulong'}, {'name': 'saved_auxv', 'type': '[ffi::c_ulong; 56usize]'}, {'name': 'rss_stat', 'type': '[percpu_counter; 4usize]'}, {'name': 'binfmt', 'type': '*mut linux_binfmt'}, {'name': 'context', 'type': 'mm_context_t'}, {'name': 'flags', 'type': 'mm_flags_t'}, {'name': 'ioctx_lock', 'type': 'spinlock_t'}, {'name': 'ioctx_table', 'type': '*mut kioctx_table'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'exe_file', 'type': '*mut file'}, {'name': 'notifier_subscriptions', 'type': '*mut mmu_notifier_subscriptions'}, {'name': 'tlb_flush_pending', 'type': 'atomic_t'}, {'name': 'tlb_flush_batched', 'type': 'atomic_t'}, {'name': 'uprobes_state', 'type': 'uprobes_state'}, {'name': 'hugetlb_usage', 'type': 'atomic_long_t'}, {'name': 'async_put_work', 'type': 'work_struct'}, {'name': 'iommu_mm', 'type': '*mut iommu_mm_data'}]`

### Rust Evidence

- Graph edges: `2`

## W-000240 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: semaphore
- Explanation: semaphore changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'lock', 'type': 'raw_spinlock_t'}, {'name': 'count', 'type': 'ffi::c_uint'}, {'name': 'wait_list', 'type': 'list_head'}]`
- New: `[{'name': 'lock', 'type': 'raw_spinlock_t'}, {'name': 'count', 'type': 'ffi::c_uint'}, {'name': 'first_waiter', 'type': '*mut semaphore_waiter'}]`

### Rust Evidence

- Graph edges: `2`

## W-000202 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: dma_buf_attach_ops
- Explanation: dma_buf_attach_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'allow_peer2peer', 'type': 'bool_'}, {'name': 'move_notify', 'type': '::core::option::Option<unsafe extern "C" fn(attach: *mut dma_buf_attachment)>'}]`
- New: `[{'name': 'allow_peer2peer', 'type': 'bool_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000205 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: ethtool_netdev_state
- Explanation: ethtool_netdev_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'rss_ctx', 'type': 'xarray'}, {'name': 'rss_lock', 'type': 'mutex'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 7usize]'}]`
- New: `[{'name': 'rss_ctx', 'type': 'xarray'}, {'name': 'rss_lock', 'type': 'mutex'}, {'name': 'rss_indir_user_size', 'type': 'u32_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 3usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000206 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: ethtool_pause_stats__bindgen_ty_1__bindgen_ty_1
- Explanation: ethtool_pause_stats__bindgen_ty_1__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'tx_pause_frames', 'type': 'u64_'}, {'name': 'rx_pause_frames', 'type': 'u64_'}]`
- New: `[{'name': 'tx_pause_frames', 'type': 'u64_'}, {'name': 'rx_pause_frames', 'type': 'u64_'}, {'name': 'tx_pause_storm_events', 'type': 'u64_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000207 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: ethtool_pause_stats__bindgen_ty_1__bindgen_ty_2
- Explanation: ethtool_pause_stats__bindgen_ty_1__bindgen_ty_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'tx_pause_frames', 'type': 'u64_'}, {'name': 'rx_pause_frames', 'type': 'u64_'}]`
- New: `[{'name': 'tx_pause_frames', 'type': 'u64_'}, {'name': 'rx_pause_frames', 'type': 'u64_'}, {'name': 'tx_pause_storm_events', 'type': 'u64_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000211 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: hrtimer_clock_base
- Explanation: hrtimer_clock_base changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'cpu_base', 'type': '*mut hrtimer_cpu_base'}, {'name': 'index', 'type': 'ffi::c_uint'}, {'name': 'clockid', 'type': 'clockid_t'}, {'name': 'seq', 'type': 'seqcount_raw_spinlock_t'}, {'name': 'running', 'type': '*mut hrtimer'}, {'name': 'active', 'type': 'timerqueue_head'}, {'name': 'offset', 'type': 'ktime_t'}]`
- New: `[{'name': 'cpu_base', 'type': '*mut hrtimer_cpu_base'}, {'name': 'index', 'type': 'ffi::c_uint'}, {'name': 'clockid', 'type': 'clockid_t'}, {'name': 'seq', 'type': 'seqcount_raw_spinlock_t'}, {'name': 'expires_next', 'type': 'ktime_t'}, {'name': 'running', 'type': '*mut hrtimer'}, {'name': 'active', 'type': 'timerqueue_linked_head'}, {'name': 'offset', 'type': 'ktime_t'}]`

### Rust Evidence

- Graph edges: `1`

## W-000212 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: hrtimer_cpu_base
- Explanation: hrtimer_cpu_base changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'lock', 'type': 'raw_spinlock_t'}, {'name': 'cpu', 'type': 'ffi::c_uint'}, {'name': 'active_bases', 'type': 'ffi::c_uint'}, {'name': 'clock_was_set_seq', 'type': 'ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'nr_events', 'type': 'ffi::c_uint'}, {'name': 'nr_retries', 'type': 'ffi::c_ushort'}, {'name': 'nr_hangs', 'type': 'ffi::c_ushort'}, {'name': 'max_hang_time', 'type': 'ffi::c_uint'}, {'name': 'expires_next', 'type': 'ktime_t'}, {'name': 'next_timer', 'type': '*mut hrtimer'}, {'name': 'softirq_expires_next', 'type': 'ktime_t'}, {'name': 'softirq_next_timer', 'type': '*mut hrtimer'}, {'name': 'clock_base', 'type': '[hrtimer_clock_base; 8usize]'}, {'name': 'csd', 'type': 'call_single_data_t'}]`
- New: `[{'name': 'lock', 'type': 'raw_spinlock_t'}, {'name': 'cpu', 'type': 'ffi::c_uint'}, {'name': 'active_bases', 'type': 'ffi::c_uint'}, {'name': 'clock_was_set_seq', 'type': 'ffi::c_uint'}, {'name': 'hres_active', 'type': 'bool_'}, {'name': 'deferred_rearm', 'type': 'bool_'}, {'name': 'deferred_needs_update', 'type': 'bool_'}, {'name': 'hang_detected', 'type': 'bool_'}, {'name': 'softirq_activated', 'type': 'bool_'}, {'name': 'online', 'type': 'bool_'}, {'name': 'nr_events', 'type': 'ffi::c_uint'}, {'name': 'nr_retries', 'type': 'ffi::c_ushort'}, {'name': 'nr_hangs', 'type': 'ffi::c_ushort'}, {'name': 'max_hang_time', 'type': 'ffi::c_uint'}, {'name': 'expires_next', 'type': 'ktime_t'}, {'name': 'next_timer', 'type': '*mut hrtimer'}, {'name': 'softirq_expires_next', 'type': 'ktime_t'}, {'name': 'softirq_next_timer', 'type': '*mut hrtimer'}, {'name': 'deferred_expires_next', 'type': 'ktime_t'}, {'name': '__bindgen_padding_0', 'type': '[u64; 6usize]'}, {'name': 'clock_base', 'type': '[hrtimer_clock_base; 8usize]'}, {'name': 'csd', 'type': 'call_single_data_t'}]`

### Rust Evidence

- Graph edges: `1`

## W-000215 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: kernel_ethtool_coalesce
- Explanation: kernel_ethtool_coalesce changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'use_cqe_mode_tx', 'type': 'u8_'}, {'name': 'use_cqe_mode_rx', 'type': 'u8_'}, {'name': 'tx_aggr_max_bytes', 'type': 'u32_'}, {'name': 'tx_aggr_max_frames', 'type': 'u32_'}, {'name': 'tx_aggr_time_usecs', 'type': 'u32_'}]`
- New: `[{'name': 'use_cqe_mode_tx', 'type': 'u8_'}, {'name': 'use_cqe_mode_rx', 'type': 'u8_'}, {'name': 'tx_aggr_max_bytes', 'type': 'u32_'}, {'name': 'tx_aggr_max_frames', 'type': 'u32_'}, {'name': 'tx_aggr_time_usecs', 'type': 'u32_'}, {'name': 'rx_cqe_frames', 'type': 'u32_'}, {'name': 'rx_cqe_nsecs', 'type': 'u32_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000219 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: mmu_interval_notifier_ops
- Explanation: mmu_interval_notifier_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'invalidate', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'invalidate', 'type': '::core::option::Option<'}, {'name': 'invalidate_start', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-000223 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: page__bindgen_ty_1__bindgen_ty_3
- Explanation: page__bindgen_ty_1__bindgen_ty_3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'compound_head', 'type': 'ffi::c_ulong'}]`
- New: `[{'name': 'compound_info', 'type': 'ffi::c_ulong'}]`

### Rust Evidence

- Graph edges: `1`

## W-000224 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: page__bindgen_ty_1__bindgen_ty_4
- Explanation: page__bindgen_ty_1__bindgen_ty_4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_unused_pgmap_compound_head', 'type': '*mut ffi::c_void'}, {'name': 'zone_device_data', 'type': '*mut ffi::c_void'}]`
- New: `[{'name': '_unused_pgmap_compound_info', 'type': '*mut ffi::c_void'}, {'name': 'zone_device_data', 'type': '*mut ffi::c_void'}]`

### Rust Evidence

- Graph edges: `1`

## W-000227 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: per_cpu_nodestat
- Explanation: per_cpu_nodestat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'stat_threshold', 'type': 's8'}, {'name': 'vm_node_stat_diff', 'type': '[s8; 48usize]'}]`
- New: `[{'name': 'stat_threshold', 'type': 's8'}, {'name': 'vm_node_stat_diff', 'type': '[s8; 64usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000228 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: pglist_data
- Explanation: pglist_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'node_zones', 'type': '[zone; 4usize]'}, {'name': 'node_zonelists', 'type': '[zonelist; 2usize]'}, {'name': 'nr_zones', 'type': 'ffi::c_int'}, {'name': 'node_start_pfn', 'type': 'ffi::c_ulong'}, {'name': 'node_present_pages', 'type': 'ffi::c_ulong'}, {'name': 'node_spanned_pages', 'type': 'ffi::c_ulong'}, {'name': 'node_id', 'type': 'ffi::c_int'}, {'name': 'kswapd_wait', 'type': 'wait_queue_head_t'}, {'name': 'pfmemalloc_wait', 'type': 'wait_queue_head_t'}, {'name': 'reclaim_wait', 'type': '[wait_queue_head_t; 4usize]'}, {'name': 'nr_writeback_throttled', 'type': 'atomic_t'}, {'name': 'nr_reclaim_start', 'type': 'ffi::c_ulong'}, {'name': 'kswapd', 'type': '*mut task_struct'}, {'name': 'kswapd_order', 'type': 'ffi::c_int'}, {'name': 'kswapd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kswapd_failures', 'type': 'atomic_t'}, {'name': 'kcompactd_max_order', 'type': 'ffi::c_int'}, {'name': 'kcompactd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kcompactd_wait', 'type': 'wait_queue_head_t'}, {'name': 'kcompactd', 'type': '*mut task_struct'}, {'name': 'proactive_compact_trigger', 'type': 'bool_'}, {'name': 'totalreserve_pages', 'type': 'ffi::c_ulong'}, {'name': 'min_unmapped_pages', 'type': 'ffi::c_ulong'}, {'name': 'min_slab_pages', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': '__lruvec', 'type': 'lruvec'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_padding_1', 'type': '[u64; 6usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'per_cpu_nodestats', 'type': '*mut per_cpu_nodestat'}, {'name': 'vm_stat', 'type': '[atomic_long_t; 48usize]'}, {'name': 'memtier', 'type': '*mut memory_tier'}]`
- New: `[{'name': 'node_zones', 'type': '[zone; 4usize]'}, {'name': 'node_zonelists', 'type': '[zonelist; 2usize]'}, {'name': 'nr_zones', 'type': 'ffi::c_int'}, {'name': 'node_start_pfn', 'type': 'ffi::c_ulong'}, {'name': 'node_present_pages', 'type': 'ffi::c_ulong'}, {'name': 'node_spanned_pages', 'type': 'ffi::c_ulong'}, {'name': 'node_id', 'type': 'ffi::c_int'}, {'name': 'kswapd_wait', 'type': 'wait_queue_head_t'}, {'name': 'pfmemalloc_wait', 'type': 'wait_queue_head_t'}, {'name': 'reclaim_wait', 'type': '[wait_queue_head_t; 4usize]'}, {'name': 'nr_writeback_throttled', 'type': 'atomic_t'}, {'name': 'nr_reclaim_start', 'type': 'ffi::c_ulong'}, {'name': 'kswapd', 'type': '*mut task_struct'}, {'name': 'kswapd_order', 'type': 'ffi::c_int'}, {'name': 'kswapd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kswapd_failures', 'type': 'atomic_t'}, {'name': 'kcompactd_max_order', 'type': 'ffi::c_int'}, {'name': 'kcompactd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kcompactd_wait', 'type': 'wait_queue_head_t'}, {'name': 'kcompactd', 'type': '*mut task_struct'}, {'name': 'proactive_compact_trigger', 'type': 'bool_'}, {'name': 'totalreserve_pages', 'type': 'ffi::c_ulong'}, {'name': 'min_unmapped_pages', 'type': 'ffi::c_ulong'}, {'name': 'min_slab_pages', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': '__lruvec', 'type': 'lruvec'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_padding_1', 'type': '[u64; 6usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'per_cpu_nodestats', 'type': '*mut per_cpu_nodestat'}, {'name': 'vm_stat', 'type': '[atomic_long_t; 64usize]'}, {'name': 'memtier', 'type': '*mut memory_tier'}]`

### Rust Evidence

- Graph edges: `1`

## W-000230 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: platform_device_info
- Explanation: platform_device_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'parent', 'type': '*mut device'}, {'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'of_node_reused', 'type': 'bool_'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'res', 'type': '*const resource'}, {'name': 'num_res', 'type': 'ffi::c_uint'}, {'name': 'data', 'type': '*const ffi::c_void'}, {'name': 'size_data', 'type': 'usize'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'properties', 'type': '*const property_entry'}]`
- New: `[{'name': 'parent', 'type': '*mut device'}, {'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'of_node_reused', 'type': 'bool_'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'res', 'type': '*const resource'}, {'name': 'num_res', 'type': 'ffi::c_uint'}, {'name': 'data', 'type': '*const ffi::c_void'}, {'name': 'size_data', 'type': 'usize'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'swnode', 'type': '*const software_node'}, {'name': 'properties', 'type': '*const property_entry'}]`

### Rust Evidence

- Graph edges: `1`

## W-000231 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: proto_ops
- Explanation: proto_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'family', 'type': 'ffi::c_int'}, {'name': 'owner', 'type': '*mut module'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(sock: *mut socket) -> ffi::c_int>'}, {'name': 'bind', 'type': '::core::option::Option<'}, {'name': 'connect', 'type': '::core::option::Option<'}, {'name': 'socketpair', 'type': '::core::option::Option<'}, {'name': 'accept', 'type': '::core::option::Option<'}, {'name': 'getname', 'type': '::core::option::Option<'}, {'name': 'poll', 'type': '::core::option::Option<'}, {'name': 'ioctl', 'type': '::core::option::Option<'}, {'name': 'compat_ioctl', 'type': '::core::option::Option<'}, {'name': 'gettstamp', 'type': '::core::option::Option<'}, {'name': 'listen', 'type': '::core::option::Option<'}, {'name': 'shutdown', 'type': '::core::option::Option<'}, {'name': 'setsockopt', 'type': '::core::option::Option<'}, {'name': 'getsockopt', 'type': '::core::option::Option<'}, {'name': 'sendmsg', 'type': '::core::option::Option<'}, {'name': 'recvmsg', 'type': '::core::option::Option<'}, {'name': 'mmap', 'type': '::core::option::Option<'}, {'name': 'splice_read', 'type': '::core::option::Option<'}, {'name': 'splice_eof', 'type': '::core::option::Option<unsafe extern "C" fn(sock: *mut socket)>'}, {'name': 'peek_len', 'type': '::core::option::Option<unsafe extern "C" fn(sock: *mut socket) -> ffi::c_int>'}, {'name': 'read_sock', 'type': '::core::option::Option<'}, {'name': 'read_skb', 'type': '::core::option::Option<'}, {'name': 'sendmsg_locked', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'family', 'type': 'ffi::c_int'}, {'name': 'owner', 'type': '*mut module'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(sock: *mut socket) -> ffi::c_int>'}, {'name': 'bind', 'type': '::core::option::Option<'}, {'name': 'connect', 'type': '::core::option::Option<'}, {'name': 'socketpair', 'type': '::core::option::Option<'}, {'name': 'accept', 'type': '::core::option::Option<'}, {'name': 'getname', 'type': '::core::option::Option<'}, {'name': 'poll', 'type': '::core::option::Option<'}, {'name': 'ioctl', 'type': '::core::option::Option<'}, {'name': 'compat_ioctl', 'type': '::core::option::Option<'}, {'name': 'gettstamp', 'type': '::core::option::Option<'}, {'name': 'listen', 'type': '::core::option::Option<'}, {'name': 'shutdown', 'type': '::core::option::Option<'}, {'name': 'setsockopt', 'type': '::core::option::Option<'}, {'name': 'getsockopt', 'type': '::core::option::Option<'}, {'name': 'getsockopt_iter', 'type': '::core::option::Option<'}, {'name': 'sendmsg', 'type': '::core::option::Option<'}, {'name': 'recvmsg', 'type': '::core::option::Option<'}, {'name': 'mmap', 'type': '::core::option::Option<'}, {'name': 'splice_read', 'type': '::core::option::Option<'}, {'name': 'splice_eof', 'type': '::core::option::Option<unsafe extern "C" fn(sock: *mut socket)>'}, {'name': 'peek_len', 'type': '::core::option::Option<unsafe extern "C" fn(sock: *mut socket) -> ffi::c_int>'}, {'name': 'read_sock', 'type': '::core::option::Option<'}, {'name': 'read_skb', 'type': '::core::option::Option<'}, {'name': 'sendmsg_locked', 'type': '::core::option::Option<'}, {'name': 'set_rcvbuf', 'type': '::core::option::Option<unsafe extern "C" fn(sk: *mut sock'}]`

### Rust Evidence

- Graph edges: `1`

## W-000232 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: pv_cpu_ops
- Explanation: pv_cpu_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'io_delay', 'type': '::core::option::Option<unsafe extern "C" fn()>'}]`
- New: `[]`

### Rust Evidence

- Graph edges: `1`

## W-000233 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: pv_info
- Explanation: pv_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'name', 'type': '*const ffi::c_char'}]`
- New: `[{'name': 'io_delay', 'type': 'bool_'}, {'name': 'name', 'type': '*const ffi::c_char'}]`

### Rust Evidence

- Graph edges: `1`

## W-000235 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: rhashtable_params
- Explanation: rhashtable_params changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'nelem_hint', 'type': 'u16_'}, {'name': 'key_len', 'type': 'u16_'}, {'name': 'key_offset', 'type': 'u16_'}, {'name': 'head_offset', 'type': 'u16_'}, {'name': 'max_size', 'type': 'ffi::c_uint'}, {'name': 'min_size', 'type': 'u16_'}, {'name': 'automatic_shrinking', 'type': 'bool_'}, {'name': 'hashfn', 'type': 'rht_hashfn_t'}, {'name': 'obj_hashfn', 'type': 'rht_obj_hashfn_t'}, {'name': 'obj_cmpfn', 'type': 'rht_obj_cmpfn_t'}]`
- New: `[{'name': 'nelem_hint', 'type': 'u16_'}, {'name': 'key_len', 'type': 'u16_'}, {'name': 'key_offset', 'type': 'u16_'}, {'name': 'head_offset', 'type': 'u16_'}, {'name': 'max_size', 'type': 'ffi::c_uint'}, {'name': 'min_size', 'type': 'u16_'}, {'name': 'insecure_elasticity', 'type': 'bool_'}, {'name': 'automatic_shrinking', 'type': 'bool_'}, {'name': 'hashfn', 'type': 'rht_hashfn_t'}, {'name': 'obj_hashfn', 'type': 'rht_obj_hashfn_t'}, {'name': 'obj_cmpfn', 'type': 'rht_obj_cmpfn_t'}]`

### Rust Evidence

- Graph edges: `1`

## W-000236 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: rw_semaphore
- Explanation: rw_semaphore changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'count', 'type': 'atomic_long_t'}, {'name': 'owner', 'type': 'atomic_long_t'}, {'name': 'osq', 'type': 'optimistic_spin_queue'}, {'name': 'wait_lock', 'type': 'raw_spinlock_t'}, {'name': 'wait_list', 'type': 'list_head'}]`
- New: `[{'name': 'count', 'type': 'atomic_long_t'}, {'name': 'owner', 'type': 'atomic_long_t'}, {'name': 'osq', 'type': 'optimistic_spin_queue'}, {'name': 'wait_lock', 'type': 'raw_spinlock_t'}, {'name': 'first_waiter', 'type': '*mut rwsem_waiter'}]`

### Rust Evidence

- Graph edges: `1`

## W-000238 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: scm_timestamping_internal
- Explanation: scm_timestamping_internal changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'ts', 'type': '[timespec64; 3usize]'}]`
- New: `[{'name': 'ts', 'type': '[ktime_t; 3usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000239 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: sd_data
- Explanation: sd_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'sd', 'type': '*mut *mut sched_domain'}, {'name': 'sds', 'type': '*mut *mut sched_domain_shared'}, {'name': 'sg', 'type': '*mut *mut sched_group'}, {'name': 'sgc', 'type': '*mut *mut sched_group_capacity'}]`
- New: `[{'name': 'sd', 'type': '*mut *mut sched_domain'}, {'name': 'sg', 'type': '*mut *mut sched_group'}, {'name': 'sgc', 'type': '*mut *mut sched_group_capacity'}]`

### Rust Evidence

- Graph edges: `1`

## W-000241 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: super_block
- Explanation: super_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 's_list', 'type': 'list_head'}, {'name': 's_dev', 'type': 'dev_t'}, {'name': 's_blocksize_bits', 'type': 'ffi::c_uchar'}, {'name': 's_blocksize', 'type': 'ffi::c_ulong'}, {'name': 's_maxbytes', 'type': 'loff_t'}, {'name': 's_type', 'type': '*mut file_system_type'}, {'name': 's_op', 'type': '*const super_operations'}, {'name': 'dq_op', 'type': '*const dquot_operations'}, {'name': 's_qcop', 'type': '*const quotactl_ops'}, {'name': 's_export_op', 'type': '*const export_operations'}, {'name': 's_flags', 'type': 'ffi::c_ulong'}, {'name': 's_iflags', 'type': 'ffi::c_ulong'}, {'name': 's_magic', 'type': 'ffi::c_ulong'}, {'name': 's_root', 'type': '*mut dentry'}, {'name': 's_umount', 'type': 'rw_semaphore'}, {'name': 's_count', 'type': 'ffi::c_int'}, {'name': 's_active', 'type': 'atomic_t'}, {'name': 's_security', 'type': '*mut ffi::c_void'}, {'name': 's_xattr', 'type': '*const *const xattr_handler'}, {'name': 's_roots', 'type': 'hlist_bl_head'}, {'name': 's_mounts', 'type': '*mut mount'}, {'name': 's_bdev', 'type': '*mut block_device'}, {'name': 's_bdev_file', 'type': '*mut file'}, {'name': 's_bdi', 'type': '*mut backing_dev_info'}, {'name': 's_mtd', 'type': '*mut mtd_info'}, {'name': 's_instances', 'type': 'hlist_node'}, {'name': 's_quota_types', 'type': 'ffi::c_uint'}, {'name': 's_dquot', 'type': 'quota_info'}, {'name': 's_writers', 'type': 'sb_writers'}, {'name': 's_fs_info', 'type': '*mut ffi::c_void'}, {'name': 's_time_gran', 'type': 'u32_'}, {'name': 's_time_min', 'type': 'time64_t'}, {'name': 's_time_max', 'type': 'time64_t'}, {'name': 's_fsnotify_mask', 'type': 'u32_'}, {'name': 's_fsnotify_info', 'type': '*mut fsnotify_sb_info'}, {'name': 's_id', 'type': '[ffi::c_char; 32usize]'}, {'name': 's_uuid', 'type': 'uuid_t'}, {'name': 's_uuid_len', 'type': 'u8_'}, {'name': 's_sysfs_name', 'type': '[ffi::c_char; 37usize]'}, {'name': 's_max_links', 'type': 'ffi::c_uint'}, {'name': 's_d_flags', 'type': 'ffi::c_uint'}, {'name': 's_vfs_rename_mutex', 'type': 'mutex'}, {'name': 's_subtype', 'type': '*const ffi::c_char'}, {'name': '__s_d_op', 'type': '*const dentry_operations'}, {'name': 's_shrink', 'type': '*mut shrinker'}, {'name': 's_remove_count', 'type': 'atomic_long_t'}, {'name': 's_readonly_remount', 'type': 'ffi::c_int'}, {'name': 's_wb_err', 'type': 'errseq_t'}, {'name': 's_dio_done_wq', 'type': '*mut workqueue_struct'}, {'name': 's_pins', 'type': 'hlist_head'}, {'name': 's_user_ns', 'type': '*mut user_namespace'}, {'name': 's_dentry_lru', 'type': 'list_lru'}, {'name': 's_inode_lru', 'type': 'list_lru'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 's_sync_lock', 'type': 'mutex'}, {'name': 's_stack_depth', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': 'u32'}, {'name': 's_inode_list_lock', 'type': 'spinlock_t'}, {'name': 's_inodes', 'type': 'list_head'}, {'name': 's_inode_wblist_lock', 'type': 'spinlock_t'}, {'name': 's_inodes_wb', 'type': 'list_head'}, {'name': 's_min_writeback_pages', 'type': 'ffi::c_long'}, {'name': 's_pending_errors', 'type': 'refcount_t'}]`
- New: `[{'name': 's_list', 'type': 'list_head'}, {'name': 's_dev', 'type': 'dev_t'}, {'name': 's_blocksize_bits', 'type': 'ffi::c_uchar'}, {'name': 's_blocksize', 'type': 'ffi::c_ulong'}, {'name': 's_maxbytes', 'type': 'loff_t'}, {'name': 's_type', 'type': '*mut file_system_type'}, {'name': 's_op', 'type': '*const super_operations'}, {'name': 'dq_op', 'type': '*const dquot_operations'}, {'name': 's_qcop', 'type': '*const quotactl_ops'}, {'name': 's_export_op', 'type': '*const export_operations'}, {'name': 's_flags', 'type': 'ffi::c_ulong'}, {'name': 's_iflags', 'type': 'ffi::c_ulong'}, {'name': 's_magic', 'type': 'ffi::c_ulong'}, {'name': 's_root', 'type': '*mut dentry'}, {'name': 's_umount', 'type': 'rw_semaphore'}, {'name': 's_count', 'type': 'ffi::c_int'}, {'name': 's_active', 'type': 'atomic_t'}, {'name': 's_security', 'type': '*mut ffi::c_void'}, {'name': 's_xattr', 'type': '*const *const xattr_handler'}, {'name': 's_roots', 'type': 'hlist_bl_head'}, {'name': 's_mounts', 'type': '*mut mount'}, {'name': 's_bdev', 'type': '*mut block_device'}, {'name': 's_bdev_file', 'type': '*mut file'}, {'name': 's_bdi', 'type': '*mut backing_dev_info'}, {'name': 's_mtd', 'type': '*mut mtd_info'}, {'name': 's_instances', 'type': 'hlist_node'}, {'name': 's_quota_types', 'type': 'ffi::c_uint'}, {'name': 's_dquot', 'type': 'quota_info'}, {'name': 's_writers', 'type': 'sb_writers'}, {'name': 's_fs_info', 'type': '*mut ffi::c_void'}, {'name': 's_time_gran', 'type': 'u32_'}, {'name': 's_time_min', 'type': 'time64_t'}, {'name': 's_time_max', 'type': 'time64_t'}, {'name': 's_fsnotify_mask', 'type': 'u32_'}, {'name': 's_fsnotify_info', 'type': '*mut fsnotify_sb_info'}, {'name': 's_id', 'type': '[ffi::c_char; 32usize]'}, {'name': 's_uuid', 'type': 'uuid_t'}, {'name': 's_uuid_len', 'type': 'u8_'}, {'name': 's_sysfs_name', 'type': '[ffi::c_char; 37usize]'}, {'name': 's_max_links', 'type': 'ffi::c_uint'}, {'name': 's_d_flags', 'type': 'ffi::c_uint'}, {'name': 's_vfs_rename_mutex', 'type': 'mutex'}, {'name': 's_subtype', 'type': '*const ffi::c_char'}, {'name': '__s_d_op', 'type': '*const dentry_operations'}, {'name': 's_shrink', 'type': '*mut shrinker'}, {'name': 's_remove_count', 'type': 'atomic_long_t'}, {'name': 's_readonly_remount', 'type': 'ffi::c_int'}, {'name': 's_wb_err', 'type': 'errseq_t'}, {'name': 's_dio_done_wq', 'type': '*mut workqueue_struct'}, {'name': 's_pins', 'type': 'hlist_head'}, {'name': 's_user_ns', 'type': '*mut user_namespace'}, {'name': 's_dentry_lru', 'type': 'list_lru'}, {'name': 's_inode_lru', 'type': 'list_lru'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 's_sync_lock', 'type': 'mutex'}, {'name': 's_stack_depth', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': '[u32; 9usize]'}, {'name': 's_inode_list_lock', 'type': 'spinlock_t'}, {'name': 's_inodes', 'type': 'list_head'}, {'name': 's_inode_wblist_lock', 'type': 'spinlock_t'}, {'name': 's_inodes_wb', 'type': 'list_head'}, {'name': 's_min_writeback_pages', 'type': 'ffi::c_long'}, {'name': 's_pending_errors', 'type': 'refcount_t'}]`

### Rust Evidence

- Graph edges: `1`

## W-000242 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: swap_info_struct
- Explanation: swap_info_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'users', 'type': 'percpu_ref'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'prio', 'type': 'ffi::c_short'}, {'name': 'list', 'type': 'plist_node'}, {'name': 'type_', 'type': 'ffi::c_schar'}, {'name': 'max', 'type': 'ffi::c_uint'}, {'name': 'swap_map', 'type': '*mut ffi::c_uchar'}, {'name': 'zeromap', 'type': '*mut ffi::c_ulong'}, {'name': 'cluster_info', 'type': '*mut swap_cluster_info'}, {'name': 'free_clusters', 'type': 'list_head'}, {'name': 'full_clusters', 'type': 'list_head'}, {'name': 'nonfull_clusters', 'type': '[list_head; 1usize]'}, {'name': 'frag_clusters', 'type': '[list_head; 1usize]'}, {'name': 'pages', 'type': 'ffi::c_uint'}, {'name': 'inuse_pages', 'type': 'atomic_long_t'}, {'name': 'global_cluster', 'type': '*mut swap_sequential_cluster'}, {'name': 'global_cluster_lock', 'type': 'spinlock_t'}, {'name': 'swap_extent_root', 'type': 'rb_root'}, {'name': 'bdev', 'type': '*mut block_device'}, {'name': 'swap_file', 'type': '*mut file'}, {'name': 'comp', 'type': 'completion'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'cont_lock', 'type': 'spinlock_t'}, {'name': 'discard_work', 'type': 'work_struct'}, {'name': 'reclaim_work', 'type': 'work_struct'}, {'name': 'discard_clusters', 'type': 'list_head'}, {'name': 'avail_list', 'type': 'plist_node'}]`
- New: `[{'name': 'users', 'type': 'percpu_ref'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'prio', 'type': 'ffi::c_short'}, {'name': 'list', 'type': 'plist_node'}, {'name': 'type_', 'type': 'ffi::c_schar'}, {'name': 'max', 'type': 'ffi::c_uint'}, {'name': 'zeromap', 'type': '*mut ffi::c_ulong'}, {'name': 'cluster_info', 'type': '*mut swap_cluster_info'}, {'name': 'free_clusters', 'type': 'list_head'}, {'name': 'full_clusters', 'type': 'list_head'}, {'name': 'nonfull_clusters', 'type': '[list_head; 1usize]'}, {'name': 'frag_clusters', 'type': '[list_head; 1usize]'}, {'name': 'pages', 'type': 'ffi::c_uint'}, {'name': 'inuse_pages', 'type': 'atomic_long_t'}, {'name': 'global_cluster', 'type': '*mut swap_sequential_cluster'}, {'name': 'global_cluster_lock', 'type': 'spinlock_t'}, {'name': 'swap_extent_root', 'type': 'rb_root'}, {'name': 'bdev', 'type': '*mut block_device'}, {'name': 'swap_file', 'type': '*mut file'}, {'name': 'comp', 'type': 'completion'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'discard_work', 'type': 'work_struct'}, {'name': 'reclaim_work', 'type': 'work_struct'}, {'name': 'discard_clusters', 'type': 'list_head'}, {'name': 'avail_list', 'type': 'plist_node'}]`

### Rust Evidence

- Graph edges: `1`

## W-000244 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vdso_image
- Explanation: vdso_image changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'data', 'type': '*mut ffi::c_void'}, {'name': 'size', 'type': 'ffi::c_ulong'}, {'name': 'alt', 'type': 'ffi::c_ulong'}, {'name': 'alt_len', 'type': 'ffi::c_ulong'}, {'name': 'extable_base', 'type': 'ffi::c_ulong'}, {'name': 'extable_len', 'type': 'ffi::c_ulong'}, {'name': 'extable', 'type': '*const ffi::c_void'}, {'name': 'sym_VDSO32_NOTE_MASK', 'type': 'ffi::c_long'}, {'name': 'sym___kernel_sigreturn', 'type': 'ffi::c_long'}, {'name': 'sym___kernel_rt_sigreturn', 'type': 'ffi::c_long'}, {'name': 'sym___kernel_vsyscall', 'type': 'ffi::c_long'}, {'name': 'sym_int80_landing_pad', 'type': 'ffi::c_long'}, {'name': 'sym_vdso32_sigreturn_landing_pad', 'type': 'ffi::c_long'}, {'name': 'sym_vdso32_rt_sigreturn_landing_pad', 'type': 'ffi::c_long'}]`
- New: `[{'name': 'data', 'type': '*mut ffi::c_void'}, {'name': 'size', 'type': 'ffi::c_ulong'}, {'name': 'alt', 'type': 'ffi::c_ulong'}, {'name': 'alt_len', 'type': 'ffi::c_ulong'}, {'name': 'extable_base', 'type': 'ffi::c_ulong'}, {'name': 'extable_len', 'type': 'ffi::c_ulong'}, {'name': 'extable', 'type': '*const ffi::c_void'}, {'name': 'sym___kernel_sigreturn', 'type': 'ffi::c_long'}, {'name': 'sym___kernel_rt_sigreturn', 'type': 'ffi::c_long'}, {'name': 'sym___kernel_vsyscall', 'type': 'ffi::c_long'}, {'name': 'sym_int80_landing_pad', 'type': 'ffi::c_long'}, {'name': 'sym_vdso32_sigreturn_landing_pad', 'type': 'ffi::c_long'}, {'name': 'sym_vdso32_rt_sigreturn_landing_pad', 'type': 'ffi::c_long'}]`

### Rust Evidence

- Graph edges: `1`

## W-000245 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vm_area_desc
- Explanation: vm_area_desc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mm', 'type': '*const mm_struct'}, {'name': 'file', 'type': '*mut file'}, {'name': 'start', 'type': 'ffi::c_ulong'}, {'name': 'end', 'type': 'ffi::c_ulong'}, {'name': 'pgoff', 'type': 'ffi::c_ulong'}, {'name': 'vm_file', 'type': '*mut file'}, {'name': 'vma_flags', 'type': 'vma_flags_t'}, {'name': 'page_prot', 'type': 'pgprot_t'}, {'name': 'vm_ops', 'type': '*const vm_operations_struct'}, {'name': 'private_data', 'type': '*mut ffi::c_void'}, {'name': 'action', 'type': 'mmap_action'}]`
- New: `[{'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'file', 'type': '*mut file'}, {'name': 'start', 'type': 'ffi::c_ulong'}, {'name': 'end', 'type': 'ffi::c_ulong'}, {'name': 'pgoff', 'type': 'ffi::c_ulong'}, {'name': 'vm_file', 'type': '*mut file'}, {'name': 'vma_flags', 'type': 'vma_flags_t'}, {'name': 'page_prot', 'type': 'pgprot_t'}, {'name': 'vm_ops', 'type': '*const vm_operations_struct'}, {'name': 'private_data', 'type': '*mut ffi::c_void'}, {'name': 'action', 'type': 'mmap_action'}]`

### Rust Evidence

- Graph edges: `1`

## W-000246 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vm_event_state
- Explanation: vm_event_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'event', 'type': '[ffi::c_ulong; 86usize]'}]`
- New: `[{'name': 'event', 'type': '[ffi::c_ulong; 73usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000247 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vm_operations_struct
- Explanation: vm_operations_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'open', 'type': '::core::option::Option<unsafe extern "C" fn(area: *mut vm_area_struct)>'}, {'name': 'close', 'type': '::core::option::Option<unsafe extern "C" fn(area: *mut vm_area_struct)>'}, {'name': 'may_split', 'type': '::core::option::Option<'}, {'name': 'mprotect', 'type': '::core::option::Option<'}, {'name': 'fault', 'type': '::core::option::Option<unsafe extern "C" fn(vmf: *mut vm_fault) -> vm_fault_t>'}, {'name': 'huge_fault', 'type': '::core::option::Option<'}, {'name': 'map_pages', 'type': '::core::option::Option<'}, {'name': 'pfn_mkwrite', 'type': '::core::option::Option<unsafe extern "C" fn(vmf: *mut vm_fault) -> vm_fault_t>'}, {'name': 'access', 'type': '::core::option::Option<'}, {'name': 'name', 'type': '::core::option::Option<'}, {'name': 'set_policy', 'type': '::core::option::Option<'}, {'name': 'get_policy', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'open', 'type': '::core::option::Option<unsafe extern "C" fn(vma: *mut vm_area_struct)>'}, {'name': 'close', 'type': '::core::option::Option<unsafe extern "C" fn(vma: *mut vm_area_struct)>'}, {'name': 'mapped', 'type': '::core::option::Option<'}, {'name': 'may_split', 'type': '::core::option::Option<'}, {'name': 'mprotect', 'type': '::core::option::Option<'}, {'name': 'fault', 'type': '::core::option::Option<unsafe extern "C" fn(vmf: *mut vm_fault) -> vm_fault_t>'}, {'name': 'huge_fault', 'type': '::core::option::Option<'}, {'name': 'map_pages', 'type': '::core::option::Option<'}, {'name': 'pfn_mkwrite', 'type': '::core::option::Option<unsafe extern "C" fn(vmf: *mut vm_fault) -> vm_fault_t>'}, {'name': 'access', 'type': '::core::option::Option<'}, {'name': 'name', 'type': '::core::option::Option<'}, {'name': 'set_policy', 'type': '::core::option::Option<'}, {'name': 'get_policy', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-000248 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: x86_cpu_id
- Explanation: x86_cpu_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'vendor', 'type': '__u16'}, {'name': 'family', 'type': '__u16'}, {'name': 'model', 'type': '__u16'}, {'name': 'steppings', 'type': '__u16'}, {'name': 'feature', 'type': '__u16'}, {'name': 'flags', 'type': '__u16'}, {'name': 'type_', 'type': '__u8'}, {'name': 'driver_data', 'type': 'kernel_ulong_t'}]`
- New: `[{'name': 'vendor', 'type': '__u16'}, {'name': 'family', 'type': '__u16'}, {'name': 'model', 'type': '__u16'}, {'name': 'steppings', 'type': '__u16'}, {'name': 'feature', 'type': '__u16'}, {'name': 'flags', 'type': '__u16'}, {'name': 'platform_mask', 'type': '__u8'}, {'name': 'type_', 'type': '__u8'}, {'name': 'driver_data', 'type': 'kernel_ulong_t'}]`

### Rust Evidence

- Graph edges: `1`

## W-000249 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: zap_details
- Explanation: zap_details changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'single_folio', 'type': '*mut folio'}, {'name': 'even_cows', 'type': 'bool_'}, {'name': 'reclaim_pt', 'type': 'bool_'}, {'name': 'zap_flags', 'type': 'zap_flags_t'}]`
- New: `[{'name': 'single_folio', 'type': '*mut folio'}, {'name': 'skip_cows', 'type': 'bool_'}, {'name': 'reclaim_pt', 'type': 'bool_'}, {'name': 'reaping', 'type': 'bool_'}, {'name': 'zap_flags', 'type': 'zap_flags_t'}]`

### Rust Evidence

- Graph edges: `1`

## W-000319 MacroConstDrift

- Risk: Medium
- Score: 8.4
- Symbol: cpuhp_state_CPUHP_AP_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `144`
- New: `143`

### Rust Evidence

- Graph edges: `4`

## W-000446 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: pin_config_param_PIN_CONFIG_SKEW_DELAY
- Explanation: pin_config_param_PIN_CONFIG_SKEW_DELAY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `23`
- New: `24`

### Rust Evidence

- Graph edges: `3`

## W-000254 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: CONFIG_RUSTC_VERSION
- Explanation: CONFIG_RUSTC_VERSION changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `107800`
- New: `108500`

### Rust Evidence

- Graph edges: `2`

## W-000262 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: ORC_REG_SP
- Explanation: ORC_REG_SP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `3`

### Rust Evidence

- Graph edges: `2`

## W-000320 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: cpuhp_state_CPUHP_AP_ONLINE_DYN
- Explanation: cpuhp_state_CPUHP_AP_ONLINE_DYN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `193`
- New: `192`

### Rust Evidence

- Graph edges: `2`

## W-000385 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: cpuhp_state_CPUHP_BP_PREPARE_DYN
- Explanation: cpuhp_state_CPUHP_BP_PREPARE_DYN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `62`
- New: `61`

### Rust Evidence

- Graph edges: `2`

## W-000519 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: vm_event_item_HTLB_BUDDY_PGALLOC
- Explanation: vm_event_item_HTLB_BUDDY_PGALLOC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `64`
- New: `51`

### Rust Evidence

- Graph edges: `2`

## W-000544 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: vm_event_item_SWAP_RA
- Explanation: vm_event_item_SWAP_RA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `73`
- New: `60`

### Rust Evidence

- Graph edges: `2`

## W-000251 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: CFI_OFFSET
- Explanation: CFI_OFFSET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `16`

### Rust Evidence

- Graph edges: `1`

## W-000252 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: CONFIG_BINDGEN_VERSION_TEXT
- Explanation: CONFIG_BINDGEN_VERSION_TEXT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `b"bindgen 0.65.1\0"`
- New: `b"bindgen 0.71.1\0"`

### Rust Evidence

- Graph edges: `1`

## W-000253 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: CONFIG_RUSTC_LLVM_VERSION
- Explanation: CONFIG_RUSTC_LLVM_VERSION changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `180102`
- New: `190107`

### Rust Evidence

- Graph edges: `1`

## W-000255 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: CONFIG_RUSTC_VERSION_TEXT
- Explanation: CONFIG_RUSTC_VERSION_TEXT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `b"rustc 1.78.0 (9b00956e5 2024-04-29)\0"`
- New: `b"rustc 1.85.0 (4d91de4e4 2025-02-17)\0"`

### Rust Evidence

- Graph edges: `1`

## W-000256 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: DISABLED_MASK11
- Explanation: DISABLED_MASK11 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8912896`
- New: `8388608`

### Rust Evidence

- Graph edges: `1`

## W-000257 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ETHTOOL_A_COALESCE_MAX
- Explanation: ETHTOOL_A_COALESCE_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `30`
- New: `32`

### Rust Evidence

- Graph edges: `1`

## W-000258 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ETHTOOL_A_PAUSE_STAT_MAX
- Explanation: ETHTOOL_A_PAUSE_STAT_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `3`
- New: `4`

### Rust Evidence

- Graph edges: `1`

## W-000259 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ORC_REG_BP_INDIRECT
- Explanation: ORC_REG_BP_INDIRECT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `10`

### Rust Evidence

- Graph edges: `1`

## W-000260 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ORC_REG_DI
- Explanation: ORC_REG_DI changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `3`
- New: `5`

### Rust Evidence

- Graph edges: `1`

## W-000261 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ORC_REG_PREV_SP
- Explanation: ORC_REG_PREV_SP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `1`
- New: `8`

### Rust Evidence

- Graph edges: `1`

## W-000263 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: QUEUE_FLAG_MAX
- Explanation: QUEUE_FLAG_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `17`
- New: `18`

### Rust Evidence

- Graph edges: `1`

## W-000264 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: RQ_nr_pinned
- Explanation: RQ_nr_pinned changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `3216`
- New: `3312`

### Rust Evidence

- Graph edges: `1`

## W-000265 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TASK_stack_canary
- Explanation: TASK_stack_canary changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `1464`
- New: `1528`

### Rust Evidence

- Graph edges: `1`

## W-000266 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TASK_threadsp
- Explanation: TASK_threadsp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `3032`
- New: `3080`

### Rust Evidence

- Graph edges: `1`

## W-000267 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __ETHTOOL_A_COALESCE_CNT
- Explanation: __ETHTOOL_A_COALESCE_CNT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `31`
- New: `33`

### Rust Evidence

- Graph edges: `1`

## W-000268 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __ETHTOOL_A_PAUSE_STAT_CNT
- Explanation: __ETHTOOL_A_PAUSE_STAT_CNT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `4`
- New: `5`

### Rust Evidence

- Graph edges: `1`

## W-000269 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ACTIVE
- Explanation: cpuhp_state_CPUHP_AP_ACTIVE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `236`
- New: `235`

### Rust Evidence

- Graph edges: `1`

## W-000270 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARC_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARC_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `126`
- New: `125`

### Rust Evidence

- Graph edges: `1`

## W-000271 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM64_DEBUG_MONITORS_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM64_DEBUG_MONITORS_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `109`
- New: `108`

### Rust Evidence

- Graph edges: `1`

## W-000272 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM64_ISNDEP_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM64_ISNDEP_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `138`
- New: `137`

### Rust Evidence

- Graph edges: `1`

## W-000273 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARMADA_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARMADA_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `123`
- New: `122`

### Rust Evidence

- Graph edges: `1`

## W-000274 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_EVTSTRM_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_EVTSTRM_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `117`
- New: `116`

### Rust Evidence

- Graph edges: `1`

## W-000275 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `116`
- New: `115`

### Rust Evidence

- Graph edges: `1`

## W-000276 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_CACHE_B15_RAC_DYING
- Explanation: cpuhp_state_CPUHP_AP_ARM_CACHE_B15_RAC_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `143`
- New: `142`

### Rust Evidence

- Graph edges: `1`

## W-000277 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_CORESIGHT_CTI_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_CORESIGHT_CTI_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `137`
- New: `136`

### Rust Evidence

- Graph edges: `1`

## W-000278 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_CORESIGHT_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_CORESIGHT_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `136`
- New: `135`

### Rust Evidence

- Graph edges: `1`

## W-000279 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_GLOBAL_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_GLOBAL_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `118`
- New: `117`

### Rust Evidence

- Graph edges: `1`

## W-000280 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_L2X0_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_L2X0_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `114`
- New: `113`

### Rust Evidence

- Graph edges: `1`

## W-000281 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_MVEBU_COHERENCY
- Explanation: cpuhp_state_CPUHP_AP_ARM_MVEBU_COHERENCY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `103`
- New: `102`

### Rust Evidence

- Graph edges: `1`

## W-000282 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_MVEBU_SYNC_CLOCKS
- Explanation: cpuhp_state_CPUHP_AP_ARM_MVEBU_SYNC_CLOCKS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `153`
- New: `152`

### Rust Evidence

- Graph edges: `1`

## W-000283 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_TWD_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_TWD_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `120`
- New: `119`

### Rust Evidence

- Graph edges: `1`

## W-000284 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_VFP_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_VFP_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `108`
- New: `107`

### Rust Evidence

- Graph edges: `1`

## W-000285 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_XEN_RUNSTATE_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_XEN_RUNSTATE_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `135`
- New: `134`

### Rust Evidence

- Graph edges: `1`

## W-000286 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_XEN_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_XEN_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `134`
- New: `133`

### Rust Evidence

- Graph edges: `1`

## W-000287 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_BASE_CACHEINFO_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_BASE_CACHEINFO_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `192`
- New: `191`

### Rust Evidence

- Graph edges: `1`

## W-000288 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_BLK_MQ_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_BLK_MQ_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `152`
- New: `151`

### Rust Evidence

- Graph edges: `1`

## W-000289 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_CACHECTRL_STARTING
- Explanation: cpuhp_state_CPUHP_AP_CACHECTRL_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `87`
- New: `86`

### Rust Evidence

- Graph edges: `1`

## W-000290 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_CLINT_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_CLINT_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `129`
- New: `128`

### Rust Evidence

- Graph edges: `1`

## W-000291 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_CPU_PM_STARTING
- Explanation: cpuhp_state_CPUHP_AP_CPU_PM_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `90`
- New: `89`

### Rust Evidence

- Graph edges: `1`

## W-000292 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_CSKY_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_CSKY_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `130`
- New: `129`

### Rust Evidence

- Graph edges: `1`

## W-000293 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_DTPM_CPU_DEAD
- Explanation: cpuhp_state_CPUHP_AP_DTPM_CPU_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `35`
- New: `34`

### Rust Evidence

- Graph edges: `1`

## W-000294 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_DUMMY_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_DUMMY_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `133`
- New: `132`

### Rust Evidence

- Graph edges: `1`

## W-000295 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_EXYNOS4_MCT_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_EXYNOS4_MCT_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `115`
- New: `114`

### Rust Evidence

- Graph edges: `1`

## W-000296 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_HRTIMERS_DYING
- Explanation: cpuhp_state_CPUHP_AP_HRTIMERS_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `140`
- New: `139`

### Rust Evidence

- Graph edges: `1`

## W-000297 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_HYPERV_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_HYPERV_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `147`
- New: `146`

### Rust Evidence

- Graph edges: `1`

## W-000298 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_HYPERV_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_HYPERV_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `132`
- New: `131`

### Rust Evidence

- Graph edges: `1`

## W-000299 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IDLE_DEAD
- Explanation: cpuhp_state_CPUHP_AP_IDLE_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `85`
- New: `84`

### Rust Evidence

- Graph edges: `1`

## W-000300 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_ACLINT_SSWI_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_ACLINT_SSWI_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `100`
- New: `99`

### Rust Evidence

- Graph edges: `1`

## W-000301 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_AFFINITY_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_IRQ_AFFINITY_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `151`
- New: `150`

### Rust Evidence

- Graph edges: `1`

## W-000302 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_APPLE_AIC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_APPLE_AIC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `93`
- New: `92`

### Rust Evidence

- Graph edges: `1`

## W-000303 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_ARMADA_XP_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_ARMADA_XP_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `94`
- New: `93`

### Rust Evidence

- Graph edges: `1`

## W-000304 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_AVECINTC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_AVECINTC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `98`
- New: `97`

### Rust Evidence

- Graph edges: `1`

## W-000305 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_BCM2836_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_BCM2836_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `95`
- New: `94`

### Rust Evidence

- Graph edges: `1`

## W-000306 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_EIOINTC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_EIOINTC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `97`
- New: `96`

### Rust Evidence

- Graph edges: `1`

## W-000307 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_GIC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_GIC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `91`
- New: `90`

### Rust Evidence

- Graph edges: `1`

## W-000308 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_HIP04_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_HIP04_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `92`
- New: `91`

### Rust Evidence

- Graph edges: `1`

## W-000309 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_MIPS_GIC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_MIPS_GIC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `96`
- New: `95`

### Rust Evidence

- Graph edges: `1`

## W-000310 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_RISCV_IMSIC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_RISCV_IMSIC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `101`
- New: `100`

### Rust Evidence

- Graph edges: `1`

## W-000311 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_RISCV_SBI_IPI_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_RISCV_SBI_IPI_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `102`
- New: `101`

### Rust Evidence

- Graph edges: `1`

## W-000312 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_SIFIVE_PLIC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_SIFIVE_PLIC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `99`
- New: `98`

### Rust Evidence

- Graph edges: `1`

## W-000313 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_JCORE_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_JCORE_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `119`
- New: `118`

### Rust Evidence

- Graph edges: `1`

## W-000314 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_KTHREADS_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_KTHREADS_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `191`
- New: `190`

### Rust Evidence

- Graph edges: `1`

## W-000315 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_KVM_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_KVM_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `148`
- New: `147`

### Rust Evidence

- Graph edges: `1`

## W-000316 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_LOONGARCH_ARCH_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_LOONGARCH_ARCH_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `124`
- New: `123`

### Rust Evidence

- Graph edges: `1`

## W-000317 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_MIPS_GIC_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_MIPS_GIC_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `125`
- New: `124`

### Rust Evidence

- Graph edges: `1`

## W-000318 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_OFFLINE
- Explanation: cpuhp_state_CPUHP_AP_OFFLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `86`
- New: `85`

### Rust Evidence

- Graph edges: `1`

## W-000321 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ONLINE_DYN_END
- Explanation: cpuhp_state_CPUHP_AP_ONLINE_DYN_END changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `233`
- New: `232`

### Rust Evidence

- Graph edges: `1`

## W-000322 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ONLINE_IDLE
- Explanation: cpuhp_state_CPUHP_AP_ONLINE_IDLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `146`
- New: `145`

### Rust Evidence

- Graph edges: `1`

## W-000323 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_ACPI_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_ACPI_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `111`
- New: `110`

### Rust Evidence

- Graph edges: `1`

## W-000324 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_APM_XGENE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_APM_XGENE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `175`
- New: `174`

### Rust Evidence

- Graph edges: `1`

## W-000325 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_CAVIUM_TX2_UNCORE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_CAVIUM_TX2_UNCORE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `176`
- New: `175`

### Rust Evidence

- Graph edges: `1`

## W-000326 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_CCI_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_CCI_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `162`
- New: `161`

### Rust Evidence

- Graph edges: `1`

## W-000327 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_CCN_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_CCN_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `163`
- New: `162`

### Rust Evidence

- Graph edges: `1`

## W-000328 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_CPA_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_CPA_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `164`
- New: `163`

### Rust Evidence

- Graph edges: `1`

## W-000329 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_DDRC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_DDRC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `165`
- New: `164`

### Rust Evidence

- Graph edges: `1`

## W-000330 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_HHA_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_HHA_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `166`
- New: `165`

### Rust Evidence

- Graph edges: `1`

## W-000331 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_L3_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_L3_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `167`
- New: `166`

### Rust Evidence

- Graph edges: `1`

## W-000332 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PA_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PA_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `168`
- New: `167`

### Rust Evidence

- Graph edges: `1`

## W-000333 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PCIE_PMU_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PCIE_PMU_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `170`
- New: `169`

### Rust Evidence

- Graph edges: `1`

## W-000334 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_SLLC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_SLLC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `169`
- New: `168`

### Rust Evidence

- Graph edges: `1`

## W-000335 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HNS3_PMU_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HNS3_PMU_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `171`
- New: `170`

### Rust Evidence

- Graph edges: `1`

## W-000336 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HW_BREAKPOINT_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HW_BREAKPOINT_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `110`
- New: `109`

### Rust Evidence

- Graph edges: `1`

## W-000337 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_L2X0_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_L2X0_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `172`
- New: `171`

### Rust Evidence

- Graph edges: `1`

## W-000338 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_MARVELL_CN10K_DDR_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_MARVELL_CN10K_DDR_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `177`
- New: `176`

### Rust Evidence

- Graph edges: `1`

## W-000339 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_MRVL_PEM_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_MRVL_PEM_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `178`
- New: `177`

### Rust Evidence

- Graph edges: `1`

## W-000340 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L2_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L2_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `173`
- New: `172`

### Rust Evidence

- Graph edges: `1`

## W-000341 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L3_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L3_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `174`
- New: `173`

### Rust Evidence

- Graph edges: `1`

## W-000342 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `112`
- New: `111`

### Rust Evidence

- Graph edges: `1`

## W-000343 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_CSKY_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_CSKY_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `185`
- New: `184`

### Rust Evidence

- Graph edges: `1`

## W-000344 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `155`
- New: `154`

### Rust Evidence

- Graph edges: `1`

## W-000345 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_CORE_IMC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_CORE_IMC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `180`
- New: `179`

### Rust Evidence

- Graph edges: `1`

## W-000346 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_HV_24x7_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_HV_24x7_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `183`
- New: `182`

### Rust Evidence

- Graph edges: `1`

## W-000347 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_HV_GPCI_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_HV_GPCI_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `184`
- New: `183`

### Rust Evidence

- Graph edges: `1`

## W-000348 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_NEST_IMC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_NEST_IMC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `179`
- New: `178`

### Rust Evidence

- Graph edges: `1`

## W-000349 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_THREAD_IMC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_THREAD_IMC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `181`
- New: `180`

### Rust Evidence

- Graph edges: `1`

## W-000350 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_TRACE_IMC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_TRACE_IMC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `182`
- New: `181`

### Rust Evidence

- Graph edges: `1`

## W-000351 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_RISCV_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_RISCV_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `113`
- New: `112`

### Rust Evidence

- Graph edges: `1`

## W-000352 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_S390_CF_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_S390_CF_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `160`
- New: `159`

### Rust Evidence

- Graph edges: `1`

## W-000353 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_S390_SF_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_S390_SF_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `161`
- New: `160`

### Rust Evidence

- Graph edges: `1`

## W-000354 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_IBS_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_IBS_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `106`
- New: `105`

### Rust Evidence

- Graph edges: `1`

## W-000355 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_POWER_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_POWER_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `159`
- New: `158`

### Rust Evidence

- Graph edges: `1`

## W-000356 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `158`
- New: `157`

### Rust Evidence

- Graph edges: `1`

## W-000357 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `104`
- New: `103`

### Rust Evidence

- Graph edges: `1`

## W-000358 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `156`
- New: `155`

### Rust Evidence

- Graph edges: `1`

## W-000359 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `105`
- New: `104`

### Rust Evidence

- Graph edges: `1`

## W-000360 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_UNCORE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_UNCORE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `157`
- New: `156`

### Rust Evidence

- Graph edges: `1`

## W-000361 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_XTENSA_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_XTENSA_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `107`
- New: `106`

### Rust Evidence

- Graph edges: `1`

## W-000362 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_QCOM_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_QCOM_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `121`
- New: `120`

### Rust Evidence

- Graph edges: `1`

## W-000363 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_RANDOM_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_RANDOM_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `189`
- New: `188`

### Rust Evidence

- Graph edges: `1`

## W-000364 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_RCUTREE_DYING
- Explanation: cpuhp_state_CPUHP_AP_RCUTREE_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `89`
- New: `88`

### Rust Evidence

- Graph edges: `1`

## W-000365 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_RCUTREE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_RCUTREE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `190`
- New: `189`

### Rust Evidence

- Graph edges: `1`

## W-000366 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_REALTEK_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_REALTEK_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `127`
- New: `126`

### Rust Evidence

- Graph edges: `1`

## W-000367 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_RISCV_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_RISCV_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `128`
- New: `127`

### Rust Evidence

- Graph edges: `1`

## W-000368 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_SCHED_STARTING
- Explanation: cpuhp_state_CPUHP_AP_SCHED_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `88`
- New: `87`

### Rust Evidence

- Graph edges: `1`

## W-000369 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_SCHED_WAIT_EMPTY
- Explanation: cpuhp_state_CPUHP_AP_SCHED_WAIT_EMPTY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `149`
- New: `148`

### Rust Evidence

- Graph edges: `1`

## W-000370 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_SMPBOOT_THREADS
- Explanation: cpuhp_state_CPUHP_AP_SMPBOOT_THREADS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `150`
- New: `149`

### Rust Evidence

- Graph edges: `1`

## W-000371 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_SMPCFD_DYING
- Explanation: cpuhp_state_CPUHP_AP_SMPCFD_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `139`
- New: `138`

### Rust Evidence

- Graph edges: `1`

## W-000372 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_TEGRA_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_TEGRA_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `122`
- New: `121`

### Rust Evidence

- Graph edges: `1`

## W-000373 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_TICK_DYING
- Explanation: cpuhp_state_CPUHP_AP_TICK_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `141`
- New: `140`

### Rust Evidence

- Graph edges: `1`

## W-000374 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_TI_GP_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_TI_GP_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `131`
- New: `130`

### Rust Evidence

- Graph edges: `1`

## W-000375 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_TMIGR_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_TMIGR_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `186`
- New: `185`

### Rust Evidence

- Graph edges: `1`

## W-000376 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_WATCHDOG_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_WATCHDOG_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `187`
- New: `186`

### Rust Evidence

- Graph edges: `1`

## W-000377 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_WORKQUEUE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_WORKQUEUE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `188`
- New: `187`

### Rust Evidence

- Graph edges: `1`

## W-000378 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_X86_HPET_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_X86_HPET_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `234`
- New: `233`

### Rust Evidence

- Graph edges: `1`

## W-000379 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_X86_INTEL_EPB_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_X86_INTEL_EPB_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `154`
- New: `153`

### Rust Evidence

- Graph edges: `1`

## W-000380 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_X86_KVM_CLK_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_X86_KVM_CLK_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `235`
- New: `234`

### Rust Evidence

- Graph edges: `1`

## W-000381 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_X86_TBOOT_DYING
- Explanation: cpuhp_state_CPUHP_AP_X86_TBOOT_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `142`
- New: `141`

### Rust Evidence

- Graph edges: `1`

## W-000382 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_ARM_BL_PREPARE
- Explanation: cpuhp_state_CPUHP_ARM_BL_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `54`
- New: `53`

### Rust Evidence

- Graph edges: `1`

## W-000383 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_ARM_SHMOBILE_SCU_PREPARE
- Explanation: cpuhp_state_CPUHP_ARM_SHMOBILE_SCU_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `50`
- New: `49`

### Rust Evidence

- Graph edges: `1`

## W-000384 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_BP_KICK_AP
- Explanation: cpuhp_state_CPUHP_BP_KICK_AP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `83`
- New: `82`

### Rust Evidence

- Graph edges: `1`

## W-000386 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_BP_PREPARE_DYN_END
- Explanation: cpuhp_state_CPUHP_BP_PREPARE_DYN_END changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `82`
- New: `81`

### Rust Evidence

- Graph edges: `1`

## W-000387 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_BRINGUP_CPU
- Explanation: cpuhp_state_CPUHP_BRINGUP_CPU changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `84`
- New: `83`

### Rust Evidence

- Graph edges: `1`

## W-000388 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_CPUIDLE_COUPLED_PREPARE
- Explanation: cpuhp_state_CPUHP_CPUIDLE_COUPLED_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `45`
- New: `44`

### Rust Evidence

- Graph edges: `1`

## W-000389 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_HRTIMERS_PREPARE
- Explanation: cpuhp_state_CPUHP_HRTIMERS_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `39`
- New: `38`

### Rust Evidence

- Graph edges: `1`

## W-000390 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_KVM_PPC_BOOK3S_PREPARE
- Explanation: cpuhp_state_CPUHP_KVM_PPC_BOOK3S_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `57`
- New: `56`

### Rust Evidence

- Graph edges: `1`

## W-000391 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_MD_RAID5_PREPARE
- Explanation: cpuhp_state_CPUHP_MD_RAID5_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `43`
- New: `42`

### Rust Evidence

- Graph edges: `1`

## W-000392 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_MIPS_SOC_PREPARE
- Explanation: cpuhp_state_CPUHP_MIPS_SOC_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `61`
- New: `60`

### Rust Evidence

- Graph edges: `1`

## W-000393 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_MM_ZSWP_POOL_PREPARE
- Explanation: cpuhp_state_CPUHP_MM_ZSWP_POOL_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `56`
- New: `55`

### Rust Evidence

- Graph edges: `1`

## W-000394 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_NET_IUCV_PREPARE
- Explanation: cpuhp_state_CPUHP_NET_IUCV_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `53`
- New: `52`

### Rust Evidence

- Graph edges: `1`

## W-000395 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_ONLINE
- Explanation: cpuhp_state_CPUHP_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `237`
- New: `236`

### Rust Evidence

- Graph edges: `1`

## W-000396 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_POWERPC_MMU_CTX_PREPARE
- Explanation: cpuhp_state_CPUHP_POWERPC_MMU_CTX_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `47`
- New: `46`

### Rust Evidence

- Graph edges: `1`

## W-000397 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_POWERPC_PMAC_PREPARE
- Explanation: cpuhp_state_CPUHP_POWERPC_PMAC_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `46`
- New: `45`

### Rust Evidence

- Graph edges: `1`

## W-000398 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_POWER_NUMA_PREPARE
- Explanation: cpuhp_state_CPUHP_POWER_NUMA_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `38`
- New: `37`

### Rust Evidence

- Graph edges: `1`

## W-000399 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_RANDOM_PREPARE
- Explanation: cpuhp_state_CPUHP_RANDOM_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `36`
- New: `35`

### Rust Evidence

- Graph edges: `1`

## W-000400 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_RCUTREE_PREP
- Explanation: cpuhp_state_CPUHP_RCUTREE_PREP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `44`
- New: `43`

### Rust Evidence

- Graph edges: `1`

## W-000401 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_RELAY_PREPARE
- Explanation: cpuhp_state_CPUHP_RELAY_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `42`
- New: `41`

### Rust Evidence

- Graph edges: `1`

## W-000402 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_SH_SH3X_PREPARE
- Explanation: cpuhp_state_CPUHP_SH_SH3X_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `51`
- New: `50`

### Rust Evidence

- Graph edges: `1`

## W-000403 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_SMPCFD_PREPARE
- Explanation: cpuhp_state_CPUHP_SMPCFD_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `41`
- New: `40`

### Rust Evidence

- Graph edges: `1`

## W-000404 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_TEARDOWN_CPU
- Explanation: cpuhp_state_CPUHP_TEARDOWN_CPU changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `145`
- New: `144`

### Rust Evidence

- Graph edges: `1`

## W-000405 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_TIMERS_PREPARE
- Explanation: cpuhp_state_CPUHP_TIMERS_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `59`
- New: `58`

### Rust Evidence

- Graph edges: `1`

## W-000406 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_TMIGR_PREPARE
- Explanation: cpuhp_state_CPUHP_TMIGR_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `60`
- New: `59`

### Rust Evidence

- Graph edges: `1`

## W-000407 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_TOPOLOGY_PREPARE
- Explanation: cpuhp_state_CPUHP_TOPOLOGY_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `52`
- New: `51`

### Rust Evidence

- Graph edges: `1`

## W-000408 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_TRACE_RB_PREPARE
- Explanation: cpuhp_state_CPUHP_TRACE_RB_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `55`
- New: `54`

### Rust Evidence

- Graph edges: `1`

## W-000409 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_WORKQUEUE_PREP
- Explanation: cpuhp_state_CPUHP_WORKQUEUE_PREP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `37`
- New: `36`

### Rust Evidence

- Graph edges: `1`

## W-000410 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_X2APIC_PREPARE
- Explanation: cpuhp_state_CPUHP_X2APIC_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `40`
- New: `39`

### Rust Evidence

- Graph edges: `1`

## W-000411 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_XEN_EVTCHN_PREPARE
- Explanation: cpuhp_state_CPUHP_XEN_EVTCHN_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `49`
- New: `48`

### Rust Evidence

- Graph edges: `1`

## W-000412 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_XEN_PREPARE
- Explanation: cpuhp_state_CPUHP_XEN_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `47`

### Rust Evidence

- Graph edges: `1`

## W-000413 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_ZCOMP_PREPARE
- Explanation: cpuhp_state_CPUHP_ZCOMP_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `58`
- New: `57`

### Rust Evidence

- Graph edges: `1`

## W-000414 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: dma_fence_flag_bits_DMA_FENCE_FLAG_ENABLE_SIGNAL_BIT
- Explanation: dma_fence_flag_bits_DMA_FENCE_FLAG_ENABLE_SIGNAL_BIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `3`
- New: `5`

### Rust Evidence

- Graph edges: `1`

## W-000415 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: dma_fence_flag_bits_DMA_FENCE_FLAG_SEQNO64_BIT
- Explanation: dma_fence_flag_bits_DMA_FENCE_FLAG_SEQNO64_BIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0`
- New: `2`

### Rust Evidence

- Graph edges: `1`

## W-000416 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: dma_fence_flag_bits_DMA_FENCE_FLAG_SIGNALED_BIT
- Explanation: dma_fence_flag_bits_DMA_FENCE_FLAG_SIGNALED_BIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `1`
- New: `3`

### Rust Evidence

- Graph edges: `1`

## W-000417 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: dma_fence_flag_bits_DMA_FENCE_FLAG_TIMESTAMP_BIT
- Explanation: dma_fence_flag_bits_DMA_FENCE_FLAG_TIMESTAMP_BIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `2`
- New: `4`

### Rust Evidence

- Graph edges: `1`

## W-000418 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: dma_fence_flag_bits_DMA_FENCE_FLAG_USER_BITS
- Explanation: dma_fence_flag_bits_DMA_FENCE_FLAG_USER_BITS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `4`
- New: `6`

### Rust Evidence

- Graph edges: `1`

## W-000419 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_KMEM
- Explanation: memcg_stat_item_MEMCG_KMEM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `52`
- New: `67`

### Rust Evidence

- Graph edges: `1`

## W-000420 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_NR_STAT
- Explanation: memcg_stat_item_MEMCG_NR_STAT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `55`
- New: `71`

### Rust Evidence

- Graph edges: `1`

## W-000421 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_PERCPU_B
- Explanation: memcg_stat_item_MEMCG_PERCPU_B changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `50`
- New: `66`

### Rust Evidence

- Graph edges: `1`

## W-000422 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_SOCK
- Explanation: memcg_stat_item_MEMCG_SOCK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `49`
- New: `65`

### Rust Evidence

- Graph edges: `1`

## W-000423 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_SWAP
- Explanation: memcg_stat_item_MEMCG_SWAP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `64`

### Rust Evidence

- Graph edges: `1`

## W-000424 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_ZSWAPPED
- Explanation: memcg_stat_item_MEMCG_ZSWAPPED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `54`
- New: `69`

### Rust Evidence

- Graph edges: `1`

## W-000425 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_ZSWAP_B
- Explanation: memcg_stat_item_MEMCG_ZSWAP_B changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `53`
- New: `68`

### Rust Evidence

- Graph edges: `1`

## W-000426 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_BALLOON_PAGES
- Explanation: node_stat_item_NR_BALLOON_PAGES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `46`
- New: `60`

### Rust Evidence

- Graph edges: `1`

## W-000427 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_HUGETLB
- Explanation: node_stat_item_NR_HUGETLB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `45`
- New: `59`

### Rust Evidence

- Graph edges: `1`

## W-000428 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_IOMMU_PAGES
- Explanation: node_stat_item_NR_IOMMU_PAGES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `39`
- New: `40`

### Rust Evidence

- Graph edges: `1`

## W-000429 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_KERNEL_FILE_PAGES
- Explanation: node_stat_item_NR_KERNEL_FILE_PAGES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `47`
- New: `61`

### Rust Evidence

- Graph edges: `1`

## W-000430 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_KERNEL_STACK_KB
- Explanation: node_stat_item_NR_KERNEL_STACK_KB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `36`
- New: `37`

### Rust Evidence

- Graph edges: `1`

## W-000431 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_PAGETABLE
- Explanation: node_stat_item_NR_PAGETABLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `37`
- New: `38`

### Rust Evidence

- Graph edges: `1`

## W-000432 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_SECONDARY_PAGETABLE
- Explanation: node_stat_item_NR_SECONDARY_PAGETABLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `38`
- New: `39`

### Rust Evidence

- Graph edges: `1`

## W-000433 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_SWAPCACHE
- Explanation: node_stat_item_NR_SWAPCACHE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `40`
- New: `41`

### Rust Evidence

- Graph edges: `1`

## W-000434 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_VM_NODE_STAT_ITEMS
- Explanation: node_stat_item_NR_VM_NODE_STAT_ITEMS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `64`

### Rust Evidence

- Graph edges: `1`

## W-000435 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_PGDEMOTE_DIRECT
- Explanation: node_stat_item_PGDEMOTE_DIRECT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `42`
- New: `43`

### Rust Evidence

- Graph edges: `1`

## W-000436 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_PGDEMOTE_KHUGEPAGED
- Explanation: node_stat_item_PGDEMOTE_KHUGEPAGED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `43`
- New: `44`

### Rust Evidence

- Graph edges: `1`

## W-000437 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_PGDEMOTE_KSWAPD
- Explanation: node_stat_item_PGDEMOTE_KSWAPD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `41`
- New: `42`

### Rust Evidence

- Graph edges: `1`

## W-000438 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_PGDEMOTE_PROACTIVE
- Explanation: node_stat_item_PGDEMOTE_PROACTIVE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `44`
- New: `45`

### Rust Evidence

- Graph edges: `1`

## W-000439 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pin_config_param_PIN_CONFIG_LEVEL
- Explanation: pin_config_param_PIN_CONFIG_LEVEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `18`
- New: `19`

### Rust Evidence

- Graph edges: `1`

## W-000440 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pin_config_param_PIN_CONFIG_MODE_LOW_POWER
- Explanation: pin_config_param_PIN_CONFIG_MODE_LOW_POWER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `17`

### Rust Evidence

- Graph edges: `1`

## W-000441 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pin_config_param_PIN_CONFIG_MODE_PWM
- Explanation: pin_config_param_PIN_CONFIG_MODE_PWM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `17`
- New: `18`

### Rust Evidence

- Graph edges: `1`

## W-000442 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pin_config_param_PIN_CONFIG_OUTPUT_ENABLE
- Explanation: pin_config_param_PIN_CONFIG_OUTPUT_ENABLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `19`
- New: `20`

### Rust Evidence

- Graph edges: `1`

## W-000443 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pin_config_param_PIN_CONFIG_OUTPUT_IMPEDANCE_OHMS
- Explanation: pin_config_param_PIN_CONFIG_OUTPUT_IMPEDANCE_OHMS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `20`
- New: `21`

### Rust Evidence

- Graph edges: `1`

## W-000444 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pin_config_param_PIN_CONFIG_PERSIST_STATE
- Explanation: pin_config_param_PIN_CONFIG_PERSIST_STATE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `21`
- New: `22`

### Rust Evidence

- Graph edges: `1`

## W-000445 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pin_config_param_PIN_CONFIG_POWER_SOURCE
- Explanation: pin_config_param_PIN_CONFIG_POWER_SOURCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `22`
- New: `23`

### Rust Evidence

- Graph edges: `1`

## W-000447 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pin_config_param_PIN_CONFIG_SKEW_DELAY_INPUT_PS
- Explanation: pin_config_param_PIN_CONFIG_SKEW_DELAY_INPUT_PS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `24`
- New: `25`

### Rust Evidence

- Graph edges: `1`

## W-000448 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pin_config_param_PIN_CONFIG_SKEW_DELAY_OUTPUT_PS
- Explanation: pin_config_param_PIN_CONFIG_SKEW_DELAY_OUTPUT_PS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `25`
- New: `26`

### Rust Evidence

- Graph edges: `1`

## W-000449 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pin_config_param_PIN_CONFIG_SLEEP_HARDWARE_STATE
- Explanation: pin_config_param_PIN_CONFIG_SLEEP_HARDWARE_STATE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `26`
- New: `27`

### Rust Evidence

- Graph edges: `1`

## W-000450 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pin_config_param_PIN_CONFIG_SLEW_RATE
- Explanation: pin_config_param_PIN_CONFIG_SLEW_RATE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `27`
- New: `28`

### Rust Evidence

- Graph edges: `1`

## W-000451 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_ARP_PVLAN_DISABLE
- Explanation: skb_drop_reason_SKB_DROP_REASON_ARP_PVLAN_DISABLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `118`
- New: `115`

### Rust Evidence

- Graph edges: `1`

## W-000452 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_BRIDGE_INGRESS_STP_STATE
- Explanation: skb_drop_reason_SKB_DROP_REASON_BRIDGE_INGRESS_STP_STATE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `120`
- New: `117`

### Rust Evidence

- Graph edges: `1`

## W-000453 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_CANFD_RX_INVALID_FRAME
- Explanation: skb_drop_reason_SKB_DROP_REASON_CANFD_RX_INVALID_FRAME changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `122`
- New: `119`

### Rust Evidence

- Graph edges: `1`

## W-000454 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_CANXL_RX_INVALID_FRAME
- Explanation: skb_drop_reason_SKB_DROP_REASON_CANXL_RX_INVALID_FRAME changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `123`
- New: `120`

### Rust Evidence

- Graph edges: `1`

## W-000455 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_CAN_RX_INVALID_FRAME
- Explanation: skb_drop_reason_SKB_DROP_REASON_CAN_RX_INVALID_FRAME changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `121`
- New: `118`

### Rust Evidence

- Graph edges: `1`

## W-000456 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_CPU_BACKLOG
- Explanation: skb_drop_reason_SKB_DROP_REASON_CPU_BACKLOG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `72`
- New: `66`

### Rust Evidence

- Graph edges: `1`

## W-000457 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_DEV_HDR
- Explanation: skb_drop_reason_SKB_DROP_REASON_DEV_HDR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `79`
- New: `76`

### Rust Evidence

- Graph edges: `1`

## W-000458 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_DEV_READY
- Explanation: skb_drop_reason_SKB_DROP_REASON_DEV_READY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `80`
- New: `77`

### Rust Evidence

- Graph edges: `1`

## W-000459 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_DUP_FRAG
- Explanation: skb_drop_reason_SKB_DROP_REASON_DUP_FRAG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `95`
- New: `92`

### Rust Evidence

- Graph edges: `1`

## W-000460 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FRAG_REASM_TIMEOUT
- Explanation: skb_drop_reason_SKB_DROP_REASON_FRAG_REASM_TIMEOUT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `96`
- New: `93`

### Rust Evidence

- Graph edges: `1`

## W-000461 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FRAG_TOO_FAR
- Explanation: skb_drop_reason_SKB_DROP_REASON_FRAG_TOO_FAR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `97`
- New: `94`

### Rust Evidence

- Graph edges: `1`

## W-000462 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FULL_RING
- Explanation: skb_drop_reason_SKB_DROP_REASON_FULL_RING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `81`
- New: `78`

### Rust Evidence

- Graph edges: `1`

## W-000463 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_HDR_TRUNC
- Explanation: skb_drop_reason_SKB_DROP_REASON_HDR_TRUNC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `83`
- New: `80`

### Rust Evidence

- Graph edges: `1`

## W-000464 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_ICMP_CSUM
- Explanation: skb_drop_reason_SKB_DROP_REASON_ICMP_CSUM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `86`
- New: `83`

### Rust Evidence

- Graph edges: `1`

## W-000465 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_INVALID_PROTO
- Explanation: skb_drop_reason_SKB_DROP_REASON_INVALID_PROTO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `87`
- New: `84`

### Rust Evidence

- Graph edges: `1`

## W-000466 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_BAD_EXTHDR
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_BAD_EXTHDR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `99`
- New: `96`

### Rust Evidence

- Graph edges: `1`

## W-000467 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_CODE
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_CODE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `102`
- New: `99`

### Rust Evidence

- Graph edges: `1`

## W-000468 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_OPTIONS
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_OPTIONS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `103`
- New: `100`

### Rust Evidence

- Graph edges: `1`

## W-000469 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_FRAG
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_FRAG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `100`
- New: `97`

### Rust Evidence

- Graph edges: `1`

## W-000470 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_HOP_LIMIT
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_HOP_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `101`
- New: `98`

### Rust Evidence

- Graph edges: `1`

## W-000471 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_NS_OTHERHOST
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_NS_OTHERHOST changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `104`
- New: `101`

### Rust Evidence

- Graph edges: `1`

## W-000472 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INADDRERRORS
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INADDRERRORS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `88`
- New: `85`

### Rust Evidence

- Graph edges: `1`

## W-000473 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INNOROUTES
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INNOROUTES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `89`
- New: `86`

### Rust Evidence

- Graph edges: `1`

## W-000474 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_DEST
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_DEST changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `93`
- New: `90`

### Rust Evidence

- Graph edges: `1`

## W-000475 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_SOURCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_SOURCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `91`
- New: `88`

### Rust Evidence

- Graph edges: `1`

## W-000476 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_LOCALNET
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_LOCALNET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `92`
- New: `89`

### Rust Evidence

- Graph edges: `1`

## W-000477 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_LOCAL_SOURCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_LOCAL_SOURCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `90`
- New: `87`

### Rust Evidence

- Graph edges: `1`

## W-000478 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_TUNNEL_ECN
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_TUNNEL_ECN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `115`
- New: `112`

### Rust Evidence

- Graph edges: `1`

## W-000479 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_LOCAL_MAC
- Explanation: skb_drop_reason_SKB_DROP_REASON_LOCAL_MAC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `117`
- New: `114`

### Rust Evidence

- Graph edges: `1`

## W-000480 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_MAC_IEEE_MAC_CONTROL
- Explanation: skb_drop_reason_SKB_DROP_REASON_MAC_IEEE_MAC_CONTROL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `119`
- New: `116`

### Rust Evidence

- Graph edges: `1`

## W-000481 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_MAC_INVALID_SOURCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_MAC_INVALID_SOURCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `112`
- New: `109`

### Rust Evidence

- Graph edges: `1`

## W-000482 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_MAX
- Explanation: skb_drop_reason_SKB_DROP_REASON_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `128`
- New: `125`

### Rust Evidence

- Graph edges: `1`

## W-000483 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NOMEM
- Explanation: skb_drop_reason_SKB_DROP_REASON_NOMEM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `82`
- New: `79`

### Rust Evidence

- Graph edges: `1`

## W-000484 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NO_TX_TARGET
- Explanation: skb_drop_reason_SKB_DROP_REASON_NO_TX_TARGET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `114`
- New: `111`

### Rust Evidence

- Graph edges: `1`

## W-000485 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_PACKET_SOCK_ERROR
- Explanation: skb_drop_reason_SKB_DROP_REASON_PACKET_SOCK_ERROR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `107`
- New: `104`

### Rust Evidence

- Graph edges: `1`

## W-000486 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_PFMEMALLOC
- Explanation: skb_drop_reason_SKB_DROP_REASON_PFMEMALLOC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `124`
- New: `121`

### Rust Evidence

- Graph edges: `1`

## W-000487 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_PKT_TOO_BIG
- Explanation: skb_drop_reason_SKB_DROP_REASON_PKT_TOO_BIG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `94`
- New: `91`

### Rust Evidence

- Graph edges: `1`

## W-000488 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_PSP_INPUT
- Explanation: skb_drop_reason_SKB_DROP_REASON_PSP_INPUT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `126`
- New: `122`

### Rust Evidence

- Graph edges: `1`

## W-000489 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_PSP_OUTPUT
- Explanation: skb_drop_reason_SKB_DROP_REASON_PSP_OUTPUT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `127`
- New: `123`

### Rust Evidence

- Graph edges: `1`

## W-000490 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_QUEUE_PURGE
- Explanation: skb_drop_reason_SKB_DROP_REASON_QUEUE_PURGE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `105`
- New: `102`

### Rust Evidence

- Graph edges: `1`

## W-000491 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SKB_CSUM
- Explanation: skb_drop_reason_SKB_DROP_REASON_SKB_CSUM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `76`
- New: `72`

### Rust Evidence

- Graph edges: `1`

## W-000492 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SKB_GSO_SEG
- Explanation: skb_drop_reason_SKB_DROP_REASON_SKB_GSO_SEG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `77`
- New: `73`

### Rust Evidence

- Graph edges: `1`

## W-000493 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SKB_UCOPY_FAULT
- Explanation: skb_drop_reason_SKB_DROP_REASON_SKB_UCOPY_FAULT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `78`
- New: `75`

### Rust Evidence

- Graph edges: `1`

## W-000494 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TAP_FILTER
- Explanation: skb_drop_reason_SKB_DROP_REASON_TAP_FILTER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `84`
- New: `81`

### Rust Evidence

- Graph edges: `1`

## W-000495 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TAP_TXFILTER
- Explanation: skb_drop_reason_SKB_DROP_REASON_TAP_TXFILTER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `85`
- New: `82`

### Rust Evidence

- Graph edges: `1`

## W-000496 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_MINTTL
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_MINTTL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `98`
- New: `95`

### Rust Evidence

- Graph edges: `1`

## W-000497 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_CHAIN_NOTFOUND
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_CHAIN_NOTFOUND changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `108`
- New: `105`

### Rust Evidence

- Graph edges: `1`

## W-000498 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_COOKIE_ERROR
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_COOKIE_ERROR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `106`
- New: `103`

### Rust Evidence

- Graph edges: `1`

## W-000499 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_INGRESS
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_INGRESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `74`
- New: `70`

### Rust Evidence

- Graph edges: `1`

## W-000500 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_RECLASSIFY_LOOP
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_RECLASSIFY_LOOP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `109`
- New: `106`

### Rust Evidence

- Graph edges: `1`

## W-000501 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TUNNEL_TXINFO
- Explanation: skb_drop_reason_SKB_DROP_REASON_TUNNEL_TXINFO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `116`
- New: `113`

### Rust Evidence

- Graph edges: `1`

## W-000502 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_UNHANDLED_PROTO
- Explanation: skb_drop_reason_SKB_DROP_REASON_UNHANDLED_PROTO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `75`
- New: `71`

### Rust Evidence

- Graph edges: `1`

## W-000503 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_VXLAN_ENTRY_EXISTS
- Explanation: skb_drop_reason_SKB_DROP_REASON_VXLAN_ENTRY_EXISTS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `113`
- New: `110`

### Rust Evidence

- Graph edges: `1`

## W-000504 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_VXLAN_INVALID_HDR
- Explanation: skb_drop_reason_SKB_DROP_REASON_VXLAN_INVALID_HDR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `110`
- New: `107`

### Rust Evidence

- Graph edges: `1`

## W-000505 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_VXLAN_VNI_NOT_FOUND
- Explanation: skb_drop_reason_SKB_DROP_REASON_VXLAN_VNI_NOT_FOUND changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `111`
- New: `108`

### Rust Evidence

- Graph edges: `1`

## W-000506 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_XDP
- Explanation: skb_drop_reason_SKB_DROP_REASON_XDP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `73`
- New: `69`

### Rust Evidence

- Graph edges: `1`

## W-000507 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_COMPACTFAIL
- Explanation: vm_event_item_COMPACTFAIL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `59`
- New: `46`

### Rust Evidence

- Graph edges: `1`

## W-000508 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_COMPACTFREE_SCANNED
- Explanation: vm_event_item_COMPACTFREE_SCANNED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `56`
- New: `43`

### Rust Evidence

- Graph edges: `1`

## W-000509 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_COMPACTISOLATED
- Explanation: vm_event_item_COMPACTISOLATED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `57`
- New: `44`

### Rust Evidence

- Graph edges: `1`

## W-000510 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_COMPACTMIGRATE_SCANNED
- Explanation: vm_event_item_COMPACTMIGRATE_SCANNED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `55`
- New: `42`

### Rust Evidence

- Graph edges: `1`

## W-000511 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_COMPACTSTALL
- Explanation: vm_event_item_COMPACTSTALL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `58`
- New: `45`

### Rust Evidence

- Graph edges: `1`

## W-000512 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_COMPACTSUCCESS
- Explanation: vm_event_item_COMPACTSUCCESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `60`
- New: `47`

### Rust Evidence

- Graph edges: `1`

## W-000513 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_DIRECT_MAP_LEVEL2_COLLAPSE
- Explanation: vm_event_item_DIRECT_MAP_LEVEL2_COLLAPSE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `79`
- New: `66`

### Rust Evidence

- Graph edges: `1`

## W-000514 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_DIRECT_MAP_LEVEL2_SPLIT
- Explanation: vm_event_item_DIRECT_MAP_LEVEL2_SPLIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `77`
- New: `64`

### Rust Evidence

- Graph edges: `1`

## W-000515 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_DIRECT_MAP_LEVEL3_COLLAPSE
- Explanation: vm_event_item_DIRECT_MAP_LEVEL3_COLLAPSE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `80`
- New: `67`

### Rust Evidence

- Graph edges: `1`

## W-000516 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_DIRECT_MAP_LEVEL3_SPLIT
- Explanation: vm_event_item_DIRECT_MAP_LEVEL3_SPLIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `78`
- New: `65`

### Rust Evidence

- Graph edges: `1`

## W-000517 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_DROP_PAGECACHE
- Explanation: vm_event_item_DROP_PAGECACHE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `47`
- New: `34`

### Rust Evidence

- Graph edges: `1`

## W-000518 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_DROP_SLAB
- Explanation: vm_event_item_DROP_SLAB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `35`

### Rust Evidence

- Graph edges: `1`

## W-000520 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_HTLB_BUDDY_PGALLOC_FAIL
- Explanation: vm_event_item_HTLB_BUDDY_PGALLOC_FAIL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `65`
- New: `52`

### Rust Evidence

- Graph edges: `1`

## W-000521 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KCOMPACTD_FREE_SCANNED
- Explanation: vm_event_item_KCOMPACTD_FREE_SCANNED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `63`
- New: `50`

### Rust Evidence

- Graph edges: `1`

## W-000522 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KCOMPACTD_MIGRATE_SCANNED
- Explanation: vm_event_item_KCOMPACTD_MIGRATE_SCANNED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `62`
- New: `49`

### Rust Evidence

- Graph edges: `1`

## W-000523 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KCOMPACTD_WAKE
- Explanation: vm_event_item_KCOMPACTD_WAKE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `61`
- New: `48`

### Rust Evidence

- Graph edges: `1`

## W-000524 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KSTACK_16K
- Explanation: vm_event_item_KSTACK_16K changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `85`
- New: `72`

### Rust Evidence

- Graph edges: `1`

## W-000525 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KSTACK_1K
- Explanation: vm_event_item_KSTACK_1K changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `81`
- New: `68`

### Rust Evidence

- Graph edges: `1`

## W-000526 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KSTACK_2K
- Explanation: vm_event_item_KSTACK_2K changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `82`
- New: `69`

### Rust Evidence

- Graph edges: `1`

## W-000527 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KSTACK_4K
- Explanation: vm_event_item_KSTACK_4K changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `83`
- New: `70`

### Rust Evidence

- Graph edges: `1`

## W-000528 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KSTACK_8K
- Explanation: vm_event_item_KSTACK_8K changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `84`
- New: `71`

### Rust Evidence

- Graph edges: `1`

## W-000529 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KSWAPD_HIGH_WMARK_HIT_QUICKLY
- Explanation: vm_event_item_KSWAPD_HIGH_WMARK_HIT_QUICKLY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `44`
- New: `31`

### Rust Evidence

- Graph edges: `1`

## W-000530 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KSWAPD_INODESTEAL
- Explanation: vm_event_item_KSWAPD_INODESTEAL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `42`
- New: `29`

### Rust Evidence

- Graph edges: `1`

## W-000531 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KSWAPD_LOW_WMARK_HIT_QUICKLY
- Explanation: vm_event_item_KSWAPD_LOW_WMARK_HIT_QUICKLY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `43`
- New: `30`

### Rust Evidence

- Graph edges: `1`

## W-000532 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_NR_VM_EVENT_ITEMS
- Explanation: vm_event_item_NR_VM_EVENT_ITEMS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `86`
- New: `73`

### Rust Evidence

- Graph edges: `1`

## W-000533 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_OOM_KILL
- Explanation: vm_event_item_OOM_KILL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `49`
- New: `36`

### Rust Evidence

- Graph edges: `1`

## W-000534 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PAGEOUTRUN
- Explanation: vm_event_item_PAGEOUTRUN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `45`
- New: `32`

### Rust Evidence

- Graph edges: `1`

## W-000535 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGINODESTEAL
- Explanation: vm_event_item_PGINODESTEAL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `40`
- New: `27`

### Rust Evidence

- Graph edges: `1`

## W-000536 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGMIGRATE_FAIL
- Explanation: vm_event_item_PGMIGRATE_FAIL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `51`
- New: `38`

### Rust Evidence

- Graph edges: `1`

## W-000537 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGMIGRATE_SUCCESS
- Explanation: vm_event_item_PGMIGRATE_SUCCESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `50`
- New: `37`

### Rust Evidence

- Graph edges: `1`

## W-000538 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGREUSE
- Explanation: vm_event_item_PGREUSE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `24`
- New: `23`

### Rust Evidence

- Graph edges: `1`

## W-000539 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGROTATED
- Explanation: vm_event_item_PGROTATED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `46`
- New: `33`

### Rust Evidence

- Graph edges: `1`

## W-000540 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGSCAN_DIRECT_THROTTLE
- Explanation: vm_event_item_PGSCAN_DIRECT_THROTTLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `33`
- New: `24`

### Rust Evidence

- Graph edges: `1`

## W-000541 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGSCAN_ZONE_RECLAIM_FAILED
- Explanation: vm_event_item_PGSCAN_ZONE_RECLAIM_FAILED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `39`
- New: `26`

### Rust Evidence

- Graph edges: `1`

## W-000542 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGSCAN_ZONE_RECLAIM_SUCCESS
- Explanation: vm_event_item_PGSCAN_ZONE_RECLAIM_SUCCESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `38`
- New: `25`

### Rust Evidence

- Graph edges: `1`

## W-000543 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_SLABS_SCANNED
- Explanation: vm_event_item_SLABS_SCANNED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `41`
- New: `28`

### Rust Evidence

- Graph edges: `1`

## W-000545 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_SWAP_RA_HIT
- Explanation: vm_event_item_SWAP_RA_HIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `74`
- New: `61`

### Rust Evidence

- Graph edges: `1`

## W-000546 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_SWPIN_ZERO
- Explanation: vm_event_item_SWPIN_ZERO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `75`
- New: `62`

### Rust Evidence

- Graph edges: `1`

## W-000547 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_SWPOUT_ZERO
- Explanation: vm_event_item_SWPOUT_ZERO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `76`
- New: `63`

### Rust Evidence

- Graph edges: `1`

## W-000548 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_THP_MIGRATION_FAIL
- Explanation: vm_event_item_THP_MIGRATION_FAIL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `53`
- New: `40`

### Rust Evidence

- Graph edges: `1`

## W-000549 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_THP_MIGRATION_SPLIT
- Explanation: vm_event_item_THP_MIGRATION_SPLIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `54`
- New: `41`

### Rust Evidence

- Graph edges: `1`

## W-000550 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_THP_MIGRATION_SUCCESS
- Explanation: vm_event_item_THP_MIGRATION_SUCCESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `52`
- New: `39`

### Rust Evidence

- Graph edges: `1`

## W-000551 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_UNEVICTABLE_PGCLEARED
- Explanation: vm_event_item_UNEVICTABLE_PGCLEARED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `71`
- New: `58`

### Rust Evidence

- Graph edges: `1`

## W-000552 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_UNEVICTABLE_PGCULLED
- Explanation: vm_event_item_UNEVICTABLE_PGCULLED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `66`
- New: `53`

### Rust Evidence

- Graph edges: `1`

## W-000553 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_UNEVICTABLE_PGMLOCKED
- Explanation: vm_event_item_UNEVICTABLE_PGMLOCKED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `69`
- New: `56`

### Rust Evidence

- Graph edges: `1`

## W-000554 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_UNEVICTABLE_PGMUNLOCKED
- Explanation: vm_event_item_UNEVICTABLE_PGMUNLOCKED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `70`
- New: `57`

### Rust Evidence

- Graph edges: `1`

## W-000555 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_UNEVICTABLE_PGRESCUED
- Explanation: vm_event_item_UNEVICTABLE_PGRESCUED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `68`
- New: `55`

### Rust Evidence

- Graph edges: `1`

## W-000556 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_UNEVICTABLE_PGSCANNED
- Explanation: vm_event_item_UNEVICTABLE_PGSCANNED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `67`
- New: `54`

### Rust Evidence

- Graph edges: `1`

## W-000557 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_UNEVICTABLE_PGSTRANDED
- Explanation: vm_event_item_UNEVICTABLE_PGSTRANDED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `72`
- New: `59`

### Rust Evidence

- Graph edges: `1`

## W-000558 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: wq_affn_scope_WQ_AFFN_NR_TYPES
- Explanation: wq_affn_scope_WQ_AFFN_NR_TYPES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `6`
- New: `7`

### Rust Evidence

- Graph edges: `1`

## W-000559 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: wq_affn_scope_WQ_AFFN_NUMA
- Explanation: wq_affn_scope_WQ_AFFN_NUMA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `4`
- New: `5`

### Rust Evidence

- Graph edges: `1`

## W-000560 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: wq_affn_scope_WQ_AFFN_SYSTEM
- Explanation: wq_affn_scope_WQ_AFFN_SYSTEM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `6`

### Rust Evidence

- Graph edges: `1`

## W-000610 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: VM_SPECIAL
- Explanation: VM_SPECIAL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `(VM_IO | VM_DONTEXPAND | VM_PFNMAP | VM_MIXEDMAP)`
- New: `vma_flags_to_legacy(VMA_SPECIAL_FLAGS)`

### Rust Evidence

- Graph edges: `1`

## W-000612 MacroConstDrift

- Risk: Medium
- Score: 7.6
- Symbol: __rust_helper
- Explanation: __rust_helper changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: ``
- New: `__always_inline`

### Rust Evidence

- Graph edges: `0`

## W-000561 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_CMU_BUS
- Explanation: CLK_DOUT_CMU_BUS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `11`

### Rust Evidence

- Graph edges: `0`

## W-000562 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_CMU_CORE_MAIN
- Explanation: CLK_DOUT_CMU_CORE_MAIN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `14`
- New: `13`

### Rust Evidence

- Graph edges: `0`

## W-000563 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_CMU_CPUCL_SWITCH
- Explanation: CLK_DOUT_CMU_CPUCL_SWITCH changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `14`

### Rust Evidence

- Graph edges: `0`

## W-000564 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_CMU_DLP_CORE
- Explanation: CLK_DOUT_CMU_DLP_CORE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `17`
- New: `15`

### Rust Evidence

- Graph edges: `0`

## W-000565 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_CMU_GPU_2D
- Explanation: CLK_DOUT_CMU_GPU_2D changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `23`
- New: `22`

### Rust Evidence

- Graph edges: `0`

## W-000566 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_CMU_GPU_3D
- Explanation: CLK_DOUT_CMU_GPU_3D changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `22`
- New: `21`

### Rust Evidence

- Graph edges: `0`

## W-000567 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_CMU_IMEM_ACLK
- Explanation: CLK_DOUT_CMU_IMEM_ACLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `24`
- New: `23`

### Rust Evidence

- Graph edges: `0`

## W-000568 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_CMU_MIF_BUSP
- Explanation: CLK_DOUT_CMU_MIF_BUSP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `27`
- New: `30`

### Rust Evidence

- Graph edges: `0`

## W-000569 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_CMU_MIF_SWITCH
- Explanation: CLK_DOUT_CMU_MIF_SWITCH changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `26`
- New: `29`

### Rust Evidence

- Graph edges: `0`

## W-000570 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_CMU_PERI_DISP
- Explanation: CLK_DOUT_CMU_PERI_DISP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `28`
- New: `31`

### Rust Evidence

- Graph edges: `0`

## W-000571 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_CMU_PERI_IP
- Explanation: CLK_DOUT_CMU_PERI_IP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `29`
- New: `32`

### Rust Evidence

- Graph edges: `0`

## W-000572 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_CMU_RSP_CORE
- Explanation: CLK_DOUT_CMU_RSP_CORE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `31`
- New: `33`

### Rust Evidence

- Graph edges: `0`

## W-000573 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_CMU_VIO_AUDIO
- Explanation: CLK_DOUT_CMU_VIO_AUDIO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `36`
- New: `40`

### Rust Evidence

- Graph edges: `0`

## W-000574 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_CMU_VIO_CORE
- Explanation: CLK_DOUT_CMU_VIO_CORE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `35`
- New: `36`

### Rust Evidence

- Graph edges: `0`

## W-000575 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_CPUCL_CLUSTER_ATCLK
- Explanation: CLK_DOUT_CPUCL_CLUSTER_ATCLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `12`

### Rust Evidence

- Graph edges: `0`

## W-000576 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_CPUCL_CMUREF
- Explanation: CLK_DOUT_CPUCL_CMUREF changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `11`

### Rust Evidence

- Graph edges: `0`

## W-000577 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_CPUCL_CPU
- Explanation: CLK_DOUT_CPUCL_CPU changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `4`
- New: `7`

### Rust Evidence

- Graph edges: `0`

## W-000578 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_CPUCL_DBG
- Explanation: CLK_DOUT_CPUCL_DBG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `11`
- New: `14`

### Rust Evidence

- Graph edges: `0`

## W-000579 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_PERI_PCLK
- Explanation: CLK_DOUT_PERI_PCLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `9`
- New: `4`

### Rust Evidence

- Graph edges: `0`

## W-000580 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_PERI_SPI
- Explanation: CLK_DOUT_PERI_SPI changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `6`
- New: `5`

### Rust Evidence

- Graph edges: `0`

## W-000581 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_PERI_UART1
- Explanation: CLK_DOUT_PERI_UART1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `7`
- New: `6`

### Rust Evidence

- Graph edges: `0`

## W-000582 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_PERI_UART2
- Explanation: CLK_DOUT_PERI_UART2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `7`

### Rust Evidence

- Graph edges: `0`

## W-000583 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_GOUT_CPUCL_CLUSTER_CPU
- Explanation: CLK_GOUT_CPUCL_CLUSTER_CPU changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `13`
- New: `16`

### Rust Evidence

- Graph edges: `0`

## W-000584 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_GOUT_CPUCL_CSSYS_IPCLKPORT_ATCLK
- Explanation: CLK_GOUT_CPUCL_CSSYS_IPCLKPORT_ATCLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `17`

### Rust Evidence

- Graph edges: `0`

## W-000585 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_GOUT_CPUCL_CSSYS_IPCLKPORT_PCLKDBG
- Explanation: CLK_GOUT_CPUCL_CSSYS_IPCLKPORT_PCLKDBG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `15`
- New: `18`

### Rust Evidence

- Graph edges: `0`

## W-000586 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_GOUT_CPUCL_SHORTSTOP
- Explanation: CLK_GOUT_CPUCL_SHORTSTOP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `14`
- New: `15`

### Rust Evidence

- Graph edges: `0`

## W-000587 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_GOUT_IMEM_PCLK_TMU0_APBIF
- Explanation: CLK_GOUT_IMEM_PCLK_TMU0_APBIF changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `6`
- New: `16`

### Rust Evidence

- Graph edges: `0`

## W-000588 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_GOUT_PERI_APB_ASYNC_DSIM_IPCLKPORT_PCLKS
- Explanation: CLK_GOUT_PERI_APB_ASYNC_DSIM_IPCLKPORT_PCLKS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `21`
- New: `18`

### Rust Evidence

- Graph edges: `0`

## W-000589 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_GOUT_PERI_DMA4DSIM_IPCLKPORT_CLK_APB_CLK
- Explanation: CLK_GOUT_PERI_DMA4DSIM_IPCLKPORT_CLK_APB_CLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `27`
- New: `8`

### Rust Evidence

- Graph edges: `0`

## W-000590 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_GOUT_PERI_DMA4DSIM_IPCLKPORT_CLK_AXI_CLK
- Explanation: CLK_GOUT_PERI_DMA4DSIM_IPCLKPORT_CLK_AXI_CLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `28`
- New: `9`

### Rust Evidence

- Graph edges: `0`

## W-000591 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_GOUT_PERI_I2C2_IPCLKPORT_I_PCLK
- Explanation: CLK_GOUT_PERI_I2C2_IPCLKPORT_I_PCLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `17`
- New: `19`

### Rust Evidence

- Graph edges: `0`

## W-000592 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_GOUT_PERI_I2C3_IPCLKPORT_I_PCLK
- Explanation: CLK_GOUT_PERI_I2C3_IPCLKPORT_I_PCLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `18`
- New: `20`

### Rust Evidence

- Graph edges: `0`

## W-000593 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_GOUT_PERI_SPI0_PCLK
- Explanation: CLK_GOUT_PERI_SPI0_PCLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `19`
- New: `21`

### Rust Evidence

- Graph edges: `0`

## W-000594 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_GOUT_PERI_SPI0_SCLK_SPI
- Explanation: CLK_GOUT_PERI_SPI0_SCLK_SPI changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `20`
- New: `22`

### Rust Evidence

- Graph edges: `0`

## W-000595 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_GOUT_PERI_UART1_PCLK
- Explanation: CLK_GOUT_PERI_UART1_PCLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `13`
- New: `23`

### Rust Evidence

- Graph edges: `0`

## W-000596 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_GOUT_PERI_UART1_SCLK_UART
- Explanation: CLK_GOUT_PERI_UART1_SCLK_UART changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `14`
- New: `24`

### Rust Evidence

- Graph edges: `0`

## W-000597 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_GOUT_PERI_UART2_PCLK
- Explanation: CLK_GOUT_PERI_UART2_PCLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `15`
- New: `25`

### Rust Evidence

- Graph edges: `0`

## W-000598 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_GOUT_PERI_UART2_SCLK_UART
- Explanation: CLK_GOUT_PERI_UART2_SCLK_UART changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `26`

### Rust Evidence

- Graph edges: `0`

## W-000599 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_MOUT_CPUCL_SWITCH_USER
- Explanation: CLK_MOUT_CPUCL_SWITCH_USER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `3`
- New: `6`

### Rust Evidence

- Graph edges: `0`

## W-000600 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_MOUT_PERI_DISP_USER
- Explanation: CLK_MOUT_PERI_DISP_USER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `2`

### Rust Evidence

- Graph edges: `0`

## W-000601 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: ETHTOOL_COALESCE_ALL_PARAMS
- Explanation: ETHTOOL_COALESCE_ALL_PARAMS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `GENMASK(28, 0)`
- New: `GENMASK(30, 0)`

### Rust Evidence

- Graph edges: `0`

## W-000602 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: I830_GMCH_GMS_LOCAL
- Explanation: I830_GMCH_GMS_LOCAL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x10`
- New: `(0x1 << 4)`

### Rust Evidence

- Graph edges: `0`

## W-000603 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: I830_GMCH_GMS_MASK
- Explanation: I830_GMCH_GMS_MASK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x70`
- New: `(0x7 << 4)`

### Rust Evidence

- Graph edges: `0`

## W-000604 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: I830_GMCH_GMS_STOLEN_1024
- Explanation: I830_GMCH_GMS_STOLEN_1024 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x30`
- New: `(0x3 << 4)`

### Rust Evidence

- Graph edges: `0`

## W-000605 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: I830_GMCH_GMS_STOLEN_512
- Explanation: I830_GMCH_GMS_STOLEN_512 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x20`
- New: `(0x2 << 4)`

### Rust Evidence

- Graph edges: `0`

## W-000606 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: I830_GMCH_GMS_STOLEN_8192
- Explanation: I830_GMCH_GMS_STOLEN_8192 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x40`
- New: `(0x4 << 4)`

### Rust Evidence

- Graph edges: `0`

## W-000607 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: I855_GMCH_GMS_MASK
- Explanation: I855_GMCH_GMS_MASK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0xF0`
- New: `(0xF << 4)`

### Rust Evidence

- Graph edges: `0`

## W-000608 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: I855_GMCH_GMS_STOLEN_0M
- Explanation: I855_GMCH_GMS_STOLEN_0M changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x0`
- New: `(0x0 << 4)`

### Rust Evidence

- Graph edges: `0`

## W-000609 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: TIF_RESTORE_SIGMASK
- Explanation: TIF_RESTORE_SIGMASK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10	// Restore signal mask in do_signal() */`
- New: `10	// Restore signal mask in do_signal()`

### Rust Evidence

- Graph edges: `0`

## W-000611 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: VM_STACK_FLAGS
- Explanation: VM_STACK_FLAGS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `(VM_STACK | VM_STACK_DEFAULT_FLAGS | VM_ACCOUNT)`
- New: `vma_flags_to_legacy(VMA_STACK_FLAGS)`

### Rust Evidence

- Graph edges: `0`

## W-000613 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: mk_vma_flags
- Explanation: mk_vma_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `__mk_vma_flags(COUNT_ARGS(__VA_ARGS__), \`
- New: `__mk_vma_flags(EMPTY_VMA_FLAGS,			\`

### Rust Evidence

- Graph edges: `0`
