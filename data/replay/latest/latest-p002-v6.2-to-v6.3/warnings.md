# BindDrift Ranked Warnings

## W-000007 SignatureDrift

- Risk: High
- Score: 14.6
- Symbol: cpuid
- Explanation: cpuid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `27`

## W-000050 OwnershipRefcountDrift

- Risk: High
- Score: 13.0
- Symbol: refcount_dec_and_test
- Explanation: refcount_dec_and_test has REFCOUNT_PUT C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['REFCOUNT_PUT']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.3/include/linux/refcount.h:333 `return __refcount_dec_and_test(r, NULL);`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:255 `drop` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:254 `// SAFETY: Also by the type invariant, we are allowed to decrement the refcount.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:259 `// SAFETY: The pointer was initialised from the result of `Box::leak`.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:255 `LIFETIME_NAMING_PATTERN`

## W-000051 OwnershipRefcountDrift

- Risk: High
- Score: 13.0
- Symbol: refcount_inc
- Explanation: refcount_inc has REFCOUNT_GET C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['REFCOUNT_GET']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.3/include/linux/refcount.h:267 `__refcount_inc(r, NULL);`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:237 `clone` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:235 `// SAFETY: By the type invariant, there is necessarily a reference to the object, so it is`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:239 `// SAFETY: We just incremented the refcount. This increment is now owned by the new `Arc`.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:237 `LIFETIME_NAMING_PATTERN`

## W-000023 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: refcount_inc
- Explanation: refcount_inc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000001 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: REFCOUNT_INIT
- Explanation: REFCOUNT_INIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000022 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: refcount_dec_and_test
- Explanation: refcount_dec_and_test changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000009 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: end
- Explanation: end changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(10usize, 1u8) as u32) } } #[inline] pub fn set_end(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(11usize, 1u8) as u32) } } #[inline] pub fn set_end(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `2`

## W-000002 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __find_nth_and_andnot_bit
- Explanation: __find_nth_and_andnot_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000004 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __vdso_getcpu
- Explanation: __vdso_getcpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000005 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: _find_next_or_bit
- Explanation: _find_next_or_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000010 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: exit_tasks_rcu_stop
- Explanation: exit_tasks_rcu_stop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000011 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: flags
- Explanation: flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000012 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ibt_save
- Explanation: ibt_save changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'u64_'}`
- New: `{'params': [{'name': 'disable', 'type': 'bool_'}], 'return_type': 'u64_'}`

### Rust Evidence

- Graph edges: `1`

## W-000013 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kvfree_call_rcu
- Explanation: kvfree_call_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'head', 'type': '*mut callback_head'}, {'name': 'func', 'type': 'rcu_callback_t'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'head', 'type': '*mut callback_head'}, {'name': 'ptr', 'type': '*mut core::ffi::c_void'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000014 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kvmemdup
- Explanation: kvmemdup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000017 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mas_preallocate
- Explanation: mas_preallocate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'mas', 'type': '*mut ma_state'}, {'name': 'entry', 'type': '*mut core::ffi::c_void'}, {'name': 'gfp', 'type': 'gfp_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'mas', 'type': '*mut ma_state'}, {'name': 'gfp', 'type': 'gfp_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000018 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: microcode_check
- Explanation: microcode_check changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': '()'}`
- New: `{'params': [{'name': 'prev_info', 'type': '*mut cpuinfo_x86'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000024 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sched_numa_find_nth_cpu
- Explanation: sched_numa_find_nth_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000025 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sched_numa_hop_mask
- Explanation: sched_numa_hop_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000026 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: signal
- Explanation: signal changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000027 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: store_cpu_caps
- Explanation: store_cpu_caps changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000035 FieldDrift

- Risk: High
- Score: 10.2
- Symbol: unwind_hint
- Explanation: unwind_hint changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'ip', 'type': 'u32_'}, {'name': 'sp_offset', 'type': 's16'}, {'name': 'sp_reg', 'type': 'u8_'}, {'name': 'type_', 'type': 'u8_'}, {'name': 'end', 'type': 'u8_'}]`
- New: `[{'name': 'ip', 'type': 'u32_'}, {'name': 'sp_offset', 'type': 's16'}, {'name': 'sp_reg', 'type': 'u8_'}, {'name': 'type_', 'type': 'u8_'}, {'name': 'signal', 'type': 'u8_'}, {'name': 'end', 'type': 'u8_'}]`

### Rust Evidence

- Graph edges: `8`

## W-000003 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __this_cpu_preempt_check
- Explanation: __this_cpu_preempt_check changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000006 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: asm_load_gs_index
- Explanation: asm_load_gs_index changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000008 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: debug_smp_processor_id
- Explanation: debug_smp_processor_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000015 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mas_dup_store
- Explanation: mas_dup_store changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000016 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mas_dup_tree
- Explanation: mas_dup_tree changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000019 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: percpu_counter_sum_all
- Explanation: percpu_counter_sum_all changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000020 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: preempt_count_add
- Explanation: preempt_count_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000021 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: preempt_count_sub
- Explanation: preempt_count_sub changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000028 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sysenter_setup
- Explanation: sysenter_setup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000029 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: alt_instr
- Explanation: alt_instr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'instr_offset', 'type': 's32'}, {'name': 'repl_offset', 'type': 's32'}, {'name': 'cpuid', 'type': 'u16_'}, {'name': 'instrlen', 'type': 'u8_'}, {'name': 'replacementlen', 'type': 'u8_'}]`
- New: `[{'name': '_bindgen_opaque_blob', 'type': '[u8; 14usize]'}]`

### Rust Evidence

- Graph edges: `2`

## W-000036 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: vm_area_struct
- Explanation: vm_area_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'vm_start', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_end', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_mm', 'type': '*mut mm_struct'}, {'name': 'vm_page_prot', 'type': 'pgprot_t'}, {'name': 'vm_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'shared', 'type': 'vm_area_struct__bindgen_ty_1'}, {'name': 'anon_vma_chain', 'type': 'list_head'}, {'name': 'anon_vma', 'type': '*mut anon_vma'}, {'name': 'vm_ops', 'type': '*mut vm_operations_struct'}, {'name': 'vm_pgoff', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_file', 'type': '*mut file'}, {'name': 'vm_private_data', 'type': '*mut core::ffi::c_void'}, {'name': 'swap_readahead_info', 'type': 'atomic_long_t'}, {'name': 'vm_policy', 'type': '*mut mempolicy'}, {'name': 'vm_userfaultfd_ctx', 'type': 'vm_userfaultfd_ctx'}]`
- New: `[{'name': 'vm_start', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_end', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_mm', 'type': '*mut mm_struct'}, {'name': 'vm_page_prot', 'type': 'pgprot_t'}, {'name': '__bindgen_anon_1', 'type': 'vm_area_struct__bindgen_ty_1'}, {'name': 'shared', 'type': 'vm_area_struct__bindgen_ty_2'}, {'name': 'anon_vma_chain', 'type': 'list_head'}, {'name': 'anon_vma', 'type': '*mut anon_vma'}, {'name': 'vm_ops', 'type': '*mut vm_operations_struct'}, {'name': 'vm_pgoff', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_file', 'type': '*mut file'}, {'name': 'vm_private_data', 'type': '*mut core::ffi::c_void'}, {'name': 'swap_readahead_info', 'type': 'atomic_long_t'}, {'name': 'vm_policy', 'type': '*mut mempolicy'}, {'name': 'vm_userfaultfd_ctx', 'type': 'vm_userfaultfd_ctx'}]`

### Rust Evidence

- Graph edges: `2`

## W-000030 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: folio__bindgen_ty_2__bindgen_ty_1
- Explanation: folio__bindgen_ty_2__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_flags_1', 'type': 'core::ffi::c_ulong'}, {'name': '_head_1', 'type': 'core::ffi::c_ulong'}, {'name': '_folio_dtor', 'type': 'core::ffi::c_uchar'}, {'name': '_folio_order', 'type': 'core::ffi::c_uchar'}, {'name': '_compound_mapcount', 'type': 'atomic_t'}, {'name': '_subpages_mapcount', 'type': 'atomic_t'}, {'name': '_pincount', 'type': 'atomic_t'}, {'name': '_folio_nr_pages', 'type': 'core::ffi::c_uint'}]`
- New: `[{'name': '_flags_1', 'type': 'core::ffi::c_ulong'}, {'name': '_head_1', 'type': 'core::ffi::c_ulong'}, {'name': '_folio_dtor', 'type': 'core::ffi::c_uchar'}, {'name': '_folio_order', 'type': 'core::ffi::c_uchar'}, {'name': '_entire_mapcount', 'type': 'atomic_t'}, {'name': '_nr_pages_mapped', 'type': 'atomic_t'}, {'name': '_pincount', 'type': 'atomic_t'}, {'name': '_folio_nr_pages', 'type': 'core::ffi::c_uint'}]`

### Rust Evidence

- Graph edges: `1`

## W-000031 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: mm_struct__bindgen_ty_1
- Explanation: mm_struct__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mm_mt', 'type': 'maple_tree'}, {'name': 'get_unmapped_area', 'type': '::core::option::Option<'}, {'name': 'mmap_base', 'type': 'core::ffi::c_ulong'}, {'name': 'mmap_legacy_base', 'type': 'core::ffi::c_ulong'}, {'name': 'mmap_compat_base', 'type': 'core::ffi::c_ulong'}, {'name': 'mmap_compat_legacy_base', 'type': 'core::ffi::c_ulong'}, {'name': 'task_size', 'type': 'core::ffi::c_ulong'}, {'name': 'pgd', 'type': '*mut pgd_t'}, {'name': 'membarrier_state', 'type': 'atomic_t'}, {'name': 'mm_users', 'type': 'atomic_t'}, {'name': 'mm_count', 'type': 'atomic_t'}, {'name': 'pgtables_bytes', 'type': 'atomic_long_t'}, {'name': 'map_count', 'type': 'core::ffi::c_int'}, {'name': 'page_table_lock', 'type': 'spinlock_t'}, {'name': 'mmap_lock', 'type': 'rw_semaphore'}, {'name': 'mmlist', 'type': 'list_head'}, {'name': 'hiwater_rss', 'type': 'core::ffi::c_ulong'}, {'name': 'hiwater_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'total_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'locked_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'pinned_vm', 'type': 'atomic64_t'}, {'name': 'data_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'exec_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'stack_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'def_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'write_protect_seq', 'type': 'seqcount_t'}, {'name': 'arg_lock', 'type': 'spinlock_t'}, {'name': 'start_code', 'type': 'core::ffi::c_ulong'}, {'name': 'end_code', 'type': 'core::ffi::c_ulong'}, {'name': 'start_data', 'type': 'core::ffi::c_ulong'}, {'name': 'end_data', 'type': 'core::ffi::c_ulong'}, {'name': 'start_brk', 'type': 'core::ffi::c_ulong'}, {'name': 'brk', 'type': 'core::ffi::c_ulong'}, {'name': 'start_stack', 'type': 'core::ffi::c_ulong'}, {'name': 'arg_start', 'type': 'core::ffi::c_ulong'}, {'name': 'arg_end', 'type': 'core::ffi::c_ulong'}, {'name': 'env_start', 'type': 'core::ffi::c_ulong'}, {'name': 'env_end', 'type': 'core::ffi::c_ulong'}, {'name': 'saved_auxv', 'type': '[core::ffi::c_ulong; 48usize]'}, {'name': 'rss_stat', 'type': '[percpu_counter; 4usize]'}, {'name': 'binfmt', 'type': '*mut linux_binfmt'}, {'name': 'context', 'type': 'mm_context_t'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'ioctx_lock', 'type': 'spinlock_t'}, {'name': 'ioctx_table', 'type': '*mut kioctx_table'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'exe_file', 'type': '*mut file'}, {'name': 'notifier_subscriptions', 'type': '*mut mmu_notifier_subscriptions'}, {'name': 'tlb_flush_pending', 'type': 'atomic_t'}, {'name': 'tlb_flush_batched', 'type': 'atomic_t'}, {'name': 'uprobes_state', 'type': 'uprobes_state'}, {'name': 'hugetlb_usage', 'type': 'atomic_long_t'}, {'name': 'async_put_work', 'type': 'work_struct'}]`
- New: `[{'name': 'mm_mt', 'type': 'maple_tree'}, {'name': 'get_unmapped_area', 'type': '::core::option::Option<'}, {'name': 'mmap_base', 'type': 'core::ffi::c_ulong'}, {'name': 'mmap_legacy_base', 'type': 'core::ffi::c_ulong'}, {'name': 'mmap_compat_base', 'type': 'core::ffi::c_ulong'}, {'name': 'mmap_compat_legacy_base', 'type': 'core::ffi::c_ulong'}, {'name': 'task_size', 'type': 'core::ffi::c_ulong'}, {'name': 'pgd', 'type': '*mut pgd_t'}, {'name': 'membarrier_state', 'type': 'atomic_t'}, {'name': 'mm_users', 'type': 'atomic_t'}, {'name': 'mm_count', 'type': 'atomic_t'}, {'name': 'cid_lock', 'type': 'raw_spinlock_t'}, {'name': 'pgtables_bytes', 'type': 'atomic_long_t'}, {'name': 'map_count', 'type': 'core::ffi::c_int'}, {'name': 'page_table_lock', 'type': 'spinlock_t'}, {'name': 'mmap_lock', 'type': 'rw_semaphore'}, {'name': 'mmlist', 'type': 'list_head'}, {'name': 'hiwater_rss', 'type': 'core::ffi::c_ulong'}, {'name': 'hiwater_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'total_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'locked_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'pinned_vm', 'type': 'atomic64_t'}, {'name': 'data_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'exec_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'stack_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'def_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'write_protect_seq', 'type': 'seqcount_t'}, {'name': 'arg_lock', 'type': 'spinlock_t'}, {'name': 'start_code', 'type': 'core::ffi::c_ulong'}, {'name': 'end_code', 'type': 'core::ffi::c_ulong'}, {'name': 'start_data', 'type': 'core::ffi::c_ulong'}, {'name': 'end_data', 'type': 'core::ffi::c_ulong'}, {'name': 'start_brk', 'type': 'core::ffi::c_ulong'}, {'name': 'brk', 'type': 'core::ffi::c_ulong'}, {'name': 'start_stack', 'type': 'core::ffi::c_ulong'}, {'name': 'arg_start', 'type': 'core::ffi::c_ulong'}, {'name': 'arg_end', 'type': 'core::ffi::c_ulong'}, {'name': 'env_start', 'type': 'core::ffi::c_ulong'}, {'name': 'env_end', 'type': 'core::ffi::c_ulong'}, {'name': 'saved_auxv', 'type': '[core::ffi::c_ulong; 52usize]'}, {'name': 'rss_stat', 'type': '[percpu_counter; 4usize]'}, {'name': 'binfmt', 'type': '*mut linux_binfmt'}, {'name': 'context', 'type': 'mm_context_t'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'ioctx_lock', 'type': 'spinlock_t'}, {'name': 'ioctx_table', 'type': '*mut kioctx_table'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'exe_file', 'type': '*mut file'}, {'name': 'notifier_subscriptions', 'type': '*mut mmu_notifier_subscriptions'}, {'name': 'tlb_flush_pending', 'type': 'atomic_t'}, {'name': 'tlb_flush_batched', 'type': 'atomic_t'}, {'name': 'uprobes_state', 'type': 'uprobes_state'}, {'name': 'hugetlb_usage', 'type': 'atomic_long_t'}, {'name': 'async_put_work', 'type': 'work_struct'}]`

### Rust Evidence

- Graph edges: `1`

## W-000032 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: page__bindgen_ty_1__bindgen_ty_3
- Explanation: page__bindgen_ty_1__bindgen_ty_3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'compound_head', 'type': 'core::ffi::c_ulong'}, {'name': 'compound_dtor', 'type': 'core::ffi::c_uchar'}, {'name': 'compound_order', 'type': 'core::ffi::c_uchar'}, {'name': 'compound_mapcount', 'type': 'atomic_t'}, {'name': 'subpages_mapcount', 'type': 'atomic_t'}, {'name': 'compound_pincount', 'type': 'atomic_t'}, {'name': 'compound_nr', 'type': 'core::ffi::c_uint'}]`
- New: `[{'name': 'compound_head', 'type': 'core::ffi::c_ulong'}]`

### Rust Evidence

- Graph edges: `1`

## W-000033 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: page__bindgen_ty_1__bindgen_ty_4
- Explanation: page__bindgen_ty_1__bindgen_ty_4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_compound_pad_1', 'type': 'core::ffi::c_ulong'}, {'name': '_compound_pad_2', 'type': 'core::ffi::c_ulong'}, {'name': 'deferred_list', 'type': 'list_head'}]`
- New: `[{'name': '_pt_pad_1', 'type': 'core::ffi::c_ulong'}, {'name': 'pmd_huge_pte', 'type': 'pgtable_t'}, {'name': '_pt_pad_2', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'page__bindgen_ty_1__bindgen_ty_4__bindgen_ty_1'}, {'name': 'ptl', 'type': 'spinlock_t'}]`

### Rust Evidence

- Graph edges: `1`

## W-000034 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: page__bindgen_ty_1__bindgen_ty_5
- Explanation: page__bindgen_ty_1__bindgen_ty_5 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_hugetlb_pad_1', 'type': 'core::ffi::c_ulong'}, {'name': 'hugetlb_subpool', 'type': '*mut core::ffi::c_void'}, {'name': 'hugetlb_cgroup', 'type': '*mut core::ffi::c_void'}, {'name': 'hugetlb_cgroup_rsvd', 'type': '*mut core::ffi::c_void'}, {'name': 'hugetlb_hwpoison', 'type': '*mut core::ffi::c_void'}]`
- New: `[{'name': 'pgmap', 'type': '*mut dev_pagemap'}, {'name': 'zone_device_data', 'type': '*mut core::ffi::c_void'}]`

### Rust Evidence

- Graph edges: `1`

## W-000037 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: AT_VECTOR_SIZE
- Explanation: AT_VECTOR_SIZE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `52`

### Rust Evidence

- Graph edges: `3`

## W-000038 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: AT_VECTOR_SIZE_BASE
- Explanation: AT_VECTOR_SIZE_BASE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `20`
- New: `22`

### Rust Evidence

- Graph edges: `1`

## W-000039 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: CONFIG_CLOCKSOURCE_WATCHDOG_MAX_SKEW_US
- Explanation: CONFIG_CLOCKSOURCE_WATCHDOG_MAX_SKEW_US changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `100`
- New: `125`

### Rust Evidence

- Graph edges: `1`

## W-000040 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: MAX_CPU_FEATURES
- Explanation: MAX_CPU_FEATURES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `640`
- New: `672`

### Rust Evidence

- Graph edges: `1`

## W-000041 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: MM_MT_FLAGS
- Explanation: MM_MT_FLAGS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `769`
- New: `771`

### Rust Evidence

- Graph edges: `1`

## W-000042 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: NCAPINTS
- Explanation: NCAPINTS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `20`
- New: `21`

### Rust Evidence

- Graph edges: `1`

## W-000043 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TDX_HYPERCALL_r10
- Explanation: TDX_HYPERCALL_r10 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0`
- New: `16`

### Rust Evidence

- Graph edges: `1`

## W-000044 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TDX_HYPERCALL_r11
- Explanation: TDX_HYPERCALL_r11 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `24`

### Rust Evidence

- Graph edges: `1`

## W-000045 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TDX_HYPERCALL_r12
- Explanation: TDX_HYPERCALL_r12 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `32`

### Rust Evidence

- Graph edges: `1`

## W-000046 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TDX_HYPERCALL_r13
- Explanation: TDX_HYPERCALL_r13 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `24`
- New: `40`

### Rust Evidence

- Graph edges: `1`

## W-000047 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TDX_HYPERCALL_r14
- Explanation: TDX_HYPERCALL_r14 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `32`
- New: `48`

### Rust Evidence

- Graph edges: `1`

## W-000048 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TDX_HYPERCALL_r15
- Explanation: TDX_HYPERCALL_r15 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `40`
- New: `56`

### Rust Evidence

- Graph edges: `1`

## W-000049 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: X86_FEATURE_LFENCE_RDTSC
- Explanation: X86_FEATURE_LFENCE_RDTSC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `114`
- New: `642`

### Rust Evidence

- Graph edges: `1`
