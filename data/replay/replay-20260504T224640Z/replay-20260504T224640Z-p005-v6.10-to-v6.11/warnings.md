# BindDrift Ranked Warnings

## W-000590 SignatureDrift

- Risk: High
- Score: 14.4
- Symbol: ERR_PTR
- Explanation: ERR_PTR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['-ENODEV'], 'return_type': 'return'}`
- New: `{'params': ['-EINVAL'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `19`

## W-000351 SignatureDrift

- Risk: High
- Score: 14.0
- Symbol: request_firmware
- Explanation: request_firmware changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `17`

## W-000031 SignatureDrift

- Risk: High
- Score: 13.4
- Symbol: alloc_pages
- Explanation: alloc_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `14`

## W-000247 SignatureDrift

- Risk: High
- Score: 12.8
- Symbol: firmware_request_nowarn
- Explanation: firmware_request_nowarn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `11`

## W-000418 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: cgroup
- Explanation: cgroup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'self_', 'type': 'cgroup_subsys_state'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'level', 'type': 'core::ffi::c_int'}, {'name': 'max_depth', 'type': 'core::ffi::c_int'}, {'name': 'nr_descendants', 'type': 'core::ffi::c_int'}, {'name': 'nr_dying_descendants', 'type': 'core::ffi::c_int'}, {'name': 'max_descendants', 'type': 'core::ffi::c_int'}, {'name': 'nr_populated_csets', 'type': 'core::ffi::c_int'}, {'name': 'nr_populated_domain_children', 'type': 'core::ffi::c_int'}, {'name': 'nr_populated_threaded_children', 'type': 'core::ffi::c_int'}, {'name': 'nr_threaded_children', 'type': 'core::ffi::c_int'}, {'name': 'kn', 'type': '*mut kernfs_node'}, {'name': 'procs_file', 'type': 'cgroup_file'}, {'name': 'events_file', 'type': 'cgroup_file'}, {'name': 'psi_files', 'type': '__IncompleteArrayField<cgroup_file>'}, {'name': 'subtree_control', 'type': 'u16_'}, {'name': 'subtree_ss_mask', 'type': 'u16_'}, {'name': 'old_subtree_control', 'type': 'u16_'}, {'name': 'old_subtree_ss_mask', 'type': 'u16_'}, {'name': 'subsys', 'type': '[*mut cgroup_subsys_state; 14usize]'}, {'name': 'root', 'type': '*mut cgroup_root'}, {'name': 'cset_links', 'type': 'list_head'}, {'name': 'e_csets', 'type': '[list_head; 14usize]'}, {'name': 'dom_cgrp', 'type': '*mut cgroup'}, {'name': 'old_dom_cgrp', 'type': '*mut cgroup'}, {'name': 'rstat_cpu', 'type': '*mut cgroup_rstat_cpu'}, {'name': 'rstat_css_list', 'type': 'list_head'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': '_pad_', 'type': 'cacheline_padding'}, {'name': 'rstat_flush_next', 'type': '*mut cgroup'}, {'name': 'last_bstat', 'type': 'cgroup_base_stat'}, {'name': 'bstat', 'type': 'cgroup_base_stat'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'pidlists', 'type': 'list_head'}, {'name': 'pidlist_mutex', 'type': 'mutex'}, {'name': 'offline_waitq', 'type': 'wait_queue_head_t'}, {'name': 'release_agent_work', 'type': 'work_struct'}, {'name': 'psi', 'type': '*mut psi_group'}, {'name': 'bpf', 'type': 'cgroup_bpf'}, {'name': 'congestion_count', 'type': 'atomic_t'}, {'name': 'freezer', 'type': 'cgroup_freezer_state'}, {'name': 'ancestors', 'type': '__IncompleteArrayField<*mut cgroup>'}]`
- New: `[{'name': 'self_', 'type': 'cgroup_subsys_state'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'level', 'type': 'core::ffi::c_int'}, {'name': 'max_depth', 'type': 'core::ffi::c_int'}, {'name': 'nr_descendants', 'type': 'core::ffi::c_int'}, {'name': 'nr_dying_descendants', 'type': 'core::ffi::c_int'}, {'name': 'max_descendants', 'type': 'core::ffi::c_int'}, {'name': 'nr_populated_csets', 'type': 'core::ffi::c_int'}, {'name': 'nr_populated_domain_children', 'type': 'core::ffi::c_int'}, {'name': 'nr_populated_threaded_children', 'type': 'core::ffi::c_int'}, {'name': 'nr_threaded_children', 'type': 'core::ffi::c_int'}, {'name': 'kn', 'type': '*mut kernfs_node'}, {'name': 'procs_file', 'type': 'cgroup_file'}, {'name': 'events_file', 'type': 'cgroup_file'}, {'name': 'psi_files', 'type': '__IncompleteArrayField<cgroup_file>'}, {'name': 'subtree_control', 'type': 'u16_'}, {'name': 'subtree_ss_mask', 'type': 'u16_'}, {'name': 'old_subtree_control', 'type': 'u16_'}, {'name': 'old_subtree_ss_mask', 'type': 'u16_'}, {'name': 'subsys', 'type': '[*mut cgroup_subsys_state; 14usize]'}, {'name': 'root', 'type': '*mut cgroup_root'}, {'name': 'cset_links', 'type': 'list_head'}, {'name': 'e_csets', 'type': '[list_head; 14usize]'}, {'name': 'dom_cgrp', 'type': '*mut cgroup'}, {'name': 'old_dom_cgrp', 'type': '*mut cgroup'}, {'name': 'rstat_cpu', 'type': '*mut cgroup_rstat_cpu'}, {'name': 'rstat_css_list', 'type': 'list_head'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': '_pad_', 'type': 'cacheline_padding'}, {'name': 'rstat_flush_next', 'type': '*mut cgroup'}, {'name': 'last_bstat', 'type': 'cgroup_base_stat'}, {'name': 'bstat', 'type': 'cgroup_base_stat'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'pidlists', 'type': 'list_head'}, {'name': 'pidlist_mutex', 'type': 'mutex'}, {'name': 'offline_waitq', 'type': 'wait_queue_head_t'}, {'name': 'release_agent_work', 'type': 'work_struct'}, {'name': 'psi', 'type': '*mut psi_group'}, {'name': 'bpf', 'type': 'cgroup_bpf'}, {'name': 'freezer', 'type': 'cgroup_freezer_state'}, {'name': 'ancestors', 'type': '__IncompleteArrayField<*mut cgroup>'}]`

### Rust Evidence

- Graph edges: `50`

## W-000423 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: inode
- Explanation: inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'i_mode', 'type': 'umode_t'}, {'name': 'i_opflags', 'type': 'core::ffi::c_ushort'}, {'name': 'i_uid', 'type': 'kuid_t'}, {'name': 'i_gid', 'type': 'kgid_t'}, {'name': 'i_flags', 'type': 'core::ffi::c_uint'}, {'name': 'i_acl', 'type': '*mut posix_acl'}, {'name': 'i_default_acl', 'type': '*mut posix_acl'}, {'name': 'i_op', 'type': '*const inode_operations'}, {'name': 'i_sb', 'type': '*mut super_block'}, {'name': 'i_mapping', 'type': '*mut address_space'}, {'name': 'i_security', 'type': '*mut core::ffi::c_void'}, {'name': 'i_ino', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'inode__bindgen_ty_1'}, {'name': 'i_rdev', 'type': 'dev_t'}, {'name': 'i_size', 'type': 'loff_t'}, {'name': '__i_atime', 'type': 'timespec64'}, {'name': '__i_mtime', 'type': 'timespec64'}, {'name': '__i_ctime', 'type': 'timespec64'}, {'name': 'i_lock', 'type': 'spinlock_t'}, {'name': 'i_bytes', 'type': 'core::ffi::c_ushort'}, {'name': 'i_blkbits', 'type': 'u8_'}, {'name': 'i_write_hint', 'type': 'rw_hint'}, {'name': 'i_blocks', 'type': 'blkcnt_t'}, {'name': 'i_state', 'type': 'core::ffi::c_ulong'}, {'name': 'i_rwsem', 'type': 'rw_semaphore'}, {'name': 'dirtied_when', 'type': 'core::ffi::c_ulong'}, {'name': 'dirtied_time_when', 'type': 'core::ffi::c_ulong'}, {'name': 'i_hash', 'type': 'hlist_node'}, {'name': 'i_io_list', 'type': 'list_head'}, {'name': 'i_lru', 'type': 'list_head'}, {'name': 'i_sb_list', 'type': 'list_head'}, {'name': 'i_wb_list', 'type': 'list_head'}, {'name': '__bindgen_anon_2', 'type': 'inode__bindgen_ty_2'}, {'name': 'i_version', 'type': 'atomic64_t'}, {'name': 'i_sequence', 'type': 'atomic64_t'}, {'name': 'i_count', 'type': 'atomic_t'}, {'name': 'i_dio_count', 'type': 'atomic_t'}, {'name': 'i_writecount', 'type': 'atomic_t'}, {'name': 'i_readcount', 'type': 'atomic_t'}, {'name': '__bindgen_anon_3', 'type': 'inode__bindgen_ty_3'}, {'name': 'i_flctx', 'type': '*mut file_lock_context'}, {'name': 'i_data', 'type': 'address_space'}, {'name': 'i_devices', 'type': 'list_head'}, {'name': '__bindgen_anon_4', 'type': 'inode__bindgen_ty_4'}, {'name': 'i_generation', 'type': '__u32'}, {'name': 'i_fsnotify_mask', 'type': '__u32'}, {'name': 'i_fsnotify_marks', 'type': '*mut fsnotify_mark_connector'}, {'name': 'i_private', 'type': '*mut core::ffi::c_void'}]`
- New: `[{'name': 'i_mode', 'type': 'umode_t'}, {'name': 'i_opflags', 'type': 'core::ffi::c_ushort'}, {'name': 'i_uid', 'type': 'kuid_t'}, {'name': 'i_gid', 'type': 'kgid_t'}, {'name': 'i_flags', 'type': 'core::ffi::c_uint'}, {'name': 'i_acl', 'type': '*mut posix_acl'}, {'name': 'i_default_acl', 'type': '*mut posix_acl'}, {'name': 'i_op', 'type': '*const inode_operations'}, {'name': 'i_sb', 'type': '*mut super_block'}, {'name': 'i_mapping', 'type': '*mut address_space'}, {'name': 'i_security', 'type': '*mut core::ffi::c_void'}, {'name': 'i_ino', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'inode__bindgen_ty_1'}, {'name': 'i_rdev', 'type': 'dev_t'}, {'name': 'i_size', 'type': 'loff_t'}, {'name': 'i_atime_sec', 'type': 'time64_t'}, {'name': 'i_mtime_sec', 'type': 'time64_t'}, {'name': 'i_ctime_sec', 'type': 'time64_t'}, {'name': 'i_atime_nsec', 'type': 'u32_'}, {'name': 'i_mtime_nsec', 'type': 'u32_'}, {'name': 'i_ctime_nsec', 'type': 'u32_'}, {'name': 'i_generation', 'type': 'u32_'}, {'name': 'i_lock', 'type': 'spinlock_t'}, {'name': 'i_bytes', 'type': 'core::ffi::c_ushort'}, {'name': 'i_blkbits', 'type': 'u8_'}, {'name': 'i_write_hint', 'type': 'rw_hint'}, {'name': 'i_blocks', 'type': 'blkcnt_t'}, {'name': 'i_state', 'type': 'core::ffi::c_ulong'}, {'name': 'i_rwsem', 'type': 'rw_semaphore'}, {'name': 'dirtied_when', 'type': 'core::ffi::c_ulong'}, {'name': 'dirtied_time_when', 'type': 'core::ffi::c_ulong'}, {'name': 'i_hash', 'type': 'hlist_node'}, {'name': 'i_io_list', 'type': 'list_head'}, {'name': 'i_lru', 'type': 'list_head'}, {'name': 'i_sb_list', 'type': 'list_head'}, {'name': 'i_wb_list', 'type': 'list_head'}, {'name': '__bindgen_anon_2', 'type': 'inode__bindgen_ty_2'}, {'name': 'i_version', 'type': 'atomic64_t'}, {'name': 'i_sequence', 'type': 'atomic64_t'}, {'name': 'i_count', 'type': 'atomic_t'}, {'name': 'i_dio_count', 'type': 'atomic_t'}, {'name': 'i_writecount', 'type': 'atomic_t'}, {'name': 'i_readcount', 'type': 'atomic_t'}, {'name': '__bindgen_anon_3', 'type': 'inode__bindgen_ty_3'}, {'name': 'i_flctx', 'type': '*mut file_lock_context'}, {'name': 'i_data', 'type': 'address_space'}, {'name': 'i_devices', 'type': 'list_head'}, {'name': '__bindgen_anon_4', 'type': 'inode__bindgen_ty_4'}, {'name': 'i_fsnotify_mask', 'type': '__u32'}, {'name': 'i_fsnotify_marks', 'type': '*mut fsnotify_mark_connector'}, {'name': 'i_private', 'type': '*mut core::ffi::c_void'}]`

### Rust Evidence

- Graph edges: `33`

## W-000431 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: statx
- Explanation: statx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'stx_mask', 'type': '__u32'}, {'name': 'stx_blksize', 'type': '__u32'}, {'name': 'stx_attributes', 'type': '__u64'}, {'name': 'stx_nlink', 'type': '__u32'}, {'name': 'stx_uid', 'type': '__u32'}, {'name': 'stx_gid', 'type': '__u32'}, {'name': 'stx_mode', 'type': '__u16'}, {'name': '__spare0', 'type': '[__u16; 1usize]'}, {'name': 'stx_ino', 'type': '__u64'}, {'name': 'stx_size', 'type': '__u64'}, {'name': 'stx_blocks', 'type': '__u64'}, {'name': 'stx_attributes_mask', 'type': '__u64'}, {'name': 'stx_atime', 'type': 'statx_timestamp'}, {'name': 'stx_btime', 'type': 'statx_timestamp'}, {'name': 'stx_ctime', 'type': 'statx_timestamp'}, {'name': 'stx_mtime', 'type': 'statx_timestamp'}, {'name': 'stx_rdev_major', 'type': '__u32'}, {'name': 'stx_rdev_minor', 'type': '__u32'}, {'name': 'stx_dev_major', 'type': '__u32'}, {'name': 'stx_dev_minor', 'type': '__u32'}, {'name': 'stx_mnt_id', 'type': '__u64'}, {'name': 'stx_dio_mem_align', 'type': '__u32'}, {'name': 'stx_dio_offset_align', 'type': '__u32'}, {'name': 'stx_subvol', 'type': '__u64'}, {'name': '__spare3', 'type': '[__u64; 11usize]'}]`
- New: `[{'name': 'stx_mask', 'type': '__u32'}, {'name': 'stx_blksize', 'type': '__u32'}, {'name': 'stx_attributes', 'type': '__u64'}, {'name': 'stx_nlink', 'type': '__u32'}, {'name': 'stx_uid', 'type': '__u32'}, {'name': 'stx_gid', 'type': '__u32'}, {'name': 'stx_mode', 'type': '__u16'}, {'name': '__spare0', 'type': '[__u16; 1usize]'}, {'name': 'stx_ino', 'type': '__u64'}, {'name': 'stx_size', 'type': '__u64'}, {'name': 'stx_blocks', 'type': '__u64'}, {'name': 'stx_attributes_mask', 'type': '__u64'}, {'name': 'stx_atime', 'type': 'statx_timestamp'}, {'name': 'stx_btime', 'type': 'statx_timestamp'}, {'name': 'stx_ctime', 'type': 'statx_timestamp'}, {'name': 'stx_mtime', 'type': 'statx_timestamp'}, {'name': 'stx_rdev_major', 'type': '__u32'}, {'name': 'stx_rdev_minor', 'type': '__u32'}, {'name': 'stx_dev_major', 'type': '__u32'}, {'name': 'stx_dev_minor', 'type': '__u32'}, {'name': 'stx_mnt_id', 'type': '__u64'}, {'name': 'stx_dio_mem_align', 'type': '__u32'}, {'name': 'stx_dio_offset_align', 'type': '__u32'}, {'name': 'stx_subvol', 'type': '__u64'}, {'name': 'stx_atomic_write_unit_min', 'type': '__u32'}, {'name': 'stx_atomic_write_unit_max', 'type': '__u32'}, {'name': 'stx_atomic_write_segments_max', 'type': '__u32'}, {'name': '__spare1', 'type': '[__u32; 1usize]'}, {'name': '__spare3', 'type': '[__u64; 9usize]'}]`

### Rust Evidence

- Graph edges: `33`

## W-000136 SignatureDrift

- Risk: High
- Score: 12.4
- Symbol: blk_mq_rq_to_pdu
- Explanation: blk_mq_rq_to_pdu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `9`

## W-000141 SignatureDrift

- Risk: High
- Score: 12.4
- Symbol: blk_mq_start_request
- Explanation: blk_mq_start_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `9`

## W-000219 SignatureDrift

- Risk: High
- Score: 12.4
- Symbol: device_add_disk
- Explanation: device_add_disk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `9`

## W-000422 FieldDrift

- Risk: High
- Score: 12.4
- Symbol: gendisk
- Explanation: gendisk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[{'name': 'major', 'type': 'core::ffi::c_int'}, {'name': 'first_minor', 'type': 'core::ffi::c_int'}, {'name': 'minors', 'type': 'core::ffi::c_int'}, {'name': 'disk_name', 'type': '[core::ffi::c_char; 32usize]'}, {'name': 'events', 'type': 'core::ffi::c_ushort'}, {'name': 'event_flags', 'type': 'core::ffi::c_ushort'}, {'name': 'part_tbl', 'type': 'xarray'}, {'name': 'part0', 'type': '*mut block_device'}, {'name': 'fops', 'type': '*const block_device_operations'}, {'name': 'queue', 'type': '*mut request_queue'}, {'name': 'private_data', 'type': '*mut core::ffi::c_void'}, {'name': 'bio_split', 'type': 'bio_set'}, {'name': 'flags', 'type': 'core::ffi::c_int'}, {'name': 'state', 'type': 'core::ffi::c_ulong'}, {'name': 'open_mutex', 'type': 'mutex'}, {'name': 'open_partitions', 'type': 'core::ffi::c_uint'}, {'name': 'bdi', 'type': '*mut backing_dev_info'}, {'name': 'queue_kobj', 'type': 'kobject'}, {'name': 'slave_dir', 'type': '*mut kobject'}, {'name': 'slave_bdevs', 'type': 'list_head'}, {'name': 'random', 'type': '*mut timer_rand_state'}, {'name': 'sync_io', 'type': 'atomic_t'}, {'name': 'ev', 'type': '*mut disk_events'}, {'name': 'cdi', 'type': '*mut cdrom_device_info'}, {'name': 'node_id', 'type': 'core::ffi::c_int'}, {'name': 'bb', 'type': '*mut badblocks'}, {'name': 'lockdep_map', 'type': 'lockdep_map'}, {'name': 'diskseq', 'type': 'u64_'}, {'name': 'open_mode', 'type': 'blk_mode_t'}, {'name': 'ia_ranges', 'type': '*mut blk_independent_access_ranges'}]`

### Rust Evidence

- Graph edges: `19`

## W-000276 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: kmap_local_page
- Explanation: kmap_local_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000118 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: blk_mq_end_request
- Explanation: blk_mq_end_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000210 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: copy_from_user
- Explanation: copy_from_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000331 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: proc_dointvec
- Explanation: proc_dointvec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*const ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `6`

## W-000349 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: release_firmware
- Explanation: release_firmware changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000007 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: __blk_mq_alloc_disk
- Explanation: __blk_mq_alloc_disk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000111 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: blk_mq_alloc_tag_set
- Explanation: blk_mq_alloc_tag_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000211 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: copy_to_user
- Explanation: copy_to_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000380 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: set_capacity
- Explanation: set_capacity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000602 ErrorDrift

- Risk: High
- Score: 11.45
- Symbol: firmware_request_nowarn
- Explanation: firmware_request_nowarn has ERROR_CODE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/include/linux/firmware.h:142 `return -EINVAL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:12 `None` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:24 `request_nowarn` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:80 `Firmware::request` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:28 `/// Abstraction around a C `struct firmware`.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:29 `///`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:79 `/// Send a request for an optional firmware module. See also`

## W-000121 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: blk_mq_free_tag_set
- Explanation: blk_mq_free_tag_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000218 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: del_gendisk
- Explanation: del_gendisk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000237 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: errno_to_blk_status
- Explanation: errno_to_blk_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000282 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: kunmap_local
- Explanation: kunmap_local changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000603 ErrorDrift

- Risk: High
- Score: 11.25
- Symbol: request_firmware
- Explanation: request_firmware has ERROR_CODE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/include/linux/firmware.h:127 `return -EINVAL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:12 `None` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:20 `request` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:74 `request_internal` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:69 `// SAFETY: `func` not bailing out with a non-zero error code, guarantees that `fw` is a`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:74 `/// Send a firmware request and wait for it. See also `bindings::request_firmware`.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:71 `NONNULL_MAPPING`

## W-000063 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: bio_chain
- Explanation: bio_chain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000081 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: bio_split
- Explanation: bio_split changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000122 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: blk_mq_freeze_queue
- Explanation: blk_mq_freeze_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000149 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: blk_mq_unique_tag
- Explanation: blk_mq_unique_tag changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000169 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: blk_rq_map_user
- Explanation: blk_rq_map_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000200 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: block_size
- Explanation: block_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000248 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: firmware_request_platform
- Explanation: firmware_request_platform changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000302 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: mempool_free
- Explanation: mempool_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000352 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: request_firmware_direct
- Explanation: request_firmware_direct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000385 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: submit_bio
- Explanation: submit_bio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000390 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: sync_blockdev
- Explanation: sync_blockdev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000021 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __register_blkdev
- Explanation: __register_blkdev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000022 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __sbitmap_queue_get
- Explanation: __sbitmap_queue_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000024 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __skb_get_hash
- Explanation: __skb_get_hash changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `2`

## W-000054 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: bio_add_folio
- Explanation: bio_add_folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000061 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: bio_associate_blkg
- Explanation: bio_associate_blkg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000067 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: bio_copy_data
- Explanation: bio_copy_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000072 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: bio_init
- Explanation: bio_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000095 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: blk_execute_rq
- Explanation: blk_execute_rq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000108 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: blk_mq_alloc_request
- Explanation: blk_mq_alloc_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000112 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: blk_mq_complete_request
- Explanation: blk_mq_complete_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000115 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: blk_mq_delay_run_hw_queue
- Explanation: blk_mq_delay_run_hw_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000123 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: blk_mq_freeze_queue_wait
- Explanation: blk_mq_freeze_queue_wait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000130 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: blk_mq_quiesce_queue
- Explanation: blk_mq_quiesce_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000137 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: blk_mq_run_hw_queue
- Explanation: blk_mq_run_hw_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000139 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: blk_mq_start_hw_queue
- Explanation: blk_mq_start_hw_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000142 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: blk_mq_start_stopped_hw_queue
- Explanation: blk_mq_start_stopped_hw_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000144 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: blk_mq_stop_hw_queue
- Explanation: blk_mq_stop_hw_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000170 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: blk_rq_map_user_io
- Explanation: blk_rq_map_user_io changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000180 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: blk_start_plug
- Explanation: blk_start_plug changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000203 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: btf_header
- Explanation: btf_header changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000234 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: early_lookup_bdev
- Explanation: early_lookup_bdev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000246 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: firmware_request_nowait_nowarn
- Explanation: firmware_request_nowait_nowarn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000298 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: mempool_create
- Explanation: mempool_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000334 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: proc_dointvec_ms_jiffies
- Explanation: proc_dointvec_ms_jiffies changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*const ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `2`

## W-000339 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: proc_douintvec
- Explanation: proc_douintvec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*const ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `2`

## W-000353 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: request_firmware_into_buf
- Explanation: request_firmware_into_buf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000354 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: request_firmware_nowait
- Explanation: request_firmware_nowait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000355 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: request_partial_firmware_into_buf
- Explanation: request_partial_firmware_into_buf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000362 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: sbitmap_get
- Explanation: sbitmap_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000366 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: sbitmap_queue_clear
- Explanation: sbitmap_queue_clear changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000395 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: tc_at_ingress
- Explanation: tc_at_ingress changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(1usize, 1u8) as u8) } } #[inline] pub fn set_tc_at_ingress(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(2usize, 1u8) as u8) } } #[inline] pub fn set_tc_at_ingress(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `2`

## W-000398 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: tstamp_type
- Explanation: tstamp_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000399 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: unpin_folio
- Explanation: unpin_folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000405 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: wifi_acked
- Explanation: wifi_acked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(11usize, 1u8) as u8) } } #[inline] pub fn set_wifi_acked(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(12usize, 1u8) as u8) } } #[inline] pub fn set_wifi_acked(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `2`

## W-000001 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: I_BDEV
- Explanation: I_BDEV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000002 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __bio_add_page
- Explanation: __bio_add_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000003 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __bio_advance
- Explanation: __bio_advance changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000004 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __bio_release_pages
- Explanation: __bio_release_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000005 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __blk_alloc_disk
- Explanation: __blk_alloc_disk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000006 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __blk_flush_plug
- Explanation: __blk_flush_plug changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000008 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __blk_mq_end_request
- Explanation: __blk_mq_end_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000009 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __blk_rq_map_sg
- Explanation: __blk_rq_map_sg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000010 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __blk_should_fake_timeout
- Explanation: __blk_should_fake_timeout changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000011 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __blkdev_issue_discard
- Explanation: __blkdev_issue_discard changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000012 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __blkdev_issue_zeroout
- Explanation: __blkdev_issue_zeroout changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000013 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __bpf_free_used_btfs
- Explanation: __bpf_free_used_btfs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'aux', 'type': '*mut bpf_prog_aux'}, {'name': 'used_btfs', 'type': '*mut btf_mod_pair'}, {'name': 'len', 'type': 'u32_'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'used_btfs', 'type': '*mut btf_mod_pair'}, {'name': 'len', 'type': 'u32_'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000014 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kmalloc_cache_node_noprof
- Explanation: __kmalloc_cache_node_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000015 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kmalloc_cache_noprof
- Explanation: __kmalloc_cache_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000016 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kmalloc_large_node_noprof
- Explanation: __kmalloc_large_node_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000017 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kmalloc_large_noprof
- Explanation: __kmalloc_large_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000018 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kmalloc_node_track_caller_noprof
- Explanation: __kmalloc_node_track_caller_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000019 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kvmalloc_node_noprof
- Explanation: __kvmalloc_node_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000023 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sbitmap_queue_get_batch
- Explanation: __sbitmap_queue_get_batch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000025 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_get_hash_net
- Explanation: __skb_get_hash_net changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000026 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_get_hash_symmetric
- Explanation: __skb_get_hash_symmetric changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000027 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_get_hash_symmetric_net
- Explanation: __skb_get_hash_symmetric_net changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000028 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sys_bind_socket
- Explanation: __sys_bind_socket changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000029 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sys_listen_socket
- Explanation: __sys_listen_socket changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000030 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: add_disk_randomness
- Explanation: add_disk_randomness changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000032 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: allocate_resource
- Explanation: allocate_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'root', 'type': '*mut resource'}, {'name': 'new', 'type': '*mut resource'}, {'name': 'size', 'type': 'resource_size_t'}, {'name': 'min', 'type': 'resource_size_t'}, {'name': 'max', 'type': 'resource_size_t'}, {'name': 'align', 'type': 'resource_size_t'}, {'name': 'alignf', 'type': '::core::option::Option< unsafe extern "C" fn( arg1: *mut core::ffi::c_void, arg2: *const resource, arg3: resource_size_t, arg4: resource_size_t,'}], 'return_type': 'resource_size_t, >, alignf_data: *mut core::ffi::c_void, ) -> core::ffi::c_int'}`
- New: `{'params': [{'name': 'root', 'type': '*mut resource'}, {'name': 'new', 'type': '*mut resource'}, {'name': 'size', 'type': 'resource_size_t'}, {'name': 'min', 'type': 'resource_size_t'}, {'name': 'max', 'type': 'resource_size_t'}, {'name': 'align', 'type': 'resource_size_t'}, {'name': 'alignf', 'type': 'resource_alignf'}, {'name': 'alignf_data', 'type': '*mut core::ffi::c_void'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000034 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_prctl_spec_ctrl_get
- Explanation: arch_prctl_spec_ctrl_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000035 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_prctl_spec_ctrl_set
- Explanation: arch_prctl_spec_ctrl_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000036 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_seccomp_spec_mitigate
- Explanation: arch_seccomp_spec_mitigate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000037 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_uprobe_trampoline
- Explanation: arch_uprobe_trampoline changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000038 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bd_abort_claiming
- Explanation: bd_abort_claiming changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000039 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bd_link_disk_holder
- Explanation: bd_link_disk_holder changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000040 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bd_prepare_to_claim
- Explanation: bd_prepare_to_claim changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000041 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bd_unlink_disk_holder
- Explanation: bd_unlink_disk_holder changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000042 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bdev_alignment_offset
- Explanation: bdev_alignment_offset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000043 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bdev_discard_alignment
- Explanation: bdev_discard_alignment changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000044 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bdev_disk_changed
- Explanation: bdev_disk_changed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000045 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bdev_end_io_acct
- Explanation: bdev_end_io_acct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000046 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bdev_file_open_by_dev
- Explanation: bdev_file_open_by_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000047 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bdev_file_open_by_path
- Explanation: bdev_file_open_by_path changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000048 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bdev_fput
- Explanation: bdev_fput changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000049 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bdev_freeze
- Explanation: bdev_freeze changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000050 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bdev_mark_dead
- Explanation: bdev_mark_dead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000051 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bdev_start_io_acct
- Explanation: bdev_start_io_acct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000052 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bdev_statx
- Explanation: bdev_statx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000053 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bdev_thaw
- Explanation: bdev_thaw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000055 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_add_folio_nofail
- Explanation: bio_add_folio_nofail changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000056 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_add_page
- Explanation: bio_add_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000057 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_add_pc_page
- Explanation: bio_add_pc_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000058 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_add_zone_append_page
- Explanation: bio_add_zone_append_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000059 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_alloc_bioset
- Explanation: bio_alloc_bioset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000060 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_alloc_clone
- Explanation: bio_alloc_clone changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000062 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_associate_blkg_from_css
- Explanation: bio_associate_blkg_from_css changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000064 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_chain_and_submit
- Explanation: bio_chain_and_submit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000065 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_check_pages_dirty
- Explanation: bio_check_pages_dirty changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000066 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_clone_blkg_association
- Explanation: bio_clone_blkg_association changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000068 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_copy_data_iter
- Explanation: bio_copy_data_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000069 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_end_io_acct_remapped
- Explanation: bio_end_io_acct_remapped changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000070 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_endio
- Explanation: bio_endio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000071 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_free_pages
- Explanation: bio_free_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000073 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_init_clone
- Explanation: bio_init_clone changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000074 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_iov_bvec_set
- Explanation: bio_iov_bvec_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000075 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_iov_iter_get_pages
- Explanation: bio_iov_iter_get_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000076 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_kmalloc
- Explanation: bio_kmalloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000077 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_poll
- Explanation: bio_poll changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000078 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_put
- Explanation: bio_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000079 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_reset
- Explanation: bio_reset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000080 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_set_pages_dirty
- Explanation: bio_set_pages_dirty changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000082 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_split_rw
- Explanation: bio_split_rw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000083 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_split_to_limits
- Explanation: bio_split_to_limits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000084 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_start_io_acct
- Explanation: bio_start_io_acct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000085 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_trim
- Explanation: bio_trim changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000086 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_uninit
- Explanation: bio_uninit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000087 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bioset_exit
- Explanation: bioset_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000088 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bioset_init
- Explanation: bioset_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000089 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: biovec_init_pool
- Explanation: biovec_init_pool changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000090 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_abort_request
- Explanation: blk_abort_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000091 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_alloc_discard_bio
- Explanation: blk_alloc_discard_bio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000092 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_check_plugged
- Explanation: blk_check_plugged changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000093 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_clear_pm_only
- Explanation: blk_clear_pm_only changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000094 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_dump_rq_flags
- Explanation: blk_dump_rq_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000096 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_execute_rq_nowait
- Explanation: blk_execute_rq_nowait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000097 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_finish_plug
- Explanation: blk_finish_plug changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000098 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_freeze_queue_start
- Explanation: blk_freeze_queue_start changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000099 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_get_queue
- Explanation: blk_get_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000100 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_insert_cloned_request
- Explanation: blk_insert_cloned_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000101 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_io_schedule
- Explanation: blk_io_schedule changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000102 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_limits_io_min
- Explanation: blk_limits_io_min changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000103 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_limits_io_opt
- Explanation: blk_limits_io_opt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000104 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_lld_busy
- Explanation: blk_lld_busy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000105 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mark_disk_dead
- Explanation: blk_mark_disk_dead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000106 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_alloc_disk_for_queue
- Explanation: blk_mq_alloc_disk_for_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000107 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_alloc_queue
- Explanation: blk_mq_alloc_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000109 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_alloc_request_hctx
- Explanation: blk_mq_alloc_request_hctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000110 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_alloc_sq_tag_set
- Explanation: blk_mq_alloc_sq_tag_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000113 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_complete_request_remote
- Explanation: blk_mq_complete_request_remote changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000114 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_delay_kick_requeue_list
- Explanation: blk_mq_delay_kick_requeue_list changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000116 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_delay_run_hw_queues
- Explanation: blk_mq_delay_run_hw_queues changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000117 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_destroy_queue
- Explanation: blk_mq_destroy_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000119 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_end_request_batch
- Explanation: blk_mq_end_request_batch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000120 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_free_request
- Explanation: blk_mq_free_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000124 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_freeze_queue_wait_timeout
- Explanation: blk_mq_freeze_queue_wait_timeout changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000125 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_hctx_set_fq_lock_class
- Explanation: blk_mq_hctx_set_fq_lock_class changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000126 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_init_allocated_queue
- Explanation: blk_mq_init_allocated_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000127 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_kick_requeue_list
- Explanation: blk_mq_kick_requeue_list changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000128 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_map_queues
- Explanation: blk_mq_map_queues changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000129 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_queue_inflight
- Explanation: blk_mq_queue_inflight changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000131 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_quiesce_queue_nowait
- Explanation: blk_mq_quiesce_queue_nowait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000132 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_quiesce_tagset
- Explanation: blk_mq_quiesce_tagset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000133 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_requeue_request
- Explanation: blk_mq_requeue_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000134 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_rq_cpu
- Explanation: blk_mq_rq_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000135 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_rq_from_pdu
- Explanation: blk_mq_rq_from_pdu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000138 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_run_hw_queues
- Explanation: blk_mq_run_hw_queues changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000140 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_start_hw_queues
- Explanation: blk_mq_start_hw_queues changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000143 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_start_stopped_hw_queues
- Explanation: blk_mq_start_stopped_hw_queues changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000145 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_stop_hw_queues
- Explanation: blk_mq_stop_hw_queues changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000146 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_tagset_busy_iter
- Explanation: blk_mq_tagset_busy_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000147 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_tagset_wait_completed_request
- Explanation: blk_mq_tagset_wait_completed_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000148 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_unfreeze_queue
- Explanation: blk_mq_unfreeze_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000150 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_unquiesce_queue
- Explanation: blk_mq_unquiesce_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000151 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_unquiesce_tagset
- Explanation: blk_mq_unquiesce_tagset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000152 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_update_nr_hw_queues
- Explanation: blk_mq_update_nr_hw_queues changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000153 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_mq_wait_quiesce_done
- Explanation: blk_mq_wait_quiesce_done changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000154 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_next_bio
- Explanation: blk_next_bio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000155 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_op_str
- Explanation: blk_op_str changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000156 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_put_queue
- Explanation: blk_put_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000157 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_queue_enter
- Explanation: blk_queue_enter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000158 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_queue_exit
- Explanation: blk_queue_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000159 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_queue_flag_clear
- Explanation: blk_queue_flag_clear changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000160 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_queue_flag_set
- Explanation: blk_queue_flag_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000161 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_queue_rq_timeout
- Explanation: blk_queue_rq_timeout changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000162 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_register_queue
- Explanation: blk_register_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000163 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_request_module
- Explanation: blk_request_module changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000164 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_revalidate_disk_zones
- Explanation: blk_revalidate_disk_zones changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000165 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_rq_append_bio
- Explanation: blk_rq_append_bio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000166 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_rq_init
- Explanation: blk_rq_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000167 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_rq_is_poll
- Explanation: blk_rq_is_poll changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000168 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_rq_map_kern
- Explanation: blk_rq_map_kern changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000171 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_rq_map_user_iov
- Explanation: blk_rq_map_user_iov changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000172 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_rq_poll
- Explanation: blk_rq_poll changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000173 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_rq_prep_clone
- Explanation: blk_rq_prep_clone changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000174 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_rq_unmap_user
- Explanation: blk_rq_unmap_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000175 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_rq_unprep_clone
- Explanation: blk_rq_unprep_clone changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000176 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_set_pm_only
- Explanation: blk_set_pm_only changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000177 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_set_queue_depth
- Explanation: blk_set_queue_depth changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000178 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_set_stacking_limits
- Explanation: blk_set_stacking_limits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000179 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_stack_limits
- Explanation: blk_stack_limits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000181 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_start_plug_nr_ios
- Explanation: blk_start_plug_nr_ios changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000182 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_status_to_errno
- Explanation: blk_status_to_errno changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000183 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_status_to_str
- Explanation: blk_status_to_str changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000184 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_steal_bios
- Explanation: blk_steal_bios changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000185 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_sync_queue
- Explanation: blk_sync_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000186 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_unregister_queue
- Explanation: blk_unregister_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000187 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_update_request
- Explanation: blk_update_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000188 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_zone_cond_str
- Explanation: blk_zone_cond_str changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000189 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blkcg_punt_bio_submit
- Explanation: blkcg_punt_bio_submit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000190 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blkdev_compat_ptr_ioctl
- Explanation: blkdev_compat_ptr_ioctl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000191 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blkdev_get_no_open
- Explanation: blkdev_get_no_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000192 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blkdev_issue_discard
- Explanation: blkdev_issue_discard changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000193 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blkdev_issue_flush
- Explanation: blkdev_issue_flush changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000194 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blkdev_issue_secure_erase
- Explanation: blkdev_issue_secure_erase changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000195 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blkdev_issue_zeroout
- Explanation: blkdev_issue_zeroout changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000196 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blkdev_put_no_open
- Explanation: blkdev_put_no_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000197 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blkdev_report_zones
- Explanation: blkdev_report_zones changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000198 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blkdev_show
- Explanation: blkdev_show changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000199 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blkdev_zone_mgmt
- Explanation: blkdev_zone_mgmt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000201 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_dynptr_from_skb_rdonly
- Explanation: bpf_dynptr_from_skb_rdonly changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'flags', 'type': 'u64_'}, {'name': 'ptr', 'type': '*mut bpf_dynptr_kern'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'skb', 'type': '*mut __sk_buff'}, {'name': 'flags', 'type': 'u64_'}, {'name': 'ptr', 'type': '*mut bpf_dynptr'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000202 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_base_btf
- Explanation: btf_base_btf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000204 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_is_vmlinux
- Explanation: btf_is_vmlinux changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000207 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: console_try_replay_all
- Explanation: console_try_replay_all changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000212 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_hotplug_disable_offlining
- Explanation: cpu_hotplug_disable_offlining changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000213 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: csum_complete_sw
- Explanation: csum_complete_sw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(4usize, 1u8) as u8) } } #[inline] pub fn set_csum_complete_sw(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(5usize, 1u8) as u8) } } #[inline] pub fn set_csum_complete_sw(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000214 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: csum_level
- Explanation: csum_level changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(5usize, 2u8) as u8) } } #[inline] pub fn set_csum_level(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(6usize, 2u8) as u8) } } #[inline] pub fn set_csum_level(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000215 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: csum_valid
- Explanation: csum_valid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(15usize, 1u8) as u8) } } #[inline] pub fn set_csum_valid(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(16usize, 1u8) as u8) } } #[inline] pub fn set_csum_valid(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000216 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_parent_ino
- Explanation: d_parent_ino changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000217 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: default_timestamp
- Explanation: default_timestamp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000220 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_driver_attach
- Explanation: device_driver_attach changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'drv', 'type': '*mut device_driver'}, {'name': 'dev', 'type': '*mut device'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'drv', 'type': '*const device_driver'}, {'name': 'dev', 'type': '*mut device'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000221 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dirtytime_interval_handler
- Explanation: dirtytime_interval_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'table', 'type': '*mut ctl_table'}, {'name': 'write', 'type': 'core::ffi::c_int'}, {'name': 'buffer', 'type': '*mut core::ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'table', 'type': '*const ctl_table'}, {'name': 'write', 'type': 'core::ffi::c_int'}, {'name': 'buffer', 'type': '*mut core::ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000222 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: disk_alloc_independent_access_ranges
- Explanation: disk_alloc_independent_access_ranges changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000223 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: disk_check_media_change
- Explanation: disk_check_media_change changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000224 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: disk_force_media_change
- Explanation: disk_force_media_change changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000225 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: disk_live
- Explanation: disk_live changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000226 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: disk_set_independent_access_ranges
- Explanation: disk_set_independent_access_ranges changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000227 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: disk_uevent
- Explanation: disk_uevent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000228 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_proc_douintvec
- Explanation: do_proc_douintvec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'table', 'type': '*mut ctl_table'}, {'name': 'write', 'type': 'core::ffi::c_int'}, {'name': 'buffer', 'type': '*mut core::ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}, {'name': 'conv', 'type': '::core::option::Option< unsafe extern "C" fn( lvalp: *mut core::ffi::c_ulong, valp: *mut core::ffi::c_uint, write: core::ffi::c_int, data: *mut core::ffi::c_void,'}], 'return_type': 'core::ffi::c_int, >, data: *mut core::ffi::c_void, ) -> core::ffi::c_int'}`
- New: `{'params': [{'name': 'table', 'type': '*const ctl_table'}, {'name': 'write', 'type': 'core::ffi::c_int'}, {'name': 'buffer', 'type': '*mut core::ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}, {'name': 'conv', 'type': '::core::option::Option< unsafe extern "C" fn( lvalp: *mut core::ffi::c_ulong, valp: *mut core::ffi::c_uint, write: core::ffi::c_int, data: *mut core::ffi::c_void,'}], 'return_type': 'core::ffi::c_int, >, data: *mut core::ffi::c_void, ) -> core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000229 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: driver_attach
- Explanation: driver_attach changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'drv', 'type': '*mut device_driver'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'drv', 'type': '*const device_driver'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000230 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: driver_create_file
- Explanation: driver_create_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'driver', 'type': '*mut device_driver'}, {'name': 'attr', 'type': '*const driver_attribute'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'driver', 'type': '*const device_driver'}, {'name': 'attr', 'type': '*const driver_attribute'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000231 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: driver_find_device
- Explanation: driver_find_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'drv', 'type': '*mut device_driver'}, {'name': 'start', 'type': '*mut device'}, {'name': 'data', 'type': '*const core::ffi::c_void'}, {'name': 'match_', 'type': '::core::option::Option< unsafe extern "C" fn( dev: *mut device, data: *const core::ffi::c_void,'}], 'return_type': 'core::ffi::c_int, >, ) -> *mut device'}`
- New: `{'params': [{'name': 'drv', 'type': '*const device_driver'}, {'name': 'start', 'type': '*mut device'}, {'name': 'data', 'type': '*const core::ffi::c_void'}, {'name': 'match_', 'type': '::core::option::Option< unsafe extern "C" fn( dev: *mut device, data: *const core::ffi::c_void,'}], 'return_type': 'core::ffi::c_int, >, ) -> *mut device'}`

### Rust Evidence

- Graph edges: `1`

## W-000232 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: driver_remove_file
- Explanation: driver_remove_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'driver', 'type': '*mut device_driver'}, {'name': 'attr', 'type': '*const driver_attribute'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'driver', 'type': '*const device_driver'}, {'name': 'attr', 'type': '*const driver_attribute'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000233 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drop_caches_sysctl_handler
- Explanation: drop_caches_sysctl_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*const ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000235 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: encap_hdr_csum
- Explanation: encap_hdr_csum changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(14usize, 1u8) as u8) } } #[inline] pub fn set_encap_hdr_csum(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(15usize, 1u8) as u8) } } #[inline] pub fn set_encap_hdr_csum(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000236 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: encapsulation
- Explanation: encapsulation changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(13usize, 1u8) as u8) } } #[inline] pub fn set_encapsulation(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(14usize, 1u8) as u8) } } #[inline] pub fn set_encapsulation(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000238 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_get_ts_info_by_layer
- Explanation: ethtool_get_ts_info_by_layer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'dev', 'type': '*mut net_device'}, {'name': 'info', 'type': '*mut ethtool_ts_info'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'dev', 'type': '*mut net_device'}, {'name': 'info', 'type': '*mut kernel_ethtool_ts_info'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000239 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_op_get_ts_info
- Explanation: ethtool_op_get_ts_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'dev', 'type': '*mut net_device'}, {'name': 'eti', 'type': '*mut ethtool_ts_info'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'dev', 'type': '*mut net_device'}, {'name': 'eti', 'type': '*mut kernel_ethtool_ts_info'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000240 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_rxfh_context_lost
- Explanation: ethtool_rxfh_context_lost changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000242 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: file_bdev
- Explanation: file_bdev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000243 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: find_resource_space
- Explanation: find_resource_space changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000244 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: firmware_request_builtin
- Explanation: firmware_request_builtin changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000245 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: firmware_request_cache
- Explanation: firmware_request_cache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000249 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: flow_hash_from_keys_seed
- Explanation: flow_hash_from_keys_seed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000250 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_alloc_mpol_noprof
- Explanation: folio_alloc_mpol_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000251 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_mc_copy
- Explanation: folio_mc_copy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000252 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_zero_user
- Explanation: folio_zero_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000253 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_reserved_page
- Explanation: free_reserved_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000254 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_atomic_write_valid
- Explanation: generic_atomic_write_valid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000255 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_ci_match
- Explanation: generic_ci_match changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000256 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_fill_statx_atomic_writes
- Explanation: generic_fill_statx_atomic_writes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000257 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: getname_flags
- Explanation: getname_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*const core::ffi::c_char'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_int'}], 'return_type': '*mut filename'}`
- New: `{'params': [{'name': 'arg1', 'type': '*const core::ffi::c_char'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}], 'return_type': '*mut filename'}`

### Rust Evidence

- Graph edges: `1`

## W-000258 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: guard_bio_eod
- Explanation: guard_bio_eod changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000259 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iget5_locked_rcu
- Explanation: iget5_locked_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000260 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: in_group_or_capable
- Explanation: in_group_or_capable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000261 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inc_diskseq
- Explanation: inc_diskseq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000262 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: indir_configured
- Explanation: indir_configured changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000263 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inner_protocol_type
- Explanation: inner_protocol_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(7usize, 1u8) as u8) } } #[inline] pub fn set_inner_protocol_type(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(8usize, 1u8) as u8) } } #[inline] pub fn set_inner_protocol_type(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000264 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: invalidate_bdev
- Explanation: invalidate_bdev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000265 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: invalidate_disk
- Explanation: invalidate_disk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000266 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iocb_bio_iopoll
- Explanation: iocb_bio_iopoll changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000267 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kblockd_mod_delayed_work_on
- Explanation: kblockd_mod_delayed_work_on changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000268 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kblockd_schedule_work
- Explanation: kblockd_schedule_work changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000269 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: key_configured
- Explanation: key_configured changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000277 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmem_buckets_create
- Explanation: kmem_buckets_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000278 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ktime_real_to_base_clock
- Explanation: ktime_real_to_base_clock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000279 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_kfree_const
- Explanation: kunit_kfree_const changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000280 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_kstrdup_const
- Explanation: kunit_kstrdup_const changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000281 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_vm_mmap
- Explanation: kunit_vm_mmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000284 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: l4_hash
- Explanation: l4_hash changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(8usize, 1u8) as u8) } } #[inline] pub fn set_l4_hash(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(9usize, 1u8) as u8) } } #[inline] pub fn set_l4_hash(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000285 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_get_color_name
- Explanation: led_get_color_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000286 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_mc_set_brightness
- Explanation: led_mc_set_brightness changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000287 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_mc_trigger_event
- Explanation: led_mc_trigger_event changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000288 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lookup_bdev
- Explanation: lookup_bdev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000289 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: match_devname_and_update_preferred_console
- Explanation: match_devname_and_update_preferred_console changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000290 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdio_device_bus_match
- Explanation: mdio_device_bus_match changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'dev', 'type': '*mut device'}, {'name': 'drv', 'type': '*mut device_driver'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'dev', 'type': '*mut device'}, {'name': 'drv', 'type': '*const device_driver'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000291 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: memfd_pin_folios
- Explanation: memfd_pin_folios changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000292 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: memmap_boot_pages_add
- Explanation: memmap_boot_pages_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000293 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: memmap_pages_add
- Explanation: memmap_pages_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000294 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_alloc_noprof
- Explanation: mempool_alloc_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000295 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_alloc_pages
- Explanation: mempool_alloc_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000296 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_alloc_preallocated
- Explanation: mempool_alloc_preallocated changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000297 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_alloc_slab
- Explanation: mempool_alloc_slab changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000299 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_create_node_noprof
- Explanation: mempool_create_node_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000300 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_destroy
- Explanation: mempool_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000301 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_exit
- Explanation: mempool_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000303 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_free_pages
- Explanation: mempool_free_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000304 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_free_slab
- Explanation: mempool_free_slab changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000305 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_init_node
- Explanation: mempool_init_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000306 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_init_noprof
- Explanation: mempool_init_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000307 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_kfree
- Explanation: mempool_kfree changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000308 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_kmalloc
- Explanation: mempool_kmalloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000309 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_kvfree
- Explanation: mempool_kvfree changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000310 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_kvmalloc
- Explanation: mempool_kvmalloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000311 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_resize
- Explanation: mempool_resize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000312 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmap_min_addr_handler
- Explanation: mmap_min_addr_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'table', 'type': '*mut ctl_table'}, {'name': 'write', 'type': 'core::ffi::c_int'}, {'name': 'buffer', 'type': '*mut core::ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'table', 'type': '*const ctl_table'}, {'name': 'write', 'type': 'core::ffi::c_int'}, {'name': 'buffer', 'type': '*mut core::ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000313 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: module_fw_flash_in_progress
- Explanation: module_fw_flash_in_progress changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000315 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ndisc_nodetype
- Explanation: ndisc_nodetype changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(16usize, 2u8) as u8) } } #[inline] pub fn set_ndisc_nodetype(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(17usize, 2u8) as u8) } } #[inline] pub fn set_ndisc_nodetype(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000316 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_bitfield_1
- Explanation: new_bitfield_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'is_c45', 'type': 'core::ffi::c_uint'}, {'name': 'is_internal', 'type': 'core::ffi::c_uint'}, {'name': 'is_pseudo_fixed_link', 'type': 'core::ffi::c_uint'}, {'name': 'is_gigabit_capable', 'type': 'core::ffi::c_uint'}, {'name': 'has_fixups', 'type': 'core::ffi::c_uint'}, {'name': 'suspended', 'type': 'core::ffi::c_uint'}, {'name': 'suspended_by_mdio_bus', 'type': 'core::ffi::c_uint'}, {'name': 'sysfs_links', 'type': 'core::ffi::c_uint'}, {'name': 'loopback_enabled', 'type': 'core::ffi::c_uint'}, {'name': 'downshifted_rate', 'type': 'core::ffi::c_uint'}, {'name': 'is_on_sfp_module', 'type': 'core::ffi::c_uint'}, {'name': 'mac_managed_pm', 'type': 'core::ffi::c_uint'}, {'name': 'wol_enabled', 'type': 'core::ffi::c_uint'}, {'name': 'autoneg', 'type': 'core::ffi::c_uint'}, {'name': 'link', 'type': 'core::ffi::c_uint'}, {'name': 'autoneg_complete', 'type': 'core::ffi::c_uint'}, {'name': 'interrupts', 'type': 'core::ffi::c_uint'}, {'name': 'irq_suspended', 'type': 'core::ffi::c_uint'}, {'name': 'irq_rerun', 'type': 'core::ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`
- New: `{'params': [{'name': 'is_c45', 'type': 'core::ffi::c_uint'}, {'name': 'is_internal', 'type': 'core::ffi::c_uint'}, {'name': 'is_pseudo_fixed_link', 'type': 'core::ffi::c_uint'}, {'name': 'is_gigabit_capable', 'type': 'core::ffi::c_uint'}, {'name': 'has_fixups', 'type': 'core::ffi::c_uint'}, {'name': 'suspended', 'type': 'core::ffi::c_uint'}, {'name': 'suspended_by_mdio_bus', 'type': 'core::ffi::c_uint'}, {'name': 'sysfs_links', 'type': 'core::ffi::c_uint'}, {'name': 'loopback_enabled', 'type': 'core::ffi::c_uint'}, {'name': 'downshifted_rate', 'type': 'core::ffi::c_uint'}, {'name': 'is_on_sfp_module', 'type': 'core::ffi::c_uint'}, {'name': 'mac_managed_pm', 'type': 'core::ffi::c_uint'}, {'name': 'wol_enabled', 'type': 'core::ffi::c_uint'}, {'name': 'autoneg', 'type': 'core::ffi::c_uint'}, {'name': 'link', 'type': 'core::ffi::c_uint'}, {'name': 'autoneg_complete', 'type': 'core::ffi::c_uint'}, {'name': 'interrupts', 'type': 'core::ffi::c_uint'}, {'name': 'irq_suspended', 'type': 'core::ffi::c_uint'}, {'name': 'irq_rerun', 'type': 'core::ffi::c_uint'}, {'name': 'default_timestamp', 'type': 'core::ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`

### Rust Evidence

- Graph edges: `1`

## W-000317 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_bitfield_2
- Explanation: new_bitfield_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'mono_delivery_time', 'type': '__u8'}, {'name': 'tc_at_ingress', 'type': '__u8'}, {'name': 'tc_skip_classify', 'type': '__u8'}, {'name': 'remcsum_offload', 'type': '__u8'}, {'name': 'csum_complete_sw', 'type': '__u8'}, {'name': 'csum_level', 'type': '__u8'}, {'name': 'inner_protocol_type', 'type': '__u8'}, {'name': 'l4_hash', 'type': '__u8'}, {'name': 'sw_hash', 'type': '__u8'}, {'name': 'wifi_acked_valid', 'type': '__u8'}, {'name': 'wifi_acked', 'type': '__u8'}, {'name': 'no_fcs', 'type': '__u8'}, {'name': 'encapsulation', 'type': '__u8'}, {'name': 'encap_hdr_csum', 'type': '__u8'}, {'name': 'csum_valid', 'type': '__u8'}, {'name': 'ndisc_nodetype', 'type': '__u8'}, {'name': 'redirected', 'type': '__u8'}, {'name': 'nf_skip_egress', 'type': '__u8'}, {'name': 'slow_gro', 'type': '__u8'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`
- New: `{'params': [{'name': 'tstamp_type', 'type': '__u8'}, {'name': 'tc_at_ingress', 'type': '__u8'}, {'name': 'tc_skip_classify', 'type': '__u8'}, {'name': 'remcsum_offload', 'type': '__u8'}, {'name': 'csum_complete_sw', 'type': '__u8'}, {'name': 'csum_level', 'type': '__u8'}, {'name': 'inner_protocol_type', 'type': '__u8'}, {'name': 'l4_hash', 'type': '__u8'}, {'name': 'sw_hash', 'type': '__u8'}, {'name': 'wifi_acked_valid', 'type': '__u8'}, {'name': 'wifi_acked', 'type': '__u8'}, {'name': 'no_fcs', 'type': '__u8'}, {'name': 'encapsulation', 'type': '__u8'}, {'name': 'encap_hdr_csum', 'type': '__u8'}, {'name': 'csum_valid', 'type': '__u8'}, {'name': 'ndisc_nodetype', 'type': '__u8'}, {'name': 'redirected', 'type': '__u8'}, {'name': 'nf_skip_egress', 'type': '__u8'}, {'name': 'slow_gro', 'type': '__u8'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`

### Rust Evidence

- Graph edges: `1`

## W-000318 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: nf_skip_egress
- Explanation: nf_skip_egress changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(19usize, 1u8) as u8) } } #[inline] pub fn set_nf_skip_egress(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(20usize, 1u8) as u8) } } #[inline] pub fn set_nf_skip_egress(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000319 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_fcs
- Explanation: no_fcs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(12usize, 1u8) as u8) } } #[inline] pub fn set_no_fcs(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(13usize, 1u8) as u8) } } #[inline] pub fn set_no_fcs(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000320 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: nr_blockdev_pages
- Explanation: nr_blockdev_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000321 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: overcommit_kbytes_handler
- Explanation: overcommit_kbytes_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*const ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000322 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: overcommit_policy_handler
- Explanation: overcommit_policy_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*const ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000323 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: overcommit_ratio_handler
- Explanation: overcommit_ratio_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*const ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000324 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: page_counter_calculate_protection
- Explanation: page_counter_calculate_protection changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000325 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: part_devt
- Explanation: part_devt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000326 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: print_tainted_verbose
- Explanation: print_tainted_verbose changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000327 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: printk_all_partitions
- Explanation: printk_all_partitions changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000328 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_do_large_bitmap
- Explanation: proc_do_large_bitmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*const ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000329 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_do_static_key
- Explanation: proc_do_static_key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'table', 'type': '*mut ctl_table'}, {'name': 'write', 'type': 'core::ffi::c_int'}, {'name': 'buffer', 'type': '*mut core::ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'table', 'type': '*const ctl_table'}, {'name': 'write', 'type': 'core::ffi::c_int'}, {'name': 'buffer', 'type': '*mut core::ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000330 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_dobool
- Explanation: proc_dobool changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'table', 'type': '*mut ctl_table'}, {'name': 'write', 'type': 'core::ffi::c_int'}, {'name': 'buffer', 'type': '*mut core::ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'table', 'type': '*const ctl_table'}, {'name': 'write', 'type': 'core::ffi::c_int'}, {'name': 'buffer', 'type': '*mut core::ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000332 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_dointvec_jiffies
- Explanation: proc_dointvec_jiffies changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*const ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000333 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_dointvec_minmax
- Explanation: proc_dointvec_minmax changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*const ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000335 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_dointvec_ms_jiffies_minmax
- Explanation: proc_dointvec_ms_jiffies_minmax changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'table', 'type': '*mut ctl_table'}, {'name': 'write', 'type': 'core::ffi::c_int'}, {'name': 'buffer', 'type': '*mut core::ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'table', 'type': '*const ctl_table'}, {'name': 'write', 'type': 'core::ffi::c_int'}, {'name': 'buffer', 'type': '*mut core::ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000336 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_dointvec_userhz_jiffies
- Explanation: proc_dointvec_userhz_jiffies changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*const ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000337 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_dostring
- Explanation: proc_dostring changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*const ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000338 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_dou8vec_minmax
- Explanation: proc_dou8vec_minmax changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'table', 'type': '*mut ctl_table'}, {'name': 'write', 'type': 'core::ffi::c_int'}, {'name': 'buffer', 'type': '*mut core::ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'table', 'type': '*const ctl_table'}, {'name': 'write', 'type': 'core::ffi::c_int'}, {'name': 'buffer', 'type': '*mut core::ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000340 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_douintvec_minmax
- Explanation: proc_douintvec_minmax changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'table', 'type': '*mut ctl_table'}, {'name': 'write', 'type': 'core::ffi::c_int'}, {'name': 'buffer', 'type': '*mut core::ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'table', 'type': '*const ctl_table'}, {'name': 'write', 'type': 'core::ffi::c_int'}, {'name': 'buffer', 'type': '*mut core::ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000341 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_doulongvec_minmax
- Explanation: proc_doulongvec_minmax changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*const ctl_table'}, {'name': 'arg2', 'type': 'core::ffi::c_int'}, {'name': 'arg3', 'type': '*mut core::ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000342 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_doulongvec_ms_jiffies_minmax
- Explanation: proc_doulongvec_ms_jiffies_minmax changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'table', 'type': '*mut ctl_table'}, {'name': 'arg1', 'type': 'core::ffi::c_int'}, {'name': 'arg2', 'type': '*mut core::ffi::c_void'}, {'name': 'arg3', 'type': '*mut usize'}, {'name': 'arg4', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'table', 'type': '*const ctl_table'}, {'name': 'arg1', 'type': 'core::ffi::c_int'}, {'name': 'arg2', 'type': '*mut core::ffi::c_void'}, {'name': 'arg3', 'type': '*mut usize'}, {'name': 'arg4', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000343 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: put_disk
- Explanation: put_disk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000344 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: queue_limits_commit_update
- Explanation: queue_limits_commit_update changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000345 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: queue_limits_set
- Explanation: queue_limits_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000346 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: queue_limits_stack_bdev
- Explanation: queue_limits_stack_bdev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000347 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rand_initialize_disk
- Explanation: rand_initialize_disk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000348 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: redirected
- Explanation: redirected changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(18usize, 1u8) as u8) } } #[inline] pub fn set_redirected(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(19usize, 1u8) as u8) } } #[inline] pub fn set_redirected(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000350 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: remcsum_offload
- Explanation: remcsum_offload changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(3usize, 1u8) as u8) } } #[inline] pub fn set_remcsum_offload(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(4usize, 1u8) as u8) } } #[inline] pub fn set_remcsum_offload(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000356 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: reserve_mem_find_by_name
- Explanation: reserve_mem_find_by_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000357 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sbitmap_add_wait_queue
- Explanation: sbitmap_add_wait_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000358 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sbitmap_any_bit_set
- Explanation: sbitmap_any_bit_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000359 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sbitmap_bitmap_show
- Explanation: sbitmap_bitmap_show changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000360 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sbitmap_del_wait_queue
- Explanation: sbitmap_del_wait_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000361 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sbitmap_finish_wait
- Explanation: sbitmap_finish_wait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000363 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sbitmap_get_shallow
- Explanation: sbitmap_get_shallow changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000364 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sbitmap_init_node
- Explanation: sbitmap_init_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000365 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sbitmap_prepare_to_wait
- Explanation: sbitmap_prepare_to_wait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000367 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sbitmap_queue_clear_batch
- Explanation: sbitmap_queue_clear_batch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000368 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sbitmap_queue_get_shallow
- Explanation: sbitmap_queue_get_shallow changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000369 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sbitmap_queue_init_node
- Explanation: sbitmap_queue_init_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000370 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sbitmap_queue_min_shallow_depth
- Explanation: sbitmap_queue_min_shallow_depth changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000371 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sbitmap_queue_recalculate_wake_batch
- Explanation: sbitmap_queue_recalculate_wake_batch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000372 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sbitmap_queue_resize
- Explanation: sbitmap_queue_resize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000373 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sbitmap_queue_show
- Explanation: sbitmap_queue_show changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000374 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sbitmap_queue_wake_all
- Explanation: sbitmap_queue_wake_all changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000375 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sbitmap_queue_wake_up
- Explanation: sbitmap_queue_wake_up changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000376 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sbitmap_resize
- Explanation: sbitmap_resize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000377 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sbitmap_show
- Explanation: sbitmap_show changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000378 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sbitmap_weight
- Explanation: sbitmap_weight changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000379 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_blocksize
- Explanation: set_blocksize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000381 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_capacity_and_notify
- Explanation: set_capacity_and_notify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000382 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_disk_ro
- Explanation: set_disk_ro changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000383 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sk_skb_reason_drop
- Explanation: sk_skb_reason_drop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000384 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: slow_gro
- Explanation: slow_gro changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(20usize, 1u8) as u8) } } #[inline] pub fn set_slow_gro(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(21usize, 1u8) as u8) } } #[inline] pub fn set_slow_gro(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000386 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: submit_bio_noacct
- Explanation: submit_bio_noacct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000387 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: submit_bio_wait
- Explanation: submit_bio_wait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000388 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sw_hash
- Explanation: sw_hash changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(9usize, 1u8) as u8) } } #[inline] pub fn set_sw_hash(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(10usize, 1u8) as u8) } } #[inline] pub fn set_sw_hash(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000389 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sync_bdevs
- Explanation: sync_bdevs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000391 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sync_blockdev_nowait
- Explanation: sync_blockdev_nowait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000392 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sync_blockdev_range
- Explanation: sync_blockdev_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000393 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysctl_max_threads
- Explanation: sysctl_max_threads changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'table', 'type': '*mut ctl_table'}, {'name': 'write', 'type': 'core::ffi::c_int'}, {'name': 'buffer', 'type': '*mut core::ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'table', 'type': '*const ctl_table'}, {'name': 'write', 'type': 'core::ffi::c_int'}, {'name': 'buffer', 'type': '*mut core::ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000394 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysctl_vm_numa_stat_handler
- Explanation: sysctl_vm_numa_stat_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'table', 'type': '*mut ctl_table'}, {'name': 'write', 'type': 'core::ffi::c_int'}, {'name': 'buffer', 'type': '*mut core::ffi::c_void'}, {'name': 'length', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'table', 'type': '*const ctl_table'}, {'name': 'write', 'type': 'core::ffi::c_int'}, {'name': 'buffer', 'type': '*mut core::ffi::c_void'}, {'name': 'length', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000396 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: tc_skip_classify
- Explanation: tc_skip_classify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(2usize, 1u8) as u8) } } #[inline] pub fn set_tc_skip_classify(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(3usize, 1u8) as u8) } } #[inline] pub fn set_tc_skip_classify(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000397 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: timekeeping_clocksource_has_base
- Explanation: timekeeping_clocksource_has_base changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000400 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unpin_folios
- Explanation: unpin_folios changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000401 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unregister_blkdev
- Explanation: unregister_blkdev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000402 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: uprobe_get_trampoline_vaddr
- Explanation: uprobe_get_trampoline_vaddr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000403 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: uprobe_handle_trampoline
- Explanation: uprobe_handle_trampoline changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000404 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmstat_refresh
- Explanation: vmstat_refresh changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut ctl_table'}, {'name': 'write', 'type': 'core::ffi::c_int'}, {'name': 'buffer', 'type': '*mut core::ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*const ctl_table'}, {'name': 'write', 'type': 'core::ffi::c_int'}, {'name': 'buffer', 'type': '*mut core::ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000406 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wifi_acked_valid
- Explanation: wifi_acked_valid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(10usize, 1u8) as u8) } } #[inline] pub fn set_wifi_acked_valid(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': '__u8 { unsafe { ::core::mem::transmute(self._bitfield_2.get(11usize, 1u8) as u8) } } #[inline] pub fn set_wifi_acked_valid(&mut self, val: __u8) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000407 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: zero_fill_bio_iter
- Explanation: zero_fill_bio_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000408 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: zerocopy_fill_skb_from_iter
- Explanation: zerocopy_fill_skb_from_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000592 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kmalloc_node_noprof
- Explanation: __kmalloc_node_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['bytes', 'flags', 'node'], 'return_type': 'return'}`
- New: `{'params': ['PASS_BUCKET_PARAMS(bytes, NULL)', 'flags', 'node'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `1`

## W-000595 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_get_ts_info_by_layer
- Explanation: ethtool_get_ts_info_by_layer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct net_device *dev', 'struct ethtool_ts_info *info'], 'return_type': 'int'}`
- New: `{'params': ['struct net_device *dev', 'struct kernel_ethtool_ts_info *info'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000596 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_op_get_ts_info
- Explanation: ethtool_op_get_ts_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct net_device *dev', 'struct ethtool_ts_info *eti'], 'return_type': 'int'}`
- New: `{'params': ['struct net_device *dev', 'struct kernel_ethtool_ts_info *eti'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000597 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: huge_ptep_get
- Explanation: huge_ptep_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['pte_t *ptep'], 'return_type': 'static inline pte_t'}`
- New: `{'params': ['struct mm_struct *mm', 'unsigned long addr', 'pte_t *ptep'], 'return_type': 'static inline pte_t'}`

### Rust Evidence

- Graph edges: `1`

## W-000598 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: max_t
- Explanation: max_t changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['int', 'max_t(int, sk->sk_rcvbuf & PAGE_MASK, PAGE_SIZE) - atomic_read(&ctx->rcvused)', '0'], 'return_type': 'return'}`
- New: `{'params': ['unsigned short', 'rq->nr_phys_segments', '1'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `1`

## W-000599 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdio_device_bus_match
- Explanation: mdio_device_bus_match changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct device *dev', 'struct device_driver *drv'], 'return_type': 'int'}`
- New: `{'params': ['struct device *dev', 'const struct device_driver *drv'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000416 FieldDrift

- Risk: High
- Score: 10.6
- Symbol: bpf_struct_ops
- Explanation: bpf_struct_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'verifier_ops', 'type': '*const bpf_verifier_ops'}, {'name': 'init', 'type': '::core::option::Option<unsafe extern "C" fn(btf: *mut btf) -> core::ffi::c_int>'}, {'name': 'check_member', 'type': '::core::option::Option<'}, {'name': 'init_member', 'type': '::core::option::Option<'}, {'name': 'reg', 'type': '::core::option::Option<'}, {'name': 'unreg', 'type': '::core::option::Option<unsafe extern "C" fn(kdata: *mut core::ffi::c_void)>'}, {'name': 'update', 'type': '::core::option::Option<'}, {'name': 'validate', 'type': '::core::option::Option<'}, {'name': 'cfi_stubs', 'type': '*mut core::ffi::c_void'}, {'name': 'owner', 'type': '*mut module'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'func_models', 'type': '[btf_func_model; 64usize]'}]`
- New: `[{'name': 'verifier_ops', 'type': '*const bpf_verifier_ops'}, {'name': 'init', 'type': '::core::option::Option<unsafe extern "C" fn(btf: *mut btf) -> core::ffi::c_int>'}, {'name': 'check_member', 'type': '::core::option::Option<'}, {'name': 'init_member', 'type': '::core::option::Option<'}, {'name': 'reg', 'type': '::core::option::Option<'}, {'name': 'unreg', 'type': '::core::option::Option<'}, {'name': 'update', 'type': '::core::option::Option<'}, {'name': 'validate', 'type': '::core::option::Option<'}, {'name': 'cfi_stubs', 'type': '*mut core::ffi::c_void'}, {'name': 'owner', 'type': '*mut module'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'func_models', 'type': '[btf_func_model; 64usize]'}]`

### Rust Evidence

- Graph edges: `10`

## W-000434 FieldDrift

- Risk: High
- Score: 10.4
- Symbol: task_struct
- Explanation: task_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'core::ffi::c_uint'}, {'name': 'saved_state', 'type': 'core::ffi::c_uint'}, {'name': 'stack', 'type': '*mut core::ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'ptrace', 'type': 'core::ffi::c_uint'}, {'name': 'on_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'core::ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'core::ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_cpu', 'type': 'core::ffi::c_int'}, {'name': 'on_rq', 'type': 'core::ffi::c_int'}, {'name': 'prio', 'type': 'core::ffi::c_int'}, {'name': 'static_prio', 'type': 'core::ffi::c_int'}, {'name': 'normal_prio', 'type': 'core::ffi::c_int'}, {'name': 'rt_priority', 'type': 'core::ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'dl_server', 'type': '*mut sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'core::ffi::c_uint'}, {'name': 'policy', 'type': 'core::ffi::c_uint'}, {'name': 'max_allowed_capacity', 'type': 'core::ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'core::ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut core::ffi::c_void'}, {'name': 'migration_disabled', 'type': 'core::ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'core::ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'core::ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'core::ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'rcu_tasks_exit_cpu', 'type': 'core::ffi::c_int'}, {'name': 'rcu_tasks_exit_list', 'type': 'list_head'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'faults_disabled_mapping', 'type': '*mut address_space'}, {'name': 'exit_state', 'type': 'core::ffi::c_int'}, {'name': 'exit_code', 'type': 'core::ffi::c_int'}, {'name': 'exit_signal', 'type': 'core::ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'core::ffi::c_int'}, {'name': 'jobctl', 'type': 'core::ffi::c_ulong'}, {'name': 'personality', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'core::ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'worker_private', 'type': '*mut core::ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[core::ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'core::ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'core::ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'core::ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'journal_info', 'type': '*mut core::ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'core::ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cpuset_slab_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'core::ffi::c_uint'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'core::ffi::c_short'}, {'name': 'il_weight', 'type': 'u8_'}, {'name': 'pref_node_fork', 'type': 'core::ffi::c_short'}, {'name': 'rseq', 'type': '*mut rseq'}, {'name': 'rseq_len', 'type': 'u32_'}, {'name': 'rseq_sig', 'type': 'u32_'}, {'name': 'rseq_event_mask', 'type': 'core::ffi::c_ulong'}, {'name': 'mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'last_mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'migrate_from_cpu', 'type': 'core::ffi::c_int'}, {'name': 'mm_cid_active', 'type': 'core::ffi::c_int'}, {'name': 'cid_work', 'type': 'callback_head'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'core::ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'core::ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'core::ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'core::ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'core::ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_vaddr', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'core::ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': '__bindgen_padding_1', 'type': '[u64; 6usize]'}, {'name': 'thread', 'type': 'thread_struct'}]`
- New: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'core::ffi::c_uint'}, {'name': 'saved_state', 'type': 'core::ffi::c_uint'}, {'name': 'stack', 'type': '*mut core::ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'ptrace', 'type': 'core::ffi::c_uint'}, {'name': 'on_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'core::ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'core::ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_cpu', 'type': 'core::ffi::c_int'}, {'name': 'on_rq', 'type': 'core::ffi::c_int'}, {'name': 'prio', 'type': 'core::ffi::c_int'}, {'name': 'static_prio', 'type': 'core::ffi::c_int'}, {'name': 'normal_prio', 'type': 'core::ffi::c_int'}, {'name': 'rt_priority', 'type': 'core::ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'dl_server', 'type': '*mut sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'core::ffi::c_uint'}, {'name': 'policy', 'type': 'core::ffi::c_uint'}, {'name': 'max_allowed_capacity', 'type': 'core::ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'core::ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut core::ffi::c_void'}, {'name': 'migration_disabled', 'type': 'core::ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'core::ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'core::ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'core::ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'rcu_tasks_exit_cpu', 'type': 'core::ffi::c_int'}, {'name': 'rcu_tasks_exit_list', 'type': 'list_head'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'faults_disabled_mapping', 'type': '*mut address_space'}, {'name': 'exit_state', 'type': 'core::ffi::c_int'}, {'name': 'exit_code', 'type': 'core::ffi::c_int'}, {'name': 'exit_signal', 'type': 'core::ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'core::ffi::c_int'}, {'name': 'jobctl', 'type': 'core::ffi::c_ulong'}, {'name': 'personality', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'core::ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'worker_private', 'type': '*mut core::ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[core::ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'core::ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'core::ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'core::ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'journal_info', 'type': '*mut core::ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'core::ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cpuset_slab_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'core::ffi::c_uint'}, {'name': 'perf_recursion', 'type': '[u8_; 4usize]'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'core::ffi::c_short'}, {'name': 'il_weight', 'type': 'u8_'}, {'name': 'pref_node_fork', 'type': 'core::ffi::c_short'}, {'name': 'rseq', 'type': '*mut rseq'}, {'name': 'rseq_len', 'type': 'u32_'}, {'name': 'rseq_sig', 'type': 'u32_'}, {'name': 'rseq_event_mask', 'type': 'core::ffi::c_ulong'}, {'name': 'mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'last_mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'migrate_from_cpu', 'type': 'core::ffi::c_int'}, {'name': 'mm_cid_active', 'type': 'core::ffi::c_int'}, {'name': 'cid_work', 'type': 'callback_head'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'core::ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'core::ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'core::ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'core::ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'core::ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut core::ffi::c_void'}, {'name': 'bpf_net_context', 'type': '*mut bpf_net_context'}, {'name': 'mce_vaddr', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'core::ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': '__bindgen_padding_1', 'type': '[u64; 5usize]'}, {'name': 'thread', 'type': 'thread_struct'}]`

### Rust Evidence

- Graph edges: `9`

## W-000419 FieldDrift

- Risk: High
- Score: 10.2
- Symbol: dentry
- Explanation: dentry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'd_flags', 'type': 'core::ffi::c_uint'}, {'name': 'd_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'd_hash', 'type': 'hlist_bl_node'}, {'name': 'd_parent', 'type': '*mut dentry'}, {'name': 'd_name', 'type': 'qstr'}, {'name': 'd_inode', 'type': '*mut inode'}, {'name': 'd_iname', 'type': '[core::ffi::c_uchar; 40usize]'}, {'name': 'd_lockref', 'type': 'lockref'}, {'name': 'd_op', 'type': '*const dentry_operations'}, {'name': 'd_sb', 'type': '*mut super_block'}, {'name': 'd_time', 'type': 'core::ffi::c_ulong'}, {'name': 'd_fsdata', 'type': '*mut core::ffi::c_void'}, {'name': '__bindgen_anon_1', 'type': 'dentry__bindgen_ty_1'}, {'name': 'd_sib', 'type': 'hlist_node'}, {'name': 'd_children', 'type': 'hlist_head'}, {'name': 'd_u', 'type': 'dentry__bindgen_ty_2'}]`
- New: `[{'name': 'd_flags', 'type': 'core::ffi::c_uint'}, {'name': 'd_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'd_hash', 'type': 'hlist_bl_node'}, {'name': 'd_parent', 'type': '*mut dentry'}, {'name': 'd_name', 'type': 'qstr'}, {'name': 'd_inode', 'type': '*mut inode'}, {'name': 'd_iname', 'type': '[core::ffi::c_uchar; 40usize]'}, {'name': 'd_op', 'type': '*const dentry_operations'}, {'name': 'd_sb', 'type': '*mut super_block'}, {'name': 'd_time', 'type': 'core::ffi::c_ulong'}, {'name': 'd_fsdata', 'type': '*mut core::ffi::c_void'}, {'name': 'd_lockref', 'type': 'lockref'}, {'name': '__bindgen_anon_1', 'type': 'dentry__bindgen_ty_1'}, {'name': 'd_sib', 'type': 'hlist_node'}, {'name': 'd_children', 'type': 'hlist_head'}, {'name': 'd_u', 'type': 'dentry__bindgen_ty_2'}]`

### Rust Evidence

- Graph edges: `8`

## W-000417 FieldDrift

- Risk: High
- Score: 10.0
- Symbol: cftype
- Explanation: cftype changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'name', 'type': '[core::ffi::c_char; 64usize]'}, {'name': 'private', 'type': 'core::ffi::c_ulong'}, {'name': 'max_write_len', 'type': 'usize'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'file_offset', 'type': 'core::ffi::c_uint'}, {'name': 'ss', 'type': '*mut cgroup_subsys'}, {'name': 'node', 'type': 'list_head'}, {'name': 'kf_ops', 'type': '*mut kernfs_ops'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(of: *mut kernfs_open_file)>'}, {'name': 'read_u64', 'type': '::core::option::Option<'}, {'name': 'read_s64', 'type': '::core::option::Option<'}, {'name': 'seq_show', 'type': '::core::option::Option<'}, {'name': 'seq_start', 'type': '::core::option::Option<'}, {'name': 'seq_next', 'type': '::core::option::Option<'}, {'name': 'write_u64', 'type': '::core::option::Option<'}, {'name': 'write_s64', 'type': '::core::option::Option<'}, {'name': 'write', 'type': '::core::option::Option<'}, {'name': 'poll', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'name', 'type': '[core::ffi::c_char; 64usize]'}, {'name': 'private', 'type': 'core::ffi::c_ulong'}, {'name': 'max_write_len', 'type': 'usize'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'file_offset', 'type': 'core::ffi::c_uint'}, {'name': 'ss', 'type': '*mut cgroup_subsys'}, {'name': 'node', 'type': 'list_head'}, {'name': 'kf_ops', 'type': '*mut kernfs_ops'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(of: *mut kernfs_open_file)>'}, {'name': 'read_u64', 'type': '::core::option::Option<'}, {'name': 'read_s64', 'type': '::core::option::Option<'}, {'name': 'seq_show', 'type': '::core::option::Option<'}, {'name': 'seq_start', 'type': '::core::option::Option<'}, {'name': 'seq_next', 'type': '::core::option::Option<'}, {'name': 'write_u64', 'type': '::core::option::Option<'}, {'name': 'write_s64', 'type': '::core::option::Option<'}, {'name': 'write', 'type': '::core::option::Option<'}, {'name': 'poll', 'type': '::core::option::Option<'}, {'name': 'lockdep_key', 'type': 'lock_class_key'}]`

### Rust Evidence

- Graph edges: `7`

## W-000424 FieldDrift

- Risk: High
- Score: 10.0
- Symbol: io_comp_batch
- Explanation: io_comp_batch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'req_list', 'type': '*mut request'}, {'name': 'need_ts', 'type': 'bool_'}, {'name': 'complete', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut io_comp_batch)>'}]`

### Rust Evidence

- Graph edges: `7`

## W-000426 FieldDrift

- Risk: High
- Score: 10.0
- Symbol: kstat
- Explanation: kstat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'result_mask', 'type': 'u32_'}, {'name': 'mode', 'type': 'umode_t'}, {'name': 'nlink', 'type': 'core::ffi::c_uint'}, {'name': 'blksize', 'type': 'u32'}, {'name': 'attributes', 'type': 'u64_'}, {'name': 'attributes_mask', 'type': 'u64_'}, {'name': 'ino', 'type': 'u64_'}, {'name': 'dev', 'type': 'dev_t'}, {'name': 'rdev', 'type': 'dev_t'}, {'name': 'uid', 'type': 'kuid_t'}, {'name': 'gid', 'type': 'kgid_t'}, {'name': 'size', 'type': 'loff_t'}, {'name': 'atime', 'type': 'timespec64'}, {'name': 'mtime', 'type': 'timespec64'}, {'name': 'ctime', 'type': 'timespec64'}, {'name': 'btime', 'type': 'timespec64'}, {'name': 'blocks', 'type': 'u64_'}, {'name': 'mnt_id', 'type': 'u64_'}, {'name': 'dio_mem_align', 'type': 'u32_'}, {'name': 'dio_offset_align', 'type': 'u32_'}, {'name': 'change_cookie', 'type': 'u64_'}, {'name': 'subvol', 'type': 'u64_'}]`
- New: `[{'name': 'result_mask', 'type': 'u32_'}, {'name': 'mode', 'type': 'umode_t'}, {'name': 'nlink', 'type': 'core::ffi::c_uint'}, {'name': 'blksize', 'type': 'u32'}, {'name': 'attributes', 'type': 'u64_'}, {'name': 'attributes_mask', 'type': 'u64_'}, {'name': 'ino', 'type': 'u64_'}, {'name': 'dev', 'type': 'dev_t'}, {'name': 'rdev', 'type': 'dev_t'}, {'name': 'uid', 'type': 'kuid_t'}, {'name': 'gid', 'type': 'kgid_t'}, {'name': 'size', 'type': 'loff_t'}, {'name': 'atime', 'type': 'timespec64'}, {'name': 'mtime', 'type': 'timespec64'}, {'name': 'ctime', 'type': 'timespec64'}, {'name': 'btime', 'type': 'timespec64'}, {'name': 'blocks', 'type': 'u64_'}, {'name': 'mnt_id', 'type': 'u64_'}, {'name': 'dio_mem_align', 'type': 'u32_'}, {'name': 'dio_offset_align', 'type': 'u32_'}, {'name': 'change_cookie', 'type': 'u64_'}, {'name': 'subvol', 'type': 'u64_'}, {'name': 'atomic_write_unit_min', 'type': 'u32_'}, {'name': 'atomic_write_unit_max', 'type': 'u32_'}, {'name': 'atomic_write_segments_max', 'type': 'u32_'}]`

### Rust Evidence

- Graph edges: `7`

## W-000020 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __page_file_index
- Explanation: __page_file_index changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000033 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: amd_clear_divider
- Explanation: amd_clear_divider changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000205 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: clear_huge_page
- Explanation: clear_huge_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000206 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: console_replay_all
- Explanation: console_replay_all changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000208 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: convert_art_ns_to_tsc
- Explanation: convert_art_ns_to_tsc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000209 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: convert_art_to_tsc
- Explanation: convert_art_to_tsc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000241 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: exit_tasks_rcu_stop
- Explanation: exit_tasks_rcu_stop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000270 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: kfree_skb_reason
- Explanation: kfree_skb_reason changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000271 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: kmalloc_large_node_noprof
- Explanation: kmalloc_large_node_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000272 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: kmalloc_large_noprof
- Explanation: kmalloc_large_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000273 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: kmalloc_node_trace_noprof
- Explanation: kmalloc_node_trace_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000274 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: kmalloc_node_track_caller_noprof
- Explanation: kmalloc_node_track_caller_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000275 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: kmalloc_trace_noprof
- Explanation: kmalloc_trace_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000283 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: kvmalloc_node_noprof
- Explanation: kvmalloc_node_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000314 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mono_delivery_time
- Explanation: mono_delivery_time changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000591 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: IS_ENABLED
- Explanation: IS_ENABLED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['CONFIG_PREEMPT_RT'], 'return_type': 'return'}`
- New: `{'params': ['CONFIG_BLK_DEV_ZONED) && (q->limits.features & BLK_FEAT_ZONED'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-000593 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: acpi_iommu_fwspec_init
- Explanation: acpi_iommu_fwspec_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct device *dev', 'u32 id', 'struct fwnode_handle *fwnode', 'const struct iommu_ops *ops'], 'return_type': 'int'}`
- New: `{'params': ['struct device *dev', 'u32 id', 'struct fwnode_handle *fwnode'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000594 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_buddy_block_trim
- Explanation: drm_buddy_block_trim changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_buddy *mm', 'u64 new_size', 'struct list_head *blocks'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_buddy *mm', 'u64 *start', 'u64 new_size', 'struct list_head *blocks'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000600 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_ts_info
- Explanation: phy_ts_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct phy_device *phydev', 'struct ethtool_ts_info *tsinfo'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct phy_device *phydev', 'struct kernel_ethtool_ts_info *tsinfo'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `0`

## W-000601 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: void
- Explanation: void changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['*drmres_release_t)(struct drm_device *dev, void *res'], 'return_type': 'typedef'}`
- New: `{'params': ['*blk_plug_cb_fn)(struct blk_plug_cb *, bool'], 'return_type': 'typedef'}`

### Rust Evidence

- Graph edges: `0`

## W-000414 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: block_device
- Explanation: block_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'bd_start_sect', 'type': 'sector_t'}, {'name': 'bd_nr_sectors', 'type': 'sector_t'}, {'name': 'bd_disk', 'type': '*mut gendisk'}, {'name': 'bd_queue', 'type': '*mut request_queue'}, {'name': 'bd_stats', 'type': '*mut disk_stats'}, {'name': 'bd_stamp', 'type': 'core::ffi::c_ulong'}, {'name': '__bd_flags', 'type': 'atomic_t'}, {'name': 'bd_dev', 'type': 'dev_t'}, {'name': 'bd_mapping', 'type': '*mut address_space'}, {'name': 'bd_openers', 'type': 'atomic_t'}, {'name': 'bd_size_lock', 'type': 'spinlock_t'}, {'name': 'bd_claiming', 'type': '*mut core::ffi::c_void'}, {'name': 'bd_holder', 'type': '*mut core::ffi::c_void'}, {'name': 'bd_holder_ops', 'type': '*mut blk_holder_ops'}, {'name': 'bd_holder_lock', 'type': 'mutex'}, {'name': 'bd_holders', 'type': 'core::ffi::c_int'}, {'name': 'bd_holder_dir', 'type': '*mut kobject'}, {'name': 'bd_fsfreeze_count', 'type': 'atomic_t'}, {'name': 'bd_fsfreeze_mutex', 'type': 'mutex'}, {'name': 'bd_meta_info', 'type': '*mut partition_meta_info'}, {'name': 'bd_writers', 'type': 'core::ffi::c_int'}, {'name': 'bd_device', 'type': 'device'}]`
- New: `[{'name': 'bd_start_sect', 'type': 'sector_t'}, {'name': 'bd_nr_sectors', 'type': 'sector_t'}, {'name': 'bd_disk', 'type': '*mut gendisk'}, {'name': 'bd_queue', 'type': '*mut request_queue'}, {'name': 'bd_stats', 'type': '*mut disk_stats'}, {'name': 'bd_stamp', 'type': 'core::ffi::c_ulong'}, {'name': '__bd_flags', 'type': 'atomic_t'}, {'name': 'bd_dev', 'type': 'dev_t'}, {'name': 'bd_mapping', 'type': '*mut address_space'}, {'name': 'bd_openers', 'type': 'atomic_t'}, {'name': 'bd_size_lock', 'type': 'spinlock_t'}, {'name': 'bd_claiming', 'type': '*mut core::ffi::c_void'}, {'name': 'bd_holder', 'type': '*mut core::ffi::c_void'}, {'name': 'bd_holder_ops', 'type': '*const blk_holder_ops'}, {'name': 'bd_holder_lock', 'type': 'mutex'}, {'name': 'bd_holders', 'type': 'core::ffi::c_int'}, {'name': 'bd_holder_dir', 'type': '*mut kobject'}, {'name': 'bd_fsfreeze_count', 'type': 'atomic_t'}, {'name': 'bd_fsfreeze_mutex', 'type': 'mutex'}, {'name': 'bd_meta_info', 'type': '*mut partition_meta_info'}, {'name': 'bd_writers', 'type': 'core::ffi::c_int'}, {'name': 'bd_device', 'type': 'device'}]`

### Rust Evidence

- Graph edges: `3`

## W-000428 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: partition_meta_info
- Explanation: partition_meta_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[{'name': 'uuid', 'type': '[core::ffi::c_char; 37usize]'}, {'name': 'volname', 'type': '[u8_; 64usize]'}]`

### Rust Evidence

- Graph edges: `3`

## W-000433 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: taint_flag
- Explanation: taint_flag changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'c_true', 'type': 'core::ffi::c_char'}, {'name': 'c_false', 'type': 'core::ffi::c_char'}, {'name': 'module', 'type': 'bool_'}]`
- New: `[{'name': 'c_true', 'type': 'core::ffi::c_char'}, {'name': 'c_false', 'type': 'core::ffi::c_char'}, {'name': 'module', 'type': 'bool_'}, {'name': 'desc', 'type': '*const core::ffi::c_char'}]`

### Rust Evidence

- Graph edges: `3`

## W-000410 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: bio_set
- Explanation: bio_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'bio_slab', 'type': '*mut kmem_cache'}, {'name': 'front_pad', 'type': 'core::ffi::c_uint'}, {'name': 'cache', 'type': '*mut bio_alloc_cache'}, {'name': 'bio_pool', 'type': 'mempool_t'}, {'name': 'bvec_pool', 'type': 'mempool_t'}, {'name': 'back_pad', 'type': 'core::ffi::c_uint'}, {'name': 'rescue_lock', 'type': 'spinlock_t'}, {'name': 'rescue_list', 'type': 'bio_list'}, {'name': 'rescue_work', 'type': 'work_struct'}, {'name': 'rescue_workqueue', 'type': '*mut workqueue_struct'}, {'name': 'cpuhp_dead', 'type': 'hlist_node'}]`

### Rust Evidence

- Graph edges: `2`

## W-000412 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: blk_plug
- Explanation: blk_plug changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'mq_list', 'type': '*mut request'}, {'name': 'cached_rq', 'type': '*mut request'}, {'name': 'cur_ktime', 'type': 'u64_'}, {'name': 'nr_ios', 'type': 'core::ffi::c_ushort'}, {'name': 'rq_count', 'type': 'core::ffi::c_ushort'}, {'name': 'multiple_queues', 'type': 'bool_'}, {'name': 'has_elevator', 'type': 'bool_'}, {'name': 'cb_list', 'type': 'list_head'}]`

### Rust Evidence

- Graph edges: `2`

## W-000409 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bio_list
- Explanation: bio_list changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'head', 'type': '*mut bio'}, {'name': 'tail', 'type': '*mut bio'}]`

### Rust Evidence

- Graph edges: `1`

## W-000411 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: blk_holder_ops
- Explanation: blk_holder_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[{'name': 'sync', 'type': '::core::option::Option<unsafe extern "C" fn(bdev: *mut block_device)>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000413 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: blkcg_gq
- Explanation: blkcg_gq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[]`

### Rust Evidence

- Graph edges: `1`

## W-000415 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bpf_link_ops
- Explanation: bpf_link_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(link: *mut bpf_link)>'}, {'name': 'dealloc', 'type': '::core::option::Option<unsafe extern "C" fn(link: *mut bpf_link)>'}, {'name': 'dealloc_deferred', 'type': '::core::option::Option<unsafe extern "C" fn(link: *mut bpf_link)>'}, {'name': 'update_prog', 'type': '::core::option::Option<'}, {'name': 'fill_link_info', 'type': '::core::option::Option<'}, {'name': 'update_map', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(link: *mut bpf_link)>'}, {'name': 'dealloc', 'type': '::core::option::Option<unsafe extern "C" fn(link: *mut bpf_link)>'}, {'name': 'dealloc_deferred', 'type': '::core::option::Option<unsafe extern "C" fn(link: *mut bpf_link)>'}, {'name': 'update_prog', 'type': '::core::option::Option<'}, {'name': 'fill_link_info', 'type': '::core::option::Option<'}, {'name': 'update_map', 'type': '::core::option::Option<'}, {'name': 'poll', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-000420 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: ethtool_ops
- Explanation: ethtool_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'supported_coalesce_params', 'type': 'u32_'}, {'name': 'supported_ring_params', 'type': 'u32_'}, {'name': 'get_drvinfo', 'type': '::core::option::Option<'}, {'name': 'get_regs', 'type': '::core::option::Option<'}, {'name': 'get_wol', 'type': '::core::option::Option<'}, {'name': 'set_wol', 'type': '::core::option::Option<'}, {'name': 'get_msglevel', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'get_link', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'get_link_ext_state', 'type': '::core::option::Option<'}, {'name': 'get_link_ext_stats', 'type': '::core::option::Option<'}, {'name': 'get_eeprom', 'type': '::core::option::Option<'}, {'name': 'set_eeprom', 'type': '::core::option::Option<'}, {'name': 'get_coalesce', 'type': '::core::option::Option<'}, {'name': 'set_coalesce', 'type': '::core::option::Option<'}, {'name': 'get_ringparam', 'type': '::core::option::Option<'}, {'name': 'set_ringparam', 'type': '::core::option::Option<'}, {'name': 'get_pause_stats', 'type': '::core::option::Option<'}, {'name': 'get_pauseparam', 'type': '::core::option::Option<'}, {'name': 'set_pauseparam', 'type': '::core::option::Option<'}, {'name': 'self_test', 'type': '::core::option::Option<'}, {'name': 'get_strings', 'type': '::core::option::Option<'}, {'name': 'set_phys_id', 'type': '::core::option::Option<'}, {'name': 'get_ethtool_stats', 'type': '::core::option::Option<'}, {'name': 'complete', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device)>'}, {'name': 'get_priv_flags', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'set_priv_flags', 'type': '::core::option::Option<'}, {'name': 'get_sset_count', 'type': '::core::option::Option<'}, {'name': 'get_rxnfc', 'type': '::core::option::Option<'}, {'name': 'set_rxnfc', 'type': '::core::option::Option<'}, {'name': 'flash_device', 'type': '::core::option::Option<'}, {'name': 'reset', 'type': '::core::option::Option<'}, {'name': 'get_rxfh', 'type': '::core::option::Option<'}, {'name': 'set_rxfh', 'type': '::core::option::Option<'}, {'name': 'get_channels', 'type': '::core::option::Option<'}, {'name': 'set_channels', 'type': '::core::option::Option<'}, {'name': 'get_dump_flag', 'type': '::core::option::Option<'}, {'name': 'get_dump_data', 'type': '::core::option::Option<'}, {'name': 'set_dump', 'type': '::core::option::Option<'}, {'name': 'get_ts_info', 'type': '::core::option::Option<'}, {'name': 'get_ts_stats', 'type': '::core::option::Option<'}, {'name': 'get_module_info', 'type': '::core::option::Option<'}, {'name': 'get_module_eeprom', 'type': '::core::option::Option<'}, {'name': 'get_eee', 'type': '::core::option::Option<'}, {'name': 'set_eee', 'type': '::core::option::Option<'}, {'name': 'get_tunable', 'type': '::core::option::Option<'}, {'name': 'set_tunable', 'type': '::core::option::Option<'}, {'name': 'get_per_queue_coalesce', 'type': '::core::option::Option<'}, {'name': 'set_per_queue_coalesce', 'type': '::core::option::Option<'}, {'name': 'get_link_ksettings', 'type': '::core::option::Option<'}, {'name': 'set_link_ksettings', 'type': '::core::option::Option<'}, {'name': 'get_fec_stats', 'type': '::core::option::Option<'}, {'name': 'get_fecparam', 'type': '::core::option::Option<'}, {'name': 'set_fecparam', 'type': '::core::option::Option<'}, {'name': 'get_ethtool_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_phy_tunable', 'type': '::core::option::Option<'}, {'name': 'set_phy_tunable', 'type': '::core::option::Option<'}, {'name': 'get_module_eeprom_by_page', 'type': '::core::option::Option<'}, {'name': 'get_eth_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_eth_mac_stats', 'type': '::core::option::Option<'}, {'name': 'get_eth_ctrl_stats', 'type': '::core::option::Option<'}, {'name': 'get_rmon_stats', 'type': '::core::option::Option<'}, {'name': 'get_module_power_mode', 'type': '::core::option::Option<'}, {'name': 'set_module_power_mode', 'type': '::core::option::Option<'}, {'name': 'get_mm', 'type': '::core::option::Option<'}, {'name': 'set_mm', 'type': '::core::option::Option<'}, {'name': 'get_mm_stats', 'type': '::core::option::Option<'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rxfh_indir_space', 'type': 'u32_'}, {'name': 'rxfh_key_space', 'type': 'u16_'}, {'name': 'rxfh_priv_size', 'type': 'u16_'}, {'name': 'rxfh_max_num_contexts', 'type': 'u32_'}, {'name': 'supported_coalesce_params', 'type': 'u32_'}, {'name': 'supported_ring_params', 'type': 'u32_'}, {'name': 'get_drvinfo', 'type': '::core::option::Option<'}, {'name': 'get_regs', 'type': '::core::option::Option<'}, {'name': 'get_wol', 'type': '::core::option::Option<'}, {'name': 'set_wol', 'type': '::core::option::Option<'}, {'name': 'get_msglevel', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'get_link', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'get_link_ext_state', 'type': '::core::option::Option<'}, {'name': 'get_link_ext_stats', 'type': '::core::option::Option<'}, {'name': 'get_eeprom', 'type': '::core::option::Option<'}, {'name': 'set_eeprom', 'type': '::core::option::Option<'}, {'name': 'get_coalesce', 'type': '::core::option::Option<'}, {'name': 'set_coalesce', 'type': '::core::option::Option<'}, {'name': 'get_ringparam', 'type': '::core::option::Option<'}, {'name': 'set_ringparam', 'type': '::core::option::Option<'}, {'name': 'get_pause_stats', 'type': '::core::option::Option<'}, {'name': 'get_pauseparam', 'type': '::core::option::Option<'}, {'name': 'set_pauseparam', 'type': '::core::option::Option<'}, {'name': 'self_test', 'type': '::core::option::Option<'}, {'name': 'get_strings', 'type': '::core::option::Option<'}, {'name': 'set_phys_id', 'type': '::core::option::Option<'}, {'name': 'get_ethtool_stats', 'type': '::core::option::Option<'}, {'name': 'complete', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device)>'}, {'name': 'get_priv_flags', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'set_priv_flags', 'type': '::core::option::Option<'}, {'name': 'get_sset_count', 'type': '::core::option::Option<'}, {'name': 'get_rxnfc', 'type': '::core::option::Option<'}, {'name': 'set_rxnfc', 'type': '::core::option::Option<'}, {'name': 'flash_device', 'type': '::core::option::Option<'}, {'name': 'reset', 'type': '::core::option::Option<'}, {'name': 'get_rxfh', 'type': '::core::option::Option<'}, {'name': 'set_rxfh', 'type': '::core::option::Option<'}, {'name': 'create_rxfh_context', 'type': '::core::option::Option<'}, {'name': 'modify_rxfh_context', 'type': '::core::option::Option<'}, {'name': 'remove_rxfh_context', 'type': '::core::option::Option<'}, {'name': 'get_channels', 'type': '::core::option::Option<'}, {'name': 'set_channels', 'type': '::core::option::Option<'}, {'name': 'get_dump_flag', 'type': '::core::option::Option<'}, {'name': 'get_dump_data', 'type': '::core::option::Option<'}, {'name': 'set_dump', 'type': '::core::option::Option<'}, {'name': 'get_ts_info', 'type': '::core::option::Option<'}, {'name': 'get_ts_stats', 'type': '::core::option::Option<'}, {'name': 'get_module_info', 'type': '::core::option::Option<'}, {'name': 'get_module_eeprom', 'type': '::core::option::Option<'}, {'name': 'get_eee', 'type': '::core::option::Option<'}, {'name': 'set_eee', 'type': '::core::option::Option<'}, {'name': 'get_tunable', 'type': '::core::option::Option<'}, {'name': 'set_tunable', 'type': '::core::option::Option<'}, {'name': 'get_per_queue_coalesce', 'type': '::core::option::Option<'}, {'name': 'set_per_queue_coalesce', 'type': '::core::option::Option<'}, {'name': 'get_link_ksettings', 'type': '::core::option::Option<'}, {'name': 'set_link_ksettings', 'type': '::core::option::Option<'}, {'name': 'get_fec_stats', 'type': '::core::option::Option<'}, {'name': 'get_fecparam', 'type': '::core::option::Option<'}, {'name': 'set_fecparam', 'type': '::core::option::Option<'}, {'name': 'get_ethtool_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_phy_tunable', 'type': '::core::option::Option<'}, {'name': 'set_phy_tunable', 'type': '::core::option::Option<'}, {'name': 'get_module_eeprom_by_page', 'type': '::core::option::Option<'}, {'name': 'set_module_eeprom_by_page', 'type': '::core::option::Option<'}, {'name': 'get_eth_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_eth_mac_stats', 'type': '::core::option::Option<'}, {'name': 'get_eth_ctrl_stats', 'type': '::core::option::Option<'}, {'name': 'get_rmon_stats', 'type': '::core::option::Option<'}, {'name': 'get_module_power_mode', 'type': '::core::option::Option<'}, {'name': 'set_module_power_mode', 'type': '::core::option::Option<'}, {'name': 'get_mm', 'type': '::core::option::Option<'}, {'name': 'set_mm', 'type': '::core::option::Option<'}, {'name': 'get_mm_stats', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-000421 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: fpu_state_config
- Explanation: fpu_state_config changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'max_size', 'type': 'core::ffi::c_uint'}, {'name': 'default_size', 'type': 'core::ffi::c_uint'}, {'name': 'max_features', 'type': 'u64_'}, {'name': 'default_features', 'type': 'u64_'}, {'name': 'legacy_features', 'type': 'u64_'}]`
- New: `[{'name': 'max_size', 'type': 'core::ffi::c_uint'}, {'name': 'default_size', 'type': 'core::ffi::c_uint'}, {'name': 'max_features', 'type': 'u64_'}, {'name': 'default_features', 'type': 'u64_'}, {'name': 'legacy_features', 'type': 'u64_'}, {'name': 'independent_features', 'type': 'u64_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000425 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: kmsan_ctx
- Explanation: kmsan_ctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'cstate', 'type': 'kmsan_context_state'}, {'name': 'kmsan_in_runtime', 'type': 'core::ffi::c_int'}, {'name': 'allow_reporting', 'type': 'bool_'}]`
- New: `[{'name': 'cstate', 'type': 'kmsan_context_state'}, {'name': 'kmsan_in_runtime', 'type': 'core::ffi::c_int'}, {'name': 'depth', 'type': 'core::ffi::c_uint'}]`

### Rust Evidence

- Graph edges: `1`

## W-000427 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: netlink_kernel_cfg
- Explanation: netlink_kernel_cfg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'groups', 'type': 'core::ffi::c_uint'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'input', 'type': '::core::option::Option<unsafe extern "C" fn(skb: *mut sk_buff)>'}, {'name': 'cb_mutex', 'type': '*mut mutex'}, {'name': 'bind', 'type': '::core::option::Option<'}, {'name': 'release', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'groups', 'type': 'core::ffi::c_uint'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'input', 'type': '::core::option::Option<unsafe extern "C" fn(skb: *mut sk_buff)>'}, {'name': 'bind', 'type': '::core::option::Option<'}, {'name': 'release', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-000429 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: request_queue
- Explanation: request_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[{'name': 'queuedata', 'type': '*mut core::ffi::c_void'}, {'name': 'elevator', 'type': '*mut elevator_queue'}, {'name': 'mq_ops', 'type': '*const blk_mq_ops'}, {'name': 'queue_ctx', 'type': '*mut blk_mq_ctx'}, {'name': 'queue_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'rq_timeout', 'type': 'core::ffi::c_uint'}, {'name': 'queue_depth', 'type': 'core::ffi::c_uint'}, {'name': 'refs', 'type': 'refcount_t'}, {'name': 'nr_hw_queues', 'type': 'core::ffi::c_uint'}, {'name': 'hctx_table', 'type': 'xarray'}, {'name': 'q_usage_counter', 'type': 'percpu_ref'}, {'name': 'last_merge', 'type': '*mut request'}, {'name': 'queue_lock', 'type': 'spinlock_t'}, {'name': 'quiesce_depth', 'type': 'core::ffi::c_int'}, {'name': 'disk', 'type': '*mut gendisk'}, {'name': 'mq_kobj', 'type': '*mut kobject'}, {'name': 'limits', 'type': 'queue_limits'}, {'name': 'dev', 'type': '*mut device'}, {'name': 'rpm_status', 'type': 'rpm_status'}, {'name': 'pm_only', 'type': 'atomic_t'}, {'name': 'stats', 'type': '*mut blk_queue_stats'}, {'name': 'rq_qos', 'type': '*mut rq_qos'}, {'name': 'rq_qos_mutex', 'type': 'mutex'}, {'name': 'id', 'type': 'core::ffi::c_int'}, {'name': 'nr_requests', 'type': 'core::ffi::c_ulong'}, {'name': 'timeout', 'type': 'timer_list'}, {'name': 'timeout_work', 'type': 'work_struct'}, {'name': 'nr_active_requests_shared_tags', 'type': 'atomic_t'}, {'name': 'sched_shared_tags', 'type': '*mut blk_mq_tags'}, {'name': 'icq_list', 'type': 'list_head'}, {'name': 'blkcg_pols', 'type': '[core::ffi::c_ulong; 1usize]'}, {'name': 'root_blkg', 'type': '*mut blkcg_gq'}, {'name': 'blkg_list', 'type': 'list_head'}, {'name': 'blkcg_mutex', 'type': 'mutex'}, {'name': 'node', 'type': 'core::ffi::c_int'}, {'name': 'requeue_lock', 'type': 'spinlock_t'}, {'name': 'requeue_list', 'type': 'list_head'}, {'name': 'requeue_work', 'type': 'delayed_work'}, {'name': 'blk_trace', 'type': '*mut blk_trace'}, {'name': 'fq', 'type': '*mut blk_flush_queue'}, {'name': 'flush_list', 'type': 'list_head'}, {'name': 'sysfs_lock', 'type': 'mutex'}, {'name': 'sysfs_dir_lock', 'type': 'mutex'}, {'name': 'limits_lock', 'type': 'mutex'}, {'name': 'unused_hctx_list', 'type': 'list_head'}, {'name': 'unused_hctx_lock', 'type': 'spinlock_t'}, {'name': 'mq_freeze_depth', 'type': 'core::ffi::c_int'}, {'name': 'callback_head', 'type': 'callback_head'}, {'name': 'mq_freeze_wq', 'type': 'wait_queue_head_t'}, {'name': 'mq_freeze_lock', 'type': 'mutex'}, {'name': 'tag_set', 'type': '*mut blk_mq_tag_set'}, {'name': 'tag_set_list', 'type': 'list_head'}, {'name': 'debugfs_dir', 'type': '*mut dentry'}, {'name': 'sched_debugfs_dir', 'type': '*mut dentry'}, {'name': 'rqos_debugfs_dir', 'type': '*mut dentry'}, {'name': 'debugfs_mutex', 'type': 'mutex'}, {'name': 'mq_sysfs_init_done', 'type': 'bool_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000430 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: smp_ops
- Explanation: smp_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'smp_prepare_boot_cpu', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'smp_prepare_cpus', 'type': '::core::option::Option<unsafe extern "C" fn(max_cpus: core::ffi::c_uint)>'}, {'name': 'smp_cpus_done', 'type': '::core::option::Option<unsafe extern "C" fn(max_cpus: core::ffi::c_uint)>'}, {'name': 'stop_other_cpus', 'type': '::core::option::Option<unsafe extern "C" fn(wait: core::ffi::c_int)>'}, {'name': 'crash_stop_other_cpus', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'smp_send_reschedule', 'type': '::core::option::Option<unsafe extern "C" fn(cpu: core::ffi::c_int)>'}, {'name': 'cleanup_dead_cpu', 'type': '::core::option::Option<unsafe extern "C" fn(cpu: core::ffi::c_uint)>'}, {'name': 'poll_sync_state', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'kick_ap_alive', 'type': '::core::option::Option<'}, {'name': 'cpu_disable', 'type': '::core::option::Option<unsafe extern "C" fn() -> core::ffi::c_int>'}, {'name': 'cpu_die', 'type': '::core::option::Option<unsafe extern "C" fn(cpu: core::ffi::c_uint)>'}, {'name': 'play_dead', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'send_call_func_ipi', 'type': '::core::option::Option<unsafe extern "C" fn(mask: *const cpumask)>'}]`
- New: `[{'name': 'smp_prepare_boot_cpu', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'smp_prepare_cpus', 'type': '::core::option::Option<unsafe extern "C" fn(max_cpus: core::ffi::c_uint)>'}, {'name': 'smp_cpus_done', 'type': '::core::option::Option<unsafe extern "C" fn(max_cpus: core::ffi::c_uint)>'}, {'name': 'stop_other_cpus', 'type': '::core::option::Option<unsafe extern "C" fn(wait: core::ffi::c_int)>'}, {'name': 'crash_stop_other_cpus', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'smp_send_reschedule', 'type': '::core::option::Option<unsafe extern "C" fn(cpu: core::ffi::c_int)>'}, {'name': 'cleanup_dead_cpu', 'type': '::core::option::Option<unsafe extern "C" fn(cpu: core::ffi::c_uint)>'}, {'name': 'poll_sync_state', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'kick_ap_alive', 'type': '::core::option::Option<'}, {'name': 'cpu_disable', 'type': '::core::option::Option<unsafe extern "C" fn() -> core::ffi::c_int>'}, {'name': 'cpu_die', 'type': '::core::option::Option<unsafe extern "C" fn(cpu: core::ffi::c_uint)>'}, {'name': 'play_dead', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'stop_this_cpu', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'send_call_func_ipi', 'type': '::core::option::Option<unsafe extern "C" fn(mask: *const cpumask)>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000432 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: system_counterval_t
- Explanation: system_counterval_t changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'cycles', 'type': 'u64_'}, {'name': 'cs_id', 'type': 'clocksource_ids'}]`
- New: `[{'name': 'cycles', 'type': 'u64_'}, {'name': 'cs_id', 'type': 'clocksource_ids'}, {'name': 'use_nsecs', 'type': 'bool_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000435 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: x86_guest
- Explanation: x86_guest changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'enc_status_change_prepare', 'type': '::core::option::Option<'}, {'name': 'enc_status_change_finish', 'type': '::core::option::Option<'}, {'name': 'enc_tlb_flush_required', 'type': '::core::option::Option<unsafe extern "C" fn(enc: bool_) -> bool_>'}, {'name': 'enc_cache_flush_required', 'type': '::core::option::Option<unsafe extern "C" fn() -> bool_>'}]`
- New: `[{'name': 'enc_status_change_prepare', 'type': '::core::option::Option<'}, {'name': 'enc_status_change_finish', 'type': '::core::option::Option<'}, {'name': 'enc_tlb_flush_required', 'type': '::core::option::Option<unsafe extern "C" fn(enc: bool_) -> bool_>'}, {'name': 'enc_cache_flush_required', 'type': '::core::option::Option<unsafe extern "C" fn() -> bool_>'}, {'name': 'enc_kexec_begin', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'enc_kexec_finish', 'type': '::core::option::Option<unsafe extern "C" fn()>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000473 MacroConstDrift

- Risk: Medium
- Score: 8.4
- Symbol: cpuhp_state_CPUHP_AP_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `143`
- New: `145`

### Rust Evidence

- Graph edges: `4`

## W-000474 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: cpuhp_state_CPUHP_AP_ONLINE_DYN
- Explanation: cpuhp_state_CPUHP_AP_ONLINE_DYN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `192`
- New: `194`

### Rust Evidence

- Graph edges: `2`

## W-000436 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: CONFIG_SATA_MOBILE_LPM_POLICY
- Explanation: CONFIG_SATA_MOBILE_LPM_POLICY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0`
- New: `3`

### Rust Evidence

- Graph edges: `1`

## W-000437 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TC_AT_INGRESS_MASK
- Explanation: TC_AT_INGRESS_MASK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `2`
- New: `4`

### Rust Evidence

- Graph edges: `1`

## W-000438 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: alt_slen
- Explanation: alt_slen changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `b"662b-661b\0"`
- New: `b"772b-771b\0"`

### Rust Evidence

- Graph edges: `1`

## W-000439 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: alt_total_slen
- Explanation: alt_total_slen changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `b"663b-661b\0"`
- New: `b"773b-771b\0"`

### Rust Evidence

- Graph edges: `1`

## W-000440 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cc_attr_CC_ATTR_HOST_SEV_SNP
- Explanation: cc_attr_CC_ATTR_HOST_SEV_SNP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `7`
- New: `6`

### Rust Evidence

- Graph edges: `1`

## W-000441 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: clocksource_ids_CSID_MAX
- Explanation: clocksource_ids_CSID_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `6`

### Rust Evidence

- Graph edges: `1`

## W-000442 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ACTIVE
- Explanation: cpuhp_state_CPUHP_AP_ACTIVE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `235`
- New: `237`

### Rust Evidence

- Graph edges: `1`

## W-000443 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARC_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARC_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `126`
- New: `127`

### Rust Evidence

- Graph edges: `1`

## W-000444 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM64_DEBUG_MONITORS_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM64_DEBUG_MONITORS_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `110`
- New: `111`

### Rust Evidence

- Graph edges: `1`

## W-000445 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM64_ISNDEP_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM64_ISNDEP_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `137`
- New: `139`

### Rust Evidence

- Graph edges: `1`

## W-000446 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARMADA_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARMADA_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `124`
- New: `125`

### Rust Evidence

- Graph edges: `1`

## W-000447 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_EVTSTRM_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_EVTSTRM_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `118`
- New: `119`

### Rust Evidence

- Graph edges: `1`

## W-000448 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `117`
- New: `118`

### Rust Evidence

- Graph edges: `1`

## W-000449 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_CACHE_B15_RAC_DYING
- Explanation: cpuhp_state_CPUHP_AP_ARM_CACHE_B15_RAC_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `142`
- New: `144`

### Rust Evidence

- Graph edges: `1`

## W-000450 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_CORESIGHT_CTI_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_CORESIGHT_CTI_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `136`
- New: `138`

### Rust Evidence

- Graph edges: `1`

## W-000451 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_CORESIGHT_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_CORESIGHT_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `135`
- New: `137`

### Rust Evidence

- Graph edges: `1`

## W-000452 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_GLOBAL_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_GLOBAL_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `119`
- New: `120`

### Rust Evidence

- Graph edges: `1`

## W-000453 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_L2X0_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_L2X0_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `115`
- New: `116`

### Rust Evidence

- Graph edges: `1`

## W-000454 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_MVEBU_COHERENCY
- Explanation: cpuhp_state_CPUHP_AP_ARM_MVEBU_COHERENCY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `103`
- New: `104`

### Rust Evidence

- Graph edges: `1`

## W-000455 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_MVEBU_SYNC_CLOCKS
- Explanation: cpuhp_state_CPUHP_AP_ARM_MVEBU_SYNC_CLOCKS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `152`
- New: `154`

### Rust Evidence

- Graph edges: `1`

## W-000456 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_TWD_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_TWD_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `121`
- New: `122`

### Rust Evidence

- Graph edges: `1`

## W-000457 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_VFP_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_VFP_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `109`
- New: `110`

### Rust Evidence

- Graph edges: `1`

## W-000458 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_XEN_RUNSTATE_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_XEN_RUNSTATE_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `134`
- New: `136`

### Rust Evidence

- Graph edges: `1`

## W-000459 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_XEN_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_XEN_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `133`
- New: `135`

### Rust Evidence

- Graph edges: `1`

## W-000460 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_BASE_CACHEINFO_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_BASE_CACHEINFO_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `191`
- New: `193`

### Rust Evidence

- Graph edges: `1`

## W-000461 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_BLK_MQ_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_BLK_MQ_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `151`
- New: `153`

### Rust Evidence

- Graph edges: `1`

## W-000462 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_CLINT_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_CLINT_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `128`
- New: `130`

### Rust Evidence

- Graph edges: `1`

## W-000463 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_CSKY_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_CSKY_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `129`
- New: `131`

### Rust Evidence

- Graph edges: `1`

## W-000464 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_DUMMY_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_DUMMY_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `132`
- New: `134`

### Rust Evidence

- Graph edges: `1`

## W-000465 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_EXYNOS4_MCT_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_EXYNOS4_MCT_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `116`
- New: `117`

### Rust Evidence

- Graph edges: `1`

## W-000466 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_HRTIMERS_DYING
- Explanation: cpuhp_state_CPUHP_AP_HRTIMERS_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `139`
- New: `141`

### Rust Evidence

- Graph edges: `1`

## W-000467 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_HYPERV_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_HYPERV_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `146`
- New: `148`

### Rust Evidence

- Graph edges: `1`

## W-000468 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_HYPERV_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_HYPERV_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `131`
- New: `133`

### Rust Evidence

- Graph edges: `1`

## W-000469 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_AFFINITY_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_IRQ_AFFINITY_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `150`
- New: `152`

### Rust Evidence

- Graph edges: `1`

## W-000470 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_JCORE_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_JCORE_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `120`
- New: `121`

### Rust Evidence

- Graph edges: `1`

## W-000471 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_KVM_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_KVM_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `147`
- New: `149`

### Rust Evidence

- Graph edges: `1`

## W-000472 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_MIPS_GIC_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_MIPS_GIC_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `125`
- New: `126`

### Rust Evidence

- Graph edges: `1`

## W-000475 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ONLINE_DYN_END
- Explanation: cpuhp_state_CPUHP_AP_ONLINE_DYN_END changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `232`
- New: `234`

### Rust Evidence

- Graph edges: `1`

## W-000476 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ONLINE_IDLE
- Explanation: cpuhp_state_CPUHP_AP_ONLINE_IDLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `145`
- New: `147`

### Rust Evidence

- Graph edges: `1`

## W-000477 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_ACPI_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_ACPI_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `112`
- New: `113`

### Rust Evidence

- Graph edges: `1`

## W-000478 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_APM_XGENE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_APM_XGENE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `176`
- New: `178`

### Rust Evidence

- Graph edges: `1`

## W-000479 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_CAVIUM_TX2_UNCORE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_CAVIUM_TX2_UNCORE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `177`
- New: `179`

### Rust Evidence

- Graph edges: `1`

## W-000480 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_CCI_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_CCI_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `163`
- New: `165`

### Rust Evidence

- Graph edges: `1`

## W-000481 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_CCN_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_CCN_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `164`
- New: `166`

### Rust Evidence

- Graph edges: `1`

## W-000482 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_CPA_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_CPA_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `165`
- New: `167`

### Rust Evidence

- Graph edges: `1`

## W-000483 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_DDRC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_DDRC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `166`
- New: `168`

### Rust Evidence

- Graph edges: `1`

## W-000484 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_HHA_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_HHA_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `167`
- New: `169`

### Rust Evidence

- Graph edges: `1`

## W-000485 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_L3_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_L3_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `168`
- New: `170`

### Rust Evidence

- Graph edges: `1`

## W-000486 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PA_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PA_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `169`
- New: `171`

### Rust Evidence

- Graph edges: `1`

## W-000487 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PCIE_PMU_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PCIE_PMU_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `171`
- New: `173`

### Rust Evidence

- Graph edges: `1`

## W-000488 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_SLLC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_SLLC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `170`
- New: `172`

### Rust Evidence

- Graph edges: `1`

## W-000489 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HNS3_PMU_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HNS3_PMU_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `172`
- New: `174`

### Rust Evidence

- Graph edges: `1`

## W-000490 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HW_BREAKPOINT_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HW_BREAKPOINT_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `111`
- New: `112`

### Rust Evidence

- Graph edges: `1`

## W-000491 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_L2X0_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_L2X0_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `173`
- New: `175`

### Rust Evidence

- Graph edges: `1`

## W-000492 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_MARVELL_CN10K_DDR_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_MARVELL_CN10K_DDR_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `178`
- New: `180`

### Rust Evidence

- Graph edges: `1`

## W-000493 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L2_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L2_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `174`
- New: `176`

### Rust Evidence

- Graph edges: `1`

## W-000494 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L3_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L3_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `175`
- New: `177`

### Rust Evidence

- Graph edges: `1`

## W-000495 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `113`
- New: `114`

### Rust Evidence

- Graph edges: `1`

## W-000496 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_CSKY_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_CSKY_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `185`
- New: `187`

### Rust Evidence

- Graph edges: `1`

## W-000497 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `154`
- New: `156`

### Rust Evidence

- Graph edges: `1`

## W-000498 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_CORE_IMC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_CORE_IMC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `180`
- New: `182`

### Rust Evidence

- Graph edges: `1`

## W-000499 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_HV_24x7_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_HV_24x7_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `183`
- New: `185`

### Rust Evidence

- Graph edges: `1`

## W-000500 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_HV_GPCI_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_HV_GPCI_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `184`
- New: `186`

### Rust Evidence

- Graph edges: `1`

## W-000501 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_NEST_IMC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_NEST_IMC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `179`
- New: `181`

### Rust Evidence

- Graph edges: `1`

## W-000502 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_THREAD_IMC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_THREAD_IMC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `181`
- New: `183`

### Rust Evidence

- Graph edges: `1`

## W-000503 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_TRACE_IMC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_TRACE_IMC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `182`
- New: `184`

### Rust Evidence

- Graph edges: `1`

## W-000504 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_RISCV_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_RISCV_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `114`
- New: `115`

### Rust Evidence

- Graph edges: `1`

## W-000505 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_S390_CF_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_S390_CF_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `161`
- New: `163`

### Rust Evidence

- Graph edges: `1`

## W-000506 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_S390_SF_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_S390_SF_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `162`
- New: `164`

### Rust Evidence

- Graph edges: `1`

## W-000507 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_IBS_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_IBS_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `106`
- New: `107`

### Rust Evidence

- Graph edges: `1`

## W-000508 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_POWER_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_POWER_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `158`
- New: `160`

### Rust Evidence

- Graph edges: `1`

## W-000509 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `157`
- New: `159`

### Rust Evidence

- Graph edges: `1`

## W-000510 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `104`
- New: `105`

### Rust Evidence

- Graph edges: `1`

## W-000511 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_CSTATE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_CSTATE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `160`
- New: `162`

### Rust Evidence

- Graph edges: `1`

## W-000512 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_CSTATE_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_CSTATE_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `107`
- New: `108`

### Rust Evidence

- Graph edges: `1`

## W-000513 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `155`
- New: `157`

### Rust Evidence

- Graph edges: `1`

## W-000514 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_RAPL_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_RAPL_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `159`
- New: `161`

### Rust Evidence

- Graph edges: `1`

## W-000515 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `105`
- New: `106`

### Rust Evidence

- Graph edges: `1`

## W-000516 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_UNCORE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_UNCORE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `156`
- New: `158`

### Rust Evidence

- Graph edges: `1`

## W-000517 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_XTENSA_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_XTENSA_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `108`
- New: `109`

### Rust Evidence

- Graph edges: `1`

## W-000518 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_QCOM_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_QCOM_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `122`
- New: `123`

### Rust Evidence

- Graph edges: `1`

## W-000519 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_RANDOM_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_RANDOM_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `189`
- New: `191`

### Rust Evidence

- Graph edges: `1`

## W-000520 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_RCUTREE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_RCUTREE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `190`
- New: `192`

### Rust Evidence

- Graph edges: `1`

## W-000521 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_RISCV_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_RISCV_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `127`
- New: `129`

### Rust Evidence

- Graph edges: `1`

## W-000522 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_SCHED_WAIT_EMPTY
- Explanation: cpuhp_state_CPUHP_AP_SCHED_WAIT_EMPTY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `148`
- New: `150`

### Rust Evidence

- Graph edges: `1`

## W-000523 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_SMPBOOT_THREADS
- Explanation: cpuhp_state_CPUHP_AP_SMPBOOT_THREADS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `149`
- New: `151`

### Rust Evidence

- Graph edges: `1`

## W-000524 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_SMPCFD_DYING
- Explanation: cpuhp_state_CPUHP_AP_SMPCFD_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `138`
- New: `140`

### Rust Evidence

- Graph edges: `1`

## W-000525 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_TEGRA_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_TEGRA_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `123`
- New: `124`

### Rust Evidence

- Graph edges: `1`

## W-000526 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_TICK_DYING
- Explanation: cpuhp_state_CPUHP_AP_TICK_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `140`
- New: `142`

### Rust Evidence

- Graph edges: `1`

## W-000527 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_TI_GP_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_TI_GP_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `130`
- New: `132`

### Rust Evidence

- Graph edges: `1`

## W-000528 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_TMIGR_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_TMIGR_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `186`
- New: `188`

### Rust Evidence

- Graph edges: `1`

## W-000529 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_WATCHDOG_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_WATCHDOG_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `187`
- New: `189`

### Rust Evidence

- Graph edges: `1`

## W-000530 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_WORKQUEUE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_WORKQUEUE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `188`
- New: `190`

### Rust Evidence

- Graph edges: `1`

## W-000531 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_X86_HPET_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_X86_HPET_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `233`
- New: `235`

### Rust Evidence

- Graph edges: `1`

## W-000532 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_X86_INTEL_EPB_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_X86_INTEL_EPB_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `153`
- New: `155`

### Rust Evidence

- Graph edges: `1`

## W-000533 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_X86_KVM_CLK_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_X86_KVM_CLK_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `234`
- New: `236`

### Rust Evidence

- Graph edges: `1`

## W-000534 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_X86_TBOOT_DYING
- Explanation: cpuhp_state_CPUHP_AP_X86_TBOOT_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `141`
- New: `143`

### Rust Evidence

- Graph edges: `1`

## W-000535 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_ARM_BL_PREPARE
- Explanation: cpuhp_state_CPUHP_ARM_BL_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `57`
- New: `56`

### Rust Evidence

- Graph edges: `1`

## W-000536 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_ARM_SHMOBILE_SCU_PREPARE
- Explanation: cpuhp_state_CPUHP_ARM_SHMOBILE_SCU_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `53`
- New: `52`

### Rust Evidence

- Graph edges: `1`

## W-000537 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_CPUIDLE_COUPLED_PREPARE
- Explanation: cpuhp_state_CPUHP_CPUIDLE_COUPLED_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `47`

### Rust Evidence

- Graph edges: `1`

## W-000538 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_KVM_PPC_BOOK3S_PREPARE
- Explanation: cpuhp_state_CPUHP_KVM_PPC_BOOK3S_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `61`
- New: `60`

### Rust Evidence

- Graph edges: `1`

## W-000539 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_MD_RAID5_PREPARE
- Explanation: cpuhp_state_CPUHP_MD_RAID5_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `46`
- New: `45`

### Rust Evidence

- Graph edges: `1`

## W-000540 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_MM_ZSWP_POOL_PREPARE
- Explanation: cpuhp_state_CPUHP_MM_ZSWP_POOL_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `60`
- New: `59`

### Rust Evidence

- Graph edges: `1`

## W-000541 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_MM_ZS_PREPARE
- Explanation: cpuhp_state_CPUHP_MM_ZS_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `59`
- New: `58`

### Rust Evidence

- Graph edges: `1`

## W-000542 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_NET_IUCV_PREPARE
- Explanation: cpuhp_state_CPUHP_NET_IUCV_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `56`
- New: `55`

### Rust Evidence

- Graph edges: `1`

## W-000543 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_ONLINE
- Explanation: cpuhp_state_CPUHP_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `236`
- New: `238`

### Rust Evidence

- Graph edges: `1`

## W-000544 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_POWERPC_MMU_CTX_PREPARE
- Explanation: cpuhp_state_CPUHP_POWERPC_MMU_CTX_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `50`
- New: `49`

### Rust Evidence

- Graph edges: `1`

## W-000545 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_POWERPC_PMAC_PREPARE
- Explanation: cpuhp_state_CPUHP_POWERPC_PMAC_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `49`
- New: `48`

### Rust Evidence

- Graph edges: `1`

## W-000546 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_RCUTREE_PREP
- Explanation: cpuhp_state_CPUHP_RCUTREE_PREP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `47`
- New: `46`

### Rust Evidence

- Graph edges: `1`

## W-000547 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_RELAY_PREPARE
- Explanation: cpuhp_state_CPUHP_RELAY_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `45`
- New: `44`

### Rust Evidence

- Graph edges: `1`

## W-000548 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_SH_SH3X_PREPARE
- Explanation: cpuhp_state_CPUHP_SH_SH3X_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `54`
- New: `53`

### Rust Evidence

- Graph edges: `1`

## W-000549 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_SMPCFD_PREPARE
- Explanation: cpuhp_state_CPUHP_SMPCFD_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `44`
- New: `43`

### Rust Evidence

- Graph edges: `1`

## W-000550 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_TEARDOWN_CPU
- Explanation: cpuhp_state_CPUHP_TEARDOWN_CPU changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `144`
- New: `146`

### Rust Evidence

- Graph edges: `1`

## W-000551 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_TIMERS_PREPARE
- Explanation: cpuhp_state_CPUHP_TIMERS_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `63`
- New: `62`

### Rust Evidence

- Graph edges: `1`

## W-000552 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_TOPOLOGY_PREPARE
- Explanation: cpuhp_state_CPUHP_TOPOLOGY_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `55`
- New: `54`

### Rust Evidence

- Graph edges: `1`

## W-000553 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_TRACE_RB_PREPARE
- Explanation: cpuhp_state_CPUHP_TRACE_RB_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `58`
- New: `57`

### Rust Evidence

- Graph edges: `1`

## W-000554 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_X2APIC_PREPARE
- Explanation: cpuhp_state_CPUHP_X2APIC_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `43`
- New: `42`

### Rust Evidence

- Graph edges: `1`

## W-000555 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_XEN_EVTCHN_PREPARE
- Explanation: cpuhp_state_CPUHP_XEN_EVTCHN_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `52`
- New: `51`

### Rust Evidence

- Graph edges: `1`

## W-000556 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_XEN_PREPARE
- Explanation: cpuhp_state_CPUHP_XEN_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `51`
- New: `50`

### Rust Evidence

- Graph edges: `1`

## W-000557 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_ZCOMP_PREPARE
- Explanation: cpuhp_state_CPUHP_ZCOMP_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `62`
- New: `61`

### Rust Evidence

- Graph edges: `1`

## W-000558 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ethtool_link_mode_bit_indices___ETHTOOL_LINK_MODE_MASK_NBITS
- Explanation: ethtool_link_mode_bit_indices___ETHTOOL_LINK_MODE_MASK_NBITS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `102`
- New: `103`

### Rust Evidence

- Graph edges: `1`

## W-000559 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: hwtstamp_source_HWTSTAMP_SOURCE_NETDEV
- Explanation: hwtstamp_source_HWTSTAMP_SOURCE_NETDEV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0`
- New: `1`

### Rust Evidence

- Graph edges: `1`

## W-000560 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: hwtstamp_source_HWTSTAMP_SOURCE_PHYLIB
- Explanation: hwtstamp_source_HWTSTAMP_SOURCE_PHYLIB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `1`
- New: `2`

### Rust Evidence

- Graph edges: `1`

## W-000561 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: mf_action_page_type_MF_MSG_DIFFERENT_COMPOUND
- Explanation: mf_action_page_type_MF_MSG_DIFFERENT_COMPOUND changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `3`
- New: `2`

### Rust Evidence

- Graph edges: `1`

## W-000562 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: mf_action_page_type_MF_MSG_FREE_HUGE
- Explanation: mf_action_page_type_MF_MSG_FREE_HUGE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `4`

### Rust Evidence

- Graph edges: `1`

## W-000563 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: mf_action_page_type_MF_MSG_HUGE
- Explanation: mf_action_page_type_MF_MSG_HUGE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `4`
- New: `3`

### Rust Evidence

- Graph edges: `1`

## W-000564 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: mf_action_page_type_MF_MSG_UNKNOWN
- Explanation: mf_action_page_type_MF_MSG_UNKNOWN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `19`
- New: `20`

### Rust Evidence

- Graph edges: `1`

## W-000565 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: migrate_reason_MR_TYPES
- Explanation: migrate_reason_MR_TYPES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `9`
- New: `10`

### Rust Evidence

- Graph edges: `1`

## W-000566 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pagetype_PAGE_MAPCOUNT_RESERVE
- Explanation: pagetype_PAGE_MAPCOUNT_RESERVE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `-128`
- New: `-65536`

### Rust Evidence

- Graph edges: `1`

## W-000567 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pagetype_PAGE_TYPE_BASE
- Explanation: pagetype_PAGE_TYPE_BASE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `4026531840`
- New: `2147483648`

### Rust Evidence

- Graph edges: `1`

## W-000568 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pagetype_PG_buddy
- Explanation: pagetype_PG_buddy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `128`
- New: `1073741824`

### Rust Evidence

- Graph edges: `1`

## W-000569 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pagetype_PG_guard
- Explanation: pagetype_PG_guard changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `1024`
- New: `134217728`

### Rust Evidence

- Graph edges: `1`

## W-000570 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pagetype_PG_hugetlb
- Explanation: pagetype_PG_hugetlb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `2048`
- New: `67108864`

### Rust Evidence

- Graph edges: `1`

## W-000571 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pagetype_PG_offline
- Explanation: pagetype_PG_offline changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `256`
- New: `536870912`

### Rust Evidence

- Graph edges: `1`

## W-000572 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pagetype_PG_slab
- Explanation: pagetype_PG_slab changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `4096`
- New: `33554432`

### Rust Evidence

- Graph edges: `1`

## W-000573 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pagetype_PG_table
- Explanation: pagetype_PG_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `512`
- New: `268435456`

### Rust Evidence

- Graph edges: `1`

## W-000574 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pg_level_PG_LEVEL_NUM
- Explanation: pg_level_PG_LEVEL_NUM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `6`

### Rust Evidence

- Graph edges: `1`

## W-000575 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: phy_interface_t_PHY_INTERFACE_MODE_MAX
- Explanation: phy_interface_t_PHY_INTERFACE_MODE_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `33`
- New: `34`

### Rust Evidence

- Graph edges: `1`

## W-000576 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: req_flag_bits___REQ_NOUNMAP
- Explanation: req_flag_bits___REQ_NOUNMAP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `27`
- New: `28`

### Rust Evidence

- Graph edges: `1`

## W-000577 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: req_flag_bits___REQ_NR_BITS
- Explanation: req_flag_bits___REQ_NR_BITS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `28`
- New: `29`

### Rust Evidence

- Graph edges: `1`

## W-000578 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AXI_DMA
- Explanation: CLKID_AXI_DMA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `57`
- New: `76`

### Rust Evidence

- Graph edges: `0`

## W-000579 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AXI_NIC
- Explanation: CLKID_AXI_NIC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `56`
- New: `75`

### Rust Evidence

- Graph edges: `0`

## W-000580 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SPICC_A
- Explanation: CLKID_SPICC_A changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `17`
- New: `136`

### Rust Evidence

- Graph edges: `0`

## W-000581 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SPICC_B
- Explanation: CLKID_SPICC_B changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `139`

### Rust Evidence

- Graph edges: `0`

## W-000582 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_CTRL
- Explanation: CLKID_SYS_CTRL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `13`
- New: `8`

### Rust Evidence

- Graph edges: `0`

## W-000583 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_USB_CTRL
- Explanation: CLKID_USB_CTRL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `36`
- New: `6`

### Rust Evidence

- Graph edges: `0`

## W-000584 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: DP_ALPM_LOCK_ERROR_IRQ_HPD_ENABLE
- Explanation: DP_ALPM_LOCK_ERROR_IRQ_HPD_ENABLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `(1 << 1)`
- New: `(1 << 1) /* eDP 1.5 */`

### Rust Evidence

- Graph edges: `0`

## W-000585 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: ETHTOOL_COALESCE_ALL_PARAMS
- Explanation: ETHTOOL_COALESCE_ALL_PARAMS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `GENMASK(26, 0)`
- New: `GENMASK(28, 0)`

### Rust Evidence

- Graph edges: `0`

## W-000586 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: INTEL_QUANTA_VGA_DEVICE
- Explanation: INTEL_QUANTA_VGA_DEVICE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{		\`
- New: `{ \`

### Rust Evidence

- Graph edges: `0`

## W-000587 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: INTEL_VGA_DEVICE
- Explanation: INTEL_VGA_DEVICE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{		\`
- New: `{ \`

### Rust Evidence

- Graph edges: `0`

## W-000588 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: to_acpi_driver
- Explanation: to_acpi_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `container_of(d, struct acpi_driver, drv)`
- New: `container_of_const(d, struct acpi_driver, drv)`

### Rust Evidence

- Graph edges: `0`

## W-000589 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: to_phy_driver
- Explanation: to_phy_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `container_of(to_mdio_common_driver(d),		\`
- New: `container_of_const(to_mdio_common_driver(d),		\`

### Rust Evidence

- Graph edges: `0`
