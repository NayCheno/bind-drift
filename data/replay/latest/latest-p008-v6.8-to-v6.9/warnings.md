# BindDrift Ranked Warnings

## W-000283 SignatureDrift

- Risk: High
- Score: 14.6
- Symbol: cs
- Explanation: cs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `44`

## W-000624 SignatureDrift

- Risk: High
- Score: 14.2
- Symbol: ss
- Explanation: ss changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `18`

## W-000612 SignatureDrift

- Risk: High
- Score: 13.2
- Symbol: sl
- Explanation: sl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `13`

## W-000648 SignatureDrift

- Risk: High
- Score: 12.8
- Symbol: text_poke
- Explanation: text_poke changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `11`

## W-000704 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: bio
- Explanation: bio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'bi_next', 'type': '*mut bio'}, {'name': 'bi_bdev', 'type': '*mut block_device'}, {'name': 'bi_opf', 'type': 'blk_opf_t'}, {'name': 'bi_flags', 'type': 'core::ffi::c_ushort'}, {'name': 'bi_ioprio', 'type': 'core::ffi::c_ushort'}, {'name': 'bi_write_hint', 'type': 'rw_hint'}, {'name': 'bi_status', 'type': 'blk_status_t'}, {'name': '__bi_remaining', 'type': 'atomic_t'}, {'name': 'bi_iter', 'type': 'bvec_iter'}, {'name': 'bi_cookie', 'type': 'blk_qc_t'}, {'name': 'bi_end_io', 'type': 'bio_end_io_t'}, {'name': 'bi_private', 'type': '*mut core::ffi::c_void'}, {'name': 'bi_blkg', 'type': '*mut blkcg_gq'}, {'name': 'bi_issue', 'type': 'bio_issue'}, {'name': 'bi_iocost_cost', 'type': 'u64_'}, {'name': '__bindgen_anon_1', 'type': 'bio__bindgen_ty_1'}, {'name': 'bi_vcnt', 'type': 'core::ffi::c_ushort'}, {'name': 'bi_max_vecs', 'type': 'core::ffi::c_ushort'}, {'name': '__bi_cnt', 'type': 'atomic_t'}, {'name': 'bi_io_vec', 'type': '*mut bio_vec'}, {'name': 'bi_pool', 'type': '*mut bio_set'}, {'name': 'bi_inline_vecs', 'type': '__IncompleteArrayField<bio_vec>'}]`

### Rust Evidence

- Graph edges: `23`

## W-000708 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: bpf_prog
- Explanation: bpf_prog changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'pages', 'type': 'u16_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'type_', 'type': 'bpf_prog_type'}, {'name': 'expected_attach_type', 'type': 'bpf_attach_type'}, {'name': 'len', 'type': 'u32_'}, {'name': 'jited_len', 'type': 'u32_'}, {'name': 'tag', 'type': '[u8_; 8usize]'}, {'name': 'stats', 'type': '*mut bpf_prog_stats'}, {'name': 'active', 'type': '*mut core::ffi::c_int'}, {'name': 'bpf_func', 'type': '::core::option::Option<'}, {'name': 'aux', 'type': '*mut bpf_prog_aux'}, {'name': 'orig_prog', 'type': '*mut sock_fprog_kern'}, {'name': '__bindgen_anon_1', 'type': 'bpf_prog__bindgen_ty_1'}]`

### Rust Evidence

- Graph edges: `50`

## W-000709 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: cgroup
- Explanation: cgroup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[{'name': 'self_', 'type': 'cgroup_subsys_state'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'level', 'type': 'core::ffi::c_int'}, {'name': 'max_depth', 'type': 'core::ffi::c_int'}, {'name': 'nr_descendants', 'type': 'core::ffi::c_int'}, {'name': 'nr_dying_descendants', 'type': 'core::ffi::c_int'}, {'name': 'max_descendants', 'type': 'core::ffi::c_int'}, {'name': 'nr_populated_csets', 'type': 'core::ffi::c_int'}, {'name': 'nr_populated_domain_children', 'type': 'core::ffi::c_int'}, {'name': 'nr_populated_threaded_children', 'type': 'core::ffi::c_int'}, {'name': 'nr_threaded_children', 'type': 'core::ffi::c_int'}, {'name': 'kn', 'type': '*mut kernfs_node'}, {'name': 'procs_file', 'type': 'cgroup_file'}, {'name': 'events_file', 'type': 'cgroup_file'}, {'name': 'psi_files', 'type': '__IncompleteArrayField<cgroup_file>'}, {'name': 'subtree_control', 'type': 'u16_'}, {'name': 'subtree_ss_mask', 'type': 'u16_'}, {'name': 'old_subtree_control', 'type': 'u16_'}, {'name': 'old_subtree_ss_mask', 'type': 'u16_'}, {'name': 'subsys', 'type': '[*mut cgroup_subsys_state; 14usize]'}, {'name': 'root', 'type': '*mut cgroup_root'}, {'name': 'cset_links', 'type': 'list_head'}, {'name': 'e_csets', 'type': '[list_head; 14usize]'}, {'name': 'dom_cgrp', 'type': '*mut cgroup'}, {'name': 'old_dom_cgrp', 'type': '*mut cgroup'}, {'name': 'rstat_cpu', 'type': '*mut cgroup_rstat_cpu'}, {'name': 'rstat_css_list', 'type': 'list_head'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': '_pad_', 'type': 'cacheline_padding'}, {'name': 'rstat_flush_next', 'type': '*mut cgroup'}, {'name': 'last_bstat', 'type': 'cgroup_base_stat'}, {'name': 'bstat', 'type': 'cgroup_base_stat'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'pidlists', 'type': 'list_head'}, {'name': 'pidlist_mutex', 'type': 'mutex'}, {'name': 'offline_waitq', 'type': 'wait_queue_head_t'}, {'name': 'release_agent_work', 'type': 'work_struct'}, {'name': 'psi', 'type': '*mut psi_group'}, {'name': 'bpf', 'type': 'cgroup_bpf'}, {'name': 'congestion_count', 'type': 'atomic_t'}, {'name': 'freezer', 'type': 'cgroup_freezer_state'}, {'name': 'ancestors', 'type': '__IncompleteArrayField<*mut cgroup>'}]`

### Rust Evidence

- Graph edges: `50`

## W-000716 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: inode
- Explanation: inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'i_mode', 'type': 'umode_t'}, {'name': 'i_opflags', 'type': 'core::ffi::c_ushort'}, {'name': 'i_uid', 'type': 'kuid_t'}, {'name': 'i_gid', 'type': 'kgid_t'}, {'name': 'i_flags', 'type': 'core::ffi::c_uint'}, {'name': 'i_acl', 'type': '*mut posix_acl'}, {'name': 'i_default_acl', 'type': '*mut posix_acl'}, {'name': 'i_op', 'type': '*const inode_operations'}, {'name': 'i_sb', 'type': '*mut super_block'}, {'name': 'i_mapping', 'type': '*mut address_space'}, {'name': 'i_security', 'type': '*mut core::ffi::c_void'}, {'name': 'i_ino', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'inode__bindgen_ty_1'}, {'name': 'i_rdev', 'type': 'dev_t'}, {'name': 'i_size', 'type': 'loff_t'}, {'name': '__i_atime', 'type': 'timespec64'}, {'name': '__i_mtime', 'type': 'timespec64'}, {'name': '__i_ctime', 'type': 'timespec64'}, {'name': 'i_lock', 'type': 'spinlock_t'}, {'name': 'i_bytes', 'type': 'core::ffi::c_ushort'}, {'name': 'i_blkbits', 'type': 'u8_'}, {'name': 'i_write_hint', 'type': 'u8_'}, {'name': 'i_blocks', 'type': 'blkcnt_t'}, {'name': 'i_state', 'type': 'core::ffi::c_ulong'}, {'name': 'i_rwsem', 'type': 'rw_semaphore'}, {'name': 'dirtied_when', 'type': 'core::ffi::c_ulong'}, {'name': 'dirtied_time_when', 'type': 'core::ffi::c_ulong'}, {'name': 'i_hash', 'type': 'hlist_node'}, {'name': 'i_io_list', 'type': 'list_head'}, {'name': 'i_lru', 'type': 'list_head'}, {'name': 'i_sb_list', 'type': 'list_head'}, {'name': 'i_wb_list', 'type': 'list_head'}, {'name': '__bindgen_anon_2', 'type': 'inode__bindgen_ty_2'}, {'name': 'i_version', 'type': 'atomic64_t'}, {'name': 'i_sequence', 'type': 'atomic64_t'}, {'name': 'i_count', 'type': 'atomic_t'}, {'name': 'i_dio_count', 'type': 'atomic_t'}, {'name': 'i_writecount', 'type': 'atomic_t'}, {'name': 'i_readcount', 'type': 'atomic_t'}, {'name': '__bindgen_anon_3', 'type': 'inode__bindgen_ty_3'}, {'name': 'i_flctx', 'type': '*mut file_lock_context'}, {'name': 'i_data', 'type': 'address_space'}, {'name': 'i_devices', 'type': 'list_head'}, {'name': '__bindgen_anon_4', 'type': 'inode__bindgen_ty_4'}, {'name': 'i_generation', 'type': '__u32'}, {'name': 'i_fsnotify_mask', 'type': '__u32'}, {'name': 'i_fsnotify_marks', 'type': '*mut fsnotify_mark_connector'}, {'name': 'i_private', 'type': '*mut core::ffi::c_void'}]`
- New: `[{'name': 'i_mode', 'type': 'umode_t'}, {'name': 'i_opflags', 'type': 'core::ffi::c_ushort'}, {'name': 'i_uid', 'type': 'kuid_t'}, {'name': 'i_gid', 'type': 'kgid_t'}, {'name': 'i_flags', 'type': 'core::ffi::c_uint'}, {'name': 'i_acl', 'type': '*mut posix_acl'}, {'name': 'i_default_acl', 'type': '*mut posix_acl'}, {'name': 'i_op', 'type': '*const inode_operations'}, {'name': 'i_sb', 'type': '*mut super_block'}, {'name': 'i_mapping', 'type': '*mut address_space'}, {'name': 'i_security', 'type': '*mut core::ffi::c_void'}, {'name': 'i_ino', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'inode__bindgen_ty_1'}, {'name': 'i_rdev', 'type': 'dev_t'}, {'name': 'i_size', 'type': 'loff_t'}, {'name': '__i_atime', 'type': 'timespec64'}, {'name': '__i_mtime', 'type': 'timespec64'}, {'name': '__i_ctime', 'type': 'timespec64'}, {'name': 'i_lock', 'type': 'spinlock_t'}, {'name': 'i_bytes', 'type': 'core::ffi::c_ushort'}, {'name': 'i_blkbits', 'type': 'u8_'}, {'name': 'i_write_hint', 'type': 'rw_hint'}, {'name': 'i_blocks', 'type': 'blkcnt_t'}, {'name': 'i_state', 'type': 'core::ffi::c_ulong'}, {'name': 'i_rwsem', 'type': 'rw_semaphore'}, {'name': 'dirtied_when', 'type': 'core::ffi::c_ulong'}, {'name': 'dirtied_time_when', 'type': 'core::ffi::c_ulong'}, {'name': 'i_hash', 'type': 'hlist_node'}, {'name': 'i_io_list', 'type': 'list_head'}, {'name': 'i_lru', 'type': 'list_head'}, {'name': 'i_sb_list', 'type': 'list_head'}, {'name': 'i_wb_list', 'type': 'list_head'}, {'name': '__bindgen_anon_2', 'type': 'inode__bindgen_ty_2'}, {'name': 'i_version', 'type': 'atomic64_t'}, {'name': 'i_sequence', 'type': 'atomic64_t'}, {'name': 'i_count', 'type': 'atomic_t'}, {'name': 'i_dio_count', 'type': 'atomic_t'}, {'name': 'i_writecount', 'type': 'atomic_t'}, {'name': 'i_readcount', 'type': 'atomic_t'}, {'name': '__bindgen_anon_3', 'type': 'inode__bindgen_ty_3'}, {'name': 'i_flctx', 'type': '*mut file_lock_context'}, {'name': 'i_data', 'type': 'address_space'}, {'name': 'i_devices', 'type': 'list_head'}, {'name': '__bindgen_anon_4', 'type': 'inode__bindgen_ty_4'}, {'name': 'i_generation', 'type': '__u32'}, {'name': 'i_fsnotify_mask', 'type': '__u32'}, {'name': 'i_fsnotify_marks', 'type': '*mut fsnotify_mark_connector'}, {'name': 'i_private', 'type': '*mut core::ffi::c_void'}]`

### Rust Evidence

- Graph edges: `33`

## W-000719 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: module
- Explanation: module changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'state', 'type': 'module_state'}, {'name': 'list', 'type': 'list_head'}, {'name': 'name', 'type': '[core::ffi::c_char; 56usize]'}, {'name': 'mkobj', 'type': 'module_kobject'}, {'name': 'modinfo_attrs', 'type': '*mut module_attribute'}, {'name': 'version', 'type': '*const core::ffi::c_char'}, {'name': 'srcversion', 'type': '*const core::ffi::c_char'}, {'name': 'holders_dir', 'type': '*mut kobject'}, {'name': 'syms', 'type': '*mut kernel_symbol'}, {'name': 'crcs', 'type': '*const s32'}, {'name': 'num_syms', 'type': 'core::ffi::c_uint'}, {'name': 'param_lock', 'type': 'mutex'}, {'name': 'kp', 'type': '*mut kernel_param'}, {'name': 'num_kp', 'type': 'core::ffi::c_uint'}, {'name': 'num_gpl_syms', 'type': 'core::ffi::c_uint'}, {'name': 'gpl_syms', 'type': '*const kernel_symbol'}, {'name': 'gpl_crcs', 'type': '*const s32'}, {'name': 'using_gplonly_symbols', 'type': 'bool_'}, {'name': 'async_probe_requested', 'type': 'bool_'}, {'name': 'num_exentries', 'type': 'core::ffi::c_uint'}, {'name': 'extable', 'type': '*mut exception_table_entry'}, {'name': 'init', 'type': '::core::option::Option<unsafe extern "C" fn() -> core::ffi::c_int>'}, {'name': 'mem', 'type': '[module_memory; 7usize]'}, {'name': 'arch', 'type': 'mod_arch_specific'}, {'name': 'taints', 'type': 'core::ffi::c_ulong'}, {'name': 'num_bugs', 'type': 'core::ffi::c_uint'}, {'name': 'bug_list', 'type': 'list_head'}, {'name': 'bug_table', 'type': '*mut bug_entry'}, {'name': 'kallsyms', 'type': '*mut mod_kallsyms'}, {'name': 'core_kallsyms', 'type': 'mod_kallsyms'}, {'name': 'sect_attrs', 'type': '*mut module_sect_attrs'}, {'name': 'notes_attrs', 'type': '*mut module_notes_attrs'}, {'name': 'args', 'type': '*mut core::ffi::c_char'}, {'name': 'percpu', 'type': '*mut core::ffi::c_void'}, {'name': 'percpu_size', 'type': 'core::ffi::c_uint'}, {'name': 'noinstr_text_start', 'type': '*mut core::ffi::c_void'}, {'name': 'noinstr_text_size', 'type': 'core::ffi::c_uint'}, {'name': 'num_tracepoints', 'type': 'core::ffi::c_uint'}, {'name': 'tracepoints_ptrs', 'type': '*const core::ffi::c_int'}, {'name': 'num_srcu_structs', 'type': 'core::ffi::c_uint'}, {'name': 'srcu_struct_ptrs', 'type': '*mut *mut srcu_struct'}, {'name': 'jump_entries', 'type': '*mut jump_entry'}, {'name': 'num_jump_entries', 'type': 'core::ffi::c_uint'}, {'name': 'num_trace_bprintk_fmt', 'type': 'core::ffi::c_uint'}, {'name': 'trace_bprintk_fmt_start', 'type': '*mut *const core::ffi::c_char'}, {'name': 'trace_events', 'type': '*mut *mut trace_event_call'}, {'name': 'num_trace_events', 'type': 'core::ffi::c_uint'}, {'name': 'trace_evals', 'type': '*mut *mut trace_eval_map'}, {'name': 'num_trace_evals', 'type': 'core::ffi::c_uint'}, {'name': 'kprobes_text_start', 'type': '*mut core::ffi::c_void'}, {'name': 'kprobes_text_size', 'type': 'core::ffi::c_uint'}, {'name': 'kprobe_blacklist', 'type': '*mut core::ffi::c_ulong'}, {'name': 'num_kprobe_blacklist', 'type': 'core::ffi::c_uint'}, {'name': 'num_static_call_sites', 'type': 'core::ffi::c_int'}, {'name': 'static_call_sites', 'type': '*mut static_call_site'}, {'name': 'source_list', 'type': 'list_head'}, {'name': 'target_list', 'type': 'list_head'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'refcnt', 'type': 'atomic_t'}, {'name': 'ctors', 'type': '*mut ctor_fn_t'}, {'name': 'num_ctors', 'type': 'core::ffi::c_uint'}]`
- New: `[{'name': 'state', 'type': 'module_state'}, {'name': 'list', 'type': 'list_head'}, {'name': 'name', 'type': '[core::ffi::c_char; 56usize]'}, {'name': 'mkobj', 'type': 'module_kobject'}, {'name': 'modinfo_attrs', 'type': '*mut module_attribute'}, {'name': 'version', 'type': '*const core::ffi::c_char'}, {'name': 'srcversion', 'type': '*const core::ffi::c_char'}, {'name': 'holders_dir', 'type': '*mut kobject'}, {'name': 'syms', 'type': '*mut kernel_symbol'}, {'name': 'crcs', 'type': '*const s32'}, {'name': 'num_syms', 'type': 'core::ffi::c_uint'}, {'name': 'param_lock', 'type': 'mutex'}, {'name': 'kp', 'type': '*mut kernel_param'}, {'name': 'num_kp', 'type': 'core::ffi::c_uint'}, {'name': 'num_gpl_syms', 'type': 'core::ffi::c_uint'}, {'name': 'gpl_syms', 'type': '*const kernel_symbol'}, {'name': 'gpl_crcs', 'type': '*const s32'}, {'name': 'using_gplonly_symbols', 'type': 'bool_'}, {'name': 'async_probe_requested', 'type': 'bool_'}, {'name': 'num_exentries', 'type': 'core::ffi::c_uint'}, {'name': 'extable', 'type': '*mut exception_table_entry'}, {'name': 'init', 'type': '::core::option::Option<unsafe extern "C" fn() -> core::ffi::c_int>'}, {'name': 'mem', 'type': '[module_memory; 7usize]'}, {'name': 'arch', 'type': 'mod_arch_specific'}, {'name': 'taints', 'type': 'core::ffi::c_ulong'}, {'name': 'num_bugs', 'type': 'core::ffi::c_uint'}, {'name': 'bug_list', 'type': 'list_head'}, {'name': 'bug_table', 'type': '*mut bug_entry'}, {'name': 'kallsyms', 'type': '*mut mod_kallsyms'}, {'name': 'core_kallsyms', 'type': 'mod_kallsyms'}, {'name': 'sect_attrs', 'type': '*mut module_sect_attrs'}, {'name': 'notes_attrs', 'type': '*mut module_notes_attrs'}, {'name': 'args', 'type': '*mut core::ffi::c_char'}, {'name': 'percpu', 'type': '*mut core::ffi::c_void'}, {'name': 'percpu_size', 'type': 'core::ffi::c_uint'}, {'name': 'noinstr_text_start', 'type': '*mut core::ffi::c_void'}, {'name': 'noinstr_text_size', 'type': 'core::ffi::c_uint'}, {'name': 'num_tracepoints', 'type': 'core::ffi::c_uint'}, {'name': 'tracepoints_ptrs', 'type': '*const core::ffi::c_int'}, {'name': 'num_srcu_structs', 'type': 'core::ffi::c_uint'}, {'name': 'srcu_struct_ptrs', 'type': '*mut *mut srcu_struct'}, {'name': 'jump_entries', 'type': '*mut jump_entry'}, {'name': 'num_jump_entries', 'type': 'core::ffi::c_uint'}, {'name': 'num_trace_bprintk_fmt', 'type': 'core::ffi::c_uint'}, {'name': 'trace_bprintk_fmt_start', 'type': '*mut *const core::ffi::c_char'}, {'name': 'trace_events', 'type': '*mut *mut trace_event_call'}, {'name': 'num_trace_events', 'type': 'core::ffi::c_uint'}, {'name': 'trace_evals', 'type': '*mut *mut trace_eval_map'}, {'name': 'num_trace_evals', 'type': 'core::ffi::c_uint'}, {'name': 'kprobes_text_start', 'type': '*mut core::ffi::c_void'}, {'name': 'kprobes_text_size', 'type': 'core::ffi::c_uint'}, {'name': 'kprobe_blacklist', 'type': '*mut core::ffi::c_ulong'}, {'name': 'num_kprobe_blacklist', 'type': 'core::ffi::c_uint'}, {'name': 'num_static_call_sites', 'type': 'core::ffi::c_int'}, {'name': 'static_call_sites', 'type': '*mut static_call_site'}, {'name': 'source_list', 'type': 'list_head'}, {'name': 'target_list', 'type': 'list_head'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'refcnt', 'type': 'atomic_t'}]`

### Rust Evidence

- Graph edges: `34`

## W-000724 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: phy_device
- Explanation: phy_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mdio', 'type': 'mdio_device'}, {'name': 'drv', 'type': '*mut phy_driver'}, {'name': 'devlink', 'type': '*mut device_link'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'c45_ids', 'type': 'phy_c45_device_ids'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'rate_matching', 'type': 'core::ffi::c_int'}, {'name': 'state', 'type': 'phy_state'}, {'name': 'dev_flags', 'type': 'u32_'}, {'name': 'interface', 'type': 'phy_interface_t'}, {'name': 'possible_interfaces', 'type': '[core::ffi::c_ulong; 1usize]'}, {'name': 'speed', 'type': 'core::ffi::c_int'}, {'name': 'duplex', 'type': 'core::ffi::c_int'}, {'name': 'port', 'type': 'core::ffi::c_int'}, {'name': 'pause', 'type': 'core::ffi::c_int'}, {'name': 'asym_pause', 'type': 'core::ffi::c_int'}, {'name': 'master_slave_get', 'type': 'u8_'}, {'name': 'master_slave_set', 'type': 'u8_'}, {'name': 'master_slave_state', 'type': 'u8_'}, {'name': 'supported', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'advertising', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'lp_advertising', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'adv_old', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'supported_eee', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'advertising_eee', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'eee_enabled', 'type': 'bool_'}, {'name': 'host_interfaces', 'type': '[core::ffi::c_ulong; 1usize]'}, {'name': 'eee_broken_modes', 'type': 'u32_'}, {'name': 'leds', 'type': 'list_head'}, {'name': 'irq', 'type': 'core::ffi::c_int'}, {'name': 'priv_', 'type': '*mut core::ffi::c_void'}, {'name': 'shared', 'type': '*mut phy_package_shared'}, {'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'ehdr', 'type': '*mut core::ffi::c_void'}, {'name': 'nest', 'type': '*mut nlattr'}, {'name': 'state_queue', 'type': 'delayed_work'}, {'name': 'lock', 'type': 'mutex'}, {'name': 'sfp_bus_attached', 'type': 'bool_'}, {'name': 'sfp_bus', 'type': '*mut sfp_bus'}, {'name': 'phylink', 'type': '*mut phylink'}, {'name': 'attached_dev', 'type': '*mut net_device'}, {'name': 'mii_ts', 'type': '*mut mii_timestamper'}, {'name': 'psec', 'type': '*mut pse_control'}, {'name': 'mdix', 'type': 'u8_'}, {'name': 'mdix_ctrl', 'type': 'u8_'}, {'name': 'pma_extable', 'type': 'core::ffi::c_int'}, {'name': 'link_down_events', 'type': 'core::ffi::c_uint'}, {'name': 'adjust_link', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut net_device)>'}]`
- New: `[{'name': 'mdio', 'type': 'mdio_device'}, {'name': 'drv', 'type': '*const phy_driver'}, {'name': 'devlink', 'type': '*mut device_link'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'c45_ids', 'type': 'phy_c45_device_ids'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'rate_matching', 'type': 'core::ffi::c_int'}, {'name': 'state', 'type': 'phy_state'}, {'name': 'dev_flags', 'type': 'u32_'}, {'name': 'interface', 'type': 'phy_interface_t'}, {'name': 'possible_interfaces', 'type': '[core::ffi::c_ulong; 1usize]'}, {'name': 'speed', 'type': 'core::ffi::c_int'}, {'name': 'duplex', 'type': 'core::ffi::c_int'}, {'name': 'port', 'type': 'core::ffi::c_int'}, {'name': 'pause', 'type': 'core::ffi::c_int'}, {'name': 'asym_pause', 'type': 'core::ffi::c_int'}, {'name': 'master_slave_get', 'type': 'u8_'}, {'name': 'master_slave_set', 'type': 'u8_'}, {'name': 'master_slave_state', 'type': 'u8_'}, {'name': 'supported', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'advertising', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'lp_advertising', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'adv_old', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'supported_eee', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'advertising_eee', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'eee_enabled', 'type': 'bool_'}, {'name': 'host_interfaces', 'type': '[core::ffi::c_ulong; 1usize]'}, {'name': 'eee_broken_modes', 'type': 'u32_'}, {'name': 'enable_tx_lpi', 'type': 'bool_'}, {'name': 'eee_cfg', 'type': 'eee_config'}, {'name': 'leds', 'type': 'list_head'}, {'name': 'irq', 'type': 'core::ffi::c_int'}, {'name': 'priv_', 'type': '*mut core::ffi::c_void'}, {'name': 'shared', 'type': '*mut phy_package_shared'}, {'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'ehdr', 'type': '*mut core::ffi::c_void'}, {'name': 'nest', 'type': '*mut nlattr'}, {'name': 'state_queue', 'type': 'delayed_work'}, {'name': 'lock', 'type': 'mutex'}, {'name': 'sfp_bus_attached', 'type': 'bool_'}, {'name': 'sfp_bus', 'type': '*mut sfp_bus'}, {'name': 'phylink', 'type': '*mut phylink'}, {'name': 'attached_dev', 'type': '*mut net_device'}, {'name': 'mii_ts', 'type': '*mut mii_timestamper'}, {'name': 'psec', 'type': '*mut pse_control'}, {'name': 'mdix', 'type': 'u8_'}, {'name': 'mdix_ctrl', 'type': 'u8_'}, {'name': 'pma_extable', 'type': 'core::ffi::c_int'}, {'name': 'link_down_events', 'type': 'core::ffi::c_uint'}, {'name': 'adjust_link', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut net_device)>'}]`

### Rust Evidence

- Graph edges: `50`

## W-000725 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: phy_driver
- Explanation: phy_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mdiodrv', 'type': 'mdio_driver_common'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'name', 'type': '*mut core::ffi::c_char'}, {'name': 'phy_id_mask', 'type': 'u32_'}, {'name': 'features', 'type': '*const core::ffi::c_ulong'}, {'name': 'flags', 'type': 'u32_'}, {'name': 'driver_data', 'type': '*const core::ffi::c_void'}, {'name': 'get_rate_matching', 'type': '::core::option::Option<'}, {'name': 'remove', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device)>'}, {'name': 'set_wol', 'type': '::core::option::Option<'}, {'name': 'get_wol', 'type': '::core::option::Option<'}, {'name': 'link_change_notify', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device)>'}, {'name': 'read_mmd', 'type': '::core::option::Option<'}, {'name': 'write_mmd', 'type': '::core::option::Option<'}, {'name': 'write_page', 'type': '::core::option::Option<'}, {'name': 'module_info', 'type': '::core::option::Option<'}, {'name': 'module_eeprom', 'type': '::core::option::Option<'}, {'name': 'cable_test_tdr_start', 'type': '::core::option::Option<'}, {'name': 'cable_test_get_status', 'type': '::core::option::Option<'}, {'name': 'get_stats', 'type': '::core::option::Option<'}, {'name': 'get_tunable', 'type': '::core::option::Option<'}, {'name': 'set_tunable', 'type': '::core::option::Option<'}, {'name': 'set_loopback', 'type': '::core::option::Option<'}, {'name': 'get_plca_cfg', 'type': '::core::option::Option<'}, {'name': 'set_plca_cfg', 'type': '::core::option::Option<'}, {'name': 'get_plca_status', 'type': '::core::option::Option<'}, {'name': 'led_brightness_set', 'type': '::core::option::Option<'}, {'name': 'led_blink_set', 'type': '::core::option::Option<'}, {'name': 'led_hw_is_supported', 'type': '::core::option::Option<'}, {'name': 'led_hw_control_set', 'type': '::core::option::Option<'}, {'name': 'led_hw_control_get', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'mdiodrv', 'type': 'mdio_driver_common'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'name', 'type': '*mut core::ffi::c_char'}, {'name': 'phy_id_mask', 'type': 'u32_'}, {'name': 'features', 'type': '*const core::ffi::c_ulong'}, {'name': 'flags', 'type': 'u32_'}, {'name': 'driver_data', 'type': '*const core::ffi::c_void'}, {'name': 'get_rate_matching', 'type': '::core::option::Option<'}, {'name': 'remove', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device)>'}, {'name': 'set_wol', 'type': '::core::option::Option<'}, {'name': 'get_wol', 'type': '::core::option::Option<'}, {'name': 'link_change_notify', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device)>'}, {'name': 'read_mmd', 'type': '::core::option::Option<'}, {'name': 'write_mmd', 'type': '::core::option::Option<'}, {'name': 'write_page', 'type': '::core::option::Option<'}, {'name': 'module_info', 'type': '::core::option::Option<'}, {'name': 'module_eeprom', 'type': '::core::option::Option<'}, {'name': 'cable_test_tdr_start', 'type': '::core::option::Option<'}, {'name': 'cable_test_get_status', 'type': '::core::option::Option<'}, {'name': 'get_stats', 'type': '::core::option::Option<'}, {'name': 'get_tunable', 'type': '::core::option::Option<'}, {'name': 'set_tunable', 'type': '::core::option::Option<'}, {'name': 'set_loopback', 'type': '::core::option::Option<'}, {'name': 'get_plca_cfg', 'type': '::core::option::Option<'}, {'name': 'set_plca_cfg', 'type': '::core::option::Option<'}, {'name': 'get_plca_status', 'type': '::core::option::Option<'}, {'name': 'led_brightness_set', 'type': '::core::option::Option<'}, {'name': 'led_blink_set', 'type': '::core::option::Option<'}, {'name': 'led_hw_is_supported', 'type': '::core::option::Option<'}, {'name': 'led_hw_control_set', 'type': '::core::option::Option<'}, {'name': 'led_hw_control_get', 'type': '::core::option::Option<'}, {'name': 'led_polarity_set', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `25`

## W-000738 FieldDrift

- Risk: High
- Score: 12.4
- Symbol: taskstats
- Explanation: taskstats changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[{'name': 'version', 'type': '__u16'}, {'name': 'ac_exitcode', 'type': '__u32'}, {'name': 'ac_flag', 'type': '__u8'}, {'name': 'ac_nice', 'type': '__u8'}, {'name': 'cpu_count', 'type': '__u64'}, {'name': 'cpu_delay_total', 'type': '__u64'}, {'name': 'blkio_count', 'type': '__u64'}, {'name': 'blkio_delay_total', 'type': '__u64'}, {'name': 'swapin_count', 'type': '__u64'}, {'name': 'swapin_delay_total', 'type': '__u64'}, {'name': 'cpu_run_real_total', 'type': '__u64'}, {'name': 'cpu_run_virtual_total', 'type': '__u64'}, {'name': 'ac_comm', 'type': '[core::ffi::c_char; 32usize]'}, {'name': 'ac_sched', 'type': '__u8'}, {'name': 'ac_pad', 'type': '[__u8; 3usize]'}, {'name': '__bindgen_padding_0', 'type': 'u32'}, {'name': 'ac_uid', 'type': '__u32'}, {'name': 'ac_gid', 'type': '__u32'}, {'name': 'ac_pid', 'type': '__u32'}, {'name': 'ac_ppid', 'type': '__u32'}, {'name': 'ac_btime', 'type': '__u32'}, {'name': 'ac_etime', 'type': '__u64'}, {'name': 'ac_utime', 'type': '__u64'}, {'name': 'ac_stime', 'type': '__u64'}, {'name': 'ac_minflt', 'type': '__u64'}, {'name': 'ac_majflt', 'type': '__u64'}, {'name': 'coremem', 'type': '__u64'}, {'name': 'virtmem', 'type': '__u64'}, {'name': 'hiwater_rss', 'type': '__u64'}, {'name': 'hiwater_vm', 'type': '__u64'}, {'name': 'read_char', 'type': '__u64'}, {'name': 'write_char', 'type': '__u64'}, {'name': 'read_syscalls', 'type': '__u64'}, {'name': 'write_syscalls', 'type': '__u64'}, {'name': 'read_bytes', 'type': '__u64'}, {'name': 'write_bytes', 'type': '__u64'}, {'name': 'cancelled_write_bytes', 'type': '__u64'}, {'name': 'nvcsw', 'type': '__u64'}, {'name': 'nivcsw', 'type': '__u64'}, {'name': 'ac_utimescaled', 'type': '__u64'}, {'name': 'ac_stimescaled', 'type': '__u64'}, {'name': 'cpu_scaled_run_real_total', 'type': '__u64'}, {'name': 'freepages_count', 'type': '__u64'}, {'name': 'freepages_delay_total', 'type': '__u64'}, {'name': 'thrashing_count', 'type': '__u64'}, {'name': 'thrashing_delay_total', 'type': '__u64'}, {'name': 'ac_btime64', 'type': '__u64'}, {'name': 'compact_count', 'type': '__u64'}, {'name': 'compact_delay_total', 'type': '__u64'}, {'name': 'ac_tgid', 'type': '__u32'}, {'name': 'ac_tgetime', 'type': '__u64'}, {'name': 'ac_exe_dev', 'type': '__u64'}, {'name': 'ac_exe_inode', 'type': '__u64'}, {'name': 'wpcopy_count', 'type': '__u64'}, {'name': 'wpcopy_delay_total', 'type': '__u64'}, {'name': 'irq_count', 'type': '__u64'}, {'name': 'irq_delay_total', 'type': '__u64'}]`

### Rust Evidence

- Graph edges: `19`

## W-000727 FieldDrift

- Risk: High
- Score: 12.2
- Symbol: pid
- Explanation: pid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'count', 'type': 'refcount_t'}, {'name': 'level', 'type': 'core::ffi::c_uint'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'tasks', 'type': '[hlist_head; 4usize]'}, {'name': 'inodes', 'type': 'hlist_head'}, {'name': 'wait_pidfd', 'type': 'wait_queue_head_t'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'numbers', 'type': '__IncompleteArrayField<upid>'}]`
- New: `[{'name': 'count', 'type': 'refcount_t'}, {'name': 'level', 'type': 'core::ffi::c_uint'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'stashed', 'type': '*mut dentry'}, {'name': 'ino', 'type': 'u64_'}, {'name': 'tasks', 'type': '[hlist_head; 4usize]'}, {'name': 'inodes', 'type': 'hlist_head'}, {'name': 'wait_pidfd', 'type': 'wait_queue_head_t'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'numbers', 'type': '__IncompleteArrayField<upid>'}]`

### Rust Evidence

- Graph edges: `18`

## W-000485 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: nmi
- Explanation: nmi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000718 FieldDrift

- Risk: High
- Score: 12.0
- Symbol: kernfs_node
- Explanation: kernfs_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'count', 'type': 'atomic_t'}, {'name': 'active', 'type': 'atomic_t'}, {'name': 'parent', 'type': '*mut kernfs_node'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'rb', 'type': 'rb_node'}, {'name': 'ns', 'type': '*const core::ffi::c_void'}, {'name': 'hash', 'type': 'core::ffi::c_uint'}, {'name': '__bindgen_anon_1', 'type': 'kernfs_node__bindgen_ty_1'}, {'name': 'priv_', 'type': '*mut core::ffi::c_void'}, {'name': 'id', 'type': 'u64_'}, {'name': 'flags', 'type': 'core::ffi::c_ushort'}, {'name': 'mode', 'type': 'umode_t'}, {'name': 'iattr', 'type': '*mut kernfs_iattrs'}]`
- New: `[{'name': 'count', 'type': 'atomic_t'}, {'name': 'active', 'type': 'atomic_t'}, {'name': 'parent', 'type': '*mut kernfs_node'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'rb', 'type': 'rb_node'}, {'name': 'ns', 'type': '*const core::ffi::c_void'}, {'name': 'hash', 'type': 'core::ffi::c_uint'}, {'name': 'flags', 'type': 'core::ffi::c_ushort'}, {'name': 'mode', 'type': 'umode_t'}, {'name': '__bindgen_anon_1', 'type': 'kernfs_node__bindgen_ty_1'}, {'name': 'id', 'type': 'u64_'}, {'name': 'priv_', 'type': '*mut core::ffi::c_void'}, {'name': 'iattr', 'type': '*mut kernfs_iattrs'}, {'name': 'rcu', 'type': 'callback_head'}]`

### Rust Evidence

- Graph edges: `17`

## W-000059 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: arch_cpu_idle
- Explanation: arch_cpu_idle changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000160 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: btf_get
- Explanation: btf_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000566 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: seq_hlist_start
- Explanation: seq_hlist_start changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000206 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: cgroup_free
- Explanation: cgroup_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000573 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: seq_list_start
- Explanation: seq_list_start changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000732 FieldDrift

- Risk: High
- Score: 11.4
- Symbol: sk_buff
- Explanation: sk_buff changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'sk_buff__bindgen_ty_1'}, {'name': '__bindgen_anon_2', 'type': 'sk_buff__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'sk_buff__bindgen_ty_3'}, {'name': 'cb', 'type': '[core::ffi::c_char; 48usize]'}, {'name': '__bindgen_anon_4', 'type': 'sk_buff__bindgen_ty_4'}, {'name': '_nfct', 'type': 'core::ffi::c_ulong'}, {'name': 'len', 'type': 'core::ffi::c_uint'}, {'name': 'data_len', 'type': 'core::ffi::c_uint'}, {'name': 'mac_len', 'type': '__u16'}, {'name': 'hdr_len', 'type': '__u16'}, {'name': 'queue_mapping', 'type': '__u16'}, {'name': '__cloned_offset', 'type': '__IncompleteArrayField<__u8>'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'active_extensions', 'type': '__u8'}, {'name': '__bindgen_anon_5', 'type': 'sk_buff__bindgen_ty_5'}, {'name': 'tail', 'type': 'sk_buff_data_t'}, {'name': 'end', 'type': 'sk_buff_data_t'}, {'name': 'head', 'type': '*mut core::ffi::c_uchar'}, {'name': 'data', 'type': '*mut core::ffi::c_uchar'}, {'name': 'truesize', 'type': 'core::ffi::c_uint'}, {'name': 'users', 'type': 'refcount_t'}, {'name': 'extensions', 'type': '*mut skb_ext'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'sk_buff__bindgen_ty_1'}, {'name': 'sk', 'type': '*mut sock'}, {'name': '__bindgen_anon_2', 'type': 'sk_buff__bindgen_ty_2'}, {'name': 'cb', 'type': '[core::ffi::c_char; 48usize]'}, {'name': '__bindgen_anon_3', 'type': 'sk_buff__bindgen_ty_3'}, {'name': '_nfct', 'type': 'core::ffi::c_ulong'}, {'name': 'len', 'type': 'core::ffi::c_uint'}, {'name': 'data_len', 'type': 'core::ffi::c_uint'}, {'name': 'mac_len', 'type': '__u16'}, {'name': 'hdr_len', 'type': '__u16'}, {'name': 'queue_mapping', 'type': '__u16'}, {'name': '__cloned_offset', 'type': '__IncompleteArrayField<__u8>'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'active_extensions', 'type': '__u8'}, {'name': '__bindgen_anon_4', 'type': 'sk_buff__bindgen_ty_4'}, {'name': 'tail', 'type': 'sk_buff_data_t'}, {'name': 'end', 'type': 'sk_buff_data_t'}, {'name': 'head', 'type': '*mut core::ffi::c_uchar'}, {'name': 'data', 'type': '*mut core::ffi::c_uchar'}, {'name': 'truesize', 'type': 'core::ffi::c_uint'}, {'name': 'users', 'type': 'refcount_t'}, {'name': 'extensions', 'type': '*mut skb_ext'}]`

### Rust Evidence

- Graph edges: `14`

## W-000125 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: bpf_prog_array_copy
- Explanation: bpf_prog_array_copy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000207 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: cgroup_freeze
- Explanation: cgroup_freeze changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000223 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: cgroup_rstat_flush
- Explanation: cgroup_rstat_flush changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000405 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: kallsyms_lookup
- Explanation: kallsyms_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000420 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: kstrdup_quotable
- Explanation: kstrdup_quotable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000563 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: seq_hlist_next
- Explanation: seq_hlist_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000619 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: sprint_symbol
- Explanation: sprint_symbol changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000644 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: tasklet_unlock
- Explanation: tasklet_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000003 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __bpf_dynptr_data
- Explanation: __bpf_dynptr_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000012 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __cgroup_account_cputime
- Explanation: __cgroup_account_cputime changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000014 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __cpuhp_remove_state
- Explanation: __cpuhp_remove_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000016 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __cpuhp_setup_state
- Explanation: __cpuhp_setup_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000018 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __cpuhp_state_add_instance
- Explanation: __cpuhp_state_add_instance changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000023 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __fprop_add_percpu
- Explanation: __fprop_add_percpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000030 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __register_one_node
- Explanation: __register_one_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000088 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: balance_dirty_pages_ratelimited
- Explanation: balance_dirty_pages_ratelimited changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000128 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: bpf_prog_array_delete_safe
- Explanation: bpf_prog_array_delete_safe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000130 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: bpf_prog_array_free
- Explanation: bpf_prog_array_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000180 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: btf_type_seq_show
- Explanation: btf_type_seq_show changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000213 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: cgroup_init
- Explanation: cgroup_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000240 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: cpu_add_dev_attr
- Explanation: cpu_add_dev_attr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000254 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: cpu_remove_dev_attr
- Explanation: cpu_remove_dev_attr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000308 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: disable_irq
- Explanation: disable_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000334 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: extra
- Explanation: extra changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000394 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: irq_set_affinity
- Explanation: irq_set_affinity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000424 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: kthread_bind
- Explanation: kthread_bind changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000432 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: kthread_create_worker
- Explanation: kthread_create_worker changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000438 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: kthread_flush_work
- Explanation: kthread_flush_work changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000444 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: kthread_park
- Explanation: kthread_park changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000451 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: kthread_should_stop
- Explanation: kthread_should_stop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000453 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: kthread_stop
- Explanation: kthread_stop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000492 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: nr_context_switches
- Explanation: nr_context_switches changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000496 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: offset
- Explanation: offset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000524 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: raise_softirq
- Explanation: raise_softirq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000531 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: register_cpu
- Explanation: register_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000567 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: seq_hlist_start_head
- Explanation: seq_hlist_start_head changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000571 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: seq_list_next
- Explanation: seq_list_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000574 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: seq_list_start_head
- Explanation: seq_list_start_head changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000578 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: seq_open
- Explanation: seq_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000581 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: seq_path
- Explanation: seq_path changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000585 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: seq_put_decimal_ull
- Explanation: seq_put_decimal_ull changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000590 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: seq_read
- Explanation: seq_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000592 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: seq_release
- Explanation: seq_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000603 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: single_open
- Explanation: single_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000617 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: sprint_backtrace
- Explanation: sprint_backtrace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000629 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: sti
- Explanation: sti changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000650 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: text_poke_copy
- Explanation: text_poke_copy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000674 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: unregister_cpu
- Explanation: unregister_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000685 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: wakeup_flusher_threads
- Explanation: wakeup_flusher_threads changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000696 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: writeback_inodes_sb
- Explanation: writeback_inodes_sb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000002 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __bitmap_weight_andnot
- Explanation: __bitmap_weight_andnot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000004 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __bpf_dynptr_data_rw
- Explanation: __bpf_dynptr_data_rw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000005 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __bpf_dynptr_size
- Explanation: __bpf_dynptr_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000006 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __bpf_free_used_btfs
- Explanation: __bpf_free_used_btfs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000007 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __bpf_free_used_maps
- Explanation: __bpf_free_used_maps changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000008 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __bpf_prog_enter_sleepable_recur
- Explanation: __bpf_prog_enter_sleepable_recur changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000009 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __bpf_prog_exit_sleepable_recur
- Explanation: __bpf_prog_exit_sleepable_recur changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000010 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __bpf_tramp_enter
- Explanation: __bpf_tramp_enter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000011 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __bpf_tramp_exit
- Explanation: __bpf_tramp_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000013 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __cgroup_account_cputime_field
- Explanation: __cgroup_account_cputime_field changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000015 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __cpuhp_remove_state_cpuslocked
- Explanation: __cpuhp_remove_state_cpuslocked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000017 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __cpuhp_setup_state_cpuslocked
- Explanation: __cpuhp_setup_state_cpuslocked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000019 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __cpuhp_state_add_instance_cpuslocked
- Explanation: __cpuhp_state_add_instance_cpuslocked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000020 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __cpuhp_state_remove_instance
- Explanation: __cpuhp_state_remove_instance changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000021 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __do_softirq
- Explanation: __do_softirq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000022 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __folio_batch_release
- Explanation: __folio_batch_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000024 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __fprop_add_percpu_max
- Explanation: __fprop_add_percpu_max changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000025 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __handle_irq
- Explanation: __handle_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000026 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __irq_apply_affinity_hint
- Explanation: __irq_apply_affinity_hint changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000027 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kthread_init_worker
- Explanation: __kthread_init_worker changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000028 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __page_frag_alloc_align
- Explanation: __page_frag_alloc_align changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000029 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __raise_softirq_irqoff
- Explanation: __raise_softirq_irqoff changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000031 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __request_percpu_irq
- Explanation: __request_percpu_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000032 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __seq_open_private
- Explanation: __seq_open_private changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000033 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __stack_depot_get_stack_record
- Explanation: __stack_depot_get_stack_record changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000034 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __static_call_fixup
- Explanation: __static_call_fixup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000035 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __static_call_return0
- Explanation: __static_call_return0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000036 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __static_call_update
- Explanation: __static_call_update changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000037 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __tasklet_hi_schedule
- Explanation: __tasklet_hi_schedule changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000038 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __tasklet_schedule
- Explanation: __tasklet_schedule changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000039 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __warn_thunk
- Explanation: __warn_thunk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000040 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: account_guest_time
- Explanation: account_guest_time changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000041 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: account_idle_ticks
- Explanation: account_idle_ticks changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000042 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: account_idle_time
- Explanation: account_idle_time changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000043 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: account_process_tick
- Explanation: account_process_tick changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000044 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: account_steal_time
- Explanation: account_steal_time changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000045 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: account_system_index_time
- Explanation: account_system_index_time changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000046 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: account_system_time
- Explanation: account_system_time changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000047 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: account_user_time
- Explanation: account_user_time changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000048 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: add_cpu
- Explanation: add_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000049 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: add_timer_global
- Explanation: add_timer_global changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000050 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: add_timer_local
- Explanation: add_timer_local changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000052 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_file_pseudo_noaccount
- Explanation: alloc_file_pseudo_noaccount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000053 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_ucounts
- Explanation: alloc_ucounts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000055 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: apply_relocation
- Explanation: apply_relocation changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000056 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_alloc_bpf_trampoline
- Explanation: arch_alloc_bpf_trampoline changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000057 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_bpf_trampoline_size
- Explanation: arch_bpf_trampoline_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000058 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_cpu_finalize_init
- Explanation: arch_cpu_finalize_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000060 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_cpu_idle_dead
- Explanation: arch_cpu_idle_dead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000061 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_cpu_idle_enter
- Explanation: arch_cpu_idle_enter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000062 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_cpu_idle_exit
- Explanation: arch_cpu_idle_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000063 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_cpu_idle_prepare
- Explanation: arch_cpu_idle_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000064 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_cpu_is_hotpluggable
- Explanation: arch_cpu_is_hotpluggable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000065 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_cpu_probe
- Explanation: arch_cpu_probe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000066 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_cpu_release
- Explanation: arch_cpu_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000067 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_cpuhp_cleanup_dead_cpu
- Explanation: arch_cpuhp_cleanup_dead_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000068 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_cpuhp_cleanup_kick_cpu
- Explanation: arch_cpuhp_cleanup_kick_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000069 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_cpuhp_init_parallel_bringup
- Explanation: arch_cpuhp_init_parallel_bringup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000070 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_cpuhp_kick_ap_alive
- Explanation: arch_cpuhp_kick_ap_alive changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000071 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_cpuhp_sync_state_poll
- Explanation: arch_cpuhp_sync_state_poll changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000072 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_early_irq_init
- Explanation: arch_early_irq_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000073 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_find_n_match_cpu_physical_id
- Explanation: arch_find_n_match_cpu_physical_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000074 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_free_bpf_trampoline
- Explanation: arch_free_bpf_trampoline changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000075 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_match_cpu_phys_id
- Explanation: arch_match_cpu_phys_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000076 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_prepare_bpf_trampoline
- Explanation: arch_prepare_bpf_trampoline changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000077 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_probe_nr_irqs
- Explanation: arch_probe_nr_irqs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000078 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_protect_bpf_trampoline
- Explanation: arch_protect_bpf_trampoline changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000079 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_register_cpu
- Explanation: arch_register_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000080 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_show_interrupts
- Explanation: arch_show_interrupts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000081 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_static_call_transform
- Explanation: arch_static_call_transform changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000082 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_tick_broadcast_enter
- Explanation: arch_tick_broadcast_enter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000083 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_tick_broadcast_exit
- Explanation: arch_tick_broadcast_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000084 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_trigger_cpumask_backtrace
- Explanation: arch_trigger_cpumask_backtrace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000085 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_unprotect_bpf_trampoline
- Explanation: arch_unprotect_bpf_trampoline changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000086 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_unregister_cpu
- Explanation: arch_unregister_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000087 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: async_suspend
- Explanation: async_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(1usize, 1u8) as u32) } } #[inline] pub fn set_async_suspend(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(1usize, 1u8) as u8) } } #[inline] pub fn set_async_suspend(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000089 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: balance_dirty_pages_ratelimited_flags
- Explanation: balance_dirty_pages_ratelimited_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000090 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blinded
- Explanation: blinded changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000091 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blinding_requested
- Explanation: blinding_requested changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000092 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: boot_cpu_hotplug_init
- Explanation: boot_cpu_hotplug_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000093 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: boot_cpu_init
- Explanation: boot_cpu_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000094 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_arch_poke_desc_update
- Explanation: bpf_arch_poke_desc_update changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000095 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_arch_text_copy
- Explanation: bpf_arch_text_copy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000096 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_arch_text_invalidate
- Explanation: bpf_arch_text_invalidate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000097 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_arch_text_poke
- Explanation: bpf_arch_text_poke changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000098 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_arena_get_kern_vm_start
- Explanation: bpf_arena_get_kern_vm_start changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000099 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_arena_get_user_vm_start
- Explanation: bpf_arena_get_user_vm_start changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000100 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_bprintf_cleanup
- Explanation: bpf_bprintf_cleanup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000101 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_bprintf_prepare
- Explanation: bpf_bprintf_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000102 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_dynptr_check_size
- Explanation: bpf_dynptr_check_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000103 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_dynptr_from_skb_rdonly
- Explanation: bpf_dynptr_from_skb_rdonly changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000104 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_event_output
- Explanation: bpf_event_output changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000105 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_find_btf_id
- Explanation: bpf_find_btf_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000106 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_get_raw_cpu_id
- Explanation: bpf_get_raw_cpu_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000107 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_get_trace_printk_proto
- Explanation: bpf_get_trace_printk_proto changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000108 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_get_trace_vprintk_proto
- Explanation: bpf_get_trace_vprintk_proto changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000109 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_list_head_free
- Explanation: bpf_list_head_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000110 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_map_meta_equal
- Explanation: bpf_map_meta_equal changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000111 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_map_offload_delete_elem
- Explanation: bpf_map_offload_delete_elem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000112 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_map_offload_get_next_key
- Explanation: bpf_map_offload_get_next_key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000113 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_map_offload_info_fill
- Explanation: bpf_map_offload_info_fill changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000114 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_map_offload_lookup_elem
- Explanation: bpf_map_offload_lookup_elem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000115 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_map_offload_update_elem
- Explanation: bpf_map_offload_update_elem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000116 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_obj_name_cpy
- Explanation: bpf_obj_name_cpy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000117 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_offload_dev_create
- Explanation: bpf_offload_dev_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000118 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_offload_dev_destroy
- Explanation: bpf_offload_dev_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000119 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_offload_dev_match
- Explanation: bpf_offload_dev_match changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000120 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_offload_dev_netdev_register
- Explanation: bpf_offload_dev_netdev_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000121 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_offload_dev_netdev_unregister
- Explanation: bpf_offload_dev_netdev_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000122 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_offload_dev_priv
- Explanation: bpf_offload_dev_priv changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000123 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_offload_prog_map_match
- Explanation: bpf_offload_prog_map_match changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000124 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_prog_array_alloc
- Explanation: bpf_prog_array_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000126 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_prog_array_copy_info
- Explanation: bpf_prog_array_copy_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000127 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_prog_array_copy_to_user
- Explanation: bpf_prog_array_copy_to_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000129 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_prog_array_delete_safe_at
- Explanation: bpf_prog_array_delete_safe_at changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000131 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_prog_array_free_sleepable
- Explanation: bpf_prog_array_free_sleepable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000132 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_prog_array_is_empty
- Explanation: bpf_prog_array_is_empty changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000133 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_prog_array_length
- Explanation: bpf_prog_array_length changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000134 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_prog_array_update_at
- Explanation: bpf_prog_array_update_at changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000135 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_prog_calc_tag
- Explanation: bpf_prog_calc_tag changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000136 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_prog_dev_bound_destroy
- Explanation: bpf_prog_dev_bound_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000137 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_prog_get_ok
- Explanation: bpf_prog_get_ok changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000138 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_prog_map_compatible
- Explanation: bpf_prog_map_compatible changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000139 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_prog_offload_compile
- Explanation: bpf_prog_offload_compile changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000140 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_prog_offload_info_fill
- Explanation: bpf_prog_offload_info_fill changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000141 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_rb_root_free
- Explanation: bpf_rb_root_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000142 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_sock_common_is_valid_access
- Explanation: bpf_sock_common_is_valid_access changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000143 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_sock_convert_ctx_access
- Explanation: bpf_sock_convert_ctx_access changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000144 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_sock_is_valid_access
- Explanation: bpf_sock_is_valid_access changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000145 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_tcp_sock_convert_ctx_access
- Explanation: bpf_tcp_sock_convert_ctx_access changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000146 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_tcp_sock_is_valid_access
- Explanation: bpf_tcp_sock_is_valid_access changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000147 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_timer_cancel_and_free
- Explanation: bpf_timer_cancel_and_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000148 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_trampoline_enter
- Explanation: bpf_trampoline_enter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000149 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_trampoline_exit
- Explanation: bpf_trampoline_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000150 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_user_rnd_init_once
- Explanation: bpf_user_rnd_init_once changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000151 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_user_rnd_u32
- Explanation: bpf_user_rnd_u32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000152 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_xdp_sock_convert_ctx_access
- Explanation: bpf_xdp_sock_convert_ctx_access changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000153 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_xdp_sock_is_valid_access
- Explanation: bpf_xdp_sock_is_valid_access changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000154 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bringup_hibernate_cpu
- Explanation: bringup_hibernate_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000155 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bringup_nonboot_cpus
- Explanation: bringup_nonboot_cpus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000156 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bsearch
- Explanation: bsearch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000157 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_check_and_fixup_fields
- Explanation: btf_check_and_fixup_fields changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000158 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_ctx_arg_offset
- Explanation: btf_ctx_arg_offset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000159 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_find_by_name_kind
- Explanation: btf_find_by_name_kind changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000161 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_get_by_fd
- Explanation: btf_get_by_fd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000162 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_get_fd_by_id
- Explanation: btf_get_fd_by_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000163 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_get_info_by_fd
- Explanation: btf_get_info_by_fd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000164 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_get_name
- Explanation: btf_get_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000165 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_is_kernel
- Explanation: btf_is_kernel changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000166 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_is_module
- Explanation: btf_is_module changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000167 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_member_is_reg_int
- Explanation: btf_member_is_reg_int changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000168 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_new_fd
- Explanation: btf_new_fd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000169 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_nr_types
- Explanation: btf_nr_types changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000170 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_obj_id
- Explanation: btf_obj_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000171 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_param_match_suffix
- Explanation: btf_param_match_suffix changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000172 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_parse_fields
- Explanation: btf_parse_fields changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000173 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_put
- Explanation: btf_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000174 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_resolve_size
- Explanation: btf_resolve_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000175 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_try_get_module
- Explanation: btf_try_get_module changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000176 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_type_id_size
- Explanation: btf_type_id_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000177 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_type_is_void
- Explanation: btf_type_is_void changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000178 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_type_resolve_func_ptr
- Explanation: btf_type_resolve_func_ptr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000179 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_type_resolve_ptr
- Explanation: btf_type_resolve_ptr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000181 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_type_seq_show_flags
- Explanation: btf_type_seq_show_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000182 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_type_skip_modifiers
- Explanation: btf_type_skip_modifiers changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000183 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_type_snprintf_show
- Explanation: btf_type_snprintf_show changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000184 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_type_str
- Explanation: btf_type_str changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000187 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: call_get_func_ip
- Explanation: call_get_func_ip changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000188 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: call_get_stack
- Explanation: call_get_stack changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000189 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: called
- Explanation: called changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000193 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: can_wakeup
- Explanation: can_wakeup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(0usize, 1u8) as u32) } } #[inline] pub fn set_can_wakeup(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(0usize, 1u8) as u8) } } #[inline] pub fn set_can_wakeup(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000194 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cb_access
- Explanation: cb_access changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000195 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_add_dfl_cftypes
- Explanation: cgroup_add_dfl_cftypes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000196 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_add_legacy_cftypes
- Explanation: cgroup_add_legacy_cftypes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000197 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_attach_task_all
- Explanation: cgroup_attach_task_all changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000198 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_can_fork
- Explanation: cgroup_can_fork changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000199 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_cancel_fork
- Explanation: cgroup_cancel_fork changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000200 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_e_css
- Explanation: cgroup_e_css changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000201 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_enter_frozen
- Explanation: cgroup_enter_frozen changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000202 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_exit
- Explanation: cgroup_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000203 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_file_notify
- Explanation: cgroup_file_notify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000204 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_file_show
- Explanation: cgroup_file_show changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000205 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_fork
- Explanation: cgroup_fork changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000208 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_freezer_migrate_task
- Explanation: cgroup_freezer_migrate_task changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000209 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_get_e_css
- Explanation: cgroup_get_e_css changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000210 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_get_from_fd
- Explanation: cgroup_get_from_fd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000211 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_get_from_id
- Explanation: cgroup_get_from_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000212 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_get_from_path
- Explanation: cgroup_get_from_path changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000214 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_init_early
- Explanation: cgroup_init_early changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000215 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_leave_frozen
- Explanation: cgroup_leave_frozen changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000216 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_parse_float
- Explanation: cgroup_parse_float changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000217 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_path_from_kernfs_id
- Explanation: cgroup_path_from_kernfs_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000218 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_path_ns
- Explanation: cgroup_path_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000219 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_post_fork
- Explanation: cgroup_post_fork changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000220 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_psi_enabled
- Explanation: cgroup_psi_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000221 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_release
- Explanation: cgroup_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000222 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_rm_cftypes
- Explanation: cgroup_rm_cftypes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000224 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_rstat_flush_hold
- Explanation: cgroup_rstat_flush_hold changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000225 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_rstat_flush_release
- Explanation: cgroup_rstat_flush_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000226 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_rstat_updated
- Explanation: cgroup_rstat_updated changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000227 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_sk_alloc
- Explanation: cgroup_sk_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000228 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_sk_clone
- Explanation: cgroup_sk_clone changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000229 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_sk_free
- Explanation: cgroup_sk_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000230 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_taskset_first
- Explanation: cgroup_taskset_first changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000231 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_taskset_next
- Explanation: cgroup_taskset_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000232 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_transfer_tasks
- Explanation: cgroup_transfer_tasks changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000233 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_update_frozen
- Explanation: cgroup_update_frozen changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000234 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_v1v2_get_from_fd
- Explanation: cgroup_v1v2_get_from_fd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000235 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroupstats_build
- Explanation: cgroupstats_build changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000236 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: clear_bhb_loop
- Explanation: clear_bhb_loop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000237 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: clear_tasks_mm_cpumask
- Explanation: clear_tasks_mm_cpumask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000238 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_cgroup_ns
- Explanation: copy_cgroup_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000239 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_map_value_locked
- Explanation: copy_map_value_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000241 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_add_dev_attr_group
- Explanation: cpu_add_dev_attr_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000242 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_device_create
- Explanation: cpu_device_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000243 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_device_down
- Explanation: cpu_device_down changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000244 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_device_up
- Explanation: cpu_device_up changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000245 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_hotplug_disable
- Explanation: cpu_hotplug_disable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000246 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_hotplug_enable
- Explanation: cpu_hotplug_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000247 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_idle_poll_ctrl
- Explanation: cpu_idle_poll_ctrl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000248 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_in_idle
- Explanation: cpu_in_idle changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000249 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_is_hotpluggable
- Explanation: cpu_is_hotpluggable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000250 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_maps_update_begin
- Explanation: cpu_maps_update_begin changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000251 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_maps_update_done
- Explanation: cpu_maps_update_done changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000252 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_mitigations_auto_nosmt
- Explanation: cpu_mitigations_auto_nosmt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000253 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_mitigations_off
- Explanation: cpu_mitigations_off changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000255 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_remove_dev_attr_group
- Explanation: cpu_remove_dev_attr_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000256 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_show_gds
- Explanation: cpu_show_gds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000257 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_show_itlb_multihit
- Explanation: cpu_show_itlb_multihit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000258 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_show_l1tf
- Explanation: cpu_show_l1tf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000259 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_show_mds
- Explanation: cpu_show_mds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000260 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_show_meltdown
- Explanation: cpu_show_meltdown changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000261 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_show_mmio_stale_data
- Explanation: cpu_show_mmio_stale_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000262 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_show_reg_file_data_sampling
- Explanation: cpu_show_reg_file_data_sampling changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000263 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_show_retbleed
- Explanation: cpu_show_retbleed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000264 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_show_spec_rstack_overflow
- Explanation: cpu_show_spec_rstack_overflow changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000265 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_show_spec_store_bypass
- Explanation: cpu_show_spec_store_bypass changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000266 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_show_spectre_v1
- Explanation: cpu_show_spectre_v1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000267 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_show_spectre_v2
- Explanation: cpu_show_spectre_v2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000268 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_show_srbds
- Explanation: cpu_show_srbds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000269 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_show_tsx_async_abort
- Explanation: cpu_show_tsx_async_abort changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000270 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_startup_entry
- Explanation: cpu_startup_entry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000271 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpuacct_account_field
- Explanation: cpuacct_account_field changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000272 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpuacct_charge
- Explanation: cpuacct_charge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000273 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpuhp_ap_report_dead
- Explanation: cpuhp_ap_report_dead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000274 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpuhp_ap_sync_alive
- Explanation: cpuhp_ap_sync_alive changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000275 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpuhp_online_idle
- Explanation: cpuhp_online_idle changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000276 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpuhp_report_idle_dead
- Explanation: cpuhp_report_idle_dead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000277 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpus_equal_capacity
- Explanation: cpus_equal_capacity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000278 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpus_read_lock
- Explanation: cpus_read_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000279 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpus_read_trylock
- Explanation: cpus_read_trylock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000280 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpus_read_unlock
- Explanation: cpus_read_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000281 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpus_write_lock
- Explanation: cpus_write_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000282 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpus_write_unlock
- Explanation: cpus_write_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000284 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: css_from_id
- Explanation: css_from_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000285 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: css_has_online_children
- Explanation: css_has_online_children changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000286 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: css_next_child
- Explanation: css_next_child changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000287 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: css_next_descendant_post
- Explanation: css_next_descendant_post changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000288 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: css_next_descendant_pre
- Explanation: css_next_descendant_pre changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000289 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: css_rightmost_descendant
- Explanation: css_rightmost_descendant changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000290 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: css_task_iter_end
- Explanation: css_task_iter_end changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000291 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: css_task_iter_next
- Explanation: css_task_iter_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000292 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: css_task_iter_start
- Explanation: css_task_iter_start changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000293 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: css_tryget_online_from_dir
- Explanation: css_tryget_online_from_dir changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000294 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dec_rlimit_put_ucounts
- Explanation: dec_rlimit_put_ucounts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000295 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dec_rlimit_ucounts
- Explanation: dec_rlimit_ucounts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000296 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dec_ucount
- Explanation: dec_ucount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000299 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: deferred_resume
- Explanation: deferred_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_3.get(5usize, 1u8) as u32) } } #[inline] pub fn set_deferred_resume(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_3.get(5usize, 1u8) as u8) } } #[inline] pub fn set_deferred_resume(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000300 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_link_wait_removal
- Explanation: device_link_wait_removal changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000301 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_free_irq
- Explanation: devm_free_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000302 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_kasprintf_strarray
- Explanation: devm_kasprintf_strarray changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000303 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_of_phy_package_join
- Explanation: devm_of_phy_package_join changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000304 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_request_any_context_irq
- Explanation: devm_request_any_context_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000305 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_request_threaded_irq
- Explanation: devm_request_threaded_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000306 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dirtytime_interval_handler
- Explanation: dirtytime_interval_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000307 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: disable_hardirq
- Explanation: disable_hardirq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000309 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: disable_irq_nosync
- Explanation: disable_irq_nosync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000310 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: disable_nmi_nosync
- Explanation: disable_nmi_nosync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000311 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: disable_percpu_irq
- Explanation: disable_percpu_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000312 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: disable_percpu_nmi
- Explanation: disable_percpu_nmi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000313 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_notify_pidfd
- Explanation: do_notify_pidfd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000314 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_softirq
- Explanation: do_softirq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000315 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_writepages
- Explanation: do_writepages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000316 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dst_needed
- Explanation: dst_needed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000317 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dst_reg
- Explanation: dst_reg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000318 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dump_page
- Explanation: dump_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'page', 'type': '*mut page'}, {'name': 'reason', 'type': '*const core::ffi::c_char'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'page', 'type': '*const page'}, {'name': 'reason', 'type': '*const core::ffi::c_char'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000319 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: early_init
- Explanation: early_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(8usize, 1u8) as u8) } } #[inline] pub fn set_early_init(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(0usize, 1u8) as u8) } } #[inline] pub fn set_early_init(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000320 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: early_irq_init
- Explanation: early_irq_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000321 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: enable_irq
- Explanation: enable_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000322 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: enable_nmi
- Explanation: enable_nmi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000323 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: enable_percpu_irq
- Explanation: enable_percpu_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000324 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: enable_percpu_nmi
- Explanation: enable_percpu_nmi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000325 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: enclave
- Explanation: enclave changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000326 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: enforce_expected_attach_type
- Explanation: enforce_expected_attach_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000327 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: eventfd_ctx_do_read
- Explanation: eventfd_ctx_do_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000328 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: eventfd_ctx_fdget
- Explanation: eventfd_ctx_fdget changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000329 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: eventfd_ctx_fileget
- Explanation: eventfd_ctx_fileget changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000330 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: eventfd_ctx_put
- Explanation: eventfd_ctx_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000331 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: eventfd_ctx_remove_wait_queue
- Explanation: eventfd_ctx_remove_wait_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000332 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: eventfd_fget
- Explanation: eventfd_fget changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000333 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: eventfd_signal_mask
- Explanation: eventfd_signal_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000335 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: file_remove_privs_flags
- Explanation: file_remove_privs_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000336 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_dirty_folio
- Explanation: filemap_dirty_folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000337 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fixup_irqs
- Explanation: fixup_irqs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000338 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_batch_remove_exceptionals
- Explanation: folio_batch_remove_exceptionals changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000339 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_redirty_for_writepage
- Explanation: folio_redirty_for_writepage changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000340 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folios_put_refs
- Explanation: folios_put_refs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000341 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: for_background
- Explanation: for_background changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000342 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: for_kupdate
- Explanation: for_kupdate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000343 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: for_reclaim
- Explanation: for_reclaim changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000344 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: for_sync
- Explanation: for_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000345 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fprop_fraction_percpu
- Explanation: fprop_fraction_percpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000346 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fprop_global_destroy
- Explanation: fprop_global_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000347 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fprop_global_init
- Explanation: fprop_global_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000348 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fprop_local_destroy_percpu
- Explanation: fprop_local_destroy_percpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000349 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fprop_local_init_percpu
- Explanation: fprop_local_init_percpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000350 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fprop_new_period
- Explanation: fprop_new_period changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000351 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_cgroup_ns
- Explanation: free_cgroup_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000352 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_irq
- Explanation: free_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000353 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_kthread_struct
- Explanation: free_kthread_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000354 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_nmi
- Explanation: free_nmi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000355 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_percpu_irq
- Explanation: free_percpu_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000356 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_percpu_nmi
- Explanation: free_percpu_nmi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000357 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: freeze_secondary_cpus
- Explanation: freeze_secondary_cpus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000358 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_link_add
- Explanation: fwnode_link_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'con', 'type': '*mut fwnode_handle'}, {'name': 'sup', 'type': '*mut fwnode_handle'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'con', 'type': '*mut fwnode_handle'}, {'name': 'sup', 'type': '*mut fwnode_handle'}, {'name': 'flags', 'type': 'u8_'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000361 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_set_sb_d_ops
- Explanation: generic_set_sb_d_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000362 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c37_read_status
- Explanation: genphy_c37_read_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'changed', 'type': '*mut bool_'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000363 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_ethtool_get_eee
- Explanation: genphy_c45_ethtool_get_eee changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'data', 'type': '*mut ethtool_eee'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'data', 'type': '*mut ethtool_keee'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000364 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_ethtool_set_eee
- Explanation: genphy_c45_ethtool_set_eee changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'data', 'type': '*mut ethtool_eee'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'data', 'type': '*mut ethtool_keee'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000365 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_cpu_device
- Explanation: get_cpu_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000366 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_idle_time
- Explanation: get_idle_time changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000367 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_kthread_comm
- Explanation: get_kthread_comm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000368 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_ucounts
- Explanation: get_ucounts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000369 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: global_dirty_limits
- Explanation: global_dirty_limits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000371 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpl_compatible
- Explanation: gpl_compatible changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000372 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: has_callchain_buf
- Explanation: has_callchain_buf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000373 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: idle_notification
- Explanation: idle_notification changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_3.get(3usize, 1u8) as u32) } } #[inline] pub fn set_idle_notification(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_3.get(3usize, 1u8) as u8) } } #[inline] pub fn set_idle_notification(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000374 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: implicit_on_dfl
- Explanation: implicit_on_dfl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000375 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inc_rlimit_get_ucounts
- Explanation: inc_rlimit_get_ucounts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000376 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inc_rlimit_ucounts
- Explanation: inc_rlimit_ucounts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000377 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inc_ucount
- Explanation: inc_ucount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000378 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: init_ISA_irqs
- Explanation: init_ISA_irqs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000379 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: init_irq_proc
- Explanation: init_irq_proc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000380 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_io_list_del
- Explanation: inode_io_list_del changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000381 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_wait_for_writeback
- Explanation: inode_wait_for_writeback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000382 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: insnlen
- Explanation: insnlen changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000383 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_calc_affinity_vectors
- Explanation: irq_calc_affinity_vectors changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000384 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_can_set_affinity
- Explanation: irq_can_set_affinity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000385 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_create_affinity_masks
- Explanation: irq_create_affinity_masks changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000386 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_force_affinity
- Explanation: irq_force_affinity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000387 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_get_irqchip_state
- Explanation: irq_get_irqchip_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000388 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_has_action
- Explanation: irq_has_action changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000389 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_init_percpu_irqstack
- Explanation: irq_init_percpu_irqstack changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000390 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_inject_interrupt
- Explanation: irq_inject_interrupt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000391 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_percpu_is_enabled
- Explanation: irq_percpu_is_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000392 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_safe
- Explanation: irq_safe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_3.get(10usize, 1u8) as u32) } } #[inline] pub fn set_irq_safe(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_3.get(10usize, 1u8) as u8) } } #[inline] pub fn set_irq_safe(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000393 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_select_affinity
- Explanation: irq_select_affinity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000395 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_set_affinity_notifier
- Explanation: irq_set_affinity_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000396 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_set_irq_wake
- Explanation: irq_set_irq_wake changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000397 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_set_irqchip_state
- Explanation: irq_set_irqchip_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000398 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_update_affinity_desc
- Explanation: irq_update_affinity_desc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000399 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_wake_thread
- Explanation: irq_wake_thread changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000400 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_func
- Explanation: is_func changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000401 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_managed
- Explanation: is_managed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000402 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_rlimit_overlimit
- Explanation: is_rlimit_overlimit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000403 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: jit_requested
- Explanation: jit_requested changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000404 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: jited
- Explanation: jited changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000406 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kallsyms_lookup_name
- Explanation: kallsyms_lookup_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000407 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kallsyms_lookup_size_offset
- Explanation: kallsyms_lookup_size_offset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000408 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kallsyms_on_each_match_symbol
- Explanation: kallsyms_on_each_match_symbol changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000409 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kallsyms_on_each_symbol
- Explanation: kallsyms_on_each_symbol changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000410 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kallsyms_show_value
- Explanation: kallsyms_show_value changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000411 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kallsyms_sym_address
- Explanation: kallsyms_sym_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000412 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kasprintf_strarray
- Explanation: kasprintf_strarray changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000413 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kfree_strarray
- Explanation: kfree_strarray changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000414 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmemdup_array
- Explanation: kmemdup_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000415 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kprobe_override
- Explanation: kprobe_override changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000416 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kstat_incr_irq_this_cpu
- Explanation: kstat_incr_irq_this_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000417 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kstat_irqs_cpu
- Explanation: kstat_irqs_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000418 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kstat_irqs_usr
- Explanation: kstat_irqs_usr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000419 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kstrdup_and_replace
- Explanation: kstrdup_and_replace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000421 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kstrdup_quotable_cmdline
- Explanation: kstrdup_quotable_cmdline changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000422 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kstrdup_quotable_file
- Explanation: kstrdup_quotable_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000423 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_associate_blkcg
- Explanation: kthread_associate_blkcg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000425 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_bind_mask
- Explanation: kthread_bind_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000426 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_blkcg
- Explanation: kthread_blkcg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000427 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_cancel_delayed_work_sync
- Explanation: kthread_cancel_delayed_work_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000428 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_cancel_work_sync
- Explanation: kthread_cancel_work_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000429 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_complete_and_exit
- Explanation: kthread_complete_and_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000430 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_create_on_cpu
- Explanation: kthread_create_on_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000431 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_create_on_node
- Explanation: kthread_create_on_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000433 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_create_worker_on_cpu
- Explanation: kthread_create_worker_on_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000434 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_data
- Explanation: kthread_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000435 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_delayed_work_timer_fn
- Explanation: kthread_delayed_work_timer_fn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000436 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_destroy_worker
- Explanation: kthread_destroy_worker changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000437 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_exit
- Explanation: kthread_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000439 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_flush_worker
- Explanation: kthread_flush_worker changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000440 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_freezable_should_stop
- Explanation: kthread_freezable_should_stop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000441 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_func
- Explanation: kthread_func changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000442 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_is_per_cpu
- Explanation: kthread_is_per_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000443 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_mod_delayed_work
- Explanation: kthread_mod_delayed_work changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000445 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_parkme
- Explanation: kthread_parkme changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000446 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_probe_data
- Explanation: kthread_probe_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000447 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_queue_delayed_work
- Explanation: kthread_queue_delayed_work changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000448 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_queue_work
- Explanation: kthread_queue_work changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000449 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_set_per_cpu
- Explanation: kthread_set_per_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000450 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_should_park
- Explanation: kthread_should_park changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000452 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_should_stop_or_park
- Explanation: kthread_should_stop_or_park changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000454 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_stop_put
- Explanation: kthread_stop_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000455 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_unpark
- Explanation: kthread_unpark changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000456 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_unuse_mm
- Explanation: kthread_unuse_mm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000457 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_use_mm
- Explanation: kthread_use_mm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000458 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_worker_fn
- Explanation: kthread_worker_fn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000459 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthreadd
- Explanation: kthreadd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000460 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: laptop_io_completion
- Explanation: laptop_io_completion changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000461 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: laptop_mode_timer_fn
- Explanation: laptop_mode_timer_fn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000462 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: laptop_sync_completion
- Explanation: laptop_sync_completion changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000463 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: leave_mm
- Explanation: leave_mm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'cpu', 'type': 'core::ffi::c_int'}], 'return_type': '()'}`
- New: `{'params': [], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000465 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lockdep_assert_cpus_held
- Explanation: lockdep_assert_cpus_held changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000466 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lockdep_is_cpus_held
- Explanation: lockdep_is_cpus_held changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000467 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lookup_symbol_name
- Explanation: lookup_symbol_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000468 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lsm_fill_user_ctx
- Explanation: lsm_fill_user_ctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'uctx', 'type': '*mut lsm_ctx'}, {'name': 'uctx_len', 'type': '*mut usize'}, {'name': 'val', 'type': '*mut core::ffi::c_void'}, {'name': 'val_len', 'type': 'usize'}, {'name': 'id', 'type': 'u64_'}, {'name': 'flags', 'type': 'u64_'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'uctx', 'type': '*mut lsm_ctx'}, {'name': 'uctx_len', 'type': '*mut u32_'}, {'name': 'val', 'type': '*mut core::ffi::c_void'}, {'name': 'val_len', 'type': 'usize'}, {'name': 'id', 'type': 'u64_'}, {'name': 'flags', 'type': 'u64_'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000469 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mangle_path
- Explanation: mangle_path changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000470 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: map_check_no_btf
- Explanation: map_check_no_btf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000471 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mas_alloc_cyclic
- Explanation: mas_alloc_cyclic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000472 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: may_skip_resume
- Explanation: may_skip_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_2.get(5usize, 1u8) as u32) } } #[inline] pub fn set_may_skip_resume(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_2.get(5usize, 1u8) as u8) } } #[inline] pub fn set_may_skip_resume(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000473 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mem_cgroup_charge_skmem
- Explanation: mem_cgroup_charge_skmem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000474 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mem_cgroup_uncharge_skmem
- Explanation: mem_cgroup_uncharge_skmem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000475 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: memalloc_noio
- Explanation: memalloc_noio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_3.get(13usize, 1u8) as u32) } } #[inline] pub fn set_memalloc_noio(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_3.get(13usize, 1u8) as u8) } } #[inline] pub fn set_memalloc_noio(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000476 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mpparse_find_mptable
- Explanation: mpparse_find_mptable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000477 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mpparse_parse_early_smp_config
- Explanation: mpparse_parse_early_smp_config changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000478 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mpparse_parse_smp_config
- Explanation: mpparse_parse_smp_config changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000479 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mtree_alloc_cyclic
- Explanation: mtree_alloc_cyclic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000480 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: must_resume
- Explanation: must_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_2.get(4usize, 1u8) as u32) } } #[inline] pub fn set_must_resume(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_2.get(4usize, 1u8) as u8) } } #[inline] pub fn set_must_resume(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000481 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: native_init_IRQ
- Explanation: native_init_IRQ changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000482 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: needs_force_resume
- Explanation: needs_force_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_3.get(6usize, 1u8) as u32) } } #[inline] pub fn set_needs_force_resume(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_3.get(6usize, 1u8) as u8) } } #[inline] pub fn set_needs_force_resume(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000483 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: nested
- Explanation: nested changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000484 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_bitfield_3
- Explanation: new_bitfield_3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'disable_depth', 'type': 'core::ffi::c_uint'}, {'name': 'idle_notification', 'type': 'core::ffi::c_uint'}, {'name': 'request_pending', 'type': 'core::ffi::c_uint'}, {'name': 'deferred_resume', 'type': 'core::ffi::c_uint'}, {'name': 'needs_force_resume', 'type': 'core::ffi::c_uint'}, {'name': 'runtime_auto', 'type': 'core::ffi::c_uint'}, {'name': 'ignore_children', 'type': 'bool_'}, {'name': 'no_callbacks', 'type': 'core::ffi::c_uint'}, {'name': 'irq_safe', 'type': 'core::ffi::c_uint'}, {'name': 'use_autosuspend', 'type': 'core::ffi::c_uint'}, {'name': 'timer_autosuspends', 'type': 'core::ffi::c_uint'}, {'name': 'memalloc_noio', 'type': 'core::ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`
- New: `{'params': [{'name': 'disable_depth', 'type': 'core::ffi::c_uint'}, {'name': 'idle_notification', 'type': 'bool_'}, {'name': 'request_pending', 'type': 'bool_'}, {'name': 'deferred_resume', 'type': 'bool_'}, {'name': 'needs_force_resume', 'type': 'bool_'}, {'name': 'runtime_auto', 'type': 'bool_'}, {'name': 'ignore_children', 'type': 'bool_'}, {'name': 'no_callbacks', 'type': 'bool_'}, {'name': 'irq_safe', 'type': 'bool_'}, {'name': 'use_autosuspend', 'type': 'bool_'}, {'name': 'timer_autosuspends', 'type': 'bool_'}, {'name': 'memalloc_noio', 'type': 'bool_'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`

### Rust Evidence

- Graph edges: `1`

## W-000486 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_action
- Explanation: no_action changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000487 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_callbacks
- Explanation: no_callbacks changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_3.get(9usize, 1u8) as u32) } } #[inline] pub fn set_no_callbacks(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_3.get(9usize, 1u8) as u8) } } #[inline] pub fn set_no_callbacks(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000488 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_cgroup_owner
- Explanation: no_cgroup_owner changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000489 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: node_dev_init
- Explanation: node_dev_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000490 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: node_dirty_ok
- Explanation: node_dirty_ok changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000491 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: notify_cpu_starting
- Explanation: notify_cpu_starting changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000493 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: nr_context_switches_cpu
- Explanation: nr_context_switches_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000494 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: of_css
- Explanation: of_css changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000495 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: of_phy_package_join
- Explanation: of_phy_package_join changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000497 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: open_softirq
- Explanation: open_softirq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000498 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: page_counter_cancel
- Explanation: page_counter_cancel changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000499 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: page_counter_charge
- Explanation: page_counter_charge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000500 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: page_counter_memparse
- Explanation: page_counter_memparse changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000501 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: page_counter_set_low
- Explanation: page_counter_set_low changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000502 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: page_counter_set_max
- Explanation: page_counter_set_max changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000503 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: page_counter_set_min
- Explanation: page_counter_set_min changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000504 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: page_counter_try_charge
- Explanation: page_counter_try_charge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000505 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: page_counter_uncharge
- Explanation: page_counter_uncharge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000507 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: page_frag_cache_drain
- Explanation: page_frag_cache_drain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000508 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: parse_int_array_user
- Explanation: parse_int_array_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000509 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_advertise_eee_all
- Explanation: phy_advertise_eee_all changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000510 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_ethtool_get_eee
- Explanation: phy_ethtool_get_eee changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'data', 'type': '*mut ethtool_eee'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'data', 'type': '*mut ethtool_keee'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000511 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_ethtool_set_eee
- Explanation: phy_ethtool_set_eee changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'data', 'type': '*mut ethtool_eee'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'phydev', 'type': '*mut phy_device'}, {'name': 'data', 'type': '*mut ethtool_keee'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000512 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_support_eee
- Explanation: phy_support_eee changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000514 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: play_idle_precise
- Explanation: play_idle_precise changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000515 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: poke_int3_handler
- Explanation: poke_int3_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000516 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pool_index_plus_1
- Explanation: pool_index_plus_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000517 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: prepare_percpu_nmi
- Explanation: prepare_percpu_nmi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000518 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: probe_irq_mask
- Explanation: probe_irq_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000519 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: probe_irq_off
- Explanation: probe_irq_off changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000520 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: probe_irq_on
- Explanation: probe_irq_on changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000521 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_cgroup_show
- Explanation: proc_cgroup_show changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000522 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ptdump_walk_pgd_level_checkwx
- Explanation: ptdump_walk_pgd_level_checkwx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': '()'}`
- New: `{'params': [], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000523 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: put_ucounts
- Explanation: put_ucounts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000525 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: raise_softirq_irqoff
- Explanation: raise_softirq_irqoff changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000526 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: range_cyclic
- Explanation: range_cyclic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000528 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rearm_wake_irq
- Explanation: rearm_wake_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000530 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: redirty_page_for_writepage
- Explanation: redirty_page_for_writepage changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000532 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: register_cpu_under_node
- Explanation: register_cpu_under_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000533 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: register_memory_node_under_compute_node
- Explanation: register_memory_node_under_compute_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000534 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: remove_cpu
- Explanation: remove_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000535 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: request_any_context_irq
- Explanation: request_any_context_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000536 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: request_nmi
- Explanation: request_nmi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000537 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: request_pending
- Explanation: request_pending changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_3.get(4usize, 1u8) as u32) } } #[inline] pub fn set_request_pending(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_3.get(4usize, 1u8) as u8) } } #[inline] pub fn set_request_pending(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000538 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: request_percpu_nmi
- Explanation: request_percpu_nmi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000539 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: request_threaded_irq
- Explanation: request_threaded_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000540 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: resume_device_irqs
- Explanation: resume_device_irqs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000541 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: retire_userns_sysctls
- Explanation: retire_userns_sysctls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000542 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: runtime_auto
- Explanation: runtime_auto changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_3.get(7usize, 1u8) as u32) } } #[inline] pub fn set_runtime_auto(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_3.get(7usize, 1u8) as u8) } } #[inline] pub fn set_runtime_auto(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000543 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sb_clear_inode_writeback
- Explanation: sb_clear_inode_writeback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000544 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sb_mark_inode_writeback
- Explanation: sb_mark_inode_writeback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000545 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_file_post_open
- Explanation: security_file_post_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000546 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_file_release
- Explanation: security_file_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000547 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_getselfattr
- Explanation: security_getselfattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'attr', 'type': 'core::ffi::c_uint'}, {'name': 'ctx', 'type': '*mut lsm_ctx'}, {'name': 'size', 'type': '*mut usize'}, {'name': 'flags', 'type': 'u32_'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'attr', 'type': 'core::ffi::c_uint'}, {'name': 'ctx', 'type': '*mut lsm_ctx'}, {'name': 'size', 'type': '*mut u32_'}, {'name': 'flags', 'type': 'u32_'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000548 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_post_create_tmpfile
- Explanation: security_inode_post_create_tmpfile changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000549 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_post_remove_acl
- Explanation: security_inode_post_remove_acl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000550 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_post_removexattr
- Explanation: security_inode_post_removexattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000551 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_post_set_acl
- Explanation: security_inode_post_set_acl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000552 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_post_setattr
- Explanation: security_inode_post_setattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000553 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_key_post_create_or_update
- Explanation: security_key_post_create_or_update changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000554 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_setselfattr
- Explanation: security_setselfattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'attr', 'type': 'core::ffi::c_uint'}, {'name': 'ctx', 'type': '*mut lsm_ctx'}, {'name': 'size', 'type': 'usize'}, {'name': 'flags', 'type': 'u32_'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'attr', 'type': 'core::ffi::c_uint'}, {'name': 'ctx', 'type': '*mut lsm_ctx'}, {'name': 'size', 'type': 'u32_'}, {'name': 'flags', 'type': 'u32_'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000555 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: select_idle_routine
- Explanation: select_idle_routine changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'c', 'type': '*const cpuinfo_x86'}], 'return_type': '()'}`
- New: `{'params': [], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000557 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_bprintf
- Explanation: seq_bprintf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000558 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_dentry
- Explanation: seq_dentry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000559 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_escape_mem
- Explanation: seq_escape_mem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000560 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_file_init
- Explanation: seq_file_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000561 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_file_path
- Explanation: seq_file_path changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000562 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_hex_dump
- Explanation: seq_hex_dump changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000564 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_hlist_next_percpu
- Explanation: seq_hlist_next_percpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000565 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_hlist_next_rcu
- Explanation: seq_hlist_next_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000568 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_hlist_start_head_rcu
- Explanation: seq_hlist_start_head_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000569 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_hlist_start_percpu
- Explanation: seq_hlist_start_percpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000570 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_hlist_start_rcu
- Explanation: seq_hlist_start_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000572 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_list_next_rcu
- Explanation: seq_list_next_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000575 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_list_start_head_rcu
- Explanation: seq_list_start_head_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000576 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_list_start_rcu
- Explanation: seq_list_start_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000577 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_lseek
- Explanation: seq_lseek changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000579 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_open_private
- Explanation: seq_open_private changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000580 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_pad
- Explanation: seq_pad changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000582 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_path_root
- Explanation: seq_path_root changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000583 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_printf
- Explanation: seq_printf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000584 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_put_decimal_ll
- Explanation: seq_put_decimal_ll changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000586 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_put_decimal_ull_width
- Explanation: seq_put_decimal_ull_width changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000587 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_put_hex_ll
- Explanation: seq_put_hex_ll changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000588 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_putc
- Explanation: seq_putc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000589 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_puts
- Explanation: seq_puts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000591 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_read_iter
- Explanation: seq_read_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000593 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_release_private
- Explanation: seq_release_private changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000594 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_vprintf
- Explanation: seq_vprintf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000595 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: seq_write
- Explanation: seq_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000596 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_kthread_struct
- Explanation: set_kthread_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000597 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: setup_pcp_cacheinfo
- Explanation: setup_pcp_cacheinfo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': '()'}`
- New: `{'params': [{'name': 'cpu', 'type': 'core::ffi::c_uint'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000598 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: setup_userns_sysctls
- Explanation: setup_userns_sysctls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000599 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: show_interrupts
- Explanation: show_interrupts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000601 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_nosetlease
- Explanation: simple_nosetlease changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut file'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut *mut file_lock'}, {'name': 'arg4', 'type': '*mut *mut core::ffi::c_void'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*mut file'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut *mut file_lease'}, {'name': 'arg4', 'type': '*mut *mut core::ffi::c_void'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000602 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_offset_empty
- Explanation: simple_offset_empty changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000604 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: single_open_size
- Explanation: single_open_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000605 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: single_release
- Explanation: single_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000606 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: single_start
- Explanation: single_start changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000607 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sized_strscpy
- Explanation: sized_strscpy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000608 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_add_rx_frag
- Explanation: skb_add_rx_frag changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000609 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_add_rx_frag_netmem
- Explanation: skb_add_rx_frag_netmem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000610 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_cow_data_for_xdp
- Explanation: skb_cow_data_for_xdp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000611 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_pp_cow_data
- Explanation: skb_pp_cow_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000613 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sleepable
- Explanation: sleepable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000614 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: smp_prepare_boot_cpu
- Explanation: smp_prepare_boot_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000615 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: smp_shutdown_nonboot_cpus
- Explanation: smp_shutdown_nonboot_cpus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000616 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: softirq_init
- Explanation: softirq_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000618 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sprint_backtrace_build_id
- Explanation: sprint_backtrace_build_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000620 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sprint_symbol_build_id
- Explanation: sprint_symbol_build_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000621 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sprint_symbol_no_offset
- Explanation: sprint_symbol_no_offset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000622 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: src_reg
- Explanation: src_reg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000623 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: srso_alias_untrain_ret
- Explanation: srso_alias_untrain_ret changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000625 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: static_call_force_reinit
- Explanation: static_call_force_reinit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000626 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: static_call_init
- Explanation: static_call_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000627 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: static_call_mod_init
- Explanation: static_call_mod_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000628 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: static_call_text_reserved
- Explanation: static_call_text_reserved changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000630 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: string_escape_mem
- Explanation: string_escape_mem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000631 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: string_get_size
- Explanation: string_get_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000632 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: string_unescape
- Explanation: string_unescape changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000635 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: suspend_device_irqs
- Explanation: suspend_device_irqs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000636 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: swevent
- Explanation: swevent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000637 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sync_inodes_sb
- Explanation: sync_inodes_sb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000638 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: tag_pages_for_writeback
- Explanation: tag_pages_for_writeback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000639 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: tagged_writepages
- Explanation: tagged_writepages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000640 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: task_get_cgroup1
- Explanation: task_get_cgroup1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000641 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: tasklet_init
- Explanation: tasklet_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000642 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: tasklet_kill
- Explanation: tasklet_kill changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000643 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: tasklet_setup
- Explanation: tasklet_setup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000645 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: tasklet_unlock_spin_wait
- Explanation: tasklet_unlock_spin_wait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000646 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: tasklet_unlock_wait
- Explanation: tasklet_unlock_wait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000647 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: teardown_percpu_nmi
- Explanation: teardown_percpu_nmi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000649 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: text_poke_bp
- Explanation: text_poke_bp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000651 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: text_poke_copy_locked
- Explanation: text_poke_copy_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000652 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: text_poke_early
- Explanation: text_poke_early changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000653 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: text_poke_finish
- Explanation: text_poke_finish changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000654 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: text_poke_kgdb
- Explanation: text_poke_kgdb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000655 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: text_poke_queue
- Explanation: text_poke_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000656 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: text_poke_set
- Explanation: text_poke_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000657 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: text_poke_sync
- Explanation: text_poke_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000658 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: thaw_secondary_cpus
- Explanation: thaw_secondary_cpus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000659 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: this_cpu_in_panic
- Explanation: this_cpu_in_panic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000661 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: threaded
- Explanation: threaded changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000662 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: timer_autosuspends
- Explanation: timer_autosuspends changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_3.get(12usize, 1u8) as u32) } } #[inline] pub fn set_timer_autosuspends(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_3.get(12usize, 1u8) as u8) } } #[inline] pub fn set_timer_autosuspends(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000663 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: topology_get_logical_id
- Explanation: topology_get_logical_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000667 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: tracing_prog_func_proto
- Explanation: tracing_prog_func_proto changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000668 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: trap_init
- Explanation: trap_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000669 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: try_to_writeback_inodes_sb
- Explanation: try_to_writeback_inodes_sb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000670 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: tsk_fork_get_node
- Explanation: tsk_fork_get_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000671 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: tstamp_type_access
- Explanation: tstamp_type_access changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000672 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unpinned_netfs_wb
- Explanation: unpinned_netfs_wb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000673 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unpriv_ebpf_notify
- Explanation: unpriv_ebpf_notify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000675 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unregister_cpu_under_node
- Explanation: unregister_cpu_under_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000676 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unregister_memory_block_under_nodes
- Explanation: unregister_memory_block_under_nodes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000677 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unregister_node
- Explanation: unregister_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000678 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unregister_one_node
- Explanation: unregister_one_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000679 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: use_autosuspend
- Explanation: use_autosuspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_3.get(11usize, 1u8) as u32) } } #[inline] pub fn set_use_autosuspend(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_3.get(11usize, 1u8) as u8) } } #[inline] pub fn set_use_autosuspend(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000680 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vector
- Explanation: vector changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000681 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: verified
- Explanation: verified changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000682 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_area_map_pages
- Explanation: vm_area_map_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000683 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_area_unmap_pages
- Explanation: vm_area_unmap_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000684 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmap_page_range
- Explanation: vmap_page_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000686 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wakeup_flusher_threads_bdi
- Explanation: wakeup_flusher_threads_bdi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000687 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wb_calc_thresh
- Explanation: wb_calc_thresh changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000688 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wb_domain_init
- Explanation: wb_domain_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000689 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wb_over_bg_thresh
- Explanation: wb_over_bg_thresh changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000690 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wb_update_bandwidth
- Explanation: wb_update_bandwidth changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000691 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wfe
- Explanation: wfe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000692 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: workqueue_set_min_active
- Explanation: workqueue_set_min_active changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000693 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: workqueue_softirq_action
- Explanation: workqueue_softirq_action changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000694 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: workqueue_softirq_dead
- Explanation: workqueue_softirq_dead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000695 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: write_cache_pages
- Explanation: write_cache_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000697 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: writeback_inodes_sb_nr
- Explanation: writeback_inodes_sb_nr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000698 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: writeback_iter
- Explanation: writeback_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000699 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: writeback_set_ratelimit
- Explanation: writeback_set_ratelimit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000838 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __refcount_sub_and_test
- Explanation: __refcount_sub_and_test changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['int i', 'refcount_t *r', 'int *oldp'], 'return_type': 'static inline __must_check bool'}`
- New: `{'params': ['int i', 'refcount_t *r', 'int *oldp'], 'return_type': 'static inline __must_check __signed_wrap bool'}`

### Rust Evidence

- Graph edges: `1`

## W-000839 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c37_read_status
- Explanation: genphy_c37_read_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct phy_device *phydev'], 'return_type': 'int'}`
- New: `{'params': ['struct phy_device *phydev', 'bool *changed'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000840 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_ethtool_get_eee
- Explanation: genphy_c45_ethtool_get_eee changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct phy_device *phydev', 'struct ethtool_eee *data'], 'return_type': 'int'}`
- New: `{'params': ['struct phy_device *phydev', 'struct ethtool_keee *data'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000841 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_ethtool_set_eee
- Explanation: genphy_c45_ethtool_set_eee changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct phy_device *phydev', 'struct ethtool_eee *data'], 'return_type': 'int'}`
- New: `{'params': ['struct phy_device *phydev', 'struct ethtool_keee *data'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000842 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_ethtool_get_eee
- Explanation: phy_ethtool_get_eee changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct phy_device *phydev', 'struct ethtool_eee *data'], 'return_type': 'int'}`
- New: `{'params': ['struct phy_device *phydev', 'struct ethtool_keee *data'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000843 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_ethtool_set_eee
- Explanation: phy_ethtool_set_eee changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct phy_device *phydev', 'struct ethtool_eee *data'], 'return_type': 'int'}`
- New: `{'params': ['struct phy_device *phydev', 'struct ethtool_keee *data'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000737 FieldDrift

- Risk: High
- Score: 10.4
- Symbol: task_struct
- Explanation: task_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'core::ffi::c_uint'}, {'name': 'saved_state', 'type': 'core::ffi::c_uint'}, {'name': 'stack', 'type': '*mut core::ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'ptrace', 'type': 'core::ffi::c_uint'}, {'name': 'on_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'core::ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'core::ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_cpu', 'type': 'core::ffi::c_int'}, {'name': 'on_rq', 'type': 'core::ffi::c_int'}, {'name': 'prio', 'type': 'core::ffi::c_int'}, {'name': 'static_prio', 'type': 'core::ffi::c_int'}, {'name': 'normal_prio', 'type': 'core::ffi::c_int'}, {'name': 'rt_priority', 'type': 'core::ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'dl_server', 'type': '*mut sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'core::ffi::c_uint'}, {'name': 'policy', 'type': 'core::ffi::c_uint'}, {'name': 'nr_cpus_allowed', 'type': 'core::ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut core::ffi::c_void'}, {'name': 'migration_disabled', 'type': 'core::ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'core::ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'core::ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'core::ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'faults_disabled_mapping', 'type': '*mut address_space'}, {'name': 'exit_state', 'type': 'core::ffi::c_int'}, {'name': 'exit_code', 'type': 'core::ffi::c_int'}, {'name': 'exit_signal', 'type': 'core::ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'core::ffi::c_int'}, {'name': 'jobctl', 'type': 'core::ffi::c_ulong'}, {'name': 'personality', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'core::ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'worker_private', 'type': '*mut core::ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[core::ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'core::ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'core::ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'core::ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'journal_info', 'type': '*mut core::ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'core::ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cpuset_slab_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'core::ffi::c_uint'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'core::ffi::c_short'}, {'name': 'pref_node_fork', 'type': 'core::ffi::c_short'}, {'name': 'rseq', 'type': '*mut rseq'}, {'name': 'rseq_len', 'type': 'u32_'}, {'name': 'rseq_sig', 'type': 'u32_'}, {'name': 'rseq_event_mask', 'type': 'core::ffi::c_ulong'}, {'name': 'mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'last_mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'migrate_from_cpu', 'type': 'core::ffi::c_int'}, {'name': 'mm_cid_active', 'type': 'core::ffi::c_int'}, {'name': 'cid_work', 'type': 'callback_head'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'core::ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'core::ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'core::ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'core::ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'core::ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_vaddr', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'core::ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': '__bindgen_padding_1', 'type': '[u64; 2usize]'}, {'name': 'thread', 'type': 'thread_struct'}]`
- New: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'core::ffi::c_uint'}, {'name': 'saved_state', 'type': 'core::ffi::c_uint'}, {'name': 'stack', 'type': '*mut core::ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'ptrace', 'type': 'core::ffi::c_uint'}, {'name': 'on_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'core::ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'core::ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_cpu', 'type': 'core::ffi::c_int'}, {'name': 'on_rq', 'type': 'core::ffi::c_int'}, {'name': 'prio', 'type': 'core::ffi::c_int'}, {'name': 'static_prio', 'type': 'core::ffi::c_int'}, {'name': 'normal_prio', 'type': 'core::ffi::c_int'}, {'name': 'rt_priority', 'type': 'core::ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'dl_server', 'type': '*mut sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'core::ffi::c_uint'}, {'name': 'policy', 'type': 'core::ffi::c_uint'}, {'name': 'nr_cpus_allowed', 'type': 'core::ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut core::ffi::c_void'}, {'name': 'migration_disabled', 'type': 'core::ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'core::ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'core::ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'core::ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'rcu_tasks_exit_cpu', 'type': 'core::ffi::c_int'}, {'name': 'rcu_tasks_exit_list', 'type': 'list_head'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'faults_disabled_mapping', 'type': '*mut address_space'}, {'name': 'exit_state', 'type': 'core::ffi::c_int'}, {'name': 'exit_code', 'type': 'core::ffi::c_int'}, {'name': 'exit_signal', 'type': 'core::ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'core::ffi::c_int'}, {'name': 'jobctl', 'type': 'core::ffi::c_ulong'}, {'name': 'personality', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'core::ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'worker_private', 'type': '*mut core::ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[core::ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'core::ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'core::ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'core::ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'journal_info', 'type': '*mut core::ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'core::ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cpuset_slab_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'core::ffi::c_uint'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'core::ffi::c_short'}, {'name': 'il_weight', 'type': 'u8_'}, {'name': 'pref_node_fork', 'type': 'core::ffi::c_short'}, {'name': 'rseq', 'type': '*mut rseq'}, {'name': 'rseq_len', 'type': 'u32_'}, {'name': 'rseq_sig', 'type': 'u32_'}, {'name': 'rseq_event_mask', 'type': 'core::ffi::c_ulong'}, {'name': 'mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'last_mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'migrate_from_cpu', 'type': 'core::ffi::c_int'}, {'name': 'mm_cid_active', 'type': 'core::ffi::c_int'}, {'name': 'cid_work', 'type': 'callback_head'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'core::ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'core::ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'core::ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'core::ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'core::ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_vaddr', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'core::ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': '__bindgen_padding_1', 'type': '[u64; 7usize]'}, {'name': 'thread', 'type': 'thread_struct'}]`

### Rust Evidence

- Graph edges: `9`

## W-000001 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: PageHuge
- Explanation: PageHuge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000051 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: align_vdso_addr
- Explanation: align_vdso_addr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000054 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: amd_get_nodes_per_socket
- Explanation: amd_get_nodes_per_socket changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000185 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: calculate_max_logical_packages
- Explanation: calculate_max_logical_packages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000186 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: call_depth_return_thunk
- Explanation: call_depth_return_thunk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000190 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: callthunks_patch_builtin_calls
- Explanation: callthunks_patch_builtin_calls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000191 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: callthunks_patch_module_calls
- Explanation: callthunks_patch_module_calls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000192 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: callthunks_translate_call_dest
- Explanation: callthunks_translate_call_dest changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000297 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: default_find_smp_config
- Explanation: default_find_smp_config changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000298 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: default_get_smp_config
- Explanation: default_get_smp_config changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000359 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: generic_processor_info
- Explanation: generic_processor_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000360 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: generic_set_encrypted_ci_d_ops
- Explanation: generic_set_encrypted_ci_d_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000370 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: gpio_led_register_device
- Explanation: gpio_led_register_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000464 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: list_lru_putback
- Explanation: list_lru_putback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000506 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: page_frag_alloc_align
- Explanation: page_frag_alloc_align changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000513 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: pidfd_create
- Explanation: pidfd_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000527 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: rcu_sync_enter_start
- Explanation: rcu_sync_enter_start changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000529 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: recvmsg_copy_msghdr
- Explanation: recvmsg_copy_msghdr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000556 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sendmsg_copy_msghdr
- Explanation: sendmsg_copy_msghdr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000600 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sig_on_uaccess_err
- Explanation: sig_on_uaccess_err changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000633 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: strscpy
- Explanation: strscpy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000634 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: strscpy_pad
- Explanation: strscpy_pad changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000660 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: thread_group_exited
- Explanation: thread_group_exited changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000664 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: topology_phys_to_logical_pkg
- Explanation: topology_phys_to_logical_pkg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000665 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: topology_update_die_map
- Explanation: topology_update_die_map changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000666 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: topology_update_package_map
- Explanation: topology_update_package_map changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000700 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: x86_call_depth_emit_accounting
- Explanation: x86_call_depth_emit_accounting changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000836 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __refcount_add
- Explanation: __refcount_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['int i', 'refcount_t *r', 'int *oldp'], 'return_type': 'static inline void'}`
- New: `{'params': ['int i', 'refcount_t *r', 'int *oldp'], 'return_type': 'static inline __signed_wrap void'}`

### Rust Evidence

- Graph edges: `0`

## W-000837 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __refcount_add_not_zero
- Explanation: __refcount_add_not_zero changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['int i', 'refcount_t *r', 'int *oldp'], 'return_type': 'static inline __must_check bool'}`
- New: `{'params': ['int i', 'refcount_t *r', 'int *oldp'], 'return_type': 'static inline __must_check __signed_wrap bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000740 FieldDrift

- Risk: Medium
- Score: 9.4
- Symbol: uid_gid_map
- Explanation: uid_gid_map changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'nr_extents', 'type': 'u32_'}, {'name': '__bindgen_anon_1', 'type': 'uid_gid_map__bindgen_ty_1'}]`

### Rust Evidence

- Graph edges: `4`

## W-000701 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: address_space
- Explanation: address_space changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'host', 'type': '*mut inode'}, {'name': 'i_pages', 'type': 'xarray'}, {'name': 'invalidate_lock', 'type': 'rw_semaphore'}, {'name': 'gfp_mask', 'type': 'gfp_t'}, {'name': 'i_mmap_writable', 'type': 'atomic_t'}, {'name': 'i_mmap', 'type': 'rb_root_cached'}, {'name': 'nrpages', 'type': 'core::ffi::c_ulong'}, {'name': 'writeback_index', 'type': 'core::ffi::c_ulong'}, {'name': 'a_ops', 'type': '*const address_space_operations'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'i_mmap_rwsem', 'type': 'rw_semaphore'}, {'name': 'wb_err', 'type': 'errseq_t'}, {'name': 'i_private_lock', 'type': 'spinlock_t'}, {'name': 'i_private_list', 'type': 'list_head'}, {'name': 'i_private_data', 'type': '*mut core::ffi::c_void'}]`
- New: `[{'name': 'host', 'type': '*mut inode'}, {'name': 'i_pages', 'type': 'xarray'}, {'name': 'invalidate_lock', 'type': 'rw_semaphore'}, {'name': 'gfp_mask', 'type': 'gfp_t'}, {'name': 'i_mmap_writable', 'type': 'atomic_t'}, {'name': 'i_mmap', 'type': 'rb_root_cached'}, {'name': 'nrpages', 'type': 'core::ffi::c_ulong'}, {'name': 'writeback_index', 'type': 'core::ffi::c_ulong'}, {'name': 'a_ops', 'type': '*const address_space_operations'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'wb_err', 'type': 'errseq_t'}, {'name': 'i_private_lock', 'type': 'spinlock_t'}, {'name': 'i_private_list', 'type': 'list_head'}, {'name': 'i_mmap_rwsem', 'type': 'rw_semaphore'}, {'name': 'i_private_data', 'type': '*mut core::ffi::c_void'}]`

### Rust Evidence

- Graph edges: `3`

## W-000707 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: bpf_flow_keys
- Explanation: bpf_flow_keys changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[{'name': 'nhoff', 'type': '__u16'}, {'name': 'thoff', 'type': '__u16'}, {'name': 'addr_proto', 'type': '__u16'}, {'name': 'is_frag', 'type': '__u8'}, {'name': 'is_first_frag', 'type': '__u8'}, {'name': 'is_encap', 'type': '__u8'}, {'name': 'ip_proto', 'type': '__u8'}, {'name': 'n_proto', 'type': '__be16'}, {'name': 'sport', 'type': '__be16'}, {'name': 'dport', 'type': '__be16'}, {'name': '__bindgen_anon_1', 'type': 'bpf_flow_keys__bindgen_ty_1'}, {'name': 'flags', 'type': '__u32'}, {'name': 'flow_label', 'type': '__be32'}]`

### Rust Evidence

- Graph edges: `3`

## W-000730 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: seq_file
- Explanation: seq_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'buf', 'type': '*mut core::ffi::c_char'}, {'name': 'size', 'type': 'usize'}, {'name': 'from', 'type': 'usize'}, {'name': 'count', 'type': 'usize'}, {'name': 'pad_until', 'type': 'usize'}, {'name': 'index', 'type': 'loff_t'}, {'name': 'read_pos', 'type': 'loff_t'}, {'name': 'lock', 'type': 'mutex'}, {'name': 'op', 'type': '*const seq_operations'}, {'name': 'poll_event', 'type': 'core::ffi::c_int'}, {'name': 'file', 'type': '*const file'}, {'name': 'private', 'type': '*mut core::ffi::c_void'}]`

### Rust Evidence

- Graph edges: `3`

## W-000733 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: sk_buff__bindgen_ty_4__bindgen_ty_1
- Explanation: sk_buff__bindgen_ty_4__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_skb_refdst', 'type': 'core::ffi::c_ulong'}, {'name': 'destructor', 'type': '::core::option::Option<unsafe extern "C" fn(skb: *mut sk_buff)>'}]`
- New: `[{'name': '__pkt_type_offset', 'type': '__IncompleteArrayField<__u8>'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__mono_tc_offset', 'type': '__IncompleteArrayField<__u8>'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'tc_index', 'type': '__u16'}, {'name': 'alloc_cpu', 'type': 'u16_'}, {'name': '__bindgen_anon_1', 'type': 'sk_buff__bindgen_ty_4__bindgen_ty_1__bindgen_ty_1'}, {'name': 'priority', 'type': '__u32'}, {'name': 'skb_iif', 'type': 'core::ffi::c_int'}, {'name': 'hash', 'type': '__u32'}, {'name': '__bindgen_anon_2', 'type': 'sk_buff__bindgen_ty_4__bindgen_ty_1__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'sk_buff__bindgen_ty_4__bindgen_ty_1__bindgen_ty_3'}, {'name': 'secmark', 'type': '__u32'}, {'name': '__bindgen_anon_4', 'type': 'sk_buff__bindgen_ty_4__bindgen_ty_1__bindgen_ty_4'}, {'name': '__bindgen_anon_5', 'type': 'sk_buff__bindgen_ty_4__bindgen_ty_1__bindgen_ty_5'}, {'name': 'inner_transport_header', 'type': '__u16'}, {'name': 'inner_network_header', 'type': '__u16'}, {'name': 'inner_mac_header', 'type': '__u16'}, {'name': 'protocol', 'type': '__be16'}, {'name': 'transport_header', 'type': '__u16'}, {'name': 'network_header', 'type': '__u16'}, {'name': 'mac_header', 'type': '__u16'}]`

### Rust Evidence

- Graph edges: `3`

## W-000734 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: static_call_mod
- Explanation: static_call_mod changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[{'name': 'next', 'type': '*mut static_call_mod'}, {'name': 'mod_', 'type': '*mut module'}, {'name': 'sites', 'type': '*mut static_call_site'}]`

### Rust Evidence

- Graph edges: `2`

## W-000702 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: backing_dev_info
- Explanation: backing_dev_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'id', 'type': 'u64_'}, {'name': 'rb_node', 'type': 'rb_node'}, {'name': 'bdi_list', 'type': 'list_head'}, {'name': 'ra_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'io_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'refcnt', 'type': 'kref'}, {'name': 'capabilities', 'type': 'core::ffi::c_uint'}, {'name': 'min_ratio', 'type': 'core::ffi::c_uint'}, {'name': 'max_ratio', 'type': 'core::ffi::c_uint'}, {'name': 'max_prop_frac', 'type': 'core::ffi::c_uint'}, {'name': 'tot_write_bandwidth', 'type': 'atomic_long_t'}, {'name': 'last_bdp_sleep', 'type': 'core::ffi::c_ulong'}, {'name': 'wb', 'type': 'bdi_writeback'}, {'name': 'wb_list', 'type': 'list_head'}, {'name': 'wb_waitq', 'type': 'wait_queue_head_t'}, {'name': 'dev', 'type': '*mut device'}, {'name': 'dev_name', 'type': '[core::ffi::c_char; 64usize]'}, {'name': 'owner', 'type': '*mut device'}, {'name': 'laptop_mode_wb_timer', 'type': 'timer_list'}, {'name': 'debug_dir', 'type': '*mut dentry'}]`

### Rust Evidence

- Graph edges: `1`

## W-000703 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bdi_writeback
- Explanation: bdi_writeback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'bdi', 'type': '*mut backing_dev_info'}, {'name': 'state', 'type': 'core::ffi::c_ulong'}, {'name': 'last_old_flush', 'type': 'core::ffi::c_ulong'}, {'name': 'b_dirty', 'type': 'list_head'}, {'name': 'b_io', 'type': 'list_head'}, {'name': 'b_more_io', 'type': 'list_head'}, {'name': 'b_dirty_time', 'type': 'list_head'}, {'name': 'list_lock', 'type': 'spinlock_t'}, {'name': 'writeback_inodes', 'type': 'atomic_t'}, {'name': 'stat', 'type': '[percpu_counter; 4usize]'}, {'name': 'bw_time_stamp', 'type': 'core::ffi::c_ulong'}, {'name': 'dirtied_stamp', 'type': 'core::ffi::c_ulong'}, {'name': 'written_stamp', 'type': 'core::ffi::c_ulong'}, {'name': 'write_bandwidth', 'type': 'core::ffi::c_ulong'}, {'name': 'avg_write_bandwidth', 'type': 'core::ffi::c_ulong'}, {'name': 'dirty_ratelimit', 'type': 'core::ffi::c_ulong'}, {'name': 'balanced_dirty_ratelimit', 'type': 'core::ffi::c_ulong'}, {'name': 'completions', 'type': 'fprop_local_percpu'}, {'name': 'dirty_exceeded', 'type': 'core::ffi::c_int'}, {'name': 'start_all_reason', 'type': 'wb_reason'}, {'name': 'work_lock', 'type': 'spinlock_t'}, {'name': 'work_list', 'type': 'list_head'}, {'name': 'dwork', 'type': 'delayed_work'}, {'name': 'bw_dwork', 'type': 'delayed_work'}, {'name': 'bdi_node', 'type': 'list_head'}]`

### Rust Evidence

- Graph edges: `1`

## W-000705 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: block_device
- Explanation: block_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[{'name': 'bd_start_sect', 'type': 'sector_t'}, {'name': 'bd_nr_sectors', 'type': 'sector_t'}, {'name': 'bd_disk', 'type': '*mut gendisk'}, {'name': 'bd_queue', 'type': '*mut request_queue'}, {'name': 'bd_stats', 'type': '*mut disk_stats'}, {'name': 'bd_stamp', 'type': 'core::ffi::c_ulong'}, {'name': 'bd_read_only', 'type': 'bool_'}, {'name': 'bd_partno', 'type': 'u8_'}, {'name': 'bd_write_holder', 'type': 'bool_'}, {'name': 'bd_has_submit_bio', 'type': 'bool_'}, {'name': 'bd_dev', 'type': 'dev_t'}, {'name': 'bd_inode', 'type': '*mut inode'}, {'name': 'bd_openers', 'type': 'atomic_t'}, {'name': 'bd_size_lock', 'type': 'spinlock_t'}, {'name': 'bd_claiming', 'type': '*mut core::ffi::c_void'}, {'name': 'bd_holder', 'type': '*mut core::ffi::c_void'}, {'name': 'bd_holder_ops', 'type': '*mut blk_holder_ops'}, {'name': 'bd_holder_lock', 'type': 'mutex'}, {'name': 'bd_holders', 'type': 'core::ffi::c_int'}, {'name': 'bd_holder_dir', 'type': '*mut kobject'}, {'name': 'bd_fsfreeze_count', 'type': 'atomic_t'}, {'name': 'bd_fsfreeze_mutex', 'type': 'mutex'}, {'name': 'bd_meta_info', 'type': '*mut partition_meta_info'}, {'name': 'bd_ro_warned', 'type': 'bool_'}, {'name': 'bd_writers', 'type': 'core::ffi::c_int'}, {'name': 'bd_device', 'type': 'device'}]`

### Rust Evidence

- Graph edges: `1`

## W-000706 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: boot_params
- Explanation: boot_params changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'screen_info', 'type': 'screen_info'}, {'name': 'apm_bios_info', 'type': 'apm_bios_info'}, {'name': '_pad2', 'type': '[__u8; 4usize]'}, {'name': 'tboot_addr', 'type': '__u64'}, {'name': 'ist_info', 'type': 'ist_info'}, {'name': 'acpi_rsdp_addr', 'type': '__u64'}, {'name': '_pad3', 'type': '[__u8; 8usize]'}, {'name': 'hd0_info', 'type': '[__u8; 16usize]'}, {'name': 'hd1_info', 'type': '[__u8; 16usize]'}, {'name': 'sys_desc_table', 'type': 'sys_desc_table'}, {'name': 'olpc_ofw_header', 'type': 'olpc_ofw_header'}, {'name': 'ext_ramdisk_image', 'type': '__u32'}, {'name': 'ext_ramdisk_size', 'type': '__u32'}, {'name': 'ext_cmd_line_ptr', 'type': '__u32'}, {'name': '_pad4', 'type': '[__u8; 112usize]'}, {'name': 'cc_blob_address', 'type': '__u32'}, {'name': 'edid_info', 'type': 'edid_info'}, {'name': 'efi_info', 'type': 'efi_info'}, {'name': 'alt_mem_k', 'type': '__u32'}, {'name': 'scratch', 'type': '__u32'}, {'name': 'e820_entries', 'type': '__u8'}, {'name': 'eddbuf_entries', 'type': '__u8'}, {'name': 'edd_mbr_sig_buf_entries', 'type': '__u8'}, {'name': 'kbd_status', 'type': '__u8'}, {'name': 'secure_boot', 'type': '__u8'}, {'name': '_pad5', 'type': '[__u8; 2usize]'}, {'name': 'sentinel', 'type': '__u8'}, {'name': '_pad6', 'type': '[__u8; 1usize]'}, {'name': 'hdr', 'type': 'setup_header'}, {'name': '_pad7', 'type': '[__u8; 36usize]'}, {'name': 'edd_mbr_sig_buffer', 'type': '[__u32; 16usize]'}, {'name': 'e820_table', 'type': '[boot_e820_entry; 128usize]'}, {'name': '_pad8', 'type': '[__u8; 48usize]'}, {'name': 'eddbuf', 'type': '[edd_info; 6usize]'}, {'name': '_pad9', 'type': '[__u8; 276usize]'}]`
- New: `[]`

### Rust Evidence

- Graph edges: `1`

## W-000710 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: cgroup_namespace
- Explanation: cgroup_namespace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'ns', 'type': 'ns_common'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'ucounts', 'type': '*mut ucounts'}, {'name': 'root_cset', 'type': '*mut css_set'}]`

### Rust Evidence

- Graph edges: `1`

## W-000711 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: cpuinfo_topology
- Explanation: cpuinfo_topology changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'apicid', 'type': 'u32_'}, {'name': 'initial_apicid', 'type': 'u32_'}, {'name': 'pkg_id', 'type': 'u32_'}, {'name': 'die_id', 'type': 'u32_'}, {'name': 'cu_id', 'type': 'u32_'}, {'name': 'core_id', 'type': 'u32_'}, {'name': 'logical_pkg_id', 'type': 'u32_'}, {'name': 'logical_die_id', 'type': 'u32_'}, {'name': 'llc_id', 'type': 'u32_'}, {'name': 'l2c_id', 'type': 'u32_'}]`
- New: `[{'name': 'apicid', 'type': 'u32_'}, {'name': 'initial_apicid', 'type': 'u32_'}, {'name': 'pkg_id', 'type': 'u32_'}, {'name': 'die_id', 'type': 'u32_'}, {'name': 'cu_id', 'type': 'u32_'}, {'name': 'core_id', 'type': 'u32_'}, {'name': 'logical_pkg_id', 'type': 'u32_'}, {'name': 'logical_die_id', 'type': 'u32_'}, {'name': 'amd_node_id', 'type': 'u32_'}, {'name': 'llc_id', 'type': 'u32_'}, {'name': 'l2c_id', 'type': 'u32_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000712 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: cpuinfo_x86
- Explanation: cpuinfo_x86 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'x86', 'type': '__u8'}, {'name': 'x86_vendor', 'type': '__u8'}, {'name': 'x86_model', 'type': '__u8'}, {'name': 'x86_stepping', 'type': '__u8'}, {'name': 'x86_tlbsize', 'type': 'core::ffi::c_int'}, {'name': 'vmx_capability', 'type': '[__u32; 5usize]'}, {'name': 'x86_virt_bits', 'type': '__u8'}, {'name': 'x86_phys_bits', 'type': '__u8'}, {'name': 'x86_coreid_bits', 'type': '__u8'}, {'name': 'extended_cpuid_level', 'type': '__u32'}, {'name': 'cpuid_level', 'type': 'core::ffi::c_int'}, {'name': '__bindgen_anon_1', 'type': 'cpuinfo_x86__bindgen_ty_1'}, {'name': 'x86_vendor_id', 'type': '[core::ffi::c_char; 16usize]'}, {'name': 'x86_model_id', 'type': '[core::ffi::c_char; 64usize]'}, {'name': 'topo', 'type': 'cpuinfo_topology'}, {'name': 'x86_cache_size', 'type': 'core::ffi::c_uint'}, {'name': 'x86_cache_alignment', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_max_rmid', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_occ_scale', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_mbm_width_offset', 'type': 'core::ffi::c_int'}, {'name': 'x86_power', 'type': 'core::ffi::c_int'}, {'name': 'loops_per_jiffy', 'type': 'core::ffi::c_ulong'}, {'name': 'ppin', 'type': 'u64_'}, {'name': 'x86_max_cores', 'type': 'u16_'}, {'name': 'x86_clflush_size', 'type': 'u16_'}, {'name': 'booted_cores', 'type': 'u16_'}, {'name': 'cpu_index', 'type': 'u16_'}, {'name': 'smt_active', 'type': 'bool_'}, {'name': 'microcode', 'type': 'u32_'}, {'name': 'x86_cache_bits', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u16; 3usize]'}]`
- New: `[{'name': 'x86', 'type': '__u8'}, {'name': 'x86_vendor', 'type': '__u8'}, {'name': 'x86_model', 'type': '__u8'}, {'name': 'x86_stepping', 'type': '__u8'}, {'name': 'x86_tlbsize', 'type': 'core::ffi::c_int'}, {'name': 'vmx_capability', 'type': '[__u32; 5usize]'}, {'name': 'x86_virt_bits', 'type': '__u8'}, {'name': 'x86_phys_bits', 'type': '__u8'}, {'name': 'extended_cpuid_level', 'type': '__u32'}, {'name': 'cpuid_level', 'type': 'core::ffi::c_int'}, {'name': '__bindgen_anon_1', 'type': 'cpuinfo_x86__bindgen_ty_1'}, {'name': 'x86_vendor_id', 'type': '[core::ffi::c_char; 16usize]'}, {'name': 'x86_model_id', 'type': '[core::ffi::c_char; 64usize]'}, {'name': 'topo', 'type': 'cpuinfo_topology'}, {'name': 'x86_cache_size', 'type': 'core::ffi::c_uint'}, {'name': 'x86_cache_alignment', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_max_rmid', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_occ_scale', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_mbm_width_offset', 'type': 'core::ffi::c_int'}, {'name': 'x86_power', 'type': 'core::ffi::c_int'}, {'name': 'loops_per_jiffy', 'type': 'core::ffi::c_ulong'}, {'name': 'ppin', 'type': 'u64_'}, {'name': 'x86_clflush_size', 'type': 'u16_'}, {'name': 'booted_cores', 'type': 'u16_'}, {'name': 'cpu_index', 'type': 'u16_'}, {'name': 'smt_active', 'type': 'bool_'}, {'name': 'microcode', 'type': 'u32_'}, {'name': 'x86_cache_bits', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': 'u16'}]`

### Rust Evidence

- Graph edges: `1`

## W-000713 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: css_set
- Explanation: css_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'subsys', 'type': '[*mut cgroup_subsys_state; 14usize]'}, {'name': 'refcount', 'type': 'refcount_t'}, {'name': 'dom_cset', 'type': '*mut css_set'}, {'name': 'dfl_cgrp', 'type': '*mut cgroup'}, {'name': 'nr_tasks', 'type': 'core::ffi::c_int'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'mg_tasks', 'type': 'list_head'}, {'name': 'dying_tasks', 'type': 'list_head'}, {'name': 'task_iters', 'type': 'list_head'}, {'name': 'e_cset_node', 'type': '[list_head; 14usize]'}, {'name': 'threaded_csets', 'type': 'list_head'}, {'name': 'threaded_csets_node', 'type': 'list_head'}, {'name': 'hlist', 'type': 'hlist_node'}, {'name': 'cgrp_links', 'type': 'list_head'}, {'name': 'mg_src_preload_node', 'type': 'list_head'}, {'name': 'mg_dst_preload_node', 'type': 'list_head'}, {'name': 'mg_node', 'type': 'list_head'}, {'name': 'mg_src_cgrp', 'type': '*mut cgroup'}, {'name': 'mg_dst_cgrp', 'type': '*mut cgroup'}, {'name': 'mg_dst_cset', 'type': '*mut css_set'}, {'name': 'dead', 'type': 'bool_'}, {'name': 'callback_head', 'type': 'callback_head'}]`

### Rust Evidence

- Graph edges: `1`

## W-000714 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: em_perf_domain
- Explanation: em_perf_domain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'table', 'type': '*mut em_perf_state'}, {'name': 'nr_perf_states', 'type': 'core::ffi::c_int'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'cpus', 'type': '__IncompleteArrayField<core::ffi::c_ulong>'}]`
- New: `[{'name': 'em_table', 'type': '*mut em_perf_table'}, {'name': 'nr_perf_states', 'type': 'core::ffi::c_int'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'cpus', 'type': '__IncompleteArrayField<core::ffi::c_ulong>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000715 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: em_perf_state
- Explanation: em_perf_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'frequency', 'type': 'core::ffi::c_ulong'}, {'name': 'power', 'type': 'core::ffi::c_ulong'}, {'name': 'cost', 'type': 'core::ffi::c_ulong'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}]`
- New: `[{'name': 'performance', 'type': 'core::ffi::c_ulong'}, {'name': 'frequency', 'type': 'core::ffi::c_ulong'}, {'name': 'power', 'type': 'core::ffi::c_ulong'}, {'name': 'cost', 'type': 'core::ffi::c_ulong'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}]`

### Rust Evidence

- Graph edges: `1`

## W-000717 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: irq_cpustat_t
- Explanation: irq_cpustat_t changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__nmi_count', 'type': 'core::ffi::c_uint'}, {'name': 'apic_timer_irqs', 'type': 'core::ffi::c_uint'}, {'name': 'irq_spurious_count', 'type': 'core::ffi::c_uint'}, {'name': 'icr_read_retry_count', 'type': 'core::ffi::c_uint'}, {'name': 'kvm_posted_intr_ipis', 'type': 'core::ffi::c_uint'}, {'name': 'kvm_posted_intr_wakeup_ipis', 'type': 'core::ffi::c_uint'}, {'name': 'kvm_posted_intr_nested_ipis', 'type': 'core::ffi::c_uint'}, {'name': 'x86_platform_ipis', 'type': 'core::ffi::c_uint'}, {'name': 'apic_perf_irqs', 'type': 'core::ffi::c_uint'}, {'name': 'apic_irq_work_irqs', 'type': 'core::ffi::c_uint'}, {'name': 'irq_resched_count', 'type': 'core::ffi::c_uint'}, {'name': 'irq_call_count', 'type': 'core::ffi::c_uint'}, {'name': 'irq_tlb_count', 'type': 'core::ffi::c_uint'}, {'name': 'irq_thermal_count', 'type': 'core::ffi::c_uint'}, {'name': 'irq_threshold_count', 'type': 'core::ffi::c_uint'}, {'name': 'irq_deferred_error_count', 'type': 'core::ffi::c_uint'}, {'name': 'irq_hv_callback_count', 'type': 'core::ffi::c_uint'}]`
- New: `[{'name': '__nmi_count', 'type': 'core::ffi::c_uint'}, {'name': 'apic_timer_irqs', 'type': 'core::ffi::c_uint'}, {'name': 'irq_spurious_count', 'type': 'core::ffi::c_uint'}, {'name': 'icr_read_retry_count', 'type': 'core::ffi::c_uint'}, {'name': 'x86_platform_ipis', 'type': 'core::ffi::c_uint'}, {'name': 'apic_perf_irqs', 'type': 'core::ffi::c_uint'}, {'name': 'apic_irq_work_irqs', 'type': 'core::ffi::c_uint'}, {'name': 'irq_resched_count', 'type': 'core::ffi::c_uint'}, {'name': 'irq_call_count', 'type': 'core::ffi::c_uint'}, {'name': 'irq_tlb_count', 'type': 'core::ffi::c_uint'}, {'name': 'irq_thermal_count', 'type': 'core::ffi::c_uint'}, {'name': 'irq_threshold_count', 'type': 'core::ffi::c_uint'}, {'name': 'irq_deferred_error_count', 'type': 'core::ffi::c_uint'}, {'name': 'irq_hv_callback_count', 'type': 'core::ffi::c_uint'}]`

### Rust Evidence

- Graph edges: `1`

## W-000720 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: netlink_callback
- Explanation: netlink_callback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'nlh', 'type': '*const nlmsghdr'}, {'name': 'dump', 'type': '::core::option::Option<'}, {'name': 'data', 'type': '*mut core::ffi::c_void'}, {'name': 'module', 'type': '*mut module'}, {'name': 'extack', 'type': '*mut netlink_ext_ack'}, {'name': 'family', 'type': 'u16_'}, {'name': 'answer_flags', 'type': 'u16_'}, {'name': 'min_dump_alloc', 'type': 'u32_'}, {'name': 'prev_seq', 'type': 'core::ffi::c_uint'}, {'name': 'seq', 'type': 'core::ffi::c_uint'}, {'name': 'strict_check', 'type': 'bool_'}, {'name': '__bindgen_anon_1', 'type': 'netlink_callback__bindgen_ty_1'}]`
- New: `[{'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'nlh', 'type': '*const nlmsghdr'}, {'name': 'dump', 'type': '::core::option::Option<'}, {'name': 'data', 'type': '*mut core::ffi::c_void'}, {'name': 'module', 'type': '*mut module'}, {'name': 'extack', 'type': '*mut netlink_ext_ack'}, {'name': 'family', 'type': 'u16_'}, {'name': 'answer_flags', 'type': 'u16_'}, {'name': 'min_dump_alloc', 'type': 'u32_'}, {'name': 'prev_seq', 'type': 'core::ffi::c_uint'}, {'name': 'seq', 'type': 'core::ffi::c_uint'}, {'name': 'flags', 'type': 'core::ffi::c_int'}, {'name': 'strict_check', 'type': 'bool_'}, {'name': '__bindgen_anon_1', 'type': 'netlink_callback__bindgen_ty_1'}]`

### Rust Evidence

- Graph edges: `1`

## W-000721 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: netlink_dump_control
- Explanation: netlink_dump_control changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'start', 'type': '::core::option::Option<'}, {'name': 'dump', 'type': '::core::option::Option<'}, {'name': 'done', 'type': '::core::option::Option<'}, {'name': 'extack', 'type': '*mut netlink_ext_ack'}, {'name': 'data', 'type': '*mut core::ffi::c_void'}, {'name': 'module', 'type': '*mut module'}, {'name': 'min_dump_alloc', 'type': 'u32_'}]`
- New: `[{'name': 'start', 'type': '::core::option::Option<'}, {'name': 'dump', 'type': '::core::option::Option<'}, {'name': 'done', 'type': '::core::option::Option<'}, {'name': 'extack', 'type': '*mut netlink_ext_ack'}, {'name': 'data', 'type': '*mut core::ffi::c_void'}, {'name': 'module', 'type': '*mut module'}, {'name': 'min_dump_alloc', 'type': 'u32_'}, {'name': 'flags', 'type': 'core::ffi::c_int'}]`

### Rust Evidence

- Graph edges: `1`

## W-000722 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: offset_ctx
- Explanation: offset_ctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'xa', 'type': 'xarray'}, {'name': 'next_offset', 'type': 'u32_'}]`
- New: `[{'name': 'mt', 'type': 'maple_tree'}, {'name': 'next_offset', 'type': 'core::ffi::c_ulong'}]`

### Rust Evidence

- Graph edges: `1`

## W-000723 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: pcpu_hot__bindgen_ty_1__bindgen_ty_1
- Explanation: pcpu_hot__bindgen_ty_1__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'current_task', 'type': '*mut task_struct'}, {'name': 'preempt_count', 'type': 'core::ffi::c_int'}, {'name': 'cpu_number', 'type': 'core::ffi::c_int'}, {'name': 'call_depth', 'type': 'u64_'}, {'name': 'top_of_stack', 'type': 'core::ffi::c_ulong'}, {'name': 'hardirq_stack_ptr', 'type': '*mut core::ffi::c_void'}, {'name': 'softirq_pending', 'type': 'u16_'}, {'name': 'hardirq_stack_inuse', 'type': 'bool_'}]`
- New: `[{'name': 'current_task', 'type': '*mut task_struct'}, {'name': 'preempt_count', 'type': 'core::ffi::c_int'}, {'name': 'cpu_number', 'type': 'core::ffi::c_int'}, {'name': 'top_of_stack', 'type': 'core::ffi::c_ulong'}, {'name': 'hardirq_stack_ptr', 'type': '*mut core::ffi::c_void'}, {'name': 'softirq_pending', 'type': 'u16_'}, {'name': 'hardirq_stack_inuse', 'type': 'bool_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000726 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: phy_package_shared
- Explanation: phy_package_shared changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'base_addr', 'type': 'u8_'}, {'name': 'refcnt', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'priv_size', 'type': 'usize'}, {'name': 'priv_', 'type': '*mut core::ffi::c_void'}]`
- New: `[{'name': 'base_addr', 'type': 'u8_'}, {'name': 'np', 'type': '*mut device_node'}, {'name': 'refcnt', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'priv_size', 'type': 'usize'}, {'name': 'priv_', 'type': '*mut core::ffi::c_void'}]`

### Rust Evidence

- Graph edges: `1`

## W-000728 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: pt_regs
- Explanation: pt_regs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'r15', 'type': 'core::ffi::c_ulong'}, {'name': 'r14', 'type': 'core::ffi::c_ulong'}, {'name': 'r13', 'type': 'core::ffi::c_ulong'}, {'name': 'r12', 'type': 'core::ffi::c_ulong'}, {'name': 'bp', 'type': 'core::ffi::c_ulong'}, {'name': 'bx', 'type': 'core::ffi::c_ulong'}, {'name': 'r11', 'type': 'core::ffi::c_ulong'}, {'name': 'r10', 'type': 'core::ffi::c_ulong'}, {'name': 'r9', 'type': 'core::ffi::c_ulong'}, {'name': 'r8', 'type': 'core::ffi::c_ulong'}, {'name': 'ax', 'type': 'core::ffi::c_ulong'}, {'name': 'cx', 'type': 'core::ffi::c_ulong'}, {'name': 'dx', 'type': 'core::ffi::c_ulong'}, {'name': 'si', 'type': 'core::ffi::c_ulong'}, {'name': 'di', 'type': 'core::ffi::c_ulong'}, {'name': 'orig_ax', 'type': 'core::ffi::c_ulong'}, {'name': 'ip', 'type': 'core::ffi::c_ulong'}, {'name': 'cs', 'type': 'core::ffi::c_ulong'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'sp', 'type': 'core::ffi::c_ulong'}, {'name': 'ss', 'type': 'core::ffi::c_ulong'}]`
- New: `[{'name': 'r15', 'type': 'core::ffi::c_ulong'}, {'name': 'r14', 'type': 'core::ffi::c_ulong'}, {'name': 'r13', 'type': 'core::ffi::c_ulong'}, {'name': 'r12', 'type': 'core::ffi::c_ulong'}, {'name': 'bp', 'type': 'core::ffi::c_ulong'}, {'name': 'bx', 'type': 'core::ffi::c_ulong'}, {'name': 'r11', 'type': 'core::ffi::c_ulong'}, {'name': 'r10', 'type': 'core::ffi::c_ulong'}, {'name': 'r9', 'type': 'core::ffi::c_ulong'}, {'name': 'r8', 'type': 'core::ffi::c_ulong'}, {'name': 'ax', 'type': 'core::ffi::c_ulong'}, {'name': 'cx', 'type': 'core::ffi::c_ulong'}, {'name': 'dx', 'type': 'core::ffi::c_ulong'}, {'name': 'si', 'type': 'core::ffi::c_ulong'}, {'name': 'di', 'type': 'core::ffi::c_ulong'}, {'name': 'orig_ax', 'type': 'core::ffi::c_ulong'}, {'name': 'ip', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'pt_regs__bindgen_ty_1'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'sp', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_2', 'type': 'pt_regs__bindgen_ty_2'}]`

### Rust Evidence

- Graph edges: `1`

## W-000729 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: scm_fp_list
- Explanation: scm_fp_list changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'count', 'type': 'core::ffi::c_short'}, {'name': 'max', 'type': 'core::ffi::c_short'}, {'name': 'user', 'type': '*mut user_struct'}, {'name': 'fp', 'type': '[*mut file; 253usize]'}]`
- New: `[{'name': 'count', 'type': 'core::ffi::c_short'}, {'name': 'count_unix', 'type': 'core::ffi::c_short'}, {'name': 'max', 'type': 'core::ffi::c_short'}, {'name': 'user', 'type': '*mut user_struct'}, {'name': 'fp', 'type': '[*mut file; 253usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000731 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: seq_operations
- Explanation: seq_operations changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'start', 'type': '::core::option::Option<'}, {'name': 'next', 'type': '::core::option::Option<'}, {'name': 'show', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-000735 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: super_block
- Explanation: super_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 's_list', 'type': 'list_head'}, {'name': 's_dev', 'type': 'dev_t'}, {'name': 's_blocksize_bits', 'type': 'core::ffi::c_uchar'}, {'name': 's_blocksize', 'type': 'core::ffi::c_ulong'}, {'name': 's_maxbytes', 'type': 'loff_t'}, {'name': 's_type', 'type': '*mut file_system_type'}, {'name': 's_op', 'type': '*const super_operations'}, {'name': 'dq_op', 'type': '*const dquot_operations'}, {'name': 's_qcop', 'type': '*const quotactl_ops'}, {'name': 's_export_op', 'type': '*const export_operations'}, {'name': 's_flags', 'type': 'core::ffi::c_ulong'}, {'name': 's_iflags', 'type': 'core::ffi::c_ulong'}, {'name': 's_magic', 'type': 'core::ffi::c_ulong'}, {'name': 's_root', 'type': '*mut dentry'}, {'name': 's_umount', 'type': 'rw_semaphore'}, {'name': 's_count', 'type': 'core::ffi::c_int'}, {'name': 's_active', 'type': 'atomic_t'}, {'name': 's_security', 'type': '*mut core::ffi::c_void'}, {'name': 's_xattr', 'type': '*const *mut xattr_handler'}, {'name': 's_roots', 'type': 'hlist_bl_head'}, {'name': 's_mounts', 'type': 'list_head'}, {'name': 's_bdev', 'type': '*mut block_device'}, {'name': 's_bdev_handle', 'type': '*mut bdev_handle'}, {'name': 's_bdi', 'type': '*mut backing_dev_info'}, {'name': 's_mtd', 'type': '*mut mtd_info'}, {'name': 's_instances', 'type': 'hlist_node'}, {'name': 's_quota_types', 'type': 'core::ffi::c_uint'}, {'name': 's_dquot', 'type': 'quota_info'}, {'name': 's_writers', 'type': 'sb_writers'}, {'name': 's_fs_info', 'type': '*mut core::ffi::c_void'}, {'name': 's_time_gran', 'type': 'u32_'}, {'name': 's_time_min', 'type': 'time64_t'}, {'name': 's_time_max', 'type': 'time64_t'}, {'name': 's_fsnotify_mask', 'type': '__u32'}, {'name': 's_fsnotify_marks', 'type': '*mut fsnotify_mark_connector'}, {'name': 's_id', 'type': '[core::ffi::c_char; 32usize]'}, {'name': 's_uuid', 'type': 'uuid_t'}, {'name': 's_max_links', 'type': 'core::ffi::c_uint'}, {'name': 's_vfs_rename_mutex', 'type': 'mutex'}, {'name': 's_subtype', 'type': '*const core::ffi::c_char'}, {'name': 's_d_op', 'type': '*const dentry_operations'}, {'name': 's_shrink', 'type': '*mut shrinker'}, {'name': 's_remove_count', 'type': 'atomic_long_t'}, {'name': 's_fsnotify_connectors', 'type': 'atomic_long_t'}, {'name': 's_readonly_remount', 'type': 'core::ffi::c_int'}, {'name': 's_wb_err', 'type': 'errseq_t'}, {'name': 's_dio_done_wq', 'type': '*mut workqueue_struct'}, {'name': 's_pins', 'type': 'hlist_head'}, {'name': 's_user_ns', 'type': '*mut user_namespace'}, {'name': 's_dentry_lru', 'type': 'list_lru'}, {'name': 's_inode_lru', 'type': 'list_lru'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 's_sync_lock', 'type': 'mutex'}, {'name': 's_stack_depth', 'type': 'core::ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': '[u32; 9usize]'}, {'name': 's_inode_list_lock', 'type': 'spinlock_t'}, {'name': 's_inodes', 'type': 'list_head'}, {'name': 's_inode_wblist_lock', 'type': 'spinlock_t'}, {'name': 's_inodes_wb', 'type': 'list_head'}]`
- New: `[{'name': 's_list', 'type': 'list_head'}, {'name': 's_dev', 'type': 'dev_t'}, {'name': 's_blocksize_bits', 'type': 'core::ffi::c_uchar'}, {'name': 's_blocksize', 'type': 'core::ffi::c_ulong'}, {'name': 's_maxbytes', 'type': 'loff_t'}, {'name': 's_type', 'type': '*mut file_system_type'}, {'name': 's_op', 'type': '*const super_operations'}, {'name': 'dq_op', 'type': '*const dquot_operations'}, {'name': 's_qcop', 'type': '*const quotactl_ops'}, {'name': 's_export_op', 'type': '*const export_operations'}, {'name': 's_flags', 'type': 'core::ffi::c_ulong'}, {'name': 's_iflags', 'type': 'core::ffi::c_ulong'}, {'name': 's_magic', 'type': 'core::ffi::c_ulong'}, {'name': 's_root', 'type': '*mut dentry'}, {'name': 's_umount', 'type': 'rw_semaphore'}, {'name': 's_count', 'type': 'core::ffi::c_int'}, {'name': 's_active', 'type': 'atomic_t'}, {'name': 's_security', 'type': '*mut core::ffi::c_void'}, {'name': 's_xattr', 'type': '*const *mut xattr_handler'}, {'name': 's_roots', 'type': 'hlist_bl_head'}, {'name': 's_mounts', 'type': 'list_head'}, {'name': 's_bdev', 'type': '*mut block_device'}, {'name': 's_bdev_file', 'type': '*mut file'}, {'name': 's_bdi', 'type': '*mut backing_dev_info'}, {'name': 's_mtd', 'type': '*mut mtd_info'}, {'name': 's_instances', 'type': 'hlist_node'}, {'name': 's_quota_types', 'type': 'core::ffi::c_uint'}, {'name': 's_dquot', 'type': 'quota_info'}, {'name': 's_writers', 'type': 'sb_writers'}, {'name': 's_fs_info', 'type': '*mut core::ffi::c_void'}, {'name': 's_time_gran', 'type': 'u32_'}, {'name': 's_time_min', 'type': 'time64_t'}, {'name': 's_time_max', 'type': 'time64_t'}, {'name': 's_fsnotify_mask', 'type': '__u32'}, {'name': 's_fsnotify_marks', 'type': '*mut fsnotify_mark_connector'}, {'name': 's_id', 'type': '[core::ffi::c_char; 32usize]'}, {'name': 's_uuid', 'type': 'uuid_t'}, {'name': 's_uuid_len', 'type': 'u8_'}, {'name': 's_sysfs_name', 'type': '[core::ffi::c_char; 37usize]'}, {'name': 's_max_links', 'type': 'core::ffi::c_uint'}, {'name': 's_vfs_rename_mutex', 'type': 'mutex'}, {'name': 's_subtype', 'type': '*const core::ffi::c_char'}, {'name': 's_d_op', 'type': '*const dentry_operations'}, {'name': 's_shrink', 'type': '*mut shrinker'}, {'name': 's_remove_count', 'type': 'atomic_long_t'}, {'name': 's_fsnotify_connectors', 'type': 'atomic_long_t'}, {'name': 's_readonly_remount', 'type': 'core::ffi::c_int'}, {'name': 's_wb_err', 'type': 'errseq_t'}, {'name': 's_dio_done_wq', 'type': '*mut workqueue_struct'}, {'name': 's_pins', 'type': 'hlist_head'}, {'name': 's_user_ns', 'type': '*mut user_namespace'}, {'name': 's_dentry_lru', 'type': 'list_lru'}, {'name': 's_inode_lru', 'type': 'list_lru'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 's_sync_lock', 'type': 'mutex'}, {'name': 's_stack_depth', 'type': 'core::ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': '[u32; 15usize]'}, {'name': 's_inode_list_lock', 'type': 'spinlock_t'}, {'name': 's_inodes', 'type': 'list_head'}, {'name': 's_inode_wblist_lock', 'type': 'spinlock_t'}, {'name': 's_inodes_wb', 'type': 'list_head'}]`

### Rust Evidence

- Graph edges: `1`

## W-000736 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: system_counterval_t
- Explanation: system_counterval_t changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'cycles', 'type': 'u64_'}, {'name': 'cs', 'type': '*mut clocksource'}]`
- New: `[{'name': 'cycles', 'type': 'u64_'}, {'name': 'cs_id', 'type': 'clocksource_ids'}]`

### Rust Evidence

- Graph edges: `1`

## W-000739 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: ucounts
- Explanation: ucounts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'node', 'type': 'hlist_node'}, {'name': 'ns', 'type': '*mut user_namespace'}, {'name': 'uid', 'type': 'kuid_t'}, {'name': 'count', 'type': 'atomic_t'}, {'name': 'ucount', 'type': '[atomic_long_t; 10usize]'}, {'name': 'rlimit', 'type': '[atomic_long_t; 4usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000741 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: user_namespace
- Explanation: user_namespace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'uid_map', 'type': 'uid_gid_map'}, {'name': 'gid_map', 'type': 'uid_gid_map'}, {'name': 'projid_map', 'type': 'uid_gid_map'}, {'name': 'parent', 'type': '*mut user_namespace'}, {'name': 'level', 'type': 'core::ffi::c_int'}, {'name': 'owner', 'type': 'kuid_t'}, {'name': 'group', 'type': 'kgid_t'}, {'name': 'ns', 'type': 'ns_common'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'parent_could_setfcap', 'type': 'bool_'}, {'name': 'keyring_name_list', 'type': 'list_head'}, {'name': 'user_keyring_register', 'type': '*mut key'}, {'name': 'keyring_sem', 'type': 'rw_semaphore'}, {'name': 'work', 'type': 'work_struct'}, {'name': 'set', 'type': 'ctl_table_set'}, {'name': 'sysctls', 'type': '*mut ctl_table_header'}, {'name': 'ucounts', 'type': '*mut ucounts'}, {'name': 'ucount_max', 'type': '[core::ffi::c_long; 10usize]'}, {'name': 'rlimit_max', 'type': '[core::ffi::c_long; 4usize]'}, {'name': 'binfmt_misc', 'type': '*mut binfmt_misc'}]`

### Rust Evidence

- Graph edges: `1`

## W-000742 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vmem_altmap
- Explanation: vmem_altmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'base_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'end_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'reserve', 'type': 'core::ffi::c_ulong'}, {'name': 'free', 'type': 'core::ffi::c_ulong'}, {'name': 'align', 'type': 'core::ffi::c_ulong'}, {'name': 'alloc', 'type': 'core::ffi::c_ulong'}]`
- New: `[{'name': 'base_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'end_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'reserve', 'type': 'core::ffi::c_ulong'}, {'name': 'free', 'type': 'core::ffi::c_ulong'}, {'name': 'align', 'type': 'core::ffi::c_ulong'}, {'name': 'alloc', 'type': 'core::ffi::c_ulong'}, {'name': 'inaccessible', 'type': 'bool_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000743 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: writeback_control
- Explanation: writeback_control changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'nr_to_write', 'type': 'core::ffi::c_long'}, {'name': 'pages_skipped', 'type': 'core::ffi::c_long'}, {'name': 'range_start', 'type': 'loff_t'}, {'name': 'range_end', 'type': 'loff_t'}, {'name': 'sync_mode', 'type': 'writeback_sync_modes'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'swap_plug', 'type': '*mut *mut swap_iocb'}, {'name': 'fbatch', 'type': 'folio_batch'}, {'name': 'index', 'type': 'core::ffi::c_ulong'}, {'name': 'saved_err', 'type': 'core::ffi::c_int'}]`

### Rust Evidence

- Graph edges: `1`

## W-000744 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: x86_init_mpparse
- Explanation: x86_init_mpparse changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'setup_ioapic_ids', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'find_smp_config', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'get_smp_config', 'type': '::core::option::Option<unsafe extern "C" fn(early: core::ffi::c_uint)>'}]`
- New: `[{'name': 'setup_ioapic_ids', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'find_mptable', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'early_parse_smp_cfg', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'parse_smp_cfg', 'type': '::core::option::Option<unsafe extern "C" fn()>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000745 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: x86_init_resources
- Explanation: x86_init_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'probe_roms', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'reserve_resources', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'memory_setup', 'type': '::core::option::Option<unsafe extern "C" fn() -> *mut core::ffi::c_char>'}]`
- New: `[{'name': 'probe_roms', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'reserve_resources', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'memory_setup', 'type': '::core::option::Option<unsafe extern "C" fn() -> *mut core::ffi::c_char>'}, {'name': 'dmi_setup', 'type': '::core::option::Option<unsafe extern "C" fn()>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000811 MacroConstDrift

- Risk: Medium
- Score: 8.8
- Symbol: PF_MEMALLOC
- Explanation: PF_MEMALLOC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000800	/* Allocating memory */`
- New: `0x00000800	/* Allocating memory to free memory. See memalloc_noreclaim_save() */`

### Rust Evidence

- Graph edges: `6`

## W-000746 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: CONFIG_LD_ORPHAN_WARN_LEVEL
- Explanation: CONFIG_LD_ORPHAN_WARN_LEVEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `b"warn\0"`
- New: `b"error\0"`

### Rust Evidence

- Graph edges: `1`

## W-000747 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: CONFIG_RUSTC_VERSION_TEXT
- Explanation: CONFIG_RUSTC_VERSION_TEXT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `b"rustc 1.74.1 (a28077b28 2023-12-04)\0"`
- New: `b"rustc 1.76.0 (07dca489a 2024-02-04)\0"`

### Rust Evidence

- Graph edges: `1`

## W-000748 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: MAX_CPU_FEATURES
- Explanation: MAX_CPU_FEATURES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `672`
- New: `704`

### Rust Evidence

- Graph edges: `1`

## W-000749 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: NCAPINTS
- Explanation: NCAPINTS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `21`
- New: `22`

### Rust Evidence

- Graph edges: `1`

## W-000750 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: clocksource_ids_CSID_MAX
- Explanation: clocksource_ids_CSID_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `2`
- New: `5`

### Rust Evidence

- Graph edges: `1`

## W-000751 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_BPF_CGROUP_EGRESS
- Explanation: skb_drop_reason_SKB_DROP_REASON_BPF_CGROUP_EGRESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `45`
- New: `47`

### Rust Evidence

- Graph edges: `1`

## W-000752 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_CPU_BACKLOG
- Explanation: skb_drop_reason_SKB_DROP_REASON_CPU_BACKLOG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `53`
- New: `56`

### Rust Evidence

- Graph edges: `1`

## W-000753 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_DEV_HDR
- Explanation: skb_drop_reason_SKB_DROP_REASON_DEV_HDR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `60`
- New: `63`

### Rust Evidence

- Graph edges: `1`

## W-000754 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_DEV_READY
- Explanation: skb_drop_reason_SKB_DROP_REASON_DEV_READY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `61`
- New: `64`

### Rust Evidence

- Graph edges: `1`

## W-000755 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_DUP_FRAG
- Explanation: skb_drop_reason_SKB_DROP_REASON_DUP_FRAG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `72`
- New: `75`

### Rust Evidence

- Graph edges: `1`

## W-000756 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FRAG_REASM_TIMEOUT
- Explanation: skb_drop_reason_SKB_DROP_REASON_FRAG_REASM_TIMEOUT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `73`
- New: `76`

### Rust Evidence

- Graph edges: `1`

## W-000757 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FRAG_TOO_FAR
- Explanation: skb_drop_reason_SKB_DROP_REASON_FRAG_TOO_FAR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `74`
- New: `77`

### Rust Evidence

- Graph edges: `1`

## W-000758 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FULL_RING
- Explanation: skb_drop_reason_SKB_DROP_REASON_FULL_RING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `62`
- New: `65`

### Rust Evidence

- Graph edges: `1`

## W-000759 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_HDR_TRUNC
- Explanation: skb_drop_reason_SKB_DROP_REASON_HDR_TRUNC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `64`
- New: `67`

### Rust Evidence

- Graph edges: `1`

## W-000760 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_ICMP_CSUM
- Explanation: skb_drop_reason_SKB_DROP_REASON_ICMP_CSUM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `67`
- New: `70`

### Rust Evidence

- Graph edges: `1`

## W-000761 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_INVALID_PROTO
- Explanation: skb_drop_reason_SKB_DROP_REASON_INVALID_PROTO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `68`
- New: `71`

### Rust Evidence

- Graph edges: `1`

## W-000762 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6DISABLED
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6DISABLED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `46`
- New: `48`

### Rust Evidence

- Graph edges: `1`

## W-000763 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_BAD_EXTHDR
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_BAD_EXTHDR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `76`
- New: `79`

### Rust Evidence

- Graph edges: `1`

## W-000764 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_CODE
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_CODE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `79`
- New: `82`

### Rust Evidence

- Graph edges: `1`

## W-000765 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_OPTIONS
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_OPTIONS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `80`
- New: `83`

### Rust Evidence

- Graph edges: `1`

## W-000766 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_FRAG
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_FRAG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `77`
- New: `80`

### Rust Evidence

- Graph edges: `1`

## W-000767 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_HOP_LIMIT
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_HOP_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `78`
- New: `81`

### Rust Evidence

- Graph edges: `1`

## W-000768 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_NS_OTHERHOST
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_NS_OTHERHOST changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `81`
- New: `84`

### Rust Evidence

- Graph edges: `1`

## W-000769 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INADDRERRORS
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INADDRERRORS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `69`
- New: `72`

### Rust Evidence

- Graph edges: `1`

## W-000770 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INNOROUTES
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INNOROUTES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `70`
- New: `73`

### Rust Evidence

- Graph edges: `1`

## W-000771 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_OUTNOROUTES
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_OUTNOROUTES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `44`
- New: `46`

### Rust Evidence

- Graph edges: `1`

## W-000772 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_MAX
- Explanation: skb_drop_reason_SKB_DROP_REASON_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `87`
- New: `90`

### Rust Evidence

- Graph edges: `1`

## W-000773 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NEIGH_CREATEFAIL
- Explanation: skb_drop_reason_SKB_DROP_REASON_NEIGH_CREATEFAIL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `47`
- New: `49`

### Rust Evidence

- Graph edges: `1`

## W-000774 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NEIGH_DEAD
- Explanation: skb_drop_reason_SKB_DROP_REASON_NEIGH_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `50`
- New: `52`

### Rust Evidence

- Graph edges: `1`

## W-000775 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NEIGH_FAILED
- Explanation: skb_drop_reason_SKB_DROP_REASON_NEIGH_FAILED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `50`

### Rust Evidence

- Graph edges: `1`

## W-000776 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NEIGH_QUEUEFULL
- Explanation: skb_drop_reason_SKB_DROP_REASON_NEIGH_QUEUEFULL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `49`
- New: `51`

### Rust Evidence

- Graph edges: `1`

## W-000777 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NOMEM
- Explanation: skb_drop_reason_SKB_DROP_REASON_NOMEM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `63`
- New: `66`

### Rust Evidence

- Graph edges: `1`

## W-000778 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_PACKET_SOCK_ERROR
- Explanation: skb_drop_reason_SKB_DROP_REASON_PACKET_SOCK_ERROR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `84`
- New: `87`

### Rust Evidence

- Graph edges: `1`

## W-000779 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_PKT_TOO_BIG
- Explanation: skb_drop_reason_SKB_DROP_REASON_PKT_TOO_BIG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `71`
- New: `74`

### Rust Evidence

- Graph edges: `1`

## W-000780 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_QDISC_DROP
- Explanation: skb_drop_reason_SKB_DROP_REASON_QDISC_DROP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `52`
- New: `55`

### Rust Evidence

- Graph edges: `1`

## W-000781 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_QUEUE_PURGE
- Explanation: skb_drop_reason_SKB_DROP_REASON_QUEUE_PURGE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `82`
- New: `85`

### Rust Evidence

- Graph edges: `1`

## W-000782 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SKB_CSUM
- Explanation: skb_drop_reason_SKB_DROP_REASON_SKB_CSUM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `57`
- New: `60`

### Rust Evidence

- Graph edges: `1`

## W-000783 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SKB_GSO_SEG
- Explanation: skb_drop_reason_SKB_DROP_REASON_SKB_GSO_SEG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `58`
- New: `61`

### Rust Evidence

- Graph edges: `1`

## W-000784 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SKB_UCOPY_FAULT
- Explanation: skb_drop_reason_SKB_DROP_REASON_SKB_UCOPY_FAULT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `59`
- New: `62`

### Rust Evidence

- Graph edges: `1`

## W-000785 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TAP_FILTER
- Explanation: skb_drop_reason_SKB_DROP_REASON_TAP_FILTER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `65`
- New: `68`

### Rust Evidence

- Graph edges: `1`

## W-000786 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TAP_TXFILTER
- Explanation: skb_drop_reason_SKB_DROP_REASON_TAP_TXFILTER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `66`
- New: `69`

### Rust Evidence

- Graph edges: `1`

## W-000787 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_ACK_UNSENT_DATA
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_ACK_UNSENT_DATA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `41`
- New: `43`

### Rust Evidence

- Graph edges: `1`

## W-000788 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_CLOSE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_CLOSE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `37`
- New: `39`

### Rust Evidence

- Graph edges: `1`

## W-000789 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_FASTOPEN
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_FASTOPEN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `38`
- New: `40`

### Rust Evidence

- Graph edges: `1`

## W-000790 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_SEQUENCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_SEQUENCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `34`
- New: `35`

### Rust Evidence

- Graph edges: `1`

## W-000791 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_SYN
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_SYN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `36`
- New: `38`

### Rust Evidence

- Graph edges: `1`

## W-000792 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_MINTTL
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_MINTTL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `75`
- New: `78`

### Rust Evidence

- Graph edges: `1`

## W-000793 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OFOMERGE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OFOMERGE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `31`
- New: `32`

### Rust Evidence

- Graph edges: `1`

## W-000794 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OFO_DROP
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OFO_DROP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `43`
- New: `45`

### Rust Evidence

- Graph edges: `1`

## W-000795 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OFO_QUEUE_PRUNE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OFO_QUEUE_PRUNE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `42`
- New: `44`

### Rust Evidence

- Graph edges: `1`

## W-000796 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OLD_ACK
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OLD_ACK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `39`
- New: `41`

### Rust Evidence

- Graph edges: `1`

## W-000797 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OLD_DATA
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OLD_DATA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `29`
- New: `30`

### Rust Evidence

- Graph edges: `1`

## W-000798 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OLD_SEQUENCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OLD_SEQUENCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `33`
- New: `34`

### Rust Evidence

- Graph edges: `1`

## W-000799 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OVERWINDOW
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OVERWINDOW changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `30`
- New: `31`

### Rust Evidence

- Graph edges: `1`

## W-000800 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_RESET
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_RESET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `35`
- New: `37`

### Rust Evidence

- Graph edges: `1`

## W-000801 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_RFC7323_PAWS
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_RFC7323_PAWS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `32`
- New: `33`

### Rust Evidence

- Graph edges: `1`

## W-000802 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_TOO_OLD_ACK
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_TOO_OLD_ACK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `40`
- New: `42`

### Rust Evidence

- Graph edges: `1`

## W-000803 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_ZEROWINDOW
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_ZEROWINDOW changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `28`
- New: `29`

### Rust Evidence

- Graph edges: `1`

## W-000804 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_CHAIN_NOTFOUND
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_CHAIN_NOTFOUND changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `85`
- New: `88`

### Rust Evidence

- Graph edges: `1`

## W-000805 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_COOKIE_ERROR
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_COOKIE_ERROR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `83`
- New: `86`

### Rust Evidence

- Graph edges: `1`

## W-000806 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_EGRESS
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_EGRESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `51`
- New: `53`

### Rust Evidence

- Graph edges: `1`

## W-000807 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_INGRESS
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_INGRESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `55`
- New: `58`

### Rust Evidence

- Graph edges: `1`

## W-000808 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_RECLASSIFY_LOOP
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_RECLASSIFY_LOOP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `86`
- New: `89`

### Rust Evidence

- Graph edges: `1`

## W-000809 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_UNHANDLED_PROTO
- Explanation: skb_drop_reason_SKB_DROP_REASON_UNHANDLED_PROTO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `56`
- New: `59`

### Rust Evidence

- Graph edges: `1`

## W-000810 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_XDP
- Explanation: skb_drop_reason_SKB_DROP_REASON_XDP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `54`
- New: `57`

### Rust Evidence

- Graph edges: `1`

## W-000812 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: PF_MEMALLOC_NOFS
- Explanation: PF_MEMALLOC_NOFS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00040000	/* All allocation requests will inherit GFP_NOFS */`
- New: `0x00040000	/* All allocations inherit GFP_NOFS. See memalloc_nfs_save() */`

### Rust Evidence

- Graph edges: `1`

## W-000813 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: PF_MEMALLOC_NOIO
- Explanation: PF_MEMALLOC_NOIO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00080000	/* All allocation requests will inherit GFP_NOIO */`
- New: `0x00080000	/* All allocations inherit GFP_NOIO. See memalloc_noio_save() */`

### Rust Evidence

- Graph edges: `1`

## W-000814 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: PF_MEMALLOC_PIN
- Explanation: PF_MEMALLOC_PIN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x10000000	/* Allocation context constrained to zones which allow long term pinning. */`
- New: `0x10000000	/* Allocations constrained to zones which allow long term pinning.`

### Rust Evidence

- Graph edges: `1`

## W-000815 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SLAB_ACCOUNT
- Explanation: SLAB_ACCOUNT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0`
- New: `__SLAB_FLAG_UNUSED`

### Rust Evidence

- Graph edges: `0`

## W-000816 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SLAB_CACHE_DMA
- Explanation: SLAB_CACHE_DMA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `((slab_flags_t __force)0x00004000U)`
- New: `__SLAB_FLAG_BIT(_SLAB_CACHE_DMA)`

### Rust Evidence

- Graph edges: `0`

## W-000817 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SLAB_CACHE_DMA32
- Explanation: SLAB_CACHE_DMA32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `((slab_flags_t __force)0x00008000U)`
- New: `__SLAB_FLAG_BIT(_SLAB_CACHE_DMA32)`

### Rust Evidence

- Graph edges: `0`

## W-000818 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SLAB_CONSISTENCY_CHECKS
- Explanation: SLAB_CONSISTENCY_CHECKS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `((slab_flags_t __force)0x00000100U)`
- New: `__SLAB_FLAG_BIT(_SLAB_CONSISTENCY_CHECKS)`

### Rust Evidence

- Graph edges: `0`

## W-000819 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SLAB_DEBUG_OBJECTS
- Explanation: SLAB_DEBUG_OBJECTS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0`
- New: `__SLAB_FLAG_UNUSED`

### Rust Evidence

- Graph edges: `0`

## W-000820 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SLAB_FAILSLAB
- Explanation: SLAB_FAILSLAB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0`
- New: `__SLAB_FLAG_UNUSED`

### Rust Evidence

- Graph edges: `0`

## W-000821 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SLAB_HWCACHE_ALIGN
- Explanation: SLAB_HWCACHE_ALIGN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `((slab_flags_t __force)0x00002000U)`
- New: `__SLAB_FLAG_BIT(_SLAB_HWCACHE_ALIGN)`

### Rust Evidence

- Graph edges: `0`

## W-000822 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SLAB_KASAN
- Explanation: SLAB_KASAN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0`
- New: `__SLAB_FLAG_UNUSED`

### Rust Evidence

- Graph edges: `0`

## W-000823 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SLAB_KMALLOC
- Explanation: SLAB_KMALLOC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `((slab_flags_t __force)0x00001000U)`
- New: `__SLAB_FLAG_BIT(_SLAB_KMALLOC)`

### Rust Evidence

- Graph edges: `0`

## W-000824 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SLAB_NOLEAKTRACE
- Explanation: SLAB_NOLEAKTRACE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `((slab_flags_t __force)0x00800000U)`
- New: `__SLAB_FLAG_BIT(_SLAB_NOLEAKTRACE)`

### Rust Evidence

- Graph edges: `0`

## W-000825 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SLAB_NO_MERGE
- Explanation: SLAB_NO_MERGE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `((slab_flags_t __force)0x01000000U)`
- New: `__SLAB_FLAG_BIT(_SLAB_NO_MERGE)`

### Rust Evidence

- Graph edges: `0`

## W-000826 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SLAB_NO_USER_FLAGS
- Explanation: SLAB_NO_USER_FLAGS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `((slab_flags_t __force)0x10000000U)`
- New: `__SLAB_FLAG_BIT(_SLAB_NO_USER_FLAGS)`

### Rust Evidence

- Graph edges: `0`

## W-000827 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SLAB_PANIC
- Explanation: SLAB_PANIC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `((slab_flags_t __force)0x00040000U)`
- New: `__SLAB_FLAG_BIT(_SLAB_PANIC)`

### Rust Evidence

- Graph edges: `0`

## W-000828 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SLAB_POISON
- Explanation: SLAB_POISON changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `((slab_flags_t __force)0x00000800U)`
- New: `__SLAB_FLAG_BIT(_SLAB_POISON)`

### Rust Evidence

- Graph edges: `0`

## W-000829 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SLAB_RECLAIM_ACCOUNT
- Explanation: SLAB_RECLAIM_ACCOUNT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `((slab_flags_t __force)0)`
- New: `__SLAB_FLAG_UNUSED`

### Rust Evidence

- Graph edges: `0`

## W-000830 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SLAB_RED_ZONE
- Explanation: SLAB_RED_ZONE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `((slab_flags_t __force)0x00000400U)`
- New: `__SLAB_FLAG_BIT(_SLAB_RED_ZONE)`

### Rust Evidence

- Graph edges: `0`

## W-000831 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SLAB_SKIP_KFENCE
- Explanation: SLAB_SKIP_KFENCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0`
- New: `__SLAB_FLAG_UNUSED`

### Rust Evidence

- Graph edges: `0`

## W-000832 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SLAB_STORE_USER
- Explanation: SLAB_STORE_USER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `((slab_flags_t __force)0x00010000U)`
- New: `__SLAB_FLAG_BIT(_SLAB_STORE_USER)`

### Rust Evidence

- Graph edges: `0`

## W-000833 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SLAB_TRACE
- Explanation: SLAB_TRACE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `((slab_flags_t __force)0x00200000U)`
- New: `__SLAB_FLAG_BIT(_SLAB_TRACE)`

### Rust Evidence

- Graph edges: `0`

## W-000834 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SLAB_TYPESAFE_BY_RCU
- Explanation: SLAB_TYPESAFE_BY_RCU changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `((slab_flags_t __force)0x00080000U)`
- New: `__SLAB_FLAG_BIT(_SLAB_TYPESAFE_BY_RCU)`

### Rust Evidence

- Graph edges: `0`

## W-000835 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: WORK_OFFQ_CANCELING
- Explanation: WORK_OFFQ_CANCELING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `(1ul << __WORK_OFFQ_CANCELING)`
- New: `(1ul << WORK_OFFQ_CANCELING_BIT)`

### Rust Evidence

- Graph edges: `0`
