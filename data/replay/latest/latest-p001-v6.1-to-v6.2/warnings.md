# BindDrift Ranked Warnings

## W-000005 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: __wake_up
- Explanation: __wake_up changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'wq_head', 'type': '*mut wait_queue_head'}, {'name': 'mode', 'type': 'core::ffi::c_uint'}, {'name': 'nr', 'type': 'core::ffi::c_int'}, {'name': 'key', 'type': '*mut core::ffi::c_void'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'wq_head', 'type': '*mut wait_queue_head'}, {'name': 'mode', 'type': 'core::ffi::c_uint'}, {'name': 'nr', 'type': 'core::ffi::c_int'}, {'name': 'key', 'type': '*mut core::ffi::c_void'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `8`

## W-000021 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: kmem_cache_alloc
- Explanation: kmem_cache_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 's', 'type': '*mut kmem_cache'}, {'name': 'flags', 'type': 'gfp_t'}], 'return_type': '*mut core::ffi::c_void'}`
- New: `{'params': [{'name': 'cachep', 'type': '*mut kmem_cache'}, {'name': 'flags', 'type': 'gfp_t'}], 'return_type': '*mut core::ffi::c_void'}`

### Rust Evidence

- Graph edges: `4`

## W-000007 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: _atomic_dec_and_raw_lock
- Explanation: _atomic_dec_and_raw_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000030 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: static_key_slow_inc
- Explanation: static_key_slow_inc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'key', 'type': '*mut static_key'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'key', 'type': '*mut static_key'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `2`

## W-000034 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: timer_delete
- Explanation: timer_delete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000036 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: timer_shutdown
- Explanation: timer_shutdown changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000040 FieldDrift

- Risk: High
- Score: 11.0
- Symbol: folio
- Explanation: folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'folio__bindgen_ty_1'}, {'name': '_flags_1', 'type': 'core::ffi::c_ulong'}, {'name': '__head', 'type': 'core::ffi::c_ulong'}, {'name': '_folio_dtor', 'type': 'core::ffi::c_uchar'}, {'name': '_folio_order', 'type': 'core::ffi::c_uchar'}, {'name': '_total_mapcount', 'type': 'atomic_t'}, {'name': '_pincount', 'type': 'atomic_t'}, {'name': '_folio_nr_pages', 'type': 'core::ffi::c_uint'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'folio__bindgen_ty_1'}, {'name': '__bindgen_anon_2', 'type': 'folio__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'folio__bindgen_ty_3'}]`

### Rust Evidence

- Graph edges: `12`

## W-000001 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __get_random_u32_below
- Explanation: __get_random_u32_below changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000002 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __percpu_counter_compare
- Explanation: __percpu_counter_compare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000003 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __percpu_counter_init
- Explanation: __percpu_counter_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000004 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __percpu_counter_sum
- Explanation: __percpu_counter_sum changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000006 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __x86_return_skl
- Explanation: __x86_return_skl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000008 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: _atomic_dec_and_raw_lock_irqsave
- Explanation: _atomic_dec_and_raw_lock_irqsave changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000009 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: add_hwgenerator_randomness
- Explanation: add_hwgenerator_randomness changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'buf', 'type': '*const core::ffi::c_void'}, {'name': 'len', 'type': 'usize'}, {'name': 'entropy', 'type': 'usize'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'buf', 'type': '*const core::ffi::c_void'}, {'name': 'len', 'type': 'usize'}, {'name': 'entropy', 'type': 'usize'}, {'name': 'sleep_after', 'type': 'bool_'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000010 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: apply_fineibt
- Explanation: apply_fineibt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000011 SignatureDrift

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

## W-000012 SignatureDrift

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

## W-000013 SignatureDrift

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

## W-000014 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: check_panic_on_warn
- Explanation: check_panic_on_warn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000017 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: execute_with_initialized_rng
- Explanation: execute_with_initialized_rng changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000018 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ibt_restore
- Explanation: ibt_restore changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000019 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ibt_save
- Explanation: ibt_save changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000020 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_callthunk
- Explanation: is_callthunk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000023 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: percpu_counter_add_batch
- Explanation: percpu_counter_add_batch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000024 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: percpu_counter_destroy
- Explanation: percpu_counter_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000025 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: percpu_counter_set
- Explanation: percpu_counter_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000026 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: percpu_counter_sum_all
- Explanation: percpu_counter_sum_all changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000027 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: percpu_counter_sync
- Explanation: percpu_counter_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000029 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: static_key_fast_inc_not_disabled
- Explanation: static_key_fast_inc_not_disabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000031 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: static_key_slow_inc_cpuslocked
- Explanation: static_key_slow_inc_cpuslocked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'key', 'type': '*mut static_key'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'key', 'type': '*mut static_key'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000032 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: switch_gdt_and_percpu_base
- Explanation: switch_gdt_and_percpu_base changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000035 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: timer_delete_sync
- Explanation: timer_delete_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000037 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: timer_shutdown_sync
- Explanation: timer_shutdown_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000038 SignatureDrift

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

## W-000015 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: del_timer
- Explanation: del_timer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000016 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: del_timer_sync
- Explanation: del_timer_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000022 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: load_percpu_segment
- Explanation: load_percpu_segment changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000028 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: rcu_is_idle_cpu
- Explanation: rcu_is_idle_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000033 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: switch_to_new_gdt
- Explanation: switch_to_new_gdt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000039 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: x86_init_rdrand
- Explanation: x86_init_rdrand changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000042 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: page__bindgen_ty_1__bindgen_ty_1
- Explanation: page__bindgen_ty_1__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'page__bindgen_ty_1__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mapping', 'type': '*mut address_space'}, {'name': 'index', 'type': 'core::ffi::c_ulong'}, {'name': 'private', 'type': 'core::ffi::c_ulong'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'page__bindgen_ty_1__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mapping', 'type': '*mut address_space'}, {'name': '__bindgen_anon_2', 'type': 'page__bindgen_ty_1__bindgen_ty_1__bindgen_ty_2'}, {'name': 'private', 'type': 'core::ffi::c_ulong'}]`

### Rust Evidence

- Graph edges: `2`

## W-000047 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: vm_area_struct
- Explanation: vm_area_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'vm_start', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_end', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_mm', 'type': '*mut mm_struct'}, {'name': 'vm_page_prot', 'type': 'pgprot_t'}, {'name': 'vm_flags', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'vm_area_struct__bindgen_ty_1'}, {'name': 'anon_vma_chain', 'type': 'list_head'}, {'name': 'anon_vma', 'type': '*mut anon_vma'}, {'name': 'vm_ops', 'type': '*mut vm_operations_struct'}, {'name': 'vm_pgoff', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_file', 'type': '*mut file'}, {'name': 'vm_private_data', 'type': '*mut core::ffi::c_void'}, {'name': 'swap_readahead_info', 'type': 'atomic_long_t'}, {'name': 'vm_policy', 'type': '*mut mempolicy'}, {'name': 'vm_userfaultfd_ctx', 'type': 'vm_userfaultfd_ctx'}]`
- New: `[{'name': 'vm_start', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_end', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_mm', 'type': '*mut mm_struct'}, {'name': 'vm_page_prot', 'type': 'pgprot_t'}, {'name': 'vm_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'shared', 'type': 'vm_area_struct__bindgen_ty_1'}, {'name': 'anon_vma_chain', 'type': 'list_head'}, {'name': 'anon_vma', 'type': '*mut anon_vma'}, {'name': 'vm_ops', 'type': '*mut vm_operations_struct'}, {'name': 'vm_pgoff', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_file', 'type': '*mut file'}, {'name': 'vm_private_data', 'type': '*mut core::ffi::c_void'}, {'name': 'swap_readahead_info', 'type': 'atomic_long_t'}, {'name': 'vm_policy', 'type': '*mut mempolicy'}, {'name': 'vm_userfaultfd_ctx', 'type': 'vm_userfaultfd_ctx'}]`

### Rust Evidence

- Graph edges: `2`

## W-000041 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: mm_struct__bindgen_ty_1
- Explanation: mm_struct__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mm_mt', 'type': 'maple_tree'}, {'name': 'get_unmapped_area', 'type': '::core::option::Option<'}, {'name': 'mmap_base', 'type': 'core::ffi::c_ulong'}, {'name': 'mmap_legacy_base', 'type': 'core::ffi::c_ulong'}, {'name': 'mmap_compat_base', 'type': 'core::ffi::c_ulong'}, {'name': 'mmap_compat_legacy_base', 'type': 'core::ffi::c_ulong'}, {'name': 'task_size', 'type': 'core::ffi::c_ulong'}, {'name': 'pgd', 'type': '*mut pgd_t'}, {'name': 'membarrier_state', 'type': 'atomic_t'}, {'name': 'mm_users', 'type': 'atomic_t'}, {'name': 'mm_count', 'type': 'atomic_t'}, {'name': 'pgtables_bytes', 'type': 'atomic_long_t'}, {'name': 'map_count', 'type': 'core::ffi::c_int'}, {'name': 'page_table_lock', 'type': 'spinlock_t'}, {'name': 'mmap_lock', 'type': 'rw_semaphore'}, {'name': 'mmlist', 'type': 'list_head'}, {'name': 'hiwater_rss', 'type': 'core::ffi::c_ulong'}, {'name': 'hiwater_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'total_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'locked_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'pinned_vm', 'type': 'atomic64_t'}, {'name': 'data_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'exec_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'stack_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'def_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'write_protect_seq', 'type': 'seqcount_t'}, {'name': 'arg_lock', 'type': 'spinlock_t'}, {'name': 'start_code', 'type': 'core::ffi::c_ulong'}, {'name': 'end_code', 'type': 'core::ffi::c_ulong'}, {'name': 'start_data', 'type': 'core::ffi::c_ulong'}, {'name': 'end_data', 'type': 'core::ffi::c_ulong'}, {'name': 'start_brk', 'type': 'core::ffi::c_ulong'}, {'name': 'brk', 'type': 'core::ffi::c_ulong'}, {'name': 'start_stack', 'type': 'core::ffi::c_ulong'}, {'name': 'arg_start', 'type': 'core::ffi::c_ulong'}, {'name': 'arg_end', 'type': 'core::ffi::c_ulong'}, {'name': 'env_start', 'type': 'core::ffi::c_ulong'}, {'name': 'env_end', 'type': 'core::ffi::c_ulong'}, {'name': 'saved_auxv', 'type': '[core::ffi::c_ulong; 48usize]'}, {'name': 'rss_stat', 'type': 'mm_rss_stat'}, {'name': 'binfmt', 'type': '*mut linux_binfmt'}, {'name': 'context', 'type': 'mm_context_t'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'ioctx_lock', 'type': 'spinlock_t'}, {'name': 'ioctx_table', 'type': '*mut kioctx_table'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'exe_file', 'type': '*mut file'}, {'name': 'notifier_subscriptions', 'type': '*mut mmu_notifier_subscriptions'}, {'name': 'tlb_flush_pending', 'type': 'atomic_t'}, {'name': 'tlb_flush_batched', 'type': 'atomic_t'}, {'name': 'uprobes_state', 'type': 'uprobes_state'}, {'name': 'hugetlb_usage', 'type': 'atomic_long_t'}, {'name': 'async_put_work', 'type': 'work_struct'}]`
- New: `[{'name': 'mm_mt', 'type': 'maple_tree'}, {'name': 'get_unmapped_area', 'type': '::core::option::Option<'}, {'name': 'mmap_base', 'type': 'core::ffi::c_ulong'}, {'name': 'mmap_legacy_base', 'type': 'core::ffi::c_ulong'}, {'name': 'mmap_compat_base', 'type': 'core::ffi::c_ulong'}, {'name': 'mmap_compat_legacy_base', 'type': 'core::ffi::c_ulong'}, {'name': 'task_size', 'type': 'core::ffi::c_ulong'}, {'name': 'pgd', 'type': '*mut pgd_t'}, {'name': 'membarrier_state', 'type': 'atomic_t'}, {'name': 'mm_users', 'type': 'atomic_t'}, {'name': 'mm_count', 'type': 'atomic_t'}, {'name': 'pgtables_bytes', 'type': 'atomic_long_t'}, {'name': 'map_count', 'type': 'core::ffi::c_int'}, {'name': 'page_table_lock', 'type': 'spinlock_t'}, {'name': 'mmap_lock', 'type': 'rw_semaphore'}, {'name': 'mmlist', 'type': 'list_head'}, {'name': 'hiwater_rss', 'type': 'core::ffi::c_ulong'}, {'name': 'hiwater_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'total_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'locked_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'pinned_vm', 'type': 'atomic64_t'}, {'name': 'data_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'exec_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'stack_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'def_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'write_protect_seq', 'type': 'seqcount_t'}, {'name': 'arg_lock', 'type': 'spinlock_t'}, {'name': 'start_code', 'type': 'core::ffi::c_ulong'}, {'name': 'end_code', 'type': 'core::ffi::c_ulong'}, {'name': 'start_data', 'type': 'core::ffi::c_ulong'}, {'name': 'end_data', 'type': 'core::ffi::c_ulong'}, {'name': 'start_brk', 'type': 'core::ffi::c_ulong'}, {'name': 'brk', 'type': 'core::ffi::c_ulong'}, {'name': 'start_stack', 'type': 'core::ffi::c_ulong'}, {'name': 'arg_start', 'type': 'core::ffi::c_ulong'}, {'name': 'arg_end', 'type': 'core::ffi::c_ulong'}, {'name': 'env_start', 'type': 'core::ffi::c_ulong'}, {'name': 'env_end', 'type': 'core::ffi::c_ulong'}, {'name': 'saved_auxv', 'type': '[core::ffi::c_ulong; 48usize]'}, {'name': 'rss_stat', 'type': '[percpu_counter; 4usize]'}, {'name': 'binfmt', 'type': '*mut linux_binfmt'}, {'name': 'context', 'type': 'mm_context_t'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'ioctx_lock', 'type': 'spinlock_t'}, {'name': 'ioctx_table', 'type': '*mut kioctx_table'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'exe_file', 'type': '*mut file'}, {'name': 'notifier_subscriptions', 'type': '*mut mmu_notifier_subscriptions'}, {'name': 'tlb_flush_pending', 'type': 'atomic_t'}, {'name': 'tlb_flush_batched', 'type': 'atomic_t'}, {'name': 'uprobes_state', 'type': 'uprobes_state'}, {'name': 'hugetlb_usage', 'type': 'atomic_long_t'}, {'name': 'async_put_work', 'type': 'work_struct'}]`

### Rust Evidence

- Graph edges: `1`

## W-000043 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: page__bindgen_ty_1__bindgen_ty_3
- Explanation: page__bindgen_ty_1__bindgen_ty_3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'compound_head', 'type': 'core::ffi::c_ulong'}, {'name': 'compound_dtor', 'type': 'core::ffi::c_uchar'}, {'name': 'compound_order', 'type': 'core::ffi::c_uchar'}, {'name': 'compound_mapcount', 'type': 'atomic_t'}, {'name': 'compound_pincount', 'type': 'atomic_t'}, {'name': 'compound_nr', 'type': 'core::ffi::c_uint'}]`
- New: `[{'name': 'compound_head', 'type': 'core::ffi::c_ulong'}, {'name': 'compound_dtor', 'type': 'core::ffi::c_uchar'}, {'name': 'compound_order', 'type': 'core::ffi::c_uchar'}, {'name': 'compound_mapcount', 'type': 'atomic_t'}, {'name': 'subpages_mapcount', 'type': 'atomic_t'}, {'name': 'compound_pincount', 'type': 'atomic_t'}, {'name': 'compound_nr', 'type': 'core::ffi::c_uint'}]`

### Rust Evidence

- Graph edges: `1`

## W-000044 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: page__bindgen_ty_1__bindgen_ty_5
- Explanation: page__bindgen_ty_1__bindgen_ty_5 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_pt_pad_1', 'type': 'core::ffi::c_ulong'}, {'name': 'pmd_huge_pte', 'type': 'pgtable_t'}, {'name': '_pt_pad_2', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'page__bindgen_ty_1__bindgen_ty_5__bindgen_ty_1'}, {'name': 'ptl', 'type': 'spinlock_t'}]`
- New: `[{'name': '_hugetlb_pad_1', 'type': 'core::ffi::c_ulong'}, {'name': 'hugetlb_subpool', 'type': '*mut core::ffi::c_void'}, {'name': 'hugetlb_cgroup', 'type': '*mut core::ffi::c_void'}, {'name': 'hugetlb_cgroup_rsvd', 'type': '*mut core::ffi::c_void'}, {'name': 'hugetlb_hwpoison', 'type': '*mut core::ffi::c_void'}]`

### Rust Evidence

- Graph edges: `1`

## W-000045 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: page__bindgen_ty_1__bindgen_ty_6
- Explanation: page__bindgen_ty_1__bindgen_ty_6 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'pgmap', 'type': '*mut dev_pagemap'}, {'name': 'zone_device_data', 'type': '*mut core::ffi::c_void'}]`
- New: `[{'name': '_pt_pad_1', 'type': 'core::ffi::c_ulong'}, {'name': 'pmd_huge_pte', 'type': 'pgtable_t'}, {'name': '_pt_pad_2', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'page__bindgen_ty_1__bindgen_ty_6__bindgen_ty_1'}, {'name': 'ptl', 'type': 'spinlock_t'}]`

### Rust Evidence

- Graph edges: `1`

## W-000046 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: srcu_data
- Explanation: srcu_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'srcu_lock_count', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'srcu_unlock_count', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': '__bindgen_padding_0', 'type': '[u32; 8usize]'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'srcu_cblist', 'type': 'rcu_segcblist'}, {'name': 'srcu_gp_seq_needed', 'type': 'core::ffi::c_ulong'}, {'name': 'srcu_gp_seq_needed_exp', 'type': 'core::ffi::c_ulong'}, {'name': 'srcu_cblist_invoking', 'type': 'bool_'}, {'name': 'delay_work', 'type': 'timer_list'}, {'name': 'work', 'type': 'work_struct'}, {'name': 'srcu_barrier_head', 'type': 'callback_head'}, {'name': 'mynode', 'type': '*mut srcu_node'}, {'name': 'grpmask', 'type': 'core::ffi::c_ulong'}, {'name': 'cpu', 'type': 'core::ffi::c_int'}, {'name': 'ssp', 'type': '*mut srcu_struct'}]`
- New: `[{'name': 'srcu_lock_count', 'type': '[atomic_long_t; 2usize]'}, {'name': 'srcu_unlock_count', 'type': '[atomic_long_t; 2usize]'}, {'name': 'srcu_nmi_safety', 'type': 'core::ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': '[u32; 7usize]'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'srcu_cblist', 'type': 'rcu_segcblist'}, {'name': 'srcu_gp_seq_needed', 'type': 'core::ffi::c_ulong'}, {'name': 'srcu_gp_seq_needed_exp', 'type': 'core::ffi::c_ulong'}, {'name': 'srcu_cblist_invoking', 'type': 'bool_'}, {'name': 'delay_work', 'type': 'timer_list'}, {'name': 'work', 'type': 'work_struct'}, {'name': 'srcu_barrier_head', 'type': 'callback_head'}, {'name': 'mynode', 'type': '*mut srcu_node'}, {'name': 'grpmask', 'type': 'core::ffi::c_ulong'}, {'name': 'cpu', 'type': 'core::ffi::c_int'}, {'name': 'ssp', 'type': '*mut srcu_struct'}]`

### Rust Evidence

- Graph edges: `1`

## W-000048 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: x86_platform_ops
- Explanation: x86_platform_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'calibrate_cpu', 'type': '::core::option::Option<unsafe extern "C" fn() -> core::ffi::c_ulong>'}, {'name': 'calibrate_tsc', 'type': '::core::option::Option<unsafe extern "C" fn() -> core::ffi::c_ulong>'}, {'name': 'get_wallclock', 'type': '::core::option::Option<unsafe extern "C" fn(ts: *mut timespec64)>'}, {'name': 'iommu_shutdown', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'nmi_init', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'get_nmi_reason', 'type': '::core::option::Option<unsafe extern "C" fn() -> core::ffi::c_uchar>'}, {'name': 'save_sched_clock_state', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'restore_sched_clock_state', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'apic_post_init', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'legacy', 'type': 'x86_legacy_features'}, {'name': 'set_legacy_features', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'hyper', 'type': 'x86_hyper_runtime'}, {'name': 'guest', 'type': 'x86_guest'}]`
- New: `[{'name': 'calibrate_cpu', 'type': '::core::option::Option<unsafe extern "C" fn() -> core::ffi::c_ulong>'}, {'name': 'calibrate_tsc', 'type': '::core::option::Option<unsafe extern "C" fn() -> core::ffi::c_ulong>'}, {'name': 'get_wallclock', 'type': '::core::option::Option<unsafe extern "C" fn(ts: *mut timespec64)>'}, {'name': 'iommu_shutdown', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'nmi_init', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'get_nmi_reason', 'type': '::core::option::Option<unsafe extern "C" fn() -> core::ffi::c_uchar>'}, {'name': 'save_sched_clock_state', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'restore_sched_clock_state', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'apic_post_init', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'legacy', 'type': 'x86_legacy_features'}, {'name': 'set_legacy_features', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'realmode_reserve', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'realmode_init', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'hyper', 'type': 'x86_hyper_runtime'}, {'name': 'guest', 'type': 'x86_guest'}]`

### Rust Evidence

- Graph edges: `1`

## W-000049 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: EARLY_IDT_HANDLER_SIZE
- Explanation: EARLY_IDT_HANDLER_SIZE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `9`
- New: `13`

### Rust Evidence

- Graph edges: `1`

## W-000050 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ENDBR_INSN_SIZE
- Explanation: ENDBR_INSN_SIZE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0`
- New: `4`

### Rust Evidence

- Graph edges: `1`

## W-000051 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: HAS_KERNEL_IBT
- Explanation: HAS_KERNEL_IBT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0`
- New: `1`

### Rust Evidence

- Graph edges: `1`

## W-000052 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: NR_PAGEFLAGS
- Explanation: NR_PAGEFLAGS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `24`
- New: `23`

### Rust Evidence

- Graph edges: `1`

## W-000053 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: PAGEFLAGS_MASK
- Explanation: PAGEFLAGS_MASK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16777215`
- New: `8388607`

### Rust Evidence

- Graph edges: `1`

## W-000054 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: PERCPU_DYNAMIC_EARLY_SIZE
- Explanation: PERCPU_DYNAMIC_EARLY_SIZE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `12288`
- New: `20480`

### Rust Evidence

- Graph edges: `1`

## W-000055 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: XEN_EARLY_IDT_HANDLER_SIZE
- Explanation: XEN_EARLY_IDT_HANDLER_SIZE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `12`

### Rust Evidence

- Graph edges: `1`

## W-000056 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags___NR_PAGEFLAGS
- Explanation: pageflags___NR_PAGEFLAGS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `24`
- New: `23`

### Rust Evidence

- Graph edges: `1`

## W-000057 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SLAB_RECLAIM_ACCOUNT
- Explanation: SLAB_RECLAIM_ACCOUNT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `((slab_flags_t __force)0x00020000U)`
- New: `((slab_flags_t __force)0)`

### Rust Evidence

- Graph edges: `0`
