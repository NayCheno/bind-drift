# BindDrift Ranked Warnings

## W-000471 FieldDrift

- Risk: High
- Score: 13.4
- Symbol: user
- Explanation: user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'regs', 'type': 'user_regs_struct'}, {'name': 'u_fpvalid', 'type': 'core::ffi::c_int'}, {'name': 'pad0', 'type': 'core::ffi::c_int'}, {'name': 'i387', 'type': 'user_i387_struct'}, {'name': 'u_tsize', 'type': 'core::ffi::c_ulong'}, {'name': 'u_dsize', 'type': 'core::ffi::c_ulong'}, {'name': 'u_ssize', 'type': 'core::ffi::c_ulong'}, {'name': 'start_code', 'type': 'core::ffi::c_ulong'}, {'name': 'start_stack', 'type': 'core::ffi::c_ulong'}, {'name': 'signal', 'type': 'core::ffi::c_long'}, {'name': 'reserved', 'type': 'core::ffi::c_int'}, {'name': 'pad1', 'type': 'core::ffi::c_int'}, {'name': 'u_ar0', 'type': 'core::ffi::c_ulong'}, {'name': 'u_fpstate', 'type': '*mut user_i387_struct'}, {'name': 'magic', 'type': 'core::ffi::c_ulong'}, {'name': 'u_comm', 'type': '[core::ffi::c_char; 32usize]'}, {'name': 'u_debugreg', 'type': '[core::ffi::c_ulong; 8usize]'}, {'name': 'error_code', 'type': 'core::ffi::c_ulong'}, {'name': 'fault_address', 'type': 'core::ffi::c_ulong'}]`

### Rust Evidence

- Graph edges: `19`

## W-000001 SignatureDrift

- Risk: High
- Score: 13.2
- Symbol: BUG
- Explanation: BUG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': '()'}`
- New: `{'params': [], 'return_type': '!'}`

### Rust Evidence

- Graph edges: `13`

## W-000462 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: module
- Explanation: module changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'state', 'type': 'module_state'}, {'name': 'list', 'type': 'list_head'}, {'name': 'name', 'type': '[core::ffi::c_char; 56usize]'}, {'name': 'mkobj', 'type': 'module_kobject'}, {'name': 'modinfo_attrs', 'type': '*mut module_attribute'}, {'name': 'version', 'type': '*const core::ffi::c_char'}, {'name': 'srcversion', 'type': '*const core::ffi::c_char'}, {'name': 'holders_dir', 'type': '*mut kobject'}, {'name': 'syms', 'type': '*mut kernel_symbol'}, {'name': 'crcs', 'type': '*const s32'}, {'name': 'num_syms', 'type': 'core::ffi::c_uint'}, {'name': 'param_lock', 'type': 'mutex'}, {'name': 'kp', 'type': '*mut kernel_param'}, {'name': 'num_kp', 'type': 'core::ffi::c_uint'}, {'name': 'num_gpl_syms', 'type': 'core::ffi::c_uint'}, {'name': 'gpl_syms', 'type': '*const kernel_symbol'}, {'name': 'gpl_crcs', 'type': '*const s32'}, {'name': 'using_gplonly_symbols', 'type': 'bool_'}, {'name': 'async_probe_requested', 'type': 'bool_'}, {'name': 'num_exentries', 'type': 'core::ffi::c_uint'}, {'name': 'extable', 'type': '*mut exception_table_entry'}, {'name': 'init', 'type': '::core::option::Option<unsafe extern "C" fn() -> core::ffi::c_int>'}, {'name': 'mem', 'type': '[module_memory; 7usize]'}, {'name': 'arch', 'type': 'mod_arch_specific'}, {'name': 'taints', 'type': 'core::ffi::c_ulong'}, {'name': 'num_bugs', 'type': 'core::ffi::c_uint'}, {'name': 'bug_list', 'type': 'list_head'}, {'name': 'bug_table', 'type': '*mut bug_entry'}, {'name': 'kallsyms', 'type': '*mut mod_kallsyms'}, {'name': 'core_kallsyms', 'type': 'mod_kallsyms'}, {'name': 'sect_attrs', 'type': '*mut module_sect_attrs'}, {'name': 'notes_attrs', 'type': '*mut module_notes_attrs'}, {'name': 'args', 'type': '*mut core::ffi::c_char'}, {'name': 'percpu', 'type': '*mut core::ffi::c_void'}, {'name': 'percpu_size', 'type': 'core::ffi::c_uint'}, {'name': 'noinstr_text_start', 'type': '*mut core::ffi::c_void'}, {'name': 'noinstr_text_size', 'type': 'core::ffi::c_uint'}, {'name': 'num_tracepoints', 'type': 'core::ffi::c_uint'}, {'name': 'tracepoints_ptrs', 'type': '*const core::ffi::c_int'}, {'name': 'num_srcu_structs', 'type': 'core::ffi::c_uint'}, {'name': 'srcu_struct_ptrs', 'type': '*mut *mut srcu_struct'}, {'name': 'jump_entries', 'type': '*mut jump_entry'}, {'name': 'num_jump_entries', 'type': 'core::ffi::c_uint'}, {'name': 'num_trace_bprintk_fmt', 'type': 'core::ffi::c_uint'}, {'name': 'trace_bprintk_fmt_start', 'type': '*mut *const core::ffi::c_char'}, {'name': 'trace_events', 'type': '*mut *mut trace_event_call'}, {'name': 'num_trace_events', 'type': 'core::ffi::c_uint'}, {'name': 'trace_evals', 'type': '*mut *mut trace_eval_map'}, {'name': 'num_trace_evals', 'type': 'core::ffi::c_uint'}, {'name': 'kprobes_text_start', 'type': '*mut core::ffi::c_void'}, {'name': 'kprobes_text_size', 'type': 'core::ffi::c_uint'}, {'name': 'kprobe_blacklist', 'type': '*mut core::ffi::c_ulong'}, {'name': 'num_kprobe_blacklist', 'type': 'core::ffi::c_uint'}, {'name': 'num_static_call_sites', 'type': 'core::ffi::c_int'}, {'name': 'static_call_sites', 'type': '*mut static_call_site'}, {'name': 'source_list', 'type': 'list_head'}, {'name': 'target_list', 'type': 'list_head'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'refcnt', 'type': 'atomic_t'}, {'name': 'ctors', 'type': '*mut ctor_fn_t'}, {'name': 'num_ctors', 'type': 'core::ffi::c_uint'}]`

### Rust Evidence

- Graph edges: `34`

## W-000049 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: call_usermodehelper
- Explanation: call_usermodehelper changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000025 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: __usermodehelper_disable
- Explanation: __usermodehelper_disable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000026 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: __usermodehelper_set_disable_depth
- Explanation: __usermodehelper_set_disable_depth changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000050 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: call_usermodehelper_exec
- Explanation: call_usermodehelper_exec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000051 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: call_usermodehelper_setup
- Explanation: call_usermodehelper_setup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000285 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: proc_dointvec
- Explanation: proc_dointvec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000390 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: usermodehelper_read_lock_wait
- Explanation: usermodehelper_read_lock_wait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000391 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: usermodehelper_read_trylock
- Explanation: usermodehelper_read_trylock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000392 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: usermodehelper_read_unlock
- Explanation: usermodehelper_read_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000004 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: __kunit_abort
- Explanation: __kunit_abort changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000119 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: kernfs_get
- Explanation: kernfs_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000156 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: kobject_get
- Explanation: kobject_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000189 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: kunit_filter
- Explanation: kunit_filter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000194 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: kunit_get_current_test
- Explanation: kunit_get_current_test changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000236 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: panic
- Explanation: panic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'fmt', 'type': '*const core::ffi::c_char'}, {'name': '', 'type': '...'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'fmt', 'type': '*const core::ffi::c_char'}, {'name': '', 'type': '...'}], 'return_type': '!'}`

### Rust Evidence

- Graph edges: `4`

## W-000006 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: __kunit_do_failed_assertion
- Explanation: __kunit_do_failed_assertion changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000088 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: idr_alloc
- Explanation: idr_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000131 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: kernfs_remove
- Explanation: kernfs_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000210 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: kunit_unary_assert_format
- Explanation: kunit_unary_assert_format changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000300 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: radix_tree_gang_lookup
- Explanation: radix_tree_gang_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000420 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: xas_find
- Explanation: xas_find changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000020 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __register_sysctl_table
- Explanation: __register_sysctl_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000022 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __symbol_get
- Explanation: __symbol_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000028 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __xa_alloc
- Explanation: __xa_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000042 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: arch_get_unmapped_area
- Explanation: arch_get_unmapped_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000047 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: build_id_parse
- Explanation: build_id_parse changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000076 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: generic_get_unmapped_area
- Explanation: generic_get_unmapped_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000095 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: idr_get_next
- Explanation: idr_get_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000151 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: kobj_ns_type_register
- Explanation: kobj_ns_type_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000160 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: kobject_init
- Explanation: kobject_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000166 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: kobject_set_name
- Explanation: kobject_set_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000169 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: kobject_uevent
- Explanation: kobject_uevent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000177 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: kunit_add_action
- Explanation: kunit_add_action changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000222 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: mmput
- Explanation: mmput changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000253 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: param_set_bool
- Explanation: param_set_bool changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000263 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: param_set_uint
- Explanation: param_set_uint changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000268 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: parameq
- Explanation: parameq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000288 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: proc_dointvec_ms_jiffies
- Explanation: proc_dointvec_ms_jiffies changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000293 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: proc_douintvec
- Explanation: proc_douintvec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000298 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: radix_tree_delete
- Explanation: radix_tree_delete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000301 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: radix_tree_gang_lookup_tag
- Explanation: radix_tree_gang_lookup_tag changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000309 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: radix_tree_lookup
- Explanation: radix_tree_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000313 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: radix_tree_preload
- Explanation: radix_tree_preload changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000350 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: sysfs_create_group
- Explanation: sysfs_create_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000352 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: sysfs_create_link
- Explanation: sysfs_create_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000356 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: sysfs_emit
- Explanation: sysfs_emit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000372 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: sysfs_remove_group
- Explanation: sysfs_remove_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000374 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: sysfs_remove_link
- Explanation: sysfs_remove_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000381 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: sysfs_update_group
- Explanation: sysfs_update_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000405 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: xa_dump
- Explanation: xa_dump changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000409 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: xa_find
- Explanation: xa_find changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000415 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: xa_store
- Explanation: xa_store changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000429 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: xas_split
- Explanation: xas_split changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000002 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __is_module_percpu_address
- Explanation: __is_module_percpu_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000003 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kernfs_create_file
- Explanation: __kernfs_create_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000005 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kunit_add_resource
- Explanation: __kunit_add_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000007 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kunit_test_suites_exit
- Explanation: __kunit_test_suites_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000008 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kunit_test_suites_init
- Explanation: __kunit_test_suites_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000009 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mmdrop
- Explanation: __mmdrop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000010 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __module_address
- Explanation: __module_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000011 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __module_get
- Explanation: __module_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000012 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __module_put_and_kthread_exit
- Explanation: __module_put_and_kthread_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000013 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __module_text_address
- Explanation: __module_text_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000014 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __modver_version_show
- Explanation: __modver_version_show changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000015 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __percpu_counter_init
- Explanation: __percpu_counter_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000016 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __percpu_counter_init_many
- Explanation: __percpu_counter_init_many changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000017 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __radix_tree_lookup
- Explanation: __radix_tree_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000018 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __radix_tree_replace
- Explanation: __radix_tree_replace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000019 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __register_sysctl_init
- Explanation: __register_sysctl_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000021 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __request_module
- Explanation: __request_module changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000023 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __symbol_get_gpl
- Explanation: __symbol_get_gpl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000024 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __symbol_put
- Explanation: __symbol_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000027 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __wake_up_on_current_cpu
- Explanation: __wake_up_on_current_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000029 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __xa_alloc_cyclic
- Explanation: __xa_alloc_cyclic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000030 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __xa_clear_mark
- Explanation: __xa_clear_mark changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000031 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __xa_cmpxchg
- Explanation: __xa_cmpxchg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000032 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __xa_erase
- Explanation: __xa_erase changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000033 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __xa_insert
- Explanation: __xa_insert changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000034 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __xa_set_mark
- Explanation: __xa_set_mark changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000035 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __xa_store
- Explanation: __xa_store changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000036 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __xas_next
- Explanation: __xas_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000037 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __xas_prev
- Explanation: __xas_prev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000038 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: abort
- Explanation: abort changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': '()'}`
- New: `{'params': [], 'return_type': '!'}`

### Rust Evidence

- Graph edges: `1`

## W-000039 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: add_uevent_var
- Explanation: add_uevent_var changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000040 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: align_vdso_addr
- Explanation: align_vdso_addr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000041 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: amd_check_microcode
- Explanation: amd_check_microcode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000043 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_get_unmapped_area_topdown
- Explanation: arch_get_unmapped_area_topdown changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000044 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_pick_mmap_layout
- Explanation: arch_pick_mmap_layout changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000045 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_setup_additional_pages
- Explanation: arch_setup_additional_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000046 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_syscall_is_vdso_sigreturn
- Explanation: arch_syscall_is_vdso_sigreturn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000048 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: build_id_parse_buf
- Explanation: build_id_parse_buf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000052 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_id
- Explanation: class_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000053 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cleanup_module
- Explanation: cleanup_module changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000054 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: compat_arch_setup_additional_pages
- Explanation: compat_arch_setup_additional_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000055 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: compat_only_sysfs_link_entry_to_kobj
- Explanation: compat_only_sysfs_link_entry_to_kobj changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000056 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: compat_start_thread
- Explanation: compat_start_thread changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000057 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: complete_on_current_cpu
- Explanation: complete_on_current_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000059 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_smt_disable
- Explanation: cpu_smt_disable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000060 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_smt_possible
- Explanation: cpu_smt_possible changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000061 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_smt_set_num_threads
- Explanation: cpu_smt_set_num_threads changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000062 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpuhp_smt_disable
- Explanation: cpuhp_smt_disable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000063 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpuhp_smt_enable
- Explanation: cpuhp_smt_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000064 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dereference_module_function_descriptor
- Explanation: dereference_module_function_descriptor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000065 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: destroy_params
- Explanation: destroy_params changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000066 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_exit
- Explanation: do_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'error_code', 'type': 'core::ffi::c_long'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'error_code', 'type': 'core::ffi::c_long'}], 'return_type': '!'}`

### Rust Evidence

- Graph edges: `1`

## W-000067 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_proc_douintvec
- Explanation: do_proc_douintvec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000068 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_sysctl_args
- Explanation: do_sysctl_args changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000069 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: exec_mm_release
- Explanation: exec_mm_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000070 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: exit_mm_release
- Explanation: exit_mm_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000071 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: find_kallsyms_symbol_value
- Explanation: find_kallsyms_symbol_value changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000072 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: find_module
- Explanation: find_module changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000073 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fixup_vdso_exception
- Explanation: fixup_vdso_exception changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000074 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: flags
- Explanation: flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u32_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(16usize, 16u8) as u32) } } #[inline] pub fn set_flags(&mut self, val: u32_) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(24usize, 8u8) as u32) } } #[inline] pub fn set_flags(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000077 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_get_unmapped_area_topdown
- Explanation: generic_get_unmapped_area_topdown changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000078 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_processor_info
- Explanation: generic_processor_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'apicid', 'type': 'core::ffi::c_int'}, {'name': 'version', 'type': 'core::ffi::c_int'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'apicid', 'type': 'core::ffi::c_int'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000079 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_mmap_base
- Explanation: get_mmap_base changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000080 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_sigframe_size
- Explanation: get_sigframe_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000081 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_task_mm
- Explanation: get_task_mm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000083 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hlt_play_dead
- Explanation: hlt_play_dead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': '()'}`
- New: `{'params': [], 'return_type': '!'}`

### Rust Evidence

- Graph edges: `1`

## W-000084 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ida_alloc_range
- Explanation: ida_alloc_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000085 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ida_destroy
- Explanation: ida_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000086 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ida_free
- Explanation: ida_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000089 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: idr_alloc_cyclic
- Explanation: idr_alloc_cyclic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000090 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: idr_alloc_u32
- Explanation: idr_alloc_u32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000091 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: idr_destroy
- Explanation: idr_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000092 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: idr_find
- Explanation: idr_find changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000093 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: idr_for_each
- Explanation: idr_for_each changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000094 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: idr_get_free
- Explanation: idr_get_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000096 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: idr_get_next_ul
- Explanation: idr_get_next_ul changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000097 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: idr_preload
- Explanation: idr_preload changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000098 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: idr_remove
- Explanation: idr_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000099 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: idr_replace
- Explanation: idr_replace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000100 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: init_module
- Explanation: init_module changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000101 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: init_vdso_image
- Explanation: init_vdso_image changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000102 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: init_vmlinux_build_id
- Explanation: init_vmlinux_build_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000103 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_module_address
- Explanation: is_module_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000104 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_module_percpu_address
- Explanation: is_module_percpu_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000105 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_module_text_address
- Explanation: is_module_text_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000106 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_param_lock
- Explanation: kernel_param_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000107 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_param_unlock
- Explanation: kernel_param_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000108 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_activate
- Explanation: kernfs_activate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000109 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_break_active_protection
- Explanation: kernfs_break_active_protection changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000110 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_create_dir_ns
- Explanation: kernfs_create_dir_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000111 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_create_empty_dir
- Explanation: kernfs_create_empty_dir changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000112 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_create_link
- Explanation: kernfs_create_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000113 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_create_root
- Explanation: kernfs_create_root changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000114 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_destroy_root
- Explanation: kernfs_destroy_root changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000115 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_find_and_get_node_by_id
- Explanation: kernfs_find_and_get_node_by_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000116 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_find_and_get_ns
- Explanation: kernfs_find_and_get_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000117 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_free_fs_context
- Explanation: kernfs_free_fs_context changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000118 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_generic_poll
- Explanation: kernfs_generic_poll changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000120 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_get_inode
- Explanation: kernfs_get_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000121 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_get_parent
- Explanation: kernfs_get_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000122 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_get_tree
- Explanation: kernfs_get_tree changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000123 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_init
- Explanation: kernfs_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000124 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_kill_sb
- Explanation: kernfs_kill_sb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000125 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_name
- Explanation: kernfs_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000126 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_node_dentry
- Explanation: kernfs_node_dentry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000127 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_node_from_dentry
- Explanation: kernfs_node_from_dentry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000128 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_notify
- Explanation: kernfs_notify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000129 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_path_from_node
- Explanation: kernfs_path_from_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000130 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_put
- Explanation: kernfs_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000132 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_remove_by_name_ns
- Explanation: kernfs_remove_by_name_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000133 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_remove_self
- Explanation: kernfs_remove_self changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000134 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_rename_ns
- Explanation: kernfs_rename_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000135 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_root_from_sb
- Explanation: kernfs_root_from_sb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000136 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_root_to_node
- Explanation: kernfs_root_to_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000137 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_setattr
- Explanation: kernfs_setattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000138 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_show
- Explanation: kernfs_show changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000139 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_super_ns
- Explanation: kernfs_super_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000140 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_unbreak_active_protection
- Explanation: kernfs_unbreak_active_protection changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000141 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_walk_and_get_ns
- Explanation: kernfs_walk_and_get_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000142 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_xattr_get
- Explanation: kernfs_xattr_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000143 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_xattr_set
- Explanation: kernfs_xattr_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000144 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobj_child_ns_ops
- Explanation: kobj_child_ns_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000145 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobj_ns_current_may_mount
- Explanation: kobj_ns_current_may_mount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000146 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobj_ns_drop
- Explanation: kobj_ns_drop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000147 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobj_ns_grab_current
- Explanation: kobj_ns_grab_current changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000148 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobj_ns_initial
- Explanation: kobj_ns_initial changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000149 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobj_ns_netlink
- Explanation: kobj_ns_netlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000150 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobj_ns_ops
- Explanation: kobj_ns_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000152 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobj_ns_type_registered
- Explanation: kobj_ns_type_registered changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000153 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobject_add
- Explanation: kobject_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000154 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobject_create_and_add
- Explanation: kobject_create_and_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000155 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobject_del
- Explanation: kobject_del changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000157 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobject_get_ownership
- Explanation: kobject_get_ownership changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000158 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobject_get_path
- Explanation: kobject_get_path changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000159 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobject_get_unless_zero
- Explanation: kobject_get_unless_zero changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000161 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobject_init_and_add
- Explanation: kobject_init_and_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000162 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobject_move
- Explanation: kobject_move changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000163 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobject_namespace
- Explanation: kobject_namespace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000164 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobject_put
- Explanation: kobject_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000165 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobject_rename
- Explanation: kobject_rename changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000167 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobject_set_name_vargs
- Explanation: kobject_set_name_vargs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000168 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobject_synth_uevent
- Explanation: kobject_synth_uevent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000170 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobject_uevent_env
- Explanation: kobject_uevent_env changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000171 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kset_create_and_add
- Explanation: kset_create_and_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000172 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kset_find_obj
- Explanation: kset_find_obj changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000173 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kset_init
- Explanation: kset_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000174 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kset_register
- Explanation: kset_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000175 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kset_unregister
- Explanation: kset_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000176 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_action
- Explanation: kunit_action changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000178 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_add_action_or_reset
- Explanation: kunit_add_action_or_reset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000179 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_assert_prologue
- Explanation: kunit_assert_prologue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000180 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_binary_assert_format
- Explanation: kunit_binary_assert_format changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000181 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_binary_ptr_assert_format
- Explanation: kunit_binary_ptr_assert_format changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000182 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_binary_str_assert_format
- Explanation: kunit_binary_str_assert_format changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000183 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_cleanup
- Explanation: kunit_cleanup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000184 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_destroy_resource
- Explanation: kunit_destroy_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000185 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_enabled
- Explanation: kunit_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000186 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_exec_list_tests
- Explanation: kunit_exec_list_tests changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000187 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_exec_run_tests
- Explanation: kunit_exec_run_tests changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000188 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_fail_assert_format
- Explanation: kunit_fail_assert_format changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000190 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_filter_action
- Explanation: kunit_filter_action changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000191 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_filter_glob
- Explanation: kunit_filter_glob changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000192 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_filter_suites
- Explanation: kunit_filter_suites changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000193 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_free_suite_set
- Explanation: kunit_free_suite_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000195 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_init_test
- Explanation: kunit_init_test changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000196 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_kfree
- Explanation: kunit_kfree changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000197 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_kmalloc_array
- Explanation: kunit_kmalloc_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000198 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_log_append
- Explanation: kunit_log_append changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000199 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_mem_assert_format
- Explanation: kunit_mem_assert_format changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000200 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_ptr_not_err_assert_format
- Explanation: kunit_ptr_not_err_assert_format changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000201 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_release_action
- Explanation: kunit_release_action changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000202 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_remove_action
- Explanation: kunit_remove_action changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000203 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_remove_resource
- Explanation: kunit_remove_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000204 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_run_tests
- Explanation: kunit_run_tests changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000205 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_suite_has_succeeded
- Explanation: kunit_suite_has_succeeded changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000206 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_suite_num_test_cases
- Explanation: kunit_suite_num_test_cases changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000207 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_test_case_num
- Explanation: kunit_test_case_num changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000208 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_try_catch_run
- Explanation: kunit_try_catch_run changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000209 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_try_catch_throw
- Explanation: kunit_try_catch_throw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000211 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lineno
- Explanation: lineno changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000212 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lookup_module_symbol_attrs
- Explanation: lookup_module_symbol_attrs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000213 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lookup_module_symbol_name
- Explanation: lookup_module_symbol_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000214 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: map_vdso_once
- Explanation: map_vdso_once changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000215 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mas_preallocate
- Explanation: mas_preallocate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'mas', 'type': '*mut ma_state'}, {'name': 'gfp', 'type': 'gfp_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'mas', 'type': '*mut ma_state'}, {'name': 'entry', 'type': '*mut core::ffi::c_void'}, {'name': 'gfp', 'type': 'gfp_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000216 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: membarrier_exec_mmap
- Explanation: membarrier_exec_mmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000217 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: membarrier_update_current_mm
- Explanation: membarrier_update_current_mm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000218 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mm_access
- Explanation: mm_access changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000219 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mm_alloc
- Explanation: mm_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000220 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmap_address_hint_valid
- Explanation: mmap_address_hint_valid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000221 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmapped
- Explanation: mmapped changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000223 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmput_async
- Explanation: mmput_async changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000224 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: module_address_lookup
- Explanation: module_address_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000225 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: module_bug_cleanup
- Explanation: module_bug_cleanup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000226 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: module_bug_finalize
- Explanation: module_bug_finalize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000227 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: module_get_kallsym
- Explanation: module_get_kallsym changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000228 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: module_kallsyms_lookup_name
- Explanation: module_kallsyms_lookup_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000229 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: module_kallsyms_on_each_symbol
- Explanation: module_kallsyms_on_each_symbol changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000230 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: module_param_sysfs_remove
- Explanation: module_param_sysfs_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000231 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: module_param_sysfs_setup
- Explanation: module_param_sysfs_setup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000232 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: module_put
- Explanation: module_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000233 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: module_refcount
- Explanation: module_refcount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000234 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_bitfield_1
- Explanation: new_bitfield_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'sched_reset_on_fork', 'type': 'core::ffi::c_uint'}, {'name': 'sched_contributes_to_load', 'type': 'core::ffi::c_uint'}, {'name': 'sched_migrated', 'type': 'core::ffi::c_uint'}, {'name': 'sched_remote_wakeup', 'type': 'core::ffi::c_uint'}, {'name': 'in_execve', 'type': 'core::ffi::c_uint'}, {'name': 'in_iowait', 'type': 'core::ffi::c_uint'}, {'name': 'restore_sigmask', 'type': 'core::ffi::c_uint'}, {'name': 'no_cgroup_migration', 'type': 'core::ffi::c_uint'}, {'name': 'frozen', 'type': 'core::ffi::c_uint'}, {'name': 'use_memdelay', 'type': 'core::ffi::c_uint'}, {'name': 'in_eventfd', 'type': 'core::ffi::c_uint'}, {'name': 'reported_split_lock', 'type': 'core::ffi::c_uint'}, {'name': 'in_thrashing', 'type': 'core::ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`
- New: `{'params': [{'name': 'force_atomic', 'type': 'bool_'}, {'name': 'allow_reinit', 'type': 'bool_'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`

### Rust Evidence

- Graph edges: `1`

## W-000235 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: nmi_panic_self_stop
- Explanation: nmi_panic_self_stop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'regs', 'type': '*mut pt_regs'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'regs', 'type': '*mut pt_regs'}], 'return_type': '!'}`

### Rust Evidence

- Graph edges: `1`

## W-000237 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: panic_smp_self_stop
- Explanation: panic_smp_self_stop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': '()'}`
- New: `{'params': [], 'return_type': '!'}`

### Rust Evidence

- Graph edges: `1`

## W-000238 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_free_charp
- Explanation: param_free_charp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000239 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_get_bool
- Explanation: param_get_bool changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000240 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_get_byte
- Explanation: param_get_byte changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000241 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_get_charp
- Explanation: param_get_charp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000242 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_get_hexint
- Explanation: param_get_hexint changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000243 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_get_int
- Explanation: param_get_int changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000244 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_get_invbool
- Explanation: param_get_invbool changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000245 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_get_long
- Explanation: param_get_long changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000246 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_get_short
- Explanation: param_get_short changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000247 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_get_string
- Explanation: param_get_string changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000248 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_get_uint
- Explanation: param_get_uint changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000249 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_get_ullong
- Explanation: param_get_ullong changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000250 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_get_ulong
- Explanation: param_get_ulong changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000251 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_get_ushort
- Explanation: param_get_ushort changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000252 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_set_bint
- Explanation: param_set_bint changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000254 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_set_bool_enable_only
- Explanation: param_set_bool_enable_only changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000255 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_set_byte
- Explanation: param_set_byte changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000256 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_set_charp
- Explanation: param_set_charp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000257 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_set_copystring
- Explanation: param_set_copystring changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000258 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_set_hexint
- Explanation: param_set_hexint changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000259 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_set_int
- Explanation: param_set_int changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000260 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_set_invbool
- Explanation: param_set_invbool changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000261 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_set_long
- Explanation: param_set_long changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000262 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_set_short
- Explanation: param_set_short changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000264 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_set_uint_minmax
- Explanation: param_set_uint_minmax changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000265 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_set_ullong
- Explanation: param_set_ullong changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000266 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_set_ulong
- Explanation: param_set_ulong changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000267 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: param_set_ushort
- Explanation: param_set_ushort changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000269 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: parameqn
- Explanation: parameqn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000276 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: parse_args
- Explanation: parse_args changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000277 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: percpu_counter_destroy
- Explanation: percpu_counter_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000278 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: percpu_counter_destroy_many
- Explanation: percpu_counter_destroy_many changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000279 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pr_cont_kernfs_name
- Explanation: pr_cont_kernfs_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000280 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pr_cont_kernfs_path
- Explanation: pr_cont_kernfs_path changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000281 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: print_modules
- Explanation: print_modules changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000282 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_do_large_bitmap
- Explanation: proc_do_large_bitmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000283 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_do_static_key
- Explanation: proc_do_static_key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000284 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_dobool
- Explanation: proc_dobool changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000286 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_dointvec_jiffies
- Explanation: proc_dointvec_jiffies changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000287 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_dointvec_minmax
- Explanation: proc_dointvec_minmax changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000289 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_dointvec_ms_jiffies_minmax
- Explanation: proc_dointvec_ms_jiffies_minmax changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000290 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_dointvec_userhz_jiffies
- Explanation: proc_dointvec_userhz_jiffies changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000291 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_dostring
- Explanation: proc_dostring changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000292 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_dou8vec_minmax
- Explanation: proc_dou8vec_minmax changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000294 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_douintvec_minmax
- Explanation: proc_douintvec_minmax changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000295 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_doulongvec_minmax
- Explanation: proc_doulongvec_minmax changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000296 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_doulongvec_ms_jiffies_minmax
- Explanation: proc_doulongvec_ms_jiffies_minmax changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000297 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_sys_poll_notify
- Explanation: proc_sys_poll_notify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000299 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: radix_tree_delete_item
- Explanation: radix_tree_delete_item changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000302 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: radix_tree_gang_lookup_tag_slot
- Explanation: radix_tree_gang_lookup_tag_slot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000303 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: radix_tree_init
- Explanation: radix_tree_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000304 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: radix_tree_insert
- Explanation: radix_tree_insert changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000305 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: radix_tree_iter_delete
- Explanation: radix_tree_iter_delete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000306 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: radix_tree_iter_replace
- Explanation: radix_tree_iter_replace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000307 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: radix_tree_iter_resume
- Explanation: radix_tree_iter_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000308 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: radix_tree_iter_tag_clear
- Explanation: radix_tree_iter_tag_clear changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000310 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: radix_tree_lookup_slot
- Explanation: radix_tree_lookup_slot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000311 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: radix_tree_maybe_preload
- Explanation: radix_tree_maybe_preload changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000312 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: radix_tree_next_chunk
- Explanation: radix_tree_next_chunk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000314 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: radix_tree_replace_slot
- Explanation: radix_tree_replace_slot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000315 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: radix_tree_tag_clear
- Explanation: radix_tree_tag_clear changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000316 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: radix_tree_tag_get
- Explanation: radix_tree_tag_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000317 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: radix_tree_tag_set
- Explanation: radix_tree_tag_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000318 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: radix_tree_tagged
- Explanation: radix_tree_tagged changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000319 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rcu_request_urgent_qs_task
- Explanation: rcu_request_urgent_qs_task changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000320 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: register_module_notifier
- Explanation: register_module_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000321 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: register_sysctl_mount_point
- Explanation: register_sysctl_mount_point changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000322 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: register_sysctl_sz
- Explanation: register_sysctl_sz changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000323 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: released
- Explanation: released changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000324 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: retire_sysctl_set
- Explanation: retire_sysctl_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000325 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: retpoline_module_ok
- Explanation: retpoline_module_ok changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000326 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_module_sig_enforced
- Explanation: set_module_sig_enforced changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000327 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_personality_64bit
- Explanation: set_personality_64bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000328 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_personality_ia32
- Explanation: set_personality_ia32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000329 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: setup_sysctl_set
- Explanation: setup_sysctl_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000332 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: state_add_uevent_sent
- Explanation: state_add_uevent_sent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000333 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: state_in_sysfs
- Explanation: state_in_sysfs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000334 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: state_initialized
- Explanation: state_initialized changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000335 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: state_remove_uevent_sent
- Explanation: state_remove_uevent_sent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000336 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stop_this_cpu
- Explanation: stop_this_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'dummy', 'type': '*mut core::ffi::c_void'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'dummy', 'type': '*mut core::ffi::c_void'}], 'return_type': '!'}`

### Rust Evidence

- Graph edges: `1`

## W-000337 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: swake_up_locked
- Explanation: swake_up_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'q', 'type': '*mut swait_queue_head'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'q', 'type': '*mut swait_queue_head'}, {'name': 'wake_flags', 'type': 'core::ffi::c_int'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000338 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: symbol_put_addr
- Explanation: symbol_put_addr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000339 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysctl_init_bases
- Explanation: sysctl_init_bases changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000340 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysctl_max_threads
- Explanation: sysctl_max_threads changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000341 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_add_file_to_group
- Explanation: sysfs_add_file_to_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000342 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_add_link_to_group
- Explanation: sysfs_add_link_to_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000343 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_break_active_protection
- Explanation: sysfs_break_active_protection changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000344 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_change_owner
- Explanation: sysfs_change_owner changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000345 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_chmod_file
- Explanation: sysfs_chmod_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000346 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_create_bin_file
- Explanation: sysfs_create_bin_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000347 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_create_dir_ns
- Explanation: sysfs_create_dir_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000348 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_create_file_ns
- Explanation: sysfs_create_file_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000349 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_create_files
- Explanation: sysfs_create_files changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000351 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_create_groups
- Explanation: sysfs_create_groups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000353 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_create_link_nowarn
- Explanation: sysfs_create_link_nowarn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000354 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_create_mount_point
- Explanation: sysfs_create_mount_point changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000355 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_delete_link
- Explanation: sysfs_delete_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000357 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_emit_at
- Explanation: sysfs_emit_at changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000358 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_file_change_owner
- Explanation: sysfs_file_change_owner changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000359 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_group_change_owner
- Explanation: sysfs_group_change_owner changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000360 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_groups_change_owner
- Explanation: sysfs_groups_change_owner changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000361 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_init
- Explanation: sysfs_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000362 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_link_change_owner
- Explanation: sysfs_link_change_owner changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000363 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_merge_group
- Explanation: sysfs_merge_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000364 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_move_dir_ns
- Explanation: sysfs_move_dir_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000365 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_notify
- Explanation: sysfs_notify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000366 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_remove_bin_file
- Explanation: sysfs_remove_bin_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000367 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_remove_dir
- Explanation: sysfs_remove_dir changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000368 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_remove_file_from_group
- Explanation: sysfs_remove_file_from_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000369 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_remove_file_ns
- Explanation: sysfs_remove_file_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000370 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_remove_file_self
- Explanation: sysfs_remove_file_self changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000371 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_remove_files
- Explanation: sysfs_remove_files changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000373 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_remove_groups
- Explanation: sysfs_remove_groups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000375 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_remove_link_from_group
- Explanation: sysfs_remove_link_from_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000376 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_remove_mount_point
- Explanation: sysfs_remove_mount_point changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000377 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_rename_dir_ns
- Explanation: sysfs_rename_dir_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000378 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_rename_link_ns
- Explanation: sysfs_rename_link_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000379 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_unbreak_active_protection
- Explanation: sysfs_unbreak_active_protection changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000380 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_unmerge_group
- Explanation: sysfs_unmerge_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000382 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_update_groups
- Explanation: sysfs_update_groups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000383 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: task_size_32bit
- Explanation: task_size_32bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000384 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: task_size_64bit
- Explanation: task_size_64bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000386 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: try_module_get
- Explanation: try_module_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000387 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: uevent_suppress
- Explanation: uevent_suppress changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000388 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unregister_module_notifier
- Explanation: unregister_module_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000389 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unregister_sysctl_table
- Explanation: unregister_sysctl_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000393 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: workqueue_init_topology
- Explanation: workqueue_init_topology changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000394 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: x86_fsbase_read_task
- Explanation: x86_fsbase_read_task changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000395 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: x86_fsbase_write_task
- Explanation: x86_fsbase_write_task changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000396 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: x86_fsgsbase_read_task
- Explanation: x86_fsgsbase_read_task changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000397 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: x86_gsbase_read_cpu_inactive
- Explanation: x86_gsbase_read_cpu_inactive changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000398 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: x86_gsbase_read_task
- Explanation: x86_gsbase_read_task changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000399 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: x86_gsbase_write_cpu_inactive
- Explanation: x86_gsbase_write_cpu_inactive changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000400 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: x86_gsbase_write_task
- Explanation: x86_gsbase_write_task changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000402 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xa_clear_mark
- Explanation: xa_clear_mark changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000403 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xa_delete_node
- Explanation: xa_delete_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000404 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xa_destroy
- Explanation: xa_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000406 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xa_dump_node
- Explanation: xa_dump_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000407 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xa_erase
- Explanation: xa_erase changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000408 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xa_extract
- Explanation: xa_extract changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000410 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xa_find_after
- Explanation: xa_find_after changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000411 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xa_get_mark
- Explanation: xa_get_mark changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000412 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xa_get_order
- Explanation: xa_get_order changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000413 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xa_load
- Explanation: xa_load changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000414 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xa_set_mark
- Explanation: xa_set_mark changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000416 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xa_store_range
- Explanation: xa_store_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000417 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xas_clear_mark
- Explanation: xas_clear_mark changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000418 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xas_create_range
- Explanation: xas_create_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000419 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xas_destroy
- Explanation: xas_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000421 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xas_find_conflict
- Explanation: xas_find_conflict changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000422 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xas_find_marked
- Explanation: xas_find_marked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000423 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xas_get_mark
- Explanation: xas_get_mark changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000424 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xas_init_marks
- Explanation: xas_init_marks changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000425 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xas_load
- Explanation: xas_load changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000426 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xas_nomem
- Explanation: xas_nomem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000427 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xas_pause
- Explanation: xas_pause changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000428 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xas_set_mark
- Explanation: xas_set_mark changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000430 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xas_split_alloc
- Explanation: xas_split_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000431 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xas_store
- Explanation: xas_store changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000450 FieldDrift

- Risk: High
- Score: 10.8
- Symbol: local_apic__bindgen_ty_3
- Explanation: local_apic__bindgen_ty_3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]'}, {'name': '__reserved', 'type': '[core::ffi::c_uint; 3usize]'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u32; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': '__reserved', 'type': '[core::ffi::c_uint; 3usize]'}]`

### Rust Evidence

- Graph edges: `11`

## W-000516 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmalloc_node_trace
- Explanation: kmalloc_node_trace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['kmalloc_caches[kmalloc_type(flags)][index]', 'flags', 'node', 'size'], 'return_type': 'return'}`
- New: `{'params': ['kmalloc_caches[kmalloc_type(flags, _RET_IP_)][index]', 'flags', 'node', 'size'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `1`

## W-000517 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmalloc_trace
- Explanation: kmalloc_trace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['kmalloc_caches[kmalloc_type(flags)][index]', 'flags', 'size'], 'return_type': 'return'}`
- New: `{'params': ['kmalloc_caches[kmalloc_type(flags, _RET_IP_)][index]', 'flags', 'size'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `1`

## W-000518 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmalloc_type
- Explanation: kmalloc_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['gfp_t flags'], 'return_type': 'static __always_inline enum kmalloc_cache_type'}`
- New: `{'params': ['gfp_t flags', 'unsigned long caller'], 'return_type': 'static __always_inline enum kmalloc_cache_type'}`

### Rust Evidence

- Graph edges: `1`

## W-000469 FieldDrift

- Risk: High
- Score: 10.4
- Symbol: task_struct
- Explanation: task_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'core::ffi::c_uint'}, {'name': 'stack', 'type': '*mut core::ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'ptrace', 'type': 'core::ffi::c_uint'}, {'name': 'on_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'core::ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'core::ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_cpu', 'type': 'core::ffi::c_int'}, {'name': 'on_rq', 'type': 'core::ffi::c_int'}, {'name': 'prio', 'type': 'core::ffi::c_int'}, {'name': 'static_prio', 'type': 'core::ffi::c_int'}, {'name': 'normal_prio', 'type': 'core::ffi::c_int'}, {'name': 'rt_priority', 'type': 'core::ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': '__bindgen_padding_1', 'type': '[u64; 4usize]'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'core::ffi::c_uint'}, {'name': 'policy', 'type': 'core::ffi::c_uint'}, {'name': 'nr_cpus_allowed', 'type': 'core::ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut core::ffi::c_void'}, {'name': 'migration_disabled', 'type': 'core::ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'core::ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'core::ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'core::ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'exit_state', 'type': 'core::ffi::c_int'}, {'name': 'exit_code', 'type': 'core::ffi::c_int'}, {'name': 'exit_signal', 'type': 'core::ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'core::ffi::c_int'}, {'name': 'jobctl', 'type': 'core::ffi::c_ulong'}, {'name': 'personality', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]'}, {'name': 'atomic_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'core::ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_group', 'type': 'list_head'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'worker_private', 'type': '*mut core::ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*mut cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[core::ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'core::ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'core::ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'core::ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'journal_info', 'type': '*mut core::ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'core::ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cpuset_slab_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'core::ffi::c_uint'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'core::ffi::c_short'}, {'name': 'pref_node_fork', 'type': 'core::ffi::c_short'}, {'name': 'rseq', 'type': '*mut rseq'}, {'name': 'rseq_len', 'type': 'u32_'}, {'name': 'rseq_sig', 'type': 'u32_'}, {'name': 'rseq_event_mask', 'type': 'core::ffi::c_ulong'}, {'name': 'mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'last_mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'migrate_from_cpu', 'type': 'core::ffi::c_int'}, {'name': 'mm_cid_active', 'type': 'core::ffi::c_int'}, {'name': 'cid_work', 'type': 'callback_head'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'core::ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'core::ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'core::ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'core::ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'core::ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_vaddr', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'core::ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': '__bindgen_padding_2', 'type': 'u64'}, {'name': 'thread', 'type': 'thread_struct'}]`
- New: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'core::ffi::c_uint'}, {'name': 'stack', 'type': '*mut core::ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'ptrace', 'type': 'core::ffi::c_uint'}, {'name': 'on_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'core::ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'core::ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_cpu', 'type': 'core::ffi::c_int'}, {'name': 'on_rq', 'type': 'core::ffi::c_int'}, {'name': 'prio', 'type': 'core::ffi::c_int'}, {'name': 'static_prio', 'type': 'core::ffi::c_int'}, {'name': 'normal_prio', 'type': 'core::ffi::c_int'}, {'name': 'rt_priority', 'type': 'core::ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': '__bindgen_padding_1', 'type': '[u64; 4usize]'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'core::ffi::c_uint'}, {'name': 'policy', 'type': 'core::ffi::c_uint'}, {'name': 'nr_cpus_allowed', 'type': 'core::ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut core::ffi::c_void'}, {'name': 'migration_disabled', 'type': 'core::ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'core::ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'core::ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'core::ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'exit_state', 'type': 'core::ffi::c_int'}, {'name': 'exit_code', 'type': 'core::ffi::c_int'}, {'name': 'exit_signal', 'type': 'core::ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'core::ffi::c_int'}, {'name': 'jobctl', 'type': 'core::ffi::c_ulong'}, {'name': 'personality', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'core::ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_group', 'type': 'list_head'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'worker_private', 'type': '*mut core::ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[core::ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'core::ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'core::ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'core::ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'journal_info', 'type': '*mut core::ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'core::ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cpuset_slab_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'core::ffi::c_uint'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'core::ffi::c_short'}, {'name': 'pref_node_fork', 'type': 'core::ffi::c_short'}, {'name': 'rseq', 'type': '*mut rseq'}, {'name': 'rseq_len', 'type': 'u32_'}, {'name': 'rseq_sig', 'type': 'u32_'}, {'name': 'rseq_event_mask', 'type': 'core::ffi::c_ulong'}, {'name': 'mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'last_mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'migrate_from_cpu', 'type': 'core::ffi::c_int'}, {'name': 'mm_cid_active', 'type': 'core::ffi::c_int'}, {'name': 'cid_work', 'type': 'callback_head'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'core::ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'core::ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'core::ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'core::ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'core::ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_vaddr', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'core::ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': '__bindgen_padding_2', 'type': 'u64'}, {'name': 'thread', 'type': 'thread_struct'}]`

### Rust Evidence

- Graph edges: `9`

## W-000436 FieldDrift

- Risk: High
- Score: 10.2
- Symbol: ctl_table
- Explanation: ctl_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'procname', 'type': '*const core::ffi::c_char'}, {'name': 'data', 'type': '*mut core::ffi::c_void'}, {'name': 'maxlen', 'type': 'core::ffi::c_int'}, {'name': 'mode', 'type': 'umode_t'}, {'name': 'type_', 'type': 'ctl_table__bindgen_ty_1'}, {'name': 'proc_handler', 'type': 'proc_handler'}, {'name': 'poll', 'type': '*mut ctl_table_poll'}, {'name': 'extra1', 'type': '*mut core::ffi::c_void'}, {'name': 'extra2', 'type': '*mut core::ffi::c_void'}]`

### Rust Evidence

- Graph edges: `8`

## W-000058 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: cpu_has_ibpb_brtype_microcode
- Explanation: cpu_has_ibpb_brtype_microcode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000075 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: folio_test_hugetlb
- Explanation: folio_test_hugetlb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000082 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: hard_smp_processor_id
- Explanation: hard_smp_processor_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000087 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: identify_boot_cpu
- Explanation: identify_boot_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000270 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: paravirt_end_context_switch
- Explanation: paravirt_end_context_switch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000271 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: paravirt_enter_lazy_mmu
- Explanation: paravirt_enter_lazy_mmu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000272 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: paravirt_flush_lazy_mmu
- Explanation: paravirt_flush_lazy_mmu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000273 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: paravirt_get_lazy_mode
- Explanation: paravirt_get_lazy_mode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000274 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: paravirt_leave_lazy_mmu
- Explanation: paravirt_leave_lazy_mmu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000275 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: paravirt_start_context_switch
- Explanation: paravirt_start_context_switch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000330 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: smp_park_other_cpus_in_init
- Explanation: smp_park_other_cpus_in_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000331 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: smp_store_boot_cpu_info
- Explanation: smp_store_boot_cpu_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000385 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: topology_smt_supported
- Explanation: topology_smt_supported changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000401 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: x86_idle_thread_init
- Explanation: x86_idle_thread_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000457 FieldDrift

- Risk: Medium
- Score: 9.6
- Symbol: local_apic__bindgen_ty_4
- Explanation: local_apic__bindgen_ty_4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]'}, {'name': '__reserved', 'type': '[core::ffi::c_uint; 3usize]'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': '__reserved', 'type': '[core::ffi::c_uint; 3usize]'}]`

### Rust Evidence

- Graph edges: `5`

## W-000474 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: vm_area_struct
- Explanation: vm_area_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'vm_area_struct__bindgen_ty_1'}, {'name': 'vm_mm', 'type': '*mut mm_struct'}, {'name': 'vm_page_prot', 'type': 'pgprot_t'}, {'name': '__bindgen_anon_2', 'type': 'vm_area_struct__bindgen_ty_2'}, {'name': 'vm_lock_seq', 'type': 'core::ffi::c_int'}, {'name': 'vm_lock', 'type': '*mut vma_lock'}, {'name': 'detached', 'type': 'bool_'}, {'name': 'shared', 'type': 'vm_area_struct__bindgen_ty_3'}, {'name': 'anon_vma_chain', 'type': 'list_head'}, {'name': 'anon_vma', 'type': '*mut anon_vma'}, {'name': 'vm_ops', 'type': '*mut vm_operations_struct'}, {'name': 'vm_pgoff', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_file', 'type': '*mut file'}, {'name': 'vm_private_data', 'type': '*mut core::ffi::c_void'}, {'name': 'swap_readahead_info', 'type': 'atomic_long_t'}, {'name': 'vm_policy', 'type': '*mut mempolicy'}, {'name': 'vm_userfaultfd_ctx', 'type': 'vm_userfaultfd_ctx'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'vm_area_struct__bindgen_ty_1'}, {'name': 'vm_mm', 'type': '*mut mm_struct'}, {'name': 'vm_page_prot', 'type': 'pgprot_t'}, {'name': '__bindgen_anon_2', 'type': 'vm_area_struct__bindgen_ty_2'}, {'name': 'vm_lock_seq', 'type': 'core::ffi::c_int'}, {'name': 'vm_lock', 'type': '*mut vma_lock'}, {'name': 'detached', 'type': 'bool_'}, {'name': 'shared', 'type': 'vm_area_struct__bindgen_ty_3'}, {'name': 'anon_vma_chain', 'type': 'list_head'}, {'name': 'anon_vma', 'type': '*mut anon_vma'}, {'name': 'vm_ops', 'type': '*const vm_operations_struct'}, {'name': 'vm_pgoff', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_file', 'type': '*mut file'}, {'name': 'vm_private_data', 'type': '*mut core::ffi::c_void'}, {'name': 'swap_readahead_info', 'type': 'atomic_long_t'}, {'name': 'vm_policy', 'type': '*mut mempolicy'}, {'name': 'vm_userfaultfd_ctx', 'type': 'vm_userfaultfd_ctx'}]`

### Rust Evidence

- Graph edges: `3`

## W-000432 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: __kernel_timex
- Explanation: __kernel_timex changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'modes', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]'}, {'name': 'offset', 'type': 'core::ffi::c_longlong'}, {'name': 'freq', 'type': 'core::ffi::c_longlong'}, {'name': 'maxerror', 'type': 'core::ffi::c_longlong'}, {'name': 'esterror', 'type': 'core::ffi::c_longlong'}, {'name': 'status', 'type': 'core::ffi::c_int'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 4usize]'}, {'name': 'constant', 'type': 'core::ffi::c_longlong'}, {'name': 'precision', 'type': 'core::ffi::c_longlong'}, {'name': 'tolerance', 'type': 'core::ffi::c_longlong'}, {'name': 'time', 'type': '__kernel_timex_timeval'}, {'name': 'tick', 'type': 'core::ffi::c_longlong'}, {'name': 'ppsfreq', 'type': 'core::ffi::c_longlong'}, {'name': 'jitter', 'type': 'core::ffi::c_longlong'}, {'name': 'shift', 'type': 'core::ffi::c_int'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 4usize]'}, {'name': 'stabil', 'type': 'core::ffi::c_longlong'}, {'name': 'jitcnt', 'type': 'core::ffi::c_longlong'}, {'name': 'calcnt', 'type': 'core::ffi::c_longlong'}, {'name': 'errcnt', 'type': 'core::ffi::c_longlong'}, {'name': 'stbcnt', 'type': 'core::ffi::c_longlong'}, {'name': 'tai', 'type': 'core::ffi::c_int'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 44usize]'}]`
- New: `[{'name': 'modes', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': 'offset', 'type': 'core::ffi::c_longlong'}, {'name': 'freq', 'type': 'core::ffi::c_longlong'}, {'name': 'maxerror', 'type': 'core::ffi::c_longlong'}, {'name': 'esterror', 'type': 'core::ffi::c_longlong'}, {'name': 'status', 'type': 'core::ffi::c_int'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': 'constant', 'type': 'core::ffi::c_longlong'}, {'name': 'precision', 'type': 'core::ffi::c_longlong'}, {'name': 'tolerance', 'type': 'core::ffi::c_longlong'}, {'name': 'time', 'type': '__kernel_timex_timeval'}, {'name': 'tick', 'type': 'core::ffi::c_longlong'}, {'name': 'ppsfreq', 'type': 'core::ffi::c_longlong'}, {'name': 'jitter', 'type': 'core::ffi::c_longlong'}, {'name': 'shift', 'type': 'core::ffi::c_int'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': 'stabil', 'type': 'core::ffi::c_longlong'}, {'name': 'jitcnt', 'type': 'core::ffi::c_longlong'}, {'name': 'calcnt', 'type': 'core::ffi::c_longlong'}, {'name': 'errcnt', 'type': 'core::ffi::c_longlong'}, {'name': 'stbcnt', 'type': 'core::ffi::c_longlong'}, {'name': 'tai', 'type': 'core::ffi::c_int'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 44usize]>'}]`

### Rust Evidence

- Graph edges: `2`

## W-000437 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: folio__bindgen_ty_1__bindgen_ty_1
- Explanation: folio__bindgen_ty_1__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'folio__bindgen_ty_1__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mapping', 'type': '*mut address_space'}, {'name': 'index', 'type': 'core::ffi::c_ulong'}, {'name': 'private', 'type': '*mut core::ffi::c_void'}, {'name': '_mapcount', 'type': 'atomic_t'}, {'name': '_refcount', 'type': 'atomic_t'}]`
- New: `[{'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'folio__bindgen_ty_1__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mapping', 'type': '*mut address_space'}, {'name': 'index', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_2', 'type': 'folio__bindgen_ty_1__bindgen_ty_1__bindgen_ty_2'}, {'name': '_mapcount', 'type': 'atomic_t'}, {'name': '_refcount', 'type': 'atomic_t'}]`

### Rust Evidence

- Graph edges: `2`

## W-000460 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: maple_tree
- Explanation: maple_tree changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'maple_tree__bindgen_ty_1'}, {'name': 'ma_root', 'type': '*mut core::ffi::c_void'}, {'name': 'ma_flags', 'type': 'core::ffi::c_uint'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'maple_tree__bindgen_ty_1'}, {'name': 'ma_flags', 'type': 'core::ffi::c_uint'}, {'name': 'ma_root', 'type': '*mut core::ffi::c_void'}]`

### Rust Evidence

- Graph edges: `2`

## W-000433 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: alt_instr__bindgen_ty_1__bindgen_ty_1
- Explanation: alt_instr__bindgen_ty_1__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u16; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000434 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: cpuinfo_x86
- Explanation: cpuinfo_x86 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'x86', 'type': '__u8'}, {'name': 'x86_vendor', 'type': '__u8'}, {'name': 'x86_model', 'type': '__u8'}, {'name': 'x86_stepping', 'type': '__u8'}, {'name': 'x86_tlbsize', 'type': 'core::ffi::c_int'}, {'name': 'vmx_capability', 'type': '[__u32; 5usize]'}, {'name': 'x86_virt_bits', 'type': '__u8'}, {'name': 'x86_phys_bits', 'type': '__u8'}, {'name': 'x86_coreid_bits', 'type': '__u8'}, {'name': 'cu_id', 'type': '__u8'}, {'name': 'extended_cpuid_level', 'type': '__u32'}, {'name': 'cpuid_level', 'type': 'core::ffi::c_int'}, {'name': '__bindgen_anon_1', 'type': 'cpuinfo_x86__bindgen_ty_1'}, {'name': 'x86_vendor_id', 'type': '[core::ffi::c_char; 16usize]'}, {'name': 'x86_model_id', 'type': '[core::ffi::c_char; 64usize]'}, {'name': 'x86_cache_size', 'type': 'core::ffi::c_uint'}, {'name': 'x86_cache_alignment', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_max_rmid', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_occ_scale', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_mbm_width_offset', 'type': 'core::ffi::c_int'}, {'name': 'x86_power', 'type': 'core::ffi::c_int'}, {'name': 'loops_per_jiffy', 'type': 'core::ffi::c_ulong'}, {'name': 'ppin', 'type': 'u64_'}, {'name': 'x86_max_cores', 'type': 'u16_'}, {'name': 'apicid', 'type': 'u16_'}, {'name': 'initial_apicid', 'type': 'u16_'}, {'name': 'x86_clflush_size', 'type': 'u16_'}, {'name': 'booted_cores', 'type': 'u16_'}, {'name': 'phys_proc_id', 'type': 'u16_'}, {'name': 'logical_proc_id', 'type': 'u16_'}, {'name': 'cpu_core_id', 'type': 'u16_'}, {'name': 'cpu_die_id', 'type': 'u16_'}, {'name': 'logical_die_id', 'type': 'u16_'}, {'name': 'cpu_index', 'type': 'u16_'}, {'name': 'smt_active', 'type': 'bool_'}, {'name': 'microcode', 'type': 'u32_'}, {'name': 'x86_cache_bits', 'type': 'u8_'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]'}, {'name': '__bindgen_padding_0', 'type': 'u16'}]`
- New: `[{'name': 'x86', 'type': '__u8'}, {'name': 'x86_vendor', 'type': '__u8'}, {'name': 'x86_model', 'type': '__u8'}, {'name': 'x86_stepping', 'type': '__u8'}, {'name': 'x86_tlbsize', 'type': 'core::ffi::c_int'}, {'name': 'vmx_capability', 'type': '[__u32; 5usize]'}, {'name': 'x86_virt_bits', 'type': '__u8'}, {'name': 'x86_phys_bits', 'type': '__u8'}, {'name': 'x86_coreid_bits', 'type': '__u8'}, {'name': 'cu_id', 'type': '__u8'}, {'name': 'extended_cpuid_level', 'type': '__u32'}, {'name': 'cpuid_level', 'type': 'core::ffi::c_int'}, {'name': '__bindgen_anon_1', 'type': 'cpuinfo_x86__bindgen_ty_1'}, {'name': 'x86_vendor_id', 'type': '[core::ffi::c_char; 16usize]'}, {'name': 'x86_model_id', 'type': '[core::ffi::c_char; 64usize]'}, {'name': 'x86_cache_size', 'type': 'core::ffi::c_uint'}, {'name': 'x86_cache_alignment', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_max_rmid', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_occ_scale', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_mbm_width_offset', 'type': 'core::ffi::c_int'}, {'name': 'x86_power', 'type': 'core::ffi::c_int'}, {'name': 'loops_per_jiffy', 'type': 'core::ffi::c_ulong'}, {'name': 'ppin', 'type': 'u64_'}, {'name': 'x86_max_cores', 'type': 'u16_'}, {'name': 'apicid', 'type': 'u16_'}, {'name': 'initial_apicid', 'type': 'u16_'}, {'name': 'x86_clflush_size', 'type': 'u16_'}, {'name': 'booted_cores', 'type': 'u16_'}, {'name': 'phys_proc_id', 'type': 'u16_'}, {'name': 'logical_proc_id', 'type': 'u16_'}, {'name': 'cpu_core_id', 'type': 'u16_'}, {'name': 'cpu_die_id', 'type': 'u16_'}, {'name': 'logical_die_id', 'type': 'u16_'}, {'name': 'cpu_index', 'type': 'u16_'}, {'name': 'smt_active', 'type': 'bool_'}, {'name': 'microcode', 'type': 'u32_'}, {'name': 'x86_cache_bits', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': 'u16'}]`

### Rust Evidence

- Graph edges: `1`

## W-000435 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: cred
- Explanation: cred changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[]`

### Rust Evidence

- Graph edges: `1`

## W-000438 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: folio__bindgen_ty_2__bindgen_ty_1
- Explanation: folio__bindgen_ty_2__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_flags_1', 'type': 'core::ffi::c_ulong'}, {'name': '_head_1', 'type': 'core::ffi::c_ulong'}, {'name': '_folio_dtor', 'type': 'core::ffi::c_uchar'}, {'name': '_folio_order', 'type': 'core::ffi::c_uchar'}, {'name': '_entire_mapcount', 'type': 'atomic_t'}, {'name': '_nr_pages_mapped', 'type': 'atomic_t'}, {'name': '_pincount', 'type': 'atomic_t'}, {'name': '_folio_nr_pages', 'type': 'core::ffi::c_uint'}]`
- New: `[{'name': '_flags_1', 'type': 'core::ffi::c_ulong'}, {'name': '_head_1', 'type': 'core::ffi::c_ulong'}, {'name': '_folio_avail', 'type': 'core::ffi::c_ulong'}, {'name': '_entire_mapcount', 'type': 'atomic_t'}, {'name': '_nr_pages_mapped', 'type': 'atomic_t'}, {'name': '_pincount', 'type': 'atomic_t'}, {'name': '_folio_nr_pages', 'type': 'core::ffi::c_uint'}]`

### Rust Evidence

- Graph edges: `1`

## W-000439 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: fpstate
- Explanation: fpstate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'size', 'type': 'core::ffi::c_uint'}, {'name': 'user_size', 'type': 'core::ffi::c_uint'}, {'name': 'xfeatures', 'type': 'u64_'}, {'name': 'user_xfeatures', 'type': 'u64_'}, {'name': 'xfd', 'type': 'u64_'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]'}, {'name': '__bindgen_padding_0', 'type': '[u64; 3usize]'}, {'name': 'regs', 'type': 'fpregs_state'}]`
- New: `[{'name': 'size', 'type': 'core::ffi::c_uint'}, {'name': 'user_size', 'type': 'core::ffi::c_uint'}, {'name': 'xfeatures', 'type': 'u64_'}, {'name': 'user_xfeatures', 'type': 'u64_'}, {'name': 'xfd', 'type': 'u64_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u64; 3usize]'}, {'name': 'regs', 'type': 'fpregs_state'}]`

### Rust Evidence

- Graph edges: `1`

## W-000440 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: hrtimer_cpu_base
- Explanation: hrtimer_cpu_base changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'lock', 'type': 'raw_spinlock_t'}, {'name': 'cpu', 'type': 'core::ffi::c_uint'}, {'name': 'active_bases', 'type': 'core::ffi::c_uint'}, {'name': 'clock_was_set_seq', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]'}, {'name': 'nr_events', 'type': 'core::ffi::c_uint'}, {'name': 'nr_retries', 'type': 'core::ffi::c_ushort'}, {'name': 'nr_hangs', 'type': 'core::ffi::c_ushort'}, {'name': 'max_hang_time', 'type': 'core::ffi::c_uint'}, {'name': 'expires_next', 'type': 'ktime_t'}, {'name': 'next_timer', 'type': '*mut hrtimer'}, {'name': 'softirq_expires_next', 'type': 'ktime_t'}, {'name': 'softirq_next_timer', 'type': '*mut hrtimer'}, {'name': 'clock_base', 'type': '[hrtimer_clock_base; 8usize]'}]`
- New: `[{'name': 'lock', 'type': 'raw_spinlock_t'}, {'name': 'cpu', 'type': 'core::ffi::c_uint'}, {'name': 'active_bases', 'type': 'core::ffi::c_uint'}, {'name': 'clock_was_set_seq', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'nr_events', 'type': 'core::ffi::c_uint'}, {'name': 'nr_retries', 'type': 'core::ffi::c_ushort'}, {'name': 'nr_hangs', 'type': 'core::ffi::c_ushort'}, {'name': 'max_hang_time', 'type': 'core::ffi::c_uint'}, {'name': 'expires_next', 'type': 'ktime_t'}, {'name': 'next_timer', 'type': '*mut hrtimer'}, {'name': 'softirq_expires_next', 'type': 'ktime_t'}, {'name': 'softirq_next_timer', 'type': '*mut hrtimer'}, {'name': 'clock_base', 'type': '[hrtimer_clock_base; 8usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000441 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: idt_bits
- Explanation: idt_bits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000442 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: ldttss_desc
- Explanation: ldttss_desc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'limit0', 'type': 'u16_'}, {'name': 'base0', 'type': 'u16_'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]'}, {'name': 'base3', 'type': 'u32_'}, {'name': 'zero1', 'type': 'u32_'}]`
- New: `[{'name': 'limit0', 'type': 'u16_'}, {'name': 'base0', 'type': 'u16_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': 'base3', 'type': 'u32_'}, {'name': 'zero1', 'type': 'u32_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000443 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: local_apic__bindgen_ty_10
- Explanation: local_apic__bindgen_ty_10 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]'}, {'name': '__reserved_2', 'type': '[core::ffi::c_uint; 3usize]'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u32; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': '__reserved_2', 'type': '[core::ffi::c_uint; 3usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000444 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: local_apic__bindgen_ty_11
- Explanation: local_apic__bindgen_ty_11 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]'}, {'name': '__reserved_2', 'type': '[core::ffi::c_uint; 3usize]'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u32; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': '__reserved_2', 'type': '[core::ffi::c_uint; 3usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000445 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: local_apic__bindgen_ty_14
- Explanation: local_apic__bindgen_ty_14 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]'}, {'name': '__reserved_2', 'type': '[core::ffi::c_uint; 3usize]'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u32; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': '__reserved_2', 'type': '[core::ffi::c_uint; 3usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000446 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: local_apic__bindgen_ty_15
- Explanation: local_apic__bindgen_ty_15 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]'}, {'name': '__reserved_2', 'type': '[core::ffi::c_uint; 3usize]'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u32; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': '__reserved_2', 'type': '[core::ffi::c_uint; 3usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000447 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: local_apic__bindgen_ty_16
- Explanation: local_apic__bindgen_ty_16 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]'}, {'name': '__reserved_3', 'type': '[core::ffi::c_uint; 3usize]'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u32; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': '__reserved_3', 'type': '[core::ffi::c_uint; 3usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000448 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: local_apic__bindgen_ty_20__bindgen_ty_1
- Explanation: local_apic__bindgen_ty_20__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]'}, {'name': '__reserved_3', 'type': '[core::ffi::c_uint; 3usize]'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u32; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': '__reserved_3', 'type': '[core::ffi::c_uint; 3usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000449 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: local_apic__bindgen_ty_28
- Explanation: local_apic__bindgen_ty_28 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]'}, {'name': '__reserved_4', 'type': '[core::ffi::c_uint; 3usize]'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u16; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': '__reserved_4', 'type': '[core::ffi::c_uint; 3usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000451 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: local_apic__bindgen_ty_30
- Explanation: local_apic__bindgen_ty_30 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]'}, {'name': '__reserved_4', 'type': '[core::ffi::c_uint; 3usize]'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u16; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': '__reserved_4', 'type': '[core::ffi::c_uint; 3usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000452 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: local_apic__bindgen_ty_31
- Explanation: local_apic__bindgen_ty_31 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]'}, {'name': '__reserved_4', 'type': '[core::ffi::c_uint; 3usize]'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u16; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': '__reserved_4', 'type': '[core::ffi::c_uint; 3usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000453 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: local_apic__bindgen_ty_32
- Explanation: local_apic__bindgen_ty_32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]'}, {'name': '__reserved_4', 'type': '[core::ffi::c_uint; 3usize]'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u16; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': '__reserved_4', 'type': '[core::ffi::c_uint; 3usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000454 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: local_apic__bindgen_ty_33
- Explanation: local_apic__bindgen_ty_33 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]'}, {'name': '__reserved_3', 'type': '[core::ffi::c_uint; 3usize]'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u16; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': '__reserved_3', 'type': '[core::ffi::c_uint; 3usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000455 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: local_apic__bindgen_ty_34
- Explanation: local_apic__bindgen_ty_34 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]'}, {'name': '__reserved_3', 'type': '[core::ffi::c_uint; 3usize]'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u16; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': '__reserved_3', 'type': '[core::ffi::c_uint; 3usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000456 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: local_apic__bindgen_ty_35
- Explanation: local_apic__bindgen_ty_35 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]'}, {'name': '__reserved_4', 'type': '[core::ffi::c_uint; 3usize]'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u16; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': '__reserved_4', 'type': '[core::ffi::c_uint; 3usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000458 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: local_apic__bindgen_ty_42
- Explanation: local_apic__bindgen_ty_42 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]'}, {'name': '__reserved_2', 'type': '[core::ffi::c_uint; 3usize]'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u32; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': '__reserved_2', 'type': '[core::ffi::c_uint; 3usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000459 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: local_apic__bindgen_ty_9
- Explanation: local_apic__bindgen_ty_9 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]'}, {'name': '__reserved_2', 'type': '[core::ffi::c_uint; 3usize]'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u32; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': '__reserved_2', 'type': '[core::ffi::c_uint; 3usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000461 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: mm_context_t
- Explanation: mm_context_t changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'ctx_id', 'type': 'u64_'}, {'name': 'tlb_gen', 'type': 'atomic64_t'}, {'name': 'ldt_usr_sem', 'type': 'rw_semaphore'}, {'name': 'ldt', 'type': '*mut ldt_struct'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'lock', 'type': 'mutex'}, {'name': 'vdso', 'type': '*mut core::ffi::c_void'}, {'name': 'vdso_image', 'type': '*mut vdso_image'}, {'name': 'perf_rdpmc_allowed', 'type': 'atomic_t'}, {'name': 'pkey_allocation_map', 'type': 'u16_'}, {'name': 'execute_only_pkey', 'type': 's16'}]`
- New: `[{'name': 'ctx_id', 'type': 'u64_'}, {'name': 'tlb_gen', 'type': 'atomic64_t'}, {'name': 'ldt_usr_sem', 'type': 'rw_semaphore'}, {'name': 'ldt', 'type': '*mut ldt_struct'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'lock', 'type': 'mutex'}, {'name': 'vdso', 'type': '*mut core::ffi::c_void'}, {'name': 'vdso_image', 'type': '*const vdso_image'}, {'name': 'perf_rdpmc_allowed', 'type': 'atomic_t'}, {'name': 'pkey_allocation_map', 'type': 'u16_'}, {'name': 'execute_only_pkey', 'type': 's16'}]`

### Rust Evidence

- Graph edges: `1`

## W-000463 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: old_timex32
- Explanation: old_timex32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'modes', 'type': 'u32_'}, {'name': 'offset', 'type': 's32'}, {'name': 'freq', 'type': 's32'}, {'name': 'maxerror', 'type': 's32'}, {'name': 'esterror', 'type': 's32'}, {'name': 'status', 'type': 's32'}, {'name': 'constant', 'type': 's32'}, {'name': 'precision', 'type': 's32'}, {'name': 'tolerance', 'type': 's32'}, {'name': 'time', 'type': 'old_timeval32'}, {'name': 'tick', 'type': 's32'}, {'name': 'ppsfreq', 'type': 's32'}, {'name': 'jitter', 'type': 's32'}, {'name': 'shift', 'type': 's32'}, {'name': 'stabil', 'type': 's32'}, {'name': 'jitcnt', 'type': 's32'}, {'name': 'calcnt', 'type': 's32'}, {'name': 'errcnt', 'type': 's32'}, {'name': 'stbcnt', 'type': 's32'}, {'name': 'tai', 'type': 's32'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 44usize]'}]`
- New: `[{'name': 'modes', 'type': 'u32_'}, {'name': 'offset', 'type': 's32'}, {'name': 'freq', 'type': 's32'}, {'name': 'maxerror', 'type': 's32'}, {'name': 'esterror', 'type': 's32'}, {'name': 'status', 'type': 's32'}, {'name': 'constant', 'type': 's32'}, {'name': 'precision', 'type': 's32'}, {'name': 'tolerance', 'type': 's32'}, {'name': 'time', 'type': 'old_timeval32'}, {'name': 'tick', 'type': 's32'}, {'name': 'ppsfreq', 'type': 's32'}, {'name': 'jitter', 'type': 's32'}, {'name': 'shift', 'type': 's32'}, {'name': 'stabil', 'type': 's32'}, {'name': 'jitcnt', 'type': 's32'}, {'name': 'calcnt', 'type': 's32'}, {'name': 'errcnt', 'type': 's32'}, {'name': 'stbcnt', 'type': 's32'}, {'name': 'tai', 'type': 's32'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 44usize]>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000464 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: orc_entry
- Explanation: orc_entry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'sp_offset', 'type': 's16'}, {'name': 'bp_offset', 'type': 's16'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]'}]`
- New: `[{'name': 'sp_offset', 'type': 's16'}, {'name': 'bp_offset', 'type': 's16'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000465 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: page__bindgen_ty_1__bindgen_ty_4
- Explanation: page__bindgen_ty_1__bindgen_ty_4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_pt_pad_1', 'type': 'core::ffi::c_ulong'}, {'name': 'pmd_huge_pte', 'type': 'pgtable_t'}, {'name': '_pt_pad_2', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'page__bindgen_ty_1__bindgen_ty_4__bindgen_ty_1'}, {'name': 'ptl', 'type': 'spinlock_t'}]`
- New: `[{'name': 'pgmap', 'type': '*mut dev_pagemap'}, {'name': 'zone_device_data', 'type': '*mut core::ffi::c_void'}]`

### Rust Evidence

- Graph edges: `1`

## W-000466 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: percpu_ref_data
- Explanation: percpu_ref_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'count', 'type': 'atomic_long_t'}, {'name': 'release', 'type': 'percpu_ref_func_t'}, {'name': 'confirm_switch', 'type': 'percpu_ref_func_t'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'ref_', 'type': '*mut percpu_ref'}]`
- New: `[{'name': 'count', 'type': 'atomic_long_t'}, {'name': 'release', 'type': 'percpu_ref_func_t'}, {'name': 'confirm_switch', 'type': 'percpu_ref_func_t'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'ref_', 'type': '*mut percpu_ref'}]`

### Rust Evidence

- Graph edges: `1`

## W-000467 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: sched_dl_entity
- Explanation: sched_dl_entity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'rb_node', 'type': 'rb_node'}, {'name': 'dl_runtime', 'type': 'u64_'}, {'name': 'dl_deadline', 'type': 'u64_'}, {'name': 'dl_period', 'type': 'u64_'}, {'name': 'dl_bw', 'type': 'u64_'}, {'name': 'dl_density', 'type': 'u64_'}, {'name': 'runtime', 'type': 's64'}, {'name': 'deadline', 'type': 'u64_'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]'}, {'name': 'dl_timer', 'type': 'hrtimer'}, {'name': 'inactive_timer', 'type': 'hrtimer'}, {'name': 'pi_se', 'type': '*mut sched_dl_entity'}]`
- New: `[{'name': 'rb_node', 'type': 'rb_node'}, {'name': 'dl_runtime', 'type': 'u64_'}, {'name': 'dl_deadline', 'type': 'u64_'}, {'name': 'dl_period', 'type': 'u64_'}, {'name': 'dl_bw', 'type': 'u64_'}, {'name': 'dl_density', 'type': 'u64_'}, {'name': 'runtime', 'type': 's64'}, {'name': 'deadline', 'type': 'u64_'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'dl_timer', 'type': 'hrtimer'}, {'name': 'inactive_timer', 'type': 'hrtimer'}, {'name': 'pi_se', 'type': '*mut sched_dl_entity'}]`

### Rust Evidence

- Graph edges: `1`

## W-000468 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: sched_entity
- Explanation: sched_entity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'load', 'type': 'load_weight'}, {'name': 'run_node', 'type': 'rb_node'}, {'name': 'group_node', 'type': 'list_head'}, {'name': 'on_rq', 'type': 'core::ffi::c_uint'}, {'name': 'exec_start', 'type': 'u64_'}, {'name': 'sum_exec_runtime', 'type': 'u64_'}, {'name': 'vruntime', 'type': 'u64_'}, {'name': 'prev_sum_exec_runtime', 'type': 'u64_'}, {'name': 'nr_migrations', 'type': 'u64_'}, {'name': 'depth', 'type': 'core::ffi::c_int'}, {'name': 'parent', 'type': '*mut sched_entity'}, {'name': 'cfs_rq', 'type': '*mut cfs_rq'}, {'name': 'my_q', 'type': '*mut cfs_rq'}, {'name': 'runnable_weight', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': '[u64; 6usize]'}, {'name': 'avg', 'type': 'sched_avg'}]`
- New: `[{'name': 'load', 'type': 'load_weight'}, {'name': 'run_node', 'type': 'rb_node'}, {'name': 'deadline', 'type': 'u64_'}, {'name': 'min_deadline', 'type': 'u64_'}, {'name': 'group_node', 'type': 'list_head'}, {'name': 'on_rq', 'type': 'core::ffi::c_uint'}, {'name': 'exec_start', 'type': 'u64_'}, {'name': 'sum_exec_runtime', 'type': 'u64_'}, {'name': 'prev_sum_exec_runtime', 'type': 'u64_'}, {'name': 'vruntime', 'type': 'u64_'}, {'name': 'vlag', 'type': 's64'}, {'name': 'slice', 'type': 'u64_'}, {'name': 'nr_migrations', 'type': 'u64_'}, {'name': 'depth', 'type': 'core::ffi::c_int'}, {'name': 'parent', 'type': '*mut sched_entity'}, {'name': 'cfs_rq', 'type': '*mut cfs_rq'}, {'name': 'my_q', 'type': '*mut cfs_rq'}, {'name': 'runnable_weight', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': '[u64; 2usize]'}, {'name': 'avg', 'type': 'sched_avg'}]`

### Rust Evidence

- Graph edges: `1`

## W-000470 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: thread_struct
- Explanation: thread_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'tls_array', 'type': '[desc_struct; 3usize]'}, {'name': 'sp', 'type': 'core::ffi::c_ulong'}, {'name': 'es', 'type': 'core::ffi::c_ushort'}, {'name': 'ds', 'type': 'core::ffi::c_ushort'}, {'name': 'fsindex', 'type': 'core::ffi::c_ushort'}, {'name': 'gsindex', 'type': 'core::ffi::c_ushort'}, {'name': 'fsbase', 'type': 'core::ffi::c_ulong'}, {'name': 'gsbase', 'type': 'core::ffi::c_ulong'}, {'name': 'ptrace_bps', 'type': '[*mut perf_event; 4usize]'}, {'name': 'virtual_dr6', 'type': 'core::ffi::c_ulong'}, {'name': 'ptrace_dr7', 'type': 'core::ffi::c_ulong'}, {'name': 'cr2', 'type': 'core::ffi::c_ulong'}, {'name': 'trap_nr', 'type': 'core::ffi::c_ulong'}, {'name': 'error_code', 'type': 'core::ffi::c_ulong'}, {'name': 'io_bitmap', 'type': '*mut io_bitmap'}, {'name': 'iopl_emul', 'type': 'core::ffi::c_ulong'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]'}, {'name': 'pkru', 'type': 'u32_'}, {'name': '__bindgen_padding_0', 'type': '[u64; 5usize]'}, {'name': 'fpu', 'type': 'fpu'}]`
- New: `[{'name': 'tls_array', 'type': '[desc_struct; 3usize]'}, {'name': 'sp', 'type': 'core::ffi::c_ulong'}, {'name': 'es', 'type': 'core::ffi::c_ushort'}, {'name': 'ds', 'type': 'core::ffi::c_ushort'}, {'name': 'fsindex', 'type': 'core::ffi::c_ushort'}, {'name': 'gsindex', 'type': 'core::ffi::c_ushort'}, {'name': 'fsbase', 'type': 'core::ffi::c_ulong'}, {'name': 'gsbase', 'type': 'core::ffi::c_ulong'}, {'name': 'ptrace_bps', 'type': '[*mut perf_event; 4usize]'}, {'name': 'virtual_dr6', 'type': 'core::ffi::c_ulong'}, {'name': 'ptrace_dr7', 'type': 'core::ffi::c_ulong'}, {'name': 'cr2', 'type': 'core::ffi::c_ulong'}, {'name': 'trap_nr', 'type': 'core::ffi::c_ulong'}, {'name': 'error_code', 'type': 'core::ffi::c_ulong'}, {'name': 'io_bitmap', 'type': '*mut io_bitmap'}, {'name': 'iopl_emul', 'type': 'core::ffi::c_ulong'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'pkru', 'type': 'u32_'}, {'name': '__bindgen_padding_0', 'type': '[u64; 5usize]'}, {'name': 'fpu', 'type': 'fpu'}]`

### Rust Evidence

- Graph edges: `1`

## W-000472 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: user_desc
- Explanation: user_desc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'entry_number', 'type': 'core::ffi::c_uint'}, {'name': 'base_addr', 'type': 'core::ffi::c_uint'}, {'name': 'limit', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]'}, {'name': '__bindgen_padding_0', 'type': '[u8; 3usize]'}]`
- New: `[{'name': 'entry_number', 'type': 'core::ffi::c_uint'}, {'name': 'base_addr', 'type': 'core::ffi::c_uint'}, {'name': 'limit', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 3usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000473 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vdso_image
- Explanation: vdso_image changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[{'name': 'data', 'type': '*mut core::ffi::c_void'}, {'name': 'size', 'type': 'core::ffi::c_ulong'}, {'name': 'alt', 'type': 'core::ffi::c_ulong'}, {'name': 'alt_len', 'type': 'core::ffi::c_ulong'}, {'name': 'extable_base', 'type': 'core::ffi::c_ulong'}, {'name': 'extable_len', 'type': 'core::ffi::c_ulong'}, {'name': 'extable', 'type': '*const core::ffi::c_void'}, {'name': 'sym_vvar_start', 'type': 'core::ffi::c_long'}, {'name': 'sym_vvar_page', 'type': 'core::ffi::c_long'}, {'name': 'sym_pvclock_page', 'type': 'core::ffi::c_long'}, {'name': 'sym_hvclock_page', 'type': 'core::ffi::c_long'}, {'name': 'sym_timens_page', 'type': 'core::ffi::c_long'}, {'name': 'sym_VDSO32_NOTE_MASK', 'type': 'core::ffi::c_long'}, {'name': 'sym___kernel_sigreturn', 'type': 'core::ffi::c_long'}, {'name': 'sym___kernel_rt_sigreturn', 'type': 'core::ffi::c_long'}, {'name': 'sym___kernel_vsyscall', 'type': 'core::ffi::c_long'}, {'name': 'sym_int80_landing_pad', 'type': 'core::ffi::c_long'}, {'name': 'sym_vdso32_sigreturn_landing_pad', 'type': 'core::ffi::c_long'}, {'name': 'sym_vdso32_rt_sigreturn_landing_pad', 'type': 'core::ffi::c_long'}]`

### Rust Evidence

- Graph edges: `1`

## W-000475 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vm_operations_struct
- Explanation: vm_operations_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[]`

### Rust Evidence

- Graph edges: `1`

## W-000476 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vm_region
- Explanation: vm_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'vm_rb', 'type': 'rb_node'}, {'name': 'vm_flags', 'type': 'vm_flags_t'}, {'name': 'vm_start', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_end', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_top', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_pgoff', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_file', 'type': '*mut file'}, {'name': 'vm_usage', 'type': 'core::ffi::c_int'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]'}, {'name': '__bindgen_padding_0', 'type': '[u8; 3usize]'}]`
- New: `[{'name': 'vm_rb', 'type': 'rb_node'}, {'name': 'vm_flags', 'type': 'vm_flags_t'}, {'name': 'vm_start', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_end', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_top', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_pgoff', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_file', 'type': '*mut file'}, {'name': 'vm_usage', 'type': 'core::ffi::c_int'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 3usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000477 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: workqueue_attrs
- Explanation: workqueue_attrs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'nice', 'type': 'core::ffi::c_int'}, {'name': 'cpumask', 'type': 'cpumask_var_t'}, {'name': 'no_numa', 'type': 'bool_'}]`
- New: `[{'name': 'nice', 'type': 'core::ffi::c_int'}, {'name': 'cpumask', 'type': 'cpumask_var_t'}, {'name': '__pod_cpumask', 'type': 'cpumask_var_t'}, {'name': 'affn_strict', 'type': 'bool_'}, {'name': 'affn_scope', 'type': 'wq_affn_scope'}, {'name': 'ordered', 'type': 'bool_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000504 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: pageflags_PG_private
- Explanation: pageflags_PG_private changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `13`
- New: `15`

### Rust Evidence

- Graph edges: `2`

## W-000478 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: CONFIG_AS_VERSION
- Explanation: CONFIG_AS_VERSION changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `150007`
- New: `180103`

### Rust Evidence

- Graph edges: `1`

## W-000479 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: CONFIG_BINDGEN_VERSION_TEXT
- Explanation: CONFIG_BINDGEN_VERSION_TEXT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `b"bindgen 0.56.0\0"`
- New: `b"bindgen 0.65.1\0"`

### Rust Evidence

- Graph edges: `1`

## W-000480 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: CONFIG_CC_VERSION_TEXT
- Explanation: CONFIG_CC_VERSION_TEXT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `b"Ubuntu clang version 15.0.7\0"`
- New: `b"Ubuntu clang version 18.1.3 (1ubuntu1)\0"`

### Rust Evidence

- Graph edges: `1`

## W-000481 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: CONFIG_CLANG_VERSION
- Explanation: CONFIG_CLANG_VERSION changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `150007`
- New: `180103`

### Rust Evidence

- Graph edges: `1`

## W-000482 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: CONFIG_LLD_VERSION
- Explanation: CONFIG_LLD_VERSION changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `150007`
- New: `180103`

### Rust Evidence

- Graph edges: `1`

## W-000483 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: CONFIG_RUSTC_VERSION_TEXT
- Explanation: CONFIG_RUSTC_VERSION_TEXT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `b"rustc 1.68.2 (9eb3afe9e 2023-03-27)\0"`
- New: `b"rustc 1.71.1 (eb26296b5 2023-08-03)\0"`

### Rust Evidence

- Graph edges: `1`

## W-000484 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: IA32_NR_syscalls
- Explanation: IA32_NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `452`
- New: `453`

### Rust Evidence

- Graph edges: `1`

## W-000485 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: NR_syscalls
- Explanation: NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `452`
- New: `454`

### Rust Evidence

- Graph edges: `1`

## W-000486 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: NSIGSEGV
- Explanation: NSIGSEGV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `9`
- New: `10`

### Rust Evidence

- Graph edges: `1`

## W-000487 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: SECCOMP_ARCH_COMPAT_NR
- Explanation: SECCOMP_ARCH_COMPAT_NR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `452`
- New: `453`

### Rust Evidence

- Graph edges: `1`

## W-000488 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: SECCOMP_ARCH_NATIVE_NR
- Explanation: SECCOMP_ARCH_NATIVE_NR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `452`
- New: `454`

### Rust Evidence

- Graph edges: `1`

## W-000489 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: _PAGE_BIT_DEVMAP
- Explanation: _PAGE_BIT_DEVMAP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `58`
- New: `57`

### Rust Evidence

- Graph edges: `1`

## W-000490 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: _PAGE_BIT_SOFTW4
- Explanation: _PAGE_BIT_SOFTW4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `58`
- New: `57`

### Rust Evidence

- Graph edges: `1`

## W-000491 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __NR_ia32_syscalls
- Explanation: __NR_ia32_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `452`
- New: `453`

### Rust Evidence

- Graph edges: `1`

## W-000492 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __NR_syscalls
- Explanation: __NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `452`
- New: `454`

### Rust Evidence

- Graph edges: `1`

## W-000493 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_active
- Explanation: pageflags_PG_active changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `8`

### Rust Evidence

- Graph edges: `1`

## W-000494 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_arch_1
- Explanation: pageflags_PG_arch_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `11`
- New: `13`

### Rust Evidence

- Graph edges: `1`

## W-000495 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_checked
- Explanation: pageflags_PG_checked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `12`

### Rust Evidence

- Graph edges: `1`

## W-000496 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_dirty
- Explanation: pageflags_PG_dirty changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `3`
- New: `4`

### Rust Evidence

- Graph edges: `1`

## W-000497 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_error
- Explanation: pageflags_PG_error changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `10`

### Rust Evidence

- Graph edges: `1`

## W-000498 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_foreign
- Explanation: pageflags_PG_foreign changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `12`

### Rust Evidence

- Graph edges: `1`

## W-000499 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_fscache
- Explanation: pageflags_PG_fscache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `14`
- New: `16`

### Rust Evidence

- Graph edges: `1`

## W-000500 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_head
- Explanation: pageflags_PG_head changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `6`

### Rust Evidence

- Graph edges: `1`

## W-000501 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_lru
- Explanation: pageflags_PG_lru changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `4`
- New: `5`

### Rust Evidence

- Graph edges: `1`

## W-000502 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_owner_priv_1
- Explanation: pageflags_PG_owner_priv_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `12`

### Rust Evidence

- Graph edges: `1`

## W-000503 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_pinned
- Explanation: pageflags_PG_pinned changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `12`

### Rust Evidence

- Graph edges: `1`

## W-000505 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_private_2
- Explanation: pageflags_PG_private_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `14`
- New: `16`

### Rust Evidence

- Graph edges: `1`

## W-000506 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_referenced
- Explanation: pageflags_PG_referenced changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `1`
- New: `2`

### Rust Evidence

- Graph edges: `1`

## W-000507 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_reported
- Explanation: pageflags_PG_reported changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `2`
- New: `3`

### Rust Evidence

- Graph edges: `1`

## W-000508 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_reserved
- Explanation: pageflags_PG_reserved changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `12`
- New: `14`

### Rust Evidence

- Graph edges: `1`

## W-000509 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_savepinned
- Explanation: pageflags_PG_savepinned changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `3`
- New: `4`

### Rust Evidence

- Graph edges: `1`

## W-000510 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_slab
- Explanation: pageflags_PG_slab changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `9`
- New: `11`

### Rust Evidence

- Graph edges: `1`

## W-000511 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_swapcache
- Explanation: pageflags_PG_swapcache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `12`

### Rust Evidence

- Graph edges: `1`

## W-000512 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_uptodate
- Explanation: pageflags_PG_uptodate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `2`
- New: `3`

### Rust Evidence

- Graph edges: `1`

## W-000513 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_workingset
- Explanation: pageflags_PG_workingset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `6`
- New: `9`

### Rust Evidence

- Graph edges: `1`

## W-000514 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_writeback
- Explanation: pageflags_PG_writeback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `15`
- New: `1`

### Rust Evidence

- Graph edges: `1`

## W-000515 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_xen_remapped
- Explanation: pageflags_PG_xen_remapped changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `12`

### Rust Evidence

- Graph edges: `1`
