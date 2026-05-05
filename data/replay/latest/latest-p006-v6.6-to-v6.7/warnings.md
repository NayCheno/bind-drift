# BindDrift Ranked Warnings

## W-000940 SignatureDrift

- Risk: High
- Score: 14.6
- Symbol: up
- Explanation: up changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `47`

## W-000266 SignatureDrift

- Risk: High
- Score: 13.2
- Symbol: down
- Explanation: down changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `13`

## W-000863 SignatureDrift

- Risk: High
- Score: 13.2
- Symbol: siginfo_layout
- Explanation: siginfo_layout changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `13`

## W-000353 SignatureDrift

- Risk: High
- Score: 12.8
- Symbol: force_sig
- Explanation: force_sig changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `11`

## W-000821 SignatureDrift

- Risk: High
- Score: 12.8
- Symbol: send_sig
- Explanation: send_sig changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `11`

## W-001012 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: file
- Explanation: file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'file__bindgen_ty_1'}, {'name': 'f_lock', 'type': 'spinlock_t'}, {'name': 'f_mode', 'type': 'fmode_t'}, {'name': 'f_count', 'type': 'atomic_long_t'}, {'name': 'f_pos_lock', 'type': 'mutex'}, {'name': 'f_pos', 'type': 'loff_t'}, {'name': 'f_flags', 'type': 'core::ffi::c_uint'}, {'name': 'f_owner', 'type': 'fown_struct'}, {'name': 'f_cred', 'type': '*const cred'}, {'name': 'f_ra', 'type': 'file_ra_state'}, {'name': 'f_path', 'type': 'path'}, {'name': 'f_inode', 'type': '*mut inode'}, {'name': 'f_op', 'type': '*const file_operations'}, {'name': 'f_version', 'type': 'u64_'}, {'name': 'f_security', 'type': '*mut core::ffi::c_void'}, {'name': 'private_data', 'type': '*mut core::ffi::c_void'}, {'name': 'f_ep', 'type': '*mut hlist_head'}, {'name': 'f_mapping', 'type': '*mut address_space'}, {'name': 'f_wb_err', 'type': 'errseq_t'}, {'name': 'f_sb_err', 'type': 'errseq_t'}]`

### Rust Evidence

- Graph edges: `38`

## W-001016 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: inode
- Explanation: inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'i_mode', 'type': 'umode_t'}, {'name': 'i_opflags', 'type': 'core::ffi::c_ushort'}, {'name': 'i_uid', 'type': 'kuid_t'}, {'name': 'i_gid', 'type': 'kgid_t'}, {'name': 'i_flags', 'type': 'core::ffi::c_uint'}, {'name': 'i_acl', 'type': '*mut posix_acl'}, {'name': 'i_default_acl', 'type': '*mut posix_acl'}, {'name': 'i_op', 'type': '*const inode_operations'}, {'name': 'i_sb', 'type': '*mut super_block'}, {'name': 'i_mapping', 'type': '*mut address_space'}, {'name': 'i_security', 'type': '*mut core::ffi::c_void'}, {'name': 'i_ino', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'inode__bindgen_ty_1'}, {'name': 'i_rdev', 'type': 'dev_t'}, {'name': 'i_size', 'type': 'loff_t'}, {'name': '__i_atime', 'type': 'timespec64'}, {'name': '__i_mtime', 'type': 'timespec64'}, {'name': '__i_ctime', 'type': 'timespec64'}, {'name': 'i_lock', 'type': 'spinlock_t'}, {'name': 'i_bytes', 'type': 'core::ffi::c_ushort'}, {'name': 'i_blkbits', 'type': 'u8_'}, {'name': 'i_write_hint', 'type': 'u8_'}, {'name': 'i_blocks', 'type': 'blkcnt_t'}, {'name': 'i_state', 'type': 'core::ffi::c_ulong'}, {'name': 'i_rwsem', 'type': 'rw_semaphore'}, {'name': 'dirtied_when', 'type': 'core::ffi::c_ulong'}, {'name': 'dirtied_time_when', 'type': 'core::ffi::c_ulong'}, {'name': 'i_hash', 'type': 'hlist_node'}, {'name': 'i_io_list', 'type': 'list_head'}, {'name': 'i_lru', 'type': 'list_head'}, {'name': 'i_sb_list', 'type': 'list_head'}, {'name': 'i_wb_list', 'type': 'list_head'}, {'name': '__bindgen_anon_2', 'type': 'inode__bindgen_ty_2'}, {'name': 'i_version', 'type': 'atomic64_t'}, {'name': 'i_sequence', 'type': 'atomic64_t'}, {'name': 'i_count', 'type': 'atomic_t'}, {'name': 'i_dio_count', 'type': 'atomic_t'}, {'name': 'i_writecount', 'type': 'atomic_t'}, {'name': 'i_readcount', 'type': 'atomic_t'}, {'name': '__bindgen_anon_3', 'type': 'inode__bindgen_ty_3'}, {'name': 'i_flctx', 'type': '*mut file_lock_context'}, {'name': 'i_data', 'type': 'address_space'}, {'name': 'i_devices', 'type': 'list_head'}, {'name': '__bindgen_anon_4', 'type': 'inode__bindgen_ty_4'}, {'name': 'i_generation', 'type': '__u32'}, {'name': 'i_fsnotify_mask', 'type': '__u32'}, {'name': 'i_fsnotify_marks', 'type': '*mut fsnotify_mark_connector'}, {'name': 'i_private', 'type': '*mut core::ffi::c_void'}]`

### Rust Evidence

- Graph edges: `31`

## W-001019 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: key
- Explanation: key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[{'name': 'usage', 'type': 'refcount_t'}, {'name': 'serial', 'type': 'key_serial_t'}, {'name': '__bindgen_anon_1', 'type': 'key__bindgen_ty_1'}, {'name': 'sem', 'type': 'rw_semaphore'}, {'name': 'user', 'type': '*mut key_user'}, {'name': 'security', 'type': '*mut core::ffi::c_void'}, {'name': '__bindgen_anon_2', 'type': 'key__bindgen_ty_2'}, {'name': 'last_used_at', 'type': 'time64_t'}, {'name': 'uid', 'type': 'kuid_t'}, {'name': 'gid', 'type': 'kgid_t'}, {'name': 'perm', 'type': 'key_perm_t'}, {'name': 'quotalen', 'type': 'core::ffi::c_ushort'}, {'name': 'datalen', 'type': 'core::ffi::c_ushort'}, {'name': 'state', 'type': 'core::ffi::c_short'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_3', 'type': 'key__bindgen_ty_3'}, {'name': '__bindgen_anon_4', 'type': 'key__bindgen_ty_4'}, {'name': 'restrict_link', 'type': '*mut key_restriction'}]`

### Rust Evidence

- Graph edges: `50`

## W-001020 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: kunit
- Explanation: kunit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'priv_', 'type': '*mut core::ffi::c_void'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'log', 'type': '*mut core::ffi::c_char'}, {'name': 'try_catch', 'type': 'kunit_try_catch'}, {'name': 'param_value', 'type': '*const core::ffi::c_void'}, {'name': 'param_index', 'type': 'core::ffi::c_int'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'status', 'type': 'kunit_status'}, {'name': 'resources', 'type': 'list_head'}, {'name': 'status_comment', 'type': '[core::ffi::c_char; 256usize]'}]`
- New: `[{'name': 'priv_', 'type': '*mut core::ffi::c_void'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'log', 'type': '*mut string_stream'}, {'name': 'try_catch', 'type': 'kunit_try_catch'}, {'name': 'param_value', 'type': '*const core::ffi::c_void'}, {'name': 'param_index', 'type': 'core::ffi::c_int'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'status', 'type': 'kunit_status'}, {'name': 'resources', 'type': 'list_head'}, {'name': 'status_comment', 'type': '[core::ffi::c_char; 256usize]'}]`

### Rust Evidence

- Graph edges: `50`

## W-001033 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: zone
- Explanation: zone changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_watermark', 'type': '[core::ffi::c_ulong; 4usize]'}, {'name': 'watermark_boost', 'type': 'core::ffi::c_ulong'}, {'name': 'nr_reserved_highatomic', 'type': 'core::ffi::c_ulong'}, {'name': 'lowmem_reserve', 'type': '[core::ffi::c_long; 4usize]'}, {'name': 'node', 'type': 'core::ffi::c_int'}, {'name': 'zone_pgdat', 'type': '*mut pglist_data'}, {'name': 'per_cpu_pageset', 'type': '*mut per_cpu_pages'}, {'name': 'per_cpu_zonestats', 'type': '*mut per_cpu_zonestat'}, {'name': 'pageset_high', 'type': 'core::ffi::c_int'}, {'name': 'pageset_batch', 'type': 'core::ffi::c_int'}, {'name': 'zone_start_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'managed_pages', 'type': 'atomic_long_t'}, {'name': 'spanned_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'present_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'initialized', 'type': 'core::ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': '[u64; 3usize]'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': 'free_area', 'type': '[free_area; 11usize]'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': '__bindgen_padding_1', 'type': '[u64; 3usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'percpu_drift_mark', 'type': 'core::ffi::c_ulong'}, {'name': 'compact_cached_free_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'compact_cached_migrate_pfn', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'compact_init_migrate_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'compact_init_free_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'compact_considered', 'type': 'core::ffi::c_uint'}, {'name': 'compact_defer_shift', 'type': 'core::ffi::c_uint'}, {'name': 'compact_order_failed', 'type': 'core::ffi::c_int'}, {'name': 'compact_blockskip_flush', 'type': 'bool_'}, {'name': 'contiguous', 'type': 'bool_'}, {'name': '__bindgen_padding_2', 'type': '[u64; 0usize]'}, {'name': '_pad3_', 'type': 'cacheline_padding'}, {'name': 'vm_stat', 'type': '[atomic_long_t; 10usize]'}, {'name': 'vm_numa_event', 'type': '[atomic_long_t; 6usize]'}]`
- New: `[{'name': '_watermark', 'type': '[core::ffi::c_ulong; 4usize]'}, {'name': 'watermark_boost', 'type': 'core::ffi::c_ulong'}, {'name': 'nr_reserved_highatomic', 'type': 'core::ffi::c_ulong'}, {'name': 'lowmem_reserve', 'type': '[core::ffi::c_long; 4usize]'}, {'name': 'node', 'type': 'core::ffi::c_int'}, {'name': 'zone_pgdat', 'type': '*mut pglist_data'}, {'name': 'per_cpu_pageset', 'type': '*mut per_cpu_pages'}, {'name': 'per_cpu_zonestats', 'type': '*mut per_cpu_zonestat'}, {'name': 'pageset_high_min', 'type': 'core::ffi::c_int'}, {'name': 'pageset_high_max', 'type': 'core::ffi::c_int'}, {'name': 'pageset_batch', 'type': 'core::ffi::c_int'}, {'name': 'zone_start_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'managed_pages', 'type': 'atomic_long_t'}, {'name': 'spanned_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'present_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'initialized', 'type': 'core::ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': '[u64; 2usize]'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': 'free_area', 'type': '[free_area; 11usize]'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': '__bindgen_padding_1', 'type': '[u64; 3usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'percpu_drift_mark', 'type': 'core::ffi::c_ulong'}, {'name': 'compact_cached_free_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'compact_cached_migrate_pfn', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'compact_init_migrate_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'compact_init_free_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'compact_considered', 'type': 'core::ffi::c_uint'}, {'name': 'compact_defer_shift', 'type': 'core::ffi::c_uint'}, {'name': 'compact_order_failed', 'type': 'core::ffi::c_int'}, {'name': 'compact_blockskip_flush', 'type': 'bool_'}, {'name': 'contiguous', 'type': 'bool_'}, {'name': '__bindgen_padding_2', 'type': '[u64; 0usize]'}, {'name': '_pad3_', 'type': 'cacheline_padding'}, {'name': 'vm_stat', 'type': '[atomic_long_t; 10usize]'}, {'name': 'vm_numa_event', 'type': '[atomic_long_t; 6usize]'}]`

### Rust Evidence

- Graph edges: `38`

## W-000573 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: key_alloc
- Explanation: key_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000310 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: fasync_helper
- Explanation: fasync_helper changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000142 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: bit_wait
- Explanation: bit_wait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000204 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: d_alloc
- Explanation: d_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000497 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: inode_init
- Explanation: inode_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000919 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: sync_file_range
- Explanation: sync_file_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000218 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: d_instantiate
- Explanation: d_instantiate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000306 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: f_getown
- Explanation: f_getown changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000444 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: getname
- Explanation: getname changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000492 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: init_work_with_key
- Explanation: init_work_with_key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000582 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: key_lookup
- Explanation: key_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-001023 FieldDrift

- Risk: High
- Score: 11.4
- Symbol: list_lru
- Explanation: list_lru changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'node', 'type': '*mut list_lru_node'}]`

### Rust Evidence

- Graph edges: `14`

## W-000011 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: __d_lookup
- Explanation: __d_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000097 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: __sys_socket
- Explanation: __sys_socket changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000113 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: _copy_from_iter
- Explanation: _copy_from_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000307 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: f_setown
- Explanation: f_setown changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000355 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: force_sig_fault
- Explanation: force_sig_fault changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000472 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: ilookup
- Explanation: ilookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000603 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: kill_pid
- Explanation: kill_pid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000626 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: lockref_get
- Explanation: lockref_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000697 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: ns_capable
- Explanation: ns_capable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000704 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: out_of_line_wait_on_bit
- Explanation: out_of_line_wait_on_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000738 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: ptdump_walk_pgd_level
- Explanation: ptdump_walk_pgd_level changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000752 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: put_cmsg
- Explanation: put_cmsg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000853 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: sget
- Explanation: sget changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000893 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: simple_rename
- Explanation: simple_rename changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000065 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __put_task_struct
- Explanation: __put_task_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000076 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __register_chrdev
- Explanation: __register_chrdev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000082 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __sys_connect
- Explanation: __sys_connect changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000089 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __sys_recvmsg
- Explanation: __sys_recvmsg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000092 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __sys_sendmsg
- Explanation: __sys_sendmsg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000095 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __sys_shutdown
- Explanation: __sys_shutdown changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000103 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __wait_on_bit
- Explanation: __wait_on_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000136 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: assoc_array_insert
- Explanation: assoc_array_insert changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000143 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: bit_wait_io
- Explanation: bit_wait_io changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000150 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: bmap
- Explanation: bmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000154 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: capable
- Explanation: capable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000178 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: copy_page_from_iter
- Explanation: copy_page_from_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000180 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: copy_page_to_iter
- Explanation: copy_page_to_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000183 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: copy_siginfo_from_user
- Explanation: copy_siginfo_from_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000202 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: d_add
- Explanation: d_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000213 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: d_find_alias
- Explanation: d_find_alias changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000248 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: dentry_path
- Explanation: dentry_path changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000274 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: drop_super
- Explanation: drop_super changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000281 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: early_memremap_decrypted
- Explanation: early_memremap_decrypted changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000283 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: early_memremap_encrypted
- Explanation: early_memremap_encrypted changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000290 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: errseq_check
- Explanation: errseq_check changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000393 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: from_kqid
- Explanation: from_kqid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000410 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: generic_file_llseek
- Explanation: generic_file_llseek changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000428 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: generic_write_checks
- Explanation: generic_write_checks changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000455 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: has_capability
- Explanation: has_capability changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000458 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: has_ns_capability
- Explanation: has_ns_capability changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000473 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: ilookup5
- Explanation: ilookup5 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000513 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: inode_update_time
- Explanation: inode_update_time changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000515 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: insert_inode_locked
- Explanation: insert_inode_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000554 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: iterate_supers
- Explanation: iterate_supers changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000560 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: kern_unmount
- Explanation: kern_unmount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000562 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: kernel_clone
- Explanation: kernel_clone changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000570 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: kernel_wait
- Explanation: kernel_wait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000574 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: key_create
- Explanation: key_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000584 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: key_put
- Explanation: key_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000618 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: list_lru_isolate
- Explanation: list_lru_isolate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000621 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: list_lru_walk_one
- Explanation: list_lru_walk_one changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000644 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: may_umount
- Explanation: may_umount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000650 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: mmu_interval_notifier_insert
- Explanation: mmu_interval_notifier_insert changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000661 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: mnt_drop_write
- Explanation: mnt_drop_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000670 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: mnt_want_write
- Explanation: mnt_want_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000684 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: new_inode
- Explanation: new_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000689 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: no_seek_end_llseek
- Explanation: no_seek_end_llseek changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000753 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: put_cmsg_scm_timestamping
- Explanation: put_cmsg_scm_timestamping changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000775 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: rcu_sync_enter
- Explanation: rcu_sync_enter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000783 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: recalc_sigpending
- Explanation: recalc_sigpending changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000815 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: sched_dead
- Explanation: sched_dead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000822 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: send_sig_fault
- Explanation: send_sig_fault changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000832 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: set_anon_super
- Explanation: set_anon_super changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000843 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: set_security_override
- Explanation: set_security_override changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000873 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: simple_attr_write
- Explanation: simple_attr_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000912 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: strncpy_from_user
- Explanation: strncpy_from_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000914 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: strnlen_user
- Explanation: strnlen_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000916 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: super_setup_bdi
- Explanation: super_setup_bdi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000948 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vfs_caches_init
- Explanation: vfs_caches_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000952 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vfs_create
- Explanation: vfs_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000954 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vfs_dedupe_file_range
- Explanation: vfs_dedupe_file_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000960 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vfs_fstat
- Explanation: vfs_fstat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000962 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vfs_fsync
- Explanation: vfs_fsync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000965 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vfs_getattr
- Explanation: vfs_getattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000978 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vfs_read
- Explanation: vfs_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000997 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: work_on_cpu
- Explanation: work_on_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `2`

## W-001102 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __printf
- Explanation: __printf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['2', '3) kunit_log_append(char *log, const char *fmt, ...'], 'return_type': 'void'}`
- New: `{'params': ['1', '2) void set_worker_desc(const char *fmt, ...'], 'return_type': 'extern'}`

### Rust Evidence

- Graph edges: `2`

## W-001140 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: work_on_cpu
- Explanation: work_on_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['cpu', 'fn', 'arg'], 'return_type': 'return'}`
- New: `{'params': ['int cpu', 'long (*fn)(void *)', 'void *arg'], 'return_type': 'static inline long'}`

### Rust Evidence

- Graph edges: `2`

## W-000001 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __blockdev_direct_IO
- Explanation: __blockdev_direct_IO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000002 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __check_sticky
- Explanation: __check_sticky changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000003 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __cleanup_sighand
- Explanation: __cleanup_sighand changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000004 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __compat_save_altstack
- Explanation: __compat_save_altstack changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000005 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __copy_io
- Explanation: __copy_io changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000006 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __copy_msghdr
- Explanation: __copy_msghdr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000007 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __copy_siginfo_to_user32
- Explanation: __copy_siginfo_to_user32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000008 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __copy_user_flushcache
- Explanation: __copy_user_flushcache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000009 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __copy_user_nocache
- Explanation: __copy_user_nocache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000010 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __d_drop
- Explanation: __d_drop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000012 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __d_lookup_rcu
- Explanation: __d_lookup_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000013 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __d_lookup_unhash_wake
- Explanation: __d_lookup_unhash_wake changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000014 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __d_path
- Explanation: __d_path changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000015 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __destroy_inode
- Explanation: __destroy_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000016 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __early_make_pgtable
- Explanation: __early_make_pgtable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000017 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __early_set_fixmap
- Explanation: __early_set_fixmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000018 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __f_setown
- Explanation: __f_setown changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000019 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __flush_tlb_all
- Explanation: __flush_tlb_all changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000020 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __generic_file_fsync
- Explanation: __generic_file_fsync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000021 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __generic_file_write_iter
- Explanation: __generic_file_write_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000022 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __generic_remap_file_range_prep
- Explanation: __generic_remap_file_range_prep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000023 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __get_task_ioprio
- Explanation: __get_task_ioprio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000024 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __get_user_1
- Explanation: __get_user_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000025 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __get_user_2
- Explanation: __get_user_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000026 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __get_user_4
- Explanation: __get_user_4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000027 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __get_user_8
- Explanation: __get_user_8 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000028 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __get_user_bad
- Explanation: __get_user_bad changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000029 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __get_user_nocheck_1
- Explanation: __get_user_nocheck_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000030 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __get_user_nocheck_2
- Explanation: __get_user_nocheck_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000031 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __get_user_nocheck_4
- Explanation: __get_user_nocheck_4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000032 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __get_user_nocheck_8
- Explanation: __get_user_nocheck_8 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000033 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __ia32_sys_ni_syscall
- Explanation: __ia32_sys_ni_syscall changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000034 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __iget
- Explanation: __iget changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000035 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __import_iovec
- Explanation: __import_iovec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000036 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __inode_add_bytes
- Explanation: __inode_add_bytes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000037 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __inode_sub_bytes
- Explanation: __inode_sub_bytes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000038 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __insert_inode_hash
- Explanation: __insert_inode_hash changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000039 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kernel_read
- Explanation: __kernel_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000040 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kernel_write
- Explanation: __kernel_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000041 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kill_pgrp_info
- Explanation: __kill_pgrp_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000042 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __list_lru_init
- Explanation: __list_lru_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000043 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __lock_task_sighand
- Explanation: __lock_task_sighand changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000044 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mark_inode_dirty
- Explanation: __mark_inode_dirty changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000045 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mmap_lock_do_trace_acquire_returned
- Explanation: __mmap_lock_do_trace_acquire_returned changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000046 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mmap_lock_do_trace_released
- Explanation: __mmap_lock_do_trace_released changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000047 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mmap_lock_do_trace_start_locking
- Explanation: __mmap_lock_do_trace_start_locking changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000048 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mmu_notifier_arch_invalidate_secondary_tlbs
- Explanation: __mmu_notifier_arch_invalidate_secondary_tlbs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000049 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mmu_notifier_change_pte
- Explanation: __mmu_notifier_change_pte changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000050 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mmu_notifier_clear_flush_young
- Explanation: __mmu_notifier_clear_flush_young changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000051 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mmu_notifier_clear_young
- Explanation: __mmu_notifier_clear_young changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000052 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mmu_notifier_invalidate_range_end
- Explanation: __mmu_notifier_invalidate_range_end changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000053 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mmu_notifier_invalidate_range_start
- Explanation: __mmu_notifier_invalidate_range_start changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000054 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mmu_notifier_register
- Explanation: __mmu_notifier_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000055 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mmu_notifier_release
- Explanation: __mmu_notifier_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000056 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mmu_notifier_subscriptions_destroy
- Explanation: __mmu_notifier_subscriptions_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000057 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mmu_notifier_test_young
- Explanation: __mmu_notifier_test_young changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000058 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mnt_is_readonly
- Explanation: __mnt_is_readonly changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000059 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __native_set_fixmap
- Explanation: __native_set_fixmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000060 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __percpu_counter_limited_add
- Explanation: __percpu_counter_limited_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000061 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __percpu_down_read
- Explanation: __percpu_down_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000062 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __percpu_init_rwsem
- Explanation: __percpu_init_rwsem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000063 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __pti_set_user_pgtbl
- Explanation: __pti_set_user_pgtbl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000064 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __put_cred
- Explanation: __put_cred changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000066 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __put_task_struct_rcu_cb
- Explanation: __put_task_struct_rcu_cb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000067 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __put_user_1
- Explanation: __put_user_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000068 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __put_user_2
- Explanation: __put_user_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000069 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __put_user_4
- Explanation: __put_user_4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000070 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __put_user_8
- Explanation: __put_user_8 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000071 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __put_user_bad
- Explanation: __put_user_bad changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000072 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __put_user_nocheck_1
- Explanation: __put_user_nocheck_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000073 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __put_user_nocheck_2
- Explanation: __put_user_nocheck_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000074 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __put_user_nocheck_4
- Explanation: __put_user_nocheck_4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000075 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __put_user_nocheck_8
- Explanation: __put_user_nocheck_8 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000077 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __remove_inode_hash
- Explanation: __remove_inode_hash changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000078 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __save_altstack
- Explanation: __save_altstack changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000079 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __set_current_blocked
- Explanation: __set_current_blocked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000080 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sys_accept4
- Explanation: __sys_accept4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000081 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sys_bind
- Explanation: __sys_bind changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000083 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sys_connect_file
- Explanation: __sys_connect_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000084 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sys_getpeername
- Explanation: __sys_getpeername changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000085 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sys_getsockname
- Explanation: __sys_getsockname changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000086 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sys_listen
- Explanation: __sys_listen changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000087 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sys_recvfrom
- Explanation: __sys_recvfrom changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000088 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sys_recvmmsg
- Explanation: __sys_recvmmsg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000090 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sys_recvmsg_sock
- Explanation: __sys_recvmsg_sock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000091 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sys_sendmmsg
- Explanation: __sys_sendmmsg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000093 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sys_sendmsg_sock
- Explanation: __sys_sendmsg_sock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000094 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sys_sendto
- Explanation: __sys_sendto changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000096 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sys_shutdown_sock
- Explanation: __sys_shutdown_sock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000098 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sys_socket_file
- Explanation: __sys_socket_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000099 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sys_socketpair
- Explanation: __sys_socketpair changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000100 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __try_cmpxchg_user_wrong_size
- Explanation: __try_cmpxchg_user_wrong_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000101 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __unregister_chrdev
- Explanation: __unregister_chrdev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000102 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __var_waitqueue
- Explanation: __var_waitqueue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000104 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __wait_on_bit_lock
- Explanation: __wait_on_bit_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000105 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __wake_up_bit
- Explanation: __wake_up_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000107 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __wake_up_parent
- Explanation: __wake_up_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000108 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __x64_sys_getcpu
- Explanation: __x64_sys_getcpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000109 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __x64_sys_gettimeofday
- Explanation: __x64_sys_gettimeofday changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000110 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __x64_sys_ni_syscall
- Explanation: __x64_sys_ni_syscall changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000111 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __x64_sys_time
- Explanation: __x64_sys_time changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000114 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: _copy_from_iter_flushcache
- Explanation: _copy_from_iter_flushcache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000115 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: _copy_from_iter_nocache
- Explanation: _copy_from_iter_nocache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000116 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: _copy_from_user
- Explanation: _copy_from_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000117 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: _copy_mc_to_iter
- Explanation: _copy_mc_to_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000118 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: _copy_to_iter
- Explanation: _copy_to_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000119 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: _copy_to_user
- Explanation: _copy_to_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000120 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: abort_creds
- Explanation: abort_creds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000121 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: address_space_init_once
- Explanation: address_space_init_once changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000122 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_anon_inode
- Explanation: alloc_anon_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000123 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_chrdev_region
- Explanation: alloc_chrdev_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000124 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_pages_mpol
- Explanation: alloc_pages_mpol changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000125 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_uid
- Explanation: alloc_uid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000126 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: always_delete_dentry
- Explanation: always_delete_dentry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000127 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_check_zapped_pmd
- Explanation: arch_check_zapped_pmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000128 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_check_zapped_pte
- Explanation: arch_check_zapped_pte changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000129 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: assoc_array_apply_edit
- Explanation: assoc_array_apply_edit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000130 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: assoc_array_cancel_edit
- Explanation: assoc_array_cancel_edit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000131 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: assoc_array_clear
- Explanation: assoc_array_clear changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000132 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: assoc_array_delete
- Explanation: assoc_array_delete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000133 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: assoc_array_destroy
- Explanation: assoc_array_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000134 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: assoc_array_find
- Explanation: assoc_array_find changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000135 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: assoc_array_gc
- Explanation: assoc_array_gc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000137 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: assoc_array_insert_set_object
- Explanation: assoc_array_insert_set_object changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000138 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: assoc_array_iterate
- Explanation: assoc_array_iterate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000139 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atime_needs_update
- Explanation: atime_needs_update changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000140 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: backing_file_open
- Explanation: backing_file_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000141 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: backing_file_user_path
- Explanation: backing_file_user_path changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000144 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bit_wait_io_timeout
- Explanation: bit_wait_io_timeout changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000145 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bit_wait_timeout
- Explanation: bit_wait_timeout changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000146 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bit_waitqueue
- Explanation: bit_waitqueue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000151 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: calculate_sigpending
- Explanation: calculate_sigpending changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000152 SignatureDrift

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

## W-000153 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_convert_nscap
- Explanation: cap_convert_nscap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000155 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: capable_wrt_inode_uidgid
- Explanation: capable_wrt_inode_uidgid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000156 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: check_fsmapping
- Explanation: check_fsmapping changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000157 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: check_zeroed_user
- Explanation: check_zeroed_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000158 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: chrdev_show
- Explanation: chrdev_show changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000159 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cifs_root_data
- Explanation: cifs_root_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000160 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cleanup_highmap
- Explanation: cleanup_highmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000161 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: clear_inode
- Explanation: clear_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000162 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: clear_nlink
- Explanation: clear_nlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000163 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: clone_private_mount
- Explanation: clone_private_mount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000164 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: collect_mounts
- Explanation: collect_mounts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000165 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: commit_creds
- Explanation: commit_creds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000166 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: compat_arch_ptrace
- Explanation: compat_arch_ptrace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000167 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: compat_get_bitmap
- Explanation: compat_get_bitmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000168 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: compat_ptr_ioctl
- Explanation: compat_ptr_ioctl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000169 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: compat_ptrace_request
- Explanation: compat_ptrace_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000170 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: compat_put_bitmap
- Explanation: compat_put_bitmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000171 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: compat_restore_altstack
- Explanation: compat_restore_altstack changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000172 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_creds
- Explanation: copy_creds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000173 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_from_kernel_nofault_allowed
- Explanation: copy_from_kernel_nofault_allowed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000174 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_from_user_nmi
- Explanation: copy_from_user_nmi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000175 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_from_user_nofault
- Explanation: copy_from_user_nofault changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000176 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_mc_to_kernel
- Explanation: copy_mc_to_kernel changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000177 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_mc_to_user
- Explanation: copy_mc_to_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000179 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_page_from_iter_atomic
- Explanation: copy_page_from_iter_atomic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000181 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_page_to_iter_nofault
- Explanation: copy_page_to_iter_nofault changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000182 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_process
- Explanation: copy_process changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000184 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_siginfo_from_user32
- Explanation: copy_siginfo_from_user32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000185 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_siginfo_to_external32
- Explanation: copy_siginfo_to_external32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000186 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_siginfo_to_user
- Explanation: copy_siginfo_to_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000187 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_splice_read
- Explanation: copy_splice_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000188 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_thread
- Explanation: copy_thread changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000189 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_to_kernel_nofault
- Explanation: copy_to_kernel_nofault changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000190 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_to_user_nofault
- Explanation: copy_to_user_nofault changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000191 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_has_xfeatures
- Explanation: cpu_has_xfeatures changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000192 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cr4_read_shadow
- Explanation: cr4_read_shadow changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000193 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cr4_update_irqsoff
- Explanation: cr4_update_irqsoff changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000194 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: create_io_thread
- Explanation: create_io_thread changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000195 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cred_alloc_blank
- Explanation: cred_alloc_blank changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000196 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cred_fscmp
- Explanation: cred_fscmp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000197 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cred_init
- Explanation: cred_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000198 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: current_is_single_threaded
- Explanation: current_is_single_threaded changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000199 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: current_time
- Explanation: current_time changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000200 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: current_umask
- Explanation: current_umask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000201 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_absolute_path
- Explanation: d_absolute_path changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000203 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_add_ci
- Explanation: d_add_ci changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000205 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_alloc_anon
- Explanation: d_alloc_anon changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000206 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_alloc_name
- Explanation: d_alloc_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000207 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_alloc_parallel
- Explanation: d_alloc_parallel changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000208 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_ancestor
- Explanation: d_ancestor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000209 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_delete
- Explanation: d_delete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000210 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_drop
- Explanation: d_drop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000211 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_exact_alias
- Explanation: d_exact_alias changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000212 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_exchange
- Explanation: d_exchange changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000214 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_find_alias_rcu
- Explanation: d_find_alias_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000215 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_find_any_alias
- Explanation: d_find_any_alias changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000216 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_genocide
- Explanation: d_genocide changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000217 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_hash_and_lookup
- Explanation: d_hash_and_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000219 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_instantiate_anon
- Explanation: d_instantiate_anon changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000220 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_instantiate_new
- Explanation: d_instantiate_new changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000221 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_instantiate_unique
- Explanation: d_instantiate_unique changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000222 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_invalidate
- Explanation: d_invalidate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000223 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_lookup
- Explanation: d_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000224 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_make_root
- Explanation: d_make_root changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000225 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_mark_dontcache
- Explanation: d_mark_dontcache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000226 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_mark_tmpfile
- Explanation: d_mark_tmpfile changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000227 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_move
- Explanation: d_move changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000228 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_obtain_alias
- Explanation: d_obtain_alias changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000229 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_obtain_root
- Explanation: d_obtain_root changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000230 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_path
- Explanation: d_path changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000231 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_prune_aliases
- Explanation: d_prune_aliases changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000232 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_rehash
- Explanation: d_rehash changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000233 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_same_name
- Explanation: d_same_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000234 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_set_d_op
- Explanation: d_set_d_op changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000235 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_set_fallthru
- Explanation: d_set_fallthru changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000236 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_splice_alias
- Explanation: d_splice_alias changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000237 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_tmpfile
- Explanation: d_tmpfile changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000238 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dcache_dir_close
- Explanation: dcache_dir_close changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000239 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dcache_dir_lseek
- Explanation: dcache_dir_lseek changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000240 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dcache_dir_open
- Explanation: dcache_dir_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000241 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dcache_readdir
- Explanation: dcache_readdir changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000242 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: deactivate_locked_super
- Explanation: deactivate_locked_super changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000243 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: deactivate_super
- Explanation: deactivate_super changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000244 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: decay_pcp_high
- Explanation: decay_pcp_high changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000245 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: default_llseek
- Explanation: default_llseek changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000246 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dentry_create
- Explanation: dentry_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000247 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dentry_open
- Explanation: dentry_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000249 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dentry_path_raw
- Explanation: dentry_path_raw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000250 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dequeue_signal
- Explanation: dequeue_signal changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000251 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dget_parent
- Explanation: dget_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000252 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: direct_write_fallback
- Explanation: direct_write_fallback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000253 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: discard_new_inode
- Explanation: discard_new_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000254 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_accept
- Explanation: do_accept changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000255 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_clone_file_range
- Explanation: do_clone_file_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000256 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_group_exit
- Explanation: do_group_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000257 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_mount
- Explanation: do_mount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000258 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_notify_parent
- Explanation: do_notify_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000259 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_pipe_flags
- Explanation: do_pipe_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000260 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_send_sig_info
- Explanation: do_send_sig_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000261 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_sigaction
- Explanation: do_sigaction changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000262 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_splice_direct
- Explanation: do_splice_direct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000263 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_sys_open
- Explanation: do_sys_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000264 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_task_dead
- Explanation: do_task_dead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000265 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_truncate
- Explanation: do_truncate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000267 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: down_interruptible
- Explanation: down_interruptible changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000268 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: down_killable
- Explanation: down_killable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000269 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: down_timeout
- Explanation: down_timeout changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000270 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: down_trylock
- Explanation: down_trylock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000271 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dput
- Explanation: dput changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000272 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drop_collected_mounts
- Explanation: drop_collected_mounts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000273 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drop_nlink
- Explanation: drop_nlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000275 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drop_super_exclusive
- Explanation: drop_super_exclusive changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000276 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dump_mapping
- Explanation: dump_mapping changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000277 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dup_iter
- Explanation: dup_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000278 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dynamic_dname
- Explanation: dynamic_dname changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000279 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: early_alloc_pgt_buf
- Explanation: early_alloc_pgt_buf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000280 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: early_fixup_exception
- Explanation: early_fixup_exception changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000282 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: early_memremap_decrypted_wp
- Explanation: early_memremap_decrypted_wp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000284 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: early_memremap_encrypted_wp
- Explanation: early_memremap_encrypted_wp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000285 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: emergency_remount
- Explanation: emergency_remount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000286 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: emergency_sync
- Explanation: emergency_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000287 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: emergency_thaw_all
- Explanation: emergency_thaw_all changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000289 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: entry_SYSCALL32_ignore
- Explanation: entry_SYSCALL32_ignore changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000291 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: errseq_check_and_advance
- Explanation: errseq_check_and_advance changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000292 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: errseq_sample
- Explanation: errseq_sample changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000293 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: errseq_set
- Explanation: errseq_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000294 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: evict_inodes
- Explanation: evict_inodes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000295 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ex_get_fixup_type
- Explanation: ex_get_fixup_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000296 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ex_handler_msr_mce
- Explanation: ex_handler_msr_mce changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000297 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: exit_creds
- Explanation: exit_creds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000298 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: exit_files
- Explanation: exit_files changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000299 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: exit_io_context
- Explanation: exit_io_context changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000300 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: exit_itimers
- Explanation: exit_itimers changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000301 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: exit_signals
- Explanation: exit_signals changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000302 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: exit_task_stack_account
- Explanation: exit_task_stack_account changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000303 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: exit_thread
- Explanation: exit_thread changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000304 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: extract_iter_to_sg
- Explanation: extract_iter_to_sg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000305 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: f_delown
- Explanation: f_delown changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000308 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fasync_alloc
- Explanation: fasync_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000309 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fasync_free
- Explanation: fasync_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000311 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fasync_insert_entry
- Explanation: fasync_insert_entry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000312 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fasync_remove_entry
- Explanation: fasync_remove_entry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000313 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fault_in_iov_iter_readable
- Explanation: fault_in_iov_iter_readable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000314 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fault_in_iov_iter_writeable
- Explanation: fault_in_iov_iter_writeable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000315 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fc_mount
- Explanation: fc_mount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000316 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fd_statfs
- Explanation: fd_statfs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000317 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: file_check_and_advance_wb_err
- Explanation: file_check_and_advance_wb_err changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000318 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: file_fdatawait_range
- Explanation: file_fdatawait_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000319 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: file_modified
- Explanation: file_modified changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000320 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: file_ns_capable
- Explanation: file_ns_capable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000321 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: file_open_name
- Explanation: file_open_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000322 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: file_open_root
- Explanation: file_open_root changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000323 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: file_path
- Explanation: file_path changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000324 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: file_ra_state_init
- Explanation: file_ra_state_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000325 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: file_remove_privs
- Explanation: file_remove_privs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000326 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: file_update_time
- Explanation: file_update_time changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000327 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: file_write_and_wait_range
- Explanation: file_write_and_wait_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000328 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_invalidate_lock_two
- Explanation: filemap_invalidate_lock_two changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000329 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_invalidate_unlock_two
- Explanation: filemap_invalidate_unlock_two changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000330 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_read
- Explanation: filemap_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000331 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_splice_read
- Explanation: filemap_splice_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000332 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: files_init
- Explanation: files_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000333 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: files_maxfiles_init
- Explanation: files_maxfiles_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000334 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filp_close
- Explanation: filp_close changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000335 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filp_open
- Explanation: filp_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000336 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: find_inode_by_ino_rcu
- Explanation: find_inode_by_ino_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000337 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: find_inode_nowait
- Explanation: find_inode_nowait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000338 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: find_inode_rcu
- Explanation: find_inode_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000339 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: find_user
- Explanation: find_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000340 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: finish_no_open
- Explanation: finish_no_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000341 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: finish_open
- Explanation: finish_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000342 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: finish_rcuwait
- Explanation: finish_rcuwait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000343 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fixed_size_llseek
- Explanation: fixed_size_llseek changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000344 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fixup_bug
- Explanation: fixup_bug changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000345 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fixup_exception
- Explanation: fixup_exception changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000346 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: flush_itimer_signals
- Explanation: flush_itimer_signals changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000347 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: flush_signal_handlers
- Explanation: flush_signal_handlers changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000348 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: flush_signals
- Explanation: flush_signals changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000349 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: flush_sigqueue
- Explanation: flush_sigqueue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000350 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: flush_thread
- Explanation: flush_thread changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000351 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: force_exit_sig
- Explanation: force_exit_sig changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000352 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: force_fatal_sig
- Explanation: force_fatal_sig changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000354 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: force_sig_bnderr
- Explanation: force_sig_bnderr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000356 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: force_sig_fault_to_task
- Explanation: force_sig_fault_to_task changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000357 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: force_sig_fault_trapno
- Explanation: force_sig_fault_trapno changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000358 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: force_sig_info
- Explanation: force_sig_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000359 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: force_sig_mceerr
- Explanation: force_sig_mceerr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000360 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: force_sig_pkuerr
- Explanation: force_sig_pkuerr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000361 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: force_sig_ptrace_errno_trap
- Explanation: force_sig_ptrace_errno_trap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000362 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: force_sig_seccomp
- Explanation: force_sig_seccomp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000363 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: force_sigsegv
- Explanation: force_sigsegv changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000364 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fork_idle
- Explanation: fork_idle changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000365 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fork_init
- Explanation: fork_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000366 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fpregs_assert_state_consistent
- Explanation: fpregs_assert_state_consistent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000367 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fpregs_lock_and_load
- Explanation: fpregs_lock_and_load changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000368 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fpregs_mark_activate
- Explanation: fpregs_mark_activate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000369 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fpstate_clear_xstate_component
- Explanation: fpstate_clear_xstate_component changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000370 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fpstate_free
- Explanation: fpstate_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000371 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fpu__exception_code
- Explanation: fpu__exception_code changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000372 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fpu__init_check_bugs
- Explanation: fpu__init_check_bugs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000373 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fpu__init_cpu
- Explanation: fpu__init_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000374 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fpu__init_system
- Explanation: fpu__init_system changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000375 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fpu__resume_cpu
- Explanation: fpu__resume_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000376 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fpu_alloc_guest_fpstate
- Explanation: fpu_alloc_guest_fpstate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000377 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fpu_copy_guest_fpstate_to_uabi
- Explanation: fpu_copy_guest_fpstate_to_uabi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000378 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fpu_copy_uabi_to_guest_fpstate
- Explanation: fpu_copy_uabi_to_guest_fpstate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000379 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fpu_enable_guest_xfd_features
- Explanation: fpu_enable_guest_xfd_features changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000380 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fpu_free_guest_fpstate
- Explanation: fpu_free_guest_fpstate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000381 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fpu_idle_fpregs
- Explanation: fpu_idle_fpregs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000382 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fpu_reset_from_exception_fixup
- Explanation: fpu_reset_from_exception_fixup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000383 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fpu_swap_kvm_fpstate
- Explanation: fpu_swap_kvm_fpstate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000384 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fpu_sync_fpstate
- Explanation: fpu_sync_fpstate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000385 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fpu_sync_guest_vmexit_xfd_state
- Explanation: fpu_sync_guest_vmexit_xfd_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000386 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fpu_update_guest_xfd
- Explanation: fpu_update_guest_xfd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000387 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fpu_xstate_prctl
- Explanation: fpu_xstate_prctl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000388 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_anon_bdev
- Explanation: free_anon_bdev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000389 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_inode_nonrcu
- Explanation: free_inode_nonrcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000390 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_task
- Explanation: free_task changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000391 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_uid
- Explanation: free_uid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000392 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: freeze_super
- Explanation: freeze_super changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000394 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: from_kqid_munged
- Explanation: from_kqid_munged changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000395 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: from_vfsgid
- Explanation: from_vfsgid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000396 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: from_vfsuid
- Explanation: from_vfsuid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000397 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: frozen
- Explanation: frozen changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(37usize, 1u8) as u32) } } #[inline] pub fn set_frozen(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(38usize, 1u8) as u32) } } #[inline] pub fn set_frozen(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000398 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fs_ftype_to_dtype
- Explanation: fs_ftype_to_dtype changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000399 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fs_umode_to_dtype
- Explanation: fs_umode_to_dtype changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000400 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fs_umode_to_ftype
- Explanation: fs_umode_to_ftype changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000401 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: full_name_hash
- Explanation: full_name_hash changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000402 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generate_random_guid
- Explanation: generate_random_guid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000403 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generate_random_uuid
- Explanation: generate_random_uuid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000404 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_check_addressable
- Explanation: generic_check_addressable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000405 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_copy_file_range
- Explanation: generic_copy_file_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000406 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_delete_inode
- Explanation: generic_delete_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000407 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_fadvise
- Explanation: generic_fadvise changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000408 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_file_direct_write
- Explanation: generic_file_direct_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000409 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_file_fsync
- Explanation: generic_file_fsync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000411 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_file_llseek_size
- Explanation: generic_file_llseek_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000412 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_file_mmap
- Explanation: generic_file_mmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000413 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_file_open
- Explanation: generic_file_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000414 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_file_read_iter
- Explanation: generic_file_read_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000415 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_file_readonly_mmap
- Explanation: generic_file_readonly_mmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000416 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_file_rw_checks
- Explanation: generic_file_rw_checks changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000417 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_file_write_iter
- Explanation: generic_file_write_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000418 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_fill_statx_attr
- Explanation: generic_fill_statx_attr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000419 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_fillattr
- Explanation: generic_fillattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000420 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_perform_write
- Explanation: generic_perform_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000421 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_permission
- Explanation: generic_permission changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000422 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_read_dir
- Explanation: generic_read_dir changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000423 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_remap_file_range_prep
- Explanation: generic_remap_file_range_prep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000424 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_set_encrypted_ci_d_ops
- Explanation: generic_set_encrypted_ci_d_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000425 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_shutdown_super
- Explanation: generic_shutdown_super changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000426 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_update_time
- Explanation: generic_update_time changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000427 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_write_check_limits
- Explanation: generic_write_check_limits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000429 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_write_checks_count
- Explanation: generic_write_checks_count changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000430 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_active_super
- Explanation: get_active_super changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000431 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_anon_bdev
- Explanation: get_anon_bdev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000432 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_compat_sigevent
- Explanation: get_compat_sigevent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000433 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_compat_sigset
- Explanation: get_compat_sigset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000434 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_file_active
- Explanation: get_file_active changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000435 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_file_rcu
- Explanation: get_file_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000436 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_filesystem
- Explanation: get_filesystem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000437 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_fs_type
- Explanation: get_fs_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000439 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_max_files
- Explanation: get_max_files changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000440 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_next_ino
- Explanation: get_next_ino changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000441 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_signal
- Explanation: get_signal changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000442 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_task_cred
- Explanation: get_task_cred changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000443 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_vfs_caps_from_disk
- Explanation: get_vfs_caps_from_disk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000445 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: getname_flags
- Explanation: getname_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000446 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: getname_kernel
- Explanation: getname_kernel changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000447 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: getname_uflags
- Explanation: getname_uflags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000448 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: group_send_sig_info
- Explanation: group_send_sig_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000449 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: groups_alloc
- Explanation: groups_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000450 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: groups_free
- Explanation: groups_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000451 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: groups_search
- Explanation: groups_search changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000452 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: groups_sort
- Explanation: groups_sort changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000453 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: guid_gen
- Explanation: guid_gen changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000454 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: guid_parse
- Explanation: guid_parse changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000456 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: has_capability_noaudit
- Explanation: has_capability_noaudit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000457 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: has_child_subreaper
- Explanation: has_child_subreaper changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000459 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: has_ns_capability_noaudit
- Explanation: has_ns_capability_noaudit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000460 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hashlen_string
- Explanation: hashlen_string changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000461 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hrtimers_cpu_dying
- Explanation: hrtimers_cpu_dying changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000463 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ia32_pick_mmap_layout
- Explanation: ia32_pick_mmap_layout changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000464 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ia32_setup_arg_pages
- Explanation: ia32_setup_arg_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000465 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iget5_locked
- Explanation: iget5_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000466 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iget_failed
- Explanation: iget_failed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000467 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iget_locked
- Explanation: iget_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000468 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ignore_signals
- Explanation: ignore_signals changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000470 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: igrab
- Explanation: igrab changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000471 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ihold
- Explanation: ihold changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000474 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ilookup5_nowait
- Explanation: ilookup5_nowait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000475 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: import_iovec
- Explanation: import_iovec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000476 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: import_single_range
- Explanation: import_single_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000477 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: import_ubuf
- Explanation: import_ubuf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000478 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: in_egroup_p
- Explanation: in_egroup_p changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000479 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: in_eventfd
- Explanation: in_eventfd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(39usize, 1u8) as u32) } } #[inline] pub fn set_in_eventfd(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(40usize, 1u8) as u32) } } #[inline] pub fn set_in_eventfd(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000480 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: in_execve
- Explanation: in_execve changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(33usize, 1u8) as u32) } } #[inline] pub fn set_in_execve(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(34usize, 1u8) as u32) } } #[inline] pub fn set_in_execve(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000481 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: in_group_p
- Explanation: in_group_p changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000482 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: in_iowait
- Explanation: in_iowait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(34usize, 1u8) as u32) } } #[inline] pub fn set_in_iowait(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(35usize, 1u8) as u32) } } #[inline] pub fn set_in_iowait(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000483 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: in_thrashing
- Explanation: in_thrashing changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(41usize, 1u8) as u32) } } #[inline] pub fn set_in_thrashing(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(42usize, 1u8) as u32) } } #[inline] pub fn set_in_thrashing(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000484 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inc_nlink
- Explanation: inc_nlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000485 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: init_extra_mapping_uc
- Explanation: init_extra_mapping_uc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000486 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: init_extra_mapping_wb
- Explanation: init_extra_mapping_wb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000487 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: init_idle
- Explanation: init_idle changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000488 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: init_mem_mapping
- Explanation: init_mem_mapping changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000489 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: init_memory_mapping
- Explanation: init_memory_mapping changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000490 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: init_special_inode
- Explanation: init_special_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000491 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: init_wait_var_entry
- Explanation: init_wait_var_entry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000493 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_add_bytes
- Explanation: inode_add_bytes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000494 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_add_lru
- Explanation: inode_add_lru changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000495 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_dio_wait
- Explanation: inode_dio_wait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000496 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_get_bytes
- Explanation: inode_get_bytes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000498 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_init_always
- Explanation: inode_init_always changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000499 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_init_early
- Explanation: inode_init_early changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000500 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_init_once
- Explanation: inode_init_once changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000501 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_init_owner
- Explanation: inode_init_owner changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000502 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_insert5
- Explanation: inode_insert5 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000503 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_needs_sync
- Explanation: inode_needs_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000504 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_newsize_ok
- Explanation: inode_newsize_ok changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000505 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_nohighmem
- Explanation: inode_nohighmem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000506 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_owner_or_capable
- Explanation: inode_owner_or_capable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000507 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_permission
- Explanation: inode_permission changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000508 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_sb_list_add
- Explanation: inode_sb_list_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000509 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_set_bytes
- Explanation: inode_set_bytes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000510 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_set_ctime_current
- Explanation: inode_set_ctime_current changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000511 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_set_flags
- Explanation: inode_set_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000512 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_sub_bytes
- Explanation: inode_sub_bytes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000514 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_update_timestamps
- Explanation: inode_update_timestamps changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000516 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: insert_inode_locked4
- Explanation: insert_inode_locked4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000517 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: install_thread_keyring_to_cred
- Explanation: install_thread_keyring_to_cred changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000518 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: interval_tree_insert
- Explanation: interval_tree_insert changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000519 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: interval_tree_iter_first
- Explanation: interval_tree_iter_first changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000520 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: interval_tree_iter_next
- Explanation: interval_tree_iter_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000521 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: interval_tree_remove
- Explanation: interval_tree_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000522 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: interval_tree_span_iter_advance
- Explanation: interval_tree_span_iter_advance changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000523 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: interval_tree_span_iter_first
- Explanation: interval_tree_span_iter_first changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000524 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: interval_tree_span_iter_next
- Explanation: interval_tree_span_iter_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000525 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: io_thread
- Explanation: io_thread changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000526 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ioprio_check_cap
- Explanation: ioprio_check_cap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000527 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iov_iter_advance
- Explanation: iov_iter_advance changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000528 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iov_iter_alignment
- Explanation: iov_iter_alignment changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000529 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iov_iter_bvec
- Explanation: iov_iter_bvec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000530 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iov_iter_discard
- Explanation: iov_iter_discard changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000531 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iov_iter_extract_pages
- Explanation: iov_iter_extract_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000532 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iov_iter_gap_alignment
- Explanation: iov_iter_gap_alignment changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000533 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iov_iter_get_pages2
- Explanation: iov_iter_get_pages2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000534 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iov_iter_get_pages_alloc2
- Explanation: iov_iter_get_pages_alloc2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000535 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iov_iter_init
- Explanation: iov_iter_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000536 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iov_iter_is_aligned
- Explanation: iov_iter_is_aligned changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000537 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iov_iter_kvec
- Explanation: iov_iter_kvec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000538 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iov_iter_npages
- Explanation: iov_iter_npages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000539 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iov_iter_restore
- Explanation: iov_iter_restore changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000540 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iov_iter_revert
- Explanation: iov_iter_revert changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000541 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iov_iter_single_seg_count
- Explanation: iov_iter_single_seg_count changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000542 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iov_iter_xarray
- Explanation: iov_iter_xarray changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000543 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iov_iter_zero
- Explanation: iov_iter_zero changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000544 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iovec_from_user
- Explanation: iovec_from_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000545 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iput
- Explanation: iput changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000546 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_fpu_usable
- Explanation: irq_fpu_usable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000547 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_bad_inode
- Explanation: is_bad_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000548 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_child_subreaper
- Explanation: is_child_subreaper changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000549 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_empty_dir_inode
- Explanation: is_empty_dir_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000550 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_subdir
- Explanation: is_subdir changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000551 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iter_file_splice_write
- Explanation: iter_file_splice_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000552 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iterate_dir
- Explanation: iterate_dir changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000553 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iterate_mounts
- Explanation: iterate_mounts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000555 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iterate_supers_type
- Explanation: iterate_supers_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000556 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iunique
- Explanation: iunique changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000557 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kcompat_sys_fstatfs64
- Explanation: kcompat_sys_fstatfs64 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000558 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kcompat_sys_statfs64
- Explanation: kcompat_sys_statfs64 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000559 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kern_mount
- Explanation: kern_mount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000561 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kern_unmount_array
- Explanation: kern_unmount_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000563 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_file_open
- Explanation: kernel_file_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000564 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_fpu_begin_mask
- Explanation: kernel_fpu_begin_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000565 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_fpu_end
- Explanation: kernel_fpu_end changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000566 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_read
- Explanation: kernel_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000567 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_sigaction
- Explanation: kernel_sigaction changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000568 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_thread
- Explanation: kernel_thread changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000569 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_tmpfile_open
- Explanation: kernel_tmpfile_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000571 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_wait4
- Explanation: kernel_wait4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000572 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_write
- Explanation: kernel_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000575 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: key_create_or_update
- Explanation: key_create_or_update changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000576 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: key_free_user_ns
- Explanation: key_free_user_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000577 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: key_fsgid_changed
- Explanation: key_fsgid_changed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000578 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: key_fsuid_changed
- Explanation: key_fsuid_changed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000579 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: key_init
- Explanation: key_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000580 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: key_invalidate
- Explanation: key_invalidate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000581 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: key_link
- Explanation: key_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000583 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: key_move
- Explanation: key_move changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000585 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: key_put_tag
- Explanation: key_put_tag changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000586 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: key_remove_domain
- Explanation: key_remove_domain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000587 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: key_revoke
- Explanation: key_revoke changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000588 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: key_set_timeout
- Explanation: key_set_timeout changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000589 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: key_unlink
- Explanation: key_unlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000590 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: key_update
- Explanation: key_update changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000591 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: key_validate
- Explanation: key_validate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000592 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: keyring_add_key
- Explanation: keyring_add_key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000593 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: keyring_alloc
- Explanation: keyring_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000594 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: keyring_clear
- Explanation: keyring_clear changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000595 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: keyring_restrict
- Explanation: keyring_restrict changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000596 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: keyring_search
- Explanation: keyring_search changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000597 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kfree_link
- Explanation: kfree_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000598 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kill_anon_super
- Explanation: kill_anon_super changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000599 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kill_block_super
- Explanation: kill_block_super changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000600 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kill_fasync
- Explanation: kill_fasync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000601 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kill_litter_super
- Explanation: kill_litter_super changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000602 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kill_pgrp
- Explanation: kill_pgrp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000604 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kill_pid_info
- Explanation: kill_pid_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000605 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kill_pid_usb_asyncio
- Explanation: kill_pid_usb_asyncio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000606 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kiocb_modified
- Explanation: kiocb_modified changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000607 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmem_dump_obj
- Explanation: kmem_dump_obj changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'object', 'type': '*mut core::ffi::c_void'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'object', 'type': '*mut core::ffi::c_void'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000609 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread
- Explanation: kthread changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000610 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_init_test
- Explanation: kunit_init_test changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'test', 'type': '*mut kunit'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'log', 'type': '*mut core::ffi::c_char'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'test', 'type': '*mut kunit'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'log', 'type': '*mut string_stream'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000611 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_log_append
- Explanation: kunit_log_append changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'log', 'type': '*mut core::ffi::c_char'}, {'name': 'fmt', 'type': '*const core::ffi::c_char'}, {'name': '', 'type': '...'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'log', 'type': '*mut string_stream'}, {'name': 'fmt', 'type': '*const core::ffi::c_char'}, {'name': '', 'type': '...'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000612 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: list_bdev_fs_names
- Explanation: list_bdev_fs_names changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000613 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: list_lru_add
- Explanation: list_lru_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000614 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: list_lru_count_node
- Explanation: list_lru_count_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000615 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: list_lru_count_one
- Explanation: list_lru_count_one changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000616 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: list_lru_del
- Explanation: list_lru_del changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000617 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: list_lru_destroy
- Explanation: list_lru_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000619 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: list_lru_isolate_move
- Explanation: list_lru_isolate_move changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000620 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: list_lru_walk_node
- Explanation: list_lru_walk_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000622 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: list_lru_walk_one_irq
- Explanation: list_lru_walk_one_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000623 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: llist_del_first_this
- Explanation: llist_del_first_this changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000624 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lock_two_nondirectories
- Explanation: lock_two_nondirectories changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000625 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lockdep_tasklist_lock_is_held
- Explanation: lockdep_tasklist_lock_is_held changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000627 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lockref_get_not_dead
- Explanation: lockref_get_not_dead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000628 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lockref_get_not_zero
- Explanation: lockref_get_not_zero changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000629 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lockref_mark_dead
- Explanation: lockref_mark_dead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000630 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lockref_put_not_zero
- Explanation: lockref_put_not_zero changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000631 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lockref_put_or_lock
- Explanation: lockref_put_or_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000632 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lockref_put_return
- Explanation: lockref_put_return changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000633 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lookup_user_key
- Explanation: lookup_user_key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000634 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: make_bad_inode
- Explanation: make_bad_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000635 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: make_empty_dir_inode
- Explanation: make_empty_dir_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000636 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: make_task_dead
- Explanation: make_task_dead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000637 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: make_vfsgid
- Explanation: make_vfsgid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000638 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: make_vfsuid
- Explanation: make_vfsuid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000639 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mark_info_dirty
- Explanation: mark_info_dirty changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000640 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mark_mounts_for_expiry
- Explanation: mark_mounts_for_expiry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000641 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: may_open_dev
- Explanation: may_open_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000642 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: may_setattr
- Explanation: may_setattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000643 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: may_setgroups
- Explanation: may_setgroups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000645 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: may_umount_tree
- Explanation: may_umount_tree changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000646 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: memblock_find_dma_reserve
- Explanation: memblock_find_dma_reserve changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000647 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: memcg_list_lru_alloc
- Explanation: memcg_list_lru_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000648 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: memcg_reparent_list_lrus
- Explanation: memcg_reparent_list_lrus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000649 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mm_cache_init
- Explanation: mm_cache_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000651 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmu_interval_notifier_insert_locked
- Explanation: mmu_interval_notifier_insert_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000652 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmu_interval_notifier_remove
- Explanation: mmu_interval_notifier_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000653 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmu_interval_read_begin
- Explanation: mmu_interval_read_begin changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000654 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmu_notifier_get_locked
- Explanation: mmu_notifier_get_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000655 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmu_notifier_put
- Explanation: mmu_notifier_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000656 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmu_notifier_range_update_to_read_only
- Explanation: mmu_notifier_range_update_to_read_only changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000657 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmu_notifier_register
- Explanation: mmu_notifier_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000658 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmu_notifier_synchronize
- Explanation: mmu_notifier_synchronize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000659 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmu_notifier_unregister
- Explanation: mmu_notifier_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000660 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mnt_clone_internal
- Explanation: mnt_clone_internal changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000662 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mnt_drop_write_file
- Explanation: mnt_drop_write_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000663 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mnt_get_write_access
- Explanation: mnt_get_write_access changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000664 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mnt_idmap_get
- Explanation: mnt_idmap_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000665 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mnt_idmap_put
- Explanation: mnt_idmap_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000666 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mnt_make_shortterm
- Explanation: mnt_make_shortterm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000667 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mnt_may_suid
- Explanation: mnt_may_suid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000668 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mnt_put_write_access
- Explanation: mnt_put_write_access changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000669 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mnt_set_expiry
- Explanation: mnt_set_expiry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000671 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mnt_want_write_file
- Explanation: mnt_want_write_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000672 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mntget
- Explanation: mntget changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000673 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mntput
- Explanation: mntput changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000674 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mode_strip_sgid
- Explanation: mode_strip_sgid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000675 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mount_bdev
- Explanation: mount_bdev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000676 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mount_nodev
- Explanation: mount_nodev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000677 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mount_single
- Explanation: mount_single changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000678 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mount_subtree
- Explanation: mount_subtree changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000679 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: move_addr_to_kernel
- Explanation: move_addr_to_kernel changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000680 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: msg_control_is_user
- Explanation: msg_control_is_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000681 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: msg_get_inq
- Explanation: msg_get_inq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000682 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: native_set_fixmap
- Explanation: native_set_fixmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000683 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_bitfield_1
- Explanation: new_bitfield_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'force_atomic', 'type': 'bool_'}, {'name': 'allow_reinit', 'type': 'bool_'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`
- New: `{'params': [{'name': 'lineno', 'type': 'core::ffi::c_uint'}, {'name': 'class_id', 'type': 'core::ffi::c_uint'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`

### Rust Evidence

- Graph edges: `1`

## W-000685 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_inode_pseudo
- Explanation: new_inode_pseudo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000686 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: next_signal
- Explanation: next_signal changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000687 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_cgroup_migration
- Explanation: no_cgroup_migration changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(36usize, 1u8) as u32) } } #[inline] pub fn set_no_cgroup_migration(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(37usize, 1u8) as u32) } } #[inline] pub fn set_no_cgroup_migration(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000688 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_files
- Explanation: no_files changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000690 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_seek_end_llseek_size
- Explanation: no_seek_end_llseek_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000691 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: nonseekable_open
- Explanation: nonseekable_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000692 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: noop_direct_IO
- Explanation: noop_direct_IO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000693 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: noop_fsync
- Explanation: noop_fsync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000694 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: noop_llseek
- Explanation: noop_llseek changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000695 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: normalize_rt_tasks
- Explanation: normalize_rt_tasks changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000696 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: notify_change
- Explanation: notify_change changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000698 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ns_capable_noaudit
- Explanation: ns_capable_noaudit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000699 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ns_capable_setid
- Explanation: ns_capable_setid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000701 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: numa_nearest_node
- Explanation: numa_nearest_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000702 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: open_exec
- Explanation: open_exec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000703 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: our_mnt
- Explanation: our_mnt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000705 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: out_of_line_wait_on_bit_lock
- Explanation: out_of_line_wait_on_bit_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000706 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: out_of_line_wait_on_bit_timeout
- Explanation: out_of_line_wait_on_bit_timeout changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000707 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: override_creds
- Explanation: override_creds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000708 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: page_get_link
- Explanation: page_get_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000709 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: page_put_link
- Explanation: page_put_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000710 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: page_readlink
- Explanation: page_readlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000711 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: page_symlink
- Explanation: page_symlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000712 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: paging_init
- Explanation: paging_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000713 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: path_get
- Explanation: path_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000714 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: path_has_submounts
- Explanation: path_has_submounts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000715 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: path_is_mountpoint
- Explanation: path_is_mountpoint changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000716 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: path_is_under
- Explanation: path_is_under changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000717 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: path_noexec
- Explanation: path_noexec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000718 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: path_put
- Explanation: path_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000719 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcpu_alloc_size
- Explanation: pcpu_alloc_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000720 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: percpu_down_write
- Explanation: percpu_down_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000721 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: percpu_free_rwsem
- Explanation: percpu_free_rwsem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000722 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: percpu_is_read_locked
- Explanation: percpu_is_read_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000723 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: percpu_up_write
- Explanation: percpu_up_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000724 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pfn_modify_allowed
- Explanation: pfn_modify_allowed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000725 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pgd_page_get_mm
- Explanation: pgd_page_get_mm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000726 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pmd_mkwrite
- Explanation: pmd_mkwrite changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000727 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pmdp_clear_flush_young
- Explanation: pmdp_clear_flush_young changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000728 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pmdp_invalidate_ad
- Explanation: pmdp_invalidate_ad changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000729 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pmdp_set_access_flags
- Explanation: pmdp_set_access_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000730 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pmdp_test_and_clear_young
- Explanation: pmdp_test_and_clear_young changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000731 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: populate_extra_pmd
- Explanation: populate_extra_pmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000732 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: populate_extra_pte
- Explanation: populate_extra_pte changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000733 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: prepare_creds
- Explanation: prepare_creds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000734 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: prepare_exec_creds
- Explanation: prepare_exec_creds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000735 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: prepare_kernel_cred
- Explanation: prepare_kernel_cred changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000736 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: privileged_wrt_inode_uidgid
- Explanation: privileged_wrt_inode_uidgid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000737 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_caches_init
- Explanation: proc_caches_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000739 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ptdump_walk_pgd_level_checkwx
- Explanation: ptdump_walk_pgd_level_checkwx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000740 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ptdump_walk_pgd_level_debugfs
- Explanation: ptdump_walk_pgd_level_debugfs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000741 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ptdump_walk_user_pgd_level_checkwx
- Explanation: ptdump_walk_user_pgd_level_checkwx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000742 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pte_mkwrite
- Explanation: pte_mkwrite changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000743 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ptep_clear_flush_young
- Explanation: ptep_clear_flush_young changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000744 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ptep_set_access_flags
- Explanation: ptep_set_access_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000745 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ptep_test_and_clear_young
- Explanation: ptep_test_and_clear_young changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000746 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pti_check_boottime_disable
- Explanation: pti_check_boottime_disable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000747 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pti_finalize
- Explanation: pti_finalize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000748 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pti_init
- Explanation: pti_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000749 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ptracer_capable
- Explanation: ptracer_capable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000750 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pudp_set_access_flags
- Explanation: pudp_set_access_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000751 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pudp_test_and_clear_young
- Explanation: pudp_test_and_clear_young changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000754 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: put_cmsg_scm_timestamping64
- Explanation: put_cmsg_scm_timestamping64 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000755 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: put_compat_rusage
- Explanation: put_compat_rusage changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000756 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: put_filesystem
- Explanation: put_filesystem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000757 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: put_io_context
- Explanation: put_io_context changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000758 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: put_task_stack
- Explanation: put_task_stack changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000759 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: put_task_struct_rcu_user
- Explanation: put_task_struct_rcu_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000760 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: putname
- Explanation: putname changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000761 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: qid_eq
- Explanation: qid_eq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000762 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: qid_lt
- Explanation: qid_lt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000763 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: qid_valid
- Explanation: qid_valid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000764 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: qtree_delete_dquot
- Explanation: qtree_delete_dquot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000765 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: qtree_entry_unused
- Explanation: qtree_entry_unused changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000766 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: qtree_get_next_id
- Explanation: qtree_get_next_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000767 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: qtree_read_dquot
- Explanation: qtree_read_dquot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000768 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: qtree_release_dquot
- Explanation: qtree_release_dquot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000769 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: qtree_write_dquot
- Explanation: qtree_write_dquot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000770 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: quota_send_warning
- Explanation: quota_send_warning changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000774 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rcu_sync_dtor
- Explanation: rcu_sync_dtor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000776 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rcu_sync_enter_start
- Explanation: rcu_sync_enter_start changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000777 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rcu_sync_exit
- Explanation: rcu_sync_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000778 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rcu_sync_init
- Explanation: rcu_sync_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000779 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rcutree_report_cpu_dead
- Explanation: rcutree_report_cpu_dead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000780 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rcutree_report_cpu_starting
- Explanation: rcutree_report_cpu_starting changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000781 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rcuwait_wake_up
- Explanation: rcuwait_wake_up changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000782 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: readlink_copy
- Explanation: readlink_copy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000784 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: recalc_sigpending_and_wake
- Explanation: recalc_sigpending_and_wake changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000785 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: recvmsg_copy_msghdr
- Explanation: recvmsg_copy_msghdr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000786 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: register_chrdev_region
- Explanation: register_chrdev_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000787 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: register_filesystem
- Explanation: register_filesystem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000788 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: register_quota_format
- Explanation: register_quota_format changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000789 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: release_dentry_name_snapshot
- Explanation: release_dentry_name_snapshot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000790 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: release_task
- Explanation: release_task changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000791 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: release_thread
- Explanation: release_thread changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000792 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: render_sigset_t
- Explanation: render_sigset_t changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000793 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rep_movs_alternative
- Explanation: rep_movs_alternative changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000794 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rep_stos_alternative
- Explanation: rep_stos_alternative changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000795 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: reported_split_lock
- Explanation: reported_split_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(40usize, 1u8) as u32) } } #[inline] pub fn set_reported_split_lock(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(41usize, 1u8) as u32) } } #[inline] pub fn set_reported_split_lock(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000796 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: request_key_rcu
- Explanation: request_key_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000797 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: request_key_tag
- Explanation: request_key_tag changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000798 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: request_key_with_auxdata
- Explanation: request_key_with_auxdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000799 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: reserve_top_address
- Explanation: reserve_top_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000800 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: restore_altstack
- Explanation: restore_altstack changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000801 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: restore_sigmask
- Explanation: restore_sigmask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(35usize, 1u8) as u32) } } #[inline] pub fn set_restore_sigmask(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(36usize, 1u8) as u32) } } #[inline] pub fn set_restore_sigmask(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000802 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: restrict_link_reject
- Explanation: restrict_link_reject changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000804 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: retire_super
- Explanation: retire_super changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000805 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: revert_creds
- Explanation: revert_creds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000806 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rt_mutex_adjust_pi
- Explanation: rt_mutex_adjust_pi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000807 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rt_mutex_post_schedule
- Explanation: rt_mutex_post_schedule changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000808 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rt_mutex_pre_schedule
- Explanation: rt_mutex_pre_schedule changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000809 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rt_mutex_schedule
- Explanation: rt_mutex_schedule changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000810 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rt_mutex_setprio
- Explanation: rt_mutex_setprio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000811 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rw_verify_area
- Explanation: rw_verify_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000812 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sb_min_blocksize
- Explanation: sb_min_blocksize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000813 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sb_set_blocksize
- Explanation: sb_set_blocksize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000814 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sched_cgroup_fork
- Explanation: sched_cgroup_fork changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000816 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sched_exec
- Explanation: sched_exec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000817 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sched_fork
- Explanation: sched_fork changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000818 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sched_post_fork
- Explanation: sched_post_fork changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000819 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sched_rt_mutex
- Explanation: sched_rt_mutex changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000820 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: schedule_tail
- Explanation: schedule_tail changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000823 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: send_sig_fault_trapno
- Explanation: send_sig_fault_trapno changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000824 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: send_sig_info
- Explanation: send_sig_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000825 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: send_sig_mceerr
- Explanation: send_sig_mceerr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000826 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: send_sig_perf
- Explanation: send_sig_perf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000827 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: send_sigio
- Explanation: send_sigio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000828 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: send_signal_locked
- Explanation: send_signal_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000829 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: send_sigqueue
- Explanation: send_sigqueue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000830 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: send_sigurg
- Explanation: send_sigurg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000831 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sendmsg_copy_msghdr
- Explanation: sendmsg_copy_msghdr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000833 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_anon_super_fc
- Explanation: set_anon_super_fc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000834 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_compat_user_sigmask
- Explanation: set_compat_user_sigmask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000835 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_create_files_as
- Explanation: set_create_files_as changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000836 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_cred_ucounts
- Explanation: set_cred_ucounts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000837 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_current_blocked
- Explanation: set_current_blocked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000838 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_current_groups
- Explanation: set_current_groups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000839 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_groups
- Explanation: set_groups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000840 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_nlink
- Explanation: set_nlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000841 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_pte_vaddr_p4d
- Explanation: set_pte_vaddr_p4d changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000842 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_pte_vaddr_pud
- Explanation: set_pte_vaddr_pud changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000844 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_security_override_from_ctx
- Explanation: set_security_override_from_ctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000845 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_task_ioprio
- Explanation: set_task_ioprio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000846 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_task_stack_end_magic
- Explanation: set_task_stack_end_magic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000847 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_user_sigmask
- Explanation: set_user_sigmask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000848 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: setattr_copy
- Explanation: setattr_copy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000849 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: setattr_prepare
- Explanation: setattr_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000850 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: setattr_should_drop_sgid
- Explanation: setattr_should_drop_sgid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000851 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: setattr_should_drop_suidgid
- Explanation: setattr_should_drop_suidgid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000852 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: setup_pcp_cacheinfo
- Explanation: setup_pcp_cacheinfo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000854 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sget_dev
- Explanation: sget_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000855 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sget_fc
- Explanation: sget_fc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000856 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: shrink_dcache_for_umount
- Explanation: shrink_dcache_for_umount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000857 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: shrink_dcache_parent
- Explanation: shrink_dcache_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000858 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: shrink_dcache_sb
- Explanation: shrink_dcache_sb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000859 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: shrinker_alloc
- Explanation: shrinker_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000860 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: shrinker_free
- Explanation: shrinker_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000861 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: shrinker_register
- Explanation: shrinker_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000862 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sigaltstack_size_valid
- Explanation: sigaltstack_size_valid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000864 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: signal_setup_done
- Explanation: signal_setup_done changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000865 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: signal_wake_up_state
- Explanation: signal_wake_up_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000866 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: signals_init
- Explanation: signals_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000867 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sigprocmask
- Explanation: sigprocmask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000868 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sigqueue_alloc
- Explanation: sigqueue_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000869 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sigqueue_free
- Explanation: sigqueue_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000870 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_attr_open
- Explanation: simple_attr_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000871 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_attr_read
- Explanation: simple_attr_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000872 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_attr_release
- Explanation: simple_attr_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000874 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_attr_write_signed
- Explanation: simple_attr_write_signed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000875 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_empty
- Explanation: simple_empty changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000876 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_fill_super
- Explanation: simple_fill_super changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000877 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_get_link
- Explanation: simple_get_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000878 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_getattr
- Explanation: simple_getattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000879 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_inode_init_ts
- Explanation: simple_inode_init_ts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000880 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_link
- Explanation: simple_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000881 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_lookup
- Explanation: simple_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000882 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_nosetlease
- Explanation: simple_nosetlease changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000883 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_offset_add
- Explanation: simple_offset_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000884 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_offset_destroy
- Explanation: simple_offset_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000885 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_offset_init
- Explanation: simple_offset_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000886 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_offset_remove
- Explanation: simple_offset_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000887 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_offset_rename_exchange
- Explanation: simple_offset_rename_exchange changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000888 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_open
- Explanation: simple_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000889 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_pin_fs
- Explanation: simple_pin_fs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000890 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_read_from_buffer
- Explanation: simple_read_from_buffer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000891 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_recursive_removal
- Explanation: simple_recursive_removal changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000892 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_release_fs
- Explanation: simple_release_fs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000894 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_rename_exchange
- Explanation: simple_rename_exchange changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000895 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_rename_timestamp
- Explanation: simple_rename_timestamp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000896 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_rmdir
- Explanation: simple_rmdir changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000897 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_setattr
- Explanation: simple_setattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000898 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_statfs
- Explanation: simple_statfs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000899 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_transaction_get
- Explanation: simple_transaction_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000900 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_transaction_read
- Explanation: simple_transaction_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000901 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_transaction_release
- Explanation: simple_transaction_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000902 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_transaction_set
- Explanation: simple_transaction_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000903 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_unlink
- Explanation: simple_unlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000904 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_write_begin
- Explanation: simple_write_begin changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000905 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_write_to_buffer
- Explanation: simple_write_to_buffer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000906 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: smp_call_function_single_async
- Explanation: smp_call_function_single_async changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'cpu', 'type': 'core::ffi::c_int'}, {'name': 'csd', 'type': '*mut __call_single_data'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'cpu', 'type': 'core::ffi::c_int'}, {'name': 'csd', 'type': '*mut call_single_data_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000907 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: socket_seq_show
- Explanation: socket_seq_show changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000910 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stream_open
- Explanation: stream_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000911 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: strncpy_from_kernel_nofault
- Explanation: strncpy_from_kernel_nofault changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000913 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: strncpy_from_user_nofault
- Explanation: strncpy_from_user_nofault changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000915 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: strnlen_user_nofault
- Explanation: strnlen_user_nofault changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000917 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: super_setup_bdi_name
- Explanation: super_setup_bdi_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000918 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: switch_fpu_return
- Explanation: switch_fpu_return changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000920 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sync_filesystem
- Explanation: sync_filesystem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000921 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sync_inode_metadata
- Explanation: sync_inode_metadata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000922 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysctl_is_alias
- Explanation: sysctl_is_alias changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000923 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: take_dentry_name_snapshot
- Explanation: take_dentry_name_snapshot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000924 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: task_clear_jobctl_pending
- Explanation: task_clear_jobctl_pending changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000925 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: task_clear_jobctl_trapping
- Explanation: task_clear_jobctl_trapping changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000926 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: task_join_group_stop
- Explanation: task_join_group_stop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000927 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: task_set_jobctl_pending
- Explanation: task_set_jobctl_pending changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000928 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: thaw_super
- Explanation: thaw_super changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000929 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: thread_group_exited
- Explanation: thread_group_exited changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000930 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: thread_stack_cache_init
- Explanation: thread_stack_cache_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000931 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: timestamp_truncate
- Explanation: timestamp_truncate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000932 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: touch_atime
- Explanation: touch_atime changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000933 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: uids_sysfs_init
- Explanation: uids_sysfs_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000934 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unhandled_signal
- Explanation: unhandled_signal changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000935 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unlock_new_inode
- Explanation: unlock_new_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000936 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unlock_two_nondirectories
- Explanation: unlock_two_nondirectories changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000937 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unregister_chrdev_region
- Explanation: unregister_chrdev_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000938 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unregister_filesystem
- Explanation: unregister_filesystem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000939 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unregister_quota_format
- Explanation: unregister_quota_format changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000941 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: use_memdelay
- Explanation: use_memdelay changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(38usize, 1u8) as u32) } } #[inline] pub fn set_use_memdelay(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(39usize, 1u8) as u32) } } #[inline] pub fn set_use_memdelay(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000942 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: user_mode_thread
- Explanation: user_mode_thread changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000943 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: user_statfs
- Explanation: user_statfs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000944 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: user_worker
- Explanation: user_worker changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000945 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: uuid_gen
- Explanation: uuid_gen changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000946 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: uuid_is_valid
- Explanation: uuid_is_valid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000947 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: uuid_parse
- Explanation: uuid_parse changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000949 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_caches_init_early
- Explanation: vfs_caches_init_early changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000950 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_clone_file_range
- Explanation: vfs_clone_file_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000951 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_copy_file_range
- Explanation: vfs_copy_file_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000953 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_create_mount
- Explanation: vfs_create_mount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000955 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_dedupe_file_range_one
- Explanation: vfs_dedupe_file_range_one changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000956 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_fadvise
- Explanation: vfs_fadvise changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000957 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_fallocate
- Explanation: vfs_fallocate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000958 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_fchmod
- Explanation: vfs_fchmod changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000959 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_fchown
- Explanation: vfs_fchown changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000961 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_fstatat
- Explanation: vfs_fstatat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000963 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_fsync_range
- Explanation: vfs_fsync_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000964 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_get_link
- Explanation: vfs_get_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000966 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_getattr_nosec
- Explanation: vfs_getattr_nosec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000967 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_iocb_iter_read
- Explanation: vfs_iocb_iter_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000968 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_iocb_iter_write
- Explanation: vfs_iocb_iter_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000969 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_ioctl
- Explanation: vfs_ioctl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000970 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_iter_read
- Explanation: vfs_iter_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000971 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_iter_write
- Explanation: vfs_iter_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000972 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_kern_mount
- Explanation: vfs_kern_mount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000973 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_link
- Explanation: vfs_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000974 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_llseek
- Explanation: vfs_llseek changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000975 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_mkdir
- Explanation: vfs_mkdir changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000976 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_mknod
- Explanation: vfs_mknod changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000977 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_mkobj
- Explanation: vfs_mkobj changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000979 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_readlink
- Explanation: vfs_readlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000980 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_rename
- Explanation: vfs_rename changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000981 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_rmdir
- Explanation: vfs_rmdir changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000982 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_setpos
- Explanation: vfs_setpos changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000983 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_statfs
- Explanation: vfs_statfs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000984 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_submount
- Explanation: vfs_submount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000985 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_symlink
- Explanation: vfs_symlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000986 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_truncate
- Explanation: vfs_truncate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000987 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_unlink
- Explanation: vfs_unlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000988 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_utimes
- Explanation: vfs_utimes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000989 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_write
- Explanation: vfs_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000990 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfsgid_in_group_p
- Explanation: vfsgid_in_group_p changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000991 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wait_bit_init
- Explanation: wait_bit_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000992 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wait_for_key_construction
- Explanation: wait_for_key_construction changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000993 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wake_bit_function
- Explanation: wake_bit_function changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000994 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wake_up_bit
- Explanation: wake_up_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000995 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wake_up_var
- Explanation: wake_up_var changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000996 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: walk_process_tree
- Explanation: walk_process_tree changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000998 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: work_on_cpu_key
- Explanation: work_on_cpu_key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000999 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: work_on_cpu_safe
- Explanation: work_on_cpu_safe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-001000 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: work_on_cpu_safe_key
- Explanation: work_on_cpu_safe_key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001001 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wrap_directory_iterator
- Explanation: wrap_directory_iterator changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001002 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xstate_get_guest_group_perm
- Explanation: xstate_get_guest_group_perm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001003 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: zap_other_threads
- Explanation: zap_other_threads changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001136 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmem_dump_obj
- Explanation: kmem_dump_obj changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['void *object'], 'return_type': 'void'}`
- New: `{'params': ['void *object'], 'return_type': 'static inline bool'}`

### Rust Evidence

- Graph edges: `1`

## W-001137 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_init_test
- Explanation: kunit_init_test changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct kunit *test', 'const char *name', 'char *log'], 'return_type': 'void'}`
- New: `{'params': ['struct kunit *test', 'const char *name', 'struct string_stream *log'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-001031 FieldDrift

- Risk: High
- Score: 10.4
- Symbol: task_struct
- Explanation: task_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'core::ffi::c_uint'}, {'name': 'stack', 'type': '*mut core::ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'ptrace', 'type': 'core::ffi::c_uint'}, {'name': 'on_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'core::ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'core::ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_cpu', 'type': 'core::ffi::c_int'}, {'name': 'on_rq', 'type': 'core::ffi::c_int'}, {'name': 'prio', 'type': 'core::ffi::c_int'}, {'name': 'static_prio', 'type': 'core::ffi::c_int'}, {'name': 'normal_prio', 'type': 'core::ffi::c_int'}, {'name': 'rt_priority', 'type': 'core::ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': '__bindgen_padding_1', 'type': '[u64; 4usize]'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'core::ffi::c_uint'}, {'name': 'policy', 'type': 'core::ffi::c_uint'}, {'name': 'nr_cpus_allowed', 'type': 'core::ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut core::ffi::c_void'}, {'name': 'migration_disabled', 'type': 'core::ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'core::ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'core::ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'core::ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'exit_state', 'type': 'core::ffi::c_int'}, {'name': 'exit_code', 'type': 'core::ffi::c_int'}, {'name': 'exit_signal', 'type': 'core::ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'core::ffi::c_int'}, {'name': 'jobctl', 'type': 'core::ffi::c_ulong'}, {'name': 'personality', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'core::ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_group', 'type': 'list_head'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'worker_private', 'type': '*mut core::ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[core::ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'core::ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'core::ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'core::ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'journal_info', 'type': '*mut core::ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'core::ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cpuset_slab_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'core::ffi::c_uint'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'core::ffi::c_short'}, {'name': 'pref_node_fork', 'type': 'core::ffi::c_short'}, {'name': 'rseq', 'type': '*mut rseq'}, {'name': 'rseq_len', 'type': 'u32_'}, {'name': 'rseq_sig', 'type': 'u32_'}, {'name': 'rseq_event_mask', 'type': 'core::ffi::c_ulong'}, {'name': 'mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'last_mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'migrate_from_cpu', 'type': 'core::ffi::c_int'}, {'name': 'mm_cid_active', 'type': 'core::ffi::c_int'}, {'name': 'cid_work', 'type': 'callback_head'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'core::ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'core::ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'core::ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'core::ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'core::ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_vaddr', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'core::ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': '__bindgen_padding_2', 'type': 'u64'}, {'name': 'thread', 'type': 'thread_struct'}]`
- New: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'core::ffi::c_uint'}, {'name': 'saved_state', 'type': 'core::ffi::c_uint'}, {'name': 'stack', 'type': '*mut core::ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'ptrace', 'type': 'core::ffi::c_uint'}, {'name': 'on_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'core::ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'core::ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_cpu', 'type': 'core::ffi::c_int'}, {'name': 'on_rq', 'type': 'core::ffi::c_int'}, {'name': 'prio', 'type': 'core::ffi::c_int'}, {'name': 'static_prio', 'type': 'core::ffi::c_int'}, {'name': 'normal_prio', 'type': 'core::ffi::c_int'}, {'name': 'rt_priority', 'type': 'core::ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': '__bindgen_padding_1', 'type': '[u64; 4usize]'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'core::ffi::c_uint'}, {'name': 'policy', 'type': 'core::ffi::c_uint'}, {'name': 'nr_cpus_allowed', 'type': 'core::ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut core::ffi::c_void'}, {'name': 'migration_disabled', 'type': 'core::ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'core::ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'core::ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'core::ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'faults_disabled_mapping', 'type': '*mut address_space'}, {'name': 'exit_state', 'type': 'core::ffi::c_int'}, {'name': 'exit_code', 'type': 'core::ffi::c_int'}, {'name': 'exit_signal', 'type': 'core::ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'core::ffi::c_int'}, {'name': 'jobctl', 'type': 'core::ffi::c_ulong'}, {'name': 'personality', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'core::ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'worker_private', 'type': '*mut core::ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[core::ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'core::ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'core::ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'core::ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'journal_info', 'type': '*mut core::ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'core::ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cpuset_slab_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'core::ffi::c_uint'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'core::ffi::c_short'}, {'name': 'pref_node_fork', 'type': 'core::ffi::c_short'}, {'name': 'rseq', 'type': '*mut rseq'}, {'name': 'rseq_len', 'type': 'u32_'}, {'name': 'rseq_sig', 'type': 'u32_'}, {'name': 'rseq_event_mask', 'type': 'core::ffi::c_ulong'}, {'name': 'mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'last_mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'migrate_from_cpu', 'type': 'core::ffi::c_int'}, {'name': 'mm_cid_active', 'type': 'core::ffi::c_int'}, {'name': 'cid_work', 'type': 'callback_head'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'core::ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'core::ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'core::ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'core::ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'core::ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_vaddr', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'core::ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': '__bindgen_padding_2', 'type': '[u64; 2usize]'}, {'name': 'thread', 'type': 'thread_struct'}]`

### Rust Evidence

- Graph edges: `9`

## W-001010 FieldDrift

- Risk: High
- Score: 10.2
- Symbol: dentry
- Explanation: dentry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'd_flags', 'type': 'core::ffi::c_uint'}, {'name': 'd_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'd_hash', 'type': 'hlist_bl_node'}, {'name': 'd_parent', 'type': '*mut dentry'}, {'name': 'd_name', 'type': 'qstr'}, {'name': 'd_inode', 'type': '*mut inode'}, {'name': 'd_iname', 'type': '[core::ffi::c_uchar; 32usize]'}, {'name': 'd_lockref', 'type': 'lockref'}, {'name': 'd_op', 'type': '*const dentry_operations'}, {'name': 'd_sb', 'type': '*mut super_block'}, {'name': 'd_time', 'type': 'core::ffi::c_ulong'}, {'name': 'd_fsdata', 'type': '*mut core::ffi::c_void'}, {'name': '__bindgen_anon_1', 'type': 'dentry__bindgen_ty_1'}, {'name': 'd_child', 'type': 'list_head'}, {'name': 'd_subdirs', 'type': 'list_head'}, {'name': 'd_u', 'type': 'dentry__bindgen_ty_2'}]`

### Rust Evidence

- Graph edges: `8`

## W-000106 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __wake_up_locked_key_bookmark
- Explanation: __wake_up_locked_key_bookmark changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000112 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __x86_return_skl
- Explanation: __x86_return_skl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000147 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: bitmap_allocate_region
- Explanation: bitmap_allocate_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000148 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: bitmap_find_free_region
- Explanation: bitmap_find_free_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000149 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: bitmap_release_region
- Explanation: bitmap_release_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000288 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: entry_INT80_compat
- Explanation: entry_INT80_compat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000438 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: get_llc_id
- Explanation: get_llc_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000462 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: hrtimers_dead_cpu
- Explanation: hrtimers_dead_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000469 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ignore_sysret
- Explanation: ignore_sysret changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000608 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: kmem_valid_obj
- Explanation: kmem_valid_obj changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000700 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: numa_map_to_online_node
- Explanation: numa_map_to_online_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000771 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: rcu_cpu_starting
- Explanation: rcu_cpu_starting changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000772 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: rcu_eqs_special_set
- Explanation: rcu_eqs_special_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000773 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: rcu_report_dead
- Explanation: rcu_report_dead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000803 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: retbleed_untrain_ret
- Explanation: retbleed_untrain_ret changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000908 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: srso_alias_untrain_ret
- Explanation: srso_alias_untrain_ret changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000909 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: srso_untrain_ret
- Explanation: srso_untrain_ret changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001103 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: accel_debugfs_init
- Explanation: accel_debugfs_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_minor *minor', 'int minor_id'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct drm_device *dev'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-001104 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: acpi_dev_install_notify_handler
- Explanation: acpi_dev_install_notify_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct acpi_device *adev', 'u32 handler_type', 'acpi_notify_handler handler'], 'return_type': 'int'}`
- New: `{'params': ['struct acpi_device *adev', 'u32 handler_type', 'acpi_notify_handler handler', 'void *context'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-001105 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: container_of
- Explanation: container_of changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['res', 'struct ttm_range_mgr_node', 'base'], 'return_type': 'return'}`
- New: `{'params': ['work', 'struct rcu_work', 'work'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001106 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_ahash_export
- Explanation: crypto_ahash_export changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct ahash_request *req', 'void *out'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct ahash_request *req', 'void *out'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-001107 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_ahash_import
- Explanation: crypto_ahash_import changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct ahash_request *req', 'const void *in'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct ahash_request *req', 'const void *in'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-001108 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_ahash_init
- Explanation: crypto_ahash_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct ahash_request *req'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct ahash_request *req'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-001109 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_ahash_update
- Explanation: crypto_ahash_update changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct ahash_request *req'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct ahash_request *req'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-001110 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_engine_exit
- Explanation: crypto_engine_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct crypto_engine *engine'], 'return_type': 'int'}`
- New: `{'params': ['struct crypto_engine *engine'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001111 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_instance_ctx
- Explanation: crypto_instance_ctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['skcipher_crypto_instance(inst)'], 'return_type': 'return'}`
- New: `{'params': ['lskcipher_crypto_instance(inst)'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001112 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_shash_export
- Explanation: crypto_shash_export changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct shash_desc *desc', 'void *out'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct shash_desc *desc', 'void *out'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-001113 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_shash_import
- Explanation: crypto_shash_import changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct shash_desc *desc', 'const void *in'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct shash_desc *desc', 'const void *in'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-001114 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_tfm_alg_alignmask
- Explanation: crypto_tfm_alg_alignmask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['crypto_skcipher_tfm(tfm)'], 'return_type': 'return'}`
- New: `{'params': ['crypto_lskcipher_tfm(tfm)'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001115 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_tfm_alg_blocksize
- Explanation: crypto_tfm_alg_blocksize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['crypto_skcipher_tfm(tfm)'], 'return_type': 'return'}`
- New: `{'params': ['crypto_lskcipher_tfm(tfm)'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001116 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_tfm_alg_driver_name
- Explanation: crypto_tfm_alg_driver_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['crypto_skcipher_tfm(tfm)'], 'return_type': 'return'}`
- New: `{'params': ['crypto_lskcipher_tfm(tfm)'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001117 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_tfm_get_flags
- Explanation: crypto_tfm_get_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['crypto_skcipher_tfm(tfm)'], 'return_type': 'return'}`
- New: `{'params': ['crypto_lskcipher_tfm(tfm)'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001118 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_bridge_debugfs_init
- Explanation: drm_bridge_debugfs_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_minor *minor'], 'return_type': 'void'}`
- New: `{'params': ['struct drm_device *dev'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001119 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_client_debugfs_init
- Explanation: drm_client_debugfs_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_minor *minor'], 'return_type': 'void'}`
- New: `{'params': ['struct drm_device *dev'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001120 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_connector_oob_hotplug_event
- Explanation: drm_connector_oob_hotplug_event changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct fwnode_handle *connector_fwnode'], 'return_type': 'void'}`
- New: `{'params': ['struct fwnode_handle *connector_fwnode', 'enum drm_connector_status status'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001121 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_debugfs_gpuva_info
- Explanation: drm_debugfs_gpuva_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct seq_file *m', 'struct drm_gpuva_manager *mgr'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct seq_file *m', 'struct drm_gpuvm *gpuvm'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `0`

## W-001122 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_debugfs_remove_files
- Explanation: drm_debugfs_remove_files changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct drm_info_list *files', 'int count', 'struct drm_minor *minor'], 'return_type': 'static inline int'}`
- New: `{'params': ['const struct drm_info_list *files', 'int count', 'struct dentry *root', 'struct drm_minor *minor'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `0`

## W-001123 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_dp_downstream_debug
- Explanation: drm_dp_downstream_debug changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct seq_file *m', 'const u8 dpcd[DP_RECEIVER_CAP_SIZE]', 'const u8 port_cap[4]', 'const struct edid *edid', 'struct drm_dp_aux *aux'], 'return_type': 'void'}`
- New: `{'params': ['struct seq_file *m', 'const u8 dpcd[DP_RECEIVER_CAP_SIZE]', 'const u8 port_cap[4]', 'const struct drm_edid *drm_edid', 'struct drm_dp_aux *aux'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001124 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_dp_downstream_is_tmds
- Explanation: drm_dp_downstream_is_tmds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const u8 dpcd[DP_RECEIVER_CAP_SIZE]', 'const u8 port_cap[4]', 'const struct edid *edid'], 'return_type': 'bool'}`
- New: `{'params': ['const u8 dpcd[DP_RECEIVER_CAP_SIZE]', 'const u8 port_cap[4]', 'const struct drm_edid *drm_edid'], 'return_type': 'bool'}`

### Rust Evidence

- Graph edges: `0`

## W-001125 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_dp_downstream_max_bpc
- Explanation: drm_dp_downstream_max_bpc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const u8 dpcd[DP_RECEIVER_CAP_SIZE]', 'const u8 port_cap[4]', 'const struct edid *edid'], 'return_type': 'int'}`
- New: `{'params': ['const u8 dpcd[DP_RECEIVER_CAP_SIZE]', 'const u8 port_cap[4]', 'const struct drm_edid *drm_edid'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-001126 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_dp_downstream_max_tmds_clock
- Explanation: drm_dp_downstream_max_tmds_clock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const u8 dpcd[DP_RECEIVER_CAP_SIZE]', 'const u8 port_cap[4]', 'const struct edid *edid'], 'return_type': 'int'}`
- New: `{'params': ['const u8 dpcd[DP_RECEIVER_CAP_SIZE]', 'const u8 port_cap[4]', 'const struct drm_edid *drm_edid'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-001127 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_dp_downstream_min_tmds_clock
- Explanation: drm_dp_downstream_min_tmds_clock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const u8 dpcd[DP_RECEIVER_CAP_SIZE]', 'const u8 port_cap[4]', 'const struct edid *edid'], 'return_type': 'int'}`
- New: `{'params': ['const u8 dpcd[DP_RECEIVER_CAP_SIZE]', 'const u8 port_cap[4]', 'const struct drm_edid *drm_edid'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-001128 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_gpuva_find
- Explanation: drm_gpuva_find changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_gpuva_manager *mgr', 'u64 addr', 'u64 range'], 'return_type': 'struct drm_gpuva *'}`
- New: `{'params': ['struct drm_gpuvm *gpuvm', 'u64 addr', 'u64 range'], 'return_type': 'struct drm_gpuva *'}`

### Rust Evidence

- Graph edges: `0`

## W-001129 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_gpuva_find_first
- Explanation: drm_gpuva_find_first changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_gpuva_manager *mgr', 'u64 addr', 'u64 range'], 'return_type': 'struct drm_gpuva *'}`
- New: `{'params': ['struct drm_gpuvm *gpuvm', 'u64 addr', 'u64 range'], 'return_type': 'struct drm_gpuva *'}`

### Rust Evidence

- Graph edges: `0`

## W-001130 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_gpuva_find_next
- Explanation: drm_gpuva_find_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_gpuva_manager *mgr', 'u64 end'], 'return_type': 'struct drm_gpuva *'}`
- New: `{'params': ['struct drm_gpuvm *gpuvm', 'u64 end'], 'return_type': 'struct drm_gpuva *'}`

### Rust Evidence

- Graph edges: `0`

## W-001131 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_gpuva_find_prev
- Explanation: drm_gpuva_find_prev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_gpuva_manager *mgr', 'u64 start'], 'return_type': 'struct drm_gpuva *'}`
- New: `{'params': ['struct drm_gpuvm *gpuvm', 'u64 start'], 'return_type': 'struct drm_gpuva *'}`

### Rust Evidence

- Graph edges: `0`

## W-001132 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_gpuva_insert
- Explanation: drm_gpuva_insert changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_gpuva_manager *mgr', 'struct drm_gpuva *va'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_gpuvm *gpuvm', 'struct drm_gpuva *va'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-001133 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_gpuva_map
- Explanation: drm_gpuva_map changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_gpuva_manager *mgr', 'struct drm_gpuva *va', 'struct drm_gpuva_op_map *op'], 'return_type': 'void'}`
- New: `{'params': ['struct drm_gpuvm *gpuvm', 'struct drm_gpuva *va', 'struct drm_gpuva_op_map *op'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001134 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_gpuva_ops_free
- Explanation: drm_gpuva_ops_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_gpuva_manager *mgr', 'struct drm_gpuva_ops *ops'], 'return_type': 'void'}`
- New: `{'params': ['struct drm_gpuvm *gpuvm', 'struct drm_gpuva_ops *ops'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001135 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_sched_init
- Explanation: drm_sched_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_gpu_scheduler *sched', 'const struct drm_sched_backend_ops *ops', 'uint32_t hw_submission', 'unsigned hang_limit', 'long timeout', 'struct workqueue_struct *timeout_wq', 'atomic_t *score', 'const char *name', 'struct device *dev'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_gpu_scheduler *sched', 'const struct drm_sched_backend_ops *ops', 'u32 num_rqs', 'uint32_t hw_submission', 'unsigned int hang_limit', 'long timeout', 'struct workqueue_struct *timeout_wq', 'atomic_t *score', 'const char *name', 'struct device *dev'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-001138 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: samsung_dsim_remove
- Explanation: samsung_dsim_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct platform_device *pdev'], 'return_type': 'extern int'}`
- New: `{'params': ['struct platform_device *pdev'], 'return_type': 'extern void'}`

### Rust Evidence

- Graph edges: `0`

## W-001139 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: void
- Explanation: void changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['*drmres_release_t)(struct drm_device *dev, void *res'], 'return_type': 'typedef'}`
- New: `{'params': ['*work_func_t)(struct work_struct *work'], 'return_type': 'typedef'}`

### Rust Evidence

- Graph edges: `0`

## W-001008 FieldDrift

- Risk: Medium
- Score: 9.4
- Symbol: cred
- Explanation: cred changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'usage', 'type': 'atomic_long_t'}, {'name': 'uid', 'type': 'kuid_t'}, {'name': 'gid', 'type': 'kgid_t'}, {'name': 'suid', 'type': 'kuid_t'}, {'name': 'sgid', 'type': 'kgid_t'}, {'name': 'euid', 'type': 'kuid_t'}, {'name': 'egid', 'type': 'kgid_t'}, {'name': 'fsuid', 'type': 'kuid_t'}, {'name': 'fsgid', 'type': 'kgid_t'}, {'name': 'securebits', 'type': 'core::ffi::c_uint'}, {'name': 'cap_inheritable', 'type': 'kernel_cap_t'}, {'name': 'cap_permitted', 'type': 'kernel_cap_t'}, {'name': 'cap_effective', 'type': 'kernel_cap_t'}, {'name': 'cap_bset', 'type': 'kernel_cap_t'}, {'name': 'cap_ambient', 'type': 'kernel_cap_t'}, {'name': 'jit_keyring', 'type': 'core::ffi::c_uchar'}, {'name': 'session_keyring', 'type': '*mut key'}, {'name': 'process_keyring', 'type': '*mut key'}, {'name': 'thread_keyring', 'type': '*mut key'}, {'name': 'request_key_auth', 'type': '*mut key'}, {'name': 'security', 'type': '*mut core::ffi::c_void'}, {'name': 'user', 'type': '*mut user_struct'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'ucounts', 'type': '*mut ucounts'}, {'name': 'group_info', 'type': '*mut group_info'}, {'name': '__bindgen_anon_1', 'type': 'cred__bindgen_ty_1'}]`

### Rust Evidence

- Graph edges: `4`

## W-001022 FieldDrift

- Risk: Medium
- Score: 9.4
- Symbol: kunit_suite
- Explanation: kunit_suite changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'name', 'type': '[core::ffi::c_char; 256usize]'}, {'name': 'suite_exit', 'type': '::core::option::Option<unsafe extern "C" fn(suite: *mut kunit_suite)>'}, {'name': 'init', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit) -> core::ffi::c_int>'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'test_cases', 'type': '*mut kunit_case'}, {'name': 'attr', 'type': 'kunit_attributes'}, {'name': 'status_comment', 'type': '[core::ffi::c_char; 256usize]'}, {'name': 'debugfs', 'type': '*mut dentry'}, {'name': 'log', 'type': '*mut core::ffi::c_char'}, {'name': 'suite_init_err', 'type': 'core::ffi::c_int'}]`
- New: `[{'name': 'name', 'type': '[core::ffi::c_char; 256usize]'}, {'name': 'suite_exit', 'type': '::core::option::Option<unsafe extern "C" fn(suite: *mut kunit_suite)>'}, {'name': 'init', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit) -> core::ffi::c_int>'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'test_cases', 'type': '*mut kunit_case'}, {'name': 'attr', 'type': 'kunit_attributes'}, {'name': 'status_comment', 'type': '[core::ffi::c_char; 256usize]'}, {'name': 'debugfs', 'type': '*mut dentry'}, {'name': 'log', 'type': '*mut string_stream'}, {'name': 'suite_init_err', 'type': 'core::ffi::c_int'}]`

### Rust Evidence

- Graph edges: `4`

## W-001004 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: address_space
- Explanation: address_space changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'host', 'type': '*mut inode'}, {'name': 'i_pages', 'type': 'xarray'}, {'name': 'invalidate_lock', 'type': 'rw_semaphore'}, {'name': 'gfp_mask', 'type': 'gfp_t'}, {'name': 'i_mmap_writable', 'type': 'atomic_t'}, {'name': 'i_mmap', 'type': 'rb_root_cached'}, {'name': 'nrpages', 'type': 'core::ffi::c_ulong'}, {'name': 'writeback_index', 'type': 'core::ffi::c_ulong'}, {'name': 'a_ops', 'type': '*const address_space_operations'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'i_mmap_rwsem', 'type': 'rw_semaphore'}, {'name': 'wb_err', 'type': 'errseq_t'}, {'name': 'private_lock', 'type': 'spinlock_t'}, {'name': 'private_list', 'type': 'list_head'}, {'name': 'private_data', 'type': '*mut core::ffi::c_void'}]`

### Rust Evidence

- Graph edges: `3`

## W-001005 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bin_attribute
- Explanation: bin_attribute changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'attr', 'type': 'attribute'}, {'name': 'size', 'type': 'usize'}, {'name': 'private', 'type': '*mut core::ffi::c_void'}, {'name': 'f_mapping', 'type': '::core::option::Option<unsafe extern "C" fn() -> *mut address_space>'}, {'name': 'read', 'type': '::core::option::Option<'}, {'name': 'write', 'type': '::core::option::Option<'}, {'name': 'mmap', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'attr', 'type': 'attribute'}, {'name': 'size', 'type': 'usize'}, {'name': 'private', 'type': '*mut core::ffi::c_void'}, {'name': 'f_mapping', 'type': '::core::option::Option<unsafe extern "C" fn() -> *mut address_space>'}, {'name': 'read', 'type': '::core::option::Option<'}, {'name': 'write', 'type': '::core::option::Option<'}, {'name': 'llseek', 'type': '::core::option::Option<'}, {'name': 'mmap', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-001006 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: compat_robust_list_head
- Explanation: compat_robust_list_head changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[{'name': 'list', 'type': 'compat_robust_list'}, {'name': 'futex_offset', 'type': 'compat_long_t'}, {'name': 'list_op_pending', 'type': 'compat_uptr_t'}]`

### Rust Evidence

- Graph edges: `1`

## W-001007 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: cpuinfo_x86
- Explanation: cpuinfo_x86 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'x86', 'type': '__u8'}, {'name': 'x86_vendor', 'type': '__u8'}, {'name': 'x86_model', 'type': '__u8'}, {'name': 'x86_stepping', 'type': '__u8'}, {'name': 'x86_tlbsize', 'type': 'core::ffi::c_int'}, {'name': 'vmx_capability', 'type': '[__u32; 5usize]'}, {'name': 'x86_virt_bits', 'type': '__u8'}, {'name': 'x86_phys_bits', 'type': '__u8'}, {'name': 'x86_coreid_bits', 'type': '__u8'}, {'name': 'cu_id', 'type': '__u8'}, {'name': 'extended_cpuid_level', 'type': '__u32'}, {'name': 'cpuid_level', 'type': 'core::ffi::c_int'}, {'name': '__bindgen_anon_1', 'type': 'cpuinfo_x86__bindgen_ty_1'}, {'name': 'x86_vendor_id', 'type': '[core::ffi::c_char; 16usize]'}, {'name': 'x86_model_id', 'type': '[core::ffi::c_char; 64usize]'}, {'name': 'x86_cache_size', 'type': 'core::ffi::c_uint'}, {'name': 'x86_cache_alignment', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_max_rmid', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_occ_scale', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_mbm_width_offset', 'type': 'core::ffi::c_int'}, {'name': 'x86_power', 'type': 'core::ffi::c_int'}, {'name': 'loops_per_jiffy', 'type': 'core::ffi::c_ulong'}, {'name': 'ppin', 'type': 'u64_'}, {'name': 'x86_max_cores', 'type': 'u16_'}, {'name': 'apicid', 'type': 'u16_'}, {'name': 'initial_apicid', 'type': 'u16_'}, {'name': 'x86_clflush_size', 'type': 'u16_'}, {'name': 'booted_cores', 'type': 'u16_'}, {'name': 'phys_proc_id', 'type': 'u16_'}, {'name': 'logical_proc_id', 'type': 'u16_'}, {'name': 'cpu_core_id', 'type': 'u16_'}, {'name': 'cpu_die_id', 'type': 'u16_'}, {'name': 'logical_die_id', 'type': 'u16_'}, {'name': 'cpu_index', 'type': 'u16_'}, {'name': 'smt_active', 'type': 'bool_'}, {'name': 'microcode', 'type': 'u32_'}, {'name': 'x86_cache_bits', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': 'u16'}]`
- New: `[{'name': 'x86', 'type': '__u8'}, {'name': 'x86_vendor', 'type': '__u8'}, {'name': 'x86_model', 'type': '__u8'}, {'name': 'x86_stepping', 'type': '__u8'}, {'name': 'x86_tlbsize', 'type': 'core::ffi::c_int'}, {'name': 'vmx_capability', 'type': '[__u32; 5usize]'}, {'name': 'x86_virt_bits', 'type': '__u8'}, {'name': 'x86_phys_bits', 'type': '__u8'}, {'name': 'x86_coreid_bits', 'type': '__u8'}, {'name': 'extended_cpuid_level', 'type': '__u32'}, {'name': 'cpuid_level', 'type': 'core::ffi::c_int'}, {'name': '__bindgen_anon_1', 'type': 'cpuinfo_x86__bindgen_ty_1'}, {'name': 'x86_vendor_id', 'type': '[core::ffi::c_char; 16usize]'}, {'name': 'x86_model_id', 'type': '[core::ffi::c_char; 64usize]'}, {'name': 'topo', 'type': 'cpuinfo_topology'}, {'name': 'x86_cache_size', 'type': 'core::ffi::c_uint'}, {'name': 'x86_cache_alignment', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_max_rmid', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_occ_scale', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_mbm_width_offset', 'type': 'core::ffi::c_int'}, {'name': 'x86_power', 'type': 'core::ffi::c_int'}, {'name': 'loops_per_jiffy', 'type': 'core::ffi::c_ulong'}, {'name': 'ppin', 'type': 'u64_'}, {'name': 'x86_max_cores', 'type': 'u16_'}, {'name': 'x86_clflush_size', 'type': 'u16_'}, {'name': 'booted_cores', 'type': 'u16_'}, {'name': 'cpu_index', 'type': 'u16_'}, {'name': 'smt_active', 'type': 'bool_'}, {'name': 'microcode', 'type': 'u32_'}, {'name': 'x86_cache_bits', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u16; 3usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-001009 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: css_set
- Explanation: css_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[]`

### Rust Evidence

- Graph edges: `1`

## W-001011 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: exception_table_entry
- Explanation: exception_table_entry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'insn', 'type': 'core::ffi::c_int'}, {'name': 'fixup', 'type': 'core::ffi::c_int'}, {'name': 'data', 'type': 'core::ffi::c_int'}]`

### Rust Evidence

- Graph edges: `1`

## W-001013 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: file_operations
- Explanation: file_operations changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'owner', 'type': '*mut module'}, {'name': 'llseek', 'type': '::core::option::Option<'}, {'name': 'read', 'type': '::core::option::Option<'}, {'name': 'write', 'type': '::core::option::Option<'}, {'name': 'read_iter', 'type': '::core::option::Option<'}, {'name': 'write_iter', 'type': '::core::option::Option<'}, {'name': 'iopoll', 'type': '::core::option::Option<'}, {'name': 'iterate_shared', 'type': '::core::option::Option<'}, {'name': 'poll', 'type': '::core::option::Option<'}, {'name': 'unlocked_ioctl', 'type': '::core::option::Option<'}, {'name': 'compat_ioctl', 'type': '::core::option::Option<'}, {'name': 'mmap', 'type': '::core::option::Option<'}, {'name': 'mmap_supported_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'open', 'type': '::core::option::Option<'}, {'name': 'flush', 'type': '::core::option::Option<'}, {'name': 'release', 'type': '::core::option::Option<'}, {'name': 'fsync', 'type': '::core::option::Option<'}, {'name': 'fasync', 'type': '::core::option::Option<'}, {'name': 'lock', 'type': '::core::option::Option<'}, {'name': 'get_unmapped_area', 'type': '::core::option::Option<'}, {'name': 'flock', 'type': '::core::option::Option<'}, {'name': 'splice_write', 'type': '::core::option::Option<'}, {'name': 'splice_read', 'type': '::core::option::Option<'}, {'name': 'splice_eof', 'type': '::core::option::Option<unsafe extern "C" fn(file: *mut file)>'}, {'name': 'setlease', 'type': '::core::option::Option<'}, {'name': 'fallocate', 'type': '::core::option::Option<'}, {'name': 'show_fdinfo', 'type': '::core::option::Option<unsafe extern "C" fn(m: *mut seq_file'}, {'name': 'copy_file_range', 'type': '::core::option::Option<'}, {'name': 'remap_file_range', 'type': '::core::option::Option<'}, {'name': 'fadvise', 'type': '::core::option::Option<'}, {'name': 'uring_cmd', 'type': '::core::option::Option<'}, {'name': 'uring_cmd_iopoll', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-001014 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: file_system_type
- Explanation: file_system_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'fs_flags', 'type': 'core::ffi::c_int'}, {'name': 'parameters', 'type': '*const fs_parameter_spec'}, {'name': 'mount', 'type': '::core::option::Option<'}, {'name': 'kill_sb', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut super_block)>'}, {'name': 'owner', 'type': '*mut module'}, {'name': 'next', 'type': '*mut file_system_type'}, {'name': 'fs_supers', 'type': 'hlist_head'}, {'name': 's_lock_key', 'type': 'lock_class_key'}, {'name': 's_umount_key', 'type': 'lock_class_key'}, {'name': 's_vfs_rename_key', 'type': 'lock_class_key'}, {'name': 's_writers_key', 'type': '[lock_class_key; 3usize]'}, {'name': 'i_lock_key', 'type': 'lock_class_key'}, {'name': 'i_mutex_key', 'type': 'lock_class_key'}, {'name': 'invalidate_lock_key', 'type': 'lock_class_key'}, {'name': 'i_mutex_dir_key', 'type': 'lock_class_key'}]`

### Rust Evidence

- Graph edges: `1`

## W-001015 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: iattr
- Explanation: iattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'ia_valid', 'type': 'core::ffi::c_uint'}, {'name': 'ia_mode', 'type': 'umode_t'}, {'name': '__bindgen_anon_1', 'type': 'iattr__bindgen_ty_1'}, {'name': '__bindgen_anon_2', 'type': 'iattr__bindgen_ty_2'}, {'name': 'ia_size', 'type': 'loff_t'}, {'name': 'ia_atime', 'type': 'timespec64'}, {'name': 'ia_mtime', 'type': 'timespec64'}, {'name': 'ia_ctime', 'type': 'timespec64'}, {'name': 'ia_file', 'type': '*mut file'}]`

### Rust Evidence

- Graph edges: `1`

## W-001017 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: io_context
- Explanation: io_context changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'refcount', 'type': 'atomic_long_t'}, {'name': 'active_ref', 'type': 'atomic_t'}, {'name': 'ioprio', 'type': 'core::ffi::c_ushort'}]`

### Rust Evidence

- Graph edges: `1`

## W-001018 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: kernfs_ops
- Explanation: kernfs_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(of: *mut kernfs_open_file)>'}, {'name': 'seq_show', 'type': '::core::option::Option<'}, {'name': 'seq_start', 'type': '::core::option::Option<'}, {'name': 'seq_next', 'type': '::core::option::Option<'}, {'name': 'read', 'type': '::core::option::Option<'}, {'name': 'atomic_write_len', 'type': 'usize'}, {'name': 'prealloc', 'type': 'bool_'}, {'name': 'write', 'type': '::core::option::Option<'}, {'name': 'poll', 'type': '::core::option::Option<'}, {'name': 'mmap', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(of: *mut kernfs_open_file)>'}, {'name': 'seq_show', 'type': '::core::option::Option<'}, {'name': 'seq_start', 'type': '::core::option::Option<'}, {'name': 'seq_next', 'type': '::core::option::Option<'}, {'name': 'read', 'type': '::core::option::Option<'}, {'name': 'atomic_write_len', 'type': 'usize'}, {'name': 'prealloc', 'type': 'bool_'}, {'name': 'write', 'type': '::core::option::Option<'}, {'name': 'poll', 'type': '::core::option::Option<'}, {'name': 'mmap', 'type': '::core::option::Option<'}, {'name': 'llseek', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-001021 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: kunit_case
- Explanation: kunit_case changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'run_case', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'generate_params', 'type': '::core::option::Option<'}, {'name': 'attr', 'type': 'kunit_attributes'}, {'name': 'status', 'type': 'kunit_status'}, {'name': 'module_name', 'type': '*mut core::ffi::c_char'}, {'name': 'log', 'type': '*mut core::ffi::c_char'}]`
- New: `[{'name': 'run_case', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'generate_params', 'type': '::core::option::Option<'}, {'name': 'attr', 'type': 'kunit_attributes'}, {'name': 'status', 'type': 'kunit_status'}, {'name': 'module_name', 'type': '*mut core::ffi::c_char'}, {'name': 'log', 'type': '*mut string_stream'}]`

### Rust Evidence

- Graph edges: `1`

## W-001024 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: mmu_notifier_subscriptions
- Explanation: mmu_notifier_subscriptions changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[]`

### Rust Evidence

- Graph edges: `1`

## W-001025 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: page__bindgen_ty_1__bindgen_ty_2
- Explanation: page__bindgen_ty_1__bindgen_ty_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'pp_magic', 'type': 'core::ffi::c_ulong'}, {'name': 'pp', 'type': '*mut page_pool'}, {'name': '_pp_mapping_pad', 'type': 'core::ffi::c_ulong'}, {'name': 'dma_addr', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'page__bindgen_ty_1__bindgen_ty_2__bindgen_ty_1'}]`
- New: `[{'name': 'pp_magic', 'type': 'core::ffi::c_ulong'}, {'name': 'pp', 'type': '*mut page_pool'}, {'name': '_pp_mapping_pad', 'type': 'core::ffi::c_ulong'}, {'name': 'dma_addr', 'type': 'core::ffi::c_ulong'}, {'name': 'pp_frag_count', 'type': 'atomic_long_t'}]`

### Rust Evidence

- Graph edges: `1`

## W-001026 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: per_cpu_pages
- Explanation: per_cpu_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'lock', 'type': 'spinlock_t'}, {'name': 'count', 'type': 'core::ffi::c_int'}, {'name': 'high', 'type': 'core::ffi::c_int'}, {'name': 'batch', 'type': 'core::ffi::c_int'}, {'name': 'free_factor', 'type': 'core::ffi::c_short'}, {'name': 'expire', 'type': 'core::ffi::c_short'}, {'name': 'lists', 'type': '[list_head; 12usize]'}]`
- New: `[{'name': 'lock', 'type': 'spinlock_t'}, {'name': 'count', 'type': 'core::ffi::c_int'}, {'name': 'high', 'type': 'core::ffi::c_int'}, {'name': 'high_min', 'type': 'core::ffi::c_int'}, {'name': 'high_max', 'type': 'core::ffi::c_int'}, {'name': 'batch', 'type': 'core::ffi::c_int'}, {'name': 'flags', 'type': 'u8_'}, {'name': 'alloc_factor', 'type': 'u8_'}, {'name': 'expire', 'type': 'u8_'}, {'name': 'free_count', 'type': 'core::ffi::c_short'}, {'name': 'lists', 'type': '[list_head; 12usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-001027 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: sched_param
- Explanation: sched_param changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'sched_priority', 'type': 'core::ffi::c_int'}]`

### Rust Evidence

- Graph edges: `1`

## W-001028 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: sighand_struct
- Explanation: sighand_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'siglock', 'type': 'spinlock_t'}, {'name': 'count', 'type': 'refcount_t'}, {'name': 'signalfd_wqh', 'type': 'wait_queue_head_t'}, {'name': 'action', 'type': '[k_sigaction; 64usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-001029 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: signal_struct
- Explanation: signal_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'sigcnt', 'type': 'refcount_t'}, {'name': 'live', 'type': 'atomic_t'}, {'name': 'nr_threads', 'type': 'core::ffi::c_int'}, {'name': 'quick_threads', 'type': 'core::ffi::c_int'}, {'name': 'thread_head', 'type': 'list_head'}, {'name': 'wait_chldexit', 'type': 'wait_queue_head_t'}, {'name': 'curr_target', 'type': '*mut task_struct'}, {'name': 'shared_pending', 'type': 'sigpending'}, {'name': 'multiprocess', 'type': 'hlist_head'}, {'name': 'group_exit_code', 'type': 'core::ffi::c_int'}, {'name': 'notify_count', 'type': 'core::ffi::c_int'}, {'name': 'group_exec_task', 'type': '*mut task_struct'}, {'name': 'group_stop_count', 'type': 'core::ffi::c_int'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'core_state', 'type': '*mut core_state'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'next_posix_timer_id', 'type': 'core::ffi::c_uint'}, {'name': 'posix_timers', 'type': 'list_head'}, {'name': 'real_timer', 'type': 'hrtimer'}, {'name': 'it_real_incr', 'type': 'ktime_t'}, {'name': 'it', 'type': '[cpu_itimer; 2usize]'}, {'name': 'cputimer', 'type': 'thread_group_cputimer'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'pids', 'type': '[*mut pid; 4usize]'}, {'name': 'tty_old_pgrp', 'type': '*mut pid'}, {'name': 'leader', 'type': 'core::ffi::c_int'}, {'name': 'tty', 'type': '*mut tty_struct'}, {'name': 'stats_lock', 'type': 'seqlock_t'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'cutime', 'type': 'u64_'}, {'name': 'cstime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'cgtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'cnvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'cnivcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'min_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'cmin_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'cmaj_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'inblock', 'type': 'core::ffi::c_ulong'}, {'name': 'oublock', 'type': 'core::ffi::c_ulong'}, {'name': 'cinblock', 'type': 'core::ffi::c_ulong'}, {'name': 'coublock', 'type': 'core::ffi::c_ulong'}, {'name': 'maxrss', 'type': 'core::ffi::c_ulong'}, {'name': 'cmaxrss', 'type': 'core::ffi::c_ulong'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'sum_sched_runtime', 'type': 'core::ffi::c_ulonglong'}, {'name': 'rlim', 'type': '[rlimit; 16usize]'}, {'name': 'pacct', 'type': 'pacct_struct'}, {'name': 'stats', 'type': '*mut taskstats'}, {'name': 'audit_tty', 'type': 'core::ffi::c_uint'}, {'name': 'tty_audit_buf', 'type': '*mut tty_audit_buf'}, {'name': 'oom_flag_origin', 'type': 'bool_'}, {'name': 'oom_score_adj', 'type': 'core::ffi::c_short'}, {'name': 'oom_score_adj_min', 'type': 'core::ffi::c_short'}, {'name': 'oom_mm', 'type': '*mut mm_struct'}, {'name': 'cred_guard_mutex', 'type': 'mutex'}, {'name': 'exec_update_lock', 'type': 'rw_semaphore'}]`

### Rust Evidence

- Graph edges: `1`

## W-001030 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: super_block
- Explanation: super_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 's_list', 'type': 'list_head'}, {'name': 's_dev', 'type': 'dev_t'}, {'name': 's_blocksize_bits', 'type': 'core::ffi::c_uchar'}, {'name': 's_blocksize', 'type': 'core::ffi::c_ulong'}, {'name': 's_maxbytes', 'type': 'loff_t'}, {'name': 's_type', 'type': '*mut file_system_type'}, {'name': 's_op', 'type': '*const super_operations'}, {'name': 'dq_op', 'type': '*const dquot_operations'}, {'name': 's_qcop', 'type': '*const quotactl_ops'}, {'name': 's_export_op', 'type': '*const export_operations'}, {'name': 's_flags', 'type': 'core::ffi::c_ulong'}, {'name': 's_iflags', 'type': 'core::ffi::c_ulong'}, {'name': 's_magic', 'type': 'core::ffi::c_ulong'}, {'name': 's_root', 'type': '*mut dentry'}, {'name': 's_umount', 'type': 'rw_semaphore'}, {'name': 's_count', 'type': 'core::ffi::c_int'}, {'name': 's_active', 'type': 'atomic_t'}, {'name': 's_security', 'type': '*mut core::ffi::c_void'}, {'name': 's_xattr', 'type': '*const *mut xattr_handler'}, {'name': 's_roots', 'type': 'hlist_bl_head'}, {'name': 's_mounts', 'type': 'list_head'}, {'name': 's_bdev', 'type': '*mut block_device'}, {'name': 's_bdev_handle', 'type': '*mut bdev_handle'}, {'name': 's_bdi', 'type': '*mut backing_dev_info'}, {'name': 's_mtd', 'type': '*mut mtd_info'}, {'name': 's_instances', 'type': 'hlist_node'}, {'name': 's_quota_types', 'type': 'core::ffi::c_uint'}, {'name': 's_dquot', 'type': 'quota_info'}, {'name': 's_writers', 'type': 'sb_writers'}, {'name': 's_fs_info', 'type': '*mut core::ffi::c_void'}, {'name': 's_time_gran', 'type': 'u32_'}, {'name': 's_time_min', 'type': 'time64_t'}, {'name': 's_time_max', 'type': 'time64_t'}, {'name': 's_fsnotify_mask', 'type': '__u32'}, {'name': 's_fsnotify_marks', 'type': '*mut fsnotify_mark_connector'}, {'name': 's_id', 'type': '[core::ffi::c_char; 32usize]'}, {'name': 's_uuid', 'type': 'uuid_t'}, {'name': 's_max_links', 'type': 'core::ffi::c_uint'}, {'name': 's_vfs_rename_mutex', 'type': 'mutex'}, {'name': 's_subtype', 'type': '*const core::ffi::c_char'}, {'name': 's_d_op', 'type': '*const dentry_operations'}, {'name': 's_shrink', 'type': '*mut shrinker'}, {'name': 's_remove_count', 'type': 'atomic_long_t'}, {'name': 's_fsnotify_connectors', 'type': 'atomic_long_t'}, {'name': 's_readonly_remount', 'type': 'core::ffi::c_int'}, {'name': 's_wb_err', 'type': 'errseq_t'}, {'name': 's_dio_done_wq', 'type': '*mut workqueue_struct'}, {'name': 's_pins', 'type': 'hlist_head'}, {'name': 's_user_ns', 'type': '*mut user_namespace'}, {'name': 's_dentry_lru', 'type': 'list_lru'}, {'name': 's_inode_lru', 'type': 'list_lru'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 's_sync_lock', 'type': 'mutex'}, {'name': 's_stack_depth', 'type': 'core::ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': '[u32; 11usize]'}, {'name': 's_inode_list_lock', 'type': 'spinlock_t'}, {'name': 's_inodes', 'type': 'list_head'}, {'name': 's_inode_wblist_lock', 'type': 'spinlock_t'}, {'name': 's_inodes_wb', 'type': 'list_head'}]`

### Rust Evidence

- Graph edges: `1`

## W-001032 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vma_numab_state
- Explanation: vma_numab_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'next_scan', 'type': 'core::ffi::c_ulong'}, {'name': 'next_pid_reset', 'type': 'core::ffi::c_ulong'}, {'name': 'access_pids', 'type': '[core::ffi::c_ulong; 2usize]'}]`
- New: `[{'name': 'next_scan', 'type': 'core::ffi::c_ulong'}, {'name': 'pids_active_reset', 'type': 'core::ffi::c_ulong'}, {'name': 'pids_active', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'prev_scan_seq', 'type': 'core::ffi::c_int'}]`

### Rust Evidence

- Graph edges: `1`

## W-001034 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ANNOTATE_IGNORE_ALTERNATIVE
- Explanation: ANNOTATE_IGNORE_ALTERNATIVE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `b"999:\n\t.pushsection .discard.ignore_alts\n\t.long 999b - .\n\t.popsection\n\t\0"`
- New: `b"999:\n\t.pushsection .discard.ignore_alts\n\t.long 999b\n\t.popsection\n\t\0"`

### Rust Evidence

- Graph edges: `1`

## W-001035 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ANNOTATE_NOENDBR
- Explanation: ANNOTATE_NOENDBR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `b"986: \n\t.pushsection .discard.noendbr\n\t.long 986b - .\n\t.popsection\n\t\0"`
- New: `b"986: \n\t.pushsection .discard.noendbr\n\t.long 986b\n\t.popsection\n\t\0"`

### Rust Evidence

- Graph edges: `1`

## W-001036 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ANNOTATE_RETPOLINE_SAFE
- Explanation: ANNOTATE_RETPOLINE_SAFE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `b"999:\n\t.pushsection .discard.retpoline_safe\n\t.long 999b - .\n\t.popsection\n\t\0"`
- New: `b"999:\n\t.pushsection .discard.retpoline_safe\n\t.long 999b\n\t.popsection\n\t\0"`

### Rust Evidence

- Graph edges: `1`

## W-001037 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ASM_REACHABLE
- Explanation: ASM_REACHABLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `b"998:\n\t.pushsection .discard.reachable\n\t.long 998b - .\n\t.popsection\n\t\0"`
- New: `b"998:\n\t.pushsection .discard.reachable\n\t.long 998b\n\t.popsection\n\t\0"`

### Rust Evidence

- Graph edges: `1`

## W-001038 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: CONFIG_RUSTC_VERSION_TEXT
- Explanation: CONFIG_RUSTC_VERSION_TEXT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `b"rustc 1.71.1 (eb26296b5 2023-08-03)\0"`
- New: `b"rustc 1.73.0 (cc66ad468 2023-10-03)\0"`

### Rust Evidence

- Graph edges: `1`

## W-001039 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: IA32_NR_syscalls
- Explanation: IA32_NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `453`
- New: `457`

### Rust Evidence

- Graph edges: `1`

## W-001040 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: NR_syscalls
- Explanation: NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `454`
- New: `457`

### Rust Evidence

- Graph edges: `1`

## W-001041 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: SECCOMP_ARCH_COMPAT_NR
- Explanation: SECCOMP_ARCH_COMPAT_NR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `453`
- New: `457`

### Rust Evidence

- Graph edges: `1`

## W-001042 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: SECCOMP_ARCH_NATIVE_NR
- Explanation: SECCOMP_ARCH_NATIVE_NR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `454`
- New: `457`

### Rust Evidence

- Graph edges: `1`

## W-001043 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TASK_stack_canary
- Explanation: TASK_stack_canary changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `1320`
- New: `1328`

### Rust Evidence

- Graph edges: `1`

## W-001044 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: WQ_FLAG_CUSTOM
- Explanation: WQ_FLAG_CUSTOM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `4`

### Rust Evidence

- Graph edges: `1`

## W-001045 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: WQ_FLAG_DONE
- Explanation: WQ_FLAG_DONE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `8`

### Rust Evidence

- Graph edges: `1`

## W-001046 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: WQ_FLAG_PRIORITY
- Explanation: WQ_FLAG_PRIORITY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `32`
- New: `16`

### Rust Evidence

- Graph edges: `1`

## W-001047 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __NR_ia32_syscalls
- Explanation: __NR_ia32_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `453`
- New: `457`

### Rust Evidence

- Graph edges: `1`

## W-001048 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __NR_syscalls
- Explanation: __NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `454`
- New: `457`

### Rust Evidence

- Graph edges: `1`

## W-001099 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: WQ_FLAG_CUSTOM
- Explanation: WQ_FLAG_CUSTOM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x08`
- New: `0x04`

### Rust Evidence

- Graph edges: `1`

## W-001100 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: WQ_FLAG_DONE
- Explanation: WQ_FLAG_DONE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x10`
- New: `0x08`

### Rust Evidence

- Graph edges: `1`

## W-001101 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: WQ_FLAG_PRIORITY
- Explanation: WQ_FLAG_PRIORITY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x20`
- New: `0x10`

### Rust Evidence

- Graph edges: `1`

## W-001049 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CEC
- Explanation: CLKID_CEC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `25`
- New: `175`

### Rust Evidence

- Graph edges: `0`

## W-001050 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CECA_32K_DIV
- Explanation: CLKID_CECA_32K_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `116`
- New: `13`

### Rust Evidence

- Graph edges: `0`

## W-001051 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CECA_32K_SEL
- Explanation: CLKID_CECA_32K_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `118`
- New: `15`

### Rust Evidence

- Graph edges: `0`

## W-001052 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CECA_32K_SEL_PRE
- Explanation: CLKID_CECA_32K_SEL_PRE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `117`
- New: `14`

### Rust Evidence

- Graph edges: `0`

## W-001053 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CECB_32K_DIV
- Explanation: CLKID_CECB_32K_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `112`
- New: `18`

### Rust Evidence

- Graph edges: `0`

## W-001054 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CECB_32K_SEL
- Explanation: CLKID_CECB_32K_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `114`
- New: `20`

### Rust Evidence

- Graph edges: `0`

## W-001055 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CECB_32K_SEL_PRE
- Explanation: CLKID_CECB_32K_SEL_PRE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `113`
- New: `19`

### Rust Evidence

- Graph edges: `0`

## W-001056 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_GEN
- Explanation: CLKID_GEN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `73`
- New: `168`

### Rust Evidence

- Graph edges: `0`

## W-001057 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_GEN_DIV
- Explanation: CLKID_GEN_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `122`
- New: `167`

### Rust Evidence

- Graph edges: `0`

## W-001058 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_GEN_SEL
- Explanation: CLKID_GEN_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `121`
- New: `166`

### Rust Evidence

- Graph edges: `0`

## W-001059 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_I2C_M_A
- Explanation: CLKID_I2C_M_A changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `31`
- New: `198`

### Rust Evidence

- Graph edges: `0`

## W-001060 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_I2C_M_B
- Explanation: CLKID_I2C_M_B changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `30`
- New: `199`

### Rust Evidence

- Graph edges: `0`

## W-001061 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_I2C_M_C
- Explanation: CLKID_I2C_M_C changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `29`
- New: `200`

### Rust Evidence

- Graph edges: `0`

## W-001062 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_I2C_M_D
- Explanation: CLKID_I2C_M_D changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `28`
- New: `201`

### Rust Evidence

- Graph edges: `0`

## W-001063 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_IR_CTRL
- Explanation: CLKID_IR_CTRL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `27`
- New: `183`

### Rust Evidence

- Graph edges: `0`

## W-001064 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MSR
- Explanation: CLKID_MSR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `18`
- New: `182`

### Rust Evidence

- Graph edges: `0`

## W-001065 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_A
- Explanation: CLKID_PWM_A changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `76`
- New: `135`

### Rust Evidence

- Graph edges: `0`

## W-001066 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_AB
- Explanation: CLKID_PWM_AB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `24`
- New: `214`

### Rust Evidence

- Graph edges: `0`

## W-001067 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_A_DIV
- Explanation: CLKID_PWM_A_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `125`
- New: `134`

### Rust Evidence

- Graph edges: `0`

## W-001068 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_A_SEL
- Explanation: CLKID_PWM_A_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `124`
- New: `133`

### Rust Evidence

- Graph edges: `0`

## W-001069 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_B
- Explanation: CLKID_PWM_B changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `77`
- New: `138`

### Rust Evidence

- Graph edges: `0`

## W-001070 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_B_DIV
- Explanation: CLKID_PWM_B_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `127`
- New: `137`

### Rust Evidence

- Graph edges: `0`

## W-001071 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_B_SEL
- Explanation: CLKID_PWM_B_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `126`
- New: `136`

### Rust Evidence

- Graph edges: `0`

## W-001072 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_C
- Explanation: CLKID_PWM_C changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `78`
- New: `141`

### Rust Evidence

- Graph edges: `0`

## W-001073 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_CD
- Explanation: CLKID_PWM_CD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `23`
- New: `215`

### Rust Evidence

- Graph edges: `0`

## W-001074 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_C_DIV
- Explanation: CLKID_PWM_C_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `129`
- New: `140`

### Rust Evidence

- Graph edges: `0`

## W-001075 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_C_SEL
- Explanation: CLKID_PWM_C_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `128`
- New: `139`

### Rust Evidence

- Graph edges: `0`

## W-001076 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_D
- Explanation: CLKID_PWM_D changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `79`
- New: `144`

### Rust Evidence

- Graph edges: `0`

## W-001077 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_D_DIV
- Explanation: CLKID_PWM_D_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `131`
- New: `143`

### Rust Evidence

- Graph edges: `0`

## W-001078 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_D_SEL
- Explanation: CLKID_PWM_D_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `130`
- New: `142`

### Rust Evidence

- Graph edges: `0`

## W-001079 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_E
- Explanation: CLKID_PWM_E changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `80`
- New: `147`

### Rust Evidence

- Graph edges: `0`

## W-001080 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_EF
- Explanation: CLKID_PWM_EF changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `22`
- New: `216`

### Rust Evidence

- Graph edges: `0`

## W-001081 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_E_DIV
- Explanation: CLKID_PWM_E_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `133`
- New: `146`

### Rust Evidence

- Graph edges: `0`

## W-001082 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_E_SEL
- Explanation: CLKID_PWM_E_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `132`
- New: `145`

### Rust Evidence

- Graph edges: `0`

## W-001083 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_F
- Explanation: CLKID_PWM_F changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `81`
- New: `150`

### Rust Evidence

- Graph edges: `0`

## W-001084 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_F_DIV
- Explanation: CLKID_PWM_F_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `135`
- New: `149`

### Rust Evidence

- Graph edges: `0`

## W-001085 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_F_SEL
- Explanation: CLKID_PWM_F_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `134`
- New: `148`

### Rust Evidence

- Graph edges: `0`

## W-001086 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_RSA
- Explanation: CLKID_RSA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `47`
- New: `208`

### Rust Evidence

- Graph edges: `0`

## W-001087 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_RTC
- Explanation: CLKID_RTC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `67`
- New: `4`

### Rust Evidence

- Graph edges: `0`

## W-001088 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_RTC_32K_DIV
- Explanation: CLKID_RTC_32K_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `108`
- New: `1`

### Rust Evidence

- Graph edges: `0`

## W-001089 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_RTC_32K_SEL
- Explanation: CLKID_RTC_32K_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `110`
- New: `2`

### Rust Evidence

- Graph edges: `0`

## W-001090 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SARADC
- Explanation: CLKID_SARADC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `75`
- New: `165`

### Rust Evidence

- Graph edges: `0`

## W-001091 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SARADC_DIV
- Explanation: CLKID_SARADC_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `123`
- New: `164`

### Rust Evidence

- Graph edges: `0`

## W-001092 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SARADC_SEL
- Explanation: CLKID_SARADC_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `74`
- New: `163`

### Rust Evidence

- Graph edges: `0`

## W-001093 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SPIFC
- Explanation: CLKID_SPIFC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `84`
- New: `181`

### Rust Evidence

- Graph edges: `0`

## W-001094 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_UART_A
- Explanation: CLKID_UART_A changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `45`
- New: `186`

### Rust Evidence

- Graph edges: `0`

## W-001095 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_UART_B
- Explanation: CLKID_UART_B changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `44`
- New: `187`

### Rust Evidence

- Graph edges: `0`

## W-001096 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_UART_C
- Explanation: CLKID_UART_C changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `43`
- New: `188`

### Rust Evidence

- Graph edges: `0`

## W-001097 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: DRM_BUDDY_RANGE_ALLOCATION
- Explanation: DRM_BUDDY_RANGE_ALLOCATION changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `(1 << 0)`
- New: `BIT(0)`

### Rust Evidence

- Graph edges: `0`

## W-001098 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: DRM_BUDDY_TOPDOWN_ALLOCATION
- Explanation: DRM_BUDDY_TOPDOWN_ALLOCATION changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `(1 << 1)`
- New: `BIT(1)`

### Rust Evidence

- Graph edges: `0`
