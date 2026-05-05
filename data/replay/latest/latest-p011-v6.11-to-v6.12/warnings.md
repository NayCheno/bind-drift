# BindDrift Ranked Warnings

## W-000122 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: bio
- Explanation: bio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'bi_next', 'type': '*mut bio'}, {'name': 'bi_bdev', 'type': '*mut block_device'}, {'name': 'bi_opf', 'type': 'blk_opf_t'}, {'name': 'bi_flags', 'type': 'core::ffi::c_ushort'}, {'name': 'bi_ioprio', 'type': 'core::ffi::c_ushort'}, {'name': 'bi_write_hint', 'type': 'rw_hint'}, {'name': 'bi_status', 'type': 'blk_status_t'}, {'name': '__bi_remaining', 'type': 'atomic_t'}, {'name': 'bi_iter', 'type': 'bvec_iter'}, {'name': '__bindgen_anon_1', 'type': 'bio__bindgen_ty_1'}, {'name': 'bi_end_io', 'type': 'bio_end_io_t'}, {'name': 'bi_private', 'type': '*mut core::ffi::c_void'}, {'name': 'bi_blkg', 'type': '*mut blkcg_gq'}, {'name': 'bi_issue', 'type': 'bio_issue'}, {'name': 'bi_iocost_cost', 'type': 'u64_'}, {'name': '__bindgen_anon_2', 'type': 'bio__bindgen_ty_2'}, {'name': 'bi_vcnt', 'type': 'core::ffi::c_ushort'}, {'name': 'bi_max_vecs', 'type': 'core::ffi::c_ushort'}, {'name': '__bi_cnt', 'type': 'atomic_t'}, {'name': 'bi_io_vec', 'type': '*mut bio_vec'}, {'name': 'bi_pool', 'type': '*mut bio_set'}, {'name': 'bi_inline_vecs', 'type': '__IncompleteArrayField<bio_vec>'}]`
- New: `[{'name': 'bi_next', 'type': '*mut bio'}, {'name': 'bi_bdev', 'type': '*mut block_device'}, {'name': 'bi_opf', 'type': 'blk_opf_t'}, {'name': 'bi_flags', 'type': 'core::ffi::c_ushort'}, {'name': 'bi_ioprio', 'type': 'core::ffi::c_ushort'}, {'name': 'bi_write_hint', 'type': 'rw_hint'}, {'name': 'bi_status', 'type': 'blk_status_t'}, {'name': '__bi_remaining', 'type': 'atomic_t'}, {'name': 'bi_iter', 'type': 'bvec_iter'}, {'name': '__bindgen_anon_1', 'type': 'bio__bindgen_ty_1'}, {'name': 'bi_end_io', 'type': 'bio_end_io_t'}, {'name': 'bi_private', 'type': '*mut core::ffi::c_void'}, {'name': 'bi_blkg', 'type': '*mut blkcg_gq'}, {'name': 'bi_issue', 'type': 'bio_issue'}, {'name': 'bi_iocost_cost', 'type': 'u64_'}, {'name': 'bi_vcnt', 'type': 'core::ffi::c_ushort'}, {'name': 'bi_max_vecs', 'type': 'core::ffi::c_ushort'}, {'name': '__bi_cnt', 'type': 'atomic_t'}, {'name': 'bi_io_vec', 'type': '*mut bio_vec'}, {'name': 'bi_pool', 'type': '*mut bio_set'}, {'name': 'bi_inline_vecs', 'type': '__IncompleteArrayField<bio_vec>'}]`

### Rust Evidence

- Graph edges: `50`

## W-000128 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: cgroup
- Explanation: cgroup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'self_', 'type': 'cgroup_subsys_state'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'level', 'type': 'core::ffi::c_int'}, {'name': 'max_depth', 'type': 'core::ffi::c_int'}, {'name': 'nr_descendants', 'type': 'core::ffi::c_int'}, {'name': 'nr_dying_descendants', 'type': 'core::ffi::c_int'}, {'name': 'max_descendants', 'type': 'core::ffi::c_int'}, {'name': 'nr_populated_csets', 'type': 'core::ffi::c_int'}, {'name': 'nr_populated_domain_children', 'type': 'core::ffi::c_int'}, {'name': 'nr_populated_threaded_children', 'type': 'core::ffi::c_int'}, {'name': 'nr_threaded_children', 'type': 'core::ffi::c_int'}, {'name': 'kn', 'type': '*mut kernfs_node'}, {'name': 'procs_file', 'type': 'cgroup_file'}, {'name': 'events_file', 'type': 'cgroup_file'}, {'name': 'psi_files', 'type': '__IncompleteArrayField<cgroup_file>'}, {'name': 'subtree_control', 'type': 'u16_'}, {'name': 'subtree_ss_mask', 'type': 'u16_'}, {'name': 'old_subtree_control', 'type': 'u16_'}, {'name': 'old_subtree_ss_mask', 'type': 'u16_'}, {'name': 'subsys', 'type': '[*mut cgroup_subsys_state; 14usize]'}, {'name': 'root', 'type': '*mut cgroup_root'}, {'name': 'cset_links', 'type': 'list_head'}, {'name': 'e_csets', 'type': '[list_head; 14usize]'}, {'name': 'dom_cgrp', 'type': '*mut cgroup'}, {'name': 'old_dom_cgrp', 'type': '*mut cgroup'}, {'name': 'rstat_cpu', 'type': '*mut cgroup_rstat_cpu'}, {'name': 'rstat_css_list', 'type': 'list_head'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': '_pad_', 'type': 'cacheline_padding'}, {'name': 'rstat_flush_next', 'type': '*mut cgroup'}, {'name': 'last_bstat', 'type': 'cgroup_base_stat'}, {'name': 'bstat', 'type': 'cgroup_base_stat'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'pidlists', 'type': 'list_head'}, {'name': 'pidlist_mutex', 'type': 'mutex'}, {'name': 'offline_waitq', 'type': 'wait_queue_head_t'}, {'name': 'release_agent_work', 'type': 'work_struct'}, {'name': 'psi', 'type': '*mut psi_group'}, {'name': 'bpf', 'type': 'cgroup_bpf'}, {'name': 'freezer', 'type': 'cgroup_freezer_state'}, {'name': 'ancestors', 'type': '__IncompleteArrayField<*mut cgroup>'}]`
- New: `[{'name': 'self_', 'type': 'cgroup_subsys_state'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'level', 'type': 'core::ffi::c_int'}, {'name': 'max_depth', 'type': 'core::ffi::c_int'}, {'name': 'nr_descendants', 'type': 'core::ffi::c_int'}, {'name': 'nr_dying_descendants', 'type': 'core::ffi::c_int'}, {'name': 'max_descendants', 'type': 'core::ffi::c_int'}, {'name': 'nr_populated_csets', 'type': 'core::ffi::c_int'}, {'name': 'nr_populated_domain_children', 'type': 'core::ffi::c_int'}, {'name': 'nr_populated_threaded_children', 'type': 'core::ffi::c_int'}, {'name': 'nr_threaded_children', 'type': 'core::ffi::c_int'}, {'name': 'kn', 'type': '*mut kernfs_node'}, {'name': 'procs_file', 'type': 'cgroup_file'}, {'name': 'events_file', 'type': 'cgroup_file'}, {'name': 'psi_files', 'type': '__IncompleteArrayField<cgroup_file>'}, {'name': 'subtree_control', 'type': 'u16_'}, {'name': 'subtree_ss_mask', 'type': 'u16_'}, {'name': 'old_subtree_control', 'type': 'u16_'}, {'name': 'old_subtree_ss_mask', 'type': 'u16_'}, {'name': 'subsys', 'type': '[*mut cgroup_subsys_state; 14usize]'}, {'name': 'nr_dying_subsys', 'type': '[core::ffi::c_int; 14usize]'}, {'name': 'root', 'type': '*mut cgroup_root'}, {'name': 'cset_links', 'type': 'list_head'}, {'name': 'e_csets', 'type': '[list_head; 14usize]'}, {'name': 'dom_cgrp', 'type': '*mut cgroup'}, {'name': 'old_dom_cgrp', 'type': '*mut cgroup'}, {'name': 'rstat_cpu', 'type': '*mut cgroup_rstat_cpu'}, {'name': 'rstat_css_list', 'type': 'list_head'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': '_pad_', 'type': 'cacheline_padding'}, {'name': 'rstat_flush_next', 'type': '*mut cgroup'}, {'name': 'last_bstat', 'type': 'cgroup_base_stat'}, {'name': 'bstat', 'type': 'cgroup_base_stat'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'pidlists', 'type': 'list_head'}, {'name': 'pidlist_mutex', 'type': 'mutex'}, {'name': 'offline_waitq', 'type': 'wait_queue_head_t'}, {'name': 'release_agent_work', 'type': 'work_struct'}, {'name': 'psi', 'type': '*mut psi_group'}, {'name': 'bpf', 'type': 'cgroup_bpf'}, {'name': 'freezer', 'type': 'cgroup_freezer_state'}, {'name': 'ancestors', 'type': '__IncompleteArrayField<*mut cgroup>'}]`

### Rust Evidence

- Graph edges: `50`

## W-000131 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: device
- Explanation: device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'kobj', 'type': 'kobject'}, {'name': 'parent', 'type': '*mut device'}, {'name': 'p', 'type': '*mut device_private'}, {'name': 'init_name', 'type': '*const core::ffi::c_char'}, {'name': 'type_', 'type': '*const device_type'}, {'name': 'bus', 'type': '*const bus_type'}, {'name': 'driver', 'type': '*mut device_driver'}, {'name': 'platform_data', 'type': '*mut core::ffi::c_void'}, {'name': 'driver_data', 'type': '*mut core::ffi::c_void'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'links', 'type': 'dev_links_info'}, {'name': 'power', 'type': 'dev_pm_info'}, {'name': 'pm_domain', 'type': '*mut dev_pm_domain'}, {'name': 'msi', 'type': 'dev_msi_info'}, {'name': 'dma_ops', 'type': '*mut dma_map_ops'}, {'name': 'dma_mask', 'type': '*mut u64_'}, {'name': 'coherent_dma_mask', 'type': 'u64_'}, {'name': 'bus_dma_limit', 'type': 'u64_'}, {'name': 'dma_range_map', 'type': '*mut bus_dma_region'}, {'name': 'dma_parms', 'type': '*mut device_dma_parameters'}, {'name': 'dma_pools', 'type': 'list_head'}, {'name': 'dma_io_tlb_mem', 'type': '*mut io_tlb_mem'}, {'name': 'archdata', 'type': 'dev_archdata'}, {'name': 'of_node', 'type': '*mut device_node'}, {'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'numa_node', 'type': 'core::ffi::c_int'}, {'name': 'devt', 'type': 'dev_t'}, {'name': 'id', 'type': 'u32_'}, {'name': 'devres_lock', 'type': 'spinlock_t'}, {'name': 'devres_head', 'type': 'list_head'}, {'name': 'class', 'type': '*const class'}, {'name': 'groups', 'type': '*mut *const attribute_group'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'iommu_group', 'type': '*mut iommu_group'}, {'name': 'iommu', 'type': '*mut dev_iommu'}, {'name': 'physical_location', 'type': '*mut device_physical_location'}, {'name': 'removable', 'type': 'device_removable'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 3usize]'}]`
- New: `[{'name': 'kobj', 'type': 'kobject'}, {'name': 'parent', 'type': '*mut device'}, {'name': 'p', 'type': '*mut device_private'}, {'name': 'init_name', 'type': '*const core::ffi::c_char'}, {'name': 'type_', 'type': '*const device_type'}, {'name': 'bus', 'type': '*const bus_type'}, {'name': 'driver', 'type': '*mut device_driver'}, {'name': 'platform_data', 'type': '*mut core::ffi::c_void'}, {'name': 'driver_data', 'type': '*mut core::ffi::c_void'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'links', 'type': 'dev_links_info'}, {'name': 'power', 'type': 'dev_pm_info'}, {'name': 'pm_domain', 'type': '*mut dev_pm_domain'}, {'name': 'msi', 'type': 'dev_msi_info'}, {'name': 'dma_mask', 'type': '*mut u64_'}, {'name': 'coherent_dma_mask', 'type': 'u64_'}, {'name': 'bus_dma_limit', 'type': 'u64_'}, {'name': 'dma_range_map', 'type': '*mut bus_dma_region'}, {'name': 'dma_parms', 'type': '*mut device_dma_parameters'}, {'name': 'dma_pools', 'type': 'list_head'}, {'name': 'dma_io_tlb_mem', 'type': '*mut io_tlb_mem'}, {'name': 'archdata', 'type': 'dev_archdata'}, {'name': 'of_node', 'type': '*mut device_node'}, {'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'numa_node', 'type': 'core::ffi::c_int'}, {'name': 'devt', 'type': 'dev_t'}, {'name': 'id', 'type': 'u32_'}, {'name': 'devres_lock', 'type': 'spinlock_t'}, {'name': 'devres_head', 'type': 'list_head'}, {'name': 'class', 'type': '*const class'}, {'name': 'groups', 'type': '*mut *const attribute_group'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'iommu_group', 'type': '*mut iommu_group'}, {'name': 'iommu', 'type': '*mut dev_iommu'}, {'name': 'physical_location', 'type': '*mut device_physical_location'}, {'name': 'removable', 'type': 'device_removable'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 3usize]'}]`

### Rust Evidence

- Graph edges: `50`

## W-000133 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: file
- Explanation: file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'file__bindgen_ty_1'}, {'name': 'f_lock', 'type': 'spinlock_t'}, {'name': 'f_mode', 'type': 'fmode_t'}, {'name': 'f_count', 'type': 'atomic_long_t'}, {'name': 'f_pos_lock', 'type': 'mutex'}, {'name': 'f_pos', 'type': 'loff_t'}, {'name': 'f_flags', 'type': 'core::ffi::c_uint'}, {'name': 'f_owner', 'type': 'fown_struct'}, {'name': 'f_cred', 'type': '*const cred'}, {'name': 'f_ra', 'type': 'file_ra_state'}, {'name': 'f_path', 'type': 'path'}, {'name': 'f_inode', 'type': '*mut inode'}, {'name': 'f_op', 'type': '*const file_operations'}, {'name': 'f_version', 'type': 'u64_'}, {'name': 'f_security', 'type': '*mut core::ffi::c_void'}, {'name': 'private_data', 'type': '*mut core::ffi::c_void'}, {'name': 'f_ep', 'type': '*mut hlist_head'}, {'name': 'f_mapping', 'type': '*mut address_space'}, {'name': 'f_wb_err', 'type': 'errseq_t'}, {'name': 'f_sb_err', 'type': 'errseq_t'}]`
- New: `[{'name': 'f_count', 'type': 'atomic_long_t'}, {'name': 'f_lock', 'type': 'spinlock_t'}, {'name': 'f_mode', 'type': 'fmode_t'}, {'name': 'f_op', 'type': '*const file_operations'}, {'name': 'f_mapping', 'type': '*mut address_space'}, {'name': 'private_data', 'type': '*mut core::ffi::c_void'}, {'name': 'f_inode', 'type': '*mut inode'}, {'name': 'f_flags', 'type': 'core::ffi::c_uint'}, {'name': 'f_iocb_flags', 'type': 'core::ffi::c_uint'}, {'name': 'f_cred', 'type': '*const cred'}, {'name': 'f_path', 'type': 'path'}, {'name': '__bindgen_anon_1', 'type': 'file__bindgen_ty_1'}, {'name': 'f_pos', 'type': 'loff_t'}, {'name': 'f_security', 'type': '*mut core::ffi::c_void'}, {'name': 'f_owner', 'type': '*mut fown_struct'}, {'name': 'f_wb_err', 'type': 'errseq_t'}, {'name': 'f_sb_err', 'type': 'errseq_t'}, {'name': 'f_ep', 'type': '*mut hlist_head'}, {'name': '__bindgen_anon_2', 'type': 'file__bindgen_ty_2'}]`

### Rust Evidence

- Graph edges: `46`

## W-000135 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: inode
- Explanation: inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'i_mode', 'type': 'umode_t'}, {'name': 'i_opflags', 'type': 'core::ffi::c_ushort'}, {'name': 'i_uid', 'type': 'kuid_t'}, {'name': 'i_gid', 'type': 'kgid_t'}, {'name': 'i_flags', 'type': 'core::ffi::c_uint'}, {'name': 'i_acl', 'type': '*mut posix_acl'}, {'name': 'i_default_acl', 'type': '*mut posix_acl'}, {'name': 'i_op', 'type': '*const inode_operations'}, {'name': 'i_sb', 'type': '*mut super_block'}, {'name': 'i_mapping', 'type': '*mut address_space'}, {'name': 'i_security', 'type': '*mut core::ffi::c_void'}, {'name': 'i_ino', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'inode__bindgen_ty_1'}, {'name': 'i_rdev', 'type': 'dev_t'}, {'name': 'i_size', 'type': 'loff_t'}, {'name': 'i_atime_sec', 'type': 'time64_t'}, {'name': 'i_mtime_sec', 'type': 'time64_t'}, {'name': 'i_ctime_sec', 'type': 'time64_t'}, {'name': 'i_atime_nsec', 'type': 'u32_'}, {'name': 'i_mtime_nsec', 'type': 'u32_'}, {'name': 'i_ctime_nsec', 'type': 'u32_'}, {'name': 'i_generation', 'type': 'u32_'}, {'name': 'i_lock', 'type': 'spinlock_t'}, {'name': 'i_bytes', 'type': 'core::ffi::c_ushort'}, {'name': 'i_blkbits', 'type': 'u8_'}, {'name': 'i_write_hint', 'type': 'rw_hint'}, {'name': 'i_blocks', 'type': 'blkcnt_t'}, {'name': 'i_state', 'type': 'core::ffi::c_ulong'}, {'name': 'i_rwsem', 'type': 'rw_semaphore'}, {'name': 'dirtied_when', 'type': 'core::ffi::c_ulong'}, {'name': 'dirtied_time_when', 'type': 'core::ffi::c_ulong'}, {'name': 'i_hash', 'type': 'hlist_node'}, {'name': 'i_io_list', 'type': 'list_head'}, {'name': 'i_lru', 'type': 'list_head'}, {'name': 'i_sb_list', 'type': 'list_head'}, {'name': 'i_wb_list', 'type': 'list_head'}, {'name': '__bindgen_anon_2', 'type': 'inode__bindgen_ty_2'}, {'name': 'i_version', 'type': 'atomic64_t'}, {'name': 'i_sequence', 'type': 'atomic64_t'}, {'name': 'i_count', 'type': 'atomic_t'}, {'name': 'i_dio_count', 'type': 'atomic_t'}, {'name': 'i_writecount', 'type': 'atomic_t'}, {'name': 'i_readcount', 'type': 'atomic_t'}, {'name': '__bindgen_anon_3', 'type': 'inode__bindgen_ty_3'}, {'name': 'i_flctx', 'type': '*mut file_lock_context'}, {'name': 'i_data', 'type': 'address_space'}, {'name': 'i_devices', 'type': 'list_head'}, {'name': '__bindgen_anon_4', 'type': 'inode__bindgen_ty_4'}, {'name': 'i_fsnotify_mask', 'type': '__u32'}, {'name': 'i_fsnotify_marks', 'type': '*mut fsnotify_mark_connector'}, {'name': 'i_private', 'type': '*mut core::ffi::c_void'}]`
- New: `[{'name': 'i_mode', 'type': 'umode_t'}, {'name': 'i_opflags', 'type': 'core::ffi::c_ushort'}, {'name': 'i_uid', 'type': 'kuid_t'}, {'name': 'i_gid', 'type': 'kgid_t'}, {'name': 'i_flags', 'type': 'core::ffi::c_uint'}, {'name': 'i_acl', 'type': '*mut posix_acl'}, {'name': 'i_default_acl', 'type': '*mut posix_acl'}, {'name': 'i_op', 'type': '*const inode_operations'}, {'name': 'i_sb', 'type': '*mut super_block'}, {'name': 'i_mapping', 'type': '*mut address_space'}, {'name': 'i_security', 'type': '*mut core::ffi::c_void'}, {'name': 'i_ino', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'inode__bindgen_ty_1'}, {'name': 'i_rdev', 'type': 'dev_t'}, {'name': 'i_size', 'type': 'loff_t'}, {'name': 'i_atime_sec', 'type': 'time64_t'}, {'name': 'i_mtime_sec', 'type': 'time64_t'}, {'name': 'i_ctime_sec', 'type': 'time64_t'}, {'name': 'i_atime_nsec', 'type': 'u32_'}, {'name': 'i_mtime_nsec', 'type': 'u32_'}, {'name': 'i_ctime_nsec', 'type': 'u32_'}, {'name': 'i_generation', 'type': 'u32_'}, {'name': 'i_lock', 'type': 'spinlock_t'}, {'name': 'i_bytes', 'type': 'core::ffi::c_ushort'}, {'name': 'i_blkbits', 'type': 'u8_'}, {'name': 'i_write_hint', 'type': 'rw_hint'}, {'name': 'i_blocks', 'type': 'blkcnt_t'}, {'name': 'i_state', 'type': 'u32_'}, {'name': 'i_rwsem', 'type': 'rw_semaphore'}, {'name': 'dirtied_when', 'type': 'core::ffi::c_ulong'}, {'name': 'dirtied_time_when', 'type': 'core::ffi::c_ulong'}, {'name': 'i_hash', 'type': 'hlist_node'}, {'name': 'i_io_list', 'type': 'list_head'}, {'name': 'i_lru', 'type': 'list_head'}, {'name': 'i_sb_list', 'type': 'list_head'}, {'name': 'i_wb_list', 'type': 'list_head'}, {'name': '__bindgen_anon_2', 'type': 'inode__bindgen_ty_2'}, {'name': 'i_version', 'type': 'atomic64_t'}, {'name': 'i_sequence', 'type': 'atomic64_t'}, {'name': 'i_count', 'type': 'atomic_t'}, {'name': 'i_dio_count', 'type': 'atomic_t'}, {'name': 'i_writecount', 'type': 'atomic_t'}, {'name': 'i_readcount', 'type': 'atomic_t'}, {'name': '__bindgen_anon_3', 'type': 'inode__bindgen_ty_3'}, {'name': 'i_flctx', 'type': '*mut file_lock_context'}, {'name': 'i_data', 'type': 'address_space'}, {'name': 'i_devices', 'type': 'list_head'}, {'name': '__bindgen_anon_4', 'type': 'inode__bindgen_ty_4'}, {'name': 'i_fsnotify_mask', 'type': '__u32'}, {'name': 'i_fsnotify_marks', 'type': '*mut fsnotify_mark_connector'}, {'name': 'i_private', 'type': '*mut core::ffi::c_void'}]`

### Rust Evidence

- Graph edges: `36`

## W-000140 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: phy_device
- Explanation: phy_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mdio', 'type': 'mdio_device'}, {'name': 'drv', 'type': '*const phy_driver'}, {'name': 'devlink', 'type': '*mut device_link'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'c45_ids', 'type': 'phy_c45_device_ids'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'rate_matching', 'type': 'core::ffi::c_int'}, {'name': 'state', 'type': 'phy_state'}, {'name': 'dev_flags', 'type': 'u32_'}, {'name': 'interface', 'type': 'phy_interface_t'}, {'name': 'possible_interfaces', 'type': '[core::ffi::c_ulong; 1usize]'}, {'name': 'speed', 'type': 'core::ffi::c_int'}, {'name': 'duplex', 'type': 'core::ffi::c_int'}, {'name': 'port', 'type': 'core::ffi::c_int'}, {'name': 'pause', 'type': 'core::ffi::c_int'}, {'name': 'asym_pause', 'type': 'core::ffi::c_int'}, {'name': 'master_slave_get', 'type': 'u8_'}, {'name': 'master_slave_set', 'type': 'u8_'}, {'name': 'master_slave_state', 'type': 'u8_'}, {'name': 'supported', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'advertising', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'lp_advertising', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'adv_old', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'supported_eee', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'advertising_eee', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'eee_enabled', 'type': 'bool_'}, {'name': 'host_interfaces', 'type': '[core::ffi::c_ulong; 1usize]'}, {'name': 'eee_broken_modes', 'type': 'u32_'}, {'name': 'enable_tx_lpi', 'type': 'bool_'}, {'name': 'eee_cfg', 'type': 'eee_config'}, {'name': 'leds', 'type': 'list_head'}, {'name': 'irq', 'type': 'core::ffi::c_int'}, {'name': 'priv_', 'type': '*mut core::ffi::c_void'}, {'name': 'shared', 'type': '*mut phy_package_shared'}, {'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'ehdr', 'type': '*mut core::ffi::c_void'}, {'name': 'nest', 'type': '*mut nlattr'}, {'name': 'state_queue', 'type': 'delayed_work'}, {'name': 'lock', 'type': 'mutex'}, {'name': 'sfp_bus_attached', 'type': 'bool_'}, {'name': 'sfp_bus', 'type': '*mut sfp_bus'}, {'name': 'phylink', 'type': '*mut phylink'}, {'name': 'attached_dev', 'type': '*mut net_device'}, {'name': 'mii_ts', 'type': '*mut mii_timestamper'}, {'name': 'psec', 'type': '*mut pse_control'}, {'name': 'mdix', 'type': 'u8_'}, {'name': 'mdix_ctrl', 'type': 'u8_'}, {'name': 'pma_extable', 'type': 'core::ffi::c_int'}, {'name': 'link_down_events', 'type': 'core::ffi::c_uint'}, {'name': 'adjust_link', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut net_device)>'}]`
- New: `[{'name': 'mdio', 'type': 'mdio_device'}, {'name': 'drv', 'type': '*const phy_driver'}, {'name': 'devlink', 'type': '*mut device_link'}, {'name': 'phyindex', 'type': 'u32_'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'c45_ids', 'type': 'phy_c45_device_ids'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'rate_matching', 'type': 'core::ffi::c_int'}, {'name': 'state', 'type': 'phy_state'}, {'name': 'dev_flags', 'type': 'u32_'}, {'name': 'interface', 'type': 'phy_interface_t'}, {'name': 'possible_interfaces', 'type': '[core::ffi::c_ulong; 1usize]'}, {'name': 'speed', 'type': 'core::ffi::c_int'}, {'name': 'duplex', 'type': 'core::ffi::c_int'}, {'name': 'port', 'type': 'core::ffi::c_int'}, {'name': 'pause', 'type': 'core::ffi::c_int'}, {'name': 'asym_pause', 'type': 'core::ffi::c_int'}, {'name': 'master_slave_get', 'type': 'u8_'}, {'name': 'master_slave_set', 'type': 'u8_'}, {'name': 'master_slave_state', 'type': 'u8_'}, {'name': 'supported', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'advertising', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'lp_advertising', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'adv_old', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'supported_eee', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'advertising_eee', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'eee_enabled', 'type': 'bool_'}, {'name': 'host_interfaces', 'type': '[core::ffi::c_ulong; 1usize]'}, {'name': 'eee_broken_modes', 'type': 'u32_'}, {'name': 'enable_tx_lpi', 'type': 'bool_'}, {'name': 'eee_cfg', 'type': 'eee_config'}, {'name': 'leds', 'type': 'list_head'}, {'name': 'irq', 'type': 'core::ffi::c_int'}, {'name': 'priv_', 'type': '*mut core::ffi::c_void'}, {'name': 'shared', 'type': '*mut phy_package_shared'}, {'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'ehdr', 'type': '*mut core::ffi::c_void'}, {'name': 'nest', 'type': '*mut nlattr'}, {'name': 'state_queue', 'type': 'delayed_work'}, {'name': 'lock', 'type': 'mutex'}, {'name': 'sfp_bus_attached', 'type': 'bool_'}, {'name': 'sfp_bus', 'type': '*mut sfp_bus'}, {'name': 'phylink', 'type': '*mut phylink'}, {'name': 'attached_dev', 'type': '*mut net_device'}, {'name': 'mii_ts', 'type': '*mut mii_timestamper'}, {'name': 'psec', 'type': '*mut pse_control'}, {'name': 'mdix', 'type': 'u8_'}, {'name': 'mdix_ctrl', 'type': 'u8_'}, {'name': 'pma_extable', 'type': 'core::ffi::c_int'}, {'name': 'link_down_events', 'type': 'core::ffi::c_uint'}, {'name': 'adjust_link', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut net_device)>'}]`

### Rust Evidence

- Graph edges: `50`

## W-000143 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: request
- Explanation: request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'q', 'type': '*mut request_queue'}, {'name': 'mq_ctx', 'type': '*mut blk_mq_ctx'}, {'name': 'mq_hctx', 'type': '*mut blk_mq_hw_ctx'}, {'name': 'cmd_flags', 'type': 'blk_opf_t'}, {'name': 'rq_flags', 'type': 'req_flags_t'}, {'name': 'tag', 'type': 'core::ffi::c_int'}, {'name': 'internal_tag', 'type': 'core::ffi::c_int'}, {'name': 'timeout', 'type': 'core::ffi::c_uint'}, {'name': '__data_len', 'type': 'core::ffi::c_uint'}, {'name': '__sector', 'type': 'sector_t'}, {'name': 'bio', 'type': '*mut bio'}, {'name': 'biotail', 'type': '*mut bio'}, {'name': '__bindgen_anon_1', 'type': 'request__bindgen_ty_1'}, {'name': 'part', 'type': '*mut block_device'}, {'name': 'alloc_time_ns', 'type': 'u64_'}, {'name': 'start_time_ns', 'type': 'u64_'}, {'name': 'io_start_time_ns', 'type': 'u64_'}, {'name': 'stats_sectors', 'type': 'core::ffi::c_ushort'}, {'name': 'nr_phys_segments', 'type': 'core::ffi::c_ushort'}, {'name': 'write_hint', 'type': 'rw_hint'}, {'name': 'ioprio', 'type': 'core::ffi::c_ushort'}, {'name': 'state', 'type': 'mq_rq_state'}, {'name': 'ref_', 'type': 'atomic_t'}, {'name': 'deadline', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_2', 'type': 'request__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'request__bindgen_ty_3'}, {'name': 'elv', 'type': 'request__bindgen_ty_4'}, {'name': 'flush', 'type': 'request__bindgen_ty_5'}, {'name': 'fifo_time', 'type': 'u64_'}, {'name': 'end_io', 'type': 'rq_end_io_fn'}, {'name': 'end_io_data', 'type': '*mut core::ffi::c_void'}]`
- New: `[{'name': 'q', 'type': '*mut request_queue'}, {'name': 'mq_ctx', 'type': '*mut blk_mq_ctx'}, {'name': 'mq_hctx', 'type': '*mut blk_mq_hw_ctx'}, {'name': 'cmd_flags', 'type': 'blk_opf_t'}, {'name': 'rq_flags', 'type': 'req_flags_t'}, {'name': 'tag', 'type': 'core::ffi::c_int'}, {'name': 'internal_tag', 'type': 'core::ffi::c_int'}, {'name': 'timeout', 'type': 'core::ffi::c_uint'}, {'name': '__data_len', 'type': 'core::ffi::c_uint'}, {'name': '__sector', 'type': 'sector_t'}, {'name': 'bio', 'type': '*mut bio'}, {'name': 'biotail', 'type': '*mut bio'}, {'name': '__bindgen_anon_1', 'type': 'request__bindgen_ty_1'}, {'name': 'part', 'type': '*mut block_device'}, {'name': 'alloc_time_ns', 'type': 'u64_'}, {'name': 'start_time_ns', 'type': 'u64_'}, {'name': 'io_start_time_ns', 'type': 'u64_'}, {'name': 'stats_sectors', 'type': 'core::ffi::c_ushort'}, {'name': 'nr_phys_segments', 'type': 'core::ffi::c_ushort'}, {'name': 'nr_integrity_segments', 'type': 'core::ffi::c_ushort'}, {'name': 'write_hint', 'type': 'rw_hint'}, {'name': 'ioprio', 'type': 'core::ffi::c_ushort'}, {'name': 'state', 'type': 'mq_rq_state'}, {'name': 'ref_', 'type': 'atomic_t'}, {'name': 'deadline', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_2', 'type': 'request__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'request__bindgen_ty_3'}, {'name': 'elv', 'type': 'request__bindgen_ty_4'}, {'name': 'flush', 'type': 'request__bindgen_ty_5'}, {'name': 'fifo_time', 'type': 'u64_'}, {'name': 'end_io', 'type': 'rq_end_io_fn'}, {'name': 'end_io_data', 'type': '*mut core::ffi::c_void'}]`

### Rust Evidence

- Graph edges: `50`

## W-000154 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: uprobe
- Explanation: uprobe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[]`

### Rust Evidence

- Graph edges: `38`

## W-000160 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: zone
- Explanation: zone changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_watermark', 'type': '[core::ffi::c_ulong; 4usize]'}, {'name': 'watermark_boost', 'type': 'core::ffi::c_ulong'}, {'name': 'nr_reserved_highatomic', 'type': 'core::ffi::c_ulong'}, {'name': 'lowmem_reserve', 'type': '[core::ffi::c_long; 4usize]'}, {'name': 'node', 'type': 'core::ffi::c_int'}, {'name': 'zone_pgdat', 'type': '*mut pglist_data'}, {'name': 'per_cpu_pageset', 'type': '*mut per_cpu_pages'}, {'name': 'per_cpu_zonestats', 'type': '*mut per_cpu_zonestat'}, {'name': 'pageset_high_min', 'type': 'core::ffi::c_int'}, {'name': 'pageset_high_max', 'type': 'core::ffi::c_int'}, {'name': 'pageset_batch', 'type': 'core::ffi::c_int'}, {'name': 'zone_start_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'managed_pages', 'type': 'atomic_long_t'}, {'name': 'spanned_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'present_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'initialized', 'type': 'core::ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': '[u64; 2usize]'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': 'free_area', 'type': '[free_area; 11usize]'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': '__bindgen_padding_1', 'type': '[u64; 3usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'percpu_drift_mark', 'type': 'core::ffi::c_ulong'}, {'name': 'compact_cached_free_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'compact_cached_migrate_pfn', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'compact_init_migrate_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'compact_init_free_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'compact_considered', 'type': 'core::ffi::c_uint'}, {'name': 'compact_defer_shift', 'type': 'core::ffi::c_uint'}, {'name': 'compact_order_failed', 'type': 'core::ffi::c_int'}, {'name': 'compact_blockskip_flush', 'type': 'bool_'}, {'name': 'contiguous', 'type': 'bool_'}, {'name': '__bindgen_padding_2', 'type': '[u64; 0usize]'}, {'name': '_pad3_', 'type': 'cacheline_padding'}, {'name': 'vm_stat', 'type': '[atomic_long_t; 10usize]'}, {'name': 'vm_numa_event', 'type': '[atomic_long_t; 6usize]'}]`
- New: `[{'name': '_watermark', 'type': '[core::ffi::c_ulong; 4usize]'}, {'name': 'watermark_boost', 'type': 'core::ffi::c_ulong'}, {'name': 'nr_reserved_highatomic', 'type': 'core::ffi::c_ulong'}, {'name': 'nr_free_highatomic', 'type': 'core::ffi::c_ulong'}, {'name': 'lowmem_reserve', 'type': '[core::ffi::c_long; 4usize]'}, {'name': 'node', 'type': 'core::ffi::c_int'}, {'name': 'zone_pgdat', 'type': '*mut pglist_data'}, {'name': 'per_cpu_pageset', 'type': '*mut per_cpu_pages'}, {'name': 'per_cpu_zonestats', 'type': '*mut per_cpu_zonestat'}, {'name': 'pageset_high_min', 'type': 'core::ffi::c_int'}, {'name': 'pageset_high_max', 'type': 'core::ffi::c_int'}, {'name': 'pageset_batch', 'type': 'core::ffi::c_int'}, {'name': 'zone_start_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'managed_pages', 'type': 'atomic_long_t'}, {'name': 'spanned_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'present_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'initialized', 'type': 'core::ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': 'u64'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': 'free_area', 'type': '[free_area; 11usize]'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': '__bindgen_padding_1', 'type': '[u64; 3usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'percpu_drift_mark', 'type': 'core::ffi::c_ulong'}, {'name': 'compact_cached_free_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'compact_cached_migrate_pfn', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'compact_init_migrate_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'compact_init_free_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'compact_considered', 'type': 'core::ffi::c_uint'}, {'name': 'compact_defer_shift', 'type': 'core::ffi::c_uint'}, {'name': 'compact_order_failed', 'type': 'core::ffi::c_int'}, {'name': 'compact_blockskip_flush', 'type': 'bool_'}, {'name': 'contiguous', 'type': 'bool_'}, {'name': '__bindgen_padding_2', 'type': '[u64; 0usize]'}, {'name': '_pad3_', 'type': 'cacheline_padding'}, {'name': 'vm_stat', 'type': '[atomic_long_t; 10usize]'}, {'name': 'vm_numa_event', 'type': '[atomic_long_t; 6usize]'}]`

### Rust Evidence

- Graph edges: `38`

## W-000086 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: rb_link_node
- Explanation: rb_link_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000006 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: __mutex_init
- Explanation: __mutex_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'lock', 'type': '*mut mutex'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'key', 'type': '*mut lock_class_key'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'mutex', 'type': '*mut mutex'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'key', 'type': '*mut lock_class_key'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `4`

## W-000034 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: dl_defer
- Explanation: dl_defer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000044 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: fdget
- Explanation: fdget changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000016 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: arch_get_unmapped_area
- Explanation: arch_get_unmapped_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut file'}, {'name': 'arg2', 'type': 'core::ffi::c_ulong'}, {'name': 'arg3', 'type': 'core::ffi::c_ulong'}, {'name': 'arg4', 'type': 'core::ffi::c_ulong'}, {'name': 'arg5', 'type': 'core::ffi::c_ulong'}], 'return_type': 'core::ffi::c_ulong'}`
- New: `{'params': [{'name': 'filp', 'type': '*mut file'}, {'name': 'addr', 'type': 'core::ffi::c_ulong'}, {'name': 'len', 'type': 'core::ffi::c_ulong'}, {'name': 'pgoff', 'type': 'core::ffi::c_ulong'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_flags', 'type': 'vm_flags_t'}], 'return_type': 'core::ffi::c_ulong'}`

### Rust Evidence

- Graph edges: `2`

## W-000054 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: generic_get_unmapped_area
- Explanation: generic_get_unmapped_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'filp', 'type': '*mut file'}, {'name': 'addr', 'type': 'core::ffi::c_ulong'}, {'name': 'len', 'type': 'core::ffi::c_ulong'}, {'name': 'pgoff', 'type': 'core::ffi::c_ulong'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}], 'return_type': 'core::ffi::c_ulong'}`
- New: `{'params': [{'name': 'filp', 'type': '*mut file'}, {'name': 'addr', 'type': 'core::ffi::c_ulong'}, {'name': 'len', 'type': 'core::ffi::c_ulong'}, {'name': 'pgoff', 'type': 'core::ffi::c_ulong'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_flags', 'type': 'vm_flags_t'}], 'return_type': 'core::ffi::c_ulong'}`

### Rust Evidence

- Graph edges: `2`

## W-000114 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: uprobe_unregister
- Explanation: uprobe_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `2`

## W-000005 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kmem_cache_create_args
- Explanation: __kmem_cache_create_args changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000007 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __printk_deferred_enter
- Explanation: __printk_deferred_enter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000008 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __printk_deferred_exit
- Explanation: __printk_deferred_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000011 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_node_data
- Explanation: alloc_node_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000012 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_offline_node_data
- Explanation: alloc_offline_node_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000013 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: amd_get_highest_perf
- Explanation: amd_get_highest_perf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000014 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_check_zapped_pud
- Explanation: arch_check_zapped_pud changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000015 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_enable_hybrid_capacity_scale
- Explanation: arch_enable_hybrid_capacity_scale changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000017 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_get_unmapped_area_topdown
- Explanation: arch_get_unmapped_area_topdown changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'filp', 'type': '*mut file'}, {'name': 'addr', 'type': 'core::ffi::c_ulong'}, {'name': 'len', 'type': 'core::ffi::c_ulong'}, {'name': 'pgoff', 'type': 'core::ffi::c_ulong'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}], 'return_type': 'core::ffi::c_ulong'}`
- New: `{'params': [{'name': 'filp', 'type': '*mut file'}, {'name': 'addr', 'type': 'core::ffi::c_ulong'}, {'name': 'len', 'type': 'core::ffi::c_ulong'}, {'name': 'pgoff', 'type': 'core::ffi::c_ulong'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'arg1', 'type': 'vm_flags_t'}], 'return_type': 'core::ffi::c_ulong'}`

### Rust Evidence

- Graph edges: `1`

## W-000020 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_scale_cpu_capacity
- Explanation: arch_scale_cpu_capacity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000021 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_set_cpu_capacity
- Explanation: arch_set_cpu_capacity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000022 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_split_rw
- Explanation: bio_split_rw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000023 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_split_rw_at
- Explanation: bio_split_rw_at changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000026 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: build_id_parse_nofault
- Explanation: build_id_parse_nofault changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000027 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bus_find_device
- Explanation: bus_find_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'bus', 'type': '*const bus_type'}, {'name': 'start', 'type': '*mut device'}, {'name': 'data', 'type': '*const core::ffi::c_void'}, {'name': 'match_', 'type': '::core::option::Option< unsafe extern "C" fn( dev: *mut device, data: *const core::ffi::c_void,'}], 'return_type': 'core::ffi::c_int, >, ) -> *mut device'}`
- New: `{'params': [{'name': 'bus', 'type': '*const bus_type'}, {'name': 'start', 'type': '*mut device'}, {'name': 'data', 'type': '*const core::ffi::c_void'}, {'name': 'match_', 'type': 'device_match_t'}], 'return_type': '*mut device'}`

### Rust Evidence

- Graph edges: `1`

## W-000028 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_find_device
- Explanation: class_find_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'class', 'type': '*const class'}, {'name': 'start', 'type': '*const device'}, {'name': 'data', 'type': '*const core::ffi::c_void'}, {'name': 'match_', 'type': '::core::option::Option< unsafe extern "C" fn( arg1: *mut device, arg2: *const core::ffi::c_void,'}], 'return_type': 'core::ffi::c_int, >, ) -> *mut device'}`
- New: `{'params': [{'name': 'class', 'type': '*const class'}, {'name': 'start', 'type': '*const device'}, {'name': 'data', 'type': '*const core::ffi::c_void'}, {'name': 'match_', 'type': 'device_match_t'}], 'return_type': '*mut device'}`

### Rust Evidence

- Graph edges: `1`

## W-000030 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_init_exception_handling
- Explanation: cpu_init_exception_handling changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': '()'}`
- New: `{'params': [{'name': 'boot_cpu', 'type': 'bool_'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000031 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_init_replace_early_idt
- Explanation: cpu_init_replace_early_idt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000032 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dequeue_signal
- Explanation: dequeue_signal changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'task', 'type': '*mut task_struct'}, {'name': 'mask', 'type': '*mut sigset_t'}, {'name': 'info', 'type': '*mut kernel_siginfo_t'}, {'name': 'type_', 'type': '*mut pid_type'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'mask', 'type': '*mut sigset_t'}, {'name': 'info', 'type': '*mut kernel_siginfo_t'}, {'name': 'type_', 'type': '*mut pid_type'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000033 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_for_each_child_reverse_from
- Explanation: device_for_each_child_reverse_from changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000035 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dl_defer_armed
- Explanation: dl_defer_armed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000036 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dl_defer_running
- Explanation: dl_defer_running changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000037 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_iommu
- Explanation: dma_iommu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000038 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_mseal
- Explanation: do_mseal changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000040 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_vmi_align_munmap
- Explanation: do_vmi_align_munmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000041 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: driver_find_device
- Explanation: driver_find_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'drv', 'type': '*const device_driver'}, {'name': 'start', 'type': '*mut device'}, {'name': 'data', 'type': '*const core::ffi::c_void'}, {'name': 'match_', 'type': '::core::option::Option< unsafe extern "C" fn( dev: *mut device, data: *const core::ffi::c_void,'}], 'return_type': 'core::ffi::c_int, >, ) -> *mut device'}`
- New: `{'params': [{'name': 'drv', 'type': '*const device_driver'}, {'name': 'start', 'type': '*mut device'}, {'name': 'data', 'type': '*const core::ffi::c_void'}, {'name': 'match_', 'type': 'device_match_t'}], 'return_type': '*mut device'}`

### Rust Evidence

- Graph edges: `1`

## W-000042 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: elf_coredump_extra_notes_size
- Explanation: elf_coredump_extra_notes_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000043 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: elf_coredump_extra_notes_write
- Explanation: elf_coredump_extra_notes_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000045 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fdget_pos
- Explanation: fdget_pos changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000046 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fdget_raw
- Explanation: fdget_raw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000047 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: file_f_owner_allocate
- Explanation: file_f_owner_allocate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000051 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: follow_pfnmap_end
- Explanation: follow_pfnmap_end changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000052 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: follow_pfnmap_start
- Explanation: follow_pfnmap_start changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000055 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_get_unmapped_area_topdown
- Explanation: generic_get_unmapped_area_topdown changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'filp', 'type': '*mut file'}, {'name': 'addr', 'type': 'core::ffi::c_ulong'}, {'name': 'len', 'type': 'core::ffi::c_ulong'}, {'name': 'pgoff', 'type': 'core::ffi::c_ulong'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}], 'return_type': 'core::ffi::c_ulong'}`
- New: `{'params': [{'name': 'filp', 'type': '*mut file'}, {'name': 'addr', 'type': 'core::ffi::c_ulong'}, {'name': 'len', 'type': 'core::ffi::c_ulong'}, {'name': 'pgoff', 'type': 'core::ffi::c_ulong'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_flags', 'type': 'vm_flags_t'}], 'return_type': 'core::ffi::c_ulong'}`

### Rust Evidence

- Graph edges: `1`

## W-000056 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_llseek_cookie
- Explanation: generic_llseek_cookie changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000057 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inc_rlimit_get_ucounts
- Explanation: inc_rlimit_get_ucounts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'ucounts', 'type': '*mut ucounts'}, {'name': 'type_', 'type': 'rlimit_type'}], 'return_type': 'core::ffi::c_long'}`
- New: `{'params': [{'name': 'ucounts', 'type': '*mut ucounts'}, {'name': 'type_', 'type': 'rlimit_type'}, {'name': 'override_rlimit', 'type': 'bool_'}], 'return_type': 'core::ffi::c_long'}`

### Rust Evidence

- Graph edges: `1`

## W-000059 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_bit_waitqueue
- Explanation: inode_bit_waitqueue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000060 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_dio_finished
- Explanation: inode_dio_finished changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000061 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_dio_wait_interruptible
- Explanation: inode_dio_wait_interruptible changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000062 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_init_always
- Explanation: inode_init_always changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000063 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_init_always_gfp
- Explanation: inode_init_always_gfp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000065 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iov_iter_folio_queue
- Explanation: iov_iter_folio_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000066 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_pte_init
- Explanation: kernel_pte_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000068 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmem_cache_charge
- Explanation: kmem_cache_charge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000071 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kvfree_rcu_barrier
- Explanation: kvfree_rcu_barrier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000072 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kvrealloc_noprof
- Explanation: kvrealloc_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'p', 'type': '*const core::ffi::c_void'}, {'name': 'oldsize', 'type': 'usize'}, {'name': 'newsize', 'type': 'usize'}, {'name': 'flags', 'type': 'gfp_t'}], 'return_type': '*mut core::ffi::c_void'}`
- New: `{'params': [{'name': 'p', 'type': '*const core::ffi::c_void'}, {'name': 'size', 'type': 'usize'}, {'name': 'flags', 'type': 'gfp_t'}], 'return_type': '*mut core::ffi::c_void'}`

### Rust Evidence

- Graph edges: `1`

## W-000074 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: nbcon_atomic_flush_unsafe
- Explanation: nbcon_atomic_flush_unsafe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000075 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: nbcon_device_release
- Explanation: nbcon_device_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000076 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: nbcon_device_try_acquire
- Explanation: nbcon_device_try_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000077 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_bitfield_2
- Explanation: new_bitfield_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'tstamp_type', 'type': '__u8'}, {'name': 'tc_at_ingress', 'type': '__u8'}, {'name': 'tc_skip_classify', 'type': '__u8'}, {'name': 'remcsum_offload', 'type': '__u8'}, {'name': 'csum_complete_sw', 'type': '__u8'}, {'name': 'csum_level', 'type': '__u8'}, {'name': 'inner_protocol_type', 'type': '__u8'}, {'name': 'l4_hash', 'type': '__u8'}, {'name': 'sw_hash', 'type': '__u8'}, {'name': 'wifi_acked_valid', 'type': '__u8'}, {'name': 'wifi_acked', 'type': '__u8'}, {'name': 'no_fcs', 'type': '__u8'}, {'name': 'encapsulation', 'type': '__u8'}, {'name': 'encap_hdr_csum', 'type': '__u8'}, {'name': 'csum_valid', 'type': '__u8'}, {'name': 'ndisc_nodetype', 'type': '__u8'}, {'name': 'redirected', 'type': '__u8'}, {'name': 'nf_skip_egress', 'type': '__u8'}, {'name': 'slow_gro', 'type': '__u8'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`
- New: `{'params': [{'name': 'tstamp_type', 'type': '__u8'}, {'name': 'tc_at_ingress', 'type': '__u8'}, {'name': 'tc_skip_classify', 'type': '__u8'}, {'name': 'remcsum_offload', 'type': '__u8'}, {'name': 'csum_complete_sw', 'type': '__u8'}, {'name': 'csum_level', 'type': '__u8'}, {'name': 'inner_protocol_type', 'type': '__u8'}, {'name': 'l4_hash', 'type': '__u8'}, {'name': 'sw_hash', 'type': '__u8'}, {'name': 'wifi_acked_valid', 'type': '__u8'}, {'name': 'wifi_acked', 'type': '__u8'}, {'name': 'no_fcs', 'type': '__u8'}, {'name': 'encapsulation', 'type': '__u8'}, {'name': 'encap_hdr_csum', 'type': '__u8'}, {'name': 'csum_valid', 'type': '__u8'}, {'name': 'ndisc_nodetype', 'type': '__u8'}, {'name': 'redirected', 'type': '__u8'}, {'name': 'nf_skip_egress', 'type': '__u8'}, {'name': 'slow_gro', 'type': '__u8'}, {'name': 'unreadable', 'type': '__u8'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`

### Rust Evidence

- Graph edges: `1`

## W-000078 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: of_peak
- Explanation: of_peak changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000079 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: open_softirq
- Explanation: open_softirq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'nr', 'type': 'core::ffi::c_int'}, {'name': 'action', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut softirq_action)>'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'nr', 'type': 'core::ffi::c_int'}, {'name': 'action', 'type': '::core::option::Option<unsafe extern "C" fn()>'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000082 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_sfp_connect_phy
- Explanation: phy_sfp_connect_phy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000083 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_sfp_disconnect_phy
- Explanation: phy_sfp_disconnect_phy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000084 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: printk_legacy_allow_panic_sync
- Explanation: printk_legacy_allow_panic_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000085 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pudp_invalidate
- Explanation: pudp_invalidate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000089 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rcu_momentary_eqs
- Explanation: rcu_momentary_eqs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000090 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rcu_tasks_torture_stats_print
- Explanation: rcu_tasks_torture_stats_print changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000091 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: register_quota_format
- Explanation: register_quota_format changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'fmt', 'type': '*mut quota_format_type'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'fmt', 'type': '*mut quota_format_type'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000092 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: relocate_vma_down
- Explanation: relocate_vma_down changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000093 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rxfh_per_ctx_key
- Explanation: rxfh_per_ctx_key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000094 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sched_cancel_fork
- Explanation: sched_cancel_fork changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000095 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sched_cgroup_fork
- Explanation: sched_cgroup_fork changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'p', 'type': '*mut task_struct'}, {'name': 'kargs', 'type': '*mut kernel_clone_args'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'p', 'type': '*mut task_struct'}, {'name': 'kargs', 'type': '*mut kernel_clone_args'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000096 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_bdev_alloc
- Explanation: security_bdev_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000097 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_bdev_free
- Explanation: security_bdev_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000098 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_bdev_setintegrity
- Explanation: security_bdev_setintegrity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000099 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_initramfs_populated
- Explanation: security_initramfs_populated changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000100 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_alloc
- Explanation: security_inode_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'inode', 'type': '*mut inode'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'inode', 'type': '*mut inode'}, {'name': 'gfp', 'type': 'gfp_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000101 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_setintegrity
- Explanation: security_inode_setintegrity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000102 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: send_sigurg
- Explanation: send_sigurg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'fown', 'type': '*mut fown_struct'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'file', 'type': '*mut file'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000104 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_write_begin
- Explanation: simple_write_begin changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'file', 'type': '*mut file'}, {'name': 'mapping', 'type': '*mut address_space'}, {'name': 'pos', 'type': 'loff_t'}, {'name': 'len', 'type': 'core::ffi::c_uint'}, {'name': 'pagep', 'type': '*mut *mut page'}, {'name': 'fsdata', 'type': '*mut *mut core::ffi::c_void'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'file', 'type': '*mut file'}, {'name': 'mapping', 'type': '*mut address_space'}, {'name': 'pos', 'type': 'loff_t'}, {'name': 'len', 'type': 'core::ffi::c_uint'}, {'name': 'foliop', 'type': '*mut *mut folio'}, {'name': 'fsdata', 'type': '*mut *mut core::ffi::c_void'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000105 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_copy_seq_read
- Explanation: skb_copy_seq_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000106 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_not_used
- Explanation: stack_not_used changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000109 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unpin_user_folio
- Explanation: unpin_user_folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000110 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unreadable
- Explanation: unreadable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000111 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: uprobe_apply
- Explanation: uprobe_apply changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'inode', 'type': '*mut inode'}, {'name': 'offset', 'type': 'loff_t'}, {'name': 'uc', 'type': '*mut uprobe_consumer'}, {'name': 'arg1', 'type': 'bool_'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'uprobe', 'type': '*mut uprobe'}, {'name': 'uc', 'type': '*mut uprobe_consumer'}, {'name': 'arg1', 'type': 'bool_'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000112 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: uprobe_register
- Explanation: uprobe_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'inode', 'type': '*mut inode'}, {'name': 'offset', 'type': 'loff_t'}, {'name': 'uc', 'type': '*mut uprobe_consumer'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'inode', 'type': '*mut inode'}, {'name': 'offset', 'type': 'loff_t'}, {'name': 'ref_ctr_offset', 'type': 'loff_t'}, {'name': 'uc', 'type': '*mut uprobe_consumer'}], 'return_type': '*mut uprobe'}`

### Rust Evidence

- Graph edges: `1`

## W-000115 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: uprobe_unregister_nosync
- Explanation: uprobe_unregister_nosync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000116 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: uprobe_unregister_sync
- Explanation: uprobe_unregister_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000316 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kvrealloc_noprof
- Explanation: kvrealloc_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const void *p', 'size_t oldsize', 'size_t newsize', 'gfp_t flags) __realloc_size(3'], 'return_type': 'extern void *'}`
- New: `{'params': ['const void *p', 'size_t size', 'gfp_t flags) __realloc_size(2'], 'return_type': 'void *'}`

### Rust Evidence

- Graph edges: `1`

## W-000132 FieldDrift

- Risk: High
- Score: 10.6
- Symbol: fd
- Explanation: fd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'file', 'type': '*mut file'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}]`
- New: `[{'name': 'word', 'type': 'core::ffi::c_ulong'}]`

### Rust Evidence

- Graph edges: `10`

## W-000139 FieldDrift

- Risk: High
- Score: 10.4
- Symbol: page_counter
- Explanation: page_counter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'usage', 'type': 'atomic_long_t'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': 'emin', 'type': 'core::ffi::c_ulong'}, {'name': 'min_usage', 'type': 'atomic_long_t'}, {'name': 'children_min_usage', 'type': 'atomic_long_t'}, {'name': 'elow', 'type': 'core::ffi::c_ulong'}, {'name': 'low_usage', 'type': 'atomic_long_t'}, {'name': 'children_low_usage', 'type': 'atomic_long_t'}, {'name': 'watermark', 'type': 'core::ffi::c_ulong'}, {'name': 'failcnt', 'type': 'core::ffi::c_ulong'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'min', 'type': 'core::ffi::c_ulong'}, {'name': 'low', 'type': 'core::ffi::c_ulong'}, {'name': 'high', 'type': 'core::ffi::c_ulong'}, {'name': 'max', 'type': 'core::ffi::c_ulong'}, {'name': 'parent', 'type': '*mut page_counter'}]`
- New: `[{'name': 'usage', 'type': 'atomic_long_t'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': 'emin', 'type': 'core::ffi::c_ulong'}, {'name': 'min_usage', 'type': 'atomic_long_t'}, {'name': 'children_min_usage', 'type': 'atomic_long_t'}, {'name': 'elow', 'type': 'core::ffi::c_ulong'}, {'name': 'low_usage', 'type': 'atomic_long_t'}, {'name': 'children_low_usage', 'type': 'atomic_long_t'}, {'name': 'watermark', 'type': 'core::ffi::c_ulong'}, {'name': 'local_watermark', 'type': 'core::ffi::c_ulong'}, {'name': 'failcnt', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_padding_1', 'type': '[u64; 7usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'protection_support', 'type': 'bool_'}, {'name': 'min', 'type': 'core::ffi::c_ulong'}, {'name': 'low', 'type': 'core::ffi::c_ulong'}, {'name': 'high', 'type': 'core::ffi::c_ulong'}, {'name': 'max', 'type': 'core::ffi::c_ulong'}, {'name': 'parent', 'type': '*mut page_counter'}]`

### Rust Evidence

- Graph edges: `9`

## W-000150 FieldDrift

- Risk: High
- Score: 10.4
- Symbol: task_struct
- Explanation: task_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'core::ffi::c_uint'}, {'name': 'saved_state', 'type': 'core::ffi::c_uint'}, {'name': 'stack', 'type': '*mut core::ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'ptrace', 'type': 'core::ffi::c_uint'}, {'name': 'on_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'core::ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'core::ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_cpu', 'type': 'core::ffi::c_int'}, {'name': 'on_rq', 'type': 'core::ffi::c_int'}, {'name': 'prio', 'type': 'core::ffi::c_int'}, {'name': 'static_prio', 'type': 'core::ffi::c_int'}, {'name': 'normal_prio', 'type': 'core::ffi::c_int'}, {'name': 'rt_priority', 'type': 'core::ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'dl_server', 'type': '*mut sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'core::ffi::c_uint'}, {'name': 'policy', 'type': 'core::ffi::c_uint'}, {'name': 'max_allowed_capacity', 'type': 'core::ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'core::ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut core::ffi::c_void'}, {'name': 'migration_disabled', 'type': 'core::ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'core::ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'core::ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'core::ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'rcu_tasks_exit_cpu', 'type': 'core::ffi::c_int'}, {'name': 'rcu_tasks_exit_list', 'type': 'list_head'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'faults_disabled_mapping', 'type': '*mut address_space'}, {'name': 'exit_state', 'type': 'core::ffi::c_int'}, {'name': 'exit_code', 'type': 'core::ffi::c_int'}, {'name': 'exit_signal', 'type': 'core::ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'core::ffi::c_int'}, {'name': 'jobctl', 'type': 'core::ffi::c_ulong'}, {'name': 'personality', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'core::ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'worker_private', 'type': '*mut core::ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[core::ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'core::ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'core::ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'core::ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'journal_info', 'type': '*mut core::ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'core::ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cpuset_slab_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'core::ffi::c_uint'}, {'name': 'perf_recursion', 'type': '[u8_; 4usize]'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'core::ffi::c_short'}, {'name': 'il_weight', 'type': 'u8_'}, {'name': 'pref_node_fork', 'type': 'core::ffi::c_short'}, {'name': 'rseq', 'type': '*mut rseq'}, {'name': 'rseq_len', 'type': 'u32_'}, {'name': 'rseq_sig', 'type': 'u32_'}, {'name': 'rseq_event_mask', 'type': 'core::ffi::c_ulong'}, {'name': 'mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'last_mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'migrate_from_cpu', 'type': 'core::ffi::c_int'}, {'name': 'mm_cid_active', 'type': 'core::ffi::c_int'}, {'name': 'cid_work', 'type': 'callback_head'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'core::ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'core::ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'core::ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'core::ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'core::ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut core::ffi::c_void'}, {'name': 'bpf_net_context', 'type': '*mut bpf_net_context'}, {'name': 'mce_vaddr', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'core::ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': '__bindgen_padding_1', 'type': '[u64; 5usize]'}, {'name': 'thread', 'type': 'thread_struct'}]`
- New: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'core::ffi::c_uint'}, {'name': 'saved_state', 'type': 'core::ffi::c_uint'}, {'name': 'stack', 'type': '*mut core::ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'ptrace', 'type': 'core::ffi::c_uint'}, {'name': 'on_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'core::ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'core::ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_cpu', 'type': 'core::ffi::c_int'}, {'name': 'on_rq', 'type': 'core::ffi::c_int'}, {'name': 'prio', 'type': 'core::ffi::c_int'}, {'name': 'static_prio', 'type': 'core::ffi::c_int'}, {'name': 'normal_prio', 'type': 'core::ffi::c_int'}, {'name': 'rt_priority', 'type': 'core::ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'dl_server', 'type': '*mut sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'core::ffi::c_uint'}, {'name': 'policy', 'type': 'core::ffi::c_uint'}, {'name': 'max_allowed_capacity', 'type': 'core::ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'core::ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut core::ffi::c_void'}, {'name': 'migration_disabled', 'type': 'core::ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'core::ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'core::ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'core::ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'rcu_tasks_exit_cpu', 'type': 'core::ffi::c_int'}, {'name': 'rcu_tasks_exit_list', 'type': 'list_head'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'faults_disabled_mapping', 'type': '*mut address_space'}, {'name': 'exit_state', 'type': 'core::ffi::c_int'}, {'name': 'exit_code', 'type': 'core::ffi::c_int'}, {'name': 'exit_signal', 'type': 'core::ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'core::ffi::c_int'}, {'name': 'jobctl', 'type': 'core::ffi::c_ulong'}, {'name': 'personality', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'core::ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'worker_private', 'type': '*mut core::ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[core::ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'core::ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'core::ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'core::ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'journal_info', 'type': '*mut core::ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'core::ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'core::ffi::c_uint'}, {'name': 'perf_recursion', 'type': '[u8_; 4usize]'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'core::ffi::c_short'}, {'name': 'il_weight', 'type': 'u8_'}, {'name': 'pref_node_fork', 'type': 'core::ffi::c_short'}, {'name': 'rseq', 'type': '*mut rseq'}, {'name': 'rseq_len', 'type': 'u32_'}, {'name': 'rseq_sig', 'type': 'u32_'}, {'name': 'rseq_event_mask', 'type': 'core::ffi::c_ulong'}, {'name': 'mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'last_mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'migrate_from_cpu', 'type': 'core::ffi::c_int'}, {'name': 'mm_cid_active', 'type': 'core::ffi::c_int'}, {'name': 'cid_work', 'type': 'callback_head'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'core::ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'core::ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'core::ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'core::ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'core::ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut core::ffi::c_void'}, {'name': 'bpf_net_context', 'type': '*mut bpf_net_context'}, {'name': 'mce_vaddr', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'core::ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': '__bindgen_padding_1', 'type': '[u64; 6usize]'}, {'name': 'thread', 'type': 'thread_struct'}]`

### Rust Evidence

- Graph edges: `9`

## W-000156 FieldDrift

- Risk: High
- Score: 10.0
- Symbol: uprobe_task
- Explanation: uprobe_task changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'state', 'type': 'uprobe_task_state'}, {'name': '__bindgen_anon_1', 'type': 'uprobe_task__bindgen_ty_1'}, {'name': 'active_uprobe', 'type': '*mut uprobe'}, {'name': 'xol_vaddr', 'type': 'core::ffi::c_ulong'}, {'name': 'return_instances', 'type': '*mut return_instance'}, {'name': 'depth', 'type': 'core::ffi::c_uint'}]`
- New: `[{'name': 'state', 'type': 'uprobe_task_state'}, {'name': '__bindgen_anon_1', 'type': 'uprobe_task__bindgen_ty_1'}, {'name': 'active_uprobe', 'type': '*mut uprobe'}, {'name': 'xol_vaddr', 'type': 'core::ffi::c_ulong'}, {'name': 'auprobe', 'type': '*mut arch_uprobe'}, {'name': 'return_instances', 'type': '*mut return_instance'}, {'name': 'depth', 'type': 'core::ffi::c_uint'}]`

### Rust Evidence

- Graph edges: `7`

## W-000001 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __fdget
- Explanation: __fdget changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000002 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __fdget_pos
- Explanation: __fdget_pos changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000003 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __fdget_raw
- Explanation: __fdget_raw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000004 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __iget
- Explanation: __iget changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000009 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __printk_safe_enter
- Explanation: __printk_safe_enter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000010 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __printk_safe_exit
- Explanation: __printk_safe_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000018 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: arch_get_unmapped_area_topdown_vmflags
- Explanation: arch_get_unmapped_area_topdown_vmflags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000019 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: arch_get_unmapped_area_vmflags
- Explanation: arch_get_unmapped_area_vmflags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000024 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: blk_limits_io_min
- Explanation: blk_limits_io_min changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000025 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: blk_limits_io_opt
- Explanation: blk_limits_io_opt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000029 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: copy_vma
- Explanation: copy_vma changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000039 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: do_vma_munmap
- Explanation: do_vma_munmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000048 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: find_mergeable_anon_vma
- Explanation: find_mergeable_anon_vma changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000049 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: fixup_bug
- Explanation: fixup_bug changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000050 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: follow_page
- Explanation: follow_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000053 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: follow_pte
- Explanation: follow_pte changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000058 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: init_freq_invariance_cppc
- Explanation: init_freq_invariance_cppc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000064 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: install_special_mapping
- Explanation: install_special_mapping changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000067 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: keyring_add_key
- Explanation: keyring_add_key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000069 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: kmem_cache_create
- Explanation: kmem_cache_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000070 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: kmem_cache_create_usercopy
- Explanation: kmem_cache_create_usercopy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000073 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: move_page_tables
- Explanation: move_page_tables changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000080 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: page_counter_calculate_protection
- Explanation: page_counter_calculate_protection changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000081 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: pcpu_alloc_size
- Explanation: pcpu_alloc_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000087 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: rcu_barrier_tasks_rude
- Explanation: rcu_barrier_tasks_rude changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000088 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: rcu_momentary_dyntick_idle
- Explanation: rcu_momentary_dyntick_idle changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000103 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: set_nx
- Explanation: set_nx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000107 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: topology_init_cpu_capacity_cppc
- Explanation: topology_init_cpu_capacity_cppc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000108 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: unlink_file_vma
- Explanation: unlink_file_vma changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000113 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: uprobe_register_refctr
- Explanation: uprobe_register_refctr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000117 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vma_expand
- Explanation: vma_expand changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000118 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vma_modify
- Explanation: vma_modify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000119 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vma_needs_dirty_tracking
- Explanation: vma_needs_dirty_tracking changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000120 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vma_shrink
- Explanation: vma_shrink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000121 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vma_wants_writenotify
- Explanation: vma_wants_writenotify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000152 FieldDrift

- Risk: Medium
- Score: 9.6
- Symbol: uid_gid_map
- Explanation: uid_gid_map changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'nr_extents', 'type': 'u32_'}, {'name': '__bindgen_anon_1', 'type': 'uid_gid_map__bindgen_ty_1'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'uid_gid_map__bindgen_ty_1'}]`

### Rust Evidence

- Graph edges: `5`

## W-000313 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_sched_start
- Explanation: drm_sched_start changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_gpu_scheduler *sched', 'bool full_recovery'], 'return_type': 'void'}`
- New: `{'params': ['struct drm_gpu_scheduler *sched'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000314 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_sched_wakeup
- Explanation: drm_sched_wakeup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_gpu_scheduler *sched', 'struct drm_sched_entity *entity'], 'return_type': 'void'}`
- New: `{'params': ['struct drm_gpu_scheduler *sched'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000315 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: kmem_cache_create_usercopy
- Explanation: kmem_cache_create_usercopy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const char *name', 'unsigned int size', 'unsigned int align', 'slab_flags_t flags', 'unsigned int useroffset', 'unsigned int usersize', 'void (*ctor)(void *)'], 'return_type': 'struct kmem_cache *'}`
- New: `{'params': ['const char *name', 'unsigned int size', 'unsigned int align', 'slab_flags_t flags', 'unsigned int useroffset', 'unsigned int usersize', 'void (*ctor)(void *)'], 'return_type': 'static inline struct kmem_cache *'}`

### Rust Evidence

- Graph edges: `0`

## W-000317 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: queue_limits_max_zone_append_sectors
- Explanation: queue_limits_max_zone_append_sectors changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct queue_limits *l'], 'return_type': 'static inline unsigned int'}`
- New: `{'params': ['const struct queue_limits *l'], 'return_type': 'static inline unsigned int'}`

### Rust Evidence

- Graph edges: `0`

## W-000318 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: simd_skcipher_create_compat
- Explanation: simd_skcipher_create_compat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const char *algname', 'const char *drvname', 'const char *basename'], 'return_type': 'struct simd_skcipher_alg *'}`
- New: `{'params': ['struct skcipher_alg *ialg', 'const char *algname', 'const char *drvname', 'const char *basename'], 'return_type': 'struct simd_skcipher_alg *'}`

### Rust Evidence

- Graph edges: `0`

## W-000319 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ttm_bo_swapout
- Explanation: ttm_bo_swapout changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct ttm_buffer_object *bo', 'struct ttm_operation_ctx *ctx', 'gfp_t gfp_flags'], 'return_type': 'int'}`
- New: `{'params': ['struct ttm_device *bdev', 'struct ttm_operation_ctx *ctx', 'struct ttm_resource_manager *man', 'gfp_t gfp_flags', 's64 target'], 'return_type': 's64'}`

### Rust Evidence

- Graph edges: `0`

## W-000320 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ttm_resource_manager_next
- Explanation: ttm_resource_manager_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct ttm_resource_manager *man', 'struct ttm_resource_cursor *cursor', 'struct ttm_resource *res'], 'return_type': 'struct ttm_resource *'}`
- New: `{'params': ['struct ttm_resource_cursor *cursor'], 'return_type': 'struct ttm_resource *'}`

### Rust Evidence

- Graph edges: `0`

## W-000124 FieldDrift

- Risk: Medium
- Score: 9.4
- Symbol: bpf_func_proto
- Explanation: bpf_func_proto changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'func', 'type': '::core::option::Option<'}, {'name': 'gpl_only', 'type': 'bool_'}, {'name': 'pkt_access', 'type': 'bool_'}, {'name': 'might_sleep', 'type': 'bool_'}, {'name': 'ret_type', 'type': 'bpf_return_type'}, {'name': '__bindgen_anon_1', 'type': 'bpf_func_proto__bindgen_ty_1'}, {'name': '__bindgen_anon_2', 'type': 'bpf_func_proto__bindgen_ty_2'}, {'name': 'ret_btf_id', 'type': '*mut core::ffi::c_int'}, {'name': 'allowed', 'type': '::core::option::Option<unsafe extern "C" fn(prog: *const bpf_prog) -> bool_>'}]`
- New: `[{'name': 'func', 'type': '::core::option::Option<'}, {'name': 'gpl_only', 'type': 'bool_'}, {'name': 'pkt_access', 'type': 'bool_'}, {'name': 'might_sleep', 'type': 'bool_'}, {'name': 'allow_fastcall', 'type': 'bool_'}, {'name': 'ret_type', 'type': 'bpf_return_type'}, {'name': '__bindgen_anon_1', 'type': 'bpf_func_proto__bindgen_ty_1'}, {'name': '__bindgen_anon_2', 'type': 'bpf_func_proto__bindgen_ty_2'}, {'name': 'ret_btf_id', 'type': '*mut core::ffi::c_int'}, {'name': 'allowed', 'type': '::core::option::Option<unsafe extern "C" fn(prog: *const bpf_prog) -> bool_>'}]`

### Rust Evidence

- Graph edges: `4`

## W-000123 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: block_device
- Explanation: block_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'bd_start_sect', 'type': 'sector_t'}, {'name': 'bd_nr_sectors', 'type': 'sector_t'}, {'name': 'bd_disk', 'type': '*mut gendisk'}, {'name': 'bd_queue', 'type': '*mut request_queue'}, {'name': 'bd_stats', 'type': '*mut disk_stats'}, {'name': 'bd_stamp', 'type': 'core::ffi::c_ulong'}, {'name': '__bd_flags', 'type': 'atomic_t'}, {'name': 'bd_dev', 'type': 'dev_t'}, {'name': 'bd_mapping', 'type': '*mut address_space'}, {'name': 'bd_openers', 'type': 'atomic_t'}, {'name': 'bd_size_lock', 'type': 'spinlock_t'}, {'name': 'bd_claiming', 'type': '*mut core::ffi::c_void'}, {'name': 'bd_holder', 'type': '*mut core::ffi::c_void'}, {'name': 'bd_holder_ops', 'type': '*const blk_holder_ops'}, {'name': 'bd_holder_lock', 'type': 'mutex'}, {'name': 'bd_holders', 'type': 'core::ffi::c_int'}, {'name': 'bd_holder_dir', 'type': '*mut kobject'}, {'name': 'bd_fsfreeze_count', 'type': 'atomic_t'}, {'name': 'bd_fsfreeze_mutex', 'type': 'mutex'}, {'name': 'bd_meta_info', 'type': '*mut partition_meta_info'}, {'name': 'bd_writers', 'type': 'core::ffi::c_int'}, {'name': 'bd_device', 'type': 'device'}]`
- New: `[{'name': 'bd_start_sect', 'type': 'sector_t'}, {'name': 'bd_nr_sectors', 'type': 'sector_t'}, {'name': 'bd_disk', 'type': '*mut gendisk'}, {'name': 'bd_queue', 'type': '*mut request_queue'}, {'name': 'bd_stats', 'type': '*mut disk_stats'}, {'name': 'bd_stamp', 'type': 'core::ffi::c_ulong'}, {'name': '__bd_flags', 'type': 'atomic_t'}, {'name': 'bd_dev', 'type': 'dev_t'}, {'name': 'bd_mapping', 'type': '*mut address_space'}, {'name': 'bd_openers', 'type': 'atomic_t'}, {'name': 'bd_size_lock', 'type': 'spinlock_t'}, {'name': 'bd_claiming', 'type': '*mut core::ffi::c_void'}, {'name': 'bd_holder', 'type': '*mut core::ffi::c_void'}, {'name': 'bd_holder_ops', 'type': '*const blk_holder_ops'}, {'name': 'bd_holder_lock', 'type': 'mutex'}, {'name': 'bd_holders', 'type': 'core::ffi::c_int'}, {'name': 'bd_holder_dir', 'type': '*mut kobject'}, {'name': 'bd_fsfreeze_count', 'type': 'atomic_t'}, {'name': 'bd_fsfreeze_mutex', 'type': 'mutex'}, {'name': 'bd_meta_info', 'type': '*mut partition_meta_info'}, {'name': 'bd_writers', 'type': 'core::ffi::c_int'}, {'name': 'bd_security', 'type': '*mut core::ffi::c_void'}, {'name': 'bd_device', 'type': 'device'}]`

### Rust Evidence

- Graph edges: `3`

## W-000136 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: k_itimer
- Explanation: k_itimer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'list', 'type': 'list_head'}, {'name': 't_hash', 'type': 'hlist_node'}, {'name': 'it_lock', 'type': 'spinlock_t'}, {'name': 'kclock', 'type': '*mut k_clock'}, {'name': 'it_clock', 'type': 'clockid_t'}, {'name': 'it_id', 'type': 'timer_t'}, {'name': 'it_active', 'type': 'core::ffi::c_int'}, {'name': 'it_overrun', 'type': 's64'}, {'name': 'it_overrun_last', 'type': 's64'}, {'name': 'it_requeue_pending', 'type': 'core::ffi::c_int'}, {'name': 'it_sigev_notify', 'type': 'core::ffi::c_int'}, {'name': 'it_interval', 'type': 'ktime_t'}, {'name': 'it_signal', 'type': '*mut signal_struct'}, {'name': '__bindgen_anon_1', 'type': 'k_itimer__bindgen_ty_1'}, {'name': 'sigq', 'type': '*mut sigqueue'}, {'name': 'it', 'type': 'k_itimer__bindgen_ty_2'}, {'name': 'rcu', 'type': 'callback_head'}]`
- New: `[{'name': 'list', 'type': 'hlist_node'}, {'name': 't_hash', 'type': 'hlist_node'}, {'name': 'it_lock', 'type': 'spinlock_t'}, {'name': 'kclock', 'type': '*mut k_clock'}, {'name': 'it_clock', 'type': 'clockid_t'}, {'name': 'it_id', 'type': 'timer_t'}, {'name': 'it_active', 'type': 'core::ffi::c_int'}, {'name': 'it_overrun', 'type': 's64'}, {'name': 'it_overrun_last', 'type': 's64'}, {'name': 'it_requeue_pending', 'type': 'core::ffi::c_int'}, {'name': 'it_sigev_notify', 'type': 'core::ffi::c_int'}, {'name': 'it_interval', 'type': 'ktime_t'}, {'name': 'it_signal', 'type': '*mut signal_struct'}, {'name': '__bindgen_anon_1', 'type': 'k_itimer__bindgen_ty_1'}, {'name': 'sigq', 'type': '*mut sigqueue'}, {'name': 'it', 'type': 'k_itimer__bindgen_ty_2'}, {'name': 'rcu', 'type': 'callback_head'}]`

### Rust Evidence

- Graph edges: `3`

## W-000151 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: tc_u32_sel
- Explanation: tc_u32_sel changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'flags', 'type': 'core::ffi::c_uchar'}, {'name': 'offshift', 'type': 'core::ffi::c_uchar'}, {'name': 'nkeys', 'type': 'core::ffi::c_uchar'}, {'name': 'offmask', 'type': '__be16'}, {'name': 'off', 'type': '__u16'}, {'name': 'offoff', 'type': 'core::ffi::c_short'}, {'name': 'hoff', 'type': 'core::ffi::c_short'}, {'name': 'hmask', 'type': '__be32'}, {'name': 'keys', 'type': '__IncompleteArrayField<tc_u32_key>'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'tc_u32_sel__bindgen_ty_1'}, {'name': 'keys', 'type': '__IncompleteArrayField<tc_u32_key>'}]`

### Rust Evidence

- Graph edges: `3`

## W-000125 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: bpf_insn_access_aux
- Explanation: bpf_insn_access_aux changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'reg_type', 'type': 'bpf_reg_type'}, {'name': '__bindgen_anon_1', 'type': 'bpf_insn_access_aux__bindgen_ty_1'}, {'name': 'log', 'type': '*mut bpf_verifier_log'}]`
- New: `[{'name': 'reg_type', 'type': 'bpf_reg_type'}, {'name': 'is_ldsx', 'type': 'bool_'}, {'name': '__bindgen_anon_1', 'type': 'bpf_insn_access_aux__bindgen_ty_1'}, {'name': 'log', 'type': '*mut bpf_verifier_log'}, {'name': 'is_retval', 'type': 'bool_'}]`

### Rust Evidence

- Graph edges: `2`

## W-000142 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: reclaim_stat
- Explanation: reclaim_stat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'nr_dirty', 'type': 'core::ffi::c_uint'}, {'name': 'nr_unqueued_dirty', 'type': 'core::ffi::c_uint'}, {'name': 'nr_congested', 'type': 'core::ffi::c_uint'}, {'name': 'nr_writeback', 'type': 'core::ffi::c_uint'}, {'name': 'nr_immediate', 'type': 'core::ffi::c_uint'}, {'name': 'nr_pageout', 'type': 'core::ffi::c_uint'}, {'name': 'nr_activate', 'type': '[core::ffi::c_uint; 2usize]'}, {'name': 'nr_ref_keep', 'type': 'core::ffi::c_uint'}, {'name': 'nr_unmap_fail', 'type': 'core::ffi::c_uint'}, {'name': 'nr_lazyfree_fail', 'type': 'core::ffi::c_uint'}]`
- New: `[{'name': 'nr_dirty', 'type': 'core::ffi::c_uint'}, {'name': 'nr_unqueued_dirty', 'type': 'core::ffi::c_uint'}, {'name': 'nr_congested', 'type': 'core::ffi::c_uint'}, {'name': 'nr_writeback', 'type': 'core::ffi::c_uint'}, {'name': 'nr_immediate', 'type': 'core::ffi::c_uint'}, {'name': 'nr_pageout', 'type': 'core::ffi::c_uint'}, {'name': 'nr_activate', 'type': '[core::ffi::c_uint; 2usize]'}, {'name': 'nr_ref_keep', 'type': 'core::ffi::c_uint'}, {'name': 'nr_unmap_fail', 'type': 'core::ffi::c_uint'}, {'name': 'nr_lazyfree_fail', 'type': 'core::ffi::c_uint'}, {'name': 'nr_demoted', 'type': 'core::ffi::c_uint'}]`

### Rust Evidence

- Graph edges: `2`

## W-000164 MacroConstDrift

- Risk: Medium
- Score: 9.0
- Symbol: I_DIRTY
- Explanation: I_DIRTY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `7`
- New: `56`

### Rust Evidence

- Graph edges: `7`

## W-000126 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bpf_map__bindgen_ty_2
- Explanation: bpf_map__bindgen_ty_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'lock', 'type': 'spinlock_t'}, {'name': 'type_', 'type': 'bpf_prog_type'}, {'name': 'jited', 'type': 'bool_'}, {'name': 'xdp_has_frags', 'type': 'bool_'}]`
- New: `[{'name': 'attach_func_proto', 'type': '*const btf_type'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'type_', 'type': 'bpf_prog_type'}, {'name': 'jited', 'type': 'bool_'}, {'name': 'xdp_has_frags', 'type': 'bool_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000127 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bpf_verifier_ops
- Explanation: bpf_verifier_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'get_func_proto', 'type': '::core::option::Option<'}, {'name': 'is_valid_access', 'type': '::core::option::Option<'}, {'name': 'gen_prologue', 'type': '::core::option::Option<'}, {'name': 'gen_ld_abs', 'type': '::core::option::Option<'}, {'name': 'convert_ctx_access', 'type': '::core::option::Option<'}, {'name': 'btf_struct_access', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'get_func_proto', 'type': '::core::option::Option<'}, {'name': 'is_valid_access', 'type': '::core::option::Option<'}, {'name': 'gen_prologue', 'type': '::core::option::Option<'}, {'name': 'gen_epilogue', 'type': '::core::option::Option<'}, {'name': 'gen_ld_abs', 'type': '::core::option::Option<'}, {'name': 'convert_ctx_access', 'type': '::core::option::Option<'}, {'name': 'btf_struct_access', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-000129 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: cgroup_subsys_state
- Explanation: cgroup_subsys_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'cgroup', 'type': '*mut cgroup'}, {'name': 'ss', 'type': '*mut cgroup_subsys'}, {'name': 'refcnt', 'type': 'percpu_ref'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'children', 'type': 'list_head'}, {'name': 'rstat_css_node', 'type': 'list_head'}, {'name': 'id', 'type': 'core::ffi::c_int'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'serial_nr', 'type': 'u64_'}, {'name': 'online_cnt', 'type': 'atomic_t'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 'destroy_rwork', 'type': 'rcu_work'}, {'name': 'parent', 'type': '*mut cgroup_subsys_state'}]`
- New: `[{'name': 'cgroup', 'type': '*mut cgroup'}, {'name': 'ss', 'type': '*mut cgroup_subsys'}, {'name': 'refcnt', 'type': 'percpu_ref'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'children', 'type': 'list_head'}, {'name': 'rstat_css_node', 'type': 'list_head'}, {'name': 'id', 'type': 'core::ffi::c_int'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'serial_nr', 'type': 'u64_'}, {'name': 'online_cnt', 'type': 'atomic_t'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 'destroy_rwork', 'type': 'rcu_work'}, {'name': 'parent', 'type': '*mut cgroup_subsys_state'}, {'name': 'nr_descendants', 'type': 'core::ffi::c_int'}]`

### Rust Evidence

- Graph edges: `1`

## W-000130 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: context_tracking
- Explanation: context_tracking changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'state', 'type': 'atomic_t'}, {'name': 'dynticks_nesting', 'type': 'core::ffi::c_long'}, {'name': 'dynticks_nmi_nesting', 'type': 'core::ffi::c_long'}]`
- New: `[{'name': 'state', 'type': 'atomic_t'}, {'name': 'nesting', 'type': 'core::ffi::c_long'}, {'name': 'nmi_nesting', 'type': 'core::ffi::c_long'}]`

### Rust Evidence

- Graph edges: `1`

## W-000134 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: fown_struct
- Explanation: fown_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'lock', 'type': 'rwlock_t'}, {'name': 'pid', 'type': '*mut pid'}, {'name': 'pid_type', 'type': 'pid_type'}, {'name': 'uid', 'type': 'kuid_t'}, {'name': 'euid', 'type': 'kuid_t'}, {'name': 'signum', 'type': 'core::ffi::c_int'}]`
- New: `[{'name': 'file', 'type': '*mut file'}, {'name': 'lock', 'type': 'rwlock_t'}, {'name': 'pid', 'type': '*mut pid'}, {'name': 'pid_type', 'type': 'pid_type'}, {'name': 'uid', 'type': 'kuid_t'}, {'name': 'euid', 'type': 'kuid_t'}, {'name': 'signum', 'type': 'core::ffi::c_int'}]`

### Rust Evidence

- Graph edges: `1`

## W-000137 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: ma_state
- Explanation: ma_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'tree', 'type': '*mut maple_tree'}, {'name': 'index', 'type': 'core::ffi::c_ulong'}, {'name': 'last', 'type': 'core::ffi::c_ulong'}, {'name': 'node', 'type': '*mut maple_enode'}, {'name': 'min', 'type': 'core::ffi::c_ulong'}, {'name': 'max', 'type': 'core::ffi::c_ulong'}, {'name': 'alloc', 'type': '*mut maple_alloc'}, {'name': 'status', 'type': 'maple_status'}, {'name': 'depth', 'type': 'core::ffi::c_uchar'}, {'name': 'offset', 'type': 'core::ffi::c_uchar'}, {'name': 'mas_flags', 'type': 'core::ffi::c_uchar'}, {'name': 'end', 'type': 'core::ffi::c_uchar'}]`
- New: `[{'name': 'tree', 'type': '*mut maple_tree'}, {'name': 'index', 'type': 'core::ffi::c_ulong'}, {'name': 'last', 'type': 'core::ffi::c_ulong'}, {'name': 'node', 'type': '*mut maple_enode'}, {'name': 'min', 'type': 'core::ffi::c_ulong'}, {'name': 'max', 'type': 'core::ffi::c_ulong'}, {'name': 'alloc', 'type': '*mut maple_alloc'}, {'name': 'status', 'type': 'maple_status'}, {'name': 'depth', 'type': 'core::ffi::c_uchar'}, {'name': 'offset', 'type': 'core::ffi::c_uchar'}, {'name': 'mas_flags', 'type': 'core::ffi::c_uchar'}, {'name': 'end', 'type': 'core::ffi::c_uchar'}, {'name': 'store_type', 'type': 'store_type'}]`

### Rust Evidence

- Graph edges: `1`

## W-000138 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: mem_cgroup_reclaim_cookie
- Explanation: mem_cgroup_reclaim_cookie changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'pgdat', 'type': '*mut pg_data_t'}, {'name': 'generation', 'type': 'core::ffi::c_uint'}]`
- New: `[{'name': 'pgdat', 'type': '*mut pg_data_t'}, {'name': 'generation', 'type': 'core::ffi::c_int'}]`

### Rust Evidence

- Graph edges: `1`

## W-000141 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: ratelimit_state
- Explanation: ratelimit_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'lock', 'type': 'raw_spinlock_t'}, {'name': 'interval', 'type': 'core::ffi::c_int'}, {'name': 'burst', 'type': 'core::ffi::c_int'}, {'name': 'printed', 'type': 'core::ffi::c_int'}, {'name': 'missed', 'type': 'core::ffi::c_int'}, {'name': 'begin', 'type': 'core::ffi::c_ulong'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}]`
- New: `[{'name': 'lock', 'type': 'raw_spinlock_t'}, {'name': 'interval', 'type': 'core::ffi::c_int'}, {'name': 'burst', 'type': 'core::ffi::c_int'}, {'name': 'printed', 'type': 'core::ffi::c_int'}, {'name': 'missed', 'type': 'core::ffi::c_int'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'begin', 'type': 'core::ffi::c_ulong'}]`

### Rust Evidence

- Graph edges: `1`

## W-000144 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: sbitmap_word
- Explanation: sbitmap_word changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'word', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': 'cleared', 'type': 'core::ffi::c_ulong'}, {'name': 'swap_lock', 'type': 'spinlock_t'}]`
- New: `[{'name': 'word', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': 'cleared', 'type': 'core::ffi::c_ulong'}, {'name': 'swap_lock', 'type': 'raw_spinlock_t'}]`

### Rust Evidence

- Graph edges: `1`

## W-000145 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: sched_dl_entity
- Explanation: sched_dl_entity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'rb_node', 'type': 'rb_node'}, {'name': 'dl_runtime', 'type': 'u64_'}, {'name': 'dl_deadline', 'type': 'u64_'}, {'name': 'dl_period', 'type': 'u64_'}, {'name': 'dl_bw', 'type': 'u64_'}, {'name': 'dl_density', 'type': 'u64_'}, {'name': 'runtime', 'type': 's64'}, {'name': 'deadline', 'type': 'u64_'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'dl_timer', 'type': 'hrtimer'}, {'name': 'inactive_timer', 'type': 'hrtimer'}, {'name': 'rq', 'type': '*mut rq'}, {'name': 'server_has_tasks', 'type': 'dl_server_has_tasks_f'}, {'name': 'server_pick', 'type': 'dl_server_pick_f'}, {'name': 'pi_se', 'type': '*mut sched_dl_entity'}]`
- New: `[{'name': 'rb_node', 'type': 'rb_node'}, {'name': 'dl_runtime', 'type': 'u64_'}, {'name': 'dl_deadline', 'type': 'u64_'}, {'name': 'dl_period', 'type': 'u64_'}, {'name': 'dl_bw', 'type': 'u64_'}, {'name': 'dl_density', 'type': 'u64_'}, {'name': 'runtime', 'type': 's64'}, {'name': 'deadline', 'type': 'u64_'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'dl_timer', 'type': 'hrtimer'}, {'name': 'inactive_timer', 'type': 'hrtimer'}, {'name': 'rq', 'type': '*mut rq'}, {'name': 'server_has_tasks', 'type': 'dl_server_has_tasks_f'}, {'name': 'server_pick_task', 'type': 'dl_server_pick_f'}, {'name': 'pi_se', 'type': '*mut sched_dl_entity'}]`

### Rust Evidence

- Graph edges: `1`

## W-000146 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: sched_entity
- Explanation: sched_entity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'load', 'type': 'load_weight'}, {'name': 'run_node', 'type': 'rb_node'}, {'name': 'deadline', 'type': 'u64_'}, {'name': 'min_vruntime', 'type': 'u64_'}, {'name': 'group_node', 'type': 'list_head'}, {'name': 'on_rq', 'type': 'core::ffi::c_uint'}, {'name': 'exec_start', 'type': 'u64_'}, {'name': 'sum_exec_runtime', 'type': 'u64_'}, {'name': 'prev_sum_exec_runtime', 'type': 'u64_'}, {'name': 'vruntime', 'type': 'u64_'}, {'name': 'vlag', 'type': 's64'}, {'name': 'slice', 'type': 'u64_'}, {'name': 'nr_migrations', 'type': 'u64_'}, {'name': 'depth', 'type': 'core::ffi::c_int'}, {'name': 'parent', 'type': '*mut sched_entity'}, {'name': 'cfs_rq', 'type': '*mut cfs_rq'}, {'name': 'my_q', 'type': '*mut cfs_rq'}, {'name': 'runnable_weight', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': '[u64; 2usize]'}, {'name': 'avg', 'type': 'sched_avg'}]`
- New: `[{'name': 'load', 'type': 'load_weight'}, {'name': 'run_node', 'type': 'rb_node'}, {'name': 'deadline', 'type': 'u64_'}, {'name': 'min_vruntime', 'type': 'u64_'}, {'name': 'min_slice', 'type': 'u64_'}, {'name': 'group_node', 'type': 'list_head'}, {'name': 'on_rq', 'type': 'core::ffi::c_uchar'}, {'name': 'sched_delayed', 'type': 'core::ffi::c_uchar'}, {'name': 'rel_deadline', 'type': 'core::ffi::c_uchar'}, {'name': 'custom_slice', 'type': 'core::ffi::c_uchar'}, {'name': 'exec_start', 'type': 'u64_'}, {'name': 'sum_exec_runtime', 'type': 'u64_'}, {'name': 'prev_sum_exec_runtime', 'type': 'u64_'}, {'name': 'vruntime', 'type': 'u64_'}, {'name': 'vlag', 'type': 's64'}, {'name': 'slice', 'type': 'u64_'}, {'name': 'nr_migrations', 'type': 'u64_'}, {'name': 'depth', 'type': 'core::ffi::c_int'}, {'name': 'parent', 'type': '*mut sched_entity'}, {'name': 'cfs_rq', 'type': '*mut cfs_rq'}, {'name': 'my_q', 'type': '*mut cfs_rq'}, {'name': 'runnable_weight', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': 'u64'}, {'name': 'avg', 'type': 'sched_avg'}]`

### Rust Evidence

- Graph edges: `1`

## W-000147 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: signal_struct
- Explanation: signal_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'sigcnt', 'type': 'refcount_t'}, {'name': 'live', 'type': 'atomic_t'}, {'name': 'nr_threads', 'type': 'core::ffi::c_int'}, {'name': 'quick_threads', 'type': 'core::ffi::c_int'}, {'name': 'thread_head', 'type': 'list_head'}, {'name': 'wait_chldexit', 'type': 'wait_queue_head_t'}, {'name': 'curr_target', 'type': '*mut task_struct'}, {'name': 'shared_pending', 'type': 'sigpending'}, {'name': 'multiprocess', 'type': 'hlist_head'}, {'name': 'group_exit_code', 'type': 'core::ffi::c_int'}, {'name': 'notify_count', 'type': 'core::ffi::c_int'}, {'name': 'group_exec_task', 'type': '*mut task_struct'}, {'name': 'group_stop_count', 'type': 'core::ffi::c_int'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'core_state', 'type': '*mut core_state'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'next_posix_timer_id', 'type': 'core::ffi::c_uint'}, {'name': 'posix_timers', 'type': 'list_head'}, {'name': 'real_timer', 'type': 'hrtimer'}, {'name': 'it_real_incr', 'type': 'ktime_t'}, {'name': 'it', 'type': '[cpu_itimer; 2usize]'}, {'name': 'cputimer', 'type': 'thread_group_cputimer'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'pids', 'type': '[*mut pid; 4usize]'}, {'name': 'tty_old_pgrp', 'type': '*mut pid'}, {'name': 'leader', 'type': 'core::ffi::c_int'}, {'name': 'tty', 'type': '*mut tty_struct'}, {'name': 'stats_lock', 'type': 'seqlock_t'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'cutime', 'type': 'u64_'}, {'name': 'cstime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'cgtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'cnvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'cnivcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'min_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'cmin_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'cmaj_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'inblock', 'type': 'core::ffi::c_ulong'}, {'name': 'oublock', 'type': 'core::ffi::c_ulong'}, {'name': 'cinblock', 'type': 'core::ffi::c_ulong'}, {'name': 'coublock', 'type': 'core::ffi::c_ulong'}, {'name': 'maxrss', 'type': 'core::ffi::c_ulong'}, {'name': 'cmaxrss', 'type': 'core::ffi::c_ulong'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'sum_sched_runtime', 'type': 'core::ffi::c_ulonglong'}, {'name': 'rlim', 'type': '[rlimit; 16usize]'}, {'name': 'pacct', 'type': 'pacct_struct'}, {'name': 'stats', 'type': '*mut taskstats'}, {'name': 'audit_tty', 'type': 'core::ffi::c_uint'}, {'name': 'tty_audit_buf', 'type': '*mut tty_audit_buf'}, {'name': 'oom_flag_origin', 'type': 'bool_'}, {'name': 'oom_score_adj', 'type': 'core::ffi::c_short'}, {'name': 'oom_score_adj_min', 'type': 'core::ffi::c_short'}, {'name': 'oom_mm', 'type': '*mut mm_struct'}, {'name': 'cred_guard_mutex', 'type': 'mutex'}, {'name': 'exec_update_lock', 'type': 'rw_semaphore'}]`
- New: `[{'name': 'sigcnt', 'type': 'refcount_t'}, {'name': 'live', 'type': 'atomic_t'}, {'name': 'nr_threads', 'type': 'core::ffi::c_int'}, {'name': 'quick_threads', 'type': 'core::ffi::c_int'}, {'name': 'thread_head', 'type': 'list_head'}, {'name': 'wait_chldexit', 'type': 'wait_queue_head_t'}, {'name': 'curr_target', 'type': '*mut task_struct'}, {'name': 'shared_pending', 'type': 'sigpending'}, {'name': 'multiprocess', 'type': 'hlist_head'}, {'name': 'group_exit_code', 'type': 'core::ffi::c_int'}, {'name': 'notify_count', 'type': 'core::ffi::c_int'}, {'name': 'group_exec_task', 'type': '*mut task_struct'}, {'name': 'group_stop_count', 'type': 'core::ffi::c_int'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'core_state', 'type': '*mut core_state'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'next_posix_timer_id', 'type': 'core::ffi::c_uint'}, {'name': 'posix_timers', 'type': 'hlist_head'}, {'name': 'real_timer', 'type': 'hrtimer'}, {'name': 'it_real_incr', 'type': 'ktime_t'}, {'name': 'it', 'type': '[cpu_itimer; 2usize]'}, {'name': 'cputimer', 'type': 'thread_group_cputimer'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'pids', 'type': '[*mut pid; 4usize]'}, {'name': 'tty_old_pgrp', 'type': '*mut pid'}, {'name': 'leader', 'type': 'core::ffi::c_int'}, {'name': 'tty', 'type': '*mut tty_struct'}, {'name': 'stats_lock', 'type': 'seqlock_t'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'cutime', 'type': 'u64_'}, {'name': 'cstime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'cgtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'cnvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'cnivcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'min_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'cmin_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'cmaj_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'inblock', 'type': 'core::ffi::c_ulong'}, {'name': 'oublock', 'type': 'core::ffi::c_ulong'}, {'name': 'cinblock', 'type': 'core::ffi::c_ulong'}, {'name': 'coublock', 'type': 'core::ffi::c_ulong'}, {'name': 'maxrss', 'type': 'core::ffi::c_ulong'}, {'name': 'cmaxrss', 'type': 'core::ffi::c_ulong'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'sum_sched_runtime', 'type': 'core::ffi::c_ulonglong'}, {'name': 'rlim', 'type': '[rlimit; 16usize]'}, {'name': 'pacct', 'type': 'pacct_struct'}, {'name': 'stats', 'type': '*mut taskstats'}, {'name': 'audit_tty', 'type': 'core::ffi::c_uint'}, {'name': 'tty_audit_buf', 'type': '*mut tty_audit_buf'}, {'name': 'oom_flag_origin', 'type': 'bool_'}, {'name': 'oom_score_adj', 'type': 'core::ffi::c_short'}, {'name': 'oom_score_adj_min', 'type': 'core::ffi::c_short'}, {'name': 'oom_mm', 'type': '*mut mm_struct'}, {'name': 'cred_guard_mutex', 'type': 'mutex'}, {'name': 'exec_update_lock', 'type': 'rw_semaphore'}]`

### Rust Evidence

- Graph edges: `1`

## W-000148 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: softirq_action
- Explanation: softirq_action changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'action', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut softirq_action)>'}]`
- New: `[{'name': 'action', 'type': '::core::option::Option<unsafe extern "C" fn()>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000149 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: super_block
- Explanation: super_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 's_list', 'type': 'list_head'}, {'name': 's_dev', 'type': 'dev_t'}, {'name': 's_blocksize_bits', 'type': 'core::ffi::c_uchar'}, {'name': 's_blocksize', 'type': 'core::ffi::c_ulong'}, {'name': 's_maxbytes', 'type': 'loff_t'}, {'name': 's_type', 'type': '*mut file_system_type'}, {'name': 's_op', 'type': '*const super_operations'}, {'name': 'dq_op', 'type': '*const dquot_operations'}, {'name': 's_qcop', 'type': '*const quotactl_ops'}, {'name': 's_export_op', 'type': '*const export_operations'}, {'name': 's_flags', 'type': 'core::ffi::c_ulong'}, {'name': 's_iflags', 'type': 'core::ffi::c_ulong'}, {'name': 's_magic', 'type': 'core::ffi::c_ulong'}, {'name': 's_root', 'type': '*mut dentry'}, {'name': 's_umount', 'type': 'rw_semaphore'}, {'name': 's_count', 'type': 'core::ffi::c_int'}, {'name': 's_active', 'type': 'atomic_t'}, {'name': 's_security', 'type': '*mut core::ffi::c_void'}, {'name': 's_xattr', 'type': '*const *mut xattr_handler'}, {'name': 's_roots', 'type': 'hlist_bl_head'}, {'name': 's_mounts', 'type': 'list_head'}, {'name': 's_bdev', 'type': '*mut block_device'}, {'name': 's_bdev_file', 'type': '*mut file'}, {'name': 's_bdi', 'type': '*mut backing_dev_info'}, {'name': 's_mtd', 'type': '*mut mtd_info'}, {'name': 's_instances', 'type': 'hlist_node'}, {'name': 's_quota_types', 'type': 'core::ffi::c_uint'}, {'name': 's_dquot', 'type': 'quota_info'}, {'name': 's_writers', 'type': 'sb_writers'}, {'name': 's_fs_info', 'type': '*mut core::ffi::c_void'}, {'name': 's_time_gran', 'type': 'u32_'}, {'name': 's_time_min', 'type': 'time64_t'}, {'name': 's_time_max', 'type': 'time64_t'}, {'name': 's_fsnotify_mask', 'type': '__u32'}, {'name': 's_fsnotify_info', 'type': '*mut fsnotify_sb_info'}, {'name': 's_id', 'type': '[core::ffi::c_char; 32usize]'}, {'name': 's_uuid', 'type': 'uuid_t'}, {'name': 's_uuid_len', 'type': 'u8_'}, {'name': 's_sysfs_name', 'type': '[core::ffi::c_char; 37usize]'}, {'name': 's_max_links', 'type': 'core::ffi::c_uint'}, {'name': 's_vfs_rename_mutex', 'type': 'mutex'}, {'name': 's_subtype', 'type': '*const core::ffi::c_char'}, {'name': 's_d_op', 'type': '*const dentry_operations'}, {'name': 's_shrink', 'type': '*mut shrinker'}, {'name': 's_remove_count', 'type': 'atomic_long_t'}, {'name': 's_readonly_remount', 'type': 'core::ffi::c_int'}, {'name': 's_wb_err', 'type': 'errseq_t'}, {'name': 's_dio_done_wq', 'type': '*mut workqueue_struct'}, {'name': 's_pins', 'type': 'hlist_head'}, {'name': 's_user_ns', 'type': '*mut user_namespace'}, {'name': 's_dentry_lru', 'type': 'list_lru'}, {'name': 's_inode_lru', 'type': 'list_lru'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 's_sync_lock', 'type': 'mutex'}, {'name': 's_stack_depth', 'type': 'core::ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': 'u32'}, {'name': 's_inode_list_lock', 'type': 'spinlock_t'}, {'name': 's_inodes', 'type': 'list_head'}, {'name': 's_inode_wblist_lock', 'type': 'spinlock_t'}, {'name': 's_inodes_wb', 'type': 'list_head'}]`
- New: `[{'name': 's_list', 'type': 'list_head'}, {'name': 's_dev', 'type': 'dev_t'}, {'name': 's_blocksize_bits', 'type': 'core::ffi::c_uchar'}, {'name': 's_blocksize', 'type': 'core::ffi::c_ulong'}, {'name': 's_maxbytes', 'type': 'loff_t'}, {'name': 's_type', 'type': '*mut file_system_type'}, {'name': 's_op', 'type': '*const super_operations'}, {'name': 'dq_op', 'type': '*const dquot_operations'}, {'name': 's_qcop', 'type': '*const quotactl_ops'}, {'name': 's_export_op', 'type': '*const export_operations'}, {'name': 's_flags', 'type': 'core::ffi::c_ulong'}, {'name': 's_iflags', 'type': 'core::ffi::c_ulong'}, {'name': 's_magic', 'type': 'core::ffi::c_ulong'}, {'name': 's_root', 'type': '*mut dentry'}, {'name': 's_umount', 'type': 'rw_semaphore'}, {'name': 's_count', 'type': 'core::ffi::c_int'}, {'name': 's_active', 'type': 'atomic_t'}, {'name': 's_security', 'type': '*mut core::ffi::c_void'}, {'name': 's_xattr', 'type': '*const *mut xattr_handler'}, {'name': 's_roots', 'type': 'hlist_bl_head'}, {'name': 's_mounts', 'type': 'list_head'}, {'name': 's_bdev', 'type': '*mut block_device'}, {'name': 's_bdev_file', 'type': '*mut file'}, {'name': 's_bdi', 'type': '*mut backing_dev_info'}, {'name': 's_mtd', 'type': '*mut mtd_info'}, {'name': 's_instances', 'type': 'hlist_node'}, {'name': 's_quota_types', 'type': 'core::ffi::c_uint'}, {'name': 's_dquot', 'type': 'quota_info'}, {'name': 's_writers', 'type': 'sb_writers'}, {'name': 's_fs_info', 'type': '*mut core::ffi::c_void'}, {'name': 's_time_gran', 'type': 'u32_'}, {'name': 's_time_min', 'type': 'time64_t'}, {'name': 's_time_max', 'type': 'time64_t'}, {'name': 's_fsnotify_mask', 'type': 'u32_'}, {'name': 's_fsnotify_info', 'type': '*mut fsnotify_sb_info'}, {'name': 's_id', 'type': '[core::ffi::c_char; 32usize]'}, {'name': 's_uuid', 'type': 'uuid_t'}, {'name': 's_uuid_len', 'type': 'u8_'}, {'name': 's_sysfs_name', 'type': '[core::ffi::c_char; 37usize]'}, {'name': 's_max_links', 'type': 'core::ffi::c_uint'}, {'name': 's_vfs_rename_mutex', 'type': 'mutex'}, {'name': 's_subtype', 'type': '*const core::ffi::c_char'}, {'name': 's_d_op', 'type': '*const dentry_operations'}, {'name': 's_shrink', 'type': '*mut shrinker'}, {'name': 's_remove_count', 'type': 'atomic_long_t'}, {'name': 's_readonly_remount', 'type': 'core::ffi::c_int'}, {'name': 's_wb_err', 'type': 'errseq_t'}, {'name': 's_dio_done_wq', 'type': '*mut workqueue_struct'}, {'name': 's_pins', 'type': 'hlist_head'}, {'name': 's_user_ns', 'type': '*mut user_namespace'}, {'name': 's_dentry_lru', 'type': 'list_lru'}, {'name': 's_inode_lru', 'type': 'list_lru'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 's_sync_lock', 'type': 'mutex'}, {'name': 's_stack_depth', 'type': 'core::ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': 'u32'}, {'name': 's_inode_list_lock', 'type': 'spinlock_t'}, {'name': 's_inodes', 'type': 'list_head'}, {'name': 's_inode_wblist_lock', 'type': 'spinlock_t'}, {'name': 's_inodes_wb', 'type': 'list_head'}]`

### Rust Evidence

- Graph edges: `1`

## W-000153 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: uid_gid_map__bindgen_ty_1__bindgen_ty_1
- Explanation: uid_gid_map__bindgen_ty_1__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'forward', 'type': '*mut uid_gid_extent'}, {'name': 'reverse', 'type': '*mut uid_gid_extent'}]`
- New: `[{'name': 'extent', 'type': '[uid_gid_extent; 5usize]'}, {'name': 'nr_extents', 'type': 'u32_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000155 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: uprobe_consumer
- Explanation: uprobe_consumer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'handler', 'type': '::core::option::Option<'}, {'name': 'ret_handler', 'type': '::core::option::Option<'}, {'name': 'filter', 'type': '::core::option::Option<'}, {'name': 'next', 'type': '*mut uprobe_consumer'}]`
- New: `[{'name': 'handler', 'type': '::core::option::Option<'}, {'name': 'ret_handler', 'type': '::core::option::Option<'}, {'name': 'filter', 'type': '::core::option::Option<'}, {'name': 'cons_node', 'type': 'list_head'}]`

### Rust Evidence

- Graph edges: `1`

## W-000157 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vm_event_state
- Explanation: vm_event_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'event', 'type': '[core::ffi::c_ulong; 74usize]'}]`
- New: `[{'name': 'event', 'type': '[core::ffi::c_ulong; 82usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000158 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vm_special_mapping
- Explanation: vm_special_mapping changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'pages', 'type': '*mut *mut page'}, {'name': 'fault', 'type': '::core::option::Option<'}, {'name': 'mremap', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'pages', 'type': '*mut *mut page'}, {'name': 'fault', 'type': '::core::option::Option<'}, {'name': 'mremap', 'type': '::core::option::Option<'}, {'name': 'close', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-000159 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: writeback_control
- Explanation: writeback_control changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'nr_to_write', 'type': 'core::ffi::c_long'}, {'name': 'pages_skipped', 'type': 'core::ffi::c_long'}, {'name': 'range_start', 'type': 'loff_t'}, {'name': 'range_end', 'type': 'loff_t'}, {'name': 'sync_mode', 'type': 'writeback_sync_modes'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'swap_plug', 'type': '*mut *mut swap_iocb'}, {'name': 'fbatch', 'type': 'folio_batch'}, {'name': 'index', 'type': 'core::ffi::c_ulong'}, {'name': 'saved_err', 'type': 'core::ffi::c_int'}]`
- New: `[{'name': 'nr_to_write', 'type': 'core::ffi::c_long'}, {'name': 'pages_skipped', 'type': 'core::ffi::c_long'}, {'name': 'range_start', 'type': 'loff_t'}, {'name': 'range_end', 'type': 'loff_t'}, {'name': 'sync_mode', 'type': 'writeback_sync_modes'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'swap_plug', 'type': '*mut *mut swap_iocb'}, {'name': 'list', 'type': '*mut list_head'}, {'name': 'fbatch', 'type': 'folio_batch'}, {'name': 'index', 'type': 'core::ffi::c_ulong'}, {'name': 'saved_err', 'type': 'core::ffi::c_int'}]`

### Rust Evidence

- Graph edges: `1`

## W-000189 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: bpf_arg_type_ARG_PTR_TO_BTF_ID
- Explanation: bpf_arg_type_ARG_PTR_TO_BTF_ID changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `15`
- New: `13`

### Rust Evidence

- Graph edges: `3`

## W-000161 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: CONFIG_LSM
- Explanation: CONFIG_LSM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `b"landlock,lockdown,yama,loadpin,safesetid,selinux,smack,tomoyo,apparmor,bpf\0"`
- New: `b"landlock,lockdown,yama,loadpin,safesetid,selinux,smack,tomoyo,apparmor,ipe,bpf\0"`

### Rust Evidence

- Graph edges: `2`

## W-000177 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: I_SYNC
- Explanation: I_SYNC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `128`
- New: `2`

### Rust Evidence

- Graph edges: `2`

## W-000197 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: bpf_arg_type_ARG_PTR_TO_SOCKET
- Explanation: bpf_arg_type_ARG_PTR_TO_SOCKET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `14`
- New: `12`

### Rust Evidence

- Graph edges: `2`

## W-000199 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: bpf_arg_type_ARG_PTR_TO_STACK
- Explanation: bpf_arg_type_ARG_PTR_TO_STACK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `21`
- New: `19`

### Rust Evidence

- Graph edges: `2`

## W-000215 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: cpuhp_state_CPUHP_AP_ONLINE_DYN
- Explanation: cpuhp_state_CPUHP_AP_ONLINE_DYN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `194`
- New: `193`

### Rust Evidence

- Graph edges: `2`

## W-000282 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: vm_event_item_HTLB_BUDDY_PGALLOC
- Explanation: vm_event_item_HTLB_BUDDY_PGALLOC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `61`
- New: `62`

### Rust Evidence

- Graph edges: `2`

## W-000299 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: vm_event_item_SWAP_RA
- Explanation: vm_event_item_SWAP_RA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `70`
- New: `71`

### Rust Evidence

- Graph edges: `2`

## W-000162 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: I_CLEAR
- Explanation: I_CLEAR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `64`
- New: `256`

### Rust Evidence

- Graph edges: `1`

## W-000163 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: I_CREATING
- Explanation: I_CREATING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `32768`
- New: `16384`

### Rust Evidence

- Graph edges: `1`

## W-000165 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: I_DIRTY_ALL
- Explanation: I_DIRTY_ALL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `2055`
- New: `2104`

### Rust Evidence

- Graph edges: `1`

## W-000166 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: I_DIRTY_DATASYNC
- Explanation: I_DIRTY_DATASYNC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `2`
- New: `16`

### Rust Evidence

- Graph edges: `1`

## W-000167 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: I_DIRTY_INODE
- Explanation: I_DIRTY_INODE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `3`
- New: `24`

### Rust Evidence

- Graph edges: `1`

## W-000168 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: I_DIRTY_PAGES
- Explanation: I_DIRTY_PAGES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `4`
- New: `32`

### Rust Evidence

- Graph edges: `1`

## W-000169 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: I_DIRTY_SYNC
- Explanation: I_DIRTY_SYNC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `1`
- New: `8`

### Rust Evidence

- Graph edges: `1`

## W-000170 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: I_DONTCACHE
- Explanation: I_DONTCACHE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `65536`
- New: `32768`

### Rust Evidence

- Graph edges: `1`

## W-000171 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: I_FREEING
- Explanation: I_FREEING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `32`
- New: `128`

### Rust Evidence

- Graph edges: `1`

## W-000172 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: I_LRU_ISOLATING
- Explanation: I_LRU_ISOLATING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `524288`
- New: `4`

### Rust Evidence

- Graph edges: `1`

## W-000173 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: I_NEW
- Explanation: I_NEW changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `1`

### Rust Evidence

- Graph edges: `1`

## W-000174 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: I_OVL_INUSE
- Explanation: I_OVL_INUSE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16384`
- New: `8192`

### Rust Evidence

- Graph edges: `1`

## W-000175 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: I_PINNING_NETFS_WB
- Explanation: I_PINNING_NETFS_WB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `262144`
- New: `131072`

### Rust Evidence

- Graph edges: `1`

## W-000176 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: I_REFERENCED
- Explanation: I_REFERENCED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `256`
- New: `512`

### Rust Evidence

- Graph edges: `1`

## W-000178 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: I_SYNC_QUEUED
- Explanation: I_SYNC_QUEUED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `131072`
- New: `65536`

### Rust Evidence

- Graph edges: `1`

## W-000179 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: I_WB_SWITCH
- Explanation: I_WB_SWITCH changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8192`
- New: `4096`

### Rust Evidence

- Graph edges: `1`

## W-000180 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: I_WILL_FREE
- Explanation: I_WILL_FREE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `64`

### Rust Evidence

- Graph edges: `1`

## W-000181 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: NR_PAGEFLAGS
- Explanation: NR_PAGEFLAGS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `22`
- New: `21`

### Rust Evidence

- Graph edges: `1`

## W-000182 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: PAGEFLAGS_MASK
- Explanation: PAGEFLAGS_MASK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `4194303`
- New: `2097151`

### Rust Evidence

- Graph edges: `1`

## W-000183 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: SOF_TIMESTAMPING_LAST
- Explanation: SOF_TIMESTAMPING_LAST changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `65536`
- New: `131072`

### Rust Evidence

- Graph edges: `1`

## W-000184 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: SOF_TIMESTAMPING_MASK
- Explanation: SOF_TIMESTAMPING_MASK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `131071`
- New: `262143`

### Rust Evidence

- Graph edges: `1`

## W-000185 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __I_LRU_ISOLATING
- Explanation: __I_LRU_ISOLATING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `19`
- New: `2`

### Rust Evidence

- Graph edges: `1`

## W-000186 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __I_NEW
- Explanation: __I_NEW changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `3`
- New: `0`

### Rust Evidence

- Graph edges: `1`

## W-000187 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __I_SYNC
- Explanation: __I_SYNC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `7`
- New: `1`

### Rust Evidence

- Graph edges: `1`

## W-000188 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_arg_type_ARG_CONST_ALLOC_SIZE_OR_ZERO
- Explanation: bpf_arg_type_ARG_CONST_ALLOC_SIZE_OR_ZERO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `17`
- New: `15`

### Rust Evidence

- Graph edges: `1`

## W-000190 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_arg_type_ARG_PTR_TO_BTF_ID_OR_NULL
- Explanation: bpf_arg_type_ARG_PTR_TO_BTF_ID_OR_NULL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `271`
- New: `269`

### Rust Evidence

- Graph edges: `1`

## W-000191 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_arg_type_ARG_PTR_TO_BTF_ID_SOCK_COMMON
- Explanation: bpf_arg_type_ARG_PTR_TO_BTF_ID_SOCK_COMMON changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `18`
- New: `16`

### Rust Evidence

- Graph edges: `1`

## W-000192 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_arg_type_ARG_PTR_TO_CONST_STR
- Explanation: bpf_arg_type_ARG_PTR_TO_CONST_STR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `22`
- New: `20`

### Rust Evidence

- Graph edges: `1`

## W-000193 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_arg_type_ARG_PTR_TO_DYNPTR
- Explanation: bpf_arg_type_ARG_PTR_TO_DYNPTR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `25`
- New: `23`

### Rust Evidence

- Graph edges: `1`

## W-000194 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_arg_type_ARG_PTR_TO_FUNC
- Explanation: bpf_arg_type_ARG_PTR_TO_FUNC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `20`
- New: `18`

### Rust Evidence

- Graph edges: `1`

## W-000195 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_arg_type_ARG_PTR_TO_PERCPU_BTF_ID
- Explanation: bpf_arg_type_ARG_PTR_TO_PERCPU_BTF_ID changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `19`
- New: `17`

### Rust Evidence

- Graph edges: `1`

## W-000196 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_arg_type_ARG_PTR_TO_RINGBUF_MEM
- Explanation: bpf_arg_type_ARG_PTR_TO_RINGBUF_MEM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `14`

### Rust Evidence

- Graph edges: `1`

## W-000198 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_arg_type_ARG_PTR_TO_SOCKET_OR_NULL
- Explanation: bpf_arg_type_ARG_PTR_TO_SOCKET_OR_NULL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `270`
- New: `268`

### Rust Evidence

- Graph edges: `1`

## W-000200 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_arg_type_ARG_PTR_TO_STACK_OR_NULL
- Explanation: bpf_arg_type_ARG_PTR_TO_STACK_OR_NULL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `277`
- New: `275`

### Rust Evidence

- Graph edges: `1`

## W-000201 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_arg_type_ARG_PTR_TO_TIMER
- Explanation: bpf_arg_type_ARG_PTR_TO_TIMER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `23`
- New: `21`

### Rust Evidence

- Graph edges: `1`

## W-000202 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_arg_type_ARG_PTR_TO_UNINIT_MEM
- Explanation: bpf_arg_type_ARG_PTR_TO_UNINIT_MEM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `32772`
- New: `67141636`

### Rust Evidence

- Graph edges: `1`

## W-000203 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_arg_type___BPF_ARG_TYPE_LIMIT
- Explanation: bpf_arg_type___BPF_ARG_TYPE_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `33554431`
- New: `134217727`

### Rust Evidence

- Graph edges: `1`

## W-000204 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_arg_type___BPF_ARG_TYPE_MAX
- Explanation: bpf_arg_type___BPF_ARG_TYPE_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `26`
- New: `24`

### Rust Evidence

- Graph edges: `1`

## W-000205 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_reg_type___BPF_REG_TYPE_LIMIT
- Explanation: bpf_reg_type___BPF_REG_TYPE_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `33554431`
- New: `134217727`

### Rust Evidence

- Graph edges: `1`

## W-000206 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_return_type___BPF_RET_TYPE_LIMIT
- Explanation: bpf_return_type___BPF_RET_TYPE_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `33554431`
- New: `134217727`

### Rust Evidence

- Graph edges: `1`

## W-000207 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_type_flag___BPF_TYPE_FLAG_MAX
- Explanation: bpf_type_flag___BPF_TYPE_FLAG_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16777217`
- New: `67108865`

### Rust Evidence

- Graph edges: `1`

## W-000208 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_type_flag___BPF_TYPE_LAST_FLAG
- Explanation: bpf_type_flag___BPF_TYPE_LAST_FLAG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16777216`
- New: `67108864`

### Rust Evidence

- Graph edges: `1`

## W-000209 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ACTIVE
- Explanation: cpuhp_state_CPUHP_AP_ACTIVE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `237`
- New: `236`

### Rust Evidence

- Graph edges: `1`

## W-000210 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_MVEBU_COHERENCY
- Explanation: cpuhp_state_CPUHP_AP_ARM_MVEBU_COHERENCY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `104`
- New: `105`

### Rust Evidence

- Graph edges: `1`

## W-000211 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_BASE_CACHEINFO_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_BASE_CACHEINFO_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `193`
- New: `192`

### Rust Evidence

- Graph edges: `1`

## W-000212 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_RISCV_IMSIC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_RISCV_IMSIC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `102`
- New: `103`

### Rust Evidence

- Graph edges: `1`

## W-000213 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_RISCV_SBI_IPI_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_RISCV_SBI_IPI_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `103`
- New: `104`

### Rust Evidence

- Graph edges: `1`

## W-000214 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_SIFIVE_PLIC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_SIFIVE_PLIC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `101`
- New: `102`

### Rust Evidence

- Graph edges: `1`

## W-000216 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ONLINE_DYN_END
- Explanation: cpuhp_state_CPUHP_AP_ONLINE_DYN_END changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `234`
- New: `233`

### Rust Evidence

- Graph edges: `1`

## W-000217 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_APM_XGENE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_APM_XGENE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `178`
- New: `177`

### Rust Evidence

- Graph edges: `1`

## W-000218 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_CAVIUM_TX2_UNCORE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_CAVIUM_TX2_UNCORE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `179`
- New: `178`

### Rust Evidence

- Graph edges: `1`

## W-000219 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_CCI_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_CCI_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `165`
- New: `164`

### Rust Evidence

- Graph edges: `1`

## W-000220 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_CCN_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_CCN_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `166`
- New: `165`

### Rust Evidence

- Graph edges: `1`

## W-000221 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_CPA_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_CPA_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `167`
- New: `166`

### Rust Evidence

- Graph edges: `1`

## W-000222 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_DDRC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_DDRC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `168`
- New: `167`

### Rust Evidence

- Graph edges: `1`

## W-000223 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_HHA_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_HHA_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `169`
- New: `168`

### Rust Evidence

- Graph edges: `1`

## W-000224 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_L3_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_L3_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `170`
- New: `169`

### Rust Evidence

- Graph edges: `1`

## W-000225 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PA_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PA_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `171`
- New: `170`

### Rust Evidence

- Graph edges: `1`

## W-000226 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PCIE_PMU_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PCIE_PMU_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `173`
- New: `172`

### Rust Evidence

- Graph edges: `1`

## W-000227 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_SLLC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_SLLC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `172`
- New: `171`

### Rust Evidence

- Graph edges: `1`

## W-000228 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HNS3_PMU_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HNS3_PMU_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `174`
- New: `173`

### Rust Evidence

- Graph edges: `1`

## W-000229 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_L2X0_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_L2X0_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `175`
- New: `174`

### Rust Evidence

- Graph edges: `1`

## W-000230 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_MARVELL_CN10K_DDR_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_MARVELL_CN10K_DDR_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `180`
- New: `179`

### Rust Evidence

- Graph edges: `1`

## W-000231 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L2_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L2_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `176`
- New: `175`

### Rust Evidence

- Graph edges: `1`

## W-000232 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L3_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L3_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `177`
- New: `176`

### Rust Evidence

- Graph edges: `1`

## W-000233 MacroConstDrift

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

## W-000234 MacroConstDrift

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

## W-000235 MacroConstDrift

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

## W-000236 MacroConstDrift

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

## W-000237 MacroConstDrift

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

## W-000238 MacroConstDrift

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

## W-000239 MacroConstDrift

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

## W-000240 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_S390_CF_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_S390_CF_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `163`
- New: `162`

### Rust Evidence

- Graph edges: `1`

## W-000241 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_S390_SF_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_S390_SF_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `164`
- New: `163`

### Rust Evidence

- Graph edges: `1`

## W-000242 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_IBS_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_IBS_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `107`
- New: `108`

### Rust Evidence

- Graph edges: `1`

## W-000243 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `105`
- New: `106`

### Rust Evidence

- Graph edges: `1`

## W-000244 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `106`
- New: `107`

### Rust Evidence

- Graph edges: `1`

## W-000245 MacroConstDrift

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

## W-000246 MacroConstDrift

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

## W-000247 MacroConstDrift

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

## W-000248 MacroConstDrift

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

## W-000249 MacroConstDrift

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

## W-000250 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_X86_HPET_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_X86_HPET_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `235`
- New: `234`

### Rust Evidence

- Graph edges: `1`

## W-000251 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_X86_KVM_CLK_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_X86_KVM_CLK_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `236`
- New: `235`

### Rust Evidence

- Graph edges: `1`

## W-000252 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_ONLINE
- Explanation: cpuhp_state_CPUHP_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `238`
- New: `237`

### Rust Evidence

- Graph edges: `1`

## W-000253 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: iter_type_ITER_DISCARD
- Explanation: iter_type_ITER_DISCARD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `6`

### Rust Evidence

- Graph edges: `1`

## W-000254 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: iter_type_ITER_XARRAY
- Explanation: iter_type_ITER_XARRAY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `4`
- New: `5`

### Rust Evidence

- Graph edges: `1`

## W-000255 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: led_trigger_netdev_modes___TRIGGER_NETDEV_MAX
- Explanation: led_trigger_netdev_modes___TRIGGER_NETDEV_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `11`
- New: `13`

### Rust Evidence

- Graph edges: `1`

## W-000256 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_anon_exclusive
- Explanation: pageflags_PG_anon_exclusive changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `11`

### Rust Evidence

- Graph edges: `1`

## W-000257 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_checked
- Explanation: pageflags_PG_checked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `11`
- New: `10`

### Rust Evidence

- Graph edges: `1`

## W-000258 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_foreign
- Explanation: pageflags_PG_foreign changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `11`
- New: `10`

### Rust Evidence

- Graph edges: `1`

## W-000259 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_has_hwpoisoned
- Explanation: pageflags_PG_has_hwpoisoned changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `8`

### Rust Evidence

- Graph edges: `1`

## W-000260 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_isolated
- Explanation: pageflags_PG_isolated changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `17`
- New: `16`

### Rust Evidence

- Graph edges: `1`

## W-000261 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_mappedtodisk
- Explanation: pageflags_PG_mappedtodisk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `11`

### Rust Evidence

- Graph edges: `1`

## W-000262 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_mlocked
- Explanation: pageflags_PG_mlocked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `20`
- New: `19`

### Rust Evidence

- Graph edges: `1`

## W-000263 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_owner_priv_1
- Explanation: pageflags_PG_owner_priv_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `11`
- New: `10`

### Rust Evidence

- Graph edges: `1`

## W-000264 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_pinned
- Explanation: pageflags_PG_pinned changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `11`
- New: `10`

### Rust Evidence

- Graph edges: `1`

## W-000265 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_readahead
- Explanation: pageflags_PG_readahead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `17`
- New: `16`

### Rust Evidence

- Graph edges: `1`

## W-000266 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_reclaim
- Explanation: pageflags_PG_reclaim changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `17`
- New: `16`

### Rust Evidence

- Graph edges: `1`

## W-000267 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_swapbacked
- Explanation: pageflags_PG_swapbacked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `18`
- New: `17`

### Rust Evidence

- Graph edges: `1`

## W-000268 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_swapcache
- Explanation: pageflags_PG_swapcache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `11`
- New: `10`

### Rust Evidence

- Graph edges: `1`

## W-000269 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_unevictable
- Explanation: pageflags_PG_unevictable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `19`
- New: `18`

### Rust Evidence

- Graph edges: `1`

## W-000270 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_xen_remapped
- Explanation: pageflags_PG_xen_remapped changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `11`
- New: `10`

### Rust Evidence

- Graph edges: `1`

## W-000271 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags___NR_PAGEFLAGS
- Explanation: pageflags___NR_PAGEFLAGS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `22`
- New: `21`

### Rust Evidence

- Graph edges: `1`

## W-000272 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_COMPACTFAIL
- Explanation: vm_event_item_COMPACTFAIL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `56`
- New: `57`

### Rust Evidence

- Graph edges: `1`

## W-000273 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_COMPACTFREE_SCANNED
- Explanation: vm_event_item_COMPACTFREE_SCANNED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `53`
- New: `54`

### Rust Evidence

- Graph edges: `1`

## W-000274 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_COMPACTISOLATED
- Explanation: vm_event_item_COMPACTISOLATED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `54`
- New: `55`

### Rust Evidence

- Graph edges: `1`

## W-000275 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_COMPACTMIGRATE_SCANNED
- Explanation: vm_event_item_COMPACTMIGRATE_SCANNED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `52`
- New: `53`

### Rust Evidence

- Graph edges: `1`

## W-000276 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_COMPACTSTALL
- Explanation: vm_event_item_COMPACTSTALL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `55`
- New: `56`

### Rust Evidence

- Graph edges: `1`

## W-000277 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_COMPACTSUCCESS
- Explanation: vm_event_item_COMPACTSUCCESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `57`
- New: `58`

### Rust Evidence

- Graph edges: `1`

## W-000278 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_DIRECT_MAP_LEVEL2_SPLIT
- Explanation: vm_event_item_DIRECT_MAP_LEVEL2_SPLIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `72`
- New: `75`

### Rust Evidence

- Graph edges: `1`

## W-000279 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_DIRECT_MAP_LEVEL3_SPLIT
- Explanation: vm_event_item_DIRECT_MAP_LEVEL3_SPLIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `73`
- New: `76`

### Rust Evidence

- Graph edges: `1`

## W-000280 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_DROP_PAGECACHE
- Explanation: vm_event_item_DROP_PAGECACHE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `44`
- New: `45`

### Rust Evidence

- Graph edges: `1`

## W-000281 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_DROP_SLAB
- Explanation: vm_event_item_DROP_SLAB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `45`
- New: `46`

### Rust Evidence

- Graph edges: `1`

## W-000283 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_HTLB_BUDDY_PGALLOC_FAIL
- Explanation: vm_event_item_HTLB_BUDDY_PGALLOC_FAIL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `62`
- New: `63`

### Rust Evidence

- Graph edges: `1`

## W-000284 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KCOMPACTD_FREE_SCANNED
- Explanation: vm_event_item_KCOMPACTD_FREE_SCANNED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `60`
- New: `61`

### Rust Evidence

- Graph edges: `1`

## W-000285 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KCOMPACTD_MIGRATE_SCANNED
- Explanation: vm_event_item_KCOMPACTD_MIGRATE_SCANNED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `59`
- New: `60`

### Rust Evidence

- Graph edges: `1`

## W-000286 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KCOMPACTD_WAKE
- Explanation: vm_event_item_KCOMPACTD_WAKE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `58`
- New: `59`

### Rust Evidence

- Graph edges: `1`

## W-000287 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KSWAPD_HIGH_WMARK_HIT_QUICKLY
- Explanation: vm_event_item_KSWAPD_HIGH_WMARK_HIT_QUICKLY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `41`
- New: `42`

### Rust Evidence

- Graph edges: `1`

## W-000288 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KSWAPD_INODESTEAL
- Explanation: vm_event_item_KSWAPD_INODESTEAL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `39`
- New: `40`

### Rust Evidence

- Graph edges: `1`

## W-000289 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_KSWAPD_LOW_WMARK_HIT_QUICKLY
- Explanation: vm_event_item_KSWAPD_LOW_WMARK_HIT_QUICKLY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `40`
- New: `41`

### Rust Evidence

- Graph edges: `1`

## W-000290 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_NR_VM_EVENT_ITEMS
- Explanation: vm_event_item_NR_VM_EVENT_ITEMS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `74`
- New: `82`

### Rust Evidence

- Graph edges: `1`

## W-000291 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_OOM_KILL
- Explanation: vm_event_item_OOM_KILL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `46`
- New: `47`

### Rust Evidence

- Graph edges: `1`

## W-000292 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PAGEOUTRUN
- Explanation: vm_event_item_PAGEOUTRUN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `42`
- New: `43`

### Rust Evidence

- Graph edges: `1`

## W-000293 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGINODESTEAL
- Explanation: vm_event_item_PGINODESTEAL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `37`
- New: `38`

### Rust Evidence

- Graph edges: `1`

## W-000294 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGMIGRATE_FAIL
- Explanation: vm_event_item_PGMIGRATE_FAIL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `49`

### Rust Evidence

- Graph edges: `1`

## W-000295 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGMIGRATE_SUCCESS
- Explanation: vm_event_item_PGMIGRATE_SUCCESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `47`
- New: `48`

### Rust Evidence

- Graph edges: `1`

## W-000296 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGROTATED
- Explanation: vm_event_item_PGROTATED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `43`
- New: `44`

### Rust Evidence

- Graph edges: `1`

## W-000297 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_PGSCAN_ZONE_RECLAIM_FAILED
- Explanation: vm_event_item_PGSCAN_ZONE_RECLAIM_FAILED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `36`
- New: `37`

### Rust Evidence

- Graph edges: `1`

## W-000298 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_SLABS_SCANNED
- Explanation: vm_event_item_SLABS_SCANNED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `38`
- New: `39`

### Rust Evidence

- Graph edges: `1`

## W-000300 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_SWAP_RA_HIT
- Explanation: vm_event_item_SWAP_RA_HIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `71`
- New: `72`

### Rust Evidence

- Graph edges: `1`

## W-000301 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_THP_MIGRATION_FAIL
- Explanation: vm_event_item_THP_MIGRATION_FAIL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `50`
- New: `51`

### Rust Evidence

- Graph edges: `1`

## W-000302 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_THP_MIGRATION_SPLIT
- Explanation: vm_event_item_THP_MIGRATION_SPLIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `51`
- New: `52`

### Rust Evidence

- Graph edges: `1`

## W-000303 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_THP_MIGRATION_SUCCESS
- Explanation: vm_event_item_THP_MIGRATION_SUCCESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `49`
- New: `50`

### Rust Evidence

- Graph edges: `1`

## W-000304 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_UNEVICTABLE_PGCLEARED
- Explanation: vm_event_item_UNEVICTABLE_PGCLEARED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `68`
- New: `69`

### Rust Evidence

- Graph edges: `1`

## W-000305 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_UNEVICTABLE_PGCULLED
- Explanation: vm_event_item_UNEVICTABLE_PGCULLED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `63`
- New: `64`

### Rust Evidence

- Graph edges: `1`

## W-000306 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_UNEVICTABLE_PGMLOCKED
- Explanation: vm_event_item_UNEVICTABLE_PGMLOCKED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `66`
- New: `67`

### Rust Evidence

- Graph edges: `1`

## W-000307 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_UNEVICTABLE_PGMUNLOCKED
- Explanation: vm_event_item_UNEVICTABLE_PGMUNLOCKED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `67`
- New: `68`

### Rust Evidence

- Graph edges: `1`

## W-000308 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_UNEVICTABLE_PGRESCUED
- Explanation: vm_event_item_UNEVICTABLE_PGRESCUED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `65`
- New: `66`

### Rust Evidence

- Graph edges: `1`

## W-000309 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_UNEVICTABLE_PGSCANNED
- Explanation: vm_event_item_UNEVICTABLE_PGSCANNED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `64`
- New: `65`

### Rust Evidence

- Graph edges: `1`

## W-000310 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: vm_event_item_UNEVICTABLE_PGSTRANDED
- Explanation: vm_event_item_UNEVICTABLE_PGSTRANDED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `69`
- New: `70`

### Rust Evidence

- Graph edges: `1`

## W-000311 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: ACPI_CA_VERSION
- Explanation: ACPI_CA_VERSION changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x20240322`
- New: `0x20240827`

### Rust Evidence

- Graph edges: `0`

## W-000312 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_MOUT_FSYS_USB30DRD_USER
- Explanation: CLK_MOUT_FSYS_USB30DRD_USER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `4`
- New: `11`

### Rust Evidence

- Graph edges: `0`
