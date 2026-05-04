# BindDrift Ranked Warnings

## W-000146 SignatureDrift

- Risk: High
- Score: 14.6
- Symbol: ioremap
- Explanation: ioremap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'offset', 'type': 'resource_size_t'}, {'name': 'size', 'type': 'ffi::c_ulong'}], 'return_type': '*mut ffi::c_void'}`
- New: `{'params': [{'name': 'offset', 'type': 'phys_addr_t'}, {'name': 'size', 'type': 'usize'}], 'return_type': '*mut ffi::c_void'}`

### Rust Evidence

- Graph edges: `40`

## W-000075 SignatureDrift

- Risk: High
- Score: 14.0
- Symbol: devm_platform_ioremap_resource
- Explanation: devm_platform_ioremap_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `17`

## W-000457 SignatureDrift

- Risk: High
- Score: 14.0
- Symbol: pci_unregister_driver
- Explanation: pci_unregister_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `17`

## W-000583 SignatureDrift

- Risk: High
- Score: 13.8
- Symbol: platform_set_drvdata
- Explanation: platform_set_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `16`

## W-000850 NullabilityDrift

- Risk: High
- Score: 13.2
- Symbol: devm_platform_ioremap_resource
- Explanation: devm_platform_ioremap_resource has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE', 'ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/include/linux/platform_device.h:91 `return ERR_PTR(-EINVAL);`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:283 `From<core::convert::Infallible>::to_result` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:278 `///     pdev: &mut PlatformDevice,`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:279 `///     index: u32,`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:280 `/// ) -> Result<*mut kernel::ffi::c_void> {`

## W-000851 NullabilityDrift

- Risk: High
- Score: 13.0
- Symbol: of_match_device
- Explanation: of_match_device has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/include/linux/of_device.h:69 `return NULL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/driver.rs:157 `of_id_info` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/driver.rs:154 `// SAFETY:`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/driver.rs:162 `// SAFETY: `DeviceId` is a `#[repr(transparent)` wrapper of `struct of_device_id` and`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/driver.rs:157 `AS_PTR`

## W-000640 SignatureDrift

- Risk: High
- Score: 12.8
- Symbol: transparent
- Explanation: transparent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `11`

## W-000656 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: cgroup
- Explanation: cgroup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'self_', 'type': 'cgroup_subsys_state'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'level', 'type': 'ffi::c_int'}, {'name': 'max_depth', 'type': 'ffi::c_int'}, {'name': 'nr_descendants', 'type': 'ffi::c_int'}, {'name': 'nr_dying_descendants', 'type': 'ffi::c_int'}, {'name': 'max_descendants', 'type': 'ffi::c_int'}, {'name': 'nr_populated_csets', 'type': 'ffi::c_int'}, {'name': 'nr_populated_domain_children', 'type': 'ffi::c_int'}, {'name': 'nr_populated_threaded_children', 'type': 'ffi::c_int'}, {'name': 'nr_threaded_children', 'type': 'ffi::c_int'}, {'name': 'kn', 'type': '*mut kernfs_node'}, {'name': 'procs_file', 'type': 'cgroup_file'}, {'name': 'events_file', 'type': 'cgroup_file'}, {'name': 'psi_files', 'type': '__IncompleteArrayField<cgroup_file>'}, {'name': 'subtree_control', 'type': 'u16_'}, {'name': 'subtree_ss_mask', 'type': 'u16_'}, {'name': 'old_subtree_control', 'type': 'u16_'}, {'name': 'old_subtree_ss_mask', 'type': 'u16_'}, {'name': 'subsys', 'type': '[*mut cgroup_subsys_state; 14usize]'}, {'name': 'nr_dying_subsys', 'type': '[ffi::c_int; 14usize]'}, {'name': 'root', 'type': '*mut cgroup_root'}, {'name': 'cset_links', 'type': 'list_head'}, {'name': 'e_csets', 'type': '[list_head; 14usize]'}, {'name': 'dom_cgrp', 'type': '*mut cgroup'}, {'name': 'old_dom_cgrp', 'type': '*mut cgroup'}, {'name': 'rstat_cpu', 'type': '*mut cgroup_rstat_cpu'}, {'name': 'rstat_css_list', 'type': 'list_head'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': '_pad_', 'type': 'cacheline_padding'}, {'name': 'rstat_flush_next', 'type': '*mut cgroup'}, {'name': 'last_bstat', 'type': 'cgroup_base_stat'}, {'name': 'bstat', 'type': 'cgroup_base_stat'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'pidlists', 'type': 'list_head'}, {'name': 'pidlist_mutex', 'type': 'mutex'}, {'name': 'offline_waitq', 'type': 'wait_queue_head_t'}, {'name': 'release_agent_work', 'type': 'work_struct'}, {'name': 'psi', 'type': '*mut psi_group'}, {'name': 'bpf', 'type': 'cgroup_bpf'}, {'name': 'freezer', 'type': 'cgroup_freezer_state'}, {'name': 'ancestors', 'type': '__IncompleteArrayField<*mut cgroup>'}]`
- New: `[{'name': 'self_', 'type': 'cgroup_subsys_state'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'level', 'type': 'ffi::c_int'}, {'name': 'max_depth', 'type': 'ffi::c_int'}, {'name': 'nr_descendants', 'type': 'ffi::c_int'}, {'name': 'nr_dying_descendants', 'type': 'ffi::c_int'}, {'name': 'max_descendants', 'type': 'ffi::c_int'}, {'name': 'nr_populated_csets', 'type': 'ffi::c_int'}, {'name': 'nr_populated_domain_children', 'type': 'ffi::c_int'}, {'name': 'nr_populated_threaded_children', 'type': 'ffi::c_int'}, {'name': 'nr_threaded_children', 'type': 'ffi::c_int'}, {'name': 'kill_seq', 'type': 'ffi::c_uint'}, {'name': 'kn', 'type': '*mut kernfs_node'}, {'name': 'procs_file', 'type': 'cgroup_file'}, {'name': 'events_file', 'type': 'cgroup_file'}, {'name': 'psi_files', 'type': '__IncompleteArrayField<cgroup_file>'}, {'name': 'subtree_control', 'type': 'u16_'}, {'name': 'subtree_ss_mask', 'type': 'u16_'}, {'name': 'old_subtree_control', 'type': 'u16_'}, {'name': 'old_subtree_ss_mask', 'type': 'u16_'}, {'name': 'subsys', 'type': '[*mut cgroup_subsys_state; 14usize]'}, {'name': 'nr_dying_subsys', 'type': '[ffi::c_int; 14usize]'}, {'name': 'root', 'type': '*mut cgroup_root'}, {'name': 'cset_links', 'type': 'list_head'}, {'name': 'e_csets', 'type': '[list_head; 14usize]'}, {'name': 'dom_cgrp', 'type': '*mut cgroup'}, {'name': 'old_dom_cgrp', 'type': '*mut cgroup'}, {'name': 'rstat_cpu', 'type': '*mut cgroup_rstat_cpu'}, {'name': 'rstat_css_list', 'type': 'list_head'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': '_pad_', 'type': 'cacheline_padding'}, {'name': 'rstat_flush_next', 'type': '*mut cgroup'}, {'name': 'last_bstat', 'type': 'cgroup_base_stat'}, {'name': 'bstat', 'type': 'cgroup_base_stat'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'pidlists', 'type': 'list_head'}, {'name': 'pidlist_mutex', 'type': 'mutex'}, {'name': 'offline_waitq', 'type': 'wait_queue_head_t'}, {'name': 'release_agent_work', 'type': 'work_struct'}, {'name': 'psi', 'type': '*mut psi_group'}, {'name': 'bpf', 'type': 'cgroup_bpf'}, {'name': 'freezer', 'type': 'cgroup_freezer_state'}, {'name': 'ancestors', 'type': '__IncompleteArrayField<*mut cgroup>'}]`

### Rust Evidence

- Graph edges: `50`

## W-000665 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: inode
- Explanation: inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'i_mode', 'type': 'umode_t'}, {'name': 'i_opflags', 'type': 'ffi::c_ushort'}, {'name': 'i_uid', 'type': 'kuid_t'}, {'name': 'i_gid', 'type': 'kgid_t'}, {'name': 'i_flags', 'type': 'ffi::c_uint'}, {'name': 'i_acl', 'type': '*mut posix_acl'}, {'name': 'i_default_acl', 'type': '*mut posix_acl'}, {'name': 'i_op', 'type': '*const inode_operations'}, {'name': 'i_sb', 'type': '*mut super_block'}, {'name': 'i_mapping', 'type': '*mut address_space'}, {'name': 'i_security', 'type': '*mut ffi::c_void'}, {'name': 'i_ino', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'inode__bindgen_ty_1'}, {'name': 'i_rdev', 'type': 'dev_t'}, {'name': 'i_size', 'type': 'loff_t'}, {'name': 'i_atime_sec', 'type': 'time64_t'}, {'name': 'i_mtime_sec', 'type': 'time64_t'}, {'name': 'i_ctime_sec', 'type': 'time64_t'}, {'name': 'i_atime_nsec', 'type': 'u32_'}, {'name': 'i_mtime_nsec', 'type': 'u32_'}, {'name': 'i_ctime_nsec', 'type': 'u32_'}, {'name': 'i_generation', 'type': 'u32_'}, {'name': 'i_lock', 'type': 'spinlock_t'}, {'name': 'i_bytes', 'type': 'ffi::c_ushort'}, {'name': 'i_blkbits', 'type': 'u8_'}, {'name': 'i_write_hint', 'type': 'rw_hint'}, {'name': 'i_blocks', 'type': 'blkcnt_t'}, {'name': 'i_state', 'type': 'u32_'}, {'name': 'i_rwsem', 'type': 'rw_semaphore'}, {'name': 'dirtied_when', 'type': 'ffi::c_ulong'}, {'name': 'dirtied_time_when', 'type': 'ffi::c_ulong'}, {'name': 'i_hash', 'type': 'hlist_node'}, {'name': 'i_io_list', 'type': 'list_head'}, {'name': 'i_lru', 'type': 'list_head'}, {'name': 'i_sb_list', 'type': 'list_head'}, {'name': 'i_wb_list', 'type': 'list_head'}, {'name': '__bindgen_anon_2', 'type': 'inode__bindgen_ty_2'}, {'name': 'i_version', 'type': 'atomic64_t'}, {'name': 'i_sequence', 'type': 'atomic64_t'}, {'name': 'i_count', 'type': 'atomic_t'}, {'name': 'i_dio_count', 'type': 'atomic_t'}, {'name': 'i_writecount', 'type': 'atomic_t'}, {'name': 'i_readcount', 'type': 'atomic_t'}, {'name': '__bindgen_anon_3', 'type': 'inode__bindgen_ty_3'}, {'name': 'i_flctx', 'type': '*mut file_lock_context'}, {'name': 'i_data', 'type': 'address_space'}, {'name': 'i_devices', 'type': 'list_head'}, {'name': '__bindgen_anon_4', 'type': 'inode__bindgen_ty_4'}, {'name': 'i_fsnotify_mask', 'type': '__u32'}, {'name': 'i_fsnotify_marks', 'type': '*mut fsnotify_mark_connector'}, {'name': 'i_private', 'type': '*mut ffi::c_void'}]`
- New: `[{'name': 'i_mode', 'type': 'umode_t'}, {'name': 'i_opflags', 'type': 'ffi::c_ushort'}, {'name': 'i_uid', 'type': 'kuid_t'}, {'name': 'i_gid', 'type': 'kgid_t'}, {'name': 'i_flags', 'type': 'ffi::c_uint'}, {'name': 'i_acl', 'type': '*mut posix_acl'}, {'name': 'i_default_acl', 'type': '*mut posix_acl'}, {'name': 'i_op', 'type': '*const inode_operations'}, {'name': 'i_sb', 'type': '*mut super_block'}, {'name': 'i_mapping', 'type': '*mut address_space'}, {'name': 'i_security', 'type': '*mut ffi::c_void'}, {'name': 'i_ino', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'inode__bindgen_ty_1'}, {'name': 'i_rdev', 'type': 'dev_t'}, {'name': 'i_size', 'type': 'loff_t'}, {'name': 'i_atime_sec', 'type': 'time64_t'}, {'name': 'i_mtime_sec', 'type': 'time64_t'}, {'name': 'i_ctime_sec', 'type': 'time64_t'}, {'name': 'i_atime_nsec', 'type': 'u32_'}, {'name': 'i_mtime_nsec', 'type': 'u32_'}, {'name': 'i_ctime_nsec', 'type': 'u32_'}, {'name': 'i_generation', 'type': 'u32_'}, {'name': 'i_lock', 'type': 'spinlock_t'}, {'name': 'i_bytes', 'type': 'ffi::c_ushort'}, {'name': 'i_blkbits', 'type': 'u8_'}, {'name': 'i_write_hint', 'type': 'rw_hint'}, {'name': 'i_blocks', 'type': 'blkcnt_t'}, {'name': 'i_state', 'type': 'u32_'}, {'name': 'i_rwsem', 'type': 'rw_semaphore'}, {'name': 'dirtied_when', 'type': 'ffi::c_ulong'}, {'name': 'dirtied_time_when', 'type': 'ffi::c_ulong'}, {'name': 'i_hash', 'type': 'hlist_node'}, {'name': 'i_io_list', 'type': 'list_head'}, {'name': 'i_lru', 'type': 'list_head'}, {'name': 'i_sb_list', 'type': 'list_head'}, {'name': 'i_wb_list', 'type': 'list_head'}, {'name': '__bindgen_anon_2', 'type': 'inode__bindgen_ty_2'}, {'name': 'i_version', 'type': 'atomic64_t'}, {'name': 'i_sequence', 'type': 'atomic64_t'}, {'name': 'i_count', 'type': 'atomic_t'}, {'name': 'i_dio_count', 'type': 'atomic_t'}, {'name': 'i_writecount', 'type': 'atomic_t'}, {'name': 'i_readcount', 'type': 'atomic_t'}, {'name': '__bindgen_anon_3', 'type': 'inode__bindgen_ty_3'}, {'name': 'i_flctx', 'type': '*mut file_lock_context'}, {'name': 'i_data', 'type': 'address_space'}, {'name': '__bindgen_anon_4', 'type': 'inode__bindgen_ty_4'}, {'name': '__bindgen_anon_5', 'type': 'inode__bindgen_ty_5'}, {'name': 'i_fsnotify_mask', 'type': '__u32'}, {'name': 'i_fsnotify_marks', 'type': '*mut fsnotify_mark_connector'}, {'name': 'i_private', 'type': '*mut ffi::c_void'}]`

### Rust Evidence

- Graph edges: `48`

## W-000673 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: module
- Explanation: module changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'state', 'type': 'module_state'}, {'name': 'list', 'type': 'list_head'}, {'name': 'name', 'type': '[ffi::c_char; 56usize]'}, {'name': 'mkobj', 'type': 'module_kobject'}, {'name': 'modinfo_attrs', 'type': '*mut module_attribute'}, {'name': 'version', 'type': '*const ffi::c_char'}, {'name': 'srcversion', 'type': '*const ffi::c_char'}, {'name': 'holders_dir', 'type': '*mut kobject'}, {'name': 'syms', 'type': '*mut kernel_symbol'}, {'name': 'crcs', 'type': '*const s32'}, {'name': 'num_syms', 'type': 'ffi::c_uint'}, {'name': 'param_lock', 'type': 'mutex'}, {'name': 'kp', 'type': '*mut kernel_param'}, {'name': 'num_kp', 'type': 'ffi::c_uint'}, {'name': 'num_gpl_syms', 'type': 'ffi::c_uint'}, {'name': 'gpl_syms', 'type': '*const kernel_symbol'}, {'name': 'gpl_crcs', 'type': '*const s32'}, {'name': 'using_gplonly_symbols', 'type': 'bool_'}, {'name': 'async_probe_requested', 'type': 'bool_'}, {'name': 'num_exentries', 'type': 'ffi::c_uint'}, {'name': 'extable', 'type': '*mut exception_table_entry'}, {'name': 'init', 'type': '::core::option::Option<unsafe extern "C" fn() -> ffi::c_int>'}, {'name': 'mem', 'type': '[module_memory; 7usize]'}, {'name': 'arch', 'type': 'mod_arch_specific'}, {'name': 'taints', 'type': 'ffi::c_ulong'}, {'name': 'num_bugs', 'type': 'ffi::c_uint'}, {'name': 'bug_list', 'type': 'list_head'}, {'name': 'bug_table', 'type': '*mut bug_entry'}, {'name': 'kallsyms', 'type': '*mut mod_kallsyms'}, {'name': 'core_kallsyms', 'type': 'mod_kallsyms'}, {'name': 'sect_attrs', 'type': '*mut module_sect_attrs'}, {'name': 'notes_attrs', 'type': '*mut module_notes_attrs'}, {'name': 'args', 'type': '*mut ffi::c_char'}, {'name': 'percpu', 'type': '*mut ffi::c_void'}, {'name': 'percpu_size', 'type': 'ffi::c_uint'}, {'name': 'noinstr_text_start', 'type': '*mut ffi::c_void'}, {'name': 'noinstr_text_size', 'type': 'ffi::c_uint'}, {'name': 'num_tracepoints', 'type': 'ffi::c_uint'}, {'name': 'tracepoints_ptrs', 'type': '*const ffi::c_int'}, {'name': 'num_srcu_structs', 'type': 'ffi::c_uint'}, {'name': 'srcu_struct_ptrs', 'type': '*mut *mut srcu_struct'}, {'name': 'jump_entries', 'type': '*mut jump_entry'}, {'name': 'num_jump_entries', 'type': 'ffi::c_uint'}, {'name': 'num_trace_bprintk_fmt', 'type': 'ffi::c_uint'}, {'name': 'trace_bprintk_fmt_start', 'type': '*mut *const ffi::c_char'}, {'name': 'trace_events', 'type': '*mut *mut trace_event_call'}, {'name': 'num_trace_events', 'type': 'ffi::c_uint'}, {'name': 'trace_evals', 'type': '*mut *mut trace_eval_map'}, {'name': 'num_trace_evals', 'type': 'ffi::c_uint'}, {'name': 'kprobes_text_start', 'type': '*mut ffi::c_void'}, {'name': 'kprobes_text_size', 'type': 'ffi::c_uint'}, {'name': 'kprobe_blacklist', 'type': '*mut ffi::c_ulong'}, {'name': 'num_kprobe_blacklist', 'type': 'ffi::c_uint'}, {'name': 'num_static_call_sites', 'type': 'ffi::c_int'}, {'name': 'static_call_sites', 'type': '*mut static_call_site'}, {'name': 'source_list', 'type': 'list_head'}, {'name': 'target_list', 'type': 'list_head'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'refcnt', 'type': 'atomic_t'}]`
- New: `[{'name': 'state', 'type': 'module_state'}, {'name': 'list', 'type': 'list_head'}, {'name': 'name', 'type': '[ffi::c_char; 56usize]'}, {'name': 'mkobj', 'type': 'module_kobject'}, {'name': 'modinfo_attrs', 'type': '*mut module_attribute'}, {'name': 'version', 'type': '*const ffi::c_char'}, {'name': 'srcversion', 'type': '*const ffi::c_char'}, {'name': 'holders_dir', 'type': '*mut kobject'}, {'name': 'syms', 'type': '*mut kernel_symbol'}, {'name': 'crcs', 'type': '*const u32_'}, {'name': 'num_syms', 'type': 'ffi::c_uint'}, {'name': 'param_lock', 'type': 'mutex'}, {'name': 'kp', 'type': '*mut kernel_param'}, {'name': 'num_kp', 'type': 'ffi::c_uint'}, {'name': 'num_gpl_syms', 'type': 'ffi::c_uint'}, {'name': 'gpl_syms', 'type': '*const kernel_symbol'}, {'name': 'gpl_crcs', 'type': '*const u32_'}, {'name': 'using_gplonly_symbols', 'type': 'bool_'}, {'name': 'async_probe_requested', 'type': 'bool_'}, {'name': 'num_exentries', 'type': 'ffi::c_uint'}, {'name': 'extable', 'type': '*mut exception_table_entry'}, {'name': 'init', 'type': '::core::option::Option<unsafe extern "C" fn() -> ffi::c_int>'}, {'name': 'mem', 'type': '[module_memory; 7usize]'}, {'name': 'arch', 'type': 'mod_arch_specific'}, {'name': 'taints', 'type': 'ffi::c_ulong'}, {'name': 'num_bugs', 'type': 'ffi::c_uint'}, {'name': 'bug_list', 'type': 'list_head'}, {'name': 'bug_table', 'type': '*mut bug_entry'}, {'name': 'kallsyms', 'type': '*mut mod_kallsyms'}, {'name': 'core_kallsyms', 'type': 'mod_kallsyms'}, {'name': 'sect_attrs', 'type': '*mut module_sect_attrs'}, {'name': 'notes_attrs', 'type': '*mut module_notes_attrs'}, {'name': 'args', 'type': '*mut ffi::c_char'}, {'name': 'percpu', 'type': '*mut ffi::c_void'}, {'name': 'percpu_size', 'type': 'ffi::c_uint'}, {'name': 'noinstr_text_start', 'type': '*mut ffi::c_void'}, {'name': 'noinstr_text_size', 'type': 'ffi::c_uint'}, {'name': 'num_tracepoints', 'type': 'ffi::c_uint'}, {'name': 'tracepoints_ptrs', 'type': '*const ffi::c_int'}, {'name': 'num_srcu_structs', 'type': 'ffi::c_uint'}, {'name': 'srcu_struct_ptrs', 'type': '*mut *mut srcu_struct'}, {'name': 'jump_entries', 'type': '*mut jump_entry'}, {'name': 'num_jump_entries', 'type': 'ffi::c_uint'}, {'name': 'num_trace_bprintk_fmt', 'type': 'ffi::c_uint'}, {'name': 'trace_bprintk_fmt_start', 'type': '*mut *const ffi::c_char'}, {'name': 'trace_events', 'type': '*mut *mut trace_event_call'}, {'name': 'num_trace_events', 'type': 'ffi::c_uint'}, {'name': 'trace_evals', 'type': '*mut *mut trace_eval_map'}, {'name': 'num_trace_evals', 'type': 'ffi::c_uint'}, {'name': 'kprobes_text_start', 'type': '*mut ffi::c_void'}, {'name': 'kprobes_text_size', 'type': 'ffi::c_uint'}, {'name': 'kprobe_blacklist', 'type': '*mut ffi::c_ulong'}, {'name': 'num_kprobe_blacklist', 'type': 'ffi::c_uint'}, {'name': 'num_static_call_sites', 'type': 'ffi::c_int'}, {'name': 'static_call_sites', 'type': '*mut static_call_site'}, {'name': 'source_list', 'type': 'list_head'}, {'name': 'target_list', 'type': 'list_head'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'refcnt', 'type': 'atomic_t'}]`

### Rust Evidence

- Graph edges: `41`

## W-000675 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: pci_bus
- Explanation: pci_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'node', 'type': 'list_head'}, {'name': 'parent', 'type': '*mut pci_bus'}, {'name': 'children', 'type': 'list_head'}, {'name': 'devices', 'type': 'list_head'}, {'name': 'self_', 'type': '*mut pci_dev'}, {'name': 'slots', 'type': 'list_head'}, {'name': 'resource', 'type': '[*mut resource; 4usize]'}, {'name': 'resources', 'type': 'list_head'}, {'name': 'busn_res', 'type': 'resource'}, {'name': 'ops', 'type': '*mut pci_ops'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procdir', 'type': '*mut proc_dir_entry'}, {'name': 'number', 'type': 'ffi::c_uchar'}, {'name': 'primary', 'type': 'ffi::c_uchar'}, {'name': 'max_bus_speed', 'type': 'ffi::c_uchar'}, {'name': 'cur_bus_speed', 'type': 'ffi::c_uchar'}, {'name': 'name', 'type': '[ffi::c_char; 48usize]'}, {'name': 'bridge_ctl', 'type': 'ffi::c_ushort'}, {'name': 'bus_flags', 'type': 'pci_bus_flags_t'}, {'name': 'bridge', 'type': '*mut device'}, {'name': 'dev', 'type': 'device'}, {'name': 'legacy_io', 'type': '*mut bin_attribute'}, {'name': 'legacy_mem', 'type': '*mut bin_attribute'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 7usize]'}]`

### Rust Evidence

- Graph edges: `50`

## W-000676 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: pci_dev
- Explanation: pci_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 11usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': 'match_driver', 'type': 'bool_'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 5usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pri_cap', 'type': 'u16_'}, {'name': 'pri_reqs_alloc', 'type': 'u32_'}, {'name': '_bitfield_align_5', 'type': '[u8; 0]'}, {'name': '_bitfield_5', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`

### Rust Evidence

- Graph edges: `50`

## W-000677 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: phy_driver
- Explanation: phy_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mdiodrv', 'type': 'mdio_driver_common'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'name', 'type': '*mut ffi::c_char'}, {'name': 'phy_id_mask', 'type': 'u32_'}, {'name': 'features', 'type': '*const ffi::c_ulong'}, {'name': 'flags', 'type': 'u32_'}, {'name': 'driver_data', 'type': '*const ffi::c_void'}, {'name': 'probe', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device) -> ffi::c_int>'}, {'name': 'get_rate_matching', 'type': '::core::option::Option<'}, {'name': 'resume', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device) -> ffi::c_int>'}, {'name': 'remove', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device)>'}, {'name': 'set_wol', 'type': '::core::option::Option<'}, {'name': 'get_wol', 'type': '::core::option::Option<'}, {'name': 'link_change_notify', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device)>'}, {'name': 'read_mmd', 'type': '::core::option::Option<'}, {'name': 'write_mmd', 'type': '::core::option::Option<'}, {'name': 'read_page', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device) -> ffi::c_int>'}, {'name': 'write_page', 'type': '::core::option::Option<'}, {'name': 'module_info', 'type': '::core::option::Option<'}, {'name': 'module_eeprom', 'type': '::core::option::Option<'}, {'name': 'cable_test_tdr_start', 'type': '::core::option::Option<'}, {'name': 'cable_test_get_status', 'type': '::core::option::Option<'}, {'name': 'get_stats', 'type': '::core::option::Option<'}, {'name': 'get_tunable', 'type': '::core::option::Option<'}, {'name': 'set_tunable', 'type': '::core::option::Option<'}, {'name': 'set_loopback', 'type': '::core::option::Option<'}, {'name': 'get_sqi', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device) -> ffi::c_int>'}, {'name': 'get_plca_cfg', 'type': '::core::option::Option<'}, {'name': 'set_plca_cfg', 'type': '::core::option::Option<'}, {'name': 'get_plca_status', 'type': '::core::option::Option<'}, {'name': 'led_brightness_set', 'type': '::core::option::Option<'}, {'name': 'led_blink_set', 'type': '::core::option::Option<'}, {'name': 'led_hw_is_supported', 'type': '::core::option::Option<'}, {'name': 'led_hw_control_set', 'type': '::core::option::Option<'}, {'name': 'led_hw_control_get', 'type': '::core::option::Option<'}, {'name': 'led_polarity_set', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'mdiodrv', 'type': 'mdio_driver_common'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'name', 'type': '*mut ffi::c_char'}, {'name': 'phy_id_mask', 'type': 'u32_'}, {'name': 'features', 'type': '*const ffi::c_ulong'}, {'name': 'flags', 'type': 'u32_'}, {'name': 'driver_data', 'type': '*const ffi::c_void'}, {'name': 'probe', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device) -> ffi::c_int>'}, {'name': 'inband_caps', 'type': '::core::option::Option<'}, {'name': 'config_inband', 'type': '::core::option::Option<'}, {'name': 'get_rate_matching', 'type': '::core::option::Option<'}, {'name': 'resume', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device) -> ffi::c_int>'}, {'name': 'remove', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device)>'}, {'name': 'set_wol', 'type': '::core::option::Option<'}, {'name': 'get_wol', 'type': '::core::option::Option<'}, {'name': 'link_change_notify', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device)>'}, {'name': 'read_mmd', 'type': '::core::option::Option<'}, {'name': 'write_mmd', 'type': '::core::option::Option<'}, {'name': 'read_page', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device) -> ffi::c_int>'}, {'name': 'write_page', 'type': '::core::option::Option<'}, {'name': 'module_info', 'type': '::core::option::Option<'}, {'name': 'module_eeprom', 'type': '::core::option::Option<'}, {'name': 'cable_test_tdr_start', 'type': '::core::option::Option<'}, {'name': 'cable_test_get_status', 'type': '::core::option::Option<'}, {'name': 'get_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_link_stats', 'type': '::core::option::Option<'}, {'name': 'get_stats', 'type': '::core::option::Option<'}, {'name': 'get_tunable', 'type': '::core::option::Option<'}, {'name': 'set_tunable', 'type': '::core::option::Option<'}, {'name': 'set_loopback', 'type': '::core::option::Option<'}, {'name': 'get_sqi', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device) -> ffi::c_int>'}, {'name': 'get_plca_cfg', 'type': '::core::option::Option<'}, {'name': 'set_plca_cfg', 'type': '::core::option::Option<'}, {'name': 'get_plca_status', 'type': '::core::option::Option<'}, {'name': 'led_brightness_set', 'type': '::core::option::Option<'}, {'name': 'led_blink_set', 'type': '::core::option::Option<'}, {'name': 'led_hw_is_supported', 'type': '::core::option::Option<'}, {'name': 'led_hw_control_set', 'type': '::core::option::Option<'}, {'name': 'led_hw_control_get', 'type': '::core::option::Option<'}, {'name': 'led_polarity_set', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `25`

## W-000678 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: pid
- Explanation: pid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'count', 'type': 'refcount_t'}, {'name': 'level', 'type': 'ffi::c_uint'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'stashed', 'type': '*mut dentry'}, {'name': 'ino', 'type': 'u64_'}, {'name': 'tasks', 'type': '[hlist_head; 4usize]'}, {'name': 'inodes', 'type': 'hlist_head'}, {'name': 'wait_pidfd', 'type': 'wait_queue_head_t'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'numbers', 'type': '__IncompleteArrayField<upid>'}]`
- New: `[{'name': 'count', 'type': 'refcount_t'}, {'name': 'level', 'type': 'ffi::c_uint'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'stashed', 'type': '*mut dentry'}, {'name': 'ino', 'type': 'u64_'}, {'name': 'pidfs_node', 'type': 'rb_node'}, {'name': 'tasks', 'type': '[hlist_head; 4usize]'}, {'name': 'inodes', 'type': 'hlist_head'}, {'name': 'wait_pidfd', 'type': 'wait_queue_head_t'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'numbers', 'type': '__IncompleteArrayField<upid>'}]`

### Rust Evidence

- Graph edges: `26`

## W-000679 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: pid_namespace
- Explanation: pid_namespace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'idr', 'type': 'idr'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'pid_allocated', 'type': 'ffi::c_uint'}, {'name': 'child_reaper', 'type': '*mut task_struct'}, {'name': 'pid_cachep', 'type': '*mut kmem_cache'}, {'name': 'level', 'type': 'ffi::c_uint'}, {'name': 'parent', 'type': '*mut pid_namespace'}, {'name': 'bacct', 'type': '*mut fs_pin'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'ucounts', 'type': '*mut ucounts'}, {'name': 'reboot', 'type': 'ffi::c_int'}, {'name': 'ns', 'type': 'ns_common'}, {'name': 'memfd_noexec_scope', 'type': 'ffi::c_int'}]`
- New: `[{'name': 'idr', 'type': 'idr'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'pid_allocated', 'type': 'ffi::c_uint'}, {'name': 'child_reaper', 'type': '*mut task_struct'}, {'name': 'pid_cachep', 'type': '*mut kmem_cache'}, {'name': 'level', 'type': 'ffi::c_uint'}, {'name': 'pid_max', 'type': 'ffi::c_int'}, {'name': 'parent', 'type': '*mut pid_namespace'}, {'name': 'bacct', 'type': '*mut fs_pin'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'ucounts', 'type': '*mut ucounts'}, {'name': 'reboot', 'type': 'ffi::c_int'}, {'name': 'ns', 'type': 'ns_common'}, {'name': 'work', 'type': 'work_struct'}, {'name': 'set', 'type': 'ctl_table_set'}, {'name': 'sysctls', 'type': '*mut ctl_table_header'}, {'name': 'memfd_noexec_scope', 'type': 'ffi::c_int'}]`

### Rust Evidence

- Graph edges: `24`

## W-000680 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: platform_device
- Explanation: platform_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'id_auto', 'type': 'bool_'}, {'name': 'dev', 'type': 'device'}, {'name': 'platform_dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'num_resources', 'type': 'u32_'}, {'name': 'resource', 'type': '*mut resource'}, {'name': 'id_entry', 'type': '*const platform_device_id'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'mfd_cell', 'type': '*mut mfd_cell'}, {'name': 'archdata', 'type': 'pdev_archdata'}]`

### Rust Evidence

- Graph edges: `36`

## W-000688 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: statx
- Explanation: statx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'stx_mask', 'type': '__u32'}, {'name': 'stx_blksize', 'type': '__u32'}, {'name': 'stx_attributes', 'type': '__u64'}, {'name': 'stx_nlink', 'type': '__u32'}, {'name': 'stx_uid', 'type': '__u32'}, {'name': 'stx_gid', 'type': '__u32'}, {'name': 'stx_mode', 'type': '__u16'}, {'name': '__spare0', 'type': '[__u16; 1usize]'}, {'name': 'stx_ino', 'type': '__u64'}, {'name': 'stx_size', 'type': '__u64'}, {'name': 'stx_blocks', 'type': '__u64'}, {'name': 'stx_attributes_mask', 'type': '__u64'}, {'name': 'stx_atime', 'type': 'statx_timestamp'}, {'name': 'stx_btime', 'type': 'statx_timestamp'}, {'name': 'stx_ctime', 'type': 'statx_timestamp'}, {'name': 'stx_mtime', 'type': 'statx_timestamp'}, {'name': 'stx_rdev_major', 'type': '__u32'}, {'name': 'stx_rdev_minor', 'type': '__u32'}, {'name': 'stx_dev_major', 'type': '__u32'}, {'name': 'stx_dev_minor', 'type': '__u32'}, {'name': 'stx_mnt_id', 'type': '__u64'}, {'name': 'stx_dio_mem_align', 'type': '__u32'}, {'name': 'stx_dio_offset_align', 'type': '__u32'}, {'name': 'stx_subvol', 'type': '__u64'}, {'name': 'stx_atomic_write_unit_min', 'type': '__u32'}, {'name': 'stx_atomic_write_unit_max', 'type': '__u32'}, {'name': 'stx_atomic_write_segments_max', 'type': '__u32'}, {'name': '__spare1', 'type': '[__u32; 1usize]'}, {'name': '__spare3', 'type': '[__u64; 9usize]'}]`
- New: `[{'name': 'stx_mask', 'type': '__u32'}, {'name': 'stx_blksize', 'type': '__u32'}, {'name': 'stx_attributes', 'type': '__u64'}, {'name': 'stx_nlink', 'type': '__u32'}, {'name': 'stx_uid', 'type': '__u32'}, {'name': 'stx_gid', 'type': '__u32'}, {'name': 'stx_mode', 'type': '__u16'}, {'name': '__spare0', 'type': '[__u16; 1usize]'}, {'name': 'stx_ino', 'type': '__u64'}, {'name': 'stx_size', 'type': '__u64'}, {'name': 'stx_blocks', 'type': '__u64'}, {'name': 'stx_attributes_mask', 'type': '__u64'}, {'name': 'stx_atime', 'type': 'statx_timestamp'}, {'name': 'stx_btime', 'type': 'statx_timestamp'}, {'name': 'stx_ctime', 'type': 'statx_timestamp'}, {'name': 'stx_mtime', 'type': 'statx_timestamp'}, {'name': 'stx_rdev_major', 'type': '__u32'}, {'name': 'stx_rdev_minor', 'type': '__u32'}, {'name': 'stx_dev_major', 'type': '__u32'}, {'name': 'stx_dev_minor', 'type': '__u32'}, {'name': 'stx_mnt_id', 'type': '__u64'}, {'name': 'stx_dio_mem_align', 'type': '__u32'}, {'name': 'stx_dio_offset_align', 'type': '__u32'}, {'name': 'stx_subvol', 'type': '__u64'}, {'name': 'stx_atomic_write_unit_min', 'type': '__u32'}, {'name': 'stx_atomic_write_unit_max', 'type': '__u32'}, {'name': 'stx_atomic_write_segments_max', 'type': '__u32'}, {'name': 'stx_dio_read_offset_align', 'type': '__u32'}, {'name': '__spare3', 'type': '[__u64; 9usize]'}]`

### Rust Evidence

- Graph edges: `34`

## W-000645 SignatureDrift

- Risk: High
- Score: 12.4
- Symbol: writeb
- Explanation: writeb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `9`

## W-000690 FieldDrift

- Risk: High
- Score: 12.4
- Symbol: taskstats
- Explanation: taskstats changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'version', 'type': '__u16'}, {'name': 'ac_exitcode', 'type': '__u32'}, {'name': 'ac_flag', 'type': '__u8'}, {'name': 'ac_nice', 'type': '__u8'}, {'name': 'cpu_count', 'type': '__u64'}, {'name': 'cpu_delay_total', 'type': '__u64'}, {'name': 'blkio_count', 'type': '__u64'}, {'name': 'blkio_delay_total', 'type': '__u64'}, {'name': 'swapin_count', 'type': '__u64'}, {'name': 'swapin_delay_total', 'type': '__u64'}, {'name': 'cpu_run_real_total', 'type': '__u64'}, {'name': 'cpu_run_virtual_total', 'type': '__u64'}, {'name': 'ac_comm', 'type': '[ffi::c_char; 32usize]'}, {'name': 'ac_sched', 'type': '__u8'}, {'name': 'ac_pad', 'type': '[__u8; 3usize]'}, {'name': '__bindgen_padding_0', 'type': 'u32'}, {'name': 'ac_uid', 'type': '__u32'}, {'name': 'ac_gid', 'type': '__u32'}, {'name': 'ac_pid', 'type': '__u32'}, {'name': 'ac_ppid', 'type': '__u32'}, {'name': 'ac_btime', 'type': '__u32'}, {'name': 'ac_etime', 'type': '__u64'}, {'name': 'ac_utime', 'type': '__u64'}, {'name': 'ac_stime', 'type': '__u64'}, {'name': 'ac_minflt', 'type': '__u64'}, {'name': 'ac_majflt', 'type': '__u64'}, {'name': 'coremem', 'type': '__u64'}, {'name': 'virtmem', 'type': '__u64'}, {'name': 'hiwater_rss', 'type': '__u64'}, {'name': 'hiwater_vm', 'type': '__u64'}, {'name': 'read_char', 'type': '__u64'}, {'name': 'write_char', 'type': '__u64'}, {'name': 'read_syscalls', 'type': '__u64'}, {'name': 'write_syscalls', 'type': '__u64'}, {'name': 'read_bytes', 'type': '__u64'}, {'name': 'write_bytes', 'type': '__u64'}, {'name': 'cancelled_write_bytes', 'type': '__u64'}, {'name': 'nvcsw', 'type': '__u64'}, {'name': 'nivcsw', 'type': '__u64'}, {'name': 'ac_utimescaled', 'type': '__u64'}, {'name': 'ac_stimescaled', 'type': '__u64'}, {'name': 'cpu_scaled_run_real_total', 'type': '__u64'}, {'name': 'freepages_count', 'type': '__u64'}, {'name': 'freepages_delay_total', 'type': '__u64'}, {'name': 'thrashing_count', 'type': '__u64'}, {'name': 'thrashing_delay_total', 'type': '__u64'}, {'name': 'ac_btime64', 'type': '__u64'}, {'name': 'compact_count', 'type': '__u64'}, {'name': 'compact_delay_total', 'type': '__u64'}, {'name': 'ac_tgid', 'type': '__u32'}, {'name': 'ac_tgetime', 'type': '__u64'}, {'name': 'ac_exe_dev', 'type': '__u64'}, {'name': 'ac_exe_inode', 'type': '__u64'}, {'name': 'wpcopy_count', 'type': '__u64'}, {'name': 'wpcopy_delay_total', 'type': '__u64'}, {'name': 'irq_count', 'type': '__u64'}, {'name': 'irq_delay_total', 'type': '__u64'}]`
- New: `[{'name': 'version', 'type': '__u16'}, {'name': 'ac_exitcode', 'type': '__u32'}, {'name': 'ac_flag', 'type': '__u8'}, {'name': 'ac_nice', 'type': '__u8'}, {'name': 'cpu_count', 'type': '__u64'}, {'name': 'cpu_delay_total', 'type': '__u64'}, {'name': 'cpu_delay_max', 'type': '__u64'}, {'name': 'cpu_delay_min', 'type': '__u64'}, {'name': 'blkio_count', 'type': '__u64'}, {'name': 'blkio_delay_total', 'type': '__u64'}, {'name': 'blkio_delay_max', 'type': '__u64'}, {'name': 'blkio_delay_min', 'type': '__u64'}, {'name': 'swapin_count', 'type': '__u64'}, {'name': 'swapin_delay_total', 'type': '__u64'}, {'name': 'swapin_delay_max', 'type': '__u64'}, {'name': 'swapin_delay_min', 'type': '__u64'}, {'name': 'cpu_run_real_total', 'type': '__u64'}, {'name': 'cpu_run_virtual_total', 'type': '__u64'}, {'name': 'ac_comm', 'type': '[ffi::c_char; 32usize]'}, {'name': 'ac_sched', 'type': '__u8'}, {'name': 'ac_pad', 'type': '[__u8; 3usize]'}, {'name': '__bindgen_padding_0', 'type': 'u32'}, {'name': 'ac_uid', 'type': '__u32'}, {'name': 'ac_gid', 'type': '__u32'}, {'name': 'ac_pid', 'type': '__u32'}, {'name': 'ac_ppid', 'type': '__u32'}, {'name': 'ac_btime', 'type': '__u32'}, {'name': 'ac_etime', 'type': '__u64'}, {'name': 'ac_utime', 'type': '__u64'}, {'name': 'ac_stime', 'type': '__u64'}, {'name': 'ac_minflt', 'type': '__u64'}, {'name': 'ac_majflt', 'type': '__u64'}, {'name': 'coremem', 'type': '__u64'}, {'name': 'virtmem', 'type': '__u64'}, {'name': 'hiwater_rss', 'type': '__u64'}, {'name': 'hiwater_vm', 'type': '__u64'}, {'name': 'read_char', 'type': '__u64'}, {'name': 'write_char', 'type': '__u64'}, {'name': 'read_syscalls', 'type': '__u64'}, {'name': 'write_syscalls', 'type': '__u64'}, {'name': 'read_bytes', 'type': '__u64'}, {'name': 'write_bytes', 'type': '__u64'}, {'name': 'cancelled_write_bytes', 'type': '__u64'}, {'name': 'nvcsw', 'type': '__u64'}, {'name': 'nivcsw', 'type': '__u64'}, {'name': 'ac_utimescaled', 'type': '__u64'}, {'name': 'ac_stimescaled', 'type': '__u64'}, {'name': 'cpu_scaled_run_real_total', 'type': '__u64'}, {'name': 'freepages_count', 'type': '__u64'}, {'name': 'freepages_delay_total', 'type': '__u64'}, {'name': 'freepages_delay_max', 'type': '__u64'}, {'name': 'freepages_delay_min', 'type': '__u64'}, {'name': 'thrashing_count', 'type': '__u64'}, {'name': 'thrashing_delay_total', 'type': '__u64'}, {'name': 'thrashing_delay_max', 'type': '__u64'}, {'name': 'thrashing_delay_min', 'type': '__u64'}, {'name': 'ac_btime64', 'type': '__u64'}, {'name': 'compact_count', 'type': '__u64'}, {'name': 'compact_delay_total', 'type': '__u64'}, {'name': 'compact_delay_max', 'type': '__u64'}, {'name': 'compact_delay_min', 'type': '__u64'}, {'name': 'ac_tgid', 'type': '__u32'}, {'name': 'ac_tgetime', 'type': '__u64'}, {'name': 'ac_exe_dev', 'type': '__u64'}, {'name': 'ac_exe_inode', 'type': '__u64'}, {'name': 'wpcopy_count', 'type': '__u64'}, {'name': 'wpcopy_delay_total', 'type': '__u64'}, {'name': 'wpcopy_delay_max', 'type': '__u64'}, {'name': 'wpcopy_delay_min', 'type': '__u64'}, {'name': 'irq_count', 'type': '__u64'}, {'name': 'irq_delay_total', 'type': '__u64'}, {'name': 'irq_delay_max', 'type': '__u64'}, {'name': 'irq_delay_min', 'type': '__u64'}]`

### Rust Evidence

- Graph edges: `19`

## W-000068 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: devm_add_action
- Explanation: devm_add_action changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000398 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: pci_release_region
- Explanation: pci_release_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000094 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: faux_device_create
- Explanation: faux_device_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000598 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: rcu_read_unlock
- Explanation: rcu_read_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000620 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: security_secid_to_secctx
- Explanation: security_secid_to_secctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'secid', 'type': 'u32_'}, {'name': 'secdata', 'type': '*mut *mut ffi::c_char'}, {'name': 'seclen', 'type': '*mut u32_'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'secid', 'type': 'u32_'}, {'name': 'cp', 'type': '*mut lsm_context'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `7`

## W-000845 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: security_secid_to_secctx
- Explanation: security_secid_to_secctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u32 secid', 'char **secdata', 'u32 *seclen'], 'return_type': 'static inline int'}`
- New: `{'params': ['u32 secid', 'struct lsm_context *cp'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `7`

## W-000005 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: __pci_register_driver
- Explanation: __pci_register_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000096 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: faux_device_destroy
- Explanation: faux_device_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000407 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: pci_request_region
- Explanation: pci_request_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000419 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: pci_resource_len
- Explanation: pci_resource_len changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000566 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: platform_driver_unregister
- Explanation: platform_driver_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000597 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: rcu_read_lock
- Explanation: rcu_read_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000059 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: device_property_present
- Explanation: device_property_present changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000308 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: pci_enable_device_mem
- Explanation: pci_enable_device_mem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000345 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: pci_get_drvdata
- Explanation: pci_get_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000534 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: pcim_iomap
- Explanation: pcim_iomap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000568 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: platform_get_drvdata
- Explanation: platform_get_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000689 FieldDrift

- Risk: High
- Score: 11.6
- Symbol: task_struct
- Explanation: task_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'ffi::c_uint'}, {'name': 'saved_state', 'type': 'ffi::c_uint'}, {'name': 'stack', 'type': '*mut ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'ptrace', 'type': 'ffi::c_uint'}, {'name': 'on_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_cpu', 'type': 'ffi::c_int'}, {'name': 'on_rq', 'type': 'ffi::c_int'}, {'name': 'prio', 'type': 'ffi::c_int'}, {'name': 'static_prio', 'type': 'ffi::c_int'}, {'name': 'normal_prio', 'type': 'ffi::c_int'}, {'name': 'rt_priority', 'type': 'ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'dl_server', 'type': '*mut sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'ffi::c_uint'}, {'name': 'policy', 'type': 'ffi::c_uint'}, {'name': 'max_allowed_capacity', 'type': 'ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut ffi::c_void'}, {'name': 'migration_disabled', 'type': 'ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'rcu_tasks_exit_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_exit_list', 'type': 'list_head'}, {'name': 'trc_reader_nesting', 'type': 'ffi::c_int'}, {'name': 'trc_ipi_to_cpu', 'type': 'ffi::c_int'}, {'name': 'trc_reader_special', 'type': 'rcu_special'}, {'name': 'trc_holdout_list', 'type': 'list_head'}, {'name': 'trc_blkd_node', 'type': 'list_head'}, {'name': 'trc_blkd_cpu', 'type': 'ffi::c_int'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'faults_disabled_mapping', 'type': '*mut address_space'}, {'name': 'exit_state', 'type': 'ffi::c_int'}, {'name': 'exit_code', 'type': 'ffi::c_int'}, {'name': 'exit_signal', 'type': 'ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'ffi::c_int'}, {'name': 'jobctl', 'type': 'ffi::c_ulong'}, {'name': 'personality', 'type': 'ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'worker_private', 'type': '*mut ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'journal_info', 'type': '*mut ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'ffi::c_uint'}, {'name': 'perf_recursion', 'type': '[u8_; 4usize]'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'ffi::c_short'}, {'name': 'il_weight', 'type': 'u8_'}, {'name': 'pref_node_fork', 'type': 'ffi::c_short'}, {'name': 'rseq', 'type': '*mut rseq'}, {'name': 'rseq_len', 'type': 'u32_'}, {'name': 'rseq_sig', 'type': 'u32_'}, {'name': 'rseq_event_mask', 'type': 'ffi::c_ulong'}, {'name': 'mm_cid', 'type': 'ffi::c_int'}, {'name': 'last_mm_cid', 'type': 'ffi::c_int'}, {'name': 'migrate_from_cpu', 'type': 'ffi::c_int'}, {'name': 'mm_cid_active', 'type': 'ffi::c_int'}, {'name': 'cid_work', 'type': 'callback_head'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'bpf_net_context', 'type': '*mut bpf_net_context'}, {'name': 'mce_vaddr', 'type': '*mut ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': '__bindgen_padding_1', 'type': '[u64; 7usize]'}, {'name': 'thread', 'type': 'thread_struct'}]`
- New: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'ffi::c_uint'}, {'name': 'saved_state', 'type': 'ffi::c_uint'}, {'name': 'stack', 'type': '*mut ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'ptrace', 'type': 'ffi::c_uint'}, {'name': 'on_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_cpu', 'type': 'ffi::c_int'}, {'name': 'on_rq', 'type': 'ffi::c_int'}, {'name': 'prio', 'type': 'ffi::c_int'}, {'name': 'static_prio', 'type': 'ffi::c_int'}, {'name': 'normal_prio', 'type': 'ffi::c_int'}, {'name': 'rt_priority', 'type': 'ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'dl_server', 'type': '*mut sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'ffi::c_uint'}, {'name': 'policy', 'type': 'ffi::c_uint'}, {'name': 'max_allowed_capacity', 'type': 'ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut ffi::c_void'}, {'name': 'migration_disabled', 'type': 'ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'rcu_tasks_exit_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_exit_list', 'type': 'list_head'}, {'name': 'trc_reader_nesting', 'type': 'ffi::c_int'}, {'name': 'trc_ipi_to_cpu', 'type': 'ffi::c_int'}, {'name': 'trc_reader_special', 'type': 'rcu_special'}, {'name': 'trc_holdout_list', 'type': 'list_head'}, {'name': 'trc_blkd_node', 'type': 'list_head'}, {'name': 'trc_blkd_cpu', 'type': 'ffi::c_int'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'faults_disabled_mapping', 'type': '*mut address_space'}, {'name': 'exit_state', 'type': 'ffi::c_int'}, {'name': 'exit_code', 'type': 'ffi::c_int'}, {'name': 'exit_signal', 'type': 'ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'ffi::c_int'}, {'name': 'jobctl', 'type': 'ffi::c_ulong'}, {'name': 'personality', 'type': 'ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'worker_private', 'type': '*mut ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'journal_info', 'type': '*mut ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'ffi::c_uint'}, {'name': 'perf_recursion', 'type': '[u8_; 4usize]'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'ffi::c_short'}, {'name': 'il_weight', 'type': 'u8_'}, {'name': 'pref_node_fork', 'type': 'ffi::c_short'}, {'name': 'rseq', 'type': '*mut rseq'}, {'name': 'rseq_len', 'type': 'u32_'}, {'name': 'rseq_sig', 'type': 'u32_'}, {'name': 'rseq_event_mask', 'type': 'ffi::c_ulong'}, {'name': 'mm_cid', 'type': 'ffi::c_int'}, {'name': 'last_mm_cid', 'type': 'ffi::c_int'}, {'name': 'migrate_from_cpu', 'type': 'ffi::c_int'}, {'name': 'mm_cid_active', 'type': 'ffi::c_int'}, {'name': 'cid_work', 'type': 'callback_head'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'bpf_net_context', 'type': '*mut bpf_net_context'}, {'name': 'mce_vaddr', 'type': '*mut ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': '__bindgen_padding_1', 'type': '[u64; 5usize]'}, {'name': 'thread', 'type': 'thread_struct'}]`

### Rust Evidence

- Graph edges: `15`

## W-000011 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: __platform_driver_register
- Explanation: __platform_driver_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000078 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: devm_remove_action_nowarn
- Explanation: devm_remove_action_nowarn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000187 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: msi_domain
- Explanation: msi_domain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000192 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: mutex_assert_is_held
- Explanation: mutex_assert_is_held changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000436 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: pci_set_master
- Explanation: pci_set_master changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000569 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: platform_get_irq
- Explanation: platform_get_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000619 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: security_release_secctx
- Explanation: security_release_secctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'secdata', 'type': '*mut ffi::c_char'}, {'name': 'seclen', 'type': 'u32_'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'cp', 'type': '*mut lsm_context'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `4`

## W-000635 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: spin_assert_is_held
- Explanation: spin_assert_is_held changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000844 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: security_release_secctx
- Explanation: security_release_secctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['char *secdata', 'u32 seclen'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct lsm_context *cp'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `4`

## W-000021 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: blk_mq_freeze_queue
- Explanation: blk_mq_freeze_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `3`

## W-000048 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: device_for_each_child
- Explanation: device_for_each_child changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'dev', 'type': '*mut device'}, {'name': 'data', 'type': '*mut ffi::c_void'}, {'name': 'fn_', 'type': '::core::option::Option< unsafe extern "C" fn(dev: *mut device, data: *mut ffi::c_void'}], 'return_type': 'ffi::c_int, >, ) -> ffi::c_int'}`
- New: `{'params': [{'name': 'parent', 'type': '*mut device'}, {'name': 'data', 'type': '*mut ffi::c_void'}, {'name': 'fn_', 'type': 'device_iter_t'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `3`

## W-000073 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: devm_platform_get_and_ioremap_resource
- Explanation: devm_platform_get_and_ioremap_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000076 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: devm_platform_ioremap_resource_byname
- Explanation: devm_platform_ioremap_resource_byname changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000104 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: fwnode_get_name
- Explanation: fwnode_get_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000170 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: lockref_get
- Explanation: lockref_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut lockref'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'lockref', 'type': '*mut lockref'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `3`

## W-000288 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: pci_dev_get
- Explanation: pci_dev_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000307 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: pci_enable_device
- Explanation: pci_enable_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000360 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: pci_irq_vector
- Explanation: pci_irq_vector changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000434 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: pci_set_drvdata
- Explanation: pci_set_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000539 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: pcim_iounmap
- Explanation: pcim_iounmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000557 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: platform_device_add
- Explanation: platform_device_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000602 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: readl
- Explanation: readl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000828 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: blk_mq_freeze_queue
- Explanation: blk_mq_freeze_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct request_queue *q'], 'return_type': 'void'}`
- New: `{'params': ['struct request_queue *q'], 'return_type': 'static inline unsigned int __must_check'}`

### Rust Evidence

- Graph edges: `3`

## W-000849 ErrorDrift

- Risk: High
- Score: 11.2
- Symbol: devm_platform_ioremap_resource
- Explanation: devm_platform_ioremap_resource has ERROR_CODE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE', 'ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/include/linux/platform_device.h:91 `return ERR_PTR(-EINVAL);`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:283 `From<core::convert::Infallible>::to_result` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:278 `///     pdev: &mut PlatformDevice,`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:279 `///     index: u32,`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.14/rust/kernel/error.rs:280 `/// ) -> Result<*mut kernel::ffi::c_void> {`

## W-000001 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __dev_fwnode
- Explanation: __dev_fwnode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000024 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: blk_mq_unfreeze_queue
- Explanation: blk_mq_unfreeze_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `2`

## W-000049 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: device_for_each_child_reverse
- Explanation: device_for_each_child_reverse changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'dev', 'type': '*mut device'}, {'name': 'data', 'type': '*mut ffi::c_void'}, {'name': 'fn_', 'type': '::core::option::Option< unsafe extern "C" fn(dev: *mut device, data: *mut ffi::c_void'}], 'return_type': 'ffi::c_int, >, ) -> ffi::c_int'}`
- New: `{'params': [{'name': 'parent', 'type': '*mut device'}, {'name': 'data', 'type': '*mut ffi::c_void'}, {'name': 'fn_', 'type': 'device_iter_t'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `2`

## W-000061 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: device_property_read_string
- Explanation: device_property_read_string changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000077 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: devm_remove_action
- Explanation: devm_remove_action changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `2`

## W-000098 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: fwnode_connection_find_match
- Explanation: fwnode_connection_find_match changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000118 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: fwnode_graph_get_remote_port
- Explanation: fwnode_graph_get_remote_port changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000123 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: fwnode_irq_get
- Explanation: fwnode_irq_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000131 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: fwnode_property_read_string
- Explanation: fwnode_property_read_string changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000144 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: io_window
- Explanation: io_window changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000163 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: kthread_create_worker
- Explanation: kthread_create_worker changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `2`

## W-000179 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: memtype_free
- Explanation: memtype_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000182 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: memtype_reserve
- Explanation: memtype_reserve changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000229 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_add_resource
- Explanation: pci_add_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000234 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_alloc_irq_vectors
- Explanation: pci_alloc_irq_vectors changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000237 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_assign_resource
- Explanation: pci_assign_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000245 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_bus_add_device
- Explanation: pci_bus_add_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000258 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_bus_remove_resource
- Explanation: pci_bus_remove_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000271 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_cfg_space_size
- Explanation: pci_cfg_space_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000300 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_disable_link_state
- Explanation: pci_disable_link_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000302 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_disable_msi
- Explanation: pci_disable_msi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000309 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_enable_link_state
- Explanation: pci_enable_link_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000311 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_enable_msi
- Explanation: pci_enable_msi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000323 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_find_next_bus
- Explanation: pci_find_next_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000328 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_find_resource
- Explanation: pci_find_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000334 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_free_irq
- Explanation: pci_free_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000337 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_generic_config_read
- Explanation: pci_generic_config_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000339 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_generic_config_write
- Explanation: pci_generic_config_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000341 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_get_base_class
- Explanation: pci_get_base_class changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000342 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_get_class
- Explanation: pci_get_class changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000343 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_get_device
- Explanation: pci_get_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000344 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_get_domain_bus_and_slot
- Explanation: pci_get_domain_bus_and_slot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000348 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_get_slot
- Explanation: pci_get_slot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000349 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_get_subsys
- Explanation: pci_get_subsys changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000350 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_host_bridge_acpi_msi_domain
- Explanation: pci_host_bridge_acpi_msi_domain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000366 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_match_id
- Explanation: pci_match_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000389 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_read_vpd
- Explanation: pci_read_vpd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000396 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_register_io_range
- Explanation: pci_register_io_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000408 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_request_regions
- Explanation: pci_request_regions changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000410 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_request_selected_regions
- Explanation: pci_request_selected_regions changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000412 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_rescan_bus
- Explanation: pci_rescan_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000415 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_reset_function
- Explanation: pci_reset_function changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000428 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_scan_root_bus
- Explanation: pci_scan_root_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000439 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_set_power_state
- Explanation: pci_set_power_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000446 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_stop_and_remove_bus_device
- Explanation: pci_stop_and_remove_bus_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000469 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_wait_for_pending
- Explanation: pci_wait_for_pending changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000476 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_write_vpd
- Explanation: pci_write_vpd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000504 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pcibios_setup
- Explanation: pcibios_setup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000536 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pcim_iomap_region
- Explanation: pcim_iomap_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000540 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pcim_iounmap_region
- Explanation: pcim_iounmap_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000563 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: platform_device_register
- Explanation: platform_device_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000570 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: platform_get_irq_byname
- Explanation: platform_get_irq_byname changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000574 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: platform_get_resource
- Explanation: platform_get_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000600 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: readb
- Explanation: readb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000605 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: readq
- Explanation: readq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000607 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: readw
- Explanation: readw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000631 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: software_node_register
- Explanation: software_node_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000633 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: software_node_unregister
- Explanation: software_node_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000647 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: writel
- Explanation: writel changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000649 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: writeq
- Explanation: writeq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000651 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: writew
- Explanation: writew changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000681 FieldDrift

- Risk: High
- Score: 11.0
- Symbol: queue_limits
- Explanation: queue_limits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`
- New: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'min_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`

### Rust Evidence

- Graph edges: `12`

## W-000829 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: blk_mq_unfreeze_queue
- Explanation: blk_mq_unfreeze_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct request_queue *q'], 'return_type': 'void'}`
- New: `{'params': ['struct request_queue *q', 'unsigned int memflags'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `2`

## W-000002 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __dev_fwnode_const
- Explanation: __dev_fwnode_const changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000003 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kunit_test_suites_init
- Explanation: __kunit_test_suites_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'suites', 'type': '*const *mut kunit_suite'}, {'name': 'num_suites', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'suites', 'type': '*const *mut kunit_suite'}, {'name': 'num_suites', 'type': 'ffi::c_int'}, {'name': 'run_tests', 'type': 'bool_'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000004 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __modver_version_show
- Explanation: __modver_version_show changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut module_attribute'}, {'name': 'arg2', 'type': '*mut module_kobject'}, {'name': 'arg3', 'type': '*mut ffi::c_char'}], 'return_type': 'isize'}`
- New: `{'params': [{'name': 'arg1', 'type': '*const module_attribute'}, {'name': 'arg2', 'type': '*mut module_kobject'}, {'name': 'arg3', 'type': '*mut ffi::c_char'}], 'return_type': 'isize'}`

### Rust Evidence

- Graph edges: `1`

## W-000006 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __pci_reset_function_locked
- Explanation: __pci_reset_function_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000007 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __phy_ethtool_get_link_ext_stats
- Explanation: __phy_ethtool_get_link_ext_stats changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000008 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __phy_ethtool_get_phy_stats
- Explanation: __phy_ethtool_get_phy_stats changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000009 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __platform_create_bundle
- Explanation: __platform_create_bundle changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000010 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __platform_driver_probe
- Explanation: __platform_driver_probe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000012 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __platform_register_drivers
- Explanation: __platform_register_drivers changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000014 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_pages_bulk_mempolicy_noprof
- Explanation: alloc_pages_bulk_mempolicy_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000015 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_pages_bulk_noprof
- Explanation: alloc_pages_bulk_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'gfp', 'type': 'gfp_t'}, {'name': 'preferred_nid', 'type': 'ffi::c_int'}, {'name': 'nodemask', 'type': '*mut nodemask_t'}, {'name': 'nr_pages', 'type': 'ffi::c_int'}, {'name': 'page_list', 'type': '*mut list_head'}, {'name': 'page_array', 'type': '*mut *mut page'}], 'return_type': 'ffi::c_ulong'}`
- New: `{'params': [{'name': 'gfp', 'type': 'gfp_t'}, {'name': 'preferred_nid', 'type': 'ffi::c_int'}, {'name': 'nodemask', 'type': '*mut nodemask_t'}, {'name': 'nr_pages', 'type': 'ffi::c_int'}, {'name': 'page_array', 'type': '*mut *mut page'}], 'return_type': 'ffi::c_ulong'}`

### Rust Evidence

- Graph edges: `1`

## W-000017 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_pci_dev_is_removable
- Explanation: arch_pci_dev_is_removable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000018 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ari_enabled
- Explanation: ari_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000019 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ats_enabled
- Explanation: ats_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000022 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_freeze_queue_nomemsave
- Explanation: blk_mq_freeze_queue_nomemsave changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000023 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_map_hw_queues
- Explanation: blk_mq_map_hw_queues changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000025 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_unfreeze_queue_nomemrestore
- Explanation: blk_mq_unfreeze_queue_nomemrestore changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000026 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: block_cfg_access
- Explanation: block_cfg_access changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000027 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bridge_d3
- Explanation: bridge_d3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000028 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: broken_intx_masking
- Explanation: broken_intx_masking changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000029 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: broken_parity_status
- Explanation: broken_parity_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000030 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bus_for_each_dev
- Explanation: bus_for_each_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'bus', 'type': '*const bus_type'}, {'name': 'start', 'type': '*mut device'}, {'name': 'data', 'type': '*mut ffi::c_void'}, {'name': 'fn_', 'type': '::core::option::Option< unsafe extern "C" fn(dev: *mut device, data: *mut ffi::c_void'}], 'return_type': 'ffi::c_int, >, ) -> ffi::c_int'}`
- New: `{'params': [{'name': 'bus', 'type': '*const bus_type'}, {'name': 'start', 'type': '*mut device'}, {'name': 'data', 'type': '*mut ffi::c_void'}, {'name': 'fn_', 'type': 'device_iter_t'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000031 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_compat_create_link
- Explanation: class_compat_create_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'cls', 'type': '*mut class_compat'}, {'name': 'dev', 'type': '*mut device'}, {'name': 'device_link', 'type': '*mut device'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'cls', 'type': '*mut class_compat'}, {'name': 'dev', 'type': '*mut device'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000032 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_compat_remove_link
- Explanation: class_compat_remove_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'cls', 'type': '*mut class_compat'}, {'name': 'dev', 'type': '*mut device'}, {'name': 'device_link', 'type': '*mut device'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'cls', 'type': '*mut class_compat'}, {'name': 'dev', 'type': '*mut device'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000033 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_for_each_device
- Explanation: class_for_each_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'class', 'type': '*const class'}, {'name': 'start', 'type': '*const device'}, {'name': 'data', 'type': '*mut ffi::c_void'}, {'name': 'fn_', 'type': '::core::option::Option< unsafe extern "C" fn(dev: *mut device, data: *mut ffi::c_void'}], 'return_type': 'ffi::c_int, >, ) -> ffi::c_int'}`
- New: `{'params': [{'name': 'class', 'type': '*const class'}, {'name': 'start', 'type': '*const device'}, {'name': 'data', 'type': '*mut ffi::c_void'}, {'name': 'fn_', 'type': 'device_iter_t'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000034 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: clear_retrain_link
- Explanation: clear_retrain_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000035 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: config_rrs_sv
- Explanation: config_rrs_sv changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000036 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_from_early_mem
- Explanation: copy_from_early_mem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'dest', 'type': '*mut ffi::c_void'}, {'name': 'src', 'type': 'phys_addr_t'}, {'name': 'size', 'type': 'ffi::c_ulong'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'dest', 'type': '*mut ffi::c_void'}, {'name': 'src', 'type': 'phys_addr_t'}, {'name': 'size', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000037 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_show_ghostwrite
- Explanation: cpu_show_ghostwrite changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000038 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d1_support
- Explanation: d1_support changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000039 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d2_support
- Explanation: d2_support changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000040 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d3cold_allowed
- Explanation: d3cold_allowed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000041 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dentry_open_nonotify
- Explanation: dentry_open_nonotify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000042 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_add_software_node
- Explanation: device_add_software_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000043 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_create_managed_software_node
- Explanation: device_create_managed_software_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000044 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_dma_supported
- Explanation: device_dma_supported changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000046 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_find_child
- Explanation: device_find_child changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'dev', 'type': '*mut device'}, {'name': 'data', 'type': '*mut ffi::c_void'}, {'name': 'match_', 'type': '::core::option::Option< unsafe extern "C" fn(dev: *mut device, data: *mut ffi::c_void'}], 'return_type': 'ffi::c_int, >, ) -> *mut device'}`
- New: `{'params': [{'name': 'parent', 'type': '*mut device'}, {'name': 'data', 'type': '*const ffi::c_void'}, {'name': 'match_', 'type': 'device_match_t'}], 'return_type': '*mut device'}`

### Rust Evidence

- Graph edges: `1`

## W-000050 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_for_each_child_reverse_from
- Explanation: device_for_each_child_reverse_from changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'parent', 'type': '*mut device'}, {'name': 'from', 'type': '*mut device'}, {'name': 'data', 'type': '*const ffi::c_void'}, {'name': 'fn_', 'type': '::core::option::Option< unsafe extern "C" fn(arg1: *mut device, arg2: *const ffi::c_void'}], 'return_type': 'ffi::c_int, >, ) -> ffi::c_int'}`
- New: `{'params': [{'name': 'parent', 'type': '*mut device'}, {'name': 'from', 'type': '*mut device'}, {'name': 'data', 'type': '*mut ffi::c_void'}, {'name': 'fn_', 'type': 'device_iter_t'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000051 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_get_child_node_count
- Explanation: device_get_child_node_count changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000052 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_get_dma_attr
- Explanation: device_get_dma_attr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000053 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_get_match_data
- Explanation: device_get_match_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000054 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_get_named_child_node
- Explanation: device_get_named_child_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000055 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_get_next_child_node
- Explanation: device_get_next_child_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000056 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_get_phy_mode
- Explanation: device_get_phy_mode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000057 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_match_type
- Explanation: device_match_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000058 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_property_match_string
- Explanation: device_property_match_string changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000060 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_property_read_bool
- Explanation: device_property_read_bool changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000062 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_property_read_string_array
- Explanation: device_property_read_string_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000063 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_property_read_u16_array
- Explanation: device_property_read_u16_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000064 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_property_read_u32_array
- Explanation: device_property_read_u32_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000065 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_property_read_u64_array
- Explanation: device_property_read_u64_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000066 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_property_read_u8_array
- Explanation: device_property_read_u8_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000067 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_remove_software_node
- Explanation: device_remove_software_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000069 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_pci_alloc_host_bridge
- Explanation: devm_pci_alloc_host_bridge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000070 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_pci_remap_cfg_resource
- Explanation: devm_pci_remap_cfg_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000071 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_pci_remap_cfgspace
- Explanation: devm_pci_remap_cfgspace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000072 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_pci_remap_iospace
- Explanation: devm_pci_remap_iospace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000074 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_platform_get_irqs_affinity
- Explanation: devm_platform_get_irqs_affinity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000079 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_request_pci_bus_resources
- Explanation: devm_request_pci_bus_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000080 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_pool_alloc
- Explanation: dma_pool_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000081 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_pool_create
- Explanation: dma_pool_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000082 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_pool_destroy
- Explanation: dma_pool_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000083 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_pool_free
- Explanation: dma_pool_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000084 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dmam_pool_create
- Explanation: dmam_pool_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000085 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dmam_pool_destroy
- Explanation: dmam_pool_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000086 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_mount
- Explanation: do_mount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*const ffi::c_char'}, {'name': 'arg2', 'type': '*const ffi::c_char'}, {'name': 'arg3', 'type': '*const ffi::c_char'}, {'name': 'arg4', 'type': 'ffi::c_ulong'}, {'name': 'arg5', 'type': '*mut ffi::c_void'}], 'return_type': 'ffi::c_long'}`
- New: `{'params': [{'name': 'arg1', 'type': '*const ffi::c_char'}, {'name': 'arg2', 'type': '*const ffi::c_char'}, {'name': 'arg3', 'type': '*const ffi::c_char'}, {'name': 'arg4', 'type': 'ffi::c_ulong'}, {'name': 'arg5', 'type': '*mut ffi::c_void'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000087 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: driver_for_each_device
- Explanation: driver_for_each_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'drv', 'type': '*mut device_driver'}, {'name': 'start', 'type': '*mut device'}, {'name': 'data', 'type': '*mut ffi::c_void'}, {'name': 'fn_', 'type': '::core::option::Option< unsafe extern "C" fn(dev: *mut device, arg1: *mut ffi::c_void'}], 'return_type': 'ffi::c_int, >, ) -> ffi::c_int'}`
- New: `{'params': [{'name': 'drv', 'type': '*mut device_driver'}, {'name': 'start', 'type': '*mut device'}, {'name': 'data', 'type': '*mut ffi::c_void'}, {'name': 'fn_', 'type': 'device_iter_t'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000088 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dump_vmg
- Explanation: dump_vmg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000089 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: early_platform_cleanup
- Explanation: early_platform_cleanup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000090 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: early_quirks
- Explanation: early_quirks changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000091 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: eetlp_prefix_max
- Explanation: eetlp_prefix_max changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000093 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: external_facing
- Explanation: external_facing changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000095 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: faux_device_create_with_groups
- Explanation: faux_device_create_with_groups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000097 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_fdatawrite_range_kick
- Explanation: filemap_fdatawrite_range_kick changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000099 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_connection_find_matches
- Explanation: fwnode_connection_find_matches changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000100 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_count_parents
- Explanation: fwnode_count_parents changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000101 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_create_software_node
- Explanation: fwnode_create_software_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000102 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_device_is_available
- Explanation: fwnode_device_is_available changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000103 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_find_reference
- Explanation: fwnode_find_reference changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000105 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_get_name_prefix
- Explanation: fwnode_get_name_prefix changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000106 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_get_named_child_node
- Explanation: fwnode_get_named_child_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000107 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_get_next_available_child_node
- Explanation: fwnode_get_next_available_child_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000108 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_get_next_child_node
- Explanation: fwnode_get_next_child_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000109 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_get_next_parent
- Explanation: fwnode_get_next_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000110 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_get_nth_parent
- Explanation: fwnode_get_nth_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000111 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_get_parent
- Explanation: fwnode_get_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000112 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_get_phy_mode
- Explanation: fwnode_get_phy_mode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000113 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_graph_get_endpoint_by_id
- Explanation: fwnode_graph_get_endpoint_by_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000114 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_graph_get_endpoint_count
- Explanation: fwnode_graph_get_endpoint_count changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000115 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_graph_get_next_endpoint
- Explanation: fwnode_graph_get_next_endpoint changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000116 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_graph_get_port_parent
- Explanation: fwnode_graph_get_port_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000117 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_graph_get_remote_endpoint
- Explanation: fwnode_graph_get_remote_endpoint changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000119 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_graph_get_remote_port_parent
- Explanation: fwnode_graph_get_remote_port_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000120 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_graph_parse_endpoint
- Explanation: fwnode_graph_parse_endpoint changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000121 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_handle_get
- Explanation: fwnode_handle_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000122 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_iomap
- Explanation: fwnode_iomap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000124 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_irq_get_byname
- Explanation: fwnode_irq_get_byname changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000125 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_name_eq
- Explanation: fwnode_name_eq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000126 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_property_get_reference_args
- Explanation: fwnode_property_get_reference_args changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000127 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_property_match_property_string
- Explanation: fwnode_property_match_property_string changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000128 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_property_match_string
- Explanation: fwnode_property_match_string changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000129 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_property_present
- Explanation: fwnode_property_present changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000130 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_property_read_bool
- Explanation: fwnode_property_read_bool changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000132 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_property_read_string_array
- Explanation: fwnode_property_read_string_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000133 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_property_read_u16_array
- Explanation: fwnode_property_read_u16_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000134 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_property_read_u32_array
- Explanation: fwnode_property_read_u32_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000135 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_property_read_u64_array
- Explanation: fwnode_property_read_u64_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000136 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_property_read_u8_array
- Explanation: fwnode_property_read_u8_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000137 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_remove_software_node
- Explanation: fwnode_remove_software_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000138 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_eee_is_active
- Explanation: genphy_c45_eee_is_active changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'adv', 'type': '*mut ffi::c_ulong'}, {'name': 'lp', 'type': '*mut ffi::c_ulong'}, {'name': 'is_enabled', 'type': '*mut bool_'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'adv', 'type': '*mut ffi::c_ulong'}, {'name': 'lp', 'type': '*mut ffi::c_ulong'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000139 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hotplug_user_indicators
- Explanation: hotplug_user_indicators changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000140 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ignore_hotplug
- Explanation: ignore_hotplug changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000141 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ignore_reset_delay
- Explanation: ignore_reset_delay changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000142 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: imm_ready
- Explanation: imm_ready changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000145 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: io_window_1k
- Explanation: io_window_1k changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000147 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_managed
- Explanation: irq_managed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000148 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_reroute_variant
- Explanation: irq_reroute_variant changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000149 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_added
- Explanation: is_added changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000150 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_busmaster
- Explanation: is_busmaster changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000151 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_hotplug_bridge
- Explanation: is_hotplug_bridge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000152 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_managed
- Explanation: is_managed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(0usize, 1u8) as u32) } } #[inline] pub fn set_is_managed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(19usize, 1u8) as u32) } } #[inline] pub fn set_is_managed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000153 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_msi_managed
- Explanation: is_msi_managed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000154 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_physfn
- Explanation: is_physfn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000155 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_probed
- Explanation: is_probed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000156 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_software_node
- Explanation: is_software_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000157 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_thunderbolt
- Explanation: is_thunderbolt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000158 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_virtfn
- Explanation: is_virtfn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000162 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_affine_preferred
- Explanation: kthread_affine_preferred changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000164 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_create_worker_on_cpu
- Explanation: kthread_create_worker_on_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'cpu', 'type': 'ffi::c_int'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'namefmt', 'type': '*const ffi::c_char'}, {'name': '', 'type': '...'}], 'return_type': '*mut kthread_worker'}`
- New: `{'params': [{'name': 'cpu', 'type': 'ffi::c_int'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'namefmt', 'type': '*const ffi::c_char'}], 'return_type': '*mut kthread_worker'}`

### Rust Evidence

- Graph edges: `1`

## W-000165 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_create_worker_on_node
- Explanation: kthread_create_worker_on_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000167 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_autorun
- Explanation: kunit_autorun changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000168 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kvfree_rcu_init
- Explanation: kvfree_rcu_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000169 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: link_active_reporting
- Explanation: link_active_reporting changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000171 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lockref_get_not_dead
- Explanation: lockref_get_not_dead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut lockref'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'lockref', 'type': '*mut lockref'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000172 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lockref_get_not_zero
- Explanation: lockref_get_not_zero changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut lockref'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'lockref', 'type': '*mut lockref'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000173 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lockref_mark_dead
- Explanation: lockref_mark_dead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut lockref'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'lockref', 'type': '*mut lockref'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000175 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lockref_put_or_lock
- Explanation: lockref_put_or_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut lockref'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'lockref', 'type': '*mut lockref'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000176 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lockref_put_return
- Explanation: lockref_put_return changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut lockref'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'lockref', 'type': '*mut lockref'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000177 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ltr_path
- Explanation: ltr_path changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000178 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: may_skip_resume
- Explanation: may_skip_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_2.get(5usize, 1u8) as u8) } } #[inline] pub fn set_may_skip_resume(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_2.get(6usize, 1u8) as u8) } } #[inline] pub fn set_may_skip_resume(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000180 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: memtype_free_io
- Explanation: memtype_free_io changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000181 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: memtype_kernel_map_sync
- Explanation: memtype_kernel_map_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000183 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: memtype_reserve_io
- Explanation: memtype_reserve_io changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000184 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmap_read_lock_maybe_expand
- Explanation: mmap_read_lock_maybe_expand changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000186 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmio_always_on
- Explanation: mmio_always_on changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000188 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: msi_domain_get_virq
- Explanation: msi_domain_get_virq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000189 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: msi_enabled
- Explanation: msi_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000190 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: msix_enabled
- Explanation: msix_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000191 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: multifunction
- Explanation: multifunction changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000193 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: native_aer
- Explanation: native_aer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000194 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: native_cxl_error
- Explanation: native_cxl_error changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000195 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: native_dpc
- Explanation: native_dpc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000196 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: native_ltr
- Explanation: native_ltr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000197 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: native_pcie_hotplug
- Explanation: native_pcie_hotplug changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000198 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: native_pme
- Explanation: native_pme changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000199 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: native_shpc_hotplug
- Explanation: native_shpc_hotplug changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000200 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: needs_freset
- Explanation: needs_freset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000201 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_bitfield_2
- Explanation: new_bitfield_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'tstamp_type', 'type': '__u8'}, {'name': 'tc_at_ingress', 'type': '__u8'}, {'name': 'tc_skip_classify', 'type': '__u8'}, {'name': 'remcsum_offload', 'type': '__u8'}, {'name': 'csum_complete_sw', 'type': '__u8'}, {'name': 'csum_level', 'type': '__u8'}, {'name': 'inner_protocol_type', 'type': '__u8'}, {'name': 'l4_hash', 'type': '__u8'}, {'name': 'sw_hash', 'type': '__u8'}, {'name': 'wifi_acked_valid', 'type': '__u8'}, {'name': 'wifi_acked', 'type': '__u8'}, {'name': 'no_fcs', 'type': '__u8'}, {'name': 'encapsulation', 'type': '__u8'}, {'name': 'encap_hdr_csum', 'type': '__u8'}, {'name': 'csum_valid', 'type': '__u8'}, {'name': 'ndisc_nodetype', 'type': '__u8'}, {'name': 'redirected', 'type': '__u8'}, {'name': 'nf_skip_egress', 'type': '__u8'}, {'name': 'slow_gro', 'type': '__u8'}, {'name': 'unreadable', 'type': '__u8'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`
- New: `{'params': [{'name': 'pme_support', 'type': 'ffi::c_uint'}, {'name': 'pme_poll', 'type': 'ffi::c_uint'}, {'name': 'pinned', 'type': 'ffi::c_uint'}, {'name': 'config_rrs_sv', 'type': 'ffi::c_uint'}, {'name': 'imm_ready', 'type': 'ffi::c_uint'}, {'name': 'd1_support', 'type': 'ffi::c_uint'}, {'name': 'd2_support', 'type': 'ffi::c_uint'}, {'name': 'no_d1d2', 'type': 'ffi::c_uint'}, {'name': 'no_d3cold', 'type': 'ffi::c_uint'}, {'name': 'bridge_d3', 'type': 'ffi::c_uint'}, {'name': 'd3cold_allowed', 'type': 'ffi::c_uint'}, {'name': 'mmio_always_on', 'type': 'ffi::c_uint'}, {'name': 'wakeup_prepared', 'type': 'ffi::c_uint'}, {'name': 'skip_bus_pm', 'type': 'ffi::c_uint'}, {'name': 'ignore_hotplug', 'type': 'ffi::c_uint'}, {'name': 'hotplug_user_indicators', 'type': 'ffi::c_uint'}, {'name': 'clear_retrain_link', 'type': 'ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`

### Rust Evidence

- Graph edges: `1`

## W-000202 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_bitfield_3
- Explanation: new_bitfield_3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'disable_depth', 'type': 'ffi::c_uint'}, {'name': 'idle_notification', 'type': 'bool_'}, {'name': 'request_pending', 'type': 'bool_'}, {'name': 'deferred_resume', 'type': 'bool_'}, {'name': 'needs_force_resume', 'type': 'bool_'}, {'name': 'runtime_auto', 'type': 'bool_'}, {'name': 'ignore_children', 'type': 'bool_'}, {'name': 'no_callbacks', 'type': 'bool_'}, {'name': 'irq_safe', 'type': 'bool_'}, {'name': 'use_autosuspend', 'type': 'bool_'}, {'name': 'timer_autosuspends', 'type': 'bool_'}, {'name': 'memalloc_noio', 'type': 'bool_'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`
- New: `{'params': [{'name': 'ltr_path', 'type': 'ffi::c_uint'}, {'name': 'pasid_no_tlp', 'type': 'ffi::c_uint'}, {'name': 'eetlp_prefix_max', 'type': 'ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`

### Rust Evidence

- Graph edges: `1`

## W-000203 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_bitfield_4
- Explanation: new_bitfield_4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000204 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_bitfield_5
- Explanation: new_bitfield_5 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000205 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_64bit_msi
- Explanation: no_64bit_msi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000206 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_command_memory
- Explanation: no_command_memory changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000207 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_d1d2
- Explanation: no_d1d2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000208 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_d3cold
- Explanation: no_d3cold changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000209 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_ext_tags
- Explanation: no_ext_tags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000210 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_inc_mrrs
- Explanation: no_inc_mrrs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000211 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_msi
- Explanation: no_msi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000212 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_pci_devices
- Explanation: no_pci_devices changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000213 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_vf_scan
- Explanation: no_vf_scan changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000214 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: non_compliant_bars
- Explanation: non_compliant_bars changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000216 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: page_get_link_raw
- Explanation: page_get_link_raw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000217 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pasid_enabled
- Explanation: pasid_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000218 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pasid_no_tlp
- Explanation: pasid_no_tlp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000219 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pasid_required
- Explanation: pasid_required changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000220 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pat_bp_init
- Explanation: pat_bp_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000221 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pat_cpu_init
- Explanation: pat_cpu_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000222 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pat_enabled
- Explanation: pat_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000223 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pat_pfn_immune_to_uc_mtrr
- Explanation: pat_pfn_immune_to_uc_mtrr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000224 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_acs_enabled
- Explanation: pci_acs_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000225 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_acs_path_enabled
- Explanation: pci_acs_path_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000226 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_add_dma_alias
- Explanation: pci_add_dma_alias changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000227 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_add_dynid
- Explanation: pci_add_dynid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000228 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_add_new_bus
- Explanation: pci_add_new_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000230 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_add_resource_offset
- Explanation: pci_add_resource_offset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000231 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_address_to_pio
- Explanation: pci_address_to_pio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000232 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_alloc_dev
- Explanation: pci_alloc_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000233 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_alloc_host_bridge
- Explanation: pci_alloc_host_bridge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000235 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_alloc_irq_vectors_affinity
- Explanation: pci_alloc_irq_vectors_affinity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000236 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_assign_irq
- Explanation: pci_assign_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000238 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_assign_unassigned_bridge_resources
- Explanation: pci_assign_unassigned_bridge_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000239 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_assign_unassigned_bus_resources
- Explanation: pci_assign_unassigned_bus_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000240 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_assign_unassigned_resources
- Explanation: pci_assign_unassigned_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000241 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_assign_unassigned_root_bus_resources
- Explanation: pci_assign_unassigned_root_bus_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000242 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_ats_disabled
- Explanation: pci_ats_disabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000243 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_back_from_sleep
- Explanation: pci_back_from_sleep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000244 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bridge_secondary_bus_reset
- Explanation: pci_bridge_secondary_bus_reset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000246 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bus_add_devices
- Explanation: pci_bus_add_devices changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000247 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bus_add_resource
- Explanation: pci_bus_add_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000248 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bus_alloc_resource
- Explanation: pci_bus_alloc_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000249 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bus_assign_resources
- Explanation: pci_bus_assign_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000250 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bus_claim_resources
- Explanation: pci_bus_claim_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000251 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bus_find_capability
- Explanation: pci_bus_find_capability changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000252 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bus_insert_busn_res
- Explanation: pci_bus_insert_busn_res changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000253 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bus_max_busnr
- Explanation: pci_bus_max_busnr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000254 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bus_read_config_byte
- Explanation: pci_bus_read_config_byte changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000255 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bus_read_config_dword
- Explanation: pci_bus_read_config_dword changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000256 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bus_read_config_word
- Explanation: pci_bus_read_config_word changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000257 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bus_release_busn_res
- Explanation: pci_bus_release_busn_res changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000259 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bus_remove_resources
- Explanation: pci_bus_remove_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000260 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bus_resource_n
- Explanation: pci_bus_resource_n changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000261 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bus_set_current_state
- Explanation: pci_bus_set_current_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000262 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bus_set_ops
- Explanation: pci_bus_set_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000263 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bus_size_bridges
- Explanation: pci_bus_size_bridges changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000264 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bus_update_busn_res_end
- Explanation: pci_bus_update_busn_res_end changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000265 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bus_write_config_byte
- Explanation: pci_bus_write_config_byte changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000266 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bus_write_config_dword
- Explanation: pci_bus_write_config_dword changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000267 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bus_write_config_word
- Explanation: pci_bus_write_config_word changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000268 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_cfg_access_lock
- Explanation: pci_cfg_access_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000269 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_cfg_access_trylock
- Explanation: pci_cfg_access_trylock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000270 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_cfg_access_unlock
- Explanation: pci_cfg_access_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000272 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_check_and_mask_intx
- Explanation: pci_check_and_mask_intx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000273 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_check_and_unmask_intx
- Explanation: pci_check_and_unmask_intx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000274 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_choose_state
- Explanation: pci_choose_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000275 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_claim_bridge_resource
- Explanation: pci_claim_bridge_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000276 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_claim_resource
- Explanation: pci_claim_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000277 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_clear_and_set_config_dword
- Explanation: pci_clear_and_set_config_dword changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000278 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_clear_master
- Explanation: pci_clear_master changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000279 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_clear_mwi
- Explanation: pci_clear_mwi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000280 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_common_swizzle
- Explanation: pci_common_swizzle changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000281 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_create_root_bus
- Explanation: pci_create_root_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000282 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_create_slot
- Explanation: pci_create_slot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000283 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_d3cold_disable
- Explanation: pci_d3cold_disable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000284 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_d3cold_enable
- Explanation: pci_d3cold_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000285 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_destroy_slot
- Explanation: pci_destroy_slot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000286 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_dev_assign_slot
- Explanation: pci_dev_assign_slot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000287 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_dev_driver
- Explanation: pci_dev_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000289 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_dev_has_default_msi_parent_domain
- Explanation: pci_dev_has_default_msi_parent_domain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000290 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_dev_lock
- Explanation: pci_dev_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000291 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_dev_present
- Explanation: pci_dev_present changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000292 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_dev_put
- Explanation: pci_dev_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000293 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_dev_run_wake
- Explanation: pci_dev_run_wake changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000294 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_dev_trylock
- Explanation: pci_dev_trylock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000295 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_dev_unlock
- Explanation: pci_dev_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000296 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_device_add
- Explanation: pci_device_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000297 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_device_is_present
- Explanation: pci_device_is_present changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000298 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_devs_are_dma_aliases
- Explanation: pci_devs_are_dma_aliases changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000299 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_disable_device
- Explanation: pci_disable_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000301 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_disable_link_state_locked
- Explanation: pci_disable_link_state_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000303 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_disable_msix
- Explanation: pci_disable_msix changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000304 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_disable_parity
- Explanation: pci_disable_parity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000305 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_disable_rom
- Explanation: pci_disable_rom changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000306 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_enable_atomic_ops_to_root
- Explanation: pci_enable_atomic_ops_to_root changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000310 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_enable_link_state_locked
- Explanation: pci_enable_link_state_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000312 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_enable_msix_range
- Explanation: pci_enable_msix_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000313 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_enable_resources
- Explanation: pci_enable_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000314 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_enable_rom
- Explanation: pci_enable_rom changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000315 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_enable_wake
- Explanation: pci_enable_wake changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000316 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_ext_cfg_avail
- Explanation: pci_ext_cfg_avail changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000317 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_find_bus
- Explanation: pci_find_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000318 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_find_capability
- Explanation: pci_find_capability changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000319 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_find_dvsec_capability
- Explanation: pci_find_dvsec_capability changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000320 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_find_ext_capability
- Explanation: pci_find_ext_capability changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000321 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_find_host_bridge
- Explanation: pci_find_host_bridge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000322 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_find_ht_capability
- Explanation: pci_find_ht_capability changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000324 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_find_next_capability
- Explanation: pci_find_next_capability changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000325 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_find_next_ext_capability
- Explanation: pci_find_next_ext_capability changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000326 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_find_next_ht_capability
- Explanation: pci_find_next_ht_capability changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000327 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_find_parent_resource
- Explanation: pci_find_parent_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000329 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_find_vsec_capability
- Explanation: pci_find_vsec_capability changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000330 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_fixup_cardbus
- Explanation: pci_fixup_cardbus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000331 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_fixup_device
- Explanation: pci_fixup_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000332 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_for_each_dma_alias
- Explanation: pci_for_each_dma_alias changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000333 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_free_host_bridge
- Explanation: pci_free_host_bridge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000335 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_free_irq_vectors
- Explanation: pci_free_irq_vectors changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000336 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_free_resource_list
- Explanation: pci_free_resource_list changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000338 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_generic_config_read32
- Explanation: pci_generic_config_read32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000340 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_generic_config_write32
- Explanation: pci_generic_config_write32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000346 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_get_dsn
- Explanation: pci_get_dsn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000347 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_get_interrupt_pin
- Explanation: pci_get_interrupt_pin changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000351 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_host_probe
- Explanation: pci_host_probe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000352 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_hp_create_module_link
- Explanation: pci_hp_create_module_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000353 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_hp_remove_module_link
- Explanation: pci_hp_remove_module_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000354 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_ignore_hotplug
- Explanation: pci_ignore_hotplug changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000355 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_intx
- Explanation: pci_intx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000356 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_iommu_alloc
- Explanation: pci_iommu_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000357 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_ioremap_bar
- Explanation: pci_ioremap_bar changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000358 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_ioremap_wc_bar
- Explanation: pci_ioremap_wc_bar changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000359 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_irq_get_affinity
- Explanation: pci_irq_get_affinity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000361 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_legacy_init
- Explanation: pci_legacy_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000362 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_load_and_free_saved_state
- Explanation: pci_load_and_free_saved_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000363 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_load_saved_state
- Explanation: pci_load_saved_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000364 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_lock_rescan_remove
- Explanation: pci_lock_rescan_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000365 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_map_rom
- Explanation: pci_map_rom changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000367 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_mmap_resource_range
- Explanation: pci_mmap_resource_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000368 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_mmcfg_early_init
- Explanation: pci_mmcfg_early_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000369 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_mmcfg_late_init
- Explanation: pci_mmcfg_late_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000370 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_msi_enabled
- Explanation: pci_msi_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000371 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_msi_register_fwnode_provider
- Explanation: pci_msi_register_fwnode_provider changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000372 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_msi_vec_count
- Explanation: pci_msi_vec_count changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000373 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_msix_alloc_irq_at
- Explanation: pci_msix_alloc_irq_at changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000374 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_msix_can_alloc_dyn
- Explanation: pci_msix_can_alloc_dyn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000375 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_msix_free_irq
- Explanation: pci_msix_free_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000376 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_msix_vec_count
- Explanation: pci_msix_vec_count changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000377 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_pio_to_address
- Explanation: pci_pio_to_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000378 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_platform_power_transition
- Explanation: pci_platform_power_transition changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000379 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_pme_active
- Explanation: pci_pme_active changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000380 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_pme_capable
- Explanation: pci_pme_capable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000381 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_pr3_present
- Explanation: pci_pr3_present changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000382 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_prepare_to_sleep
- Explanation: pci_prepare_to_sleep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000383 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_probe_reset_bus
- Explanation: pci_probe_reset_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000384 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_probe_reset_slot
- Explanation: pci_probe_reset_slot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000385 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_read_bridge_bases
- Explanation: pci_read_bridge_bases changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000386 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_read_config_byte
- Explanation: pci_read_config_byte changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000387 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_read_config_dword
- Explanation: pci_read_config_dword changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000388 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_read_config_word
- Explanation: pci_read_config_word changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000390 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_read_vpd_any
- Explanation: pci_read_vpd_any changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000391 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_real_dma_dev
- Explanation: pci_real_dma_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000392 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_reassign_bridge_resources
- Explanation: pci_reassign_bridge_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000393 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_reassign_resource
- Explanation: pci_reassign_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000394 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_rebar_get_possible_sizes
- Explanation: pci_rebar_get_possible_sizes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000395 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_reenable_device
- Explanation: pci_reenable_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000397 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_register_set_vga_state
- Explanation: pci_register_set_vga_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000399 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_release_regions
- Explanation: pci_release_regions changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000400 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_release_resource
- Explanation: pci_release_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000401 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_release_selected_regions
- Explanation: pci_release_selected_regions changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000402 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_remap_iospace
- Explanation: pci_remap_iospace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000403 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_remove_bus
- Explanation: pci_remove_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000404 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_remove_root_bus
- Explanation: pci_remove_root_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000405 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_request_acs
- Explanation: pci_request_acs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000406 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_request_irq
- Explanation: pci_request_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000409 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_request_regions_exclusive
- Explanation: pci_request_regions_exclusive changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000411 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_request_selected_regions_exclusive
- Explanation: pci_request_selected_regions_exclusive changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000413 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_rescan_bus_bridge_resize
- Explanation: pci_rescan_bus_bridge_resize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000414 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_reset_bus
- Explanation: pci_reset_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000416 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_reset_function_locked
- Explanation: pci_reset_function_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000417 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_reset_secondary_bus
- Explanation: pci_reset_secondary_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000418 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_resize_resource
- Explanation: pci_resize_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000420 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_resource_to_user
- Explanation: pci_resource_to_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000421 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_restore_msi_state
- Explanation: pci_restore_msi_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000422 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_restore_state
- Explanation: pci_restore_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000423 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_resume_bus
- Explanation: pci_resume_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000424 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_save_state
- Explanation: pci_save_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000425 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_scan_bridge
- Explanation: pci_scan_bridge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000426 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_scan_bus
- Explanation: pci_scan_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000427 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_scan_child_bus
- Explanation: pci_scan_child_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000429 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_scan_root_bus_bridge
- Explanation: pci_scan_root_bus_bridge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000430 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_scan_single_device
- Explanation: pci_scan_single_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000431 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_scan_slot
- Explanation: pci_scan_slot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000432 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_select_bars
- Explanation: pci_select_bars changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000433 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_set_cacheline_size
- Explanation: pci_set_cacheline_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000435 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_set_host_bridge_release
- Explanation: pci_set_host_bridge_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000437 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_set_mwi
- Explanation: pci_set_mwi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000438 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_set_pcie_reset_state
- Explanation: pci_set_pcie_reset_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000440 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_set_power_state_locked
- Explanation: pci_set_power_state_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000441 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_set_vga_state
- Explanation: pci_set_vga_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000442 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_setup_bridge
- Explanation: pci_setup_bridge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000443 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_setup_cardbus
- Explanation: pci_setup_cardbus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000444 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_sort_breadthfirst
- Explanation: pci_sort_breadthfirst changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000445 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_status_get_and_clear_errors
- Explanation: pci_status_get_and_clear_errors changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000447 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_stop_and_remove_bus_device_locked
- Explanation: pci_stop_and_remove_bus_device_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000448 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_stop_root_bus
- Explanation: pci_stop_root_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000449 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_store_saved_state
- Explanation: pci_store_saved_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000450 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_swizzle_interrupt_pin
- Explanation: pci_swizzle_interrupt_pin changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000451 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_try_reset_function
- Explanation: pci_try_reset_function changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000452 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_try_set_mwi
- Explanation: pci_try_set_mwi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000453 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_uevent_ers
- Explanation: pci_uevent_ers changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000454 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_unlock_rescan_remove
- Explanation: pci_unlock_rescan_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000455 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_unmap_iospace
- Explanation: pci_unmap_iospace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000456 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_unmap_rom
- Explanation: pci_unmap_rom changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000458 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_update_resource
- Explanation: pci_update_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000459 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_user_read_config_byte
- Explanation: pci_user_read_config_byte changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000460 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_user_read_config_dword
- Explanation: pci_user_read_config_dword changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000461 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_user_read_config_word
- Explanation: pci_user_read_config_word changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000462 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_user_write_config_byte
- Explanation: pci_user_write_config_byte changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000463 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_user_write_config_dword
- Explanation: pci_user_write_config_dword changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000464 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_user_write_config_word
- Explanation: pci_user_write_config_word changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000465 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_vpd_alloc
- Explanation: pci_vpd_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000466 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_vpd_check_csum
- Explanation: pci_vpd_check_csum changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000467 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_vpd_find_id_string
- Explanation: pci_vpd_find_id_string changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000468 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_vpd_find_ro_info_keyword
- Explanation: pci_vpd_find_ro_info_keyword changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000470 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_wait_for_pending_transaction
- Explanation: pci_wait_for_pending_transaction changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000471 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_wake_from_d3
- Explanation: pci_wake_from_d3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000472 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_walk_bus
- Explanation: pci_walk_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000473 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_write_config_byte
- Explanation: pci_write_config_byte changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000474 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_write_config_dword
- Explanation: pci_write_config_dword changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000475 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_write_config_word
- Explanation: pci_write_config_word changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000477 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_write_vpd_any
- Explanation: pci_write_vpd_any changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000478 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_add_bus
- Explanation: pcibios_add_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000479 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_align_resource
- Explanation: pcibios_align_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000480 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_alloc_irq
- Explanation: pcibios_alloc_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000481 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_assign_all_busses
- Explanation: pcibios_assign_all_busses changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000482 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_bus_add_device
- Explanation: pcibios_bus_add_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000483 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_bus_to_resource
- Explanation: pcibios_bus_to_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000484 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_default_alignment
- Explanation: pcibios_default_alignment changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000485 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_device_add
- Explanation: pcibios_device_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000486 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_disable_device
- Explanation: pcibios_disable_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000487 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_enable_device
- Explanation: pcibios_enable_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000488 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_fixup_bus
- Explanation: pcibios_fixup_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000489 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_free_irq
- Explanation: pcibios_free_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000490 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_get_irq_routing_table
- Explanation: pcibios_get_irq_routing_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000491 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_penalize_isa_irq
- Explanation: pcibios_penalize_isa_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000492 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_release_device
- Explanation: pcibios_release_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000493 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_remove_bus
- Explanation: pcibios_remove_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000494 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_reset_secondary_bus
- Explanation: pcibios_reset_secondary_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000495 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_resource_survey_bus
- Explanation: pcibios_resource_survey_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000496 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_resource_to_bus
- Explanation: pcibios_resource_to_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000497 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_retrieve_fw_addr
- Explanation: pcibios_retrieve_fw_addr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000498 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_root_bridge_prepare
- Explanation: pcibios_root_bridge_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000499 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_scan_root
- Explanation: pcibios_scan_root changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000500 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_scan_specific_bus
- Explanation: pcibios_scan_specific_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000501 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_set_irq_routing
- Explanation: pcibios_set_irq_routing changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000502 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_set_master
- Explanation: pcibios_set_master changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000503 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_set_pcie_reset_state
- Explanation: pcibios_set_pcie_reset_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000505 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_setup_bridge
- Explanation: pcibios_setup_bridge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000506 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcibios_window_alignment
- Explanation: pcibios_window_alignment changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000507 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_aspm_enabled
- Explanation: pcie_aspm_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000508 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_aspm_support_enabled
- Explanation: pcie_aspm_support_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000509 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_bandwidth_available
- Explanation: pcie_bandwidth_available changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000510 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_bus_configure_settings
- Explanation: pcie_bus_configure_settings changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000511 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_capability_clear_and_set_dword
- Explanation: pcie_capability_clear_and_set_dword changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000512 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_capability_clear_and_set_word_locked
- Explanation: pcie_capability_clear_and_set_word_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000513 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_capability_clear_and_set_word_unlocked
- Explanation: pcie_capability_clear_and_set_word_unlocked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000514 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_capability_read_dword
- Explanation: pcie_capability_read_dword changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000515 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_capability_read_word
- Explanation: pcie_capability_read_word changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000516 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_capability_write_dword
- Explanation: pcie_capability_write_dword changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000517 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_capability_write_word
- Explanation: pcie_capability_write_word changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000518 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_flr
- Explanation: pcie_flr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000519 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_get_mps
- Explanation: pcie_get_mps changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000520 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_get_readrq
- Explanation: pcie_get_readrq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000521 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_get_speed_cap
- Explanation: pcie_get_speed_cap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000522 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_get_width_cap
- Explanation: pcie_get_width_cap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000523 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_link_speed_mbps
- Explanation: pcie_link_speed_mbps changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000524 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_mpss
- Explanation: pcie_mpss changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000525 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_no_aspm
- Explanation: pcie_no_aspm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000526 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_print_link_status
- Explanation: pcie_print_link_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000527 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_relaxed_ordering_enabled
- Explanation: pcie_relaxed_ordering_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000528 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_reset_flr
- Explanation: pcie_reset_flr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000529 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_set_mps
- Explanation: pcie_set_mps changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000530 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_set_readrq
- Explanation: pcie_set_readrq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000531 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcie_set_target_speed
- Explanation: pcie_set_target_speed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000532 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcim_enable_device
- Explanation: pcim_enable_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000533 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcim_intx
- Explanation: pcim_intx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000535 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcim_iomap_range
- Explanation: pcim_iomap_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000537 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcim_iomap_regions
- Explanation: pcim_iomap_regions changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000538 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcim_iomap_table
- Explanation: pcim_iomap_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000541 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcim_iounmap_regions
- Explanation: pcim_iounmap_regions changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000542 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcim_pin_device
- Explanation: pcim_pin_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000543 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcim_request_all_regions
- Explanation: pcim_request_all_regions changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000544 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcim_request_region
- Explanation: pcim_request_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000545 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcim_set_mwi
- Explanation: pcim_set_mwi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000546 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcix_get_max_mmrbc
- Explanation: pcix_get_max_mmrbc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000547 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcix_get_mmrbc
- Explanation: pcix_get_mmrbc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000548 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcix_set_mmrbc
- Explanation: pcix_set_mmrbc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000549 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pgprot2cachemode
- Explanation: pgprot2cachemode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000550 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_config_inband
- Explanation: phy_config_inband changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000551 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_disable_eee
- Explanation: phy_disable_eee changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000552 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_eee_rx_clock_stop
- Explanation: phy_eee_rx_clock_stop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000553 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_eee_tx_clock_stop_capable
- Explanation: phy_eee_tx_clock_stop_capable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000554 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_inband_caps
- Explanation: phy_inband_caps changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000555 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pinned
- Explanation: pinned changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000556 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_add_devices
- Explanation: platform_add_devices changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000558 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_device_add_data
- Explanation: platform_device_add_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000559 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_device_add_resources
- Explanation: platform_device_add_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000560 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_device_alloc
- Explanation: platform_device_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000561 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_device_del
- Explanation: platform_device_del changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000562 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_device_put
- Explanation: platform_device_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000564 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_device_register_full
- Explanation: platform_device_register_full changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000565 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_device_unregister
- Explanation: platform_device_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000567 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_find_device_by_driver
- Explanation: platform_find_device_by_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000571 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_get_irq_byname_optional
- Explanation: platform_get_irq_byname_optional changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000572 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_get_irq_optional
- Explanation: platform_get_irq_optional changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000573 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_get_mem_or_io
- Explanation: platform_get_mem_or_io changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000575 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_get_resource_byname
- Explanation: platform_get_resource_byname changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000576 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_irq_count
- Explanation: platform_irq_count changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000577 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_pm_freeze
- Explanation: platform_pm_freeze changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000578 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_pm_poweroff
- Explanation: platform_pm_poweroff changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000579 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_pm_restore
- Explanation: platform_pm_restore changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000580 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_pm_resume
- Explanation: platform_pm_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000581 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_pm_suspend
- Explanation: platform_pm_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000582 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_pm_thaw
- Explanation: platform_pm_thaw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000584 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_unregister_drivers
- Explanation: platform_unregister_drivers changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000585 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pme_poll
- Explanation: pme_poll changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000586 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pme_support
- Explanation: pme_support changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000587 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pref_64_window
- Explanation: pref_64_window changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000588 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pref_window
- Explanation: pref_window changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000589 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: preserve_config
- Explanation: preserve_config changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000590 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pri_enabled
- Explanation: pri_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000591 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: property_entries_dup
- Explanation: property_entries_dup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000592 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: property_entries_free
- Explanation: property_entries_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000593 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: put_cmsg_notrunc
- Explanation: put_cmsg_notrunc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000594 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: queue_limits_commit_update_frozen
- Explanation: queue_limits_commit_update_frozen changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000595 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: raw_pci_read
- Explanation: raw_pci_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000596 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: raw_pci_write
- Explanation: raw_pci_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000599 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rcuref_put_slowpath
- Explanation: rcuref_put_slowpath changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'ref_', 'type': '*mut rcuref_t'}], 'return_type': 'bool_'}`
- New: `{'params': [{'name': 'ref_', 'type': '*mut rcuref_t'}, {'name': 'cnt', 'type': 'ffi::c_uint'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000601 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: readb_relaxed
- Explanation: readb_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000603 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: readl_relaxed
- Explanation: readl_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000604 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: readlink_copy
- Explanation: readlink_copy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut ffi::c_char'}, {'name': 'arg2', 'type': 'ffi::c_int'}, {'name': 'arg3', 'type': '*const ffi::c_char'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*mut ffi::c_char'}, {'name': 'arg2', 'type': 'ffi::c_int'}, {'name': 'arg3', 'type': '*const ffi::c_char'}, {'name': 'arg4', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000606 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: readq_relaxed
- Explanation: readq_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000608 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: readw_relaxed
- Explanation: readw_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000609 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: register_pidns_sysctls
- Explanation: register_pidns_sysctls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000610 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: resource_list_create_entry
- Explanation: resource_list_create_entry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000611 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: resource_list_free
- Explanation: resource_list_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000613 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rom_attr_enabled
- Explanation: rom_attr_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000614 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rom_bar_overlap
- Explanation: rom_bar_overlap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000615 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sched_task_hot
- Explanation: sched_task_hot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000616 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_dentry_init_security
- Explanation: security_dentry_init_security changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'dentry', 'type': '*mut dentry'}, {'name': 'mode', 'type': 'ffi::c_int'}, {'name': 'name', 'type': '*const qstr'}, {'name': 'xattr_name', 'type': '*mut *const ffi::c_char'}, {'name': 'ctx', 'type': '*mut *mut ffi::c_void'}, {'name': 'ctxlen', 'type': '*mut u32_'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'dentry', 'type': '*mut dentry'}, {'name': 'mode', 'type': 'ffi::c_int'}, {'name': 'name', 'type': '*const qstr'}, {'name': 'xattr_name', 'type': '*mut *const ffi::c_char'}, {'name': 'lsmcxt', 'type': '*mut lsm_context'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000617 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_getsecctx
- Explanation: security_inode_getsecctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'inode', 'type': '*mut inode'}, {'name': 'ctx', 'type': '*mut *mut ffi::c_void'}, {'name': 'ctxlen', 'type': '*mut u32_'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'inode', 'type': '*mut inode'}, {'name': 'cp', 'type': '*mut lsm_context'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000618 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_lsmprop_to_secctx
- Explanation: security_lsmprop_to_secctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'prop', 'type': '*mut lsm_prop'}, {'name': 'secdata', 'type': '*mut *mut ffi::c_char'}, {'name': 'seclen', 'type': '*mut u32_'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'prop', 'type': '*mut lsm_prop'}, {'name': 'cp', 'type': '*mut lsm_context'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000621 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_active
- Explanation: set_active changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000622 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_pcie_hotplug_bridge
- Explanation: set_pcie_hotplug_bridge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000623 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_pcie_port_type
- Explanation: set_pcie_port_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000624 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: shpc_managed
- Explanation: shpc_managed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000626 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: size_windows
- Explanation: size_windows changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000627 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_cow_data_for_xdp
- Explanation: skb_cow_data_for_xdp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'pool', 'type': '*mut page_pool'}, {'name': 'pskb', 'type': '*mut *mut sk_buff'}, {'name': 'prog', 'type': '*mut bpf_prog'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'pool', 'type': '*mut page_pool'}, {'name': 'pskb', 'type': '*mut *mut sk_buff'}, {'name': 'prog', 'type': '*const bpf_prog'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000628 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skip_bus_pm
- Explanation: skip_bus_pm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000629 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: software_node_find_by_name
- Explanation: software_node_find_by_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000630 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: software_node_fwnode
- Explanation: software_node_fwnode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000632 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: software_node_register_node_group
- Explanation: software_node_register_node_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000634 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: software_node_unregister_node_group
- Explanation: software_node_unregister_node_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000636 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: state_saved
- Explanation: state_saved changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000637 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_bin_attr_simple_read
- Explanation: sysfs_bin_attr_simple_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'file', 'type': '*mut file'}, {'name': 'kobj', 'type': '*mut kobject'}, {'name': 'attr', 'type': '*mut bin_attribute'}, {'name': 'buf', 'type': '*mut ffi::c_char'}, {'name': 'off', 'type': 'loff_t'}, {'name': 'count', 'type': 'usize'}], 'return_type': 'isize'}`
- New: `{'params': [{'name': 'file', 'type': '*mut file'}, {'name': 'kobj', 'type': '*mut kobject'}, {'name': 'attr', 'type': '*const bin_attribute'}, {'name': 'buf', 'type': '*mut ffi::c_char'}, {'name': 'off', 'type': 'loff_t'}, {'name': 'count', 'type': 'usize'}], 'return_type': 'isize'}`

### Rust Evidence

- Graph edges: `1`

## W-000638 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: to_software_node
- Explanation: to_software_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000639 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: tph_enabled
- Explanation: tph_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000641 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unregister_pidns_sysctls
- Explanation: unregister_pidns_sysctls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000642 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unsafe_warn
- Explanation: unsafe_warn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000643 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: untrusted
- Explanation: untrusted changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000644 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wakeup_prepared
- Explanation: wakeup_prepared changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000646 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: writeb_relaxed
- Explanation: writeb_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000648 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: writel_relaxed
- Explanation: writel_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000650 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: writeq_relaxed
- Explanation: writeq_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000652 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: writew_relaxed
- Explanation: writew_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000653 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: x86_has_pat_wp
- Explanation: x86_has_pat_wp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000824 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kunit_test_suites_init
- Explanation: __kunit_test_suites_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct kunit_suite * const * const suites', 'int num_suites'], 'return_type': 'int'}`
- New: `{'params': ['struct kunit_suite * const * const suites', 'int num_suites', 'bool run_tests'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000830 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_from_early_mem
- Explanation: copy_from_early_mem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['void *dest', 'phys_addr_t src', 'unsigned long size'], 'return_type': 'extern void'}`
- New: `{'params': ['void *dest', 'phys_addr_t src', 'unsigned long size'], 'return_type': 'extern int'}`

### Rust Evidence

- Graph edges: `1`

## W-000833 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_eee_is_active
- Explanation: genphy_c45_eee_is_active changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct phy_device *phydev', 'unsigned long *adv', 'unsigned long *lp', 'bool *is_enabled'], 'return_type': 'int'}`
- New: `{'params': ['struct phy_device *phydev', 'unsigned long *adv', 'unsigned long *lp'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000837 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: readlink_copy
- Explanation: readlink_copy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['char __user *', 'int', 'const char *'], 'return_type': 'extern int'}`
- New: `{'params': ['char __user *', 'int', 'const char *', 'int'], 'return_type': 'extern int'}`

### Rust Evidence

- Graph edges: `1`

## W-000841 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_dentry_init_security
- Explanation: security_dentry_init_security changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct dentry *dentry', 'int mode', 'const struct qstr *name', 'const char **xattr_name', 'void **ctx', 'u32 *ctxlen'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct dentry *dentry', 'int mode', 'const struct qstr *name', 'const char **xattr_name', 'struct lsm_context *lsmcxt'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `1`

## W-000842 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_getsecctx
- Explanation: security_inode_getsecctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct inode *inode', 'void **ctx', 'u32 *ctxlen'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct inode *inode', 'struct lsm_context *cp'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `1`

## W-000843 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_lsmprop_to_secctx
- Explanation: security_lsmprop_to_secctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct lsm_prop *prop', 'char **secdata', 'u32 *seclen'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct lsm_prop *prop', 'struct lsm_context *cp'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `1`

## W-000839 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_security_release_secctx
- Explanation: rust_helper_security_release_secctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['char *secdata', 'u32 seclen'], 'return_type': 'void'}`
- New: `{'params': ['struct lsm_context *cp'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000840 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_security_secid_to_secctx
- Explanation: rust_helper_security_secid_to_secctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u32 secid', 'char **secdata', 'u32 *seclen'], 'return_type': 'int'}`
- New: `{'params': ['u32 secid', 'struct lsm_context *cp'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000658 FieldDrift

- Risk: High
- Score: 10.4
- Symbol: dentry
- Explanation: dentry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'd_flags', 'type': 'ffi::c_uint'}, {'name': 'd_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'd_hash', 'type': 'hlist_bl_node'}, {'name': 'd_parent', 'type': '*mut dentry'}, {'name': 'd_name', 'type': 'qstr'}, {'name': 'd_inode', 'type': '*mut inode'}, {'name': 'd_iname', 'type': '[ffi::c_uchar; 40usize]'}, {'name': 'd_op', 'type': '*const dentry_operations'}, {'name': 'd_sb', 'type': '*mut super_block'}, {'name': 'd_time', 'type': 'ffi::c_ulong'}, {'name': 'd_fsdata', 'type': '*mut ffi::c_void'}, {'name': 'd_lockref', 'type': 'lockref'}, {'name': '__bindgen_anon_1', 'type': 'dentry__bindgen_ty_1'}, {'name': 'd_sib', 'type': 'hlist_node'}, {'name': 'd_children', 'type': 'hlist_head'}, {'name': 'd_u', 'type': 'dentry__bindgen_ty_2'}]`
- New: `[{'name': 'd_flags', 'type': 'ffi::c_uint'}, {'name': 'd_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'd_hash', 'type': 'hlist_bl_node'}, {'name': 'd_parent', 'type': '*mut dentry'}, {'name': 'd_name', 'type': 'qstr'}, {'name': 'd_inode', 'type': '*mut inode'}, {'name': 'd_shortname', 'type': 'shortname_store'}, {'name': 'd_op', 'type': '*const dentry_operations'}, {'name': 'd_sb', 'type': '*mut super_block'}, {'name': 'd_time', 'type': 'ffi::c_ulong'}, {'name': 'd_fsdata', 'type': '*mut ffi::c_void'}, {'name': 'd_lockref', 'type': 'lockref'}, {'name': '__bindgen_anon_1', 'type': 'dentry__bindgen_ty_1'}, {'name': 'd_sib', 'type': 'hlist_node'}, {'name': 'd_children', 'type': 'hlist_head'}, {'name': 'd_u', 'type': 'dentry__bindgen_ty_2'}]`

### Rust Evidence

- Graph edges: `9`

## W-000670 FieldDrift

- Risk: High
- Score: 10.0
- Symbol: kstat
- Explanation: kstat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'result_mask', 'type': 'u32_'}, {'name': 'mode', 'type': 'umode_t'}, {'name': 'nlink', 'type': 'ffi::c_uint'}, {'name': 'blksize', 'type': 'u32'}, {'name': 'attributes', 'type': 'u64_'}, {'name': 'attributes_mask', 'type': 'u64_'}, {'name': 'ino', 'type': 'u64_'}, {'name': 'dev', 'type': 'dev_t'}, {'name': 'rdev', 'type': 'dev_t'}, {'name': 'uid', 'type': 'kuid_t'}, {'name': 'gid', 'type': 'kgid_t'}, {'name': 'size', 'type': 'loff_t'}, {'name': 'atime', 'type': 'timespec64'}, {'name': 'mtime', 'type': 'timespec64'}, {'name': 'ctime', 'type': 'timespec64'}, {'name': 'btime', 'type': 'timespec64'}, {'name': 'blocks', 'type': 'u64_'}, {'name': 'mnt_id', 'type': 'u64_'}, {'name': 'dio_mem_align', 'type': 'u32_'}, {'name': 'dio_offset_align', 'type': 'u32_'}, {'name': 'change_cookie', 'type': 'u64_'}, {'name': 'subvol', 'type': 'u64_'}, {'name': 'atomic_write_unit_min', 'type': 'u32_'}, {'name': 'atomic_write_unit_max', 'type': 'u32_'}, {'name': 'atomic_write_segments_max', 'type': 'u32_'}]`
- New: `[{'name': 'result_mask', 'type': 'u32_'}, {'name': 'mode', 'type': 'umode_t'}, {'name': 'nlink', 'type': 'ffi::c_uint'}, {'name': 'blksize', 'type': 'u32'}, {'name': 'attributes', 'type': 'u64_'}, {'name': 'attributes_mask', 'type': 'u64_'}, {'name': 'ino', 'type': 'u64_'}, {'name': 'dev', 'type': 'dev_t'}, {'name': 'rdev', 'type': 'dev_t'}, {'name': 'uid', 'type': 'kuid_t'}, {'name': 'gid', 'type': 'kgid_t'}, {'name': 'size', 'type': 'loff_t'}, {'name': 'atime', 'type': 'timespec64'}, {'name': 'mtime', 'type': 'timespec64'}, {'name': 'ctime', 'type': 'timespec64'}, {'name': 'btime', 'type': 'timespec64'}, {'name': 'blocks', 'type': 'u64_'}, {'name': 'mnt_id', 'type': 'u64_'}, {'name': 'change_cookie', 'type': 'u64_'}, {'name': 'subvol', 'type': 'u64_'}, {'name': 'dio_mem_align', 'type': 'u32_'}, {'name': 'dio_offset_align', 'type': 'u32_'}, {'name': 'dio_read_offset_align', 'type': 'u32_'}, {'name': 'atomic_write_unit_min', 'type': 'u32_'}, {'name': 'atomic_write_unit_max', 'type': 'u32_'}, {'name': 'atomic_write_segments_max', 'type': 'u32_'}]`

### Rust Evidence

- Graph edges: `7`

## W-000691 FieldDrift

- Risk: High
- Score: 10.0
- Symbol: uprobe_task
- Explanation: uprobe_task changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'state', 'type': 'uprobe_task_state'}, {'name': 'depth', 'type': 'ffi::c_uint'}, {'name': 'return_instances', 'type': '*mut return_instance'}, {'name': '__bindgen_anon_1', 'type': 'uprobe_task__bindgen_ty_1'}, {'name': 'active_uprobe', 'type': '*mut uprobe'}, {'name': 'ri_timer', 'type': 'timer_list'}, {'name': 'xol_vaddr', 'type': 'ffi::c_ulong'}, {'name': 'auprobe', 'type': '*mut arch_uprobe'}]`
- New: `[{'name': 'state', 'type': 'uprobe_task_state'}, {'name': 'depth', 'type': 'ffi::c_uint'}, {'name': 'return_instances', 'type': '*mut return_instance'}, {'name': 'ri_pool', 'type': '*mut return_instance'}, {'name': 'ri_timer', 'type': 'timer_list'}, {'name': 'ri_seqcount', 'type': 'seqcount_t'}, {'name': '__bindgen_anon_1', 'type': 'uprobe_task__bindgen_ty_1'}, {'name': 'active_uprobe', 'type': '*mut uprobe'}, {'name': 'xol_vaddr', 'type': 'ffi::c_ulong'}, {'name': 'auprobe', 'type': '*mut arch_uprobe'}]`

### Rust Evidence

- Graph edges: `7`

## W-000013 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: alloc_pages_bulk_array_mempolicy_noprof
- Explanation: alloc_pages_bulk_array_mempolicy_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000016 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: alloc_pages_mpol_noprof
- Explanation: alloc_pages_mpol_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000020 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: bio_add_pc_page
- Explanation: bio_add_pc_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000045 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: device_find_any_child
- Explanation: device_find_any_child changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000047 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: device_find_child_by_name
- Explanation: device_find_child_by_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000092 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: expand_downwards
- Explanation: expand_downwards changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000143 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: init_cpu_online
- Explanation: init_cpu_online changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000159 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: kernel_sendmsg_locked
- Explanation: kernel_sendmsg_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000160 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: kobj_ns_initial
- Explanation: kobj_ns_initial changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000161 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: kobj_ns_netlink
- Explanation: kobj_ns_netlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000166 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ktime_get_fast_timestamps
- Explanation: ktime_get_fast_timestamps changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000174 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: lockref_put_not_zero
- Explanation: lockref_put_not_zero changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000185 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mmap_region
- Explanation: mmap_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000215 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: override_creds
- Explanation: override_creds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000612 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: revert_creds
- Explanation: revert_creds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000625 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: simple_offset_empty
- Explanation: simple_offset_empty changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000825 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: acpi_device_hid
- Explanation: acpi_device_hid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct acpi_device *device'], 'return_type': 'const char *'}`
- New: `{'params': ['struct acpi_device *device'], 'return_type': 'static inline const char *'}`

### Rust Evidence

- Graph edges: `0`

## W-000826 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: acpi_get_physical_device_location
- Explanation: acpi_get_physical_device_location changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['acpi_handle handle', 'struct acpi_pld_info **pld'], 'return_type': 'acpi_status'}`
- New: `{'params': ['acpi_handle handle', 'struct acpi_pld_info **pld'], 'return_type': 'static inline bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000827 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: blk_mq_add_to_batch
- Explanation: blk_mq_add_to_batch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct request *req', 'struct io_comp_batch *iob', 'int ioerror', 'void (*complete)(struct io_comp_batch *)'], 'return_type': 'static inline bool'}`
- New: `{'params': ['struct request *req', 'struct io_comp_batch *iob', 'bool is_error', 'void (*complete)(struct io_comp_batch *)'], 'return_type': 'static inline bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000831 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: dev_get_drvdata
- Explanation: dev_get_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['&mdio->dev'], 'return_type': 'return'}`
- New: `{'params': ['&pdev->dev'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-000832 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_dp_get_vc_payload_bw
- Explanation: drm_dp_get_vc_payload_bw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct drm_dp_mst_topology_mgr *mgr', 'int link_rate', 'int link_lane_count'], 'return_type': 'fixed20_12'}`
- New: `{'params': ['int link_rate', 'int link_lane_count'], 'return_type': 'fixed20_12'}`

### Rust Evidence

- Graph edges: `0`

## W-000834 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: huge_ptep_get_and_clear
- Explanation: huge_ptep_get_and_clear changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mm_struct *mm', 'unsigned long addr', 'pte_t *ptep'], 'return_type': 'static inline pte_t'}`
- New: `{'params': ['struct mm_struct *mm', 'unsigned long addr', 'pte_t *ptep', 'unsigned long sz'], 'return_type': 'static inline pte_t'}`

### Rust Evidence

- Graph edges: `0`

## W-000835 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: override_creds
- Explanation: override_creds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct cred *'], 'return_type': 'extern const struct cred *'}`
- New: `{'params': ['const struct cred *override_cred'], 'return_type': 'static inline const struct cred *'}`

### Rust Evidence

- Graph edges: `0`

## W-000836 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: pci_register_driver
- Explanation: pci_register_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['pci_drv'], 'return_type': 'return'}`
- New: `{'params': ['struct pci_driver *drv'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `0`

## W-000838 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: revert_creds
- Explanation: revert_creds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct cred *'], 'return_type': 'extern void'}`
- New: `{'params': ['const struct cred *revert_cred'], 'return_type': 'static inline const struct cred *'}`

### Rust Evidence

- Graph edges: `0`

## W-000846 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: skcipher_walk_done
- Explanation: skcipher_walk_done changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct skcipher_walk *walk', 'int err'], 'return_type': 'int'}`
- New: `{'params': ['struct skcipher_walk *walk', 'int res'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000847 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: tlb_remove_table
- Explanation: tlb_remove_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mmu_gather *tlb', 'void *table'], 'return_type': 'extern void'}`
- New: `{'params': ['struct mmu_gather *tlb', 'void *table'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-000848 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ttm_resource_alloc
- Explanation: ttm_resource_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct ttm_buffer_object *bo', 'const struct ttm_place *place', 'struct ttm_resource **res'], 'return_type': 'int'}`
- New: `{'params': ['struct ttm_buffer_object *bo', 'const struct ttm_place *place', 'struct ttm_resource **res', 'struct dmem_cgroup_pool_state **ret_limit_pool'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000684 FieldDrift

- Risk: Medium
- Score: 9.4
- Symbol: sched_domain
- Explanation: sched_domain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'parent', 'type': '*mut sched_domain'}, {'name': 'child', 'type': '*mut sched_domain'}, {'name': 'groups', 'type': '*mut sched_group'}, {'name': 'min_interval', 'type': 'ffi::c_ulong'}, {'name': 'max_interval', 'type': 'ffi::c_ulong'}, {'name': 'busy_factor', 'type': 'ffi::c_uint'}, {'name': 'imbalance_pct', 'type': 'ffi::c_uint'}, {'name': 'cache_nice_tries', 'type': 'ffi::c_uint'}, {'name': 'imb_numa_nr', 'type': 'ffi::c_uint'}, {'name': 'nohz_idle', 'type': 'ffi::c_int'}, {'name': 'flags', 'type': 'ffi::c_int'}, {'name': 'level', 'type': 'ffi::c_int'}, {'name': 'last_balance', 'type': 'ffi::c_ulong'}, {'name': 'balance_interval', 'type': 'ffi::c_uint'}, {'name': 'nr_balance_failed', 'type': 'ffi::c_uint'}, {'name': 'max_newidle_lb_cost', 'type': 'u64_'}, {'name': 'last_decay_max_lb_cost', 'type': 'ffi::c_ulong'}, {'name': 'lb_count', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_failed', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_balanced', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_imbalance', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_gained', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_hot_gained', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_nobusyg', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_nobusyq', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'alb_count', 'type': 'ffi::c_uint'}, {'name': 'alb_failed', 'type': 'ffi::c_uint'}, {'name': 'alb_pushed', 'type': 'ffi::c_uint'}, {'name': 'sbe_count', 'type': 'ffi::c_uint'}, {'name': 'sbe_balanced', 'type': 'ffi::c_uint'}, {'name': 'sbe_pushed', 'type': 'ffi::c_uint'}, {'name': 'sbf_count', 'type': 'ffi::c_uint'}, {'name': 'sbf_balanced', 'type': 'ffi::c_uint'}, {'name': 'sbf_pushed', 'type': 'ffi::c_uint'}, {'name': 'ttwu_wake_remote', 'type': 'ffi::c_uint'}, {'name': 'ttwu_move_affine', 'type': 'ffi::c_uint'}, {'name': 'ttwu_move_balance', 'type': 'ffi::c_uint'}, {'name': '__bindgen_anon_1', 'type': 'sched_domain__bindgen_ty_1'}, {'name': 'shared', 'type': '*mut sched_domain_shared'}, {'name': 'span_weight', 'type': 'ffi::c_uint'}, {'name': 'span', 'type': '__IncompleteArrayField<ffi::c_ulong>'}]`
- New: `[{'name': 'parent', 'type': '*mut sched_domain'}, {'name': 'child', 'type': '*mut sched_domain'}, {'name': 'groups', 'type': '*mut sched_group'}, {'name': 'min_interval', 'type': 'ffi::c_ulong'}, {'name': 'max_interval', 'type': 'ffi::c_ulong'}, {'name': 'busy_factor', 'type': 'ffi::c_uint'}, {'name': 'imbalance_pct', 'type': 'ffi::c_uint'}, {'name': 'cache_nice_tries', 'type': 'ffi::c_uint'}, {'name': 'imb_numa_nr', 'type': 'ffi::c_uint'}, {'name': 'nohz_idle', 'type': 'ffi::c_int'}, {'name': 'flags', 'type': 'ffi::c_int'}, {'name': 'level', 'type': 'ffi::c_int'}, {'name': 'last_balance', 'type': 'ffi::c_ulong'}, {'name': 'balance_interval', 'type': 'ffi::c_uint'}, {'name': 'nr_balance_failed', 'type': 'ffi::c_uint'}, {'name': 'max_newidle_lb_cost', 'type': 'u64_'}, {'name': 'last_decay_max_lb_cost', 'type': 'ffi::c_ulong'}, {'name': 'lb_count', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_failed', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_balanced', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_imbalance_load', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_imbalance_util', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_imbalance_task', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_imbalance_misfit', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_gained', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_hot_gained', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_nobusyg', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_nobusyq', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'alb_count', 'type': 'ffi::c_uint'}, {'name': 'alb_failed', 'type': 'ffi::c_uint'}, {'name': 'alb_pushed', 'type': 'ffi::c_uint'}, {'name': 'sbe_count', 'type': 'ffi::c_uint'}, {'name': 'sbe_balanced', 'type': 'ffi::c_uint'}, {'name': 'sbe_pushed', 'type': 'ffi::c_uint'}, {'name': 'sbf_count', 'type': 'ffi::c_uint'}, {'name': 'sbf_balanced', 'type': 'ffi::c_uint'}, {'name': 'sbf_pushed', 'type': 'ffi::c_uint'}, {'name': 'ttwu_wake_remote', 'type': 'ffi::c_uint'}, {'name': 'ttwu_move_affine', 'type': 'ffi::c_uint'}, {'name': 'ttwu_move_balance', 'type': 'ffi::c_uint'}, {'name': 'name', 'type': '*mut ffi::c_char'}, {'name': '__bindgen_anon_1', 'type': 'sched_domain__bindgen_ty_1'}, {'name': 'shared', 'type': '*mut sched_domain_shared'}, {'name': 'span_weight', 'type': 'ffi::c_uint'}, {'name': 'span', 'type': '__IncompleteArrayField<ffi::c_ulong>'}]`

### Rust Evidence

- Graph edges: `4`

## W-000657 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: cpuinfo_topology
- Explanation: cpuinfo_topology changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'apicid', 'type': 'u32_'}, {'name': 'initial_apicid', 'type': 'u32_'}, {'name': 'pkg_id', 'type': 'u32_'}, {'name': 'die_id', 'type': 'u32_'}, {'name': 'cu_id', 'type': 'u32_'}, {'name': 'core_id', 'type': 'u32_'}, {'name': 'logical_pkg_id', 'type': 'u32_'}, {'name': 'logical_die_id', 'type': 'u32_'}, {'name': 'amd_node_id', 'type': 'u32_'}, {'name': 'llc_id', 'type': 'u32_'}, {'name': 'l2c_id', 'type': 'u32_'}, {'name': '__bindgen_anon_1', 'type': 'cpuinfo_topology__bindgen_ty_1'}]`
- New: `[{'name': 'apicid', 'type': 'u32_'}, {'name': 'initial_apicid', 'type': 'u32_'}, {'name': 'pkg_id', 'type': 'u32_'}, {'name': 'die_id', 'type': 'u32_'}, {'name': 'cu_id', 'type': 'u32_'}, {'name': 'core_id', 'type': 'u32_'}, {'name': 'logical_pkg_id', 'type': 'u32_'}, {'name': 'logical_die_id', 'type': 'u32_'}, {'name': 'logical_core_id', 'type': 'u32_'}, {'name': 'amd_node_id', 'type': 'u32_'}, {'name': 'llc_id', 'type': 'u32_'}, {'name': 'l2c_id', 'type': 'u32_'}, {'name': '__bindgen_anon_1', 'type': 'cpuinfo_topology__bindgen_ty_1'}]`

### Rust Evidence

- Graph edges: `3`

## W-000692 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: vm_area_struct
- Explanation: vm_area_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'vm_area_struct__bindgen_ty_1'}, {'name': 'vm_mm', 'type': '*mut mm_struct'}, {'name': 'vm_page_prot', 'type': 'pgprot_t'}, {'name': '__bindgen_anon_2', 'type': 'vm_area_struct__bindgen_ty_2'}, {'name': 'detached', 'type': 'bool_'}, {'name': 'vm_lock_seq', 'type': 'ffi::c_int'}, {'name': 'vm_lock', 'type': '*mut vma_lock'}, {'name': 'shared', 'type': 'vm_area_struct__bindgen_ty_3'}, {'name': 'anon_vma_chain', 'type': 'list_head'}, {'name': 'anon_vma', 'type': '*mut anon_vma'}, {'name': 'vm_ops', 'type': '*const vm_operations_struct'}, {'name': 'vm_pgoff', 'type': 'ffi::c_ulong'}, {'name': 'vm_file', 'type': '*mut file'}, {'name': 'vm_private_data', 'type': '*mut ffi::c_void'}, {'name': 'swap_readahead_info', 'type': 'atomic_long_t'}, {'name': 'vm_policy', 'type': '*mut mempolicy'}, {'name': 'vm_userfaultfd_ctx', 'type': 'vm_userfaultfd_ctx'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'vm_area_struct__bindgen_ty_1'}, {'name': 'vm_mm', 'type': '*mut mm_struct'}, {'name': 'vm_page_prot', 'type': 'pgprot_t'}, {'name': '__bindgen_anon_2', 'type': 'vm_area_struct__bindgen_ty_2'}, {'name': 'detached', 'type': 'bool_'}, {'name': 'vm_lock_seq', 'type': 'ffi::c_uint'}, {'name': 'vm_lock', 'type': '*mut vma_lock'}, {'name': 'shared', 'type': 'vm_area_struct__bindgen_ty_3'}, {'name': 'anon_vma_chain', 'type': 'list_head'}, {'name': 'anon_vma', 'type': '*mut anon_vma'}, {'name': 'vm_ops', 'type': '*const vm_operations_struct'}, {'name': 'vm_pgoff', 'type': 'ffi::c_ulong'}, {'name': 'vm_file', 'type': '*mut file'}, {'name': 'vm_private_data', 'type': '*mut ffi::c_void'}, {'name': 'swap_readahead_info', 'type': 'atomic_long_t'}, {'name': 'vm_policy', 'type': '*mut mempolicy'}, {'name': 'vm_userfaultfd_ctx', 'type': 'vm_userfaultfd_ctx'}]`

### Rust Evidence

- Graph edges: `3`

## W-000672 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: mm_struct__bindgen_ty_1
- Explanation: mm_struct__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'mm_struct__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mm_mt', 'type': 'maple_tree'}, {'name': 'mmap_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'task_size', 'type': 'ffi::c_ulong'}, {'name': 'pgd', 'type': '*mut pgd_t'}, {'name': 'membarrier_state', 'type': 'atomic_t'}, {'name': 'mm_users', 'type': 'atomic_t'}, {'name': 'pcpu_cid', 'type': '*mut mm_cid'}, {'name': 'mm_cid_next_scan', 'type': 'ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_uint'}, {'name': 'max_nr_cid', 'type': 'atomic_t'}, {'name': 'cpus_allowed_lock', 'type': 'raw_spinlock_t'}, {'name': 'pgtables_bytes', 'type': 'atomic_long_t'}, {'name': 'map_count', 'type': 'ffi::c_int'}, {'name': 'page_table_lock', 'type': 'spinlock_t'}, {'name': 'mmap_lock', 'type': 'rw_semaphore'}, {'name': 'mmlist', 'type': 'list_head'}, {'name': 'mm_lock_seq', 'type': 'ffi::c_int'}, {'name': 'hiwater_rss', 'type': 'ffi::c_ulong'}, {'name': 'hiwater_vm', 'type': 'ffi::c_ulong'}, {'name': 'total_vm', 'type': 'ffi::c_ulong'}, {'name': 'locked_vm', 'type': 'ffi::c_ulong'}, {'name': 'pinned_vm', 'type': 'atomic64_t'}, {'name': 'data_vm', 'type': 'ffi::c_ulong'}, {'name': 'exec_vm', 'type': 'ffi::c_ulong'}, {'name': 'stack_vm', 'type': 'ffi::c_ulong'}, {'name': 'def_flags', 'type': 'ffi::c_ulong'}, {'name': 'write_protect_seq', 'type': 'seqcount_t'}, {'name': 'arg_lock', 'type': 'spinlock_t'}, {'name': 'start_code', 'type': 'ffi::c_ulong'}, {'name': 'end_code', 'type': 'ffi::c_ulong'}, {'name': 'start_data', 'type': 'ffi::c_ulong'}, {'name': 'end_data', 'type': 'ffi::c_ulong'}, {'name': 'start_brk', 'type': 'ffi::c_ulong'}, {'name': 'brk', 'type': 'ffi::c_ulong'}, {'name': 'start_stack', 'type': 'ffi::c_ulong'}, {'name': 'arg_start', 'type': 'ffi::c_ulong'}, {'name': 'arg_end', 'type': 'ffi::c_ulong'}, {'name': 'env_start', 'type': 'ffi::c_ulong'}, {'name': 'env_end', 'type': 'ffi::c_ulong'}, {'name': 'saved_auxv', 'type': '[ffi::c_ulong; 52usize]'}, {'name': 'rss_stat', 'type': '[percpu_counter; 4usize]'}, {'name': 'binfmt', 'type': '*mut linux_binfmt'}, {'name': 'context', 'type': 'mm_context_t'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'ioctx_lock', 'type': 'spinlock_t'}, {'name': 'ioctx_table', 'type': '*mut kioctx_table'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'exe_file', 'type': '*mut file'}, {'name': 'notifier_subscriptions', 'type': '*mut mmu_notifier_subscriptions'}, {'name': 'tlb_flush_pending', 'type': 'atomic_t'}, {'name': 'tlb_flush_batched', 'type': 'atomic_t'}, {'name': 'uprobes_state', 'type': 'uprobes_state'}, {'name': 'hugetlb_usage', 'type': 'atomic_long_t'}, {'name': 'async_put_work', 'type': 'work_struct'}, {'name': 'iommu_mm', 'type': '*mut iommu_mm_data'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'mm_struct__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mm_mt', 'type': 'maple_tree'}, {'name': 'mmap_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'task_size', 'type': 'ffi::c_ulong'}, {'name': 'pgd', 'type': '*mut pgd_t'}, {'name': 'membarrier_state', 'type': 'atomic_t'}, {'name': 'mm_users', 'type': 'atomic_t'}, {'name': 'pcpu_cid', 'type': '*mut mm_cid'}, {'name': 'mm_cid_next_scan', 'type': 'ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_uint'}, {'name': 'max_nr_cid', 'type': 'atomic_t'}, {'name': 'cpus_allowed_lock', 'type': 'raw_spinlock_t'}, {'name': 'pgtables_bytes', 'type': 'atomic_long_t'}, {'name': 'map_count', 'type': 'ffi::c_int'}, {'name': 'page_table_lock', 'type': 'spinlock_t'}, {'name': 'mmap_lock', 'type': 'rw_semaphore'}, {'name': 'mmlist', 'type': 'list_head'}, {'name': 'mm_lock_seq', 'type': 'seqcount_t'}, {'name': 'hiwater_rss', 'type': 'ffi::c_ulong'}, {'name': 'hiwater_vm', 'type': 'ffi::c_ulong'}, {'name': 'total_vm', 'type': 'ffi::c_ulong'}, {'name': 'locked_vm', 'type': 'ffi::c_ulong'}, {'name': 'pinned_vm', 'type': 'atomic64_t'}, {'name': 'data_vm', 'type': 'ffi::c_ulong'}, {'name': 'exec_vm', 'type': 'ffi::c_ulong'}, {'name': 'stack_vm', 'type': 'ffi::c_ulong'}, {'name': 'def_flags', 'type': 'ffi::c_ulong'}, {'name': 'write_protect_seq', 'type': 'seqcount_t'}, {'name': 'arg_lock', 'type': 'spinlock_t'}, {'name': 'start_code', 'type': 'ffi::c_ulong'}, {'name': 'end_code', 'type': 'ffi::c_ulong'}, {'name': 'start_data', 'type': 'ffi::c_ulong'}, {'name': 'end_data', 'type': 'ffi::c_ulong'}, {'name': 'start_brk', 'type': 'ffi::c_ulong'}, {'name': 'brk', 'type': 'ffi::c_ulong'}, {'name': 'start_stack', 'type': 'ffi::c_ulong'}, {'name': 'arg_start', 'type': 'ffi::c_ulong'}, {'name': 'arg_end', 'type': 'ffi::c_ulong'}, {'name': 'env_start', 'type': 'ffi::c_ulong'}, {'name': 'env_end', 'type': 'ffi::c_ulong'}, {'name': 'saved_auxv', 'type': '[ffi::c_ulong; 52usize]'}, {'name': 'rss_stat', 'type': '[percpu_counter; 4usize]'}, {'name': 'binfmt', 'type': '*mut linux_binfmt'}, {'name': 'context', 'type': 'mm_context_t'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'ioctx_lock', 'type': 'spinlock_t'}, {'name': 'ioctx_table', 'type': '*mut kioctx_table'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'exe_file', 'type': '*mut file'}, {'name': 'notifier_subscriptions', 'type': '*mut mmu_notifier_subscriptions'}, {'name': 'tlb_flush_pending', 'type': 'atomic_t'}, {'name': 'tlb_flush_batched', 'type': 'atomic_t'}, {'name': 'uprobes_state', 'type': 'uprobes_state'}, {'name': 'hugetlb_usage', 'type': 'atomic_long_t'}, {'name': 'async_put_work', 'type': 'work_struct'}, {'name': 'iommu_mm', 'type': '*mut iommu_mm_data'}]`

### Rust Evidence

- Graph edges: `2`

## W-000687 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: skb_shared_info
- Explanation: skb_shared_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'flags', 'type': '__u8'}, {'name': 'meta_len', 'type': '__u8'}, {'name': 'nr_frags', 'type': '__u8'}, {'name': 'tx_flags', 'type': '__u8'}, {'name': 'gso_size', 'type': 'ffi::c_ushort'}, {'name': 'gso_segs', 'type': 'ffi::c_ushort'}, {'name': 'frag_list', 'type': '*mut sk_buff'}, {'name': '__bindgen_anon_1', 'type': 'skb_shared_info__bindgen_ty_1'}, {'name': 'gso_type', 'type': 'ffi::c_uint'}, {'name': 'tskey', 'type': 'u32_'}, {'name': 'dataref', 'type': 'atomic_t'}, {'name': 'xdp_frags_size', 'type': 'ffi::c_uint'}, {'name': 'destructor_arg', 'type': '*mut ffi::c_void'}, {'name': 'frags', 'type': '[skb_frag_t; 17usize]'}]`
- New: `[{'name': 'flags', 'type': '__u8'}, {'name': 'meta_len', 'type': '__u8'}, {'name': 'nr_frags', 'type': '__u8'}, {'name': 'tx_flags', 'type': '__u8'}, {'name': 'gso_size', 'type': 'ffi::c_ushort'}, {'name': 'gso_segs', 'type': 'ffi::c_ushort'}, {'name': 'frag_list', 'type': '*mut sk_buff'}, {'name': '__bindgen_anon_1', 'type': 'skb_shared_info__bindgen_ty_1'}, {'name': 'gso_type', 'type': 'ffi::c_uint'}, {'name': 'tskey', 'type': 'u32_'}, {'name': 'dataref', 'type': 'atomic_t'}, {'name': '__bindgen_anon_2', 'type': 'skb_shared_info__bindgen_ty_2'}, {'name': 'frags', 'type': '[skb_frag_t; 17usize]'}]`

### Rust Evidence

- Graph edges: `2`

## W-000654 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bpf_attr__bindgen_ty_4
- Explanation: bpf_attr__bindgen_ty_4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'prog_type', 'type': '__u32'}, {'name': 'insn_cnt', 'type': '__u32'}, {'name': 'insns', 'type': '__u64'}, {'name': 'license', 'type': '__u64'}, {'name': 'log_level', 'type': '__u32'}, {'name': 'log_size', 'type': '__u32'}, {'name': 'log_buf', 'type': '__u64'}, {'name': 'kern_version', 'type': '__u32'}, {'name': 'prog_flags', 'type': '__u32'}, {'name': 'prog_name', 'type': '[ffi::c_char; 16usize]'}, {'name': 'prog_ifindex', 'type': '__u32'}, {'name': 'expected_attach_type', 'type': '__u32'}, {'name': 'prog_btf_fd', 'type': '__u32'}, {'name': 'func_info_rec_size', 'type': '__u32'}, {'name': 'func_info', 'type': '__u64'}, {'name': 'func_info_cnt', 'type': '__u32'}, {'name': 'line_info_rec_size', 'type': '__u32'}, {'name': 'line_info', 'type': '__u64'}, {'name': 'line_info_cnt', 'type': '__u32'}, {'name': 'attach_btf_id', 'type': '__u32'}, {'name': '__bindgen_anon_1', 'type': 'bpf_attr__bindgen_ty_4__bindgen_ty_1'}, {'name': 'core_relo_cnt', 'type': '__u32'}, {'name': 'fd_array', 'type': '__u64'}, {'name': 'core_relos', 'type': '__u64'}, {'name': 'core_relo_rec_size', 'type': '__u32'}, {'name': 'log_true_size', 'type': '__u32'}, {'name': 'prog_token_fd', 'type': '__s32'}]`
- New: `[{'name': 'prog_type', 'type': '__u32'}, {'name': 'insn_cnt', 'type': '__u32'}, {'name': 'insns', 'type': '__u64'}, {'name': 'license', 'type': '__u64'}, {'name': 'log_level', 'type': '__u32'}, {'name': 'log_size', 'type': '__u32'}, {'name': 'log_buf', 'type': '__u64'}, {'name': 'kern_version', 'type': '__u32'}, {'name': 'prog_flags', 'type': '__u32'}, {'name': 'prog_name', 'type': '[ffi::c_char; 16usize]'}, {'name': 'prog_ifindex', 'type': '__u32'}, {'name': 'expected_attach_type', 'type': '__u32'}, {'name': 'prog_btf_fd', 'type': '__u32'}, {'name': 'func_info_rec_size', 'type': '__u32'}, {'name': 'func_info', 'type': '__u64'}, {'name': 'func_info_cnt', 'type': '__u32'}, {'name': 'line_info_rec_size', 'type': '__u32'}, {'name': 'line_info', 'type': '__u64'}, {'name': 'line_info_cnt', 'type': '__u32'}, {'name': 'attach_btf_id', 'type': '__u32'}, {'name': '__bindgen_anon_1', 'type': 'bpf_attr__bindgen_ty_4__bindgen_ty_1'}, {'name': 'core_relo_cnt', 'type': '__u32'}, {'name': 'fd_array', 'type': '__u64'}, {'name': 'core_relos', 'type': '__u64'}, {'name': 'core_relo_rec_size', 'type': '__u32'}, {'name': 'log_true_size', 'type': '__u32'}, {'name': 'prog_token_fd', 'type': '__s32'}, {'name': 'fd_array_cnt', 'type': '__u32'}]`

### Rust Evidence

- Graph edges: `1`

## W-000655 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bus_type
- Explanation: bus_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'dev_name', 'type': '*const ffi::c_char'}, {'name': 'bus_groups', 'type': '*mut *const attribute_group'}, {'name': 'dev_groups', 'type': '*mut *const attribute_group'}, {'name': 'drv_groups', 'type': '*mut *const attribute_group'}, {'name': 'match_', 'type': '::core::option::Option<'}, {'name': 'uevent', 'type': '::core::option::Option<'}, {'name': 'probe', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'sync_state', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'remove', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'shutdown', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'online', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'offline', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'suspend', 'type': '::core::option::Option<'}, {'name': 'resume', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'num_vf', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'dma_configure', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'dma_cleanup', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'pm', 'type': '*const dev_pm_ops'}, {'name': 'need_parent_lock', 'type': 'bool_'}]`
- New: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'dev_name', 'type': '*const ffi::c_char'}, {'name': 'bus_groups', 'type': '*mut *const attribute_group'}, {'name': 'dev_groups', 'type': '*mut *const attribute_group'}, {'name': 'drv_groups', 'type': '*mut *const attribute_group'}, {'name': 'match_', 'type': '::core::option::Option<'}, {'name': 'uevent', 'type': '::core::option::Option<'}, {'name': 'probe', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'sync_state', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'remove', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'shutdown', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'irq_get_affinity', 'type': '::core::option::Option<'}, {'name': 'online', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'offline', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'suspend', 'type': '::core::option::Option<'}, {'name': 'resume', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'num_vf', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'dma_configure', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'dma_cleanup', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'pm', 'type': '*const dev_pm_ops'}, {'name': 'need_parent_lock', 'type': 'bool_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000659 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: dentry_operations
- Explanation: dentry_operations changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'd_revalidate', 'type': '::core::option::Option<'}, {'name': 'd_weak_revalidate', 'type': '::core::option::Option<'}, {'name': 'd_hash', 'type': '::core::option::Option<'}, {'name': 'd_compare', 'type': '::core::option::Option<'}, {'name': 'd_delete', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *const dentry) -> ffi::c_int>'}, {'name': 'd_init', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut dentry) -> ffi::c_int>'}, {'name': 'd_release', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut dentry)>'}, {'name': 'd_prune', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut dentry)>'}, {'name': 'd_iput', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut dentry'}, {'name': 'd_dname', 'type': '::core::option::Option<'}, {'name': 'd_automount', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut path) -> *mut vfsmount>'}, {'name': 'd_real', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'd_revalidate', 'type': '::core::option::Option<'}, {'name': 'd_weak_revalidate', 'type': '::core::option::Option<'}, {'name': 'd_hash', 'type': '::core::option::Option<'}, {'name': 'd_compare', 'type': '::core::option::Option<'}, {'name': 'd_delete', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *const dentry) -> ffi::c_int>'}, {'name': 'd_init', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut dentry) -> ffi::c_int>'}, {'name': 'd_release', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut dentry)>'}, {'name': 'd_prune', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut dentry)>'}, {'name': 'd_iput', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut dentry'}, {'name': 'd_dname', 'type': '::core::option::Option<'}, {'name': 'd_automount', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut path) -> *mut vfsmount>'}, {'name': 'd_real', 'type': '::core::option::Option<'}, {'name': 'd_unalias_unlock', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *const dentry)>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000660 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: ethtool_ops
- Explanation: ethtool_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rxfh_indir_space', 'type': 'u32_'}, {'name': 'rxfh_key_space', 'type': 'u16_'}, {'name': 'rxfh_priv_size', 'type': 'u16_'}, {'name': 'rxfh_max_num_contexts', 'type': 'u32_'}, {'name': 'supported_coalesce_params', 'type': 'u32_'}, {'name': 'supported_ring_params', 'type': 'u32_'}, {'name': 'get_drvinfo', 'type': '::core::option::Option<'}, {'name': 'get_regs', 'type': '::core::option::Option<'}, {'name': 'get_wol', 'type': '::core::option::Option<'}, {'name': 'set_wol', 'type': '::core::option::Option<'}, {'name': 'get_msglevel', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'get_link', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'get_link_ext_state', 'type': '::core::option::Option<'}, {'name': 'get_link_ext_stats', 'type': '::core::option::Option<'}, {'name': 'get_eeprom', 'type': '::core::option::Option<'}, {'name': 'set_eeprom', 'type': '::core::option::Option<'}, {'name': 'get_coalesce', 'type': '::core::option::Option<'}, {'name': 'set_coalesce', 'type': '::core::option::Option<'}, {'name': 'get_ringparam', 'type': '::core::option::Option<'}, {'name': 'set_ringparam', 'type': '::core::option::Option<'}, {'name': 'get_pause_stats', 'type': '::core::option::Option<'}, {'name': 'get_pauseparam', 'type': '::core::option::Option<'}, {'name': 'set_pauseparam', 'type': '::core::option::Option<'}, {'name': 'self_test', 'type': '::core::option::Option<'}, {'name': 'get_strings', 'type': '::core::option::Option<'}, {'name': 'set_phys_id', 'type': '::core::option::Option<'}, {'name': 'get_ethtool_stats', 'type': '::core::option::Option<'}, {'name': 'begin', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> ffi::c_int>'}, {'name': 'complete', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device)>'}, {'name': 'get_priv_flags', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'set_priv_flags', 'type': '::core::option::Option<'}, {'name': 'get_sset_count', 'type': '::core::option::Option<'}, {'name': 'get_rxnfc', 'type': '::core::option::Option<'}, {'name': 'set_rxnfc', 'type': '::core::option::Option<'}, {'name': 'flash_device', 'type': '::core::option::Option<'}, {'name': 'reset', 'type': '::core::option::Option<'}, {'name': 'get_rxfh', 'type': '::core::option::Option<'}, {'name': 'set_rxfh', 'type': '::core::option::Option<'}, {'name': 'create_rxfh_context', 'type': '::core::option::Option<'}, {'name': 'modify_rxfh_context', 'type': '::core::option::Option<'}, {'name': 'remove_rxfh_context', 'type': '::core::option::Option<'}, {'name': 'get_channels', 'type': '::core::option::Option<'}, {'name': 'set_channels', 'type': '::core::option::Option<'}, {'name': 'get_dump_flag', 'type': '::core::option::Option<'}, {'name': 'get_dump_data', 'type': '::core::option::Option<'}, {'name': 'set_dump', 'type': '::core::option::Option<'}, {'name': 'get_ts_info', 'type': '::core::option::Option<'}, {'name': 'get_ts_stats', 'type': '::core::option::Option<'}, {'name': 'get_module_info', 'type': '::core::option::Option<'}, {'name': 'get_module_eeprom', 'type': '::core::option::Option<'}, {'name': 'get_eee', 'type': '::core::option::Option<'}, {'name': 'set_eee', 'type': '::core::option::Option<'}, {'name': 'get_tunable', 'type': '::core::option::Option<'}, {'name': 'set_tunable', 'type': '::core::option::Option<'}, {'name': 'get_per_queue_coalesce', 'type': '::core::option::Option<'}, {'name': 'set_per_queue_coalesce', 'type': '::core::option::Option<'}, {'name': 'get_link_ksettings', 'type': '::core::option::Option<'}, {'name': 'set_link_ksettings', 'type': '::core::option::Option<'}, {'name': 'get_fec_stats', 'type': '::core::option::Option<'}, {'name': 'get_fecparam', 'type': '::core::option::Option<'}, {'name': 'set_fecparam', 'type': '::core::option::Option<'}, {'name': 'get_ethtool_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_phy_tunable', 'type': '::core::option::Option<'}, {'name': 'set_phy_tunable', 'type': '::core::option::Option<'}, {'name': 'get_module_eeprom_by_page', 'type': '::core::option::Option<'}, {'name': 'set_module_eeprom_by_page', 'type': '::core::option::Option<'}, {'name': 'get_eth_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_eth_mac_stats', 'type': '::core::option::Option<'}, {'name': 'get_eth_ctrl_stats', 'type': '::core::option::Option<'}, {'name': 'get_rmon_stats', 'type': '::core::option::Option<'}, {'name': 'get_module_power_mode', 'type': '::core::option::Option<'}, {'name': 'set_module_power_mode', 'type': '::core::option::Option<'}, {'name': 'get_mm', 'type': '::core::option::Option<'}, {'name': 'set_mm', 'type': '::core::option::Option<'}, {'name': 'get_mm_stats', 'type': '::core::option::Option<'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rxfh_indir_space', 'type': 'u32_'}, {'name': 'rxfh_key_space', 'type': 'u16_'}, {'name': 'rxfh_priv_size', 'type': 'u16_'}, {'name': 'rxfh_max_num_contexts', 'type': 'u32_'}, {'name': 'supported_coalesce_params', 'type': 'u32_'}, {'name': 'supported_ring_params', 'type': 'u32_'}, {'name': 'supported_hwtstamp_qualifiers', 'type': 'u32_'}, {'name': 'get_drvinfo', 'type': '::core::option::Option<'}, {'name': 'get_regs', 'type': '::core::option::Option<'}, {'name': 'get_wol', 'type': '::core::option::Option<'}, {'name': 'set_wol', 'type': '::core::option::Option<'}, {'name': 'get_msglevel', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'get_link', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'get_link_ext_state', 'type': '::core::option::Option<'}, {'name': 'get_link_ext_stats', 'type': '::core::option::Option<'}, {'name': 'get_eeprom', 'type': '::core::option::Option<'}, {'name': 'set_eeprom', 'type': '::core::option::Option<'}, {'name': 'get_coalesce', 'type': '::core::option::Option<'}, {'name': 'set_coalesce', 'type': '::core::option::Option<'}, {'name': 'get_ringparam', 'type': '::core::option::Option<'}, {'name': 'set_ringparam', 'type': '::core::option::Option<'}, {'name': 'get_pause_stats', 'type': '::core::option::Option<'}, {'name': 'get_pauseparam', 'type': '::core::option::Option<'}, {'name': 'set_pauseparam', 'type': '::core::option::Option<'}, {'name': 'self_test', 'type': '::core::option::Option<'}, {'name': 'get_strings', 'type': '::core::option::Option<'}, {'name': 'set_phys_id', 'type': '::core::option::Option<'}, {'name': 'get_ethtool_stats', 'type': '::core::option::Option<'}, {'name': 'begin', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> ffi::c_int>'}, {'name': 'complete', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device)>'}, {'name': 'get_priv_flags', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'set_priv_flags', 'type': '::core::option::Option<'}, {'name': 'get_sset_count', 'type': '::core::option::Option<'}, {'name': 'get_rxnfc', 'type': '::core::option::Option<'}, {'name': 'set_rxnfc', 'type': '::core::option::Option<'}, {'name': 'flash_device', 'type': '::core::option::Option<'}, {'name': 'reset', 'type': '::core::option::Option<'}, {'name': 'get_rxfh', 'type': '::core::option::Option<'}, {'name': 'set_rxfh', 'type': '::core::option::Option<'}, {'name': 'create_rxfh_context', 'type': '::core::option::Option<'}, {'name': 'modify_rxfh_context', 'type': '::core::option::Option<'}, {'name': 'remove_rxfh_context', 'type': '::core::option::Option<'}, {'name': 'get_channels', 'type': '::core::option::Option<'}, {'name': 'set_channels', 'type': '::core::option::Option<'}, {'name': 'get_dump_flag', 'type': '::core::option::Option<'}, {'name': 'get_dump_data', 'type': '::core::option::Option<'}, {'name': 'set_dump', 'type': '::core::option::Option<'}, {'name': 'get_ts_info', 'type': '::core::option::Option<'}, {'name': 'get_ts_stats', 'type': '::core::option::Option<'}, {'name': 'get_module_info', 'type': '::core::option::Option<'}, {'name': 'get_module_eeprom', 'type': '::core::option::Option<'}, {'name': 'get_eee', 'type': '::core::option::Option<'}, {'name': 'set_eee', 'type': '::core::option::Option<'}, {'name': 'get_tunable', 'type': '::core::option::Option<'}, {'name': 'set_tunable', 'type': '::core::option::Option<'}, {'name': 'get_per_queue_coalesce', 'type': '::core::option::Option<'}, {'name': 'set_per_queue_coalesce', 'type': '::core::option::Option<'}, {'name': 'get_link_ksettings', 'type': '::core::option::Option<'}, {'name': 'set_link_ksettings', 'type': '::core::option::Option<'}, {'name': 'get_fec_stats', 'type': '::core::option::Option<'}, {'name': 'get_fecparam', 'type': '::core::option::Option<'}, {'name': 'set_fecparam', 'type': '::core::option::Option<'}, {'name': 'get_ethtool_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_phy_tunable', 'type': '::core::option::Option<'}, {'name': 'set_phy_tunable', 'type': '::core::option::Option<'}, {'name': 'get_module_eeprom_by_page', 'type': '::core::option::Option<'}, {'name': 'set_module_eeprom_by_page', 'type': '::core::option::Option<'}, {'name': 'get_eth_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_eth_mac_stats', 'type': '::core::option::Option<'}, {'name': 'get_eth_ctrl_stats', 'type': '::core::option::Option<'}, {'name': 'get_rmon_stats', 'type': '::core::option::Option<'}, {'name': 'get_module_power_mode', 'type': '::core::option::Option<'}, {'name': 'set_module_power_mode', 'type': '::core::option::Option<'}, {'name': 'get_mm', 'type': '::core::option::Option<'}, {'name': 'set_mm', 'type': '::core::option::Option<'}, {'name': 'get_mm_stats', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-000661 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: ethtool_ts_stats__bindgen_ty_1__bindgen_ty_1
- Explanation: ethtool_ts_stats__bindgen_ty_1__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'pkts', 'type': 'u64_'}, {'name': 'lost', 'type': 'u64_'}, {'name': 'err', 'type': 'u64_'}]`
- New: `[{'name': 'pkts', 'type': 'u64_'}, {'name': 'onestep_pkts_unconfirmed', 'type': 'u64_'}, {'name': 'lost', 'type': 'u64_'}, {'name': 'err', 'type': 'u64_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000662 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: ethtool_ts_stats__bindgen_ty_1__bindgen_ty_2
- Explanation: ethtool_ts_stats__bindgen_ty_1__bindgen_ty_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'pkts', 'type': 'u64_'}, {'name': 'lost', 'type': 'u64_'}, {'name': 'err', 'type': 'u64_'}]`
- New: `[{'name': 'pkts', 'type': 'u64_'}, {'name': 'onestep_pkts_unconfirmed', 'type': 'u64_'}, {'name': 'lost', 'type': 'u64_'}, {'name': 'err', 'type': 'u64_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000663 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: fwnode_operations
- Explanation: fwnode_operations changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'get', 'type': '::core::option::Option<'}, {'name': 'put', 'type': '::core::option::Option<unsafe extern "C" fn(fwnode: *mut fwnode_handle)>'}, {'name': 'device_get_match_data', 'type': '::core::option::Option<'}, {'name': 'property_present', 'type': '::core::option::Option<'}, {'name': 'property_read_int_array', 'type': '::core::option::Option<'}, {'name': 'property_read_string_array', 'type': '::core::option::Option<'}, {'name': 'get_name', 'type': '::core::option::Option<'}, {'name': 'get_name_prefix', 'type': '::core::option::Option<'}, {'name': 'get_parent', 'type': '::core::option::Option<'}, {'name': 'get_next_child_node', 'type': '::core::option::Option<'}, {'name': 'get_named_child_node', 'type': '::core::option::Option<'}, {'name': 'get_reference_args', 'type': '::core::option::Option<'}, {'name': 'graph_get_next_endpoint', 'type': '::core::option::Option<'}, {'name': 'graph_get_remote_endpoint', 'type': '::core::option::Option<'}, {'name': 'graph_get_port_parent', 'type': '::core::option::Option<'}, {'name': 'graph_parse_endpoint', 'type': '::core::option::Option<'}, {'name': 'iomap', 'type': '::core::option::Option<'}, {'name': 'irq_get', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'get', 'type': '::core::option::Option<'}, {'name': 'put', 'type': '::core::option::Option<unsafe extern "C" fn(fwnode: *mut fwnode_handle)>'}, {'name': 'device_get_match_data', 'type': '::core::option::Option<'}, {'name': 'property_present', 'type': '::core::option::Option<'}, {'name': 'property_read_bool', 'type': '::core::option::Option<'}, {'name': 'property_read_int_array', 'type': '::core::option::Option<'}, {'name': 'property_read_string_array', 'type': '::core::option::Option<'}, {'name': 'get_name', 'type': '::core::option::Option<'}, {'name': 'get_name_prefix', 'type': '::core::option::Option<'}, {'name': 'get_parent', 'type': '::core::option::Option<'}, {'name': 'get_next_child_node', 'type': '::core::option::Option<'}, {'name': 'get_named_child_node', 'type': '::core::option::Option<'}, {'name': 'get_reference_args', 'type': '::core::option::Option<'}, {'name': 'graph_get_next_endpoint', 'type': '::core::option::Option<'}, {'name': 'graph_get_remote_endpoint', 'type': '::core::option::Option<'}, {'name': 'graph_get_port_parent', 'type': '::core::option::Option<'}, {'name': 'graph_parse_endpoint', 'type': '::core::option::Option<'}, {'name': 'iomap', 'type': '::core::option::Option<'}, {'name': 'irq_get', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-000664 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: hrtimer_cpu_base
- Explanation: hrtimer_cpu_base changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'lock', 'type': 'raw_spinlock_t'}, {'name': 'cpu', 'type': 'ffi::c_uint'}, {'name': 'active_bases', 'type': 'ffi::c_uint'}, {'name': 'clock_was_set_seq', 'type': 'ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'nr_events', 'type': 'ffi::c_uint'}, {'name': 'nr_retries', 'type': 'ffi::c_ushort'}, {'name': 'nr_hangs', 'type': 'ffi::c_ushort'}, {'name': 'max_hang_time', 'type': 'ffi::c_uint'}, {'name': 'expires_next', 'type': 'ktime_t'}, {'name': 'next_timer', 'type': '*mut hrtimer'}, {'name': 'softirq_expires_next', 'type': 'ktime_t'}, {'name': 'softirq_next_timer', 'type': '*mut hrtimer'}, {'name': 'clock_base', 'type': '[hrtimer_clock_base; 8usize]'}]`
- New: `[{'name': 'lock', 'type': 'raw_spinlock_t'}, {'name': 'cpu', 'type': 'ffi::c_uint'}, {'name': 'active_bases', 'type': 'ffi::c_uint'}, {'name': 'clock_was_set_seq', 'type': 'ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'nr_events', 'type': 'ffi::c_uint'}, {'name': 'nr_retries', 'type': 'ffi::c_ushort'}, {'name': 'nr_hangs', 'type': 'ffi::c_ushort'}, {'name': 'max_hang_time', 'type': 'ffi::c_uint'}, {'name': 'expires_next', 'type': 'ktime_t'}, {'name': 'next_timer', 'type': '*mut hrtimer'}, {'name': 'softirq_expires_next', 'type': 'ktime_t'}, {'name': 'softirq_next_timer', 'type': '*mut hrtimer'}, {'name': 'clock_base', 'type': '[hrtimer_clock_base; 8usize]'}, {'name': 'csd', 'type': 'call_single_data_t'}]`

### Rust Evidence

- Graph edges: `1`

## W-000666 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: kernel_clone_args
- Explanation: kernel_clone_args changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'flags', 'type': 'u64_'}, {'name': 'pidfd', 'type': '*mut ffi::c_int'}, {'name': 'child_tid', 'type': '*mut ffi::c_int'}, {'name': 'parent_tid', 'type': '*mut ffi::c_int'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'exit_signal', 'type': 'ffi::c_int'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'stack', 'type': 'ffi::c_ulong'}, {'name': 'stack_size', 'type': 'ffi::c_ulong'}, {'name': 'tls', 'type': 'ffi::c_ulong'}, {'name': 'set_tid', 'type': '*mut pid_t'}, {'name': 'set_tid_size', 'type': 'usize'}, {'name': 'cgroup', 'type': 'ffi::c_int'}, {'name': 'idle', 'type': 'ffi::c_int'}, {'name': 'fn_', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut ffi::c_void) -> ffi::c_int>'}, {'name': 'fn_arg', 'type': '*mut ffi::c_void'}, {'name': 'cgrp', 'type': '*mut cgroup'}, {'name': 'cset', 'type': '*mut css_set'}]`
- New: `[{'name': 'flags', 'type': 'u64_'}, {'name': 'pidfd', 'type': '*mut ffi::c_int'}, {'name': 'child_tid', 'type': '*mut ffi::c_int'}, {'name': 'parent_tid', 'type': '*mut ffi::c_int'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'exit_signal', 'type': 'ffi::c_int'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'stack', 'type': 'ffi::c_ulong'}, {'name': 'stack_size', 'type': 'ffi::c_ulong'}, {'name': 'tls', 'type': 'ffi::c_ulong'}, {'name': 'set_tid', 'type': '*mut pid_t'}, {'name': 'set_tid_size', 'type': 'usize'}, {'name': 'cgroup', 'type': 'ffi::c_int'}, {'name': 'idle', 'type': 'ffi::c_int'}, {'name': 'fn_', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut ffi::c_void) -> ffi::c_int>'}, {'name': 'fn_arg', 'type': '*mut ffi::c_void'}, {'name': 'cgrp', 'type': '*mut cgroup'}, {'name': 'cset', 'type': '*mut css_set'}, {'name': 'kill_seq', 'type': 'ffi::c_uint'}]`

### Rust Evidence

- Graph edges: `1`

## W-000667 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: kernel_ethtool_ringparam
- Explanation: kernel_ethtool_ringparam changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'rx_buf_len', 'type': 'u32_'}, {'name': 'tcp_data_split', 'type': 'u8_'}, {'name': 'tx_push', 'type': 'u8_'}, {'name': 'rx_push', 'type': 'u8_'}, {'name': 'cqe_size', 'type': 'u32_'}, {'name': 'tx_push_buf_len', 'type': 'u32_'}, {'name': 'tx_push_buf_max_len', 'type': 'u32_'}]`
- New: `[{'name': 'rx_buf_len', 'type': 'u32_'}, {'name': 'tcp_data_split', 'type': 'u8_'}, {'name': 'tx_push', 'type': 'u8_'}, {'name': 'rx_push', 'type': 'u8_'}, {'name': 'cqe_size', 'type': 'u32_'}, {'name': 'tx_push_buf_len', 'type': 'u32_'}, {'name': 'tx_push_buf_max_len', 'type': 'u32_'}, {'name': 'hds_thresh', 'type': 'u32_'}, {'name': 'hds_thresh_max', 'type': 'u32_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000668 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: kernel_ethtool_ts_info
- Explanation: kernel_ethtool_ts_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'cmd', 'type': 'u32_'}, {'name': 'so_timestamping', 'type': 'u32_'}, {'name': 'phc_index', 'type': 'ffi::c_int'}, {'name': 'tx_types', 'type': 'hwtstamp_tx_types'}, {'name': 'rx_filters', 'type': 'hwtstamp_rx_filters'}]`
- New: `[{'name': 'cmd', 'type': 'u32_'}, {'name': 'so_timestamping', 'type': 'u32_'}, {'name': 'phc_index', 'type': 'ffi::c_int'}, {'name': 'phc_qualifier', 'type': 'hwtstamp_provider_qualifier'}, {'name': 'tx_types', 'type': 'hwtstamp_tx_types'}, {'name': 'rx_filters', 'type': 'hwtstamp_rx_filters'}]`

### Rust Evidence

- Graph edges: `1`

## W-000669 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: kernel_hwtstamp_config
- Explanation: kernel_hwtstamp_config changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'flags', 'type': 'ffi::c_int'}, {'name': 'tx_type', 'type': 'ffi::c_int'}, {'name': 'rx_filter', 'type': 'ffi::c_int'}, {'name': 'ifr', 'type': '*mut ifreq'}, {'name': 'copied_to_user', 'type': 'bool_'}, {'name': 'source', 'type': 'hwtstamp_source'}]`
- New: `[{'name': 'flags', 'type': 'ffi::c_int'}, {'name': 'tx_type', 'type': 'ffi::c_int'}, {'name': 'rx_filter', 'type': 'ffi::c_int'}, {'name': 'ifr', 'type': '*mut ifreq'}, {'name': 'copied_to_user', 'type': 'bool_'}, {'name': 'source', 'type': 'hwtstamp_source'}, {'name': 'qualifier', 'type': 'hwtstamp_provider_qualifier'}]`

### Rust Evidence

- Graph edges: `1`

## W-000671 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: mm_context_t
- Explanation: mm_context_t changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'ctx_id', 'type': 'u64_'}, {'name': 'tlb_gen', 'type': 'atomic64_t'}, {'name': 'ldt_usr_sem', 'type': 'rw_semaphore'}, {'name': 'ldt', 'type': '*mut ldt_struct'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'lock', 'type': 'mutex'}, {'name': 'vdso', 'type': '*mut ffi::c_void'}, {'name': 'vdso_image', 'type': '*const vdso_image'}, {'name': 'perf_rdpmc_allowed', 'type': 'atomic_t'}, {'name': 'pkey_allocation_map', 'type': 'u16_'}, {'name': 'execute_only_pkey', 'type': 's16'}]`
- New: `[{'name': 'ctx_id', 'type': 'u64_'}, {'name': 'tlb_gen', 'type': 'atomic64_t'}, {'name': 'next_trim_cpumask', 'type': 'ffi::c_ulong'}, {'name': 'ldt_usr_sem', 'type': 'rw_semaphore'}, {'name': 'ldt', 'type': '*mut ldt_struct'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'lock', 'type': 'mutex'}, {'name': 'vdso', 'type': '*mut ffi::c_void'}, {'name': 'vdso_image', 'type': '*const vdso_image'}, {'name': 'perf_rdpmc_allowed', 'type': 'atomic_t'}, {'name': 'pkey_allocation_map', 'type': 'u16_'}, {'name': 'execute_only_pkey', 'type': 's16'}]`

### Rust Evidence

- Graph edges: `1`

## W-000674 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: name_snapshot
- Explanation: name_snapshot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'name', 'type': 'qstr'}, {'name': 'inline_name', 'type': '[ffi::c_uchar; 40usize]'}]`
- New: `[{'name': 'name', 'type': 'qstr'}, {'name': 'inline_name', 'type': 'shortname_store'}]`

### Rust Evidence

- Graph edges: `1`

## W-000682 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: request_queue
- Explanation: request_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'queuedata', 'type': '*mut ffi::c_void'}, {'name': 'elevator', 'type': '*mut elevator_queue'}, {'name': 'mq_ops', 'type': '*const blk_mq_ops'}, {'name': 'queue_ctx', 'type': '*mut blk_mq_ctx'}, {'name': 'queue_flags', 'type': 'ffi::c_ulong'}, {'name': 'rq_timeout', 'type': 'ffi::c_uint'}, {'name': 'queue_depth', 'type': 'ffi::c_uint'}, {'name': 'refs', 'type': 'refcount_t'}, {'name': 'nr_hw_queues', 'type': 'ffi::c_uint'}, {'name': 'hctx_table', 'type': 'xarray'}, {'name': 'q_usage_counter', 'type': 'percpu_ref'}, {'name': 'io_lock_cls_key', 'type': 'lock_class_key'}, {'name': 'io_lockdep_map', 'type': 'lockdep_map'}, {'name': 'q_lock_cls_key', 'type': 'lock_class_key'}, {'name': 'q_lockdep_map', 'type': 'lockdep_map'}, {'name': 'last_merge', 'type': '*mut request'}, {'name': 'queue_lock', 'type': 'spinlock_t'}, {'name': 'quiesce_depth', 'type': 'ffi::c_int'}, {'name': 'disk', 'type': '*mut gendisk'}, {'name': 'mq_kobj', 'type': '*mut kobject'}, {'name': 'limits', 'type': 'queue_limits'}, {'name': 'dev', 'type': '*mut device'}, {'name': 'rpm_status', 'type': 'rpm_status'}, {'name': 'pm_only', 'type': 'atomic_t'}, {'name': 'stats', 'type': '*mut blk_queue_stats'}, {'name': 'rq_qos', 'type': '*mut rq_qos'}, {'name': 'rq_qos_mutex', 'type': 'mutex'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'nr_requests', 'type': 'ffi::c_ulong'}, {'name': 'timeout', 'type': 'timer_list'}, {'name': 'timeout_work', 'type': 'work_struct'}, {'name': 'nr_active_requests_shared_tags', 'type': 'atomic_t'}, {'name': 'sched_shared_tags', 'type': '*mut blk_mq_tags'}, {'name': 'icq_list', 'type': 'list_head'}, {'name': 'blkcg_pols', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'root_blkg', 'type': '*mut blkcg_gq'}, {'name': 'blkg_list', 'type': 'list_head'}, {'name': 'blkcg_mutex', 'type': 'mutex'}, {'name': 'node', 'type': 'ffi::c_int'}, {'name': 'requeue_lock', 'type': 'spinlock_t'}, {'name': 'requeue_list', 'type': 'list_head'}, {'name': 'requeue_work', 'type': 'delayed_work'}, {'name': 'blk_trace', 'type': '*mut blk_trace'}, {'name': 'fq', 'type': '*mut blk_flush_queue'}, {'name': 'flush_list', 'type': 'list_head'}, {'name': 'sysfs_lock', 'type': 'mutex'}, {'name': 'sysfs_dir_lock', 'type': 'mutex'}, {'name': 'limits_lock', 'type': 'mutex'}, {'name': 'unused_hctx_list', 'type': 'list_head'}, {'name': 'unused_hctx_lock', 'type': 'spinlock_t'}, {'name': 'mq_freeze_depth', 'type': 'ffi::c_int'}, {'name': 'callback_head', 'type': 'callback_head'}, {'name': 'mq_freeze_wq', 'type': 'wait_queue_head_t'}, {'name': 'mq_freeze_lock', 'type': 'mutex'}, {'name': 'tag_set', 'type': '*mut blk_mq_tag_set'}, {'name': 'tag_set_list', 'type': 'list_head'}, {'name': 'debugfs_dir', 'type': '*mut dentry'}, {'name': 'sched_debugfs_dir', 'type': '*mut dentry'}, {'name': 'rqos_debugfs_dir', 'type': '*mut dentry'}, {'name': 'debugfs_mutex', 'type': 'mutex'}, {'name': 'mq_sysfs_init_done', 'type': 'bool_'}]`
- New: `[{'name': 'queuedata', 'type': '*mut ffi::c_void'}, {'name': 'elevator', 'type': '*mut elevator_queue'}, {'name': 'mq_ops', 'type': '*const blk_mq_ops'}, {'name': 'queue_ctx', 'type': '*mut blk_mq_ctx'}, {'name': 'queue_flags', 'type': 'ffi::c_ulong'}, {'name': 'rq_timeout', 'type': 'ffi::c_uint'}, {'name': 'queue_depth', 'type': 'ffi::c_uint'}, {'name': 'refs', 'type': 'refcount_t'}, {'name': 'nr_hw_queues', 'type': 'ffi::c_uint'}, {'name': 'hctx_table', 'type': 'xarray'}, {'name': 'q_usage_counter', 'type': 'percpu_ref'}, {'name': 'io_lock_cls_key', 'type': 'lock_class_key'}, {'name': 'io_lockdep_map', 'type': 'lockdep_map'}, {'name': 'q_lock_cls_key', 'type': 'lock_class_key'}, {'name': 'q_lockdep_map', 'type': 'lockdep_map'}, {'name': 'last_merge', 'type': '*mut request'}, {'name': 'queue_lock', 'type': 'spinlock_t'}, {'name': 'quiesce_depth', 'type': 'ffi::c_int'}, {'name': 'disk', 'type': '*mut gendisk'}, {'name': 'mq_kobj', 'type': '*mut kobject'}, {'name': 'limits', 'type': 'queue_limits'}, {'name': 'dev', 'type': '*mut device'}, {'name': 'rpm_status', 'type': 'rpm_status'}, {'name': 'pm_only', 'type': 'atomic_t'}, {'name': 'stats', 'type': '*mut blk_queue_stats'}, {'name': 'rq_qos', 'type': '*mut rq_qos'}, {'name': 'rq_qos_mutex', 'type': 'mutex'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'nr_requests', 'type': 'ffi::c_ulong'}, {'name': 'timeout', 'type': 'timer_list'}, {'name': 'timeout_work', 'type': 'work_struct'}, {'name': 'nr_active_requests_shared_tags', 'type': 'atomic_t'}, {'name': 'sched_shared_tags', 'type': '*mut blk_mq_tags'}, {'name': 'icq_list', 'type': 'list_head'}, {'name': 'blkcg_pols', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'root_blkg', 'type': '*mut blkcg_gq'}, {'name': 'blkg_list', 'type': 'list_head'}, {'name': 'blkcg_mutex', 'type': 'mutex'}, {'name': 'node', 'type': 'ffi::c_int'}, {'name': 'requeue_lock', 'type': 'spinlock_t'}, {'name': 'requeue_list', 'type': 'list_head'}, {'name': 'requeue_work', 'type': 'delayed_work'}, {'name': 'blk_trace', 'type': '*mut blk_trace'}, {'name': 'fq', 'type': '*mut blk_flush_queue'}, {'name': 'flush_list', 'type': 'list_head'}, {'name': 'sysfs_lock', 'type': 'mutex'}, {'name': 'limits_lock', 'type': 'mutex'}, {'name': 'unused_hctx_list', 'type': 'list_head'}, {'name': 'unused_hctx_lock', 'type': 'spinlock_t'}, {'name': 'mq_freeze_depth', 'type': 'ffi::c_int'}, {'name': 'callback_head', 'type': 'callback_head'}, {'name': 'mq_freeze_wq', 'type': 'wait_queue_head_t'}, {'name': 'mq_freeze_lock', 'type': 'mutex'}, {'name': 'tag_set', 'type': '*mut blk_mq_tag_set'}, {'name': 'tag_set_list', 'type': 'list_head'}, {'name': 'debugfs_dir', 'type': '*mut dentry'}, {'name': 'sched_debugfs_dir', 'type': '*mut dentry'}, {'name': 'rqos_debugfs_dir', 'type': '*mut dentry'}, {'name': 'debugfs_mutex', 'type': 'mutex'}]`

### Rust Evidence

- Graph edges: `1`

## W-000683 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: return_instance
- Explanation: return_instance changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'hprobe', 'type': 'hprobe'}, {'name': 'func', 'type': 'ffi::c_ulong'}, {'name': 'stack', 'type': 'ffi::c_ulong'}, {'name': 'orig_ret_vaddr', 'type': 'ffi::c_ulong'}, {'name': 'chained', 'type': 'bool_'}, {'name': 'consumers_cnt', 'type': 'ffi::c_int'}, {'name': 'next', 'type': '*mut return_instance'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'consumers', 'type': '__IncompleteArrayField<return_consumer>'}]`
- New: `[{'name': 'hprobe', 'type': 'hprobe'}, {'name': 'func', 'type': 'ffi::c_ulong'}, {'name': 'stack', 'type': 'ffi::c_ulong'}, {'name': 'orig_ret_vaddr', 'type': 'ffi::c_ulong'}, {'name': 'chained', 'type': 'bool_'}, {'name': 'cons_cnt', 'type': 'ffi::c_int'}, {'name': 'next', 'type': '*mut return_instance'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'consumer', 'type': 'return_consumer'}, {'name': 'extra_consumers', 'type': '*mut return_consumer'}]`

### Rust Evidence

- Graph edges: `1`

## W-000685 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: sched_domain_topology_level
- Explanation: sched_domain_topology_level changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mask', 'type': 'sched_domain_mask_f'}, {'name': 'sd_flags', 'type': 'sched_domain_flags_f'}, {'name': 'flags', 'type': 'ffi::c_int'}, {'name': 'numa_level', 'type': 'ffi::c_int'}, {'name': 'data', 'type': 'sd_data'}]`
- New: `[{'name': 'mask', 'type': 'sched_domain_mask_f'}, {'name': 'sd_flags', 'type': 'sched_domain_flags_f'}, {'name': 'flags', 'type': 'ffi::c_int'}, {'name': 'numa_level', 'type': 'ffi::c_int'}, {'name': 'data', 'type': 'sd_data'}, {'name': 'name', 'type': '*mut ffi::c_char'}]`

### Rust Evidence

- Graph edges: `1`

## W-000686 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: sched_info
- Explanation: sched_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'pcount', 'type': 'ffi::c_ulong'}, {'name': 'run_delay', 'type': 'ffi::c_ulonglong'}, {'name': 'last_arrival', 'type': 'ffi::c_ulonglong'}, {'name': 'last_queued', 'type': 'ffi::c_ulonglong'}]`
- New: `[{'name': 'pcount', 'type': 'ffi::c_ulong'}, {'name': 'run_delay', 'type': 'ffi::c_ulonglong'}, {'name': 'max_run_delay', 'type': 'ffi::c_ulonglong'}, {'name': 'min_run_delay', 'type': 'ffi::c_ulonglong'}, {'name': 'last_arrival', 'type': 'ffi::c_ulonglong'}, {'name': 'last_queued', 'type': 'ffi::c_ulonglong'}]`

### Rust Evidence

- Graph edges: `1`

## W-000693 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: zap_details
- Explanation: zap_details changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'single_folio', 'type': '*mut folio'}, {'name': 'even_cows', 'type': 'bool_'}, {'name': 'zap_flags', 'type': 'zap_flags_t'}]`
- New: `[{'name': 'single_folio', 'type': '*mut folio'}, {'name': 'even_cows', 'type': 'bool_'}, {'name': 'reclaim_pt', 'type': 'bool_'}, {'name': 'zap_flags', 'type': 'zap_flags_t'}]`

### Rust Evidence

- Graph edges: `1`

## W-000711 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: mthp_stat_item_MTHP_STAT_SPLIT
- Explanation: mthp_stat_item_MTHP_STAT_SPLIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `12`

### Rust Evidence

- Graph edges: `3`

## W-000700 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: cpuhp_state_CPUHP_AP_ONLINE_DYN
- Explanation: cpuhp_state_CPUHP_AP_ONLINE_DYN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `194`
- New: `195`

### Rust Evidence

- Graph edges: `2`

## W-000706 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: mthp_stat_item_MTHP_STAT_NR_ANON
- Explanation: mthp_stat_item_MTHP_STAT_NR_ANON changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `13`
- New: `15`

### Rust Evidence

- Graph edges: `2`

## W-000709 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: mthp_stat_item_MTHP_STAT_SHMEM_FALLBACK
- Explanation: mthp_stat_item_MTHP_STAT_SHMEM_FALLBACK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `10`

### Rust Evidence

- Graph edges: `2`

## W-000714 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: mthp_stat_item_MTHP_STAT_SWPOUT
- Explanation: mthp_stat_item_MTHP_STAT_SWPOUT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `7`

### Rust Evidence

- Graph edges: `2`

## W-000802 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_RFC7323_PAWS
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_RFC7323_PAWS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `33`
- New: `36`

### Rust Evidence

- Graph edges: `2`

## W-000694 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: NR_PAGEFLAGS
- Explanation: NR_PAGEFLAGS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `21`
- New: `22`

### Rust Evidence

- Graph edges: `1`

## W-000695 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: PAGEFLAGS_MASK
- Explanation: PAGEFLAGS_MASK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `2097151`
- New: `4194303`

### Rust Evidence

- Graph edges: `1`

## W-000696 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TASKSTATS_VERSION
- Explanation: TASKSTATS_VERSION changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `14`
- New: `15`

### Rust Evidence

- Graph edges: `1`

## W-000697 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cc_attr_CC_ATTR_HOST_SEV_SNP
- Explanation: cc_attr_CC_ATTR_HOST_SEV_SNP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `6`
- New: `7`

### Rust Evidence

- Graph edges: `1`

## W-000698 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ACTIVE
- Explanation: cpuhp_state_CPUHP_AP_ACTIVE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `237`
- New: `238`

### Rust Evidence

- Graph edges: `1`

## W-000699 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_BASE_CACHEINFO_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_BASE_CACHEINFO_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `193`
- New: `194`

### Rust Evidence

- Graph edges: `1`

## W-000701 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ONLINE_DYN_END
- Explanation: cpuhp_state_CPUHP_AP_ONLINE_DYN_END changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `234`
- New: `235`

### Rust Evidence

- Graph edges: `1`

## W-000702 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_X86_HPET_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_X86_HPET_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `235`
- New: `236`

### Rust Evidence

- Graph edges: `1`

## W-000703 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_X86_KVM_CLK_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_X86_KVM_CLK_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `236`
- New: `237`

### Rust Evidence

- Graph edges: `1`

## W-000704 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_ONLINE
- Explanation: cpuhp_state_CPUHP_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `238`
- New: `239`

### Rust Evidence

- Graph edges: `1`

## W-000705 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ethtool_stringset_ETH_SS_COUNT
- Explanation: ethtool_stringset_ETH_SS_COUNT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `21`
- New: `23`

### Rust Evidence

- Graph edges: `1`

## W-000707 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: mthp_stat_item_MTHP_STAT_NR_ANON_PARTIALLY_MAPPED
- Explanation: mthp_stat_item_MTHP_STAT_NR_ANON_PARTIALLY_MAPPED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `14`
- New: `16`

### Rust Evidence

- Graph edges: `1`

## W-000708 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: mthp_stat_item_MTHP_STAT_SHMEM_ALLOC
- Explanation: mthp_stat_item_MTHP_STAT_SHMEM_ALLOC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `7`
- New: `9`

### Rust Evidence

- Graph edges: `1`

## W-000710 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: mthp_stat_item_MTHP_STAT_SHMEM_FALLBACK_CHARGE
- Explanation: mthp_stat_item_MTHP_STAT_SHMEM_FALLBACK_CHARGE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `9`
- New: `11`

### Rust Evidence

- Graph edges: `1`

## W-000712 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: mthp_stat_item_MTHP_STAT_SPLIT_DEFERRED
- Explanation: mthp_stat_item_MTHP_STAT_SPLIT_DEFERRED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `12`
- New: `14`

### Rust Evidence

- Graph edges: `1`

## W-000713 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: mthp_stat_item_MTHP_STAT_SPLIT_FAILED
- Explanation: mthp_stat_item_MTHP_STAT_SPLIT_FAILED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `11`
- New: `13`

### Rust Evidence

- Graph edges: `1`

## W-000715 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: mthp_stat_item_MTHP_STAT_SWPOUT_FALLBACK
- Explanation: mthp_stat_item_MTHP_STAT_SWPOUT_FALLBACK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `6`
- New: `8`

### Rust Evidence

- Graph edges: `1`

## W-000716 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: mthp_stat_item___MTHP_STAT_COUNT
- Explanation: mthp_stat_item___MTHP_STAT_COUNT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `15`
- New: `17`

### Rust Evidence

- Graph edges: `1`

## W-000717 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_arch_2
- Explanation: pageflags_PG_arch_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `20`
- New: `21`

### Rust Evidence

- Graph edges: `1`

## W-000718 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_mlocked
- Explanation: pageflags_PG_mlocked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `19`
- New: `20`

### Rust Evidence

- Graph edges: `1`

## W-000719 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags___NR_PAGEFLAGS
- Explanation: pageflags___NR_PAGEFLAGS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `21`
- New: `22`

### Rust Evidence

- Graph edges: `1`

## W-000720 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_ARP_PVLAN_DISABLE
- Explanation: skb_drop_reason_SKB_DROP_REASON_ARP_PVLAN_DISABLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `102`
- New: `112`

### Rust Evidence

- Graph edges: `1`

## W-000721 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_BPF_CGROUP_EGRESS
- Explanation: skb_drop_reason_SKB_DROP_REASON_BPF_CGROUP_EGRESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `47`
- New: `51`

### Rust Evidence

- Graph edges: `1`

## W-000722 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_CPU_BACKLOG
- Explanation: skb_drop_reason_SKB_DROP_REASON_CPU_BACKLOG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `56`
- New: `66`

### Rust Evidence

- Graph edges: `1`

## W-000723 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_DEV_HDR
- Explanation: skb_drop_reason_SKB_DROP_REASON_DEV_HDR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `63`
- New: `73`

### Rust Evidence

- Graph edges: `1`

## W-000724 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_DEV_READY
- Explanation: skb_drop_reason_SKB_DROP_REASON_DEV_READY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `64`
- New: `74`

### Rust Evidence

- Graph edges: `1`

## W-000725 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_DUP_FRAG
- Explanation: skb_drop_reason_SKB_DROP_REASON_DUP_FRAG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `79`
- New: `89`

### Rust Evidence

- Graph edges: `1`

## W-000726 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FRAG_REASM_TIMEOUT
- Explanation: skb_drop_reason_SKB_DROP_REASON_FRAG_REASM_TIMEOUT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `80`
- New: `90`

### Rust Evidence

- Graph edges: `1`

## W-000727 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FRAG_TOO_FAR
- Explanation: skb_drop_reason_SKB_DROP_REASON_FRAG_TOO_FAR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `81`
- New: `91`

### Rust Evidence

- Graph edges: `1`

## W-000728 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FULL_RING
- Explanation: skb_drop_reason_SKB_DROP_REASON_FULL_RING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `65`
- New: `75`

### Rust Evidence

- Graph edges: `1`

## W-000729 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_HDR_TRUNC
- Explanation: skb_drop_reason_SKB_DROP_REASON_HDR_TRUNC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `67`
- New: `77`

### Rust Evidence

- Graph edges: `1`

## W-000730 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_ICMP_CSUM
- Explanation: skb_drop_reason_SKB_DROP_REASON_ICMP_CSUM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `70`
- New: `80`

### Rust Evidence

- Graph edges: `1`

## W-000731 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_INVALID_PROTO
- Explanation: skb_drop_reason_SKB_DROP_REASON_INVALID_PROTO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `71`
- New: `81`

### Rust Evidence

- Graph edges: `1`

## W-000732 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6DISABLED
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6DISABLED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `52`

### Rust Evidence

- Graph edges: `1`

## W-000733 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_BAD_EXTHDR
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_BAD_EXTHDR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `83`
- New: `93`

### Rust Evidence

- Graph edges: `1`

## W-000734 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_CODE
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_CODE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `86`
- New: `96`

### Rust Evidence

- Graph edges: `1`

## W-000735 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_OPTIONS
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_OPTIONS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `87`
- New: `97`

### Rust Evidence

- Graph edges: `1`

## W-000736 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_FRAG
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_FRAG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `84`
- New: `94`

### Rust Evidence

- Graph edges: `1`

## W-000737 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_HOP_LIMIT
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_HOP_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `85`
- New: `95`

### Rust Evidence

- Graph edges: `1`

## W-000738 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_NS_OTHERHOST
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_NS_OTHERHOST changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `88`
- New: `98`

### Rust Evidence

- Graph edges: `1`

## W-000739 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_CSUM
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_CSUM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `14`

### Rust Evidence

- Graph edges: `1`

## W-000740 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INADDRERRORS
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INADDRERRORS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `72`
- New: `82`

### Rust Evidence

- Graph edges: `1`

## W-000741 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INHDR
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INHDR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `11`
- New: `15`

### Rust Evidence

- Graph edges: `1`

## W-000742 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INNOROUTES
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INNOROUTES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `73`
- New: `83`

### Rust Evidence

- Graph edges: `1`

## W-000743 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_DEST
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_DEST changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `77`
- New: `87`

### Rust Evidence

- Graph edges: `1`

## W-000744 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_SOURCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_SOURCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `75`
- New: `85`

### Rust Evidence

- Graph edges: `1`

## W-000745 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_LOCALNET
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_LOCALNET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `76`
- New: `86`

### Rust Evidence

- Graph edges: `1`

## W-000746 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_LOCAL_SOURCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_LOCAL_SOURCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `74`
- New: `84`

### Rust Evidence

- Graph edges: `1`

## W-000747 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_NOPROTO
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_NOPROTO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `15`
- New: `19`

### Rust Evidence

- Graph edges: `1`

## W-000748 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_OUTNOROUTES
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_OUTNOROUTES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `46`
- New: `50`

### Rust Evidence

- Graph edges: `1`

## W-000749 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_RPFILTER
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_RPFILTER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `12`
- New: `16`

### Rust Evidence

- Graph edges: `1`

## W-000750 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_TUNNEL_ECN
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_TUNNEL_ECN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `99`
- New: `109`

### Rust Evidence

- Graph edges: `1`

## W-000751 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_LOCAL_MAC
- Explanation: skb_drop_reason_SKB_DROP_REASON_LOCAL_MAC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `101`
- New: `111`

### Rust Evidence

- Graph edges: `1`

## W-000752 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_MAC_INVALID_SOURCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_MAC_INVALID_SOURCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `96`
- New: `106`

### Rust Evidence

- Graph edges: `1`

## W-000753 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_MAX
- Explanation: skb_drop_reason_SKB_DROP_REASON_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `103`
- New: `115`

### Rust Evidence

- Graph edges: `1`

## W-000754 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NEIGH_CREATEFAIL
- Explanation: skb_drop_reason_SKB_DROP_REASON_NEIGH_CREATEFAIL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `49`
- New: `53`

### Rust Evidence

- Graph edges: `1`

## W-000755 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NEIGH_DEAD
- Explanation: skb_drop_reason_SKB_DROP_REASON_NEIGH_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `52`
- New: `56`

### Rust Evidence

- Graph edges: `1`

## W-000756 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NEIGH_FAILED
- Explanation: skb_drop_reason_SKB_DROP_REASON_NEIGH_FAILED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `50`
- New: `54`

### Rust Evidence

- Graph edges: `1`

## W-000757 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NEIGH_QUEUEFULL
- Explanation: skb_drop_reason_SKB_DROP_REASON_NEIGH_QUEUEFULL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `51`
- New: `55`

### Rust Evidence

- Graph edges: `1`

## W-000758 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NETFILTER_DROP
- Explanation: skb_drop_reason_SKB_DROP_REASON_NETFILTER_DROP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `12`

### Rust Evidence

- Graph edges: `1`

## W-000759 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NOMEM
- Explanation: skb_drop_reason_SKB_DROP_REASON_NOMEM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `66`
- New: `76`

### Rust Evidence

- Graph edges: `1`

## W-000760 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_OTHERHOST
- Explanation: skb_drop_reason_SKB_DROP_REASON_OTHERHOST changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `9`
- New: `13`

### Rust Evidence

- Graph edges: `1`

## W-000761 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_PACKET_SOCK_ERROR
- Explanation: skb_drop_reason_SKB_DROP_REASON_PACKET_SOCK_ERROR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `91`
- New: `101`

### Rust Evidence

- Graph edges: `1`

## W-000762 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_PKT_TOO_BIG
- Explanation: skb_drop_reason_SKB_DROP_REASON_PKT_TOO_BIG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `78`
- New: `88`

### Rust Evidence

- Graph edges: `1`

## W-000763 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_PKT_TOO_SMALL
- Explanation: skb_drop_reason_SKB_DROP_REASON_PKT_TOO_SMALL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `4`
- New: `9`

### Rust Evidence

- Graph edges: `1`

## W-000764 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_PROTO_MEM
- Explanation: skb_drop_reason_SKB_DROP_REASON_PROTO_MEM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `17`
- New: `20`

### Rust Evidence

- Graph edges: `1`

## W-000765 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_QDISC_DROP
- Explanation: skb_drop_reason_SKB_DROP_REASON_QDISC_DROP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `55`
- New: `59`

### Rust Evidence

- Graph edges: `1`

## W-000766 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_QUEUE_PURGE
- Explanation: skb_drop_reason_SKB_DROP_REASON_QUEUE_PURGE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `89`
- New: `99`

### Rust Evidence

- Graph edges: `1`

## W-000767 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SECURITY_HOOK
- Explanation: skb_drop_reason_SKB_DROP_REASON_SECURITY_HOOK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `54`
- New: `58`

### Rust Evidence

- Graph edges: `1`

## W-000768 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SKB_CSUM
- Explanation: skb_drop_reason_SKB_DROP_REASON_SKB_CSUM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `60`
- New: `70`

### Rust Evidence

- Graph edges: `1`

## W-000769 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SKB_GSO_SEG
- Explanation: skb_drop_reason_SKB_DROP_REASON_SKB_GSO_SEG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `61`
- New: `71`

### Rust Evidence

- Graph edges: `1`

## W-000770 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SKB_UCOPY_FAULT
- Explanation: skb_drop_reason_SKB_DROP_REASON_SKB_UCOPY_FAULT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `62`
- New: `72`

### Rust Evidence

- Graph edges: `1`

## W-000771 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SOCKET_BACKLOG
- Explanation: skb_drop_reason_SKB_DROP_REASON_SOCKET_BACKLOG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `26`
- New: `29`

### Rust Evidence

- Graph edges: `1`

## W-000772 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SOCKET_FILTER
- Explanation: skb_drop_reason_SKB_DROP_REASON_SOCKET_FILTER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `6`
- New: `5`

### Rust Evidence

- Graph edges: `1`

## W-000773 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SOCKET_RCVBUFF
- Explanation: skb_drop_reason_SKB_DROP_REASON_SOCKET_RCVBUFF changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `6`

### Rust Evidence

- Graph edges: `1`

## W-000774 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TAP_FILTER
- Explanation: skb_drop_reason_SKB_DROP_REASON_TAP_FILTER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `68`
- New: `78`

### Rust Evidence

- Graph edges: `1`

## W-000775 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TAP_TXFILTER
- Explanation: skb_drop_reason_SKB_DROP_REASON_TAP_TXFILTER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `69`
- New: `79`

### Rust Evidence

- Graph edges: `1`

## W-000776 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_ABORT_ON_DATA
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_ABORT_ON_DATA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `28`
- New: `31`

### Rust Evidence

- Graph edges: `1`

## W-000777 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_ACK_UNSENT_DATA
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_ACK_UNSENT_DATA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `43`
- New: `47`

### Rust Evidence

- Graph edges: `1`

## W-000778 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_AOFAILURE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_AOFAILURE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `25`
- New: `28`

### Rust Evidence

- Graph edges: `1`

## W-000779 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_AOKEYNOTFOUND
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_AOKEYNOTFOUND changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `24`
- New: `27`

### Rust Evidence

- Graph edges: `1`

## W-000780 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_AONOTFOUND
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_AONOTFOUND changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `22`
- New: `25`

### Rust Evidence

- Graph edges: `1`

## W-000781 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_AOUNEXPECTED
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_AOUNEXPECTED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `23`
- New: `26`

### Rust Evidence

- Graph edges: `1`

## W-000782 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_AUTH_HDR
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_AUTH_HDR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `18`
- New: `21`

### Rust Evidence

- Graph edges: `1`

## W-000783 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_CLOSE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_CLOSE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `39`
- New: `43`

### Rust Evidence

- Graph edges: `1`

## W-000784 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_CSUM
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_CSUM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `10`

### Rust Evidence

- Graph edges: `1`

## W-000785 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_FASTOPEN
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_FASTOPEN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `40`
- New: `44`

### Rust Evidence

- Graph edges: `1`

## W-000786 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_FLAGS
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_FLAGS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `27`
- New: `30`

### Rust Evidence

- Graph edges: `1`

## W-000787 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_ACK_SEQUENCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_ACK_SEQUENCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `36`
- New: `40`

### Rust Evidence

- Graph edges: `1`

## W-000788 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_SEQUENCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_SEQUENCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `35`
- New: `39`

### Rust Evidence

- Graph edges: `1`

## W-000789 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_SYN
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_SYN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `38`
- New: `42`

### Rust Evidence

- Graph edges: `1`

## W-000790 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_MD5FAILURE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_MD5FAILURE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `21`
- New: `24`

### Rust Evidence

- Graph edges: `1`

## W-000791 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_MD5NOTFOUND
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_MD5NOTFOUND changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `19`
- New: `22`

### Rust Evidence

- Graph edges: `1`

## W-000792 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_MD5UNEXPECTED
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_MD5UNEXPECTED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `20`
- New: `23`

### Rust Evidence

- Graph edges: `1`

## W-000793 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_MINTTL
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_MINTTL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `82`
- New: `92`

### Rust Evidence

- Graph edges: `1`

## W-000794 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OFOMERGE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OFOMERGE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `32`
- New: `35`

### Rust Evidence

- Graph edges: `1`

## W-000795 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OFO_DROP
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OFO_DROP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `45`
- New: `49`

### Rust Evidence

- Graph edges: `1`

## W-000796 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OFO_QUEUE_PRUNE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OFO_QUEUE_PRUNE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `44`
- New: `48`

### Rust Evidence

- Graph edges: `1`

## W-000797 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OLD_ACK
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OLD_ACK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `41`
- New: `45`

### Rust Evidence

- Graph edges: `1`

## W-000798 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OLD_DATA
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OLD_DATA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `30`
- New: `33`

### Rust Evidence

- Graph edges: `1`

## W-000799 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OLD_SEQUENCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OLD_SEQUENCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `34`
- New: `38`

### Rust Evidence

- Graph edges: `1`

## W-000800 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OVERWINDOW
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OVERWINDOW changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `31`
- New: `34`

### Rust Evidence

- Graph edges: `1`

## W-000801 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_RESET
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_RESET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `37`
- New: `41`

### Rust Evidence

- Graph edges: `1`

## W-000803 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_TOO_OLD_ACK
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_TOO_OLD_ACK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `42`
- New: `46`

### Rust Evidence

- Graph edges: `1`

## W-000804 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_ZEROWINDOW
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_ZEROWINDOW changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `29`
- New: `32`

### Rust Evidence

- Graph edges: `1`

## W-000805 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_CHAIN_NOTFOUND
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_CHAIN_NOTFOUND changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `92`
- New: `102`

### Rust Evidence

- Graph edges: `1`

## W-000806 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_COOKIE_ERROR
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_COOKIE_ERROR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `90`
- New: `100`

### Rust Evidence

- Graph edges: `1`

## W-000807 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_EGRESS
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_EGRESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `53`
- New: `57`

### Rust Evidence

- Graph edges: `1`

## W-000808 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_INGRESS
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_INGRESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `58`
- New: `68`

### Rust Evidence

- Graph edges: `1`

## W-000809 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_RECLASSIFY_LOOP
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_RECLASSIFY_LOOP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `93`
- New: `103`

### Rust Evidence

- Graph edges: `1`

## W-000810 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TUNNEL_TXINFO
- Explanation: skb_drop_reason_SKB_DROP_REASON_TUNNEL_TXINFO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `100`
- New: `110`

### Rust Evidence

- Graph edges: `1`

## W-000811 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_UDP_CSUM
- Explanation: skb_drop_reason_SKB_DROP_REASON_UDP_CSUM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `7`
- New: `11`

### Rust Evidence

- Graph edges: `1`

## W-000812 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_UNHANDLED_PROTO
- Explanation: skb_drop_reason_SKB_DROP_REASON_UNHANDLED_PROTO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `59`
- New: `69`

### Rust Evidence

- Graph edges: `1`

## W-000813 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_UNICAST_IN_L2_MULTICAST
- Explanation: skb_drop_reason_SKB_DROP_REASON_UNICAST_IN_L2_MULTICAST changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `13`
- New: `17`

### Rust Evidence

- Graph edges: `1`

## W-000814 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_VXLAN_ENTRY_EXISTS
- Explanation: skb_drop_reason_SKB_DROP_REASON_VXLAN_ENTRY_EXISTS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `97`
- New: `107`

### Rust Evidence

- Graph edges: `1`

## W-000815 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_VXLAN_INVALID_HDR
- Explanation: skb_drop_reason_SKB_DROP_REASON_VXLAN_INVALID_HDR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `94`
- New: `104`

### Rust Evidence

- Graph edges: `1`

## W-000816 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_VXLAN_VNI_NOT_FOUND
- Explanation: skb_drop_reason_SKB_DROP_REASON_VXLAN_VNI_NOT_FOUND changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `95`
- New: `105`

### Rust Evidence

- Graph edges: `1`

## W-000817 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_XDP
- Explanation: skb_drop_reason_SKB_DROP_REASON_XDP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `57`
- New: `67`

### Rust Evidence

- Graph edges: `1`

## W-000818 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_XFRM_POLICY
- Explanation: skb_drop_reason_SKB_DROP_REASON_XFRM_POLICY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `14`
- New: `18`

### Rust Evidence

- Graph edges: `1`

## W-000819 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: tlb_flush_reason_NR_TLB_FLUSH_REASONS
- Explanation: tlb_flush_reason_NR_TLB_FLUSH_REASONS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `6`

### Rust Evidence

- Graph edges: `1`

## W-000820 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: FMODE_BACKING
- Explanation: FMODE_BACKING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `((__force fmode_t)(1 << 25))`
- New: `((__force fmode_t)(1 << 24))`

### Rust Evidence

- Graph edges: `0`

## W-000821 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: FMODE_NONOTIFY
- Explanation: FMODE_NONOTIFY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `((__force fmode_t)(1 << 26))`
- New: `((__force fmode_t)(1 << 25))`

### Rust Evidence

- Graph edges: `0`

## W-000822 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: OPEN_FMODE
- Explanation: OPEN_FMODE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `((__force fmode_t)(((flag + 1) & O_ACCMODE) | \`
- New: `((__force fmode_t)((flag + 1) & O_ACCMODE))`

### Rust Evidence

- Graph edges: `0`

## W-000823 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: secs_to_jiffies
- Explanation: secs_to_jiffies changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `((_secs) * HZ)`
- New: `(unsigned long)((_secs) * HZ)`

### Rust Evidence

- Graph edges: `0`
