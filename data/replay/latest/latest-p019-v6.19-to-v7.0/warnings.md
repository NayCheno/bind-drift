# BindDrift Ranked Warnings

## W-000307 SignatureDrift

- Risk: High
- Score: 14.6
- Symbol: sh
- Explanation: sh changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `50`

## W-000311 SignatureDrift

- Risk: High
- Score: 13.6
- Symbol: sl
- Explanation: sl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u64_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(16usize, 2u8) as u64) } } #[inline] pub fn set_sl(&mut self, val: u64_) { unsafe { let val: u64 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u32_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(11usize, 2u8) as u32) } } #[inline] pub fn set_sl(&mut self, val: u32_) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `15`

## W-000287 SignatureDrift

- Risk: High
- Score: 13.0
- Symbol: ps
- Explanation: ps changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `12`

## W-000353 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: bio
- Explanation: bio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'bi_next', 'type': '*mut bio'}, {'name': 'bi_bdev', 'type': '*mut block_device'}, {'name': 'bi_opf', 'type': 'blk_opf_t'}, {'name': 'bi_flags', 'type': 'ffi::c_ushort'}, {'name': 'bi_ioprio', 'type': 'ffi::c_ushort'}, {'name': 'bi_write_hint', 'type': 'rw_hint'}, {'name': 'bi_write_stream', 'type': 'u8_'}, {'name': 'bi_status', 'type': 'blk_status_t'}, {'name': 'bi_bvec_gap_bit', 'type': 'u8_'}, {'name': '__bi_remaining', 'type': 'atomic_t'}, {'name': 'bi_iter', 'type': 'bvec_iter'}, {'name': '__bindgen_anon_1', 'type': 'bio__bindgen_ty_1'}, {'name': 'bi_end_io', 'type': 'bio_end_io_t'}, {'name': 'bi_private', 'type': '*mut ffi::c_void'}, {'name': 'bi_blkg', 'type': '*mut blkcg_gq'}, {'name': 'issue_time_ns', 'type': 'u64_'}, {'name': 'bi_iocost_cost', 'type': 'u64_'}, {'name': 'bi_vcnt', 'type': 'ffi::c_ushort'}, {'name': 'bi_max_vecs', 'type': 'ffi::c_ushort'}, {'name': '__bi_cnt', 'type': 'atomic_t'}, {'name': 'bi_io_vec', 'type': '*mut bio_vec'}, {'name': 'bi_pool', 'type': '*mut bio_set'}]`
- New: `[{'name': 'bi_next', 'type': '*mut bio'}, {'name': 'bi_bdev', 'type': '*mut block_device'}, {'name': 'bi_opf', 'type': 'blk_opf_t'}, {'name': 'bi_flags', 'type': 'ffi::c_ushort'}, {'name': 'bi_ioprio', 'type': 'ffi::c_ushort'}, {'name': 'bi_write_hint', 'type': 'rw_hint'}, {'name': 'bi_write_stream', 'type': 'u8_'}, {'name': 'bi_status', 'type': 'blk_status_t'}, {'name': 'bi_bvec_gap_bit', 'type': 'u8_'}, {'name': '__bi_remaining', 'type': 'atomic_t'}, {'name': 'bi_io_vec', 'type': '*mut bio_vec'}, {'name': 'bi_iter', 'type': 'bvec_iter'}, {'name': '__bindgen_anon_1', 'type': 'bio__bindgen_ty_1'}, {'name': 'bi_end_io', 'type': 'bio_end_io_t'}, {'name': 'bi_private', 'type': '*mut ffi::c_void'}, {'name': 'bi_blkg', 'type': '*mut blkcg_gq'}, {'name': 'issue_time_ns', 'type': 'u64_'}, {'name': 'bi_iocost_cost', 'type': 'u64_'}, {'name': 'bi_vcnt', 'type': 'ffi::c_ushort'}, {'name': 'bi_max_vecs', 'type': 'ffi::c_ushort'}, {'name': '__bi_cnt', 'type': 'atomic_t'}, {'name': 'bi_pool', 'type': '*mut bio_set'}]`

### Rust Evidence

- Graph edges: `50`

## W-000355 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: bpf_prog
- Explanation: bpf_prog changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'pages', 'type': 'u16_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'type_', 'type': 'bpf_prog_type'}, {'name': 'expected_attach_type', 'type': 'bpf_attach_type'}, {'name': 'len', 'type': 'u32_'}, {'name': 'jited_len', 'type': 'u32_'}, {'name': '__bindgen_anon_1', 'type': 'bpf_prog__bindgen_ty_1'}, {'name': 'stats', 'type': '*mut bpf_prog_stats'}, {'name': 'active', 'type': '*mut ffi::c_int'}, {'name': 'bpf_func', 'type': '::core::option::Option<'}, {'name': 'aux', 'type': '*mut bpf_prog_aux'}, {'name': 'orig_prog', 'type': '*mut sock_fprog_kern'}, {'name': '__bindgen_anon_2', 'type': 'bpf_prog__bindgen_ty_2'}]`
- New: `[{'name': 'pages', 'type': 'u16_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'type_', 'type': 'bpf_prog_type'}, {'name': 'expected_attach_type', 'type': 'bpf_attach_type'}, {'name': 'len', 'type': 'u32_'}, {'name': 'jited_len', 'type': 'u32_'}, {'name': '__bindgen_anon_1', 'type': 'bpf_prog__bindgen_ty_1'}, {'name': 'stats', 'type': '*mut bpf_prog_stats'}, {'name': 'active', 'type': '*mut u8_'}, {'name': 'bpf_func', 'type': '::core::option::Option<'}, {'name': 'aux', 'type': '*mut bpf_prog_aux'}, {'name': 'orig_prog', 'type': '*mut sock_fprog_kern'}, {'name': '__bindgen_anon_2', 'type': 'bpf_prog__bindgen_ty_2'}]`

### Rust Evidence

- Graph edges: `50`

## W-000359 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: cgroup
- Explanation: cgroup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'self_', 'type': 'cgroup_subsys_state'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'level', 'type': 'ffi::c_int'}, {'name': 'max_depth', 'type': 'ffi::c_int'}, {'name': 'nr_descendants', 'type': 'ffi::c_int'}, {'name': 'nr_dying_descendants', 'type': 'ffi::c_int'}, {'name': 'max_descendants', 'type': 'ffi::c_int'}, {'name': 'nr_populated_csets', 'type': 'ffi::c_int'}, {'name': 'nr_populated_domain_children', 'type': 'ffi::c_int'}, {'name': 'nr_populated_threaded_children', 'type': 'ffi::c_int'}, {'name': 'nr_threaded_children', 'type': 'ffi::c_int'}, {'name': 'kill_seq', 'type': 'ffi::c_uint'}, {'name': 'kn', 'type': '*mut kernfs_node'}, {'name': 'procs_file', 'type': 'cgroup_file'}, {'name': 'events_file', 'type': 'cgroup_file'}, {'name': 'psi_files', 'type': '__IncompleteArrayField<cgroup_file>'}, {'name': 'subtree_control', 'type': 'u16_'}, {'name': 'subtree_ss_mask', 'type': 'u16_'}, {'name': 'old_subtree_control', 'type': 'u16_'}, {'name': 'old_subtree_ss_mask', 'type': 'u16_'}, {'name': 'subsys', 'type': '[*mut cgroup_subsys_state; 14usize]'}, {'name': 'nr_dying_subsys', 'type': '[ffi::c_int; 14usize]'}, {'name': 'root', 'type': '*mut cgroup_root'}, {'name': 'cset_links', 'type': 'list_head'}, {'name': 'e_csets', 'type': '[list_head; 14usize]'}, {'name': 'dom_cgrp', 'type': '*mut cgroup'}, {'name': 'old_dom_cgrp', 'type': '*mut cgroup'}, {'name': 'rstat_base_cpu', 'type': '*mut cgroup_rstat_base_cpu'}, {'name': '__bindgen_padding_0', 'type': 'u64'}, {'name': '_pad_', 'type': 'cacheline_padding'}, {'name': 'last_bstat', 'type': 'cgroup_base_stat'}, {'name': 'bstat', 'type': 'cgroup_base_stat'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'pidlists', 'type': 'list_head'}, {'name': 'pidlist_mutex', 'type': 'mutex'}, {'name': 'offline_waitq', 'type': 'wait_queue_head_t'}, {'name': 'release_agent_work', 'type': 'work_struct'}, {'name': 'psi', 'type': '*mut psi_group'}, {'name': 'bpf', 'type': 'cgroup_bpf'}, {'name': 'freezer', 'type': 'cgroup_freezer_state'}, {'name': '__bindgen_anon_1', 'type': 'cgroup__bindgen_ty_1'}]`
- New: `[{'name': 'self_', 'type': 'cgroup_subsys_state'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'level', 'type': 'ffi::c_int'}, {'name': 'max_depth', 'type': 'ffi::c_int'}, {'name': 'nr_descendants', 'type': 'ffi::c_int'}, {'name': 'nr_dying_descendants', 'type': 'ffi::c_int'}, {'name': 'max_descendants', 'type': 'ffi::c_int'}, {'name': 'nr_populated_csets', 'type': 'ffi::c_int'}, {'name': 'nr_populated_domain_children', 'type': 'ffi::c_int'}, {'name': 'nr_populated_threaded_children', 'type': 'ffi::c_int'}, {'name': 'nr_threaded_children', 'type': 'ffi::c_int'}, {'name': 'kill_seq', 'type': 'ffi::c_uint'}, {'name': 'kn', 'type': '*mut kernfs_node'}, {'name': 'procs_file', 'type': 'cgroup_file'}, {'name': 'events_file', 'type': 'cgroup_file'}, {'name': 'psi_files', 'type': '__IncompleteArrayField<cgroup_file>'}, {'name': 'subtree_control', 'type': 'u32_'}, {'name': 'subtree_ss_mask', 'type': 'u32_'}, {'name': 'old_subtree_control', 'type': 'u32_'}, {'name': 'old_subtree_ss_mask', 'type': 'u32_'}, {'name': 'subsys', 'type': '[*mut cgroup_subsys_state; 14usize]'}, {'name': 'nr_dying_subsys', 'type': '[ffi::c_int; 14usize]'}, {'name': 'root', 'type': '*mut cgroup_root'}, {'name': 'cset_links', 'type': 'list_head'}, {'name': 'e_csets', 'type': '[list_head; 14usize]'}, {'name': 'dom_cgrp', 'type': '*mut cgroup'}, {'name': 'old_dom_cgrp', 'type': '*mut cgroup'}, {'name': 'rstat_base_cpu', 'type': '*mut cgroup_rstat_base_cpu'}, {'name': '_pad_', 'type': 'cacheline_padding'}, {'name': 'last_bstat', 'type': 'cgroup_base_stat'}, {'name': 'bstat', 'type': 'cgroup_base_stat'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'pidlists', 'type': 'list_head'}, {'name': 'pidlist_mutex', 'type': 'mutex'}, {'name': 'offline_waitq', 'type': 'wait_queue_head_t'}, {'name': 'dying_populated_waitq', 'type': 'wait_queue_head_t'}, {'name': 'release_agent_work', 'type': 'work_struct'}, {'name': 'psi', 'type': '*mut psi_group'}, {'name': 'bpf', 'type': 'cgroup_bpf'}, {'name': 'freezer', 'type': 'cgroup_freezer_state'}, {'name': '__bindgen_anon_1', 'type': 'cgroup__bindgen_ty_1'}]`

### Rust Evidence

- Graph edges: `50`

## W-000362 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: device
- Explanation: device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'kobj', 'type': 'kobject'}, {'name': 'parent', 'type': '*mut device'}, {'name': 'p', 'type': '*mut device_private'}, {'name': 'init_name', 'type': '*const ffi::c_char'}, {'name': 'type_', 'type': '*const device_type'}, {'name': 'bus', 'type': '*const bus_type'}, {'name': 'driver', 'type': '*mut device_driver'}, {'name': 'platform_data', 'type': '*mut ffi::c_void'}, {'name': 'driver_data', 'type': '*mut ffi::c_void'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'links', 'type': 'dev_links_info'}, {'name': 'power', 'type': 'dev_pm_info'}, {'name': 'pm_domain', 'type': '*mut dev_pm_domain'}, {'name': 'msi', 'type': 'dev_msi_info'}, {'name': 'dma_mask', 'type': '*mut u64_'}, {'name': 'coherent_dma_mask', 'type': 'u64_'}, {'name': 'bus_dma_limit', 'type': 'u64_'}, {'name': 'dma_range_map', 'type': '*mut bus_dma_region'}, {'name': 'dma_parms', 'type': '*mut device_dma_parameters'}, {'name': 'dma_pools', 'type': 'list_head'}, {'name': 'dma_io_tlb_mem', 'type': '*mut io_tlb_mem'}, {'name': 'archdata', 'type': 'dev_archdata'}, {'name': 'of_node', 'type': '*mut device_node'}, {'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'numa_node', 'type': 'ffi::c_int'}, {'name': 'devt', 'type': 'dev_t'}, {'name': 'id', 'type': 'u32_'}, {'name': 'devres_lock', 'type': 'spinlock_t'}, {'name': 'devres_head', 'type': 'list_head'}, {'name': 'class', 'type': '*const class'}, {'name': 'groups', 'type': '*mut *const attribute_group'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'iommu_group', 'type': '*mut iommu_group'}, {'name': 'iommu', 'type': '*mut dev_iommu'}, {'name': 'physical_location', 'type': '*mut device_physical_location'}, {'name': 'removable', 'type': 'device_removable'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 3usize]'}]`
- New: `[{'name': 'kobj', 'type': 'kobject'}, {'name': 'parent', 'type': '*mut device'}, {'name': 'p', 'type': '*mut device_private'}, {'name': 'init_name', 'type': '*const ffi::c_char'}, {'name': 'type_', 'type': '*const device_type'}, {'name': 'bus', 'type': '*const bus_type'}, {'name': 'driver', 'type': '*mut device_driver'}, {'name': 'platform_data', 'type': '*mut ffi::c_void'}, {'name': 'driver_data', 'type': '*mut ffi::c_void'}, {'name': 'driver_override', 'type': 'device__bindgen_ty_1'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'links', 'type': 'dev_links_info'}, {'name': 'power', 'type': 'dev_pm_info'}, {'name': 'pm_domain', 'type': '*mut dev_pm_domain'}, {'name': 'msi', 'type': 'dev_msi_info'}, {'name': 'dma_mask', 'type': '*mut u64_'}, {'name': 'coherent_dma_mask', 'type': 'u64_'}, {'name': 'bus_dma_limit', 'type': 'u64_'}, {'name': 'dma_range_map', 'type': '*mut bus_dma_region'}, {'name': 'dma_parms', 'type': '*mut device_dma_parameters'}, {'name': 'dma_pools', 'type': 'list_head'}, {'name': 'dma_io_tlb_mem', 'type': '*mut io_tlb_mem'}, {'name': 'archdata', 'type': 'dev_archdata'}, {'name': 'of_node', 'type': '*mut device_node'}, {'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'numa_node', 'type': 'ffi::c_int'}, {'name': 'devt', 'type': 'dev_t'}, {'name': 'id', 'type': 'u32_'}, {'name': 'devres_lock', 'type': 'spinlock_t'}, {'name': 'devres_head', 'type': 'list_head'}, {'name': 'class', 'type': '*const class'}, {'name': 'groups', 'type': '*mut *const attribute_group'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'iommu_group', 'type': '*mut iommu_group'}, {'name': 'iommu', 'type': '*mut dev_iommu'}, {'name': 'physical_location', 'type': '*mut device_physical_location'}, {'name': 'removable', 'type': 'device_removable'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 3usize]'}]`

### Rust Evidence

- Graph edges: `50`

## W-000363 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: drm_file
- Explanation: drm_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'authenticated', 'type': 'bool_'}, {'name': 'stereo_allowed', 'type': 'bool_'}, {'name': 'universal_planes', 'type': 'bool_'}, {'name': 'atomic', 'type': 'bool_'}, {'name': 'aspect_ratio_allowed', 'type': 'bool_'}, {'name': 'writeback_connectors', 'type': 'bool_'}, {'name': 'plane_color_pipeline', 'type': 'bool_'}, {'name': 'was_master', 'type': 'bool_'}, {'name': 'is_master', 'type': 'bool_'}, {'name': 'supports_virtualized_cursor_plane', 'type': 'bool_'}, {'name': 'master', 'type': '*mut drm_master'}, {'name': 'master_lookup_lock', 'type': 'spinlock_t'}, {'name': 'pid', 'type': '*mut pid'}, {'name': 'client_id', 'type': 'u64_'}, {'name': 'magic', 'type': 'drm_magic_t'}, {'name': 'lhead', 'type': 'list_head'}, {'name': 'minor', 'type': '*mut drm_minor'}, {'name': 'object_idr', 'type': 'idr'}, {'name': 'table_lock', 'type': 'spinlock_t'}, {'name': 'syncobj_idr', 'type': 'idr'}, {'name': 'syncobj_table_lock', 'type': 'spinlock_t'}, {'name': 'filp', 'type': '*mut file'}, {'name': 'driver_priv', 'type': '*mut ffi::c_void'}, {'name': 'fbs', 'type': 'list_head'}, {'name': 'fbs_lock', 'type': 'mutex'}, {'name': 'blobs', 'type': 'list_head'}, {'name': 'event_wait', 'type': 'wait_queue_head_t'}, {'name': 'pending_event_list', 'type': 'list_head'}, {'name': 'event_list', 'type': 'list_head'}, {'name': 'event_space', 'type': 'ffi::c_int'}, {'name': 'event_read_lock', 'type': 'mutex'}, {'name': 'prime', 'type': 'drm_prime_file_private'}, {'name': 'client_name', 'type': '*const ffi::c_char'}, {'name': 'client_name_lock', 'type': 'mutex'}, {'name': 'debugfs_client', 'type': '*mut dentry'}]`
- New: `[{'name': 'authenticated', 'type': 'bool_'}, {'name': 'stereo_allowed', 'type': 'bool_'}, {'name': 'universal_planes', 'type': 'bool_'}, {'name': 'atomic', 'type': 'bool_'}, {'name': 'aspect_ratio_allowed', 'type': 'bool_'}, {'name': 'writeback_connectors', 'type': 'bool_'}, {'name': 'plane_color_pipeline', 'type': 'bool_'}, {'name': 'was_master', 'type': 'bool_'}, {'name': 'is_master', 'type': 'bool_'}, {'name': 'supports_virtualized_cursor_plane', 'type': 'bool_'}, {'name': 'master', 'type': '*mut drm_master'}, {'name': 'master_lookup_lock', 'type': 'spinlock_t'}, {'name': 'pid', 'type': '*mut pid'}, {'name': 'client_id', 'type': 'u64_'}, {'name': 'magic', 'type': 'drm_magic_t'}, {'name': 'lhead', 'type': 'list_head'}, {'name': 'minor', 'type': '*mut drm_minor'}, {'name': 'object_idr', 'type': 'idr'}, {'name': 'table_lock', 'type': 'spinlock_t'}, {'name': 'syncobj_xa', 'type': 'xarray'}, {'name': 'filp', 'type': '*mut file'}, {'name': 'driver_priv', 'type': '*mut ffi::c_void'}, {'name': 'fbs', 'type': 'list_head'}, {'name': 'fbs_lock', 'type': 'mutex'}, {'name': 'blobs', 'type': 'list_head'}, {'name': 'event_wait', 'type': 'wait_queue_head_t'}, {'name': 'pending_event_list', 'type': 'list_head'}, {'name': 'event_list', 'type': 'list_head'}, {'name': 'event_space', 'type': 'ffi::c_int'}, {'name': 'event_read_lock', 'type': 'mutex'}, {'name': 'prime', 'type': 'drm_prime_file_private'}, {'name': 'client_name', 'type': '*const ffi::c_char'}, {'name': 'client_name_lock', 'type': 'mutex'}, {'name': 'debugfs_client', 'type': '*mut dentry'}]`

### Rust Evidence

- Graph edges: `47`

## W-000370 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: irq_chip
- Explanation: irq_chip changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'irq_shutdown', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_enable', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_disable', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_ack', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_mask', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_mask_ack', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_unmask', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_eoi', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_set_affinity', 'type': '::core::option::Option<'}, {'name': 'irq_set_type', 'type': '::core::option::Option<'}, {'name': 'irq_set_wake', 'type': '::core::option::Option<'}, {'name': 'irq_bus_lock', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_bus_sync_unlock', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_suspend', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_resume', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_pm_shutdown', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_calc_mask', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_release_resources', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_get_irqchip_state', 'type': '::core::option::Option<'}, {'name': 'irq_set_irqchip_state', 'type': '::core::option::Option<'}, {'name': 'irq_set_vcpu_affinity', 'type': '::core::option::Option<'}, {'name': 'irq_nmi_teardown', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_force_complete_move', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'flags', 'type': 'ffi::c_ulong'}]`
- New: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'irq_shutdown', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_enable', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_disable', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_ack', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_mask', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_mask_ack', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_unmask', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_eoi', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_set_affinity', 'type': '::core::option::Option<'}, {'name': 'irq_pre_redirect', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_set_type', 'type': '::core::option::Option<'}, {'name': 'irq_set_wake', 'type': '::core::option::Option<'}, {'name': 'irq_bus_lock', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_bus_sync_unlock', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_suspend', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_resume', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_pm_shutdown', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_calc_mask', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_release_resources', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_get_irqchip_state', 'type': '::core::option::Option<'}, {'name': 'irq_set_irqchip_state', 'type': '::core::option::Option<'}, {'name': 'irq_set_vcpu_affinity', 'type': '::core::option::Option<'}, {'name': 'irq_nmi_teardown', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'irq_force_complete_move', 'type': '::core::option::Option<unsafe extern "C" fn(data: *mut irq_data)>'}, {'name': 'flags', 'type': 'ffi::c_ulong'}]`

### Rust Evidence

- Graph edges: `27`

## W-000381 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: pci_dev
- Explanation: pci_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'rebar_cap', 'type': 'u16_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 11usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pri_cap', 'type': 'u16_'}, {'name': 'pri_reqs_alloc', 'type': 'u32_'}, {'name': '_bitfield_align_5', 'type': '[u8; 0]'}, {'name': '_bitfield_5', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`
- New: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'rebar_cap', 'type': 'u16_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'msi_addr_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 11usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pri_cap', 'type': 'u16_'}, {'name': 'pri_reqs_alloc', 'type': 'u32_'}, {'name': '_bitfield_align_5', 'type': '[u8; 0]'}, {'name': '_bitfield_5', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'acs_capabilities', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`

### Rust Evidence

- Graph edges: `50`

## W-000384 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: phy_device
- Explanation: phy_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mdio', 'type': 'mdio_device'}, {'name': 'drv', 'type': '*const phy_driver'}, {'name': 'devlink', 'type': '*mut device_link'}, {'name': 'phyindex', 'type': 'u32_'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'c45_ids', 'type': 'phy_c45_device_ids'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'rate_matching', 'type': 'ffi::c_int'}, {'name': 'state', 'type': 'phy_state'}, {'name': 'dev_flags', 'type': 'u32_'}, {'name': 'interface', 'type': 'phy_interface_t'}, {'name': 'possible_interfaces', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'speed', 'type': 'ffi::c_int'}, {'name': 'duplex', 'type': 'ffi::c_int'}, {'name': 'port', 'type': 'ffi::c_int'}, {'name': 'master_slave_get', 'type': 'u8_'}, {'name': 'master_slave_set', 'type': 'u8_'}, {'name': 'master_slave_state', 'type': 'u8_'}, {'name': 'supported', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'advertising', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'lp_advertising', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'adv_old', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'supported_eee', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'advertising_eee', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'eee_disabled_modes', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'enable_tx_lpi', 'type': 'bool_'}, {'name': 'eee_active', 'type': 'bool_'}, {'name': 'eee_cfg', 'type': 'eee_config'}, {'name': 'host_interfaces', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'leds', 'type': 'list_head'}, {'name': 'irq', 'type': 'ffi::c_int'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'ehdr', 'type': '*mut ffi::c_void'}, {'name': 'nest', 'type': '*mut nlattr'}, {'name': 'state_queue', 'type': 'delayed_work'}, {'name': 'lock', 'type': 'mutex'}, {'name': 'sfp_bus_attached', 'type': 'bool_'}, {'name': 'sfp_bus', 'type': '*mut sfp_bus'}, {'name': 'phylink', 'type': '*mut phylink'}, {'name': 'attached_dev', 'type': '*mut net_device'}, {'name': 'mii_ts', 'type': '*mut mii_timestamper'}, {'name': 'psec', 'type': '*mut pse_control'}, {'name': 'mdix', 'type': 'u8_'}, {'name': 'mdix_ctrl', 'type': 'u8_'}, {'name': 'pma_extable', 'type': 'ffi::c_int'}, {'name': 'link_down_events', 'type': 'ffi::c_uint'}, {'name': 'adjust_link', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut net_device)>'}, {'name': 'oatc14_sqi_capability', 'type': 'phy_oatc14_sqi_capability'}]`
- New: `[{'name': 'mdio', 'type': 'mdio_device'}, {'name': 'drv', 'type': '*const phy_driver'}, {'name': 'devlink', 'type': '*mut device_link'}, {'name': 'phyindex', 'type': 'u32_'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'c45_ids', 'type': 'phy_c45_device_ids'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'rate_matching', 'type': 'ffi::c_int'}, {'name': 'state', 'type': 'phy_state'}, {'name': 'dev_flags', 'type': 'u32_'}, {'name': 'interface', 'type': 'phy_interface_t'}, {'name': 'possible_interfaces', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'speed', 'type': 'ffi::c_int'}, {'name': 'duplex', 'type': 'ffi::c_int'}, {'name': 'port', 'type': 'ffi::c_int'}, {'name': 'master_slave_get', 'type': 'u8_'}, {'name': 'master_slave_set', 'type': 'u8_'}, {'name': 'master_slave_state', 'type': 'u8_'}, {'name': 'supported', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'advertising', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'lp_advertising', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'adv_old', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'supported_eee', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'advertising_eee', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'eee_disabled_modes', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'enable_tx_lpi', 'type': 'bool_'}, {'name': 'eee_active', 'type': 'bool_'}, {'name': 'eee_cfg', 'type': 'eee_config'}, {'name': 'host_interfaces', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'leds', 'type': 'list_head'}, {'name': 'irq', 'type': 'ffi::c_int'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'ehdr', 'type': '*mut ffi::c_void'}, {'name': 'nest', 'type': '*mut nlattr'}, {'name': 'state_queue', 'type': 'delayed_work'}, {'name': 'lock', 'type': 'mutex'}, {'name': 'sfp_bus_attached', 'type': 'bool_'}, {'name': 'sfp_bus', 'type': '*mut sfp_bus'}, {'name': 'phylink', 'type': '*mut phylink'}, {'name': 'attached_dev', 'type': '*mut net_device'}, {'name': 'mii_ts', 'type': '*mut mii_timestamper'}, {'name': 'psec', 'type': '*mut pse_control'}, {'name': 'ports', 'type': 'list_head'}, {'name': 'n_ports', 'type': 'ffi::c_int'}, {'name': 'max_n_ports', 'type': 'ffi::c_int'}, {'name': 'mdix', 'type': 'u8_'}, {'name': 'mdix_ctrl', 'type': 'u8_'}, {'name': 'pma_extable', 'type': 'ffi::c_int'}, {'name': 'link_down_events', 'type': 'ffi::c_uint'}, {'name': 'adjust_link', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut net_device)>'}, {'name': 'oatc14_sqi_capability', 'type': 'phy_oatc14_sqi_capability'}]`

### Rust Evidence

- Graph edges: `50`

## W-000385 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: phy_driver
- Explanation: phy_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mdiodrv', 'type': 'mdio_driver_common'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'name', 'type': '*mut ffi::c_char'}, {'name': 'phy_id_mask', 'type': 'u32_'}, {'name': 'features', 'type': '*const ffi::c_ulong'}, {'name': 'flags', 'type': 'u32_'}, {'name': 'driver_data', 'type': '*const ffi::c_void'}, {'name': 'probe', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device) -> ffi::c_int>'}, {'name': 'inband_caps', 'type': '::core::option::Option<'}, {'name': 'config_inband', 'type': '::core::option::Option<'}, {'name': 'get_rate_matching', 'type': '::core::option::Option<'}, {'name': 'resume', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device) -> ffi::c_int>'}, {'name': 'remove', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device)>'}, {'name': 'match_phy_device', 'type': '::core::option::Option<'}, {'name': 'set_wol', 'type': '::core::option::Option<'}, {'name': 'get_wol', 'type': '::core::option::Option<'}, {'name': 'link_change_notify', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device)>'}, {'name': 'read_mmd', 'type': '::core::option::Option<'}, {'name': 'write_mmd', 'type': '::core::option::Option<'}, {'name': 'read_page', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device) -> ffi::c_int>'}, {'name': 'write_page', 'type': '::core::option::Option<'}, {'name': 'module_info', 'type': '::core::option::Option<'}, {'name': 'module_eeprom', 'type': '::core::option::Option<'}, {'name': 'cable_test_tdr_start', 'type': '::core::option::Option<'}, {'name': 'cable_test_get_status', 'type': '::core::option::Option<'}, {'name': 'get_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_link_stats', 'type': '::core::option::Option<'}, {'name': 'get_stats', 'type': '::core::option::Option<'}, {'name': 'get_tunable', 'type': '::core::option::Option<'}, {'name': 'set_tunable', 'type': '::core::option::Option<'}, {'name': 'set_loopback', 'type': '::core::option::Option<'}, {'name': 'get_sqi', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device) -> ffi::c_int>'}, {'name': 'get_mse_capability', 'type': '::core::option::Option<'}, {'name': 'get_mse_snapshot', 'type': '::core::option::Option<'}, {'name': 'get_plca_cfg', 'type': '::core::option::Option<'}, {'name': 'set_plca_cfg', 'type': '::core::option::Option<'}, {'name': 'get_plca_status', 'type': '::core::option::Option<'}, {'name': 'led_brightness_set', 'type': '::core::option::Option<'}, {'name': 'led_blink_set', 'type': '::core::option::Option<'}, {'name': 'led_hw_is_supported', 'type': '::core::option::Option<'}, {'name': 'led_hw_control_set', 'type': '::core::option::Option<'}, {'name': 'led_hw_control_get', 'type': '::core::option::Option<'}, {'name': 'led_polarity_set', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'mdiodrv', 'type': 'mdio_driver_common'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'name', 'type': '*mut ffi::c_char'}, {'name': 'phy_id_mask', 'type': 'u32_'}, {'name': 'features', 'type': '*const ffi::c_ulong'}, {'name': 'flags', 'type': 'u32_'}, {'name': 'driver_data', 'type': '*const ffi::c_void'}, {'name': 'probe', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device) -> ffi::c_int>'}, {'name': 'inband_caps', 'type': '::core::option::Option<'}, {'name': 'config_inband', 'type': '::core::option::Option<'}, {'name': 'get_rate_matching', 'type': '::core::option::Option<'}, {'name': 'resume', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device) -> ffi::c_int>'}, {'name': 'remove', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device)>'}, {'name': 'match_phy_device', 'type': '::core::option::Option<'}, {'name': 'set_wol', 'type': '::core::option::Option<'}, {'name': 'get_wol', 'type': '::core::option::Option<'}, {'name': 'link_change_notify', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device)>'}, {'name': 'read_mmd', 'type': '::core::option::Option<'}, {'name': 'write_mmd', 'type': '::core::option::Option<'}, {'name': 'read_page', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device) -> ffi::c_int>'}, {'name': 'write_page', 'type': '::core::option::Option<'}, {'name': 'module_info', 'type': '::core::option::Option<'}, {'name': 'module_eeprom', 'type': '::core::option::Option<'}, {'name': 'cable_test_tdr_start', 'type': '::core::option::Option<'}, {'name': 'cable_test_get_status', 'type': '::core::option::Option<'}, {'name': 'get_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_link_stats', 'type': '::core::option::Option<'}, {'name': 'get_stats', 'type': '::core::option::Option<'}, {'name': 'get_tunable', 'type': '::core::option::Option<'}, {'name': 'set_tunable', 'type': '::core::option::Option<'}, {'name': 'set_loopback', 'type': '::core::option::Option<'}, {'name': 'get_sqi', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device) -> ffi::c_int>'}, {'name': 'get_mse_capability', 'type': '::core::option::Option<'}, {'name': 'get_mse_snapshot', 'type': '::core::option::Option<'}, {'name': 'get_plca_cfg', 'type': '::core::option::Option<'}, {'name': 'set_plca_cfg', 'type': '::core::option::Option<'}, {'name': 'get_plca_status', 'type': '::core::option::Option<'}, {'name': 'led_brightness_set', 'type': '::core::option::Option<'}, {'name': 'led_blink_set', 'type': '::core::option::Option<'}, {'name': 'led_hw_is_supported', 'type': '::core::option::Option<'}, {'name': 'led_hw_control_set', 'type': '::core::option::Option<'}, {'name': 'led_hw_control_get', 'type': '::core::option::Option<'}, {'name': 'led_polarity_set', 'type': '::core::option::Option<'}, {'name': 'attach_mii_port', 'type': '::core::option::Option<'}, {'name': 'attach_mdi_port', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `27`

## W-000387 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: pid_namespace
- Explanation: pid_namespace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'idr', 'type': 'idr'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'pid_allocated', 'type': 'ffi::c_uint'}, {'name': 'child_reaper', 'type': '*mut task_struct'}, {'name': 'pid_cachep', 'type': '*mut kmem_cache'}, {'name': 'level', 'type': 'ffi::c_uint'}, {'name': 'pid_max', 'type': 'ffi::c_int'}, {'name': 'parent', 'type': '*mut pid_namespace'}, {'name': 'bacct', 'type': '*mut fs_pin'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'ucounts', 'type': '*mut ucounts'}, {'name': 'reboot', 'type': 'ffi::c_int'}, {'name': 'ns', 'type': 'ns_common'}, {'name': 'work', 'type': 'work_struct'}, {'name': 'set', 'type': 'ctl_table_set'}, {'name': 'sysctls', 'type': '*mut ctl_table_header'}, {'name': 'memfd_noexec_scope', 'type': 'ffi::c_int'}]`
- New: `[{'name': 'idr', 'type': 'idr'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'pid_allocated', 'type': 'ffi::c_uint'}, {'name': 'memfd_noexec_scope', 'type': 'ffi::c_int'}, {'name': 'set', 'type': 'ctl_table_set'}, {'name': 'sysctls', 'type': '*mut ctl_table_header'}, {'name': 'child_reaper', 'type': '*mut task_struct'}, {'name': 'pid_cachep', 'type': '*mut kmem_cache'}, {'name': 'level', 'type': 'ffi::c_uint'}, {'name': 'pid_max', 'type': 'ffi::c_int'}, {'name': 'parent', 'type': '*mut pid_namespace'}, {'name': 'bacct', 'type': '*mut fs_pin'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'ucounts', 'type': '*mut ucounts'}, {'name': 'reboot', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': '[u64; 4usize]'}, {'name': 'ns', 'type': 'ns_common'}, {'name': 'work', 'type': 'work_struct'}]`

### Rust Evidence

- Graph edges: `24`

## W-000388 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: platform_device
- Explanation: platform_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'id_auto', 'type': 'bool_'}, {'name': 'dev', 'type': 'device'}, {'name': 'platform_dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'num_resources', 'type': 'u32_'}, {'name': 'resource', 'type': '*mut resource'}, {'name': 'id_entry', 'type': '*const platform_device_id'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'mfd_cell', 'type': '*mut mfd_cell'}, {'name': 'archdata', 'type': 'pdev_archdata'}]`
- New: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'id_auto', 'type': 'bool_'}, {'name': 'dev', 'type': 'device'}, {'name': 'platform_dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'num_resources', 'type': 'u32_'}, {'name': 'resource', 'type': '*mut resource'}, {'name': 'id_entry', 'type': '*const platform_device_id'}, {'name': 'mfd_cell', 'type': '*mut mfd_cell'}, {'name': 'archdata', 'type': 'pdev_archdata'}]`

### Rust Evidence

- Graph edges: `36`

## W-000401 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: usb_device
- Explanation: usb_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'devnum', 'type': 'ffi::c_int'}, {'name': 'devpath', 'type': '[ffi::c_char; 16usize]'}, {'name': 'route', 'type': 'u32_'}, {'name': 'state', 'type': 'usb_device_state'}, {'name': 'speed', 'type': 'usb_device_speed'}, {'name': 'rx_lanes', 'type': 'ffi::c_uint'}, {'name': 'tx_lanes', 'type': 'ffi::c_uint'}, {'name': 'ssp_rate', 'type': 'usb_ssp_rate'}, {'name': 'tt', 'type': '*mut usb_tt'}, {'name': 'ttport', 'type': 'ffi::c_int'}, {'name': 'toggle', 'type': '[ffi::c_uint; 2usize]'}, {'name': 'parent', 'type': '*mut usb_device'}, {'name': 'bus', 'type': '*mut usb_bus'}, {'name': 'ep0', 'type': 'usb_host_endpoint'}, {'name': 'dev', 'type': 'device'}, {'name': 'descriptor', 'type': 'usb_device_descriptor'}, {'name': 'bos', 'type': '*mut usb_host_bos'}, {'name': 'config', 'type': '*mut usb_host_config'}, {'name': 'actconfig', 'type': '*mut usb_host_config'}, {'name': 'ep_in', 'type': '[*mut usb_host_endpoint; 16usize]'}, {'name': 'ep_out', 'type': '[*mut usb_host_endpoint; 16usize]'}, {'name': 'rawdescriptors', 'type': '*mut *mut ffi::c_char'}, {'name': 'bus_mA', 'type': 'ffi::c_ushort'}, {'name': 'portnum', 'type': 'u8_'}, {'name': 'level', 'type': 'u8_'}, {'name': 'devaddr', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'string_langid', 'type': 'ffi::c_int'}, {'name': 'product', 'type': '*mut ffi::c_char'}, {'name': 'manufacturer', 'type': '*mut ffi::c_char'}, {'name': 'serial', 'type': '*mut ffi::c_char'}, {'name': 'filelist', 'type': 'list_head'}, {'name': 'maxchild', 'type': 'ffi::c_int'}, {'name': 'quirks', 'type': 'u32_'}, {'name': 'urbnum', 'type': 'atomic_t'}, {'name': 'active_duration', 'type': 'ffi::c_ulong'}, {'name': 'connect_time', 'type': 'ffi::c_ulong'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'offload_usage', 'type': 'ffi::c_int'}, {'name': 'tunnel_mode', 'type': 'usb_link_tunnel_mode'}, {'name': 'usb4_link', 'type': '*mut device_link'}, {'name': 'slot_id', 'type': 'ffi::c_int'}, {'name': 'l1_params', 'type': 'usb2_lpm_parameters'}, {'name': 'u1_params', 'type': 'usb3_lpm_parameters'}, {'name': 'u2_params', 'type': 'usb3_lpm_parameters'}, {'name': 'lpm_disable_count', 'type': 'ffi::c_uint'}, {'name': 'hub_delay', 'type': 'u16_'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 5usize]'}]`
- New: `[{'name': 'devnum', 'type': 'ffi::c_int'}, {'name': 'devpath', 'type': '[ffi::c_char; 16usize]'}, {'name': 'route', 'type': 'u32_'}, {'name': 'state', 'type': 'usb_device_state'}, {'name': 'speed', 'type': 'usb_device_speed'}, {'name': 'rx_lanes', 'type': 'ffi::c_uint'}, {'name': 'tx_lanes', 'type': 'ffi::c_uint'}, {'name': 'ssp_rate', 'type': 'usb_ssp_rate'}, {'name': 'tt', 'type': '*mut usb_tt'}, {'name': 'ttport', 'type': 'ffi::c_int'}, {'name': 'toggle', 'type': '[ffi::c_uint; 2usize]'}, {'name': 'parent', 'type': '*mut usb_device'}, {'name': 'bus', 'type': '*mut usb_bus'}, {'name': 'ep0', 'type': 'usb_host_endpoint'}, {'name': 'dev', 'type': 'device'}, {'name': 'descriptor', 'type': 'usb_device_descriptor'}, {'name': 'bos', 'type': '*mut usb_host_bos'}, {'name': 'config', 'type': '*mut usb_host_config'}, {'name': 'actconfig', 'type': '*mut usb_host_config'}, {'name': 'ep_in', 'type': '[*mut usb_host_endpoint; 16usize]'}, {'name': 'ep_out', 'type': '[*mut usb_host_endpoint; 16usize]'}, {'name': 'rawdescriptors', 'type': '*mut *mut ffi::c_char'}, {'name': 'bus_mA', 'type': 'ffi::c_ushort'}, {'name': 'portnum', 'type': 'u8_'}, {'name': 'level', 'type': 'u8_'}, {'name': 'devaddr', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'string_langid', 'type': 'ffi::c_int'}, {'name': 'product', 'type': '*mut ffi::c_char'}, {'name': 'manufacturer', 'type': '*mut ffi::c_char'}, {'name': 'serial', 'type': '*mut ffi::c_char'}, {'name': 'filelist', 'type': 'list_head'}, {'name': 'maxchild', 'type': 'ffi::c_int'}, {'name': 'quirks', 'type': 'u32_'}, {'name': 'urbnum', 'type': 'atomic_t'}, {'name': 'active_duration', 'type': 'ffi::c_ulong'}, {'name': 'connect_time', 'type': 'ffi::c_ulong'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'offload_usage', 'type': 'ffi::c_int'}, {'name': 'offload_lock', 'type': 'spinlock_t'}, {'name': 'tunnel_mode', 'type': 'usb_link_tunnel_mode'}, {'name': 'usb4_link', 'type': '*mut device_link'}, {'name': 'slot_id', 'type': 'ffi::c_int'}, {'name': 'l1_params', 'type': 'usb2_lpm_parameters'}, {'name': 'u1_params', 'type': 'usb3_lpm_parameters'}, {'name': 'u2_params', 'type': 'usb3_lpm_parameters'}, {'name': 'lpm_disable_count', 'type': 'ffi::c_uint'}, {'name': 'hub_delay', 'type': 'u16_'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 5usize]'}]`

### Rust Evidence

- Graph edges: `50`

## W-000376 FieldDrift

- Risk: High
- Score: 12.4
- Symbol: mdio_device
- Explanation: mdio_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'dev', 'type': 'device'}, {'name': 'bus', 'type': '*mut mii_bus'}, {'name': 'modalias', 'type': '[ffi::c_char; 32usize]'}, {'name': 'bus_match', 'type': '::core::option::Option<'}, {'name': 'device_free', 'type': '::core::option::Option<unsafe extern "C" fn(mdiodev: *mut mdio_device)>'}, {'name': 'device_remove', 'type': '::core::option::Option<unsafe extern "C" fn(mdiodev: *mut mdio_device)>'}, {'name': 'addr', 'type': 'ffi::c_int'}, {'name': 'flags', 'type': 'ffi::c_int'}, {'name': 'reset_state', 'type': 'ffi::c_int'}, {'name': 'reset_gpio', 'type': '*mut gpio_desc'}, {'name': 'reset_ctrl', 'type': '*mut reset_control'}, {'name': 'reset_assert_delay', 'type': 'ffi::c_uint'}, {'name': 'reset_deassert_delay', 'type': 'ffi::c_uint'}]`
- New: `[{'name': 'dev', 'type': 'device'}, {'name': 'bus', 'type': '*mut mii_bus'}, {'name': 'bus_match', 'type': '::core::option::Option<'}, {'name': 'device_free', 'type': '::core::option::Option<unsafe extern "C" fn(mdiodev: *mut mdio_device)>'}, {'name': 'device_remove', 'type': '::core::option::Option<unsafe extern "C" fn(mdiodev: *mut mdio_device)>'}, {'name': 'addr', 'type': 'ffi::c_int'}, {'name': 'flags', 'type': 'ffi::c_int'}, {'name': 'reset_state', 'type': 'ffi::c_int'}, {'name': 'reset_gpio', 'type': '*mut gpio_desc'}, {'name': 'reset_ctrl', 'type': '*mut reset_control'}, {'name': 'reset_assert_delay', 'type': 'ffi::c_uint'}, {'name': 'reset_deassert_delay', 'type': 'ffi::c_uint'}]`

### Rust Evidence

- Graph edges: `19`

## W-000400 FieldDrift

- Risk: High
- Score: 12.4
- Symbol: taskstats
- Explanation: taskstats changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'version', 'type': '__u16'}, {'name': 'ac_exitcode', 'type': '__u32'}, {'name': 'ac_flag', 'type': '__u8'}, {'name': 'ac_nice', 'type': '__u8'}, {'name': 'cpu_count', 'type': '__u64'}, {'name': 'cpu_delay_total', 'type': '__u64'}, {'name': 'blkio_count', 'type': '__u64'}, {'name': 'blkio_delay_total', 'type': '__u64'}, {'name': 'swapin_count', 'type': '__u64'}, {'name': 'swapin_delay_total', 'type': '__u64'}, {'name': 'cpu_run_real_total', 'type': '__u64'}, {'name': 'cpu_run_virtual_total', 'type': '__u64'}, {'name': 'ac_comm', 'type': '[ffi::c_char; 32usize]'}, {'name': 'ac_sched', 'type': '__u8'}, {'name': 'ac_pad', 'type': '[__u8; 3usize]'}, {'name': '__bindgen_padding_0', 'type': 'u32'}, {'name': 'ac_uid', 'type': '__u32'}, {'name': 'ac_gid', 'type': '__u32'}, {'name': 'ac_pid', 'type': '__u32'}, {'name': 'ac_ppid', 'type': '__u32'}, {'name': 'ac_btime', 'type': '__u32'}, {'name': 'ac_etime', 'type': '__u64'}, {'name': 'ac_utime', 'type': '__u64'}, {'name': 'ac_stime', 'type': '__u64'}, {'name': 'ac_minflt', 'type': '__u64'}, {'name': 'ac_majflt', 'type': '__u64'}, {'name': 'coremem', 'type': '__u64'}, {'name': 'virtmem', 'type': '__u64'}, {'name': 'hiwater_rss', 'type': '__u64'}, {'name': 'hiwater_vm', 'type': '__u64'}, {'name': 'read_char', 'type': '__u64'}, {'name': 'write_char', 'type': '__u64'}, {'name': 'read_syscalls', 'type': '__u64'}, {'name': 'write_syscalls', 'type': '__u64'}, {'name': 'read_bytes', 'type': '__u64'}, {'name': 'write_bytes', 'type': '__u64'}, {'name': 'cancelled_write_bytes', 'type': '__u64'}, {'name': 'nvcsw', 'type': '__u64'}, {'name': 'nivcsw', 'type': '__u64'}, {'name': 'ac_utimescaled', 'type': '__u64'}, {'name': 'ac_stimescaled', 'type': '__u64'}, {'name': 'cpu_scaled_run_real_total', 'type': '__u64'}, {'name': 'freepages_count', 'type': '__u64'}, {'name': 'freepages_delay_total', 'type': '__u64'}, {'name': 'thrashing_count', 'type': '__u64'}, {'name': 'thrashing_delay_total', 'type': '__u64'}, {'name': 'ac_btime64', 'type': '__u64'}, {'name': 'compact_count', 'type': '__u64'}, {'name': 'compact_delay_total', 'type': '__u64'}, {'name': 'ac_tgid', 'type': '__u32'}, {'name': 'ac_tgetime', 'type': '__u64'}, {'name': 'ac_exe_dev', 'type': '__u64'}, {'name': 'ac_exe_inode', 'type': '__u64'}, {'name': 'wpcopy_count', 'type': '__u64'}, {'name': 'wpcopy_delay_total', 'type': '__u64'}, {'name': 'irq_count', 'type': '__u64'}, {'name': 'irq_delay_total', 'type': '__u64'}, {'name': 'cpu_delay_max', 'type': '__u64'}, {'name': 'cpu_delay_min', 'type': '__u64'}, {'name': 'blkio_delay_max', 'type': '__u64'}, {'name': 'blkio_delay_min', 'type': '__u64'}, {'name': 'swapin_delay_max', 'type': '__u64'}, {'name': 'swapin_delay_min', 'type': '__u64'}, {'name': 'freepages_delay_max', 'type': '__u64'}, {'name': 'freepages_delay_min', 'type': '__u64'}, {'name': 'thrashing_delay_max', 'type': '__u64'}, {'name': 'thrashing_delay_min', 'type': '__u64'}, {'name': 'compact_delay_max', 'type': '__u64'}, {'name': 'compact_delay_min', 'type': '__u64'}, {'name': 'wpcopy_delay_max', 'type': '__u64'}, {'name': 'wpcopy_delay_min', 'type': '__u64'}, {'name': 'irq_delay_max', 'type': '__u64'}, {'name': 'irq_delay_min', 'type': '__u64'}]`
- New: `[{'name': 'version', 'type': '__u16'}, {'name': 'ac_exitcode', 'type': '__u32'}, {'name': 'ac_flag', 'type': '__u8'}, {'name': 'ac_nice', 'type': '__u8'}, {'name': 'cpu_count', 'type': '__u64'}, {'name': 'cpu_delay_total', 'type': '__u64'}, {'name': 'blkio_count', 'type': '__u64'}, {'name': 'blkio_delay_total', 'type': '__u64'}, {'name': 'swapin_count', 'type': '__u64'}, {'name': 'swapin_delay_total', 'type': '__u64'}, {'name': 'cpu_run_real_total', 'type': '__u64'}, {'name': 'cpu_run_virtual_total', 'type': '__u64'}, {'name': 'ac_comm', 'type': '[ffi::c_char; 32usize]'}, {'name': 'ac_sched', 'type': '__u8'}, {'name': 'ac_pad', 'type': '[__u8; 3usize]'}, {'name': '__bindgen_padding_0', 'type': 'u32'}, {'name': 'ac_uid', 'type': '__u32'}, {'name': 'ac_gid', 'type': '__u32'}, {'name': 'ac_pid', 'type': '__u32'}, {'name': 'ac_ppid', 'type': '__u32'}, {'name': 'ac_btime', 'type': '__u32'}, {'name': 'ac_etime', 'type': '__u64'}, {'name': 'ac_utime', 'type': '__u64'}, {'name': 'ac_stime', 'type': '__u64'}, {'name': 'ac_minflt', 'type': '__u64'}, {'name': 'ac_majflt', 'type': '__u64'}, {'name': 'coremem', 'type': '__u64'}, {'name': 'virtmem', 'type': '__u64'}, {'name': 'hiwater_rss', 'type': '__u64'}, {'name': 'hiwater_vm', 'type': '__u64'}, {'name': 'read_char', 'type': '__u64'}, {'name': 'write_char', 'type': '__u64'}, {'name': 'read_syscalls', 'type': '__u64'}, {'name': 'write_syscalls', 'type': '__u64'}, {'name': 'read_bytes', 'type': '__u64'}, {'name': 'write_bytes', 'type': '__u64'}, {'name': 'cancelled_write_bytes', 'type': '__u64'}, {'name': 'nvcsw', 'type': '__u64'}, {'name': 'nivcsw', 'type': '__u64'}, {'name': 'ac_utimescaled', 'type': '__u64'}, {'name': 'ac_stimescaled', 'type': '__u64'}, {'name': 'cpu_scaled_run_real_total', 'type': '__u64'}, {'name': 'freepages_count', 'type': '__u64'}, {'name': 'freepages_delay_total', 'type': '__u64'}, {'name': 'thrashing_count', 'type': '__u64'}, {'name': 'thrashing_delay_total', 'type': '__u64'}, {'name': 'ac_btime64', 'type': '__u64'}, {'name': 'compact_count', 'type': '__u64'}, {'name': 'compact_delay_total', 'type': '__u64'}, {'name': 'ac_tgid', 'type': '__u32'}, {'name': 'ac_tgetime', 'type': '__u64'}, {'name': 'ac_exe_dev', 'type': '__u64'}, {'name': 'ac_exe_inode', 'type': '__u64'}, {'name': 'wpcopy_count', 'type': '__u64'}, {'name': 'wpcopy_delay_total', 'type': '__u64'}, {'name': 'irq_count', 'type': '__u64'}, {'name': 'irq_delay_total', 'type': '__u64'}, {'name': 'cpu_delay_max', 'type': '__u64'}, {'name': 'cpu_delay_min', 'type': '__u64'}, {'name': 'blkio_delay_max', 'type': '__u64'}, {'name': 'blkio_delay_min', 'type': '__u64'}, {'name': 'swapin_delay_max', 'type': '__u64'}, {'name': 'swapin_delay_min', 'type': '__u64'}, {'name': 'freepages_delay_max', 'type': '__u64'}, {'name': 'freepages_delay_min', 'type': '__u64'}, {'name': 'thrashing_delay_max', 'type': '__u64'}, {'name': 'thrashing_delay_min', 'type': '__u64'}, {'name': 'compact_delay_max', 'type': '__u64'}, {'name': 'compact_delay_min', 'type': '__u64'}, {'name': 'wpcopy_delay_max', 'type': '__u64'}, {'name': 'wpcopy_delay_min', 'type': '__u64'}, {'name': 'irq_delay_max', 'type': '__u64'}, {'name': 'irq_delay_min', 'type': '__u64'}, {'name': 'cpu_delay_max_ts', 'type': '__kernel_timespec'}, {'name': 'blkio_delay_max_ts', 'type': '__kernel_timespec'}, {'name': 'swapin_delay_max_ts', 'type': '__kernel_timespec'}, {'name': 'freepages_delay_max_ts', 'type': '__kernel_timespec'}, {'name': 'thrashing_delay_max_ts', 'type': '__kernel_timespec'}, {'name': 'compact_delay_max_ts', 'type': '__kernel_timespec'}, {'name': 'wpcopy_delay_max_ts', 'type': '__kernel_timespec'}, {'name': 'irq_delay_max_ts', 'type': '__kernel_timespec'}]`

### Rust Evidence

- Graph edges: `19`

## W-000614 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: rust_helper___spin_lock_init
- Explanation: rust_helper___spin_lock_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['spinlock_t *lock', 'const char *name', 'struct lock_class_key *key'], 'return_type': 'void'}`
- New: `{'params': ['spinlock_t *lock', 'const char *name', 'struct lock_class_key *key'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `3`

## W-000373 FieldDrift

- Risk: High
- Score: 12.0
- Symbol: kernfs_node
- Explanation: kernfs_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'count', 'type': 'atomic_t'}, {'name': 'active', 'type': 'atomic_t'}, {'name': '__parent', 'type': '*mut kernfs_node'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'rb', 'type': 'rb_node'}, {'name': 'ns', 'type': '*const ffi::c_void'}, {'name': 'hash', 'type': 'ffi::c_uint'}, {'name': 'flags', 'type': 'ffi::c_ushort'}, {'name': 'mode', 'type': 'umode_t'}, {'name': '__bindgen_anon_1', 'type': 'kernfs_node__bindgen_ty_1'}, {'name': 'id', 'type': 'u64_'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'iattr', 'type': '*mut kernfs_iattrs'}, {'name': 'rcu', 'type': 'callback_head'}]`
- New: `[{'name': 'count', 'type': 'atomic_t'}, {'name': 'active', 'type': 'atomic_t'}, {'name': '__parent', 'type': '*mut kernfs_node'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'rb', 'type': 'rb_node'}, {'name': 'ns', 'type': '*const ns_common'}, {'name': 'hash', 'type': 'ffi::c_uint'}, {'name': 'flags', 'type': 'ffi::c_ushort'}, {'name': 'mode', 'type': 'umode_t'}, {'name': '__bindgen_anon_1', 'type': 'kernfs_node__bindgen_ty_1'}, {'name': 'id', 'type': 'u64_'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'iattr', 'type': '*mut kernfs_iattrs'}, {'name': 'rcu', 'type': 'callback_head'}]`

### Rust Evidence

- Graph edges: `17`

## W-000730 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: rust_helper_refcount_dec
- Explanation: rust_helper_refcount_dec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['refcount_t *r'], 'return_type': 'void'}`
- New: `{'params': ['refcount_t *r'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `2`

## W-000093 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: dma_set_max_seg_size
- Explanation: dma_set_max_seg_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000316 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: soc_device_unregister
- Explanation: soc_device_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000604 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: rust_helper_ERR_PTR
- Explanation: rust_helper_ERR_PTR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['long err'], 'return_type': '__force void *'}`
- New: `{'params': ['long err'], 'return_type': '__rust_helper __force void *'}`

### Rust Evidence

- Graph edges: `1`

## W-000605 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: rust_helper_IS_ERR
- Explanation: rust_helper_IS_ERR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['__force const void *ptr'], 'return_type': 'bool'}`
- New: `{'params': ['__force const void *ptr'], 'return_type': '__rust_helper bool'}`

### Rust Evidence

- Graph edges: `1`

## W-000606 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: rust_helper_PTR_ERR
- Explanation: rust_helper_PTR_ERR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['__force const void *ptr'], 'return_type': 'long'}`
- New: `{'params': ['__force const void *ptr'], 'return_type': '__rust_helper long'}`

### Rust Evidence

- Graph edges: `1`

## W-000655 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: rust_helper_drm_gem_object_get
- Explanation: rust_helper_drm_gem_object_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_gem_object *obj'], 'return_type': 'void'}`
- New: `{'params': ['struct drm_gem_object *obj'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `1`

## W-000656 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: rust_helper_drm_gem_object_put
- Explanation: rust_helper_drm_gem_object_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_gem_object *obj'], 'return_type': 'void'}`
- New: `{'params': ['struct drm_gem_object *obj'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `1`

## W-000662 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: rust_helper_fwnode_handle_put
- Explanation: rust_helper_fwnode_handle_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct fwnode_handle *fwnode'], 'return_type': 'void'}`
- New: `{'params': ['struct fwnode_handle *fwnode'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `1`

## W-000699 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: rust_helper_mutex_destroy
- Explanation: rust_helper_mutex_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mutex *lock'], 'return_type': 'void'}`
- New: `{'params': ['struct mutex *lock'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `1`

## W-000700 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: rust_helper_mutex_lock
- Explanation: rust_helper_mutex_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mutex *lock'], 'return_type': 'void'}`
- New: `{'params': ['struct mutex *lock'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `1`

## W-000720 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: rust_helper_rcu_read_lock
- Explanation: rust_helper_rcu_read_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'void'}`
- New: `{'params': [], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `1`

## W-000731 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: rust_helper_refcount_dec_and_test
- Explanation: rust_helper_refcount_dec_and_test changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['refcount_t *r'], 'return_type': 'bool'}`
- New: `{'params': ['refcount_t *r'], 'return_type': '__rust_helper bool'}`

### Rust Evidence

- Graph edges: `1`

## W-000732 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: rust_helper_refcount_inc
- Explanation: rust_helper_refcount_inc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['refcount_t *r'], 'return_type': 'void'}`
- New: `{'params': ['refcount_t *r'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `1`

## W-000736 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: rust_helper_regulator_get
- Explanation: rust_helper_regulator_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct device *dev', 'const char *id'], 'return_type': 'struct regulator *'}`
- New: `{'params': ['struct device *dev', 'const char *id'], 'return_type': '__rust_helper struct regulator *'}`

### Rust Evidence

- Graph edges: `1`

## W-000739 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: rust_helper_regulator_put
- Explanation: rust_helper_regulator_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct regulator *regulator'], 'return_type': 'void'}`
- New: `{'params': ['struct regulator *regulator'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `1`

## W-000764 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: rust_helper_spin_lock
- Explanation: rust_helper_spin_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['spinlock_t *lock'], 'return_type': 'void'}`
- New: `{'params': ['spinlock_t *lock'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `1`

## W-000227 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: kswapd_clear_hopeless
- Explanation: kswapd_clear_hopeless changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000314 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: soc_device_register
- Explanation: soc_device_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000399 FieldDrift

- Risk: High
- Score: 11.6
- Symbol: task_struct
- Explanation: task_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'ffi::c_uint'}, {'name': 'saved_state', 'type': 'ffi::c_uint'}, {'name': 'stack', 'type': '*mut ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'ptrace', 'type': 'ffi::c_uint'}, {'name': 'on_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_cpu', 'type': 'ffi::c_int'}, {'name': 'on_rq', 'type': 'ffi::c_int'}, {'name': 'prio', 'type': 'ffi::c_int'}, {'name': 'static_prio', 'type': 'ffi::c_int'}, {'name': 'normal_prio', 'type': 'ffi::c_int'}, {'name': 'rt_priority', 'type': 'ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'dl_server', 'type': '*mut sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': '__bindgen_padding_1', 'type': 'u64'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'ffi::c_uint'}, {'name': 'policy', 'type': 'ffi::c_uint'}, {'name': 'max_allowed_capacity', 'type': 'ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut ffi::c_void'}, {'name': 'migration_disabled', 'type': 'ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'rcu_tasks_exit_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_exit_list', 'type': 'list_head'}, {'name': 'trc_reader_nesting', 'type': 'ffi::c_int'}, {'name': 'trc_ipi_to_cpu', 'type': 'ffi::c_int'}, {'name': 'trc_reader_special', 'type': 'rcu_special'}, {'name': 'trc_holdout_list', 'type': 'list_head'}, {'name': 'trc_blkd_node', 'type': 'list_head'}, {'name': 'trc_blkd_cpu', 'type': 'ffi::c_int'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'faults_disabled_mapping', 'type': '*mut address_space'}, {'name': 'exit_state', 'type': 'ffi::c_int'}, {'name': 'exit_code', 'type': 'ffi::c_int'}, {'name': 'exit_signal', 'type': 'ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'ffi::c_int'}, {'name': 'jobctl', 'type': 'ffi::c_ulong'}, {'name': 'personality', 'type': 'ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'worker_private', 'type': '*mut ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'blocked_on', 'type': '*mut mutex'}, {'name': 'journal_info', 'type': '*mut ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'ffi::c_uint'}, {'name': 'perf_recursion', 'type': '[u8_; 4usize]'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'perf_ctx_data', 'type': '*mut perf_ctx_data'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'ffi::c_short'}, {'name': 'il_weight', 'type': 'u8_'}, {'name': 'pref_node_fork', 'type': 'ffi::c_short'}, {'name': 'rseq', 'type': 'rseq_data'}, {'name': 'mm_cid', 'type': 'sched_mm_cid'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'bpf_net_context', 'type': '*mut bpf_net_context'}, {'name': 'mce_vaddr', 'type': '*mut ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': 'unwind_info', 'type': 'unwind_task_info'}, {'name': 'thread', 'type': 'thread_struct'}]`
- New: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'ffi::c_uint'}, {'name': 'saved_state', 'type': 'ffi::c_uint'}, {'name': 'stack', 'type': '*mut ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'ptrace', 'type': 'ffi::c_uint'}, {'name': 'on_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_cpu', 'type': 'ffi::c_int'}, {'name': 'on_rq', 'type': 'ffi::c_int'}, {'name': 'prio', 'type': 'ffi::c_int'}, {'name': 'static_prio', 'type': 'ffi::c_int'}, {'name': 'normal_prio', 'type': 'ffi::c_int'}, {'name': 'rt_priority', 'type': 'ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'dl_server', 'type': '*mut sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': '__bindgen_padding_1', 'type': 'u64'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'ffi::c_uint'}, {'name': 'policy', 'type': 'ffi::c_uint'}, {'name': 'max_allowed_capacity', 'type': 'ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut ffi::c_void'}, {'name': 'migration_disabled', 'type': 'ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'rcu_tasks_exit_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_exit_list', 'type': 'list_head'}, {'name': 'trc_reader_nesting', 'type': 'ffi::c_int'}, {'name': 'trc_reader_scp', 'type': '*mut srcu_ctr'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'exit_state', 'type': 'ffi::c_int'}, {'name': 'exit_code', 'type': 'ffi::c_int'}, {'name': 'exit_signal', 'type': 'ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'ffi::c_int'}, {'name': 'jobctl', 'type': 'ffi::c_ulong'}, {'name': 'personality', 'type': 'ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'worker_private', 'type': '*mut ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'io_uring_restrict', 'type': '*mut io_restriction'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'blocked_on', 'type': '*mut mutex'}, {'name': 'journal_info', 'type': '*mut ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'ffi::c_uint'}, {'name': 'perf_recursion', 'type': '[u8_; 4usize]'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'perf_ctx_data', 'type': '*mut perf_ctx_data'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'ffi::c_short'}, {'name': 'il_weight', 'type': 'u8_'}, {'name': 'pref_node_fork', 'type': 'ffi::c_short'}, {'name': 'rseq', 'type': 'rseq_data'}, {'name': 'mm_cid', 'type': 'sched_mm_cid'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'bpf_net_context', 'type': '*mut bpf_net_context'}, {'name': 'mce_vaddr', 'type': '*mut ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': 'unwind_info', 'type': 'unwind_task_info'}, {'name': 'thread', 'type': 'thread_struct'}]`

### Rust Evidence

- Graph edges: `15`

## W-000023 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: alloc_io_pgtable_ops
- Explanation: alloc_io_pgtable_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000037 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic_i16_try_cmpxchg
- Explanation: atomic_i16_try_cmpxchg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000041 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic_i16_xchg
- Explanation: atomic_i16_xchg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000049 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic_i8_try_cmpxchg
- Explanation: atomic_i8_try_cmpxchg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000053 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic_i8_xchg
- Explanation: atomic_i8_xchg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000089 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: dma_fence_signal
- Explanation: dma_fence_signal changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'fence', 'type': '*mut dma_fence'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'fence', 'type': '*mut dma_fence'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `4`

## W-000104 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: free_io_pgtable_ops
- Explanation: free_io_pgtable_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000580 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: dma_free_attrs
- Explanation: dma_free_attrs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct device *dev', 'size_t size', 'void *cpu_addr', 'dma_addr_t dma_handle', 'unsigned long attrs'], 'return_type': 'static void'}`
- New: `{'params': ['struct device *dev', 'size_t size', 'void *cpu_addr', 'dma_addr_t dma_handle', 'unsigned long attrs'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `4`

## W-000167 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: iommu_map
- Explanation: iommu_map changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000336 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: tg
- Explanation: tg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000033 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: atomic_i16_read
- Explanation: atomic_i16_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000035 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: atomic_i16_set
- Explanation: atomic_i16_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000045 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: atomic_i8_read
- Explanation: atomic_i8_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000047 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: atomic_i8_set
- Explanation: atomic_i8_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000077 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: cpufreq_cpu_policy
- Explanation: cpufreq_cpu_policy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000080 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: delayed_getname
- Explanation: delayed_getname changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000087 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: dma_fence_check_and_signal
- Explanation: dma_fence_check_and_signal changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000091 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: dma_fence_signal_timestamp
- Explanation: dma_fence_signal_timestamp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'fence', 'type': '*mut dma_fence'}, {'name': 'timestamp', 'type': 'ktime_t'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'fence', 'type': '*mut dma_fence'}, {'name': 'timestamp', 'type': 'ktime_t'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `2`

## W-000122 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: iommu_attach_device
- Explanation: iommu_attach_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000127 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: iommu_detach_device
- Explanation: iommu_detach_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000156 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: iommu_group_get
- Explanation: iommu_group_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000184 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: iommu_unmap
- Explanation: iommu_unmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000202 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: irq_work_queue
- Explanation: irq_work_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000597 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: refcount_dec_and_lock
- Explanation: refcount_dec_and_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['refcount_t *r', 'spinlock_t *lock) __cond_acquires(lock'], 'return_type': 'extern __must_check bool'}`
- New: `{'params': ['refcount_t *r', 'spinlock_t *lock) __cond_acquires(true, lock'], 'return_type': 'extern __must_check bool'}`

### Rust Evidence

- Graph edges: `2`

## W-000602 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: rq_end_io_ret
- Explanation: rq_end_io_ret changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['rq_end_io_fn)(struct request *, blk_status_t'], 'return_type': 'typedef enum'}`
- New: `{'params': ['rq_end_io_fn)(struct request *, blk_status_t, const struct io_comp_batch *'], 'return_type': 'typedef enum'}`

### Rust Evidence

- Graph edges: `2`

## W-000004 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __blkdev_issue_discard
- Explanation: __blkdev_issue_discard changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'bdev', 'type': '*mut block_device'}, {'name': 'sector', 'type': 'sector_t'}, {'name': 'nr_sects', 'type': 'sector_t'}, {'name': 'gfp_mask', 'type': 'gfp_t'}, {'name': 'biop', 'type': '*mut *mut bio'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'bdev', 'type': '*mut block_device'}, {'name': 'sector', 'type': 'sector_t'}, {'name': 'nr_sects', 'type': 'sector_t'}, {'name': 'gfp_mask', 'type': 'gfp_t'}, {'name': 'biop', 'type': '*mut *mut bio'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000005 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __clear_pages_unrolled
- Explanation: __clear_pages_unrolled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000006 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __device_set_driver_override
- Explanation: __device_set_driver_override changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000008 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __get_netmem
- Explanation: __get_netmem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000009 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __irq_domain_alloc_fwnode
- Explanation: __irq_domain_alloc_fwnode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'type_', 'type': 'ffi::c_uint'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'pa', 'type': '*mut phys_addr_t'}], 'return_type': '*mut fwnode_handle'}`
- New: `{'params': [{'name': 'type_', 'type': 'ffi::c_uint'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'pa', 'type': '*mut phys_addr_t'}, {'name': 'parent', 'type': '*mut fwnode_handle'}], 'return_type': '*mut fwnode_handle'}`

### Rust Evidence

- Graph edges: `1`

## W-000010 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kernfs_create_file
- Explanation: __kernfs_create_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'parent', 'type': '*mut kernfs_node'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'mode', 'type': 'umode_t'}, {'name': 'uid', 'type': 'kuid_t'}, {'name': 'gid', 'type': 'kgid_t'}, {'name': 'size', 'type': 'loff_t'}, {'name': 'ops', 'type': '*const kernfs_ops'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'ns', 'type': '*const ffi::c_void'}, {'name': 'key', 'type': '*mut lock_class_key'}], 'return_type': '*mut kernfs_node'}`
- New: `{'params': [{'name': 'parent', 'type': '*mut kernfs_node'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'mode', 'type': 'umode_t'}, {'name': 'uid', 'type': 'kuid_t'}, {'name': 'gid', 'type': 'kgid_t'}, {'name': 'size', 'type': 'loff_t'}, {'name': 'ops', 'type': '*const kernfs_ops'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'ns', 'type': '*const ns_common'}, {'name': 'key', 'type': '*mut lock_class_key'}], 'return_type': '*mut kernfs_node'}`

### Rust Evidence

- Graph edges: `1`

## W-000013 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __pte_offset_map
- Explanation: __pte_offset_map changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000015 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __put_netmem
- Explanation: __put_netmem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000017 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __trace_puts
- Explanation: __trace_puts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'ip', 'type': 'ffi::c_ulong'}, {'name': 'str_', 'type': '*const ffi::c_char'}, {'name': 'size', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'ip', 'type': 'ffi::c_ulong'}, {'name': 'str_', 'type': '*const ffi::c_char'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000018 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __vdso_getcpu
- Explanation: __vdso_getcpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'cpu', 'type': '*mut ffi::c_uint'}, {'name': 'node', 'type': '*mut ffi::c_uint'}, {'name': 'unused', 'type': '*mut getcpu_cache'}], 'return_type': 'ffi::c_long'}`
- New: `{'params': [{'name': 'cpu', 'type': '*mut ffi::c_uint'}, {'name': 'node', 'type': '*mut ffi::c_uint'}, {'name': 'unused', 'type': '*mut ffi::c_void'}], 'return_type': 'ffi::c_long'}`

### Rust Evidence

- Graph edges: `1`

## W-000019 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __vma_exclude_readers_for_detach
- Explanation: __vma_exclude_readers_for_detach changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000020 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __vma_start_write
- Explanation: __vma_start_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'mm_lock_seq', 'type': 'ffi::c_uint'}, {'name': 'state', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'state', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000021 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: _atomic_dec_and_lock
- Explanation: _atomic_dec_and_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000022 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: _atomic_dec_and_raw_lock
- Explanation: _atomic_dec_and_raw_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000024 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_irq_work_raise
- Explanation: arch_irq_work_raise changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000025 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_prctl_get_branch_landing_pad_state
- Explanation: arch_prctl_get_branch_landing_pad_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000026 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_prctl_lock_branch_landing_pad_state
- Explanation: arch_prctl_lock_branch_landing_pad_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000027 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_prctl_set_branch_landing_pad_state
- Explanation: arch_prctl_set_branch_landing_pad_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000028 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_uprobe_get_xol_area
- Explanation: arch_uprobe_get_xol_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000029 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_zone_limits_init
- Explanation: arch_zone_limits_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000030 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ari_enabled
- Explanation: ari_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(14usize, 1u8) as u32) } } #[inline] pub fn set_ari_enabled(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(13usize, 1u8) as u32) } } #[inline] pub fn set_ari_enabled(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000031 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_dec_and_lock
- Explanation: atomic_dec_and_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000032 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_dec_and_raw_lock
- Explanation: atomic_dec_and_raw_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000034 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_i16_read_acquire
- Explanation: atomic_i16_read_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000036 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_i16_set_release
- Explanation: atomic_i16_set_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000038 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_i16_try_cmpxchg_acquire
- Explanation: atomic_i16_try_cmpxchg_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000039 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_i16_try_cmpxchg_relaxed
- Explanation: atomic_i16_try_cmpxchg_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000040 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_i16_try_cmpxchg_release
- Explanation: atomic_i16_try_cmpxchg_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000042 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_i16_xchg_acquire
- Explanation: atomic_i16_xchg_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000043 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_i16_xchg_relaxed
- Explanation: atomic_i16_xchg_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000044 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_i16_xchg_release
- Explanation: atomic_i16_xchg_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000046 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_i8_read_acquire
- Explanation: atomic_i8_read_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000048 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_i8_set_release
- Explanation: atomic_i8_set_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000050 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_i8_try_cmpxchg_acquire
- Explanation: atomic_i8_try_cmpxchg_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000051 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_i8_try_cmpxchg_relaxed
- Explanation: atomic_i8_try_cmpxchg_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000052 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_i8_try_cmpxchg_release
- Explanation: atomic_i8_try_cmpxchg_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000054 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_i8_xchg_acquire
- Explanation: atomic_i8_xchg_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000055 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_i8_xchg_relaxed
- Explanation: atomic_i8_xchg_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000056 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_i8_xchg_release
- Explanation: atomic_i8_xchg_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000057 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ats_enabled
- Explanation: ats_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(15usize, 1u8) as u32) } } #[inline] pub fn set_ats_enabled(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(14usize, 1u8) as u32) } } #[inline] pub fn set_ats_enabled(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000058 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: attach_deferred
- Explanation: attach_deferred changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000060 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_iov_iter_bounce
- Explanation: bio_iov_iter_bounce changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000061 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_iov_iter_unbounce
- Explanation: bio_iov_iter_unbounce changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000062 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_reuse
- Explanation: bio_reuse changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000063 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: block_cfg_access
- Explanation: block_cfg_access changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(8usize, 1u8) as u32) } } #[inline] pub fn set_block_cfg_access(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(7usize, 1u8) as u32) } } #[inline] pub fn set_block_cfg_access(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000064 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_arena_alloc_pages_non_sleepable
- Explanation: bpf_arena_alloc_pages_non_sleepable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000065 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_arena_free_pages_non_sleepable
- Explanation: bpf_arena_free_pages_non_sleepable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000066 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_dynptr_slice_rdwr
- Explanation: bpf_dynptr_slice_rdwr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'p', 'type': '*const bpf_dynptr'}, {'name': 'offset', 'type': 'u64_'}, {'name': 'buffer__opt', 'type': '*mut ffi::c_void'}, {'name': 'buffer__szk', 'type': 'u64_'}], 'return_type': '*mut ffi::c_void'}`
- New: `{'params': [{'name': 'p', 'type': '*const bpf_dynptr'}, {'name': 'offset', 'type': 'u64_'}, {'name': 'buffer__nullable', 'type': '*mut ffi::c_void'}, {'name': 'buffer__szk', 'type': 'u64_'}], 'return_type': '*mut ffi::c_void'}`

### Rust Evidence

- Graph edges: `1`

## W-000067 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: broken_parity_status
- Explanation: broken_parity_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(9usize, 1u8) as u32) } } #[inline] pub fn set_broken_parity_status(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(8usize, 1u8) as u32) } } #[inline] pub fn set_broken_parity_status(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000068 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_named_start_id
- Explanation: btf_named_start_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000070 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: call_session_cookie
- Explanation: call_session_cookie changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000071 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_create_file_ns
- Explanation: class_create_file_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'class', 'type': '*const class'}, {'name': 'attr', 'type': '*const class_attribute'}, {'name': 'ns', 'type': '*const ffi::c_void'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'class', 'type': '*const class'}, {'name': 'attr', 'type': '*const class_attribute'}, {'name': 'ns', 'type': '*const ns_common'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000072 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_remove_file_ns
- Explanation: class_remove_file_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'class', 'type': '*const class'}, {'name': 'attr', 'type': '*const class_attribute'}, {'name': 'ns', 'type': '*const ffi::c_void'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'class', 'type': '*const class'}, {'name': 'attr', 'type': '*const class_attribute'}, {'name': 'ns', 'type': '*const ns_common'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000076 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: complete_getname
- Explanation: complete_getname changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000081 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: delayed_getname_uflags
- Explanation: delayed_getname_uflags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000082 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dentry_create
- Explanation: dentry_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'path', 'type': '*const path'}, {'name': 'flags', 'type': 'ffi::c_int'}, {'name': 'mode', 'type': 'umode_t'}, {'name': 'cred', 'type': '*const cred'}], 'return_type': '*mut file'}`
- New: `{'params': [{'name': 'path', 'type': '*mut path'}, {'name': 'flags', 'type': 'ffi::c_int'}, {'name': 'mode', 'type': 'umode_t'}, {'name': 'cred', 'type': '*const cred'}], 'return_type': '*mut file'}`

### Rust Evidence

- Graph edges: `1`

## W-000083 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_iommu_priv_set
- Explanation: dev_iommu_priv_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000084 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_iommu_capable
- Explanation: device_iommu_capable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000086 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dismiss_delayed_filename
- Explanation: dismiss_delayed_filename changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000088 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_fence_check_and_signal_locked
- Explanation: dma_fence_check_and_signal_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000090 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_fence_signal_locked
- Explanation: dma_fence_signal_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'fence', 'type': '*mut dma_fence'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'fence', 'type': '*mut dma_fence'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000092 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_fence_signal_timestamp_locked
- Explanation: dma_fence_signal_timestamp_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'fence', 'type': '*mut dma_fence'}, {'name': 'timestamp', 'type': 'ktime_t'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'fence', 'type': '*mut dma_fence'}, {'name': 'timestamp', 'type': 'ktime_t'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000094 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_get_unmapped_area
- Explanation: drm_gem_get_unmapped_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000098 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: eth_header_parse
- Explanation: eth_header_parse changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'skb', 'type': '*const sk_buff'}, {'name': 'haddr', 'type': '*mut ffi::c_uchar'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'skb', 'type': '*const sk_buff'}, {'name': 'dev', 'type': '*const net_device'}, {'name': 'haddr', 'type': '*mut ffi::c_uchar'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000099 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_str_to_medium
- Explanation: ethtool_str_to_medium changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000100 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fm_enabled
- Explanation: fm_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(19usize, 1u8) as u32) } } #[inline] pub fn set_fm_enabled(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(18usize, 1u8) as u32) } } #[inline] pub fn set_fm_enabled(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000106 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fsl_mc_device_group
- Explanation: fsl_mc_device_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000107 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_device_group
- Explanation: generic_device_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000108 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_handle_demux_domain_irq
- Explanation: generic_handle_demux_domain_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000109 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_single_device_group
- Explanation: generic_single_device_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000110 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_update_time
- Explanation: generic_update_time changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut inode'}, {'name': 'arg2', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'inode', 'type': '*mut inode'}, {'name': 'type_', 'type': 'fs_update_time'}, {'name': 'flags', 'type': 'ffi::c_uint'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000111 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_locked_pte
- Explanation: get_locked_pte changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000118 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_update_time
- Explanation: inode_update_time changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'inode', 'type': '*mut inode'}, {'name': 'flags', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'inode', 'type': '*mut inode'}, {'name': 'type_', 'type': 'fs_update_time'}, {'name': 'flags', 'type': 'ffi::c_uint'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000120 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_alloc_global_pasid
- Explanation: iommu_alloc_global_pasid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000121 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_alloc_resv_region
- Explanation: iommu_alloc_resv_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000123 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_attach_device_pasid
- Explanation: iommu_attach_device_pasid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000124 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_attach_group
- Explanation: iommu_attach_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000125 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_default_passthrough
- Explanation: iommu_default_passthrough changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000126 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_deferred_attach
- Explanation: iommu_deferred_attach changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000128 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_detach_device_pasid
- Explanation: iommu_detach_device_pasid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000129 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_detach_group
- Explanation: iommu_detach_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000130 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_device_claim_dma_owner
- Explanation: iommu_device_claim_dma_owner changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000131 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_device_link
- Explanation: iommu_device_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000132 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_device_register
- Explanation: iommu_device_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000133 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_device_release_dma_owner
- Explanation: iommu_device_release_dma_owner changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000134 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_device_sysfs_add
- Explanation: iommu_device_sysfs_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000135 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_device_sysfs_remove
- Explanation: iommu_device_sysfs_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000136 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_device_unlink
- Explanation: iommu_device_unlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000137 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_device_unregister
- Explanation: iommu_device_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000138 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_device_unuse_default_domain
- Explanation: iommu_device_unuse_default_domain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000139 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_device_use_default_domain
- Explanation: iommu_device_use_default_domain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000140 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_domain_free
- Explanation: iommu_domain_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000141 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_driver_get_domain_for_dev
- Explanation: iommu_driver_get_domain_for_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000142 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_free_global_pasid
- Explanation: iommu_free_global_pasid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000143 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_fwspec_add_ids
- Explanation: iommu_fwspec_add_ids changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000144 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_fwspec_init
- Explanation: iommu_fwspec_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000145 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_get_dma_domain
- Explanation: iommu_get_dma_domain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000146 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_get_domain_for_dev
- Explanation: iommu_get_domain_for_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000147 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_get_group_resv_regions
- Explanation: iommu_get_group_resv_regions changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000148 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_get_msi_cookie
- Explanation: iommu_get_msi_cookie changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000149 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_get_resv_regions
- Explanation: iommu_get_resv_regions changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000150 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_group_add_device
- Explanation: iommu_group_add_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000151 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_group_alloc
- Explanation: iommu_group_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000152 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_group_claim_dma_owner
- Explanation: iommu_group_claim_dma_owner changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000153 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_group_default_domain
- Explanation: iommu_group_default_domain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000154 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_group_dma_owner_claimed
- Explanation: iommu_group_dma_owner_claimed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000155 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_group_for_each_dev
- Explanation: iommu_group_for_each_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000157 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_group_get_iommudata
- Explanation: iommu_group_get_iommudata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000158 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_group_has_isolated_msi
- Explanation: iommu_group_has_isolated_msi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000159 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_group_id
- Explanation: iommu_group_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000160 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_group_put
- Explanation: iommu_group_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000161 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_group_ref_get
- Explanation: iommu_group_ref_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000162 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_group_release_dma_owner
- Explanation: iommu_group_release_dma_owner changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000163 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_group_remove_device
- Explanation: iommu_group_remove_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000164 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_group_set_iommudata
- Explanation: iommu_group_set_iommudata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000165 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_group_set_name
- Explanation: iommu_group_set_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000166 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_iova_to_phys
- Explanation: iommu_iova_to_phys changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000168 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_map_nosync
- Explanation: iommu_map_nosync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000169 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_map_sg
- Explanation: iommu_map_sg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000170 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_paging_domain_alloc_flags
- Explanation: iommu_paging_domain_alloc_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000171 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_probe_device
- Explanation: iommu_probe_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000172 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_put_resv_regions
- Explanation: iommu_put_resv_regions changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000173 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_report_device_fault
- Explanation: iommu_report_device_fault changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000174 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_set_default_passthrough
- Explanation: iommu_set_default_passthrough changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000175 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_set_default_translated
- Explanation: iommu_set_default_translated changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000176 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_set_dma_strict
- Explanation: iommu_set_dma_strict changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000177 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_set_fault_handler
- Explanation: iommu_set_fault_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000178 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_set_pgtable_quirks
- Explanation: iommu_set_pgtable_quirks changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000179 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_sva_bind_device
- Explanation: iommu_sva_bind_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000180 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_sva_get_pasid
- Explanation: iommu_sva_get_pasid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000181 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_sva_invalidate_kva_range
- Explanation: iommu_sva_invalidate_kva_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000182 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_sva_unbind_device
- Explanation: iommu_sva_unbind_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000183 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_sync_map
- Explanation: iommu_sync_map changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000185 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iommu_unmap_fast
- Explanation: iommu_unmap_fast changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000186 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iopf_free_group
- Explanation: iopf_free_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000187 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iopf_group_response
- Explanation: iopf_group_response changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000188 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iopf_queue_add_device
- Explanation: iopf_queue_add_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000189 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iopf_queue_alloc
- Explanation: iopf_queue_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000190 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iopf_queue_discard_partial
- Explanation: iopf_queue_discard_partial changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000191 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iopf_queue_flush_dev
- Explanation: iopf_queue_flush_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000192 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iopf_queue_free
- Explanation: iopf_queue_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000193 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iopf_queue_remove_device
- Explanation: iopf_queue_remove_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000194 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iov_iter_extract_bvecs
- Explanation: iov_iter_extract_bvecs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000195 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ips
- Explanation: ips changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000196 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irgn
- Explanation: irgn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000197 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_pm_put
- Explanation: irq_chip_pm_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'data', 'type': '*mut irq_data'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'data', 'type': '*mut irq_data'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000198 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_pre_redirect_parent
- Explanation: irq_chip_pre_redirect_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000199 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_redirect_set_affinity
- Explanation: irq_chip_redirect_set_affinity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000200 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_reroute_variant
- Explanation: irq_reroute_variant changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(10usize, 2u8) as u32) } } #[inline] pub fn set_irq_reroute_variant(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(9usize, 2u8) as u32) } } #[inline] pub fn set_irq_reroute_variant(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000201 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_work_needs_cpu
- Explanation: irq_work_needs_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000203 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_work_queue_on
- Explanation: irq_work_queue_on changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000204 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_work_run
- Explanation: irq_work_run changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000205 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_work_single
- Explanation: irq_work_single changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000206 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_work_sync
- Explanation: irq_work_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000207 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_work_tick
- Explanation: irq_work_tick changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000208 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_cxl
- Explanation: is_cxl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000209 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_hotplug_bridge
- Explanation: is_hotplug_bridge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(26usize, 1u8) as u32) } } #[inline] pub fn set_is_hotplug_bridge(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(25usize, 1u8) as u32) } } #[inline] pub fn set_is_hotplug_bridge(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000210 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_managed
- Explanation: is_managed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(20usize, 1u8) as u32) } } #[inline] pub fn set_is_managed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(19usize, 1u8) as u32) } } #[inline] pub fn set_is_managed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000211 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_msi_managed
- Explanation: is_msi_managed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(21usize, 1u8) as u32) } } #[inline] pub fn set_is_msi_managed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(20usize, 1u8) as u32) } } #[inline] pub fn set_is_msi_managed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000212 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_pciehp
- Explanation: is_pciehp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(27usize, 1u8) as u32) } } #[inline] pub fn set_is_pciehp(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(26usize, 1u8) as u32) } } #[inline] pub fn set_is_pciehp(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000213 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_physfn
- Explanation: is_physfn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(24usize, 1u8) as u32) } } #[inline] pub fn set_is_physfn(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(23usize, 1u8) as u32) } } #[inline] pub fn set_is_physfn(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000214 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_thunderbolt
- Explanation: is_thunderbolt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(29usize, 1u8) as u32) } } #[inline] pub fn set_is_thunderbolt(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(28usize, 1u8) as u32) } } #[inline] pub fn set_is_thunderbolt(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000215 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_virtfn
- Explanation: is_virtfn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(25usize, 1u8) as u32) } } #[inline] pub fn set_is_virtfn(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(24usize, 1u8) as u32) } } #[inline] pub fn set_is_virtfn(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000218 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_create_dir_ns
- Explanation: kernfs_create_dir_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'parent', 'type': '*mut kernfs_node'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'mode', 'type': 'umode_t'}, {'name': 'uid', 'type': 'kuid_t'}, {'name': 'gid', 'type': 'kgid_t'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'ns', 'type': '*const ffi::c_void'}], 'return_type': '*mut kernfs_node'}`
- New: `{'params': [{'name': 'parent', 'type': '*mut kernfs_node'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'mode', 'type': 'umode_t'}, {'name': 'uid', 'type': 'kuid_t'}, {'name': 'gid', 'type': 'kgid_t'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'ns', 'type': '*const ns_common'}], 'return_type': '*mut kernfs_node'}`

### Rust Evidence

- Graph edges: `1`

## W-000219 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_find_and_get_ns
- Explanation: kernfs_find_and_get_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'parent', 'type': '*mut kernfs_node'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'ns', 'type': '*const ffi::c_void'}], 'return_type': '*mut kernfs_node'}`
- New: `{'params': [{'name': 'parent', 'type': '*mut kernfs_node'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'ns', 'type': '*const ns_common'}], 'return_type': '*mut kernfs_node'}`

### Rust Evidence

- Graph edges: `1`

## W-000220 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_remove_by_name_ns
- Explanation: kernfs_remove_by_name_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'parent', 'type': '*mut kernfs_node'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'ns', 'type': '*const ffi::c_void'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'parent', 'type': '*mut kernfs_node'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'ns', 'type': '*const ns_common'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000221 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_rename_ns
- Explanation: kernfs_rename_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'kn', 'type': '*mut kernfs_node'}, {'name': 'new_parent', 'type': '*mut kernfs_node'}, {'name': 'new_name', 'type': '*const ffi::c_char'}, {'name': 'new_ns', 'type': '*const ffi::c_void'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'kn', 'type': '*mut kernfs_node'}, {'name': 'new_parent', 'type': '*mut kernfs_node'}, {'name': 'new_name', 'type': '*const ffi::c_char'}, {'name': 'new_ns', 'type': '*const ns_common'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000222 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_super_ns
- Explanation: kernfs_super_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'sb', 'type': '*mut super_block'}], 'return_type': '*const ffi::c_void'}`
- New: `{'params': [{'name': 'sb', 'type': '*mut super_block'}], 'return_type': '*const ns_common'}`

### Rust Evidence

- Graph edges: `1`

## W-000223 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernfs_walk_and_get_ns
- Explanation: kernfs_walk_and_get_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'parent', 'type': '*mut kernfs_node'}, {'name': 'path', 'type': '*const ffi::c_char'}, {'name': 'ns', 'type': '*const ffi::c_void'}], 'return_type': '*mut kernfs_node'}`
- New: `{'params': [{'name': 'parent', 'type': '*mut kernfs_node'}, {'name': 'path', 'type': '*const ffi::c_char'}, {'name': 'ns', 'type': '*const ns_common'}], 'return_type': '*mut kernfs_node'}`

### Rust Evidence

- Graph edges: `1`

## W-000224 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobj_ns_drop
- Explanation: kobj_ns_drop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'type_', 'type': 'kobj_ns_type'}, {'name': 'ns', 'type': '*mut ffi::c_void'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'type_', 'type': 'kobj_ns_type'}, {'name': 'ns', 'type': '*mut ns_common'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000225 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobj_ns_grab_current
- Explanation: kobj_ns_grab_current changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'type_', 'type': 'kobj_ns_type'}], 'return_type': '*mut ffi::c_void'}`
- New: `{'params': [{'name': 'type_', 'type': 'kobj_ns_type'}], 'return_type': '*mut ns_common'}`

### Rust Evidence

- Graph edges: `1`

## W-000226 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kobject_namespace
- Explanation: kobject_namespace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'kobj', 'type': '*const kobject'}], 'return_type': '*const ffi::c_void'}`
- New: `{'params': [{'name': 'kobj', 'type': '*const kobject'}], 'return_type': '*const ns_common'}`

### Rust Evidence

- Graph edges: `1`

## W-000228 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kswapd_test_hopeless
- Explanation: kswapd_test_hopeless changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000229 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kswapd_try_clear_hopeless
- Explanation: kswapd_try_clear_hopeless changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000230 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthread_do_exit
- Explanation: kthread_do_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000232 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kthreads_update_housekeeping
- Explanation: kthreads_update_housekeeping changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000236 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lock_task_sighand
- Explanation: lock_task_sighand changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000237 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lockdep_is_cpus_write_held
- Explanation: lockdep_is_cpus_write_held changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000239 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: map_check_no_btf
- Explanation: map_check_no_btf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'map', 'type': '*const bpf_map'}, {'name': 'btf', 'type': '*const btf'}, {'name': 'key_type', 'type': '*const btf_type'}, {'name': 'value_type', 'type': '*const btf_type'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'map', 'type': '*mut bpf_map'}, {'name': 'btf', 'type': '*const btf'}, {'name': 'key_type', 'type': '*const btf_type'}, {'name': 'value_type', 'type': '*const btf_type'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000241 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: may_create_dentry
- Explanation: may_create_dentry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000242 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: may_delete_dentry
- Explanation: may_delete_dentry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000243 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: may_see_all_namespaces
- Explanation: may_see_all_namespaces changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000244 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: may_skip_resume
- Explanation: may_skip_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_2.get(6usize, 1u8) as u8) } } #[inline] pub fn set_may_skip_resume(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_2.get(5usize, 1u8) as u8) } } #[inline] pub fn set_may_skip_resume(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000245 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mm_core_init_early
- Explanation: mm_core_init_early changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000246 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mm_pasid_drop
- Explanation: mm_pasid_drop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000247 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: msi_enabled
- Explanation: msi_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(12usize, 1u8) as u32) } } #[inline] pub fn set_msi_enabled(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(11usize, 1u8) as u32) } } #[inline] pub fn set_msi_enabled(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000248 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: msix_enabled
- Explanation: msix_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(13usize, 1u8) as u32) } } #[inline] pub fn set_msix_enabled(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(12usize, 1u8) as u32) } } #[inline] pub fn set_msix_enabled(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000249 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: must_resume
- Explanation: must_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_2.get(5usize, 1u8) as u8) } } #[inline] pub fn set_must_resume(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_2.get(4usize, 1u8) as u8) } } #[inline] pub fn set_must_resume(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000250 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: needs_freset
- Explanation: needs_freset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(22usize, 1u8) as u32) } } #[inline] pub fn set_needs_freset(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(21usize, 1u8) as u32) } } #[inline] pub fn set_needs_freset(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000251 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_bitfield_2
- Explanation: new_bitfield_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'do_remote_wakeup', 'type': 'ffi::c_uint'}, {'name': 'reset_resume', 'type': 'ffi::c_uint'}, {'name': 'port_is_suspended', 'type': 'ffi::c_uint'}, {'name': 'offload_at_suspend', 'type': 'ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`
- New: `{'params': [{'name': 'do_remote_wakeup', 'type': 'ffi::c_uint'}, {'name': 'reset_resume', 'type': 'ffi::c_uint'}, {'name': 'port_is_suspended', 'type': 'ffi::c_uint'}, {'name': 'offload_pm_locked', 'type': 'ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`

### Rust Evidence

- Graph edges: `1`

## W-000252 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_bitfield_4
- Explanation: new_bitfield_4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'transparent', 'type': 'ffi::c_uint'}, {'name': 'io_window', 'type': 'ffi::c_uint'}, {'name': 'pref_window', 'type': 'ffi::c_uint'}, {'name': 'pref_64_window', 'type': 'ffi::c_uint'}, {'name': 'multifunction', 'type': 'ffi::c_uint'}, {'name': 'is_busmaster', 'type': 'ffi::c_uint'}, {'name': 'no_msi', 'type': 'ffi::c_uint'}, {'name': 'no_64bit_msi', 'type': 'ffi::c_uint'}, {'name': 'block_cfg_access', 'type': 'ffi::c_uint'}, {'name': 'broken_parity_status', 'type': 'ffi::c_uint'}, {'name': 'irq_reroute_variant', 'type': 'ffi::c_uint'}, {'name': 'msi_enabled', 'type': 'ffi::c_uint'}, {'name': 'msix_enabled', 'type': 'ffi::c_uint'}, {'name': 'ari_enabled', 'type': 'ffi::c_uint'}, {'name': 'ats_enabled', 'type': 'ffi::c_uint'}, {'name': 'pasid_enabled', 'type': 'ffi::c_uint'}, {'name': 'pri_enabled', 'type': 'ffi::c_uint'}, {'name': 'tph_enabled', 'type': 'ffi::c_uint'}, {'name': 'fm_enabled', 'type': 'ffi::c_uint'}, {'name': 'is_managed', 'type': 'ffi::c_uint'}, {'name': 'is_msi_managed', 'type': 'ffi::c_uint'}, {'name': 'needs_freset', 'type': 'ffi::c_uint'}, {'name': 'state_saved', 'type': 'ffi::c_uint'}, {'name': 'is_physfn', 'type': 'ffi::c_uint'}, {'name': 'is_virtfn', 'type': 'ffi::c_uint'}, {'name': 'is_hotplug_bridge', 'type': 'ffi::c_uint'}, {'name': 'is_pciehp', 'type': 'ffi::c_uint'}, {'name': 'shpc_managed', 'type': 'ffi::c_uint'}, {'name': 'is_thunderbolt', 'type': 'ffi::c_uint'}, {'name': 'untrusted', 'type': 'ffi::c_uint'}, {'name': 'external_facing', 'type': 'ffi::c_uint'}, {'name': 'broken_intx_masking', 'type': 'ffi::c_uint'}, {'name': 'io_window_1k', 'type': 'ffi::c_uint'}, {'name': 'irq_managed', 'type': 'ffi::c_uint'}, {'name': 'non_compliant_bars', 'type': 'ffi::c_uint'}, {'name': 'is_probed', 'type': 'ffi::c_uint'}, {'name': 'link_active_reporting', 'type': 'ffi::c_uint'}, {'name': 'no_vf_scan', 'type': 'ffi::c_uint'}, {'name': 'no_command_memory', 'type': 'ffi::c_uint'}, {'name': 'rom_bar_overlap', 'type': 'ffi::c_uint'}, {'name': 'rom_attr_enabled', 'type': 'ffi::c_uint'}, {'name': 'non_mappable_bars', 'type': 'ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`
- New: `{'params': [{'name': 'transparent', 'type': 'ffi::c_uint'}, {'name': 'io_window', 'type': 'ffi::c_uint'}, {'name': 'pref_window', 'type': 'ffi::c_uint'}, {'name': 'pref_64_window', 'type': 'ffi::c_uint'}, {'name': 'multifunction', 'type': 'ffi::c_uint'}, {'name': 'is_busmaster', 'type': 'ffi::c_uint'}, {'name': 'no_msi', 'type': 'ffi::c_uint'}, {'name': 'block_cfg_access', 'type': 'ffi::c_uint'}, {'name': 'broken_parity_status', 'type': 'ffi::c_uint'}, {'name': 'irq_reroute_variant', 'type': 'ffi::c_uint'}, {'name': 'msi_enabled', 'type': 'ffi::c_uint'}, {'name': 'msix_enabled', 'type': 'ffi::c_uint'}, {'name': 'ari_enabled', 'type': 'ffi::c_uint'}, {'name': 'ats_enabled', 'type': 'ffi::c_uint'}, {'name': 'pasid_enabled', 'type': 'ffi::c_uint'}, {'name': 'pri_enabled', 'type': 'ffi::c_uint'}, {'name': 'tph_enabled', 'type': 'ffi::c_uint'}, {'name': 'fm_enabled', 'type': 'ffi::c_uint'}, {'name': 'is_managed', 'type': 'ffi::c_uint'}, {'name': 'is_msi_managed', 'type': 'ffi::c_uint'}, {'name': 'needs_freset', 'type': 'ffi::c_uint'}, {'name': 'state_saved', 'type': 'ffi::c_uint'}, {'name': 'is_physfn', 'type': 'ffi::c_uint'}, {'name': 'is_virtfn', 'type': 'ffi::c_uint'}, {'name': 'is_hotplug_bridge', 'type': 'ffi::c_uint'}, {'name': 'is_pciehp', 'type': 'ffi::c_uint'}, {'name': 'shpc_managed', 'type': 'ffi::c_uint'}, {'name': 'is_thunderbolt', 'type': 'ffi::c_uint'}, {'name': 'is_cxl', 'type': 'ffi::c_uint'}, {'name': 'untrusted', 'type': 'ffi::c_uint'}, {'name': 'external_facing', 'type': 'ffi::c_uint'}, {'name': 'broken_intx_masking', 'type': 'ffi::c_uint'}, {'name': 'io_window_1k', 'type': 'ffi::c_uint'}, {'name': 'irq_managed', 'type': 'ffi::c_uint'}, {'name': 'non_compliant_bars', 'type': 'ffi::c_uint'}, {'name': 'is_probed', 'type': 'ffi::c_uint'}, {'name': 'link_active_reporting', 'type': 'ffi::c_uint'}, {'name': 'no_vf_scan', 'type': 'ffi::c_uint'}, {'name': 'no_command_memory', 'type': 'ffi::c_uint'}, {'name': 'rom_bar_overlap', 'type': 'ffi::c_uint'}, {'name': 'rom_attr_enabled', 'type': 'ffi::c_uint'}, {'name': 'non_mappable_bars', 'type': 'ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`

### Rust Evidence

- Graph edges: `1`

## W-000254 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_bw_notif
- Explanation: no_bw_notif changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000255 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: num_phys_nodes
- Explanation: num_phys_nodes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000257 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: offload_pm_locked
- Explanation: offload_pm_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000258 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: orgn
- Explanation: orgn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000259 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: out_band_wakeup
- Explanation: out_band_wakeup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_2.get(7usize, 1u8) as u8) } } #[inline] pub fn set_out_band_wakeup(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_2.get(6usize, 1u8) as u8) } } #[inline] pub fn set_out_band_wakeup(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000260 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: panic_smp_redirect_cpu
- Explanation: panic_smp_redirect_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000262 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pasid_enabled
- Explanation: pasid_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(16usize, 1u8) as u32) } } #[inline] pub fn set_pasid_enabled(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(15usize, 1u8) as u32) } } #[inline] pub fn set_pasid_enabled(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000263 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_32bit_workaround
- Explanation: pci_32bit_workaround changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000264 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_dev_reset_iommu_done
- Explanation: pci_dev_reset_iommu_done changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000265 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_dev_reset_iommu_prepare
- Explanation: pci_dev_reset_iommu_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000266 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_device_group
- Explanation: pci_device_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000267 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_probe_flush_workqueue
- Explanation: pci_probe_flush_workqueue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000268 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_setup_cardbus
- Explanation: pci_setup_cardbus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000269 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_setup_cardbus_bridge
- Explanation: pci_setup_cardbus_bridge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000270 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_get_sfp_port
- Explanation: phy_get_sfp_port changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000280 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pri_enabled
- Explanation: pri_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(17usize, 1u8) as u32) } } #[inline] pub fn set_pri_enabled(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(16usize, 1u8) as u32) } } #[inline] pub fn set_pri_enabled(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000281 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_int_conv
- Explanation: proc_int_conv changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000282 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_int_k2u_conv_kop
- Explanation: proc_int_k2u_conv_kop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000283 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_int_u2k_conv_uop
- Explanation: proc_int_u2k_conv_uop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000284 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_uint_conv
- Explanation: proc_uint_conv changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000285 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_uint_k2u_conv
- Explanation: proc_uint_k2u_conv changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000286 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_uint_u2k_conv_uop
- Explanation: proc_uint_u2k_conv_uop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000288 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pte_offset_map_lock
- Explanation: pte_offset_map_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000291 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: putname_to_delayed
- Explanation: putname_to_delayed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000295 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rcu_tasks_trace_suppress_unused
- Explanation: rcu_tasks_trace_suppress_unused changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000298 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: region_intersects_soft_reserve
- Explanation: region_intersects_soft_reserve changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000299 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: report_iommu_fault
- Explanation: report_iommu_fault changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000300 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: request_percpu_irq_affinity
- Explanation: request_percpu_irq_affinity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000301 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: require_direct
- Explanation: require_direct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000306 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sg_nents_for_dma
- Explanation: sg_nents_for_dma changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000308 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: shadow_on_flush
- Explanation: shadow_on_flush changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000309 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: shpc_managed
- Explanation: shpc_managed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(28usize, 1u8) as u32) } } #[inline] pub fn set_shpc_managed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(27usize, 1u8) as u32) } } #[inline] pub fn set_shpc_managed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000312 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sleepable
- Explanation: sleepable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u16_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(14usize, 1u8) as u16) } } #[inline] pub fn set_sleepable(&mut self, val: u16_) { unsafe { let val: u16 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u16_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(15usize, 1u8) as u16) } } #[inline] pub fn set_sleepable(&mut self, val: u16_) { unsafe { let val: u16 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000313 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: smart_suspend
- Explanation: smart_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_2.get(4usize, 1u8) as u8) } } #[inline] pub fn set_smart_suspend(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_2.get(3usize, 1u8) as u8) } } #[inline] pub fn set_smart_suspend(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000315 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: soc_device_to_device
- Explanation: soc_device_to_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000317 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sparse_init
- Explanation: sparse_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000318 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: state_saved
- Explanation: state_saved changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(23usize, 1u8) as u32) } } #[inline] pub fn set_state_saved(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(22usize, 1u8) as u32) } } #[inline] pub fn set_state_saved(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000319 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: strict_midlayer
- Explanation: strict_midlayer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_2.get(8usize, 1u8) as u8) } } #[inline] pub fn set_strict_midlayer(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_2.get(7usize, 1u8) as u8) } } #[inline] pub fn set_strict_midlayer(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000320 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: swap_alloc_hibernation_slot
- Explanation: swap_alloc_hibernation_slot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000321 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: swap_dup_entry_direct
- Explanation: swap_dup_entry_direct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000323 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: swap_free_hibernation_slot
- Explanation: swap_free_hibernation_slot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000325 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: swap_put_entries_direct
- Explanation: swap_put_entries_direct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000330 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_create_dir_ns
- Explanation: sysfs_create_dir_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'kobj', 'type': '*mut kobject'}, {'name': 'ns', 'type': '*const ffi::c_void'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'kobj', 'type': '*mut kobject'}, {'name': 'ns', 'type': '*const ns_common'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000331 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_create_file_ns
- Explanation: sysfs_create_file_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'kobj', 'type': '*mut kobject'}, {'name': 'attr', 'type': '*const attribute'}, {'name': 'ns', 'type': '*const ffi::c_void'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'kobj', 'type': '*mut kobject'}, {'name': 'attr', 'type': '*const attribute'}, {'name': 'ns', 'type': '*const ns_common'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000332 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_move_dir_ns
- Explanation: sysfs_move_dir_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'kobj', 'type': '*mut kobject'}, {'name': 'new_parent_kobj', 'type': '*mut kobject'}, {'name': 'new_ns', 'type': '*const ffi::c_void'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'kobj', 'type': '*mut kobject'}, {'name': 'new_parent_kobj', 'type': '*mut kobject'}, {'name': 'new_ns', 'type': '*const ns_common'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000333 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_remove_file_ns
- Explanation: sysfs_remove_file_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'kobj', 'type': '*mut kobject'}, {'name': 'attr', 'type': '*const attribute'}, {'name': 'ns', 'type': '*const ffi::c_void'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'kobj', 'type': '*mut kobject'}, {'name': 'attr', 'type': '*const attribute'}, {'name': 'ns', 'type': '*const ns_common'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000334 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_rename_dir_ns
- Explanation: sysfs_rename_dir_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'kobj', 'type': '*mut kobject'}, {'name': 'new_name', 'type': '*const ffi::c_char'}, {'name': 'new_ns', 'type': '*const ffi::c_void'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'kobj', 'type': '*mut kobject'}, {'name': 'new_name', 'type': '*const ffi::c_char'}, {'name': 'new_ns', 'type': '*const ns_common'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000335 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_rename_link_ns
- Explanation: sysfs_rename_link_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'kobj', 'type': '*mut kobject'}, {'name': 'target', 'type': '*mut kobject'}, {'name': 'old_name', 'type': '*const ffi::c_char'}, {'name': 'new_name', 'type': '*const ffi::c_char'}, {'name': 'new_ns', 'type': '*const ffi::c_void'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'kobj', 'type': '*mut kobject'}, {'name': 'target', 'type': '*mut kobject'}, {'name': 'old_name', 'type': '*const ffi::c_char'}, {'name': 'new_name', 'type': '*const ffi::c_char'}, {'name': 'new_ns', 'type': '*const ns_common'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000337 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: tph_enabled
- Explanation: tph_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(18usize, 1u8) as u32) } } #[inline] pub fn set_tph_enabled(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(17usize, 1u8) as u32) } } #[inline] pub fn set_tph_enabled(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000338 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: tstamp_type_access
- Explanation: tstamp_type_access changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u16_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(13usize, 1u8) as u16) } } #[inline] pub fn set_tstamp_type_access(&mut self, val: u16_) { unsafe { let val: u16 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u16_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(14usize, 1u8) as u16) } } #[inline] pub fn set_tstamp_type_access(&mut self, val: u16_) { unsafe { let val: u16 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000339 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: tsz
- Explanation: tsz changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000341 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_bulk_msg_killable
- Explanation: usb_bulk_msg_killable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000342 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: user_pasid_table
- Explanation: user_pasid_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000344 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmstat_flush_workqueue
- Explanation: vmstat_flush_workqueue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000345 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: walk_soft_reserve_res
- Explanation: walk_soft_reserve_res changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000348 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: workqueue_unbound_housekeeping_update
- Explanation: workqueue_unbound_housekeeping_update changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000553 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __blkdev_issue_discard
- Explanation: __blkdev_issue_discard changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct block_device *bdev', 'sector_t sector', 'sector_t nr_sects', 'gfp_t gfp_mask', 'struct bio **biop'], 'return_type': 'int'}`
- New: `{'params': ['struct block_device *bdev', 'sector_t sector', 'sector_t nr_sects', 'gfp_t gfp_mask', 'struct bio **biop'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-000554 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __cond_resched_lock
- Explanation: __cond_resched_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['spinlock_t *lock'], 'return_type': 'extern int'}`
- New: `{'params': ['spinlock_t *lock) __must_hold(lock'], 'return_type': 'extern int'}`

### Rust Evidence

- Graph edges: `1`

## W-000555 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __cond_resched_rwlock_read
- Explanation: __cond_resched_rwlock_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['rwlock_t *lock'], 'return_type': 'extern int'}`
- New: `{'params': ['rwlock_t *lock) __must_hold_shared(lock'], 'return_type': 'extern int'}`

### Rust Evidence

- Graph edges: `1`

## W-000556 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __cond_resched_rwlock_write
- Explanation: __cond_resched_rwlock_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['rwlock_t *lock'], 'return_type': 'extern int'}`
- New: `{'params': ['rwlock_t *lock) __must_hold(lock'], 'return_type': 'extern int'}`

### Rust Evidence

- Graph edges: `1`

## W-000557 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mdiobus_c45_read
- Explanation: __mdiobus_c45_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mii_bus *bus', 'int addr', 'int devad', 'u32 regnum'], 'return_type': 'int'}`
- New: `{'params': ['mdiodev->bus', 'mdiodev->addr', 'devad', 'regnum'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `1`

## W-000558 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mdiobus_c45_write
- Explanation: __mdiobus_c45_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mii_bus *bus', 'int addr', 'int devad', 'u32 regnum', 'u16 val'], 'return_type': 'int'}`
- New: `{'params': ['mdiodev->bus', 'mdiodev->addr', 'devad', 'regnum', 'val'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `1`

## W-000559 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __pte_offset_map
- Explanation: __pte_offset_map changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['pmd_t *pmd', 'unsigned long addr', 'pmd_t *pmdvalp'], 'return_type': 'static inline pte_t *'}`
- New: `{'params': ['pmd', 'addr', 'NULL'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `1`

## W-000567 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: aes_check_keylen
- Explanation: aes_check_keylen changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned int keylen'], 'return_type': 'static inline int'}`
- New: `{'params': ['size_t keylen'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `1`

## W-000578 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dentry_create
- Explanation: dentry_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct path *path', 'int flags', 'umode_t mode', 'const struct cred *cred'], 'return_type': 'struct file *'}`
- New: `{'params': ['struct path *path', 'int flags', 'umode_t mode', 'const struct cred *cred'], 'return_type': 'struct file *'}`

### Rust Evidence

- Graph edges: `1`

## W-000579 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_request_threaded_irq
- Explanation: devm_request_threaded_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['dev', 'irq', 'handler', 'NULL', 'irqflags', 'devname', 'dev_id'], 'return_type': 'return'}`
- New: `{'params': ['dev', 'irq', 'handler', 'NULL', 'irqflags | IRQF_COND_ONESHOT', 'devname', 'dev_id'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `1`

## W-000590 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_update_time
- Explanation: generic_update_time changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct inode *', 'int'], 'return_type': 'int'}`
- New: `{'params': ['struct inode *inode', 'enum fs_update_time type', 'unsigned int flags'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000591 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_locked_pte
- Explanation: get_locked_pte changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mm_struct *mm', 'unsigned long addr', 'spinlock_t **ptl'], 'return_type': 'static inline pte_t *'}`
- New: `{'params': ['struct mm_struct *mm', 'unsigned long addr', 'spinlock_t **ptl'], 'return_type': 'extern pte_t *'}`

### Rust Evidence

- Graph edges: `1`

## W-000592 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_update_time
- Explanation: inode_update_time changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct inode *inode', 'int flags'], 'return_type': 'int'}`
- New: `{'params': ['struct inode *inode', 'enum fs_update_time type', 'unsigned int flags'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000596 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pte_offset_map_lock
- Explanation: pte_offset_map_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mm_struct *mm', 'pmd_t *pmd', 'unsigned long addr', 'spinlock_t **ptlp'], 'return_type': 'static inline pte_t *'}`
- New: `{'params': ['struct mm_struct *mm', 'pmd_t *pmd', 'unsigned long addr', 'spinlock_t **ptlp'], 'return_type': 'pte_t *'}`

### Rust Evidence

- Graph edges: `1`

## W-000598 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: refcount_dec_and_lock_irqsave
- Explanation: refcount_dec_and_lock_irqsave changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['refcount_t *r', 'spinlock_t *lock', 'unsigned long *flags) __cond_acquires(lock'], 'return_type': 'extern __must_check bool'}`
- New: `{'params': ['refcount_t *r', 'spinlock_t *lock', 'unsigned long *flags) __cond_acquires(true, lock'], 'return_type': 'extern __must_check bool'}`

### Rust Evidence

- Graph edges: `1`

## W-000599 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: refcount_dec_and_mutex_lock
- Explanation: refcount_dec_and_mutex_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['refcount_t *r', 'struct mutex *lock) __cond_acquires(lock'], 'return_type': 'extern __must_check bool'}`
- New: `{'params': ['refcount_t *r', 'struct mutex *lock) __cond_acquires(true, lock'], 'return_type': 'extern __must_check bool'}`

### Rust Evidence

- Graph edges: `1`

## W-000600 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: request_percpu_irq_affinity
- Explanation: request_percpu_irq_affinity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned int irq', 'irq_handler_t handler', 'const char *devname', 'const cpumask_t *affinity', 'void __percpu *percpu_dev_id'], 'return_type': 'static inline int __must_check'}`
- New: `{'params': ['irq', 'handler', 'devname', 'NULL', 'percpu_dev_id'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `1`

## W-000603 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_BUG
- Explanation: rust_helper_BUG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': '__noreturn void'}`
- New: `{'params': [], 'return_type': '__rust_helper __noreturn void'}`

### Rust Evidence

- Graph edges: `0`

## W-000607 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_REFCOUNT_INIT
- Explanation: rust_helper_REFCOUNT_INIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['int n'], 'return_type': 'refcount_t'}`
- New: `{'params': ['int n'], 'return_type': '__rust_helper refcount_t'}`

### Rust Evidence

- Graph edges: `0`

## W-000608 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_WARN_ON
- Explanation: rust_helper_WARN_ON changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['bool cond'], 'return_type': 'bool'}`
- New: `{'params': ['bool cond'], 'return_type': '__rust_helper bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000609 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper___clear_bit
- Explanation: rust_helper___clear_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned long nr', 'unsigned long *addr'], 'return_type': 'void'}`
- New: `{'params': ['unsigned long nr', 'unsigned long *addr'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000610 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper___cpumask_clear_cpu
- Explanation: rust_helper___cpumask_clear_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['int cpu', 'struct cpumask *dstp'], 'return_type': 'void'}`
- New: `{'params': ['int cpu', 'struct cpumask *dstp'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000611 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper___cpumask_set_cpu
- Explanation: rust_helper___cpumask_set_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned int cpu', 'struct cpumask *dstp'], 'return_type': 'void'}`
- New: `{'params': ['unsigned int cpu', 'struct cpumask *dstp'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000612 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper___mutex_init
- Explanation: rust_helper___mutex_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mutex *mutex', 'const char *name', 'struct lock_class_key *key'], 'return_type': 'void'}`
- New: `{'params': ['struct mutex *mutex', 'const char *name', 'struct lock_class_key *key'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000613 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper___set_bit
- Explanation: rust_helper___set_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned long nr', 'unsigned long *addr'], 'return_type': 'void'}`
- New: `{'params': ['unsigned long nr', 'unsigned long *addr'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000615 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper__copy_from_user
- Explanation: rust_helper__copy_from_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['void *to', 'const void __user *from', 'unsigned long n'], 'return_type': 'unsigned long'}`
- New: `{'params': ['void *to', 'const void __user *from', 'unsigned long n'], 'return_type': '__rust_helper unsigned long'}`

### Rust Evidence

- Graph edges: `0`

## W-000616 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper__copy_to_user
- Explanation: rust_helper__copy_to_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['void __user *to', 'const void *from', 'unsigned long n'], 'return_type': 'unsigned long'}`
- New: `{'params': ['void __user *to', 'const void *from', 'unsigned long n'], 'return_type': '__rust_helper unsigned long'}`

### Rust Evidence

- Graph edges: `0`

## W-000617 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_alloc_cpumask_var
- Explanation: rust_helper_alloc_cpumask_var changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['cpumask_var_t *mask', 'gfp_t flags'], 'return_type': 'bool'}`
- New: `{'params': ['cpumask_var_t *mask', 'gfp_t flags'], 'return_type': '__rust_helper bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000618 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_alloc_pages
- Explanation: rust_helper_alloc_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['gfp_t gfp_mask', 'unsigned int order'], 'return_type': 'struct page *'}`
- New: `{'params': ['gfp_t gfp_mask', 'unsigned int order'], 'return_type': '__rust_helper struct page *'}`

### Rust Evidence

- Graph edges: `0`

## W-000619 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_auxiliary_device_delete
- Explanation: rust_helper_auxiliary_device_delete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct auxiliary_device *adev'], 'return_type': 'void'}`
- New: `{'params': ['struct auxiliary_device *adev'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000620 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_auxiliary_device_uninit
- Explanation: rust_helper_auxiliary_device_uninit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct auxiliary_device *adev'], 'return_type': 'void'}`
- New: `{'params': ['struct auxiliary_device *adev'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000621 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_bitmap_copy_and_extend
- Explanation: rust_helper_bitmap_copy_and_extend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned long *to', 'const unsigned long *from', 'unsigned int count', 'unsigned int size'], 'return_type': 'void'}`
- New: `{'params': ['unsigned long *to', 'const unsigned long *from', 'unsigned int count', 'unsigned int size'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000622 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_blk_mq_rq_from_pdu
- Explanation: rust_helper_blk_mq_rq_from_pdu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['void *pdu'], 'return_type': 'struct request *'}`
- New: `{'params': ['void *pdu'], 'return_type': '__rust_helper struct request *'}`

### Rust Evidence

- Graph edges: `0`

## W-000623 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_blk_mq_rq_to_pdu
- Explanation: rust_helper_blk_mq_rq_to_pdu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct request *rq'], 'return_type': 'void *'}`
- New: `{'params': ['struct request *rq'], 'return_type': '__rust_helper void *'}`

### Rust Evidence

- Graph edges: `0`

## W-000624 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_clear_bit
- Explanation: rust_helper_clear_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned long nr', 'volatile unsigned long *addr'], 'return_type': 'void'}`
- New: `{'params': ['unsigned long nr', 'volatile unsigned long *addr'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000625 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_copy_from_user
- Explanation: rust_helper_copy_from_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['void *to', 'const void __user *from', 'unsigned long n'], 'return_type': 'unsigned long'}`
- New: `{'params': ['void *to', 'const void __user *from', 'unsigned long n'], 'return_type': '__rust_helper unsigned long'}`

### Rust Evidence

- Graph edges: `0`

## W-000626 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_copy_to_user
- Explanation: rust_helper_copy_to_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['void __user *to', 'const void *from', 'unsigned long n'], 'return_type': 'unsigned long'}`
- New: `{'params': ['void __user *to', 'const void *from', 'unsigned long n'], 'return_type': '__rust_helper unsigned long'}`

### Rust Evidence

- Graph edges: `0`

## W-000627 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_cpu_relax
- Explanation: rust_helper_cpu_relax changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'void'}`
- New: `{'params': [], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000628 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_cpufreq_register_em_with_opp
- Explanation: rust_helper_cpufreq_register_em_with_opp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct cpufreq_policy *policy'], 'return_type': 'void'}`
- New: `{'params': ['struct cpufreq_policy *policy'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000629 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_cpumask_clear_cpu
- Explanation: rust_helper_cpumask_clear_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['int cpu', 'struct cpumask *dstp'], 'return_type': 'void'}`
- New: `{'params': ['int cpu', 'struct cpumask *dstp'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000630 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_cpumask_copy
- Explanation: rust_helper_cpumask_copy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct cpumask *dstp', 'const struct cpumask *srcp'], 'return_type': 'void'}`
- New: `{'params': ['struct cpumask *dstp', 'const struct cpumask *srcp'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000631 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_cpumask_empty
- Explanation: rust_helper_cpumask_empty changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct cpumask *srcp'], 'return_type': 'bool'}`
- New: `{'params': ['struct cpumask *srcp'], 'return_type': '__rust_helper bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000632 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_cpumask_full
- Explanation: rust_helper_cpumask_full changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct cpumask *srcp'], 'return_type': 'bool'}`
- New: `{'params': ['struct cpumask *srcp'], 'return_type': '__rust_helper bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000633 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_cpumask_set_cpu
- Explanation: rust_helper_cpumask_set_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned int cpu', 'struct cpumask *dstp'], 'return_type': 'void'}`
- New: `{'params': ['unsigned int cpu', 'struct cpumask *dstp'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000634 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_cpumask_setall
- Explanation: rust_helper_cpumask_setall changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct cpumask *dstp'], 'return_type': 'void'}`
- New: `{'params': ['struct cpumask *dstp'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000635 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_cpumask_test_cpu
- Explanation: rust_helper_cpumask_test_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['int cpu', 'struct cpumask *srcp'], 'return_type': 'bool'}`
- New: `{'params': ['int cpu', 'struct cpumask *srcp'], 'return_type': '__rust_helper bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000636 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_cpumask_weight
- Explanation: rust_helper_cpumask_weight changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct cpumask *srcp'], 'return_type': 'unsigned int'}`
- New: `{'params': ['struct cpumask *srcp'], 'return_type': '__rust_helper unsigned int'}`

### Rust Evidence

- Graph edges: `0`

## W-000637 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_current_euid
- Explanation: rust_helper_current_euid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'kuid_t'}`
- New: `{'params': [], 'return_type': '__rust_helper kuid_t'}`

### Rust Evidence

- Graph edges: `0`

## W-000638 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_current_user_ns
- Explanation: rust_helper_current_user_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'struct user_namespace *'}`
- New: `{'params': [], 'return_type': '__rust_helper struct user_namespace *'}`

### Rust Evidence

- Graph edges: `0`

## W-000639 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_dev_get_drvdata
- Explanation: rust_helper_dev_get_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct device *dev'], 'return_type': 'void *'}`
- New: `{'params': ['const struct device *dev'], 'return_type': '__rust_helper void *'}`

### Rust Evidence

- Graph edges: `0`

## W-000640 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_dev_is_pci
- Explanation: rust_helper_dev_is_pci changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct device *dev'], 'return_type': 'bool'}`
- New: `{'params': ['const struct device *dev'], 'return_type': '__rust_helper bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000641 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_dev_is_platform
- Explanation: rust_helper_dev_is_platform changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct device *dev'], 'return_type': 'bool'}`
- New: `{'params': ['const struct device *dev'], 'return_type': '__rust_helper bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000642 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_dev_set_drvdata
- Explanation: rust_helper_dev_set_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct device *dev', 'void *data'], 'return_type': 'void'}`
- New: `{'params': ['struct device *dev', 'void *data'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000643 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_devm_add_action
- Explanation: rust_helper_devm_add_action changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct device *dev', 'void (*action)(void *)', 'void *data'], 'return_type': 'int'}`
- New: `{'params': ['struct device *dev', 'void (*action)(void *)', 'void *data'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000644 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_devm_add_action_or_reset
- Explanation: rust_helper_devm_add_action_or_reset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct device *dev', 'void (*action)(void *)', 'void *data'], 'return_type': 'int'}`
- New: `{'params': ['struct device *dev', 'void (*action)(void *)', 'void *data'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000645 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_devm_regulator_get_enable
- Explanation: rust_helper_devm_regulator_get_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct device *dev', 'const char *id'], 'return_type': 'int'}`
- New: `{'params': ['struct device *dev', 'const char *id'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000646 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_devm_regulator_get_enable_optional
- Explanation: rust_helper_devm_regulator_get_enable_optional changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct device *dev', 'const char *id'], 'return_type': 'int'}`
- New: `{'params': ['struct device *dev', 'const char *id'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000647 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_dma_alloc_attrs
- Explanation: rust_helper_dma_alloc_attrs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct device *dev', 'size_t size', 'dma_addr_t *dma_handle', 'gfp_t flag', 'unsigned long attrs'], 'return_type': 'void *'}`
- New: `{'params': ['struct device *dev', 'size_t size', 'dma_addr_t *dma_handle', 'gfp_t flag', 'unsigned long attrs'], 'return_type': '__rust_helper void *'}`

### Rust Evidence

- Graph edges: `0`

## W-000648 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_dma_free_attrs
- Explanation: rust_helper_dma_free_attrs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct device *dev', 'size_t size', 'void *cpu_addr', 'dma_addr_t dma_handle', 'unsigned long attrs'], 'return_type': 'void'}`
- New: `{'params': ['struct device *dev', 'size_t size', 'void *cpu_addr', 'dma_addr_t dma_handle', 'unsigned long attrs'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000649 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_dma_map_sgtable
- Explanation: rust_helper_dma_map_sgtable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct device *dev', 'struct sg_table *sgt', 'enum dma_data_direction dir', 'unsigned long attrs'], 'return_type': 'int'}`
- New: `{'params': ['struct device *dev', 'struct sg_table *sgt', 'enum dma_data_direction dir', 'unsigned long attrs'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000650 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_dma_max_mapping_size
- Explanation: rust_helper_dma_max_mapping_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct device *dev'], 'return_type': 'size_t'}`
- New: `{'params': ['struct device *dev'], 'return_type': '__rust_helper size_t'}`

### Rust Evidence

- Graph edges: `0`

## W-000651 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_dma_set_coherent_mask
- Explanation: rust_helper_dma_set_coherent_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct device *dev', 'u64 mask'], 'return_type': 'int'}`
- New: `{'params': ['struct device *dev', 'u64 mask'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000652 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_dma_set_mask
- Explanation: rust_helper_dma_set_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct device *dev', 'u64 mask'], 'return_type': 'int'}`
- New: `{'params': ['struct device *dev', 'u64 mask'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000653 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_dma_set_mask_and_coherent
- Explanation: rust_helper_dma_set_mask_and_coherent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct device *dev', 'u64 mask'], 'return_type': 'int'}`
- New: `{'params': ['struct device *dev', 'u64 mask'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000654 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_dma_unmap_sgtable
- Explanation: rust_helper_dma_unmap_sgtable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct device *dev', 'struct sg_table *sgt', 'enum dma_data_direction dir', 'unsigned long attrs'], 'return_type': 'void'}`
- New: `{'params': ['struct device *dev', 'struct sg_table *sgt', 'enum dma_data_direction dir', 'unsigned long attrs'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000657 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_drm_vma_node_offset_addr
- Explanation: rust_helper_drm_vma_node_offset_addr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_vma_offset_node *node'], 'return_type': '__u64'}`
- New: `{'params': ['struct drm_vma_offset_node *node'], 'return_type': '__rust_helper __u64'}`

### Rust Evidence

- Graph edges: `0`

## W-000658 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_errname
- Explanation: rust_helper_errname changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['int err'], 'return_type': 'const char *'}`
- New: `{'params': ['int err'], 'return_type': '__rust_helper const char *'}`

### Rust Evidence

- Graph edges: `0`

## W-000659 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_free_cpumask_var
- Explanation: rust_helper_free_cpumask_var changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['cpumask_var_t mask'], 'return_type': 'void'}`
- New: `{'params': ['cpumask_var_t mask'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000660 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_from_kuid
- Explanation: rust_helper_from_kuid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct user_namespace *to', 'kuid_t uid'], 'return_type': 'uid_t'}`
- New: `{'params': ['struct user_namespace *to', 'kuid_t uid'], 'return_type': '__rust_helper uid_t'}`

### Rust Evidence

- Graph edges: `0`

## W-000661 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_fsleep
- Explanation: rust_helper_fsleep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned long usecs'], 'return_type': 'void'}`
- New: `{'params': ['unsigned long usecs'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000663 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_get_cred
- Explanation: rust_helper_get_cred changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct cred *cred'], 'return_type': 'const struct cred *'}`
- New: `{'params': ['const struct cred *cred'], 'return_type': '__rust_helper const struct cred *'}`

### Rust Evidence

- Graph edges: `0`

## W-000664 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_get_current
- Explanation: rust_helper_get_current changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'struct task_struct *'}`
- New: `{'params': [], 'return_type': '__rust_helper struct task_struct *'}`

### Rust Evidence

- Graph edges: `0`

## W-000665 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_get_file
- Explanation: rust_helper_get_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct file *f'], 'return_type': 'struct file *'}`
- New: `{'params': ['struct file *f'], 'return_type': '__rust_helper struct file *'}`

### Rust Evidence

- Graph edges: `0`

## W-000666 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_get_pid_ns
- Explanation: rust_helper_get_pid_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct pid_namespace *ns'], 'return_type': 'struct pid_namespace *'}`
- New: `{'params': ['struct pid_namespace *ns'], 'return_type': '__rust_helper struct pid_namespace *'}`

### Rust Evidence

- Graph edges: `0`

## W-000667 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_get_task_struct
- Explanation: rust_helper_get_task_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct task_struct *t'], 'return_type': 'void'}`
- New: `{'params': ['struct task_struct *t'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000668 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_init_completion
- Explanation: rust_helper_init_completion changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct completion *x'], 'return_type': 'void'}`
- New: `{'params': ['struct completion *x'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000669 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_init_task_work
- Explanation: rust_helper_init_task_work changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct callback_head *twork', 'task_work_func_t func'], 'return_type': 'void'}`
- New: `{'params': ['struct callback_head *twork', 'task_work_func_t func'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000670 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_init_wait
- Explanation: rust_helper_init_wait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct wait_queue_entry *wq_entry'], 'return_type': 'void'}`
- New: `{'params': ['struct wait_queue_entry *wq_entry'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000671 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_init_work_with_key
- Explanation: rust_helper_init_work_with_key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct work_struct *work', 'work_func_t func', 'bool onstack', 'const char *name', 'struct lock_class_key *key'], 'return_type': 'void'}`
- New: `{'params': ['struct work_struct *work', 'work_func_t func', 'bool onstack', 'const char *name', 'struct lock_class_key *key'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000672 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_interface_to_usbdev
- Explanation: rust_helper_interface_to_usbdev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct usb_interface *intf'], 'return_type': 'struct usb_device *'}`
- New: `{'params': ['struct usb_interface *intf'], 'return_type': '__rust_helper struct usb_device *'}`

### Rust Evidence

- Graph edges: `0`

## W-000673 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_ioremap
- Explanation: rust_helper_ioremap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['phys_addr_t offset', 'size_t size'], 'return_type': 'void __iomem *'}`
- New: `{'params': ['phys_addr_t offset', 'size_t size'], 'return_type': '__rust_helper void __iomem *'}`

### Rust Evidence

- Graph edges: `0`

## W-000674 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_ioremap_np
- Explanation: rust_helper_ioremap_np changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['phys_addr_t offset', 'size_t size'], 'return_type': 'void __iomem *'}`
- New: `{'params': ['phys_addr_t offset', 'size_t size'], 'return_type': '__rust_helper void __iomem *'}`

### Rust Evidence

- Graph edges: `0`

## W-000675 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_iounmap
- Explanation: rust_helper_iounmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['void __iomem *addr'], 'return_type': 'void'}`
- New: `{'params': ['void __iomem *addr'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000676 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_is_of_node
- Explanation: rust_helper_is_of_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct fwnode_handle *fwnode'], 'return_type': 'bool'}`
- New: `{'params': ['const struct fwnode_handle *fwnode'], 'return_type': '__rust_helper bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000677 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_kmap_local_page
- Explanation: rust_helper_kmap_local_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct page *page'], 'return_type': 'void *'}`
- New: `{'params': ['struct page *page'], 'return_type': '__rust_helper void *'}`

### Rust Evidence

- Graph edges: `0`

## W-000678 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_ktime_get_boottime
- Explanation: rust_helper_ktime_get_boottime changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'ktime_t'}`
- New: `{'params': [], 'return_type': '__rust_helper ktime_t'}`

### Rust Evidence

- Graph edges: `0`

## W-000679 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_ktime_get_clocktai
- Explanation: rust_helper_ktime_get_clocktai changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'ktime_t'}`
- New: `{'params': [], 'return_type': '__rust_helper ktime_t'}`

### Rust Evidence

- Graph edges: `0`

## W-000680 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_ktime_get_real
- Explanation: rust_helper_ktime_get_real changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'ktime_t'}`
- New: `{'params': [], 'return_type': '__rust_helper ktime_t'}`

### Rust Evidence

- Graph edges: `0`

## W-000681 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_ktime_to_ms
- Explanation: rust_helper_ktime_to_ms changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const ktime_t kt'], 'return_type': 's64'}`
- New: `{'params': ['const ktime_t kt'], 'return_type': '__rust_helper s64'}`

### Rust Evidence

- Graph edges: `0`

## W-000682 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_ktime_to_us
- Explanation: rust_helper_ktime_to_us changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const ktime_t kt'], 'return_type': 's64'}`
- New: `{'params': ['const ktime_t kt'], 'return_type': '__rust_helper s64'}`

### Rust Evidence

- Graph edges: `0`

## W-000683 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_kunit_get_current_test
- Explanation: rust_helper_kunit_get_current_test changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'struct kunit *'}`
- New: `{'params': [], 'return_type': '__rust_helper struct kunit *'}`

### Rust Evidence

- Graph edges: `0`

## W-000684 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_kunmap_local
- Explanation: rust_helper_kunmap_local changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const void *addr'], 'return_type': 'void'}`
- New: `{'params': ['const void *addr'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000685 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_list_lru_count
- Explanation: rust_helper_list_lru_count changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct list_lru *lru'], 'return_type': 'unsigned long'}`
- New: `{'params': ['struct list_lru *lru'], 'return_type': '__rust_helper unsigned long'}`

### Rust Evidence

- Graph edges: `0`

## W-000686 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_list_lru_walk
- Explanation: rust_helper_list_lru_walk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct list_lru *lru', 'list_lru_walk_cb isolate', 'void *cb_arg', 'unsigned long nr_to_walk'], 'return_type': 'unsigned long'}`
- New: `{'params': ['struct list_lru *lru', 'list_lru_walk_cb isolate', 'void *cb_arg', 'unsigned long nr_to_walk'], 'return_type': '__rust_helper unsigned long'}`

### Rust Evidence

- Graph edges: `0`

## W-000687 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_lockdep_register_key
- Explanation: rust_helper_lockdep_register_key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct lock_class_key *k'], 'return_type': 'void'}`
- New: `{'params': ['struct lock_class_key *k'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000688 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_lockdep_unregister_key
- Explanation: rust_helper_lockdep_unregister_key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct lock_class_key *k'], 'return_type': 'void'}`
- New: `{'params': ['struct lock_class_key *k'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000689 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_might_resched
- Explanation: rust_helper_might_resched changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'void'}`
- New: `{'params': [], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000690 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_mmap_read_lock
- Explanation: rust_helper_mmap_read_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mm_struct *mm'], 'return_type': 'void'}`
- New: `{'params': ['struct mm_struct *mm'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000691 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_mmap_read_trylock
- Explanation: rust_helper_mmap_read_trylock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mm_struct *mm'], 'return_type': 'bool'}`
- New: `{'params': ['struct mm_struct *mm'], 'return_type': '__rust_helper bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000692 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_mmap_read_unlock
- Explanation: rust_helper_mmap_read_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mm_struct *mm'], 'return_type': 'void'}`
- New: `{'params': ['struct mm_struct *mm'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000693 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_mmdrop
- Explanation: rust_helper_mmdrop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mm_struct *mm'], 'return_type': 'void'}`
- New: `{'params': ['struct mm_struct *mm'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000694 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_mmget
- Explanation: rust_helper_mmget changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mm_struct *mm'], 'return_type': 'void'}`
- New: `{'params': ['struct mm_struct *mm'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000695 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_mmget_not_zero
- Explanation: rust_helper_mmget_not_zero changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mm_struct *mm'], 'return_type': 'bool'}`
- New: `{'params': ['struct mm_struct *mm'], 'return_type': '__rust_helper bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000696 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_mmgrab
- Explanation: rust_helper_mmgrab changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mm_struct *mm'], 'return_type': 'void'}`
- New: `{'params': ['struct mm_struct *mm'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000697 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_mt_init_flags
- Explanation: rust_helper_mt_init_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct maple_tree *mt', 'unsigned int flags'], 'return_type': 'void'}`
- New: `{'params': ['struct maple_tree *mt', 'unsigned int flags'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000698 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_mutex_assert_is_held
- Explanation: rust_helper_mutex_assert_is_held changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mutex *mutex'], 'return_type': 'void'}`
- New: `{'params': ['struct mutex *mutex'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000701 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_mutex_trylock
- Explanation: rust_helper_mutex_trylock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mutex *lock'], 'return_type': 'int'}`
- New: `{'params': ['struct mutex *lock'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000702 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_page_to_nid
- Explanation: rust_helper_page_to_nid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct page *page'], 'return_type': 'int'}`
- New: `{'params': ['const struct page *page'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000703 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_pci_alloc_irq_vectors
- Explanation: rust_helper_pci_alloc_irq_vectors changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct pci_dev *dev', 'unsigned int min_vecs', 'unsigned int max_vecs', 'unsigned int flags'], 'return_type': 'int'}`
- New: `{'params': ['struct pci_dev *dev', 'unsigned int min_vecs', 'unsigned int max_vecs', 'unsigned int flags'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000704 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_pci_dev_id
- Explanation: rust_helper_pci_dev_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct pci_dev *dev'], 'return_type': 'u16'}`
- New: `{'params': ['struct pci_dev *dev'], 'return_type': '__rust_helper u16'}`

### Rust Evidence

- Graph edges: `0`

## W-000705 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_pci_free_irq_vectors
- Explanation: rust_helper_pci_free_irq_vectors changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct pci_dev *dev'], 'return_type': 'void'}`
- New: `{'params': ['struct pci_dev *dev'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000706 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_pci_irq_vector
- Explanation: rust_helper_pci_irq_vector changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct pci_dev *pdev', 'unsigned int nvec'], 'return_type': 'int'}`
- New: `{'params': ['struct pci_dev *pdev', 'unsigned int nvec'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000707 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_pci_resource_len
- Explanation: rust_helper_pci_resource_len changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct pci_dev *pdev', 'int bar'], 'return_type': 'resource_size_t'}`
- New: `{'params': ['struct pci_dev *pdev', 'int bar'], 'return_type': '__rust_helper resource_size_t'}`

### Rust Evidence

- Graph edges: `0`

## W-000708 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_pci_resource_start
- Explanation: rust_helper_pci_resource_start changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct pci_dev *pdev', 'int bar'], 'return_type': 'resource_size_t'}`
- New: `{'params': ['struct pci_dev *pdev', 'int bar'], 'return_type': '__rust_helper resource_size_t'}`

### Rust Evidence

- Graph edges: `0`

## W-000709 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_poll_wait
- Explanation: rust_helper_poll_wait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct file *filp', 'wait_queue_head_t *wait_address', 'poll_table *p'], 'return_type': 'void'}`
- New: `{'params': ['struct file *filp', 'wait_queue_head_t *wait_address', 'poll_table *p'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000710 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_put_cred
- Explanation: rust_helper_put_cred changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct cred *cred'], 'return_type': 'void'}`
- New: `{'params': ['const struct cred *cred'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000711 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_put_pid_ns
- Explanation: rust_helper_put_pid_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct pid_namespace *ns'], 'return_type': 'void'}`
- New: `{'params': ['struct pid_namespace *ns'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000712 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_put_task_struct
- Explanation: rust_helper_put_task_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct task_struct *t'], 'return_type': 'void'}`
- New: `{'params': ['struct task_struct *t'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000713 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_pwmchip_get_drvdata
- Explanation: rust_helper_pwmchip_get_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct pwm_chip *chip'], 'return_type': 'void *'}`
- New: `{'params': ['struct pwm_chip *chip'], 'return_type': '__rust_helper void *'}`

### Rust Evidence

- Graph edges: `0`

## W-000714 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_pwmchip_parent
- Explanation: rust_helper_pwmchip_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct pwm_chip *chip'], 'return_type': 'struct device *'}`
- New: `{'params': ['const struct pwm_chip *chip'], 'return_type': '__rust_helper struct device *'}`

### Rust Evidence

- Graph edges: `0`

## W-000715 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_pwmchip_set_drvdata
- Explanation: rust_helper_pwmchip_set_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct pwm_chip *chip', 'void *data'], 'return_type': 'void'}`
- New: `{'params': ['struct pwm_chip *chip', 'void *data'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000716 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_raw_smp_processor_id
- Explanation: rust_helper_raw_smp_processor_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'unsigned int'}`
- New: `{'params': [], 'return_type': '__rust_helper unsigned int'}`

### Rust Evidence

- Graph edges: `0`

## W-000717 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_rb_first
- Explanation: rust_helper_rb_first changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct rb_root *root'], 'return_type': 'struct rb_node *'}`
- New: `{'params': ['const struct rb_root *root'], 'return_type': '__rust_helper struct rb_node *'}`

### Rust Evidence

- Graph edges: `0`

## W-000718 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_rb_last
- Explanation: rust_helper_rb_last changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct rb_root *root'], 'return_type': 'struct rb_node *'}`
- New: `{'params': ['const struct rb_root *root'], 'return_type': '__rust_helper struct rb_node *'}`

### Rust Evidence

- Graph edges: `0`

## W-000719 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_rb_link_node
- Explanation: rust_helper_rb_link_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct rb_node *node', 'struct rb_node *parent', 'struct rb_node **rb_link'], 'return_type': 'void'}`
- New: `{'params': ['struct rb_node *node', 'struct rb_node *parent', 'struct rb_node **rb_link'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000721 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_rcu_read_unlock
- Explanation: rust_helper_rcu_read_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'void'}`
- New: `{'params': [], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000722 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_readb
- Explanation: rust_helper_readb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const void __iomem *addr'], 'return_type': 'u8'}`
- New: `{'params': ['const void __iomem *addr'], 'return_type': '__rust_helper u8'}`

### Rust Evidence

- Graph edges: `0`

## W-000723 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_readb_relaxed
- Explanation: rust_helper_readb_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const void __iomem *addr'], 'return_type': 'u8'}`
- New: `{'params': ['const void __iomem *addr'], 'return_type': '__rust_helper u8'}`

### Rust Evidence

- Graph edges: `0`

## W-000724 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_readl
- Explanation: rust_helper_readl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const void __iomem *addr'], 'return_type': 'u32'}`
- New: `{'params': ['const void __iomem *addr'], 'return_type': '__rust_helper u32'}`

### Rust Evidence

- Graph edges: `0`

## W-000725 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_readl_relaxed
- Explanation: rust_helper_readl_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const void __iomem *addr'], 'return_type': 'u32'}`
- New: `{'params': ['const void __iomem *addr'], 'return_type': '__rust_helper u32'}`

### Rust Evidence

- Graph edges: `0`

## W-000726 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_readq
- Explanation: rust_helper_readq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const void __iomem *addr'], 'return_type': 'u64'}`
- New: `{'params': ['const void __iomem *addr'], 'return_type': '__rust_helper u64'}`

### Rust Evidence

- Graph edges: `0`

## W-000727 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_readq_relaxed
- Explanation: rust_helper_readq_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const void __iomem *addr'], 'return_type': 'u64'}`
- New: `{'params': ['const void __iomem *addr'], 'return_type': '__rust_helper u64'}`

### Rust Evidence

- Graph edges: `0`

## W-000728 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_readw
- Explanation: rust_helper_readw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const void __iomem *addr'], 'return_type': 'u16'}`
- New: `{'params': ['const void __iomem *addr'], 'return_type': '__rust_helper u16'}`

### Rust Evidence

- Graph edges: `0`

## W-000729 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_readw_relaxed
- Explanation: rust_helper_readw_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const void __iomem *addr'], 'return_type': 'u16'}`
- New: `{'params': ['const void __iomem *addr'], 'return_type': '__rust_helper u16'}`

### Rust Evidence

- Graph edges: `0`

## W-000733 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_refcount_set
- Explanation: rust_helper_refcount_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['refcount_t *r', 'int n'], 'return_type': 'void'}`
- New: `{'params': ['refcount_t *r', 'int n'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000734 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_regulator_disable
- Explanation: rust_helper_regulator_disable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct regulator *regulator'], 'return_type': 'int'}`
- New: `{'params': ['struct regulator *regulator'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000735 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_regulator_enable
- Explanation: rust_helper_regulator_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct regulator *regulator'], 'return_type': 'int'}`
- New: `{'params': ['struct regulator *regulator'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000737 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_regulator_get_voltage
- Explanation: rust_helper_regulator_get_voltage changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct regulator *regulator'], 'return_type': 'int'}`
- New: `{'params': ['struct regulator *regulator'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000738 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_regulator_is_enabled
- Explanation: rust_helper_regulator_is_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct regulator *regulator'], 'return_type': 'int'}`
- New: `{'params': ['struct regulator *regulator'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000740 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_regulator_set_voltage
- Explanation: rust_helper_regulator_set_voltage changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct regulator *regulator', 'int min_uV', 'int max_uV'], 'return_type': 'int'}`
- New: `{'params': ['struct regulator *regulator', 'int min_uV', 'int max_uV'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000741 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_release_mem_region
- Explanation: rust_helper_release_mem_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['resource_size_t start', 'resource_size_t n'], 'return_type': 'void'}`
- New: `{'params': ['resource_size_t start', 'resource_size_t n'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000742 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_release_region
- Explanation: rust_helper_release_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['resource_size_t start', 'resource_size_t n'], 'return_type': 'void'}`
- New: `{'params': ['resource_size_t start', 'resource_size_t n'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000743 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_request_irq
- Explanation: rust_helper_request_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned int irq', 'irq_handler_t handler', 'unsigned long flags', 'const char *name', 'void *dev'], 'return_type': 'int'}`
- New: `{'params': ['unsigned int irq', 'irq_handler_t handler', 'unsigned long flags', 'const char *name', 'void *dev'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000744 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_request_mem_region
- Explanation: rust_helper_request_mem_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['resource_size_t start', 'resource_size_t n', 'const char *name'], 'return_type': 'struct resource *'}`
- New: `{'params': ['resource_size_t start', 'resource_size_t n', 'const char *name'], 'return_type': '__rust_helper struct resource *'}`

### Rust Evidence

- Graph edges: `0`

## W-000745 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_request_muxed_region
- Explanation: rust_helper_request_muxed_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['resource_size_t start', 'resource_size_t n', 'const char *name'], 'return_type': 'struct resource *'}`
- New: `{'params': ['resource_size_t start', 'resource_size_t n', 'const char *name'], 'return_type': '__rust_helper struct resource *'}`

### Rust Evidence

- Graph edges: `0`

## W-000746 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_request_region
- Explanation: rust_helper_request_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['resource_size_t start', 'resource_size_t n', 'const char *name'], 'return_type': 'struct resource *'}`
- New: `{'params': ['resource_size_t start', 'resource_size_t n', 'const char *name'], 'return_type': '__rust_helper struct resource *'}`

### Rust Evidence

- Graph edges: `0`

## W-000747 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_resource_size
- Explanation: rust_helper_resource_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct resource *res'], 'return_type': 'resource_size_t'}`
- New: `{'params': ['struct resource *res'], 'return_type': '__rust_helper resource_size_t'}`

### Rust Evidence

- Graph edges: `0`

## W-000748 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_security_binder_set_context_mgr
- Explanation: rust_helper_security_binder_set_context_mgr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct cred *mgr'], 'return_type': 'int'}`
- New: `{'params': ['const struct cred *mgr'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000749 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_security_binder_transaction
- Explanation: rust_helper_security_binder_transaction changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct cred *from', 'const struct cred *to'], 'return_type': 'int'}`
- New: `{'params': ['const struct cred *from', 'const struct cred *to'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000750 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_security_binder_transfer_binder
- Explanation: rust_helper_security_binder_transfer_binder changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct cred *from', 'const struct cred *to'], 'return_type': 'int'}`
- New: `{'params': ['const struct cred *from', 'const struct cred *to'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000751 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_security_binder_transfer_file
- Explanation: rust_helper_security_binder_transfer_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct cred *from', 'const struct cred *to', 'const struct file *file'], 'return_type': 'int'}`
- New: `{'params': ['const struct cred *from', 'const struct cred *to', 'const struct file *file'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000752 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_security_cred_getsecid
- Explanation: rust_helper_security_cred_getsecid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct cred *c', 'u32 *secid'], 'return_type': 'void'}`
- New: `{'params': ['const struct cred *c', 'u32 *secid'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000753 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_security_release_secctx
- Explanation: rust_helper_security_release_secctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct lsm_context *cp'], 'return_type': 'void'}`
- New: `{'params': ['struct lsm_context *cp'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000754 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_security_secid_to_secctx
- Explanation: rust_helper_security_secid_to_secctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u32 secid', 'struct lsm_context *cp'], 'return_type': 'int'}`
- New: `{'params': ['u32 secid', 'struct lsm_context *cp'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000755 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_set_bit
- Explanation: rust_helper_set_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned long nr', 'volatile unsigned long *addr'], 'return_type': 'void'}`
- New: `{'params': ['unsigned long nr', 'volatile unsigned long *addr'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000756 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_sg_dma_address
- Explanation: rust_helper_sg_dma_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct scatterlist *sg'], 'return_type': 'dma_addr_t'}`
- New: `{'params': ['struct scatterlist *sg'], 'return_type': '__rust_helper dma_addr_t'}`

### Rust Evidence

- Graph edges: `0`

## W-000757 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_sg_dma_len
- Explanation: rust_helper_sg_dma_len changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct scatterlist *sg'], 'return_type': 'unsigned int'}`
- New: `{'params': ['struct scatterlist *sg'], 'return_type': '__rust_helper unsigned int'}`

### Rust Evidence

- Graph edges: `0`

## W-000758 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_sg_next
- Explanation: rust_helper_sg_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct scatterlist *sg'], 'return_type': 'struct scatterlist *'}`
- New: `{'params': ['struct scatterlist *sg'], 'return_type': '__rust_helper struct scatterlist *'}`

### Rust Evidence

- Graph edges: `0`

## W-000759 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_signal_pending
- Explanation: rust_helper_signal_pending changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct task_struct *t'], 'return_type': 'int'}`
- New: `{'params': ['struct task_struct *t'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000760 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_smp_mb
- Explanation: rust_helper_smp_mb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'void'}`
- New: `{'params': [], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000761 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_smp_rmb
- Explanation: rust_helper_smp_rmb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'void'}`
- New: `{'params': [], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000762 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_smp_wmb
- Explanation: rust_helper_smp_wmb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'void'}`
- New: `{'params': [], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000763 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_spin_assert_is_held
- Explanation: rust_helper_spin_assert_is_held changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['spinlock_t *lock'], 'return_type': 'void'}`
- New: `{'params': ['spinlock_t *lock'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000765 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_spin_trylock
- Explanation: rust_helper_spin_trylock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['spinlock_t *lock'], 'return_type': 'int'}`
- New: `{'params': ['spinlock_t *lock'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000766 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_spin_unlock
- Explanation: rust_helper_spin_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['spinlock_t *lock'], 'return_type': 'void'}`
- New: `{'params': ['spinlock_t *lock'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000767 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_task_euid
- Explanation: rust_helper_task_euid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct task_struct *task'], 'return_type': 'kuid_t'}`
- New: `{'params': ['struct task_struct *task'], 'return_type': '__rust_helper kuid_t'}`

### Rust Evidence

- Graph edges: `0`

## W-000768 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_task_get_pid_ns
- Explanation: rust_helper_task_get_pid_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct task_struct *task'], 'return_type': 'struct pid_namespace *'}`
- New: `{'params': ['struct task_struct *task'], 'return_type': '__rust_helper struct pid_namespace *'}`

### Rust Evidence

- Graph edges: `0`

## W-000769 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_task_tgid_nr_ns
- Explanation: rust_helper_task_tgid_nr_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct task_struct *tsk', 'struct pid_namespace *ns'], 'return_type': 'pid_t'}`
- New: `{'params': ['struct task_struct *tsk', 'struct pid_namespace *ns'], 'return_type': '__rust_helper pid_t'}`

### Rust Evidence

- Graph edges: `0`

## W-000770 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_task_uid
- Explanation: rust_helper_task_uid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct task_struct *task'], 'return_type': 'kuid_t'}`
- New: `{'params': ['struct task_struct *task'], 'return_type': '__rust_helper kuid_t'}`

### Rust Evidence

- Graph edges: `0`

## W-000771 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_udelay
- Explanation: rust_helper_udelay changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned long usec'], 'return_type': 'void'}`
- New: `{'params': ['unsigned long usec'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000772 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_uid_eq
- Explanation: rust_helper_uid_eq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['kuid_t left', 'kuid_t right'], 'return_type': 'bool'}`
- New: `{'params': ['kuid_t left', 'kuid_t right'], 'return_type': '__rust_helper bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000773 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_vma_end_read
- Explanation: rust_helper_vma_end_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct vm_area_struct *vma'], 'return_type': 'void'}`
- New: `{'params': ['struct vm_area_struct *vma'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000774 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_vma_lookup
- Explanation: rust_helper_vma_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mm_struct *mm', 'unsigned long addr'], 'return_type': 'struct vm_area_struct *'}`
- New: `{'params': ['struct mm_struct *mm', 'unsigned long addr'], 'return_type': '__rust_helper struct vm_area_struct *'}`

### Rust Evidence

- Graph edges: `0`

## W-000775 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_writeb
- Explanation: rust_helper_writeb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u8 value', 'void __iomem *addr'], 'return_type': 'void'}`
- New: `{'params': ['u8 value', 'void __iomem *addr'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000776 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_writeb_relaxed
- Explanation: rust_helper_writeb_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u8 value', 'void __iomem *addr'], 'return_type': 'void'}`
- New: `{'params': ['u8 value', 'void __iomem *addr'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000777 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_writel
- Explanation: rust_helper_writel changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u32 value', 'void __iomem *addr'], 'return_type': 'void'}`
- New: `{'params': ['u32 value', 'void __iomem *addr'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000778 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_writel_relaxed
- Explanation: rust_helper_writel_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u32 value', 'void __iomem *addr'], 'return_type': 'void'}`
- New: `{'params': ['u32 value', 'void __iomem *addr'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000779 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_writeq
- Explanation: rust_helper_writeq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u64 value', 'void __iomem *addr'], 'return_type': 'void'}`
- New: `{'params': ['u64 value', 'void __iomem *addr'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000780 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_writeq_relaxed
- Explanation: rust_helper_writeq_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u64 value', 'void __iomem *addr'], 'return_type': 'void'}`
- New: `{'params': ['u64 value', 'void __iomem *addr'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000781 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_writew
- Explanation: rust_helper_writew changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u16 value', 'void __iomem *addr'], 'return_type': 'void'}`
- New: `{'params': ['u16 value', 'void __iomem *addr'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000782 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_writew_relaxed
- Explanation: rust_helper_writew_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u16 value', 'void __iomem *addr'], 'return_type': 'void'}`
- New: `{'params': ['u16 value', 'void __iomem *addr'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000783 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_xa_err
- Explanation: rust_helper_xa_err changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['void *entry'], 'return_type': 'int'}`
- New: `{'params': ['void *entry'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000784 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_xa_init_flags
- Explanation: rust_helper_xa_init_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct xarray *xa', 'gfp_t flags'], 'return_type': 'void'}`
- New: `{'params': ['struct xarray *xa', 'gfp_t flags'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000785 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_xa_lock
- Explanation: rust_helper_xa_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct xarray *xa'], 'return_type': 'void'}`
- New: `{'params': ['struct xarray *xa'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000786 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_xa_trylock
- Explanation: rust_helper_xa_trylock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct xarray *xa'], 'return_type': 'int'}`
- New: `{'params': ['struct xarray *xa'], 'return_type': '__rust_helper int'}`

### Rust Evidence

- Graph edges: `0`

## W-000787 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_xa_unlock
- Explanation: rust_helper_xa_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct xarray *xa'], 'return_type': 'void'}`
- New: `{'params': ['struct xarray *xa'], 'return_type': '__rust_helper void'}`

### Rust Evidence

- Graph edges: `0`

## W-000788 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: rust_helper_zalloc_cpumask_var
- Explanation: rust_helper_zalloc_cpumask_var changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['cpumask_var_t *mask', 'gfp_t flags'], 'return_type': 'bool'}`
- New: `{'params': ['cpumask_var_t *mask', 'gfp_t flags'], 'return_type': '__rust_helper bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000367 FieldDrift

- Risk: High
- Score: 10.0
- Symbol: io_comp_batch
- Explanation: io_comp_batch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'req_list', 'type': 'rq_list'}, {'name': 'need_ts', 'type': 'bool_'}, {'name': 'complete', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut io_comp_batch)>'}]`
- New: `[{'name': 'req_list', 'type': 'rq_list'}, {'name': 'need_ts', 'type': 'bool_'}, {'name': 'complete', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut io_comp_batch)>'}, {'name': 'poll_ctx', 'type': '*mut ffi::c_void'}]`

### Rust Evidence

- Graph edges: `7`

## W-000001 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __SCT__pv_sched_clock
- Explanation: __SCT__pv_sched_clock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000002 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __SCT__pv_steal_clock
- Explanation: __SCT__pv_steal_clock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000003 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ___pte_offset_map
- Explanation: ___pte_offset_map changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000007 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __get_locked_pte
- Explanation: __get_locked_pte changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000011 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __ksize
- Explanation: __ksize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000012 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __lock_task_sighand
- Explanation: __lock_task_sighand changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000014 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __pte_offset_map_lock
- Explanation: __pte_offset_map_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000016 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __request_percpu_irq
- Explanation: __request_percpu_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000059 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: bin2hex
- Explanation: bin2hex changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000069 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: call_rcu_tasks_trace
- Explanation: call_rcu_tasks_trace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000073 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: clear_page_erms
- Explanation: clear_page_erms changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000074 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: clear_page_orig
- Explanation: clear_page_orig changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000075 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: clear_page_rep
- Explanation: clear_page_rep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000078 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: csum_ipv6_magic
- Explanation: csum_ipv6_magic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000079 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: dec_zone_state
- Explanation: dec_zone_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000085 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: devm_pinctrl_unregister
- Explanation: devm_pinctrl_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000095 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_gem_object_init_with_mnt
- Explanation: drm_gem_object_init_with_mnt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000096 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: dummy_sched_clock
- Explanation: dummy_sched_clock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000097 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: dummy_steal_clock
- Explanation: dummy_steal_clock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000101 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: folio_alloc_swap
- Explanation: folio_alloc_swap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000102 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: free_area_init
- Explanation: free_area_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000103 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: free_contig_range
- Explanation: free_contig_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000105 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: free_swap_and_cache_nr
- Explanation: free_swap_and_cache_nr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000112 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: get_netmem
- Explanation: get_netmem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000113 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: get_rcu_tasks_trace_gp_kthread
- Explanation: get_rcu_tasks_trace_gp_kthread changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000114 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: get_swap_page_of_type
- Explanation: get_swap_page_of_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000115 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: hex2bin
- Explanation: hex2bin changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000116 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: hex_to_bin
- Explanation: hex_to_bin changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000117 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: inc_node_state
- Explanation: inc_node_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000119 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: inode_update_timestamps
- Explanation: inode_update_timestamps changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000216 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: jiffies_to_msecs
- Explanation: jiffies_to_msecs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000217 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: jiffies_to_usecs
- Explanation: jiffies_to_usecs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000231 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: kthread_exit
- Explanation: kthread_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000233 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: laptop_io_completion
- Explanation: laptop_io_completion changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000234 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: laptop_mode_timer_fn
- Explanation: laptop_mode_timer_fn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000235 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: laptop_sync_completion
- Explanation: laptop_sync_completion changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000238 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mac_pton
- Explanation: mac_pton changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000240 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mas_expected_entries
- Explanation: mas_expected_entries changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000253 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: no_64bit_msi
- Explanation: no_64bit_msi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000256 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: offload_at_suspend
- Explanation: offload_at_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000261 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: paravirt_set_sched_clock
- Explanation: paravirt_set_sched_clock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000271 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_sfp_attach
- Explanation: phy_sfp_attach changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000272 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_sfp_connect_phy
- Explanation: phy_sfp_connect_phy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000273 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_sfp_detach
- Explanation: phy_sfp_detach changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000274 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_sfp_disconnect_phy
- Explanation: phy_sfp_disconnect_phy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000275 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_sfp_probe
- Explanation: phy_sfp_probe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000276 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_unregister_fixup
- Explanation: phy_unregister_fixup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000277 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_unregister_fixup_for_id
- Explanation: phy_unregister_fixup_for_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000278 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_unregister_fixup_for_uid
- Explanation: phy_unregister_fixup_for_uid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000279 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: pinconf_generic_dt_node_to_map_pinmux
- Explanation: pinconf_generic_dt_node_to_map_pinmux changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000289 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: put_netmem
- Explanation: put_netmem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000290 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: put_swap_folio
- Explanation: put_swap_folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000292 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: rcu_barrier_tasks_trace
- Explanation: rcu_barrier_tasks_trace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000293 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: rcu_read_unlock_trace_special
- Explanation: rcu_read_unlock_trace_special changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000294 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: rcu_tasks_trace_qs_blkd
- Explanation: rcu_tasks_trace_qs_blkd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000296 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: rcu_tasks_trace_torture_stats_print
- Explanation: rcu_tasks_trace_torture_stats_print changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000297 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: rcu_trc_cmpxchg_need_qs
- Explanation: rcu_trc_cmpxchg_need_qs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000302 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sched_mm_cid_fork
- Explanation: sched_mm_cid_fork changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000303 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: set_module_sig_enforced
- Explanation: set_module_sig_enforced changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000304 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: set_security_override_from_ctx
- Explanation: set_security_override_from_ctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000305 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: setup_percpu_irq
- Explanation: setup_percpu_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000310 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: simple_nosetlease
- Explanation: simple_nosetlease changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000322 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: swap_duplicate
- Explanation: swap_duplicate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000324 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: swap_free_nr
- Explanation: swap_free_nr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000326 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: swap_shmem_alloc
- Explanation: swap_shmem_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000327 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: swapcache_prepare
- Explanation: swapcache_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000328 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: synchronize_rcu_tasks_trace
- Explanation: synchronize_rcu_tasks_trace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000329 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sysctl_kern_to_user_uint_conv
- Explanation: sysctl_kern_to_user_uint_conv changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000340 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: unmap_vmas
- Explanation: unmap_vmas changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000343 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vma_mark_detached
- Explanation: vma_mark_detached changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000346 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: work_in_progress
- Explanation: work_in_progress changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000347 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: workqueue_unbound_exclude_cpumask
- Explanation: workqueue_unbound_exclude_cpumask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000560 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __tlb_remove_page_size
- Explanation: __tlb_remove_page_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mmu_gather *tlb', 'struct page *page', 'bool delay_rmap', 'int page_size'], 'return_type': 'extern bool'}`
- New: `{'params': ['struct mmu_gather *tlb', 'struct page *page', 'int page_size'], 'return_type': 'extern bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000561 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: acpi_processor_ffh_lpi_enter
- Explanation: acpi_processor_ffh_lpi_enter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct acpi_lpi_state *lpi'], 'return_type': 'extern int'}`
- New: `{'params': ['struct acpi_lpi_state *lpi'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000562 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: acpi_processor_ffh_lpi_probe
- Explanation: acpi_processor_ffh_lpi_probe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned int cpu'], 'return_type': 'extern int'}`
- New: `{'params': ['unsigned int cpu'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000563 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: acpi_processor_hotplug
- Explanation: acpi_processor_hotplug changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct acpi_processor *pr'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct acpi_processor *pr'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000564 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: acpi_processor_power_exit
- Explanation: acpi_processor_power_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct acpi_processor *pr'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct acpi_processor *pr'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000565 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: acpi_processor_power_init
- Explanation: acpi_processor_power_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct acpi_processor *pr'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct acpi_processor *pr'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000566 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: acpi_processor_power_state_has_changed
- Explanation: acpi_processor_power_state_has_changed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct acpi_processor *pr'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct acpi_processor *pr'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000568 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: aes_decrypt
- Explanation: aes_decrypt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct crypto_aes_ctx *ctx', 'u8 *out', 'const u8 *in'], 'return_type': 'void'}`
- New: `{'params': ['const struct aes_key *key', 'u8 out[at_least AES_BLOCK_SIZE]', 'const u8 in[at_least AES_BLOCK_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000569 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: aes_encrypt
- Explanation: aes_encrypt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct crypto_aes_ctx *ctx', 'u8 *out', 'const u8 *in'], 'return_type': 'void'}`
- New: `{'params': ['aes_encrypt_arg key', 'u8 out[at_least AES_BLOCK_SIZE]', 'const u8 in[at_least AES_BLOCK_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000570 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: aescfb_decrypt
- Explanation: aescfb_decrypt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct crypto_aes_ctx *ctx', 'u8 *dst', 'const u8 *src', 'int len', 'const u8 iv[AES_BLOCK_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['const struct aes_enckey *key', 'u8 *dst', 'const u8 *src', 'int len', 'const u8 iv[AES_BLOCK_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000571 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: aescfb_encrypt
- Explanation: aescfb_encrypt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct crypto_aes_ctx *ctx', 'u8 *dst', 'const u8 *src', 'int len', 'const u8 iv[AES_BLOCK_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['const struct aes_enckey *key', 'u8 *dst', 'const u8 *src', 'int len', 'const u8 iv[AES_BLOCK_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000572 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: af_alg_count_tsgl
- Explanation: af_alg_count_tsgl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct sock *sk', 'size_t bytes', 'size_t offset'], 'return_type': 'unsigned int'}`
- New: `{'params': ['struct sock *sk', 'size_t bytes'], 'return_type': 'unsigned int'}`

### Rust Evidence

- Graph edges: `0`

## W-000573 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: af_alg_pull_tsgl
- Explanation: af_alg_pull_tsgl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct sock *sk', 'size_t used', 'struct scatterlist *dst', 'size_t dst_offset'], 'return_type': 'void'}`
- New: `{'params': ['struct sock *sk', 'size_t used', 'struct scatterlist *dst'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000574 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: bitmap_intersects
- Explanation: bitmap_intersects changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['cpumask_bits(src1p)', 'cpumask_bits(src2p)', 'small_cpumask_bits'], 'return_type': 'return'}`
- New: `{'params': ['bitmap_to_test', 'bitmap', 'NUM_VMA_FLAG_BITS'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-000575 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: bitmap_subset
- Explanation: bitmap_subset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['cpumask_bits(src1p)', 'cpumask_bits(src2p)', 'small_cpumask_bits'], 'return_type': 'return'}`
- New: `{'params': ['bitmap_to_test', 'bitmap', 'NUM_VMA_FLAG_BITS'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-000576 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_acomp_unlock_stream_bh
- Explanation: crypto_acomp_unlock_stream_bh changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct crypto_acomp_stream *stream) __releases(stream'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct crypto_acomp_stream *stream) __releases(&stream->lock'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-000577 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_drbg_ctr_df
- Explanation: crypto_drbg_ctr_df changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct crypto_aes_ctx *aes', 'unsigned char *df_data', 'size_t bytes_to_return', 'struct list_head *seedlist', 'u8 blocklen_bytes', 'u8 statelen'], 'return_type': 'int'}`
- New: `{'params': ['struct aes_enckey *aes', 'unsigned char *df_data', 'size_t bytes_to_return', 'struct list_head *seedlist', 'u8 blocklen_bytes', 'u8 statelen'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000581 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_atomic_get_new_colorop_state
- Explanation: drm_atomic_get_new_colorop_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_atomic_state *state', 'struct drm_colorop *colorop'], 'return_type': 'static inline struct drm_colorop_state *'}`
- New: `{'params': ['struct drm_atomic_state *state', 'struct drm_colorop *colorop'], 'return_type': 'struct drm_colorop_state *'}`

### Rust Evidence

- Graph edges: `0`

## W-000582 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_atomic_get_old_colorop_state
- Explanation: drm_atomic_get_old_colorop_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_atomic_state *state', 'struct drm_colorop *colorop'], 'return_type': 'static inline struct drm_colorop_state *'}`
- New: `{'params': ['struct drm_atomic_state *state', 'struct drm_colorop *colorop'], 'return_type': 'struct drm_colorop_state *'}`

### Rust Evidence

- Graph edges: `0`

## W-000583 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_crtc_wait_one_vblank
- Explanation: drm_crtc_wait_one_vblank changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_crtc *crtc'], 'return_type': 'void'}`
- New: `{'params': ['struct drm_crtc *crtc'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000584 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_gpuva_init_from_op
- Explanation: drm_gpuva_init_from_op changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_gpuva *va', 'struct drm_gpuva_op_map *op'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct drm_gpuva *va', 'const struct drm_gpuva_op_map *op'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-000585 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_gpuva_map
- Explanation: drm_gpuva_map changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_gpuvm *gpuvm', 'struct drm_gpuva *va', 'struct drm_gpuva_op_map *op'], 'return_type': 'void'}`
- New: `{'params': ['struct drm_gpuvm *gpuvm', 'struct drm_gpuva *va', 'const struct drm_gpuva_op_map *op'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000586 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_gpuva_remap
- Explanation: drm_gpuva_remap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_gpuva *prev', 'struct drm_gpuva *next', 'struct drm_gpuva_op_remap *op'], 'return_type': 'void'}`
- New: `{'params': ['struct drm_gpuva *prev', 'struct drm_gpuva *next', 'const struct drm_gpuva_op_remap *op'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000587 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_gpuva_unmap
- Explanation: drm_gpuva_unmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_gpuva_op_unmap *op'], 'return_type': 'void'}`
- New: `{'params': ['const struct drm_gpuva_op_unmap *op'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000588 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_pagemap_migrate_to_devmem
- Explanation: drm_pagemap_migrate_to_devmem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_pagemap_devmem *devmem_allocation', 'struct mm_struct *mm', 'unsigned long start', 'unsigned long end', 'unsigned long timeslice_ms', 'void *pgmap_owner'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_pagemap_devmem *devmem_allocation', 'struct mm_struct *mm', 'unsigned long start', 'unsigned long end', 'const struct drm_pagemap_migrate_details *mdetails'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000589 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_property_replace_blob_from_id
- Explanation: drm_property_replace_blob_from_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_device *dev', 'struct drm_property_blob **blob', 'uint64_t blob_id', 'ssize_t expected_size', 'ssize_t expected_elem_size', 'bool *replaced'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_device *dev', 'struct drm_property_blob **blob', 'uint64_t blob_id', 'ssize_t expected_size', 'ssize_t expected_elem_size', 'ssize_t max_size', 'bool *replaced'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000593 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: is_shared_maywrite
- Explanation: is_shared_maywrite changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['vm_flags_t vm_flags'], 'return_type': 'static inline bool'}`
- New: `{'params': ['const vma_flags_t *flags'], 'return_type': 'static inline bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000594 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: jiffies_to_msecs
- Explanation: jiffies_to_msecs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['max(0L, delta)'], 'return_type': 'return'}`
- New: `{'params': ['const unsigned long j'], 'return_type': 'static inline unsigned int'}`

### Rust Evidence

- Graph edges: `0`

## W-000595 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: jiffies_to_usecs
- Explanation: jiffies_to_usecs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const unsigned long j'], 'return_type': 'extern unsigned int'}`
- New: `{'params': ['const unsigned long j'], 'return_type': 'static inline unsigned int'}`

### Rust Evidence

- Graph edges: `0`

## W-000601 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: resource_assigned
- Explanation: resource_assigned changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct resource *res'], 'return_type': 'static inline bool'}`
- New: `{'params': ['const struct resource *res'], 'return_type': 'static inline bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000357 FieldDrift

- Risk: Medium
- Score: 9.4
- Symbol: bpf_trampoline
- Explanation: bpf_trampoline changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'hlist', 'type': 'hlist_node'}, {'name': 'fops', 'type': '*mut ftrace_ops'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'refcnt', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'u32_'}, {'name': 'key', 'type': 'u64_'}, {'name': 'func', 'type': 'bpf_trampoline__bindgen_ty_1'}, {'name': 'extension_prog', 'type': '*mut bpf_prog'}, {'name': 'progs_hlist', 'type': '[hlist_head; 3usize]'}, {'name': 'progs_cnt', 'type': '[ffi::c_int; 3usize]'}, {'name': 'cur_image', 'type': '*mut bpf_tramp_image'}]`
- New: `[{'name': 'hlist_key', 'type': 'hlist_node'}, {'name': 'hlist_ip', 'type': 'hlist_node'}, {'name': 'fops', 'type': '*mut ftrace_ops'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'refcnt', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'u32_'}, {'name': 'key', 'type': 'u64_'}, {'name': 'ip', 'type': 'ffi::c_ulong'}, {'name': 'func', 'type': 'bpf_trampoline__bindgen_ty_1'}, {'name': 'extension_prog', 'type': '*mut bpf_prog'}, {'name': 'progs_hlist', 'type': '[hlist_head; 3usize]'}, {'name': 'progs_cnt', 'type': '[ffi::c_int; 3usize]'}, {'name': 'cur_image', 'type': '*mut bpf_tramp_image'}]`

### Rust Evidence

- Graph edges: `4`

## W-000382 FieldDrift

- Risk: Medium
- Score: 9.4
- Symbol: pci_host_bridge
- Explanation: pci_host_bridge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'dev', 'type': 'device'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'ops', 'type': '*mut pci_ops'}, {'name': 'child_ops', 'type': '*mut pci_ops'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'busnr', 'type': 'ffi::c_int'}, {'name': 'domain_nr', 'type': 'ffi::c_int'}, {'name': 'windows', 'type': 'list_head'}, {'name': 'dma_ranges', 'type': 'list_head'}, {'name': 'map_irq', 'type': '::core::option::Option<'}, {'name': 'release_fn', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut pci_host_bridge)>'}, {'name': 'enable_device', 'type': '::core::option::Option<'}, {'name': 'disable_device', 'type': '::core::option::Option<'}, {'name': 'release_data', 'type': '*mut ffi::c_void'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'align_resource', 'type': '::core::option::Option<'}, {'name': '__bindgen_padding_0', 'type': '[u64; 4usize]'}, {'name': 'private', 'type': '__IncompleteArrayField<ffi::c_ulong>'}]`
- New: `[{'name': 'dev', 'type': 'device'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'ops', 'type': '*mut pci_ops'}, {'name': 'child_ops', 'type': '*mut pci_ops'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'busnr', 'type': 'ffi::c_int'}, {'name': 'domain_nr', 'type': 'ffi::c_int'}, {'name': 'windows', 'type': 'list_head'}, {'name': 'dma_ranges', 'type': 'list_head'}, {'name': 'map_irq', 'type': '::core::option::Option<'}, {'name': 'release_fn', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut pci_host_bridge)>'}, {'name': 'enable_device', 'type': '::core::option::Option<'}, {'name': 'disable_device', 'type': '::core::option::Option<'}, {'name': 'release_data', 'type': '*mut ffi::c_void'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'align_resource', 'type': '::core::option::Option<'}, {'name': '__bindgen_padding_0', 'type': '[u64; 2usize]'}, {'name': 'private', 'type': '__IncompleteArrayField<ffi::c_ulong>'}]`

### Rust Evidence

- Graph edges: `4`

## W-000393 FieldDrift

- Risk: Medium
- Score: 9.4
- Symbol: sched_mm_cid
- Explanation: sched_mm_cid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'active', 'type': 'ffi::c_uint'}, {'name': 'cid', 'type': 'ffi::c_uint'}]`
- New: `[{'name': 'active', 'type': 'ffi::c_uint'}, {'name': 'cid', 'type': 'ffi::c_uint'}, {'name': 'node', 'type': 'hlist_node'}]`

### Rust Evidence

- Graph edges: `4`

## W-000360 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: dev_iommu
- Explanation: dev_iommu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'lock', 'type': 'mutex'}, {'name': 'fault_param', 'type': '*mut iommu_fault_param'}, {'name': 'fwspec', 'type': '*mut iommu_fwspec'}, {'name': 'iommu_dev', 'type': '*mut iommu_device'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'max_pasids', 'type': 'u32_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 3usize]'}]`

### Rust Evidence

- Graph edges: `2`

## W-000378 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: mm_struct__bindgen_ty_1
- Explanation: mm_struct__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'mm_struct__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mm_mt', 'type': 'maple_tree'}, {'name': 'mmap_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'task_size', 'type': 'ffi::c_ulong'}, {'name': 'pgd', 'type': '*mut pgd_t'}, {'name': 'membarrier_state', 'type': 'atomic_t'}, {'name': 'mm_users', 'type': 'atomic_t'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': 'mm_cid', 'type': 'mm_mm_cid'}, {'name': 'pgtables_bytes', 'type': 'atomic_long_t'}, {'name': 'map_count', 'type': 'ffi::c_int'}, {'name': 'page_table_lock', 'type': 'spinlock_t'}, {'name': 'mmap_lock', 'type': 'rw_semaphore'}, {'name': 'mmlist', 'type': 'list_head'}, {'name': 'vma_writer_wait', 'type': 'rcuwait'}, {'name': 'mm_lock_seq', 'type': 'seqcount_t'}, {'name': 'futex_hash_lock', 'type': 'mutex'}, {'name': 'futex_phash', 'type': '*mut futex_private_hash'}, {'name': 'futex_phash_new', 'type': '*mut futex_private_hash'}, {'name': 'futex_batches', 'type': 'ffi::c_ulong'}, {'name': 'futex_rcu', 'type': 'callback_head'}, {'name': 'futex_atomic', 'type': 'atomic_long_t'}, {'name': 'futex_ref', 'type': '*mut ffi::c_uint'}, {'name': 'hiwater_rss', 'type': 'ffi::c_ulong'}, {'name': 'hiwater_vm', 'type': 'ffi::c_ulong'}, {'name': 'total_vm', 'type': 'ffi::c_ulong'}, {'name': 'locked_vm', 'type': 'ffi::c_ulong'}, {'name': 'pinned_vm', 'type': 'atomic64_t'}, {'name': 'data_vm', 'type': 'ffi::c_ulong'}, {'name': 'exec_vm', 'type': 'ffi::c_ulong'}, {'name': 'stack_vm', 'type': 'ffi::c_ulong'}, {'name': 'def_flags', 'type': 'vm_flags_t'}, {'name': 'write_protect_seq', 'type': 'seqcount_t'}, {'name': 'arg_lock', 'type': 'spinlock_t'}, {'name': 'start_code', 'type': 'ffi::c_ulong'}, {'name': 'end_code', 'type': 'ffi::c_ulong'}, {'name': 'start_data', 'type': 'ffi::c_ulong'}, {'name': 'end_data', 'type': 'ffi::c_ulong'}, {'name': 'start_brk', 'type': 'ffi::c_ulong'}, {'name': 'brk', 'type': 'ffi::c_ulong'}, {'name': 'start_stack', 'type': 'ffi::c_ulong'}, {'name': 'arg_start', 'type': 'ffi::c_ulong'}, {'name': 'arg_end', 'type': 'ffi::c_ulong'}, {'name': 'env_start', 'type': 'ffi::c_ulong'}, {'name': 'env_end', 'type': 'ffi::c_ulong'}, {'name': 'saved_auxv', 'type': '[ffi::c_ulong; 52usize]'}, {'name': 'rss_stat', 'type': '[percpu_counter; 4usize]'}, {'name': 'binfmt', 'type': '*mut linux_binfmt'}, {'name': 'context', 'type': 'mm_context_t'}, {'name': 'flags', 'type': 'mm_flags_t'}, {'name': 'ioctx_lock', 'type': 'spinlock_t'}, {'name': 'ioctx_table', 'type': '*mut kioctx_table'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'exe_file', 'type': '*mut file'}, {'name': 'notifier_subscriptions', 'type': '*mut mmu_notifier_subscriptions'}, {'name': 'tlb_flush_pending', 'type': 'atomic_t'}, {'name': 'tlb_flush_batched', 'type': 'atomic_t'}, {'name': 'uprobes_state', 'type': 'uprobes_state'}, {'name': 'hugetlb_usage', 'type': 'atomic_long_t'}, {'name': 'async_put_work', 'type': 'work_struct'}, {'name': 'iommu_mm', 'type': '*mut iommu_mm_data'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'mm_struct__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mm_mt', 'type': 'maple_tree'}, {'name': 'mmap_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'task_size', 'type': 'ffi::c_ulong'}, {'name': 'pgd', 'type': '*mut pgd_t'}, {'name': 'membarrier_state', 'type': 'atomic_t'}, {'name': 'mm_users', 'type': 'atomic_t'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': 'mm_cid', 'type': 'mm_mm_cid'}, {'name': 'pgtables_bytes', 'type': 'atomic_long_t'}, {'name': 'map_count', 'type': 'ffi::c_int'}, {'name': 'page_table_lock', 'type': 'spinlock_t'}, {'name': 'mmap_lock', 'type': 'rw_semaphore'}, {'name': 'mmlist', 'type': 'list_head'}, {'name': 'vma_writer_wait', 'type': 'rcuwait'}, {'name': 'mm_lock_seq', 'type': 'seqcount_t'}, {'name': 'futex_hash_lock', 'type': 'mutex'}, {'name': 'futex_phash', 'type': '*mut futex_private_hash'}, {'name': 'futex_phash_new', 'type': '*mut futex_private_hash'}, {'name': 'futex_batches', 'type': 'ffi::c_ulong'}, {'name': 'futex_rcu', 'type': 'callback_head'}, {'name': 'futex_atomic', 'type': 'atomic_long_t'}, {'name': 'futex_ref', 'type': '*mut ffi::c_uint'}, {'name': 'hiwater_rss', 'type': 'ffi::c_ulong'}, {'name': 'hiwater_vm', 'type': 'ffi::c_ulong'}, {'name': 'total_vm', 'type': 'ffi::c_ulong'}, {'name': 'locked_vm', 'type': 'ffi::c_ulong'}, {'name': 'pinned_vm', 'type': 'atomic64_t'}, {'name': 'data_vm', 'type': 'ffi::c_ulong'}, {'name': 'exec_vm', 'type': 'ffi::c_ulong'}, {'name': 'stack_vm', 'type': 'ffi::c_ulong'}, {'name': 'def_flags', 'type': 'vm_flags_t'}, {'name': 'write_protect_seq', 'type': 'seqcount_t'}, {'name': 'arg_lock', 'type': 'spinlock_t'}, {'name': 'start_code', 'type': 'ffi::c_ulong'}, {'name': 'end_code', 'type': 'ffi::c_ulong'}, {'name': 'start_data', 'type': 'ffi::c_ulong'}, {'name': 'end_data', 'type': 'ffi::c_ulong'}, {'name': 'start_brk', 'type': 'ffi::c_ulong'}, {'name': 'brk', 'type': 'ffi::c_ulong'}, {'name': 'start_stack', 'type': 'ffi::c_ulong'}, {'name': 'arg_start', 'type': 'ffi::c_ulong'}, {'name': 'arg_end', 'type': 'ffi::c_ulong'}, {'name': 'env_start', 'type': 'ffi::c_ulong'}, {'name': 'env_end', 'type': 'ffi::c_ulong'}, {'name': 'saved_auxv', 'type': '[ffi::c_ulong; 56usize]'}, {'name': 'rss_stat', 'type': '[percpu_counter; 4usize]'}, {'name': 'binfmt', 'type': '*mut linux_binfmt'}, {'name': 'context', 'type': 'mm_context_t'}, {'name': 'flags', 'type': 'mm_flags_t'}, {'name': 'ioctx_lock', 'type': 'spinlock_t'}, {'name': 'ioctx_table', 'type': '*mut kioctx_table'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'exe_file', 'type': '*mut file'}, {'name': 'notifier_subscriptions', 'type': '*mut mmu_notifier_subscriptions'}, {'name': 'tlb_flush_pending', 'type': 'atomic_t'}, {'name': 'tlb_flush_batched', 'type': 'atomic_t'}, {'name': 'uprobes_state', 'type': 'uprobes_state'}, {'name': 'hugetlb_usage', 'type': 'atomic_long_t'}, {'name': 'async_put_work', 'type': 'work_struct'}, {'name': 'iommu_mm', 'type': '*mut iommu_mm_data'}]`

### Rust Evidence

- Graph edges: `2`

## W-000379 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: ns_common
- Explanation: ns_common changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'ns_type', 'type': 'u32_'}, {'name': 'stashed', 'type': '*mut dentry'}, {'name': 'ops', 'type': '*const proc_ns_operations'}, {'name': 'inum', 'type': 'ffi::c_uint'}, {'name': '__ns_ref', 'type': 'refcount_t'}, {'name': '__bindgen_anon_1', 'type': 'ns_common__bindgen_ty_1'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'ns_common__bindgen_ty_1'}, {'name': 'ns_type', 'type': 'u32_'}, {'name': 'stashed', 'type': '*mut dentry'}, {'name': 'ops', 'type': '*const proc_ns_operations'}, {'name': 'inum', 'type': 'ffi::c_uint'}, {'name': '__bindgen_anon_2', 'type': 'ns_common__bindgen_ty_2'}]`

### Rust Evidence

- Graph edges: `2`

## W-000349 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: acpi_madt_generic_interrupt
- Explanation: acpi_madt_generic_interrupt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'header', 'type': 'acpi_subtable_header'}, {'name': 'reserved', 'type': 'u16_'}, {'name': 'cpu_interface_number', 'type': 'u32_'}, {'name': 'uid', 'type': 'u32_'}, {'name': 'flags', 'type': 'u32_'}, {'name': 'parking_version', 'type': 'u32_'}, {'name': 'performance_interrupt', 'type': 'u32_'}, {'name': 'parked_address', 'type': 'u64_'}, {'name': 'base_address', 'type': 'u64_'}, {'name': 'gicv_base_address', 'type': 'u64_'}, {'name': 'gich_base_address', 'type': 'u64_'}, {'name': 'vgic_interrupt', 'type': 'u32_'}, {'name': 'gicr_base_address', 'type': 'u64_'}, {'name': 'arm_mpidr', 'type': 'u64_'}, {'name': 'efficiency_class', 'type': 'u8_'}, {'name': 'reserved2', 'type': '[u8_; 1usize]'}, {'name': 'spe_interrupt', 'type': 'u16_'}, {'name': 'trbe_interrupt', 'type': 'u16_'}]`
- New: `[{'name': 'header', 'type': 'acpi_subtable_header'}, {'name': 'reserved', 'type': 'u16_'}, {'name': 'cpu_interface_number', 'type': 'u32_'}, {'name': 'uid', 'type': 'u32_'}, {'name': 'flags', 'type': 'u32_'}, {'name': 'parking_version', 'type': 'u32_'}, {'name': 'performance_interrupt', 'type': 'u32_'}, {'name': 'parked_address', 'type': 'u64_'}, {'name': 'base_address', 'type': 'u64_'}, {'name': 'gicv_base_address', 'type': 'u64_'}, {'name': 'gich_base_address', 'type': 'u64_'}, {'name': 'vgic_interrupt', 'type': 'u32_'}, {'name': 'gicr_base_address', 'type': 'u64_'}, {'name': 'arm_mpidr', 'type': 'u64_'}, {'name': 'efficiency_class', 'type': 'u8_'}, {'name': 'reserved2', 'type': '[u8_; 1usize]'}, {'name': 'spe_interrupt', 'type': 'u16_'}, {'name': 'trbe_interrupt', 'type': 'u16_'}, {'name': 'iaffid', 'type': 'u16_'}, {'name': 'irs_id', 'type': 'u32_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000350 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: acpi_pptt_cache_v1
- Explanation: acpi_pptt_cache_v1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'cache_id', 'type': 'u32_'}]`
- New: `[{'name': 'header', 'type': 'acpi_subtable_header'}, {'name': 'reserved', 'type': 'u16_'}, {'name': 'flags', 'type': 'u32_'}, {'name': 'next_level_of_cache', 'type': 'u32_'}, {'name': 'size', 'type': 'u32_'}, {'name': 'number_of_sets', 'type': 'u32_'}, {'name': 'associativity', 'type': 'u8_'}, {'name': 'attributes', 'type': 'u8_'}, {'name': 'line_size', 'type': 'u16_'}, {'name': 'cache_id', 'type': 'u32_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000351 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: acpi_ras2_patrol_scrub_param
- Explanation: acpi_ras2_patrol_scrub_param changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'header', 'type': 'acpi_ras2_parameter_block'}, {'name': 'command', 'type': 'u16_'}, {'name': 'req_addr_range', 'type': '[u64_; 2usize]'}, {'name': 'actl_addr_range', 'type': '[u64_; 2usize]'}, {'name': 'flags', 'type': 'u32_'}, {'name': 'scrub_params_out', 'type': 'u32_'}, {'name': 'scrub_params_in', 'type': 'u32_'}]`
- New: `[{'name': 'header', 'type': 'acpi_ras2_parameter_block'}, {'name': 'command', 'type': 'u16_'}, {'name': 'req_addr_range', 'type': '[u64_; 2usize]'}, {'name': 'actl_addr_range', 'type': '[u64_; 2usize]'}, {'name': 'flags', 'type': 'u32_'}, {'name': 'scrub_params_out', 'type': 'u32_'}, {'name': 'scrub_params_in', 'type': 'u32_'}, {'name': 'ext_scrub_params', 'type': 'u32_'}, {'name': 'scrub_rate_desc', 'type': '[u8_; 256usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000352 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: backing_dev_info
- Explanation: backing_dev_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'id', 'type': 'u64_'}, {'name': 'rb_node', 'type': 'rb_node'}, {'name': 'bdi_list', 'type': 'list_head'}, {'name': 'ra_pages', 'type': 'ffi::c_ulong'}, {'name': 'io_pages', 'type': 'ffi::c_ulong'}, {'name': 'refcnt', 'type': 'kref'}, {'name': 'capabilities', 'type': 'ffi::c_uint'}, {'name': 'min_ratio', 'type': 'ffi::c_uint'}, {'name': 'max_ratio', 'type': 'ffi::c_uint'}, {'name': 'max_prop_frac', 'type': 'ffi::c_uint'}, {'name': 'tot_write_bandwidth', 'type': 'atomic_long_t'}, {'name': 'last_bdp_sleep', 'type': 'ffi::c_ulong'}, {'name': 'wb', 'type': 'bdi_writeback'}, {'name': 'wb_list', 'type': 'list_head'}, {'name': 'wb_waitq', 'type': 'wait_queue_head_t'}, {'name': 'dev', 'type': '*mut device'}, {'name': 'dev_name', 'type': '[ffi::c_char; 64usize]'}, {'name': 'owner', 'type': '*mut device'}, {'name': 'laptop_mode_wb_timer', 'type': 'timer_list'}, {'name': 'debug_dir', 'type': '*mut dentry'}]`
- New: `[{'name': 'id', 'type': 'u64_'}, {'name': 'rb_node', 'type': 'rb_node'}, {'name': 'bdi_list', 'type': 'list_head'}, {'name': 'ra_pages', 'type': 'ffi::c_ulong'}, {'name': 'io_pages', 'type': 'ffi::c_ulong'}, {'name': 'refcnt', 'type': 'kref'}, {'name': 'capabilities', 'type': 'ffi::c_uint'}, {'name': 'min_ratio', 'type': 'ffi::c_uint'}, {'name': 'max_ratio', 'type': 'ffi::c_uint'}, {'name': 'max_prop_frac', 'type': 'ffi::c_uint'}, {'name': 'tot_write_bandwidth', 'type': 'atomic_long_t'}, {'name': 'last_bdp_sleep', 'type': 'ffi::c_ulong'}, {'name': 'wb', 'type': 'bdi_writeback'}, {'name': 'wb_list', 'type': 'list_head'}, {'name': 'wb_waitq', 'type': 'wait_queue_head_t'}, {'name': 'dev', 'type': '*mut device'}, {'name': 'dev_name', 'type': '[ffi::c_char; 64usize]'}, {'name': 'owner', 'type': '*mut device'}, {'name': 'debug_dir', 'type': '*mut dentry'}]`

### Rust Evidence

- Graph edges: `1`

## W-000354 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bpf_map_owner
- Explanation: bpf_map_owner changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'type_', 'type': 'bpf_prog_type'}, {'name': 'jited', 'type': 'bool_'}, {'name': 'xdp_has_frags', 'type': 'bool_'}, {'name': 'storage_cookie', 'type': '[u64_; 2usize]'}, {'name': 'attach_func_proto', 'type': '*const btf_type'}, {'name': 'expected_attach_type', 'type': 'bpf_attach_type'}]`
- New: `[{'name': 'type_', 'type': 'bpf_prog_type'}, {'name': 'jited', 'type': 'bool_'}, {'name': 'xdp_has_frags', 'type': 'bool_'}, {'name': 'sleepable', 'type': 'bool_'}, {'name': 'storage_cookie', 'type': '[u64_; 2usize]'}, {'name': 'attach_func_proto', 'type': '*const btf_type'}, {'name': 'expected_attach_type', 'type': 'bpf_attach_type'}]`

### Rust Evidence

- Graph edges: `1`

## W-000356 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bpf_prog_aux
- Explanation: bpf_prog_aux changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'refcnt', 'type': 'atomic64_t'}, {'name': 'used_map_cnt', 'type': 'u32_'}, {'name': 'used_btf_cnt', 'type': 'u32_'}, {'name': 'max_ctx_offset', 'type': 'u32_'}, {'name': 'max_pkt_offset', 'type': 'u32_'}, {'name': 'max_tp_access', 'type': 'u32_'}, {'name': 'stack_depth', 'type': 'u32_'}, {'name': 'id', 'type': 'u32_'}, {'name': 'func_cnt', 'type': 'u32_'}, {'name': 'real_func_cnt', 'type': 'u32_'}, {'name': 'func_idx', 'type': 'u32_'}, {'name': 'attach_btf_id', 'type': 'u32_'}, {'name': 'attach_st_ops_member_off', 'type': 'u32_'}, {'name': 'ctx_arg_info_size', 'type': 'u32_'}, {'name': 'max_rdonly_access', 'type': 'u32_'}, {'name': 'max_rdwr_access', 'type': 'u32_'}, {'name': 'subprog_start', 'type': 'u32_'}, {'name': 'attach_btf', 'type': '*mut btf'}, {'name': 'ctx_arg_info', 'type': '*mut bpf_ctx_arg_aux'}, {'name': 'priv_stack_ptr', 'type': '*mut ffi::c_void'}, {'name': 'dst_mutex', 'type': 'mutex'}, {'name': 'dst_prog', 'type': '*mut bpf_prog'}, {'name': 'dst_trampoline', 'type': '*mut bpf_trampoline'}, {'name': 'saved_dst_prog_type', 'type': 'bpf_prog_type'}, {'name': 'saved_dst_attach_type', 'type': 'bpf_attach_type'}, {'name': 'verifier_zext', 'type': 'bool_'}, {'name': 'dev_bound', 'type': 'bool_'}, {'name': 'offload_requested', 'type': 'bool_'}, {'name': 'attach_btf_trace', 'type': 'bool_'}, {'name': 'attach_tracing_prog', 'type': 'bool_'}, {'name': 'func_proto_unreliable', 'type': 'bool_'}, {'name': 'tail_call_reachable', 'type': 'bool_'}, {'name': 'xdp_has_frags', 'type': 'bool_'}, {'name': 'exception_cb', 'type': 'bool_'}, {'name': 'exception_boundary', 'type': 'bool_'}, {'name': 'is_extended', 'type': 'bool_'}, {'name': 'jits_use_priv_stack', 'type': 'bool_'}, {'name': 'priv_stack_requested', 'type': 'bool_'}, {'name': 'changes_pkt_data', 'type': 'bool_'}, {'name': 'might_sleep', 'type': 'bool_'}, {'name': 'kprobe_write_ctx', 'type': 'bool_'}, {'name': 'prog_array_member_cnt', 'type': 'u64_'}, {'name': 'ext_mutex', 'type': 'mutex'}, {'name': 'arena', 'type': '*mut bpf_arena'}, {'name': 'recursion_detected', 'type': '::core::option::Option<unsafe extern "C" fn(prog: *mut bpf_prog)>'}, {'name': 'attach_func_proto', 'type': '*const btf_type'}, {'name': 'attach_func_name', 'type': '*const ffi::c_char'}, {'name': 'func', 'type': '*mut *mut bpf_prog'}, {'name': 'main_prog_aux', 'type': '*mut bpf_prog_aux'}, {'name': 'jit_data', 'type': '*mut ffi::c_void'}, {'name': 'poke_tab', 'type': '*mut bpf_jit_poke_descriptor'}, {'name': 'kfunc_tab', 'type': '*mut bpf_kfunc_desc_tab'}, {'name': 'kfunc_btf_tab', 'type': '*mut bpf_kfunc_btf_tab'}, {'name': 'size_poke_tab', 'type': 'u32_'}, {'name': 'ksym', 'type': 'bpf_ksym'}, {'name': 'ops', 'type': '*const bpf_prog_ops'}, {'name': 'st_ops', 'type': '*const bpf_struct_ops'}, {'name': 'used_maps', 'type': '*mut *mut bpf_map'}, {'name': 'used_maps_mutex', 'type': 'mutex'}, {'name': 'used_btfs', 'type': '*mut btf_mod_pair'}, {'name': 'prog', 'type': '*mut bpf_prog'}, {'name': 'user', 'type': '*mut user_struct'}, {'name': 'load_time', 'type': 'u64_'}, {'name': 'verified_insns', 'type': 'u32_'}, {'name': 'cgroup_atype', 'type': 'ffi::c_int'}, {'name': 'cgroup_storage', 'type': '[*mut bpf_map; 2usize]'}, {'name': 'name', 'type': '[ffi::c_char; 16usize]'}, {'name': 'bpf_exception_cb', 'type': '::core::option::Option<'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'token', 'type': '*mut bpf_token'}, {'name': 'offload', 'type': '*mut bpf_prog_offload'}, {'name': 'btf', 'type': '*mut btf'}, {'name': 'func_info', 'type': '*mut bpf_func_info'}, {'name': 'func_info_aux', 'type': '*mut bpf_func_info_aux'}, {'name': 'linfo', 'type': '*mut bpf_line_info'}, {'name': 'jited_linfo', 'type': '*mut *mut ffi::c_void'}, {'name': 'func_info_cnt', 'type': 'u32_'}, {'name': 'nr_linfo', 'type': 'u32_'}, {'name': 'linfo_idx', 'type': 'u32_'}, {'name': 'mod_', 'type': '*mut module'}, {'name': 'num_exentries', 'type': 'u32_'}, {'name': 'extable', 'type': '*mut exception_table_entry'}, {'name': '__bindgen_anon_1', 'type': 'bpf_prog_aux__bindgen_ty_1'}, {'name': 'stream', 'type': '[bpf_stream; 2usize]'}]`
- New: `[{'name': 'refcnt', 'type': 'atomic64_t'}, {'name': 'used_map_cnt', 'type': 'u32_'}, {'name': 'used_btf_cnt', 'type': 'u32_'}, {'name': 'max_ctx_offset', 'type': 'u32_'}, {'name': 'max_pkt_offset', 'type': 'u32_'}, {'name': 'max_tp_access', 'type': 'u32_'}, {'name': 'stack_depth', 'type': 'u32_'}, {'name': 'id', 'type': 'u32_'}, {'name': 'func_cnt', 'type': 'u32_'}, {'name': 'real_func_cnt', 'type': 'u32_'}, {'name': 'func_idx', 'type': 'u32_'}, {'name': 'attach_btf_id', 'type': 'u32_'}, {'name': 'attach_st_ops_member_off', 'type': 'u32_'}, {'name': 'ctx_arg_info_size', 'type': 'u32_'}, {'name': 'max_rdonly_access', 'type': 'u32_'}, {'name': 'max_rdwr_access', 'type': 'u32_'}, {'name': 'subprog_start', 'type': 'u32_'}, {'name': 'attach_btf', 'type': '*mut btf'}, {'name': 'ctx_arg_info', 'type': '*mut bpf_ctx_arg_aux'}, {'name': 'priv_stack_ptr', 'type': '*mut ffi::c_void'}, {'name': 'dst_mutex', 'type': 'mutex'}, {'name': 'dst_prog', 'type': '*mut bpf_prog'}, {'name': 'dst_trampoline', 'type': '*mut bpf_trampoline'}, {'name': 'saved_dst_prog_type', 'type': 'bpf_prog_type'}, {'name': 'saved_dst_attach_type', 'type': 'bpf_attach_type'}, {'name': 'verifier_zext', 'type': 'bool_'}, {'name': 'dev_bound', 'type': 'bool_'}, {'name': 'offload_requested', 'type': 'bool_'}, {'name': 'attach_btf_trace', 'type': 'bool_'}, {'name': 'attach_tracing_prog', 'type': 'bool_'}, {'name': 'func_proto_unreliable', 'type': 'bool_'}, {'name': 'tail_call_reachable', 'type': 'bool_'}, {'name': 'xdp_has_frags', 'type': 'bool_'}, {'name': 'exception_cb', 'type': 'bool_'}, {'name': 'exception_boundary', 'type': 'bool_'}, {'name': 'is_extended', 'type': 'bool_'}, {'name': 'jits_use_priv_stack', 'type': 'bool_'}, {'name': 'priv_stack_requested', 'type': 'bool_'}, {'name': 'changes_pkt_data', 'type': 'bool_'}, {'name': 'might_sleep', 'type': 'bool_'}, {'name': 'kprobe_write_ctx', 'type': 'bool_'}, {'name': 'prog_array_member_cnt', 'type': 'u64_'}, {'name': 'ext_mutex', 'type': 'mutex'}, {'name': 'arena', 'type': '*mut bpf_arena'}, {'name': 'recursion_detected', 'type': '::core::option::Option<unsafe extern "C" fn(prog: *mut bpf_prog)>'}, {'name': 'attach_func_proto', 'type': '*const btf_type'}, {'name': 'attach_func_name', 'type': '*const ffi::c_char'}, {'name': 'func', 'type': '*mut *mut bpf_prog'}, {'name': 'main_prog_aux', 'type': '*mut bpf_prog_aux'}, {'name': 'jit_data', 'type': '*mut ffi::c_void'}, {'name': 'poke_tab', 'type': '*mut bpf_jit_poke_descriptor'}, {'name': 'kfunc_tab', 'type': '*mut bpf_kfunc_desc_tab'}, {'name': 'kfunc_btf_tab', 'type': '*mut bpf_kfunc_btf_tab'}, {'name': 'size_poke_tab', 'type': 'u32_'}, {'name': 'ksym', 'type': 'bpf_ksym'}, {'name': 'ops', 'type': '*const bpf_prog_ops'}, {'name': 'st_ops', 'type': '*const bpf_struct_ops'}, {'name': 'used_maps', 'type': '*mut *mut bpf_map'}, {'name': 'used_maps_mutex', 'type': 'mutex'}, {'name': 'used_btfs', 'type': '*mut btf_mod_pair'}, {'name': 'prog', 'type': '*mut bpf_prog'}, {'name': 'user', 'type': '*mut user_struct'}, {'name': 'load_time', 'type': 'u64_'}, {'name': 'verified_insns', 'type': 'u32_'}, {'name': 'cgroup_atype', 'type': 'ffi::c_int'}, {'name': 'cgroup_storage', 'type': '[*mut bpf_map; 2usize]'}, {'name': 'name', 'type': '[ffi::c_char; 16usize]'}, {'name': 'bpf_exception_cb', 'type': '::core::option::Option<'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'token', 'type': '*mut bpf_token'}, {'name': 'offload', 'type': '*mut bpf_prog_offload'}, {'name': 'btf', 'type': '*mut btf'}, {'name': 'func_info', 'type': '*mut bpf_func_info'}, {'name': 'func_info_aux', 'type': '*mut bpf_func_info_aux'}, {'name': 'linfo', 'type': '*mut bpf_line_info'}, {'name': 'jited_linfo', 'type': '*mut *mut ffi::c_void'}, {'name': 'func_info_cnt', 'type': 'u32_'}, {'name': 'nr_linfo', 'type': 'u32_'}, {'name': 'linfo_idx', 'type': 'u32_'}, {'name': 'mod_', 'type': '*mut module'}, {'name': 'num_exentries', 'type': 'u32_'}, {'name': 'extable', 'type': '*mut exception_table_entry'}, {'name': '__bindgen_anon_1', 'type': 'bpf_prog_aux__bindgen_ty_1'}, {'name': 'stream', 'type': '[bpf_stream; 2usize]'}, {'name': 'st_ops_assoc_mutex', 'type': 'mutex'}, {'name': 'st_ops_assoc', 'type': '*mut bpf_map'}]`

### Rust Evidence

- Graph edges: `1`

## W-000358 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bus_type
- Explanation: bus_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'dev_name', 'type': '*const ffi::c_char'}, {'name': 'bus_groups', 'type': '*mut *const attribute_group'}, {'name': 'dev_groups', 'type': '*mut *const attribute_group'}, {'name': 'drv_groups', 'type': '*mut *const attribute_group'}, {'name': 'match_', 'type': '::core::option::Option<'}, {'name': 'uevent', 'type': '::core::option::Option<'}, {'name': 'probe', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'sync_state', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'remove', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'shutdown', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'irq_get_affinity', 'type': '::core::option::Option<'}, {'name': 'online', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'offline', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'suspend', 'type': '::core::option::Option<'}, {'name': 'resume', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'num_vf', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'dma_configure', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'dma_cleanup', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'pm', 'type': '*const dev_pm_ops'}, {'name': 'need_parent_lock', 'type': 'bool_'}]`
- New: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'dev_name', 'type': '*const ffi::c_char'}, {'name': 'bus_groups', 'type': '*mut *const attribute_group'}, {'name': 'dev_groups', 'type': '*mut *const attribute_group'}, {'name': 'drv_groups', 'type': '*mut *const attribute_group'}, {'name': 'match_', 'type': '::core::option::Option<'}, {'name': 'uevent', 'type': '::core::option::Option<'}, {'name': 'probe', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'sync_state', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'remove', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'shutdown', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'irq_get_affinity', 'type': '::core::option::Option<'}, {'name': 'online', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'offline', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'suspend', 'type': '::core::option::Option<'}, {'name': 'resume', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'num_vf', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'dma_configure', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'dma_cleanup', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'pm', 'type': '*const dev_pm_ops'}, {'name': 'driver_override', 'type': 'bool_'}, {'name': 'need_parent_lock', 'type': 'bool_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000361 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: dev_pm_info
- Explanation: dev_pm_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'power_state', 'type': 'pm_message_t'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'driver_flags', 'type': 'u32_'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'entry', 'type': 'list_head'}, {'name': 'completion', 'type': 'completion'}, {'name': 'wakeup', 'type': '*mut wakeup_source'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'suspend_timer', 'type': 'hrtimer'}, {'name': 'timer_expires', 'type': 'u64_'}, {'name': 'work', 'type': 'work_struct'}, {'name': 'wait_queue', 'type': 'wait_queue_head_t'}, {'name': 'wakeirq', 'type': '*mut wake_irq'}, {'name': 'usage_count', 'type': 'atomic_t'}, {'name': 'child_count', 'type': 'atomic_t'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'links_count', 'type': 'ffi::c_uint'}, {'name': 'request', 'type': 'rpm_request'}, {'name': 'runtime_status', 'type': 'rpm_status'}, {'name': 'last_status', 'type': 'rpm_status'}, {'name': 'runtime_error', 'type': 'ffi::c_int'}, {'name': 'autosuspend_delay', 'type': 'ffi::c_int'}, {'name': 'last_busy', 'type': 'u64_'}, {'name': 'active_time', 'type': 'u64_'}, {'name': 'suspended_time', 'type': 'u64_'}, {'name': 'accounting_timestamp', 'type': 'u64_'}, {'name': 'subsys_data', 'type': '*mut pm_subsys_data'}, {'name': 'qos', 'type': '*mut dev_pm_qos'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 7usize]'}]`
- New: `[{'name': 'power_state', 'type': 'pm_message_t'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'driver_flags', 'type': 'u32_'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'entry', 'type': 'list_head'}, {'name': 'completion', 'type': 'completion'}, {'name': 'wakeup', 'type': '*mut wakeup_source'}, {'name': 'work_in_progress', 'type': 'bool_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'suspend_timer', 'type': 'hrtimer'}, {'name': 'timer_expires', 'type': 'u64_'}, {'name': 'work', 'type': 'work_struct'}, {'name': 'wait_queue', 'type': 'wait_queue_head_t'}, {'name': 'wakeirq', 'type': '*mut wake_irq'}, {'name': 'usage_count', 'type': 'atomic_t'}, {'name': 'child_count', 'type': 'atomic_t'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'links_count', 'type': 'ffi::c_uint'}, {'name': 'request', 'type': 'rpm_request'}, {'name': 'runtime_status', 'type': 'rpm_status'}, {'name': 'last_status', 'type': 'rpm_status'}, {'name': 'runtime_error', 'type': 'ffi::c_int'}, {'name': 'autosuspend_delay', 'type': 'ffi::c_int'}, {'name': 'last_busy', 'type': 'u64_'}, {'name': 'active_time', 'type': 'u64_'}, {'name': 'suspended_time', 'type': 'u64_'}, {'name': 'accounting_timestamp', 'type': 'u64_'}, {'name': 'subsys_data', 'type': '*mut pm_subsys_data'}, {'name': 'qos', 'type': '*mut dev_pm_qos'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 7usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000364 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: file_system_type
- Explanation: file_system_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'fs_flags', 'type': 'ffi::c_int'}, {'name': 'parameters', 'type': '*const fs_parameter_spec'}, {'name': 'mount', 'type': '::core::option::Option<'}, {'name': 'kill_sb', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut super_block)>'}, {'name': 'owner', 'type': '*mut module'}, {'name': 'next', 'type': '*mut file_system_type'}, {'name': 'fs_supers', 'type': 'hlist_head'}, {'name': 's_lock_key', 'type': 'lock_class_key'}, {'name': 's_umount_key', 'type': 'lock_class_key'}, {'name': 's_vfs_rename_key', 'type': 'lock_class_key'}, {'name': 's_writers_key', 'type': '[lock_class_key; 3usize]'}, {'name': 'i_lock_key', 'type': 'lock_class_key'}, {'name': 'i_mutex_key', 'type': 'lock_class_key'}, {'name': 'invalidate_lock_key', 'type': 'lock_class_key'}, {'name': 'i_mutex_dir_key', 'type': 'lock_class_key'}]`
- New: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'fs_flags', 'type': 'ffi::c_int'}, {'name': 'parameters', 'type': '*const fs_parameter_spec'}, {'name': 'kill_sb', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut super_block)>'}, {'name': 'owner', 'type': '*mut module'}, {'name': 'next', 'type': '*mut file_system_type'}, {'name': 'fs_supers', 'type': 'hlist_head'}, {'name': 's_lock_key', 'type': 'lock_class_key'}, {'name': 's_umount_key', 'type': 'lock_class_key'}, {'name': 's_vfs_rename_key', 'type': 'lock_class_key'}, {'name': 's_writers_key', 'type': '[lock_class_key; 3usize]'}, {'name': 'i_lock_key', 'type': 'lock_class_key'}, {'name': 'i_mutex_key', 'type': 'lock_class_key'}, {'name': 'invalidate_lock_key', 'type': 'lock_class_key'}, {'name': 'i_mutex_dir_key', 'type': 'lock_class_key'}]`

### Rust Evidence

- Graph edges: `1`

## W-000365 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: filename
- Explanation: filename changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'uptr', 'type': '*const ffi::c_char'}, {'name': 'refcnt', 'type': 'atomic_t'}, {'name': 'aname', 'type': '*mut audit_names'}, {'name': 'iname', 'type': '__IncompleteArrayField<ffi::c_char>'}]`
- New: `[{'name': '__bindgen_padding_0', 'type': '[u8; 24usize]'}, {'name': 'iname', 'type': '[ffi::c_char; 168usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000366 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: inode_operations
- Explanation: inode_operations changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'lookup', 'type': '::core::option::Option<'}, {'name': 'get_link', 'type': '::core::option::Option<'}, {'name': 'permission', 'type': '::core::option::Option<'}, {'name': 'get_inode_acl', 'type': '::core::option::Option<'}, {'name': 'readlink', 'type': '::core::option::Option<'}, {'name': 'create', 'type': '::core::option::Option<'}, {'name': 'link', 'type': '::core::option::Option<'}, {'name': 'unlink', 'type': '::core::option::Option<'}, {'name': 'symlink', 'type': '::core::option::Option<'}, {'name': 'mkdir', 'type': '::core::option::Option<'}, {'name': 'rmdir', 'type': '::core::option::Option<'}, {'name': 'mknod', 'type': '::core::option::Option<'}, {'name': 'rename', 'type': '::core::option::Option<'}, {'name': 'setattr', 'type': '::core::option::Option<'}, {'name': 'getattr', 'type': '::core::option::Option<'}, {'name': 'listxattr', 'type': '::core::option::Option<'}, {'name': 'fiemap', 'type': '::core::option::Option<'}, {'name': 'update_time', 'type': '::core::option::Option<'}, {'name': 'atomic_open', 'type': '::core::option::Option<'}, {'name': 'tmpfile', 'type': '::core::option::Option<'}, {'name': 'get_acl', 'type': '::core::option::Option<'}, {'name': 'set_acl', 'type': '::core::option::Option<'}, {'name': 'fileattr_set', 'type': '::core::option::Option<'}, {'name': 'fileattr_get', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'lookup', 'type': '::core::option::Option<'}, {'name': 'get_link', 'type': '::core::option::Option<'}, {'name': 'permission', 'type': '::core::option::Option<'}, {'name': 'get_inode_acl', 'type': '::core::option::Option<'}, {'name': 'readlink', 'type': '::core::option::Option<'}, {'name': 'create', 'type': '::core::option::Option<'}, {'name': 'link', 'type': '::core::option::Option<'}, {'name': 'unlink', 'type': '::core::option::Option<'}, {'name': 'symlink', 'type': '::core::option::Option<'}, {'name': 'mkdir', 'type': '::core::option::Option<'}, {'name': 'rmdir', 'type': '::core::option::Option<'}, {'name': 'mknod', 'type': '::core::option::Option<'}, {'name': 'rename', 'type': '::core::option::Option<'}, {'name': 'setattr', 'type': '::core::option::Option<'}, {'name': 'getattr', 'type': '::core::option::Option<'}, {'name': 'listxattr', 'type': '::core::option::Option<'}, {'name': 'fiemap', 'type': '::core::option::Option<'}, {'name': 'update_time', 'type': '::core::option::Option<'}, {'name': 'sync_lazytime', 'type': '::core::option::Option<unsafe extern "C" fn(inode: *mut inode)>'}, {'name': 'atomic_open', 'type': '::core::option::Option<'}, {'name': 'tmpfile', 'type': '::core::option::Option<'}, {'name': 'get_acl', 'type': '::core::option::Option<'}, {'name': 'set_acl', 'type': '::core::option::Option<'}, {'name': 'fileattr_set', 'type': '::core::option::Option<'}, {'name': 'fileattr_get', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-000368 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: iommu_mm_data
- Explanation: iommu_mm_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'pasid', 'type': 'u32_'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'sva_domains', 'type': 'list_head'}, {'name': 'mm_list_elm', 'type': 'list_head'}]`

### Rust Evidence

- Graph edges: `1`

## W-000369 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: iommu_ops
- Explanation: iommu_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'hw_info', 'type': '::core::option::Option<'}, {'name': 'domain_alloc_paging_flags', 'type': '::core::option::Option<'}, {'name': 'domain_alloc_sva', 'type': '::core::option::Option<'}, {'name': 'domain_alloc_nested', 'type': '::core::option::Option<'}, {'name': 'release_device', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'probe_finalize', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'of_xlate', 'type': '::core::option::Option<'}, {'name': 'is_attach_deferred', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> bool_>'}, {'name': 'page_response', 'type': '::core::option::Option<'}, {'name': 'get_viommu_size', 'type': '::core::option::Option<'}, {'name': 'viommu_init', 'type': '::core::option::Option<'}, {'name': 'default_domain_ops', 'type': '*const iommu_domain_ops'}, {'name': 'owner', 'type': '*mut module'}, {'name': 'identity_domain', 'type': '*mut iommu_domain'}, {'name': 'blocked_domain', 'type': '*mut iommu_domain'}, {'name': 'release_domain', 'type': '*mut iommu_domain'}, {'name': 'default_domain', 'type': '*mut iommu_domain'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 7usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000371 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: irq_desc
- Explanation: irq_desc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'irq_common_data', 'type': 'irq_common_data'}, {'name': 'irq_data', 'type': 'irq_data'}, {'name': 'kstat_irqs', 'type': '*mut irqstat'}, {'name': 'handle_irq', 'type': 'irq_flow_handler_t'}, {'name': 'action', 'type': '*mut irqaction'}, {'name': 'status_use_accessors', 'type': 'ffi::c_uint'}, {'name': 'core_internal_state__do_not_mess_with_it', 'type': 'ffi::c_uint'}, {'name': 'depth', 'type': 'ffi::c_uint'}, {'name': 'wake_depth', 'type': 'ffi::c_uint'}, {'name': 'tot_count', 'type': 'ffi::c_uint'}, {'name': 'irq_count', 'type': 'ffi::c_uint'}, {'name': 'last_unhandled', 'type': 'ffi::c_ulong'}, {'name': 'irqs_unhandled', 'type': 'ffi::c_uint'}, {'name': 'threads_handled', 'type': 'atomic_t'}, {'name': 'threads_handled_last', 'type': 'ffi::c_int'}, {'name': 'lock', 'type': 'raw_spinlock_t'}, {'name': 'percpu_enabled', 'type': '*mut cpumask'}, {'name': 'affinity_hint', 'type': '*const cpumask'}, {'name': 'affinity_notify', 'type': '*mut irq_affinity_notify'}, {'name': 'pending_mask', 'type': 'cpumask_var_t'}, {'name': 'threads_oneshot', 'type': 'ffi::c_ulong'}, {'name': 'threads_active', 'type': 'atomic_t'}, {'name': 'wait_for_threads', 'type': 'wait_queue_head_t'}, {'name': 'nr_actions', 'type': 'ffi::c_uint'}, {'name': 'no_suspend_depth', 'type': 'ffi::c_uint'}, {'name': 'cond_suspend_depth', 'type': 'ffi::c_uint'}, {'name': 'force_resume_depth', 'type': 'ffi::c_uint'}, {'name': 'dir', 'type': '*mut proc_dir_entry'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'kobj', 'type': 'kobject'}, {'name': 'request_mutex', 'type': 'mutex'}, {'name': 'parent_irq', 'type': 'ffi::c_int'}, {'name': 'owner', 'type': '*mut module'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'resend_node', 'type': 'hlist_node'}]`
- New: `[{'name': 'irq_common_data', 'type': 'irq_common_data'}, {'name': 'irq_data', 'type': 'irq_data'}, {'name': 'kstat_irqs', 'type': '*mut irqstat'}, {'name': 'handle_irq', 'type': 'irq_flow_handler_t'}, {'name': 'action', 'type': '*mut irqaction'}, {'name': 'status_use_accessors', 'type': 'ffi::c_uint'}, {'name': 'core_internal_state__do_not_mess_with_it', 'type': 'ffi::c_uint'}, {'name': 'depth', 'type': 'ffi::c_uint'}, {'name': 'wake_depth', 'type': 'ffi::c_uint'}, {'name': 'tot_count', 'type': 'ffi::c_uint'}, {'name': 'irq_count', 'type': 'ffi::c_uint'}, {'name': 'last_unhandled', 'type': 'ffi::c_ulong'}, {'name': 'irqs_unhandled', 'type': 'ffi::c_uint'}, {'name': 'threads_handled', 'type': 'atomic_t'}, {'name': 'threads_handled_last', 'type': 'ffi::c_int'}, {'name': 'lock', 'type': 'raw_spinlock_t'}, {'name': 'percpu_enabled', 'type': '*mut cpumask'}, {'name': 'redirect', 'type': 'irq_redirect'}, {'name': 'affinity_hint', 'type': '*const cpumask'}, {'name': 'affinity_notify', 'type': '*mut irq_affinity_notify'}, {'name': 'pending_mask', 'type': 'cpumask_var_t'}, {'name': 'threads_oneshot', 'type': 'ffi::c_ulong'}, {'name': 'threads_active', 'type': 'atomic_t'}, {'name': 'wait_for_threads', 'type': 'wait_queue_head_t'}, {'name': 'nr_actions', 'type': 'ffi::c_uint'}, {'name': 'no_suspend_depth', 'type': 'ffi::c_uint'}, {'name': 'cond_suspend_depth', 'type': 'ffi::c_uint'}, {'name': 'force_resume_depth', 'type': 'ffi::c_uint'}, {'name': 'dir', 'type': '*mut proc_dir_entry'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'kobj', 'type': 'kobject'}, {'name': 'request_mutex', 'type': 'mutex'}, {'name': 'parent_irq', 'type': 'ffi::c_int'}, {'name': 'owner', 'type': '*mut module'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'resend_node', 'type': 'hlist_node'}]`

### Rust Evidence

- Graph edges: `1`

## W-000372 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: kernfs_fs_context
- Explanation: kernfs_fs_context changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'root', 'type': '*mut kernfs_root'}, {'name': 'ns_tag', 'type': '*mut ffi::c_void'}, {'name': 'magic', 'type': 'ffi::c_ulong'}, {'name': 'new_sb_created', 'type': 'bool_'}]`
- New: `[{'name': 'root', 'type': '*mut kernfs_root'}, {'name': 'ns_tag', 'type': '*mut ns_common'}, {'name': 'magic', 'type': 'ffi::c_ulong'}, {'name': 'new_sb_created', 'type': 'bool_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000374 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: kobj_ns_type_operations
- Explanation: kobj_ns_type_operations changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'type_', 'type': 'kobj_ns_type'}, {'name': 'current_may_mount', 'type': '::core::option::Option<unsafe extern "C" fn() -> bool_>'}, {'name': 'grab_current_ns', 'type': '::core::option::Option<unsafe extern "C" fn() -> *mut ffi::c_void>'}, {'name': 'initial_ns', 'type': '::core::option::Option<unsafe extern "C" fn() -> *const ffi::c_void>'}, {'name': 'drop_ns', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut ffi::c_void)>'}]`
- New: `[{'name': 'type_', 'type': 'kobj_ns_type'}, {'name': 'current_may_mount', 'type': '::core::option::Option<unsafe extern "C" fn() -> bool_>'}, {'name': 'grab_current_ns', 'type': '::core::option::Option<unsafe extern "C" fn() -> *mut ns_common>'}, {'name': 'netlink_ns', 'type': '::core::option::Option<unsafe extern "C" fn(sk: *mut sock) -> *const ns_common>'}, {'name': 'initial_ns', 'type': '::core::option::Option<unsafe extern "C" fn() -> *const ns_common>'}, {'name': 'drop_ns', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut ns_common)>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000375 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: link_mode_info
- Explanation: link_mode_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'speed', 'type': 'ffi::c_int'}, {'name': 'lanes', 'type': 'u8_'}, {'name': 'duplex', 'type': 'u8_'}]`
- New: `[{'name': 'speed', 'type': 'ffi::c_int'}, {'name': 'lanes', 'type': 'u8_'}, {'name': 'min_pairs', 'type': 'u8_'}, {'name': 'pairs', 'type': 'u8_'}, {'name': 'duplex', 'type': 'u8_'}, {'name': 'mediums', 'type': 'u16_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000377 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: mm_mm_cid
- Explanation: mm_mm_cid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'pcpu', 'type': '*mut mm_cid_pcpu'}, {'name': 'mode', 'type': 'ffi::c_uint'}, {'name': 'max_cids', 'type': 'ffi::c_uint'}, {'name': 'irq_work', 'type': 'irq_work'}, {'name': 'work', 'type': 'work_struct'}, {'name': 'lock', 'type': 'raw_spinlock_t'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_uint'}, {'name': 'users', 'type': 'ffi::c_uint'}, {'name': 'pcpu_thrs', 'type': 'ffi::c_uint'}, {'name': 'update_deferred', 'type': 'ffi::c_uint'}]`
- New: `[{'name': 'pcpu', 'type': '*mut mm_cid_pcpu'}, {'name': 'mode', 'type': 'ffi::c_uint'}, {'name': 'max_cids', 'type': 'ffi::c_uint'}, {'name': 'irq_work', 'type': 'irq_work'}, {'name': 'work', 'type': 'work_struct'}, {'name': 'lock', 'type': 'raw_spinlock_t'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'user_list', 'type': 'hlist_head'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_uint'}, {'name': 'users', 'type': 'ffi::c_uint'}, {'name': 'pcpu_thrs', 'type': 'ffi::c_uint'}, {'name': 'update_deferred', 'type': 'ffi::c_uint'}]`

### Rust Evidence

- Graph edges: `1`

## W-000380 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: paravirt_patch_template
- Explanation: paravirt_patch_template changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'cpu', 'type': 'pv_cpu_ops'}, {'name': 'irq', 'type': 'pv_irq_ops'}, {'name': 'mmu', 'type': 'pv_mmu_ops'}, {'name': 'lock', 'type': 'pv_lock_ops'}]`
- New: `[{'name': 'cpu', 'type': 'pv_cpu_ops'}, {'name': 'irq', 'type': 'pv_irq_ops'}, {'name': 'mmu', 'type': 'pv_mmu_ops'}]`

### Rust Evidence

- Graph edges: `1`

## W-000383 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: pci_ops
- Explanation: pci_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'add_bus', 'type': '::core::option::Option<unsafe extern "C" fn(bus: *mut pci_bus) -> ffi::c_int>'}, {'name': 'remove_bus', 'type': '::core::option::Option<unsafe extern "C" fn(bus: *mut pci_bus)>'}, {'name': 'map_bus', 'type': '::core::option::Option<'}, {'name': 'read', 'type': '::core::option::Option<'}, {'name': 'write', 'type': '::core::option::Option<'}, {'name': 'assert_perst', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'add_bus', 'type': '::core::option::Option<unsafe extern "C" fn(bus: *mut pci_bus) -> ffi::c_int>'}, {'name': 'remove_bus', 'type': '::core::option::Option<unsafe extern "C" fn(bus: *mut pci_bus)>'}, {'name': 'map_bus', 'type': '::core::option::Option<'}, {'name': 'read', 'type': '::core::option::Option<'}, {'name': 'write', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-000386 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: pid__bindgen_ty_1
- Explanation: pid__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'ino', 'type': 'u64_'}, {'name': 'pidfs_node', 'type': 'rb_node'}, {'name': 'stashed', 'type': '*mut dentry'}, {'name': 'attr', 'type': '*mut pidfs_attr'}]`
- New: `[{'name': 'ino', 'type': 'u64_'}, {'name': 'pidfs_hash', 'type': 'rhash_head'}, {'name': 'stashed', 'type': '*mut dentry'}, {'name': 'attr', 'type': '*mut pidfs_attr'}]`

### Rust Evidence

- Graph edges: `1`

## W-000389 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: request_queue
- Explanation: request_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'queuedata', 'type': '*mut ffi::c_void'}, {'name': 'elevator', 'type': '*mut elevator_queue'}, {'name': 'mq_ops', 'type': '*const blk_mq_ops'}, {'name': 'queue_ctx', 'type': '*mut blk_mq_ctx'}, {'name': 'queue_flags', 'type': 'ffi::c_ulong'}, {'name': 'rq_timeout', 'type': 'ffi::c_uint'}, {'name': 'queue_depth', 'type': 'ffi::c_uint'}, {'name': 'refs', 'type': 'refcount_t'}, {'name': 'nr_hw_queues', 'type': 'ffi::c_uint'}, {'name': 'queue_hw_ctx', 'type': '*mut *mut blk_mq_hw_ctx'}, {'name': 'q_usage_counter', 'type': 'percpu_ref'}, {'name': 'io_lock_cls_key', 'type': 'lock_class_key'}, {'name': 'io_lockdep_map', 'type': 'lockdep_map'}, {'name': 'q_lock_cls_key', 'type': 'lock_class_key'}, {'name': 'q_lockdep_map', 'type': 'lockdep_map'}, {'name': 'last_merge', 'type': '*mut request'}, {'name': 'queue_lock', 'type': 'spinlock_t'}, {'name': 'quiesce_depth', 'type': 'ffi::c_int'}, {'name': 'disk', 'type': '*mut gendisk'}, {'name': 'mq_kobj', 'type': '*mut kobject'}, {'name': 'limits', 'type': 'queue_limits'}, {'name': 'dev', 'type': '*mut device'}, {'name': 'rpm_status', 'type': 'rpm_status'}, {'name': 'pm_only', 'type': 'atomic_t'}, {'name': 'stats', 'type': '*mut blk_queue_stats'}, {'name': 'rq_qos', 'type': '*mut rq_qos'}, {'name': 'rq_qos_mutex', 'type': 'mutex'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'nr_requests', 'type': 'ffi::c_ulong'}, {'name': 'timeout', 'type': 'timer_list'}, {'name': 'timeout_work', 'type': 'work_struct'}, {'name': 'nr_active_requests_shared_tags', 'type': 'atomic_t'}, {'name': 'sched_shared_tags', 'type': '*mut blk_mq_tags'}, {'name': 'icq_list', 'type': 'list_head'}, {'name': 'blkcg_pols', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'root_blkg', 'type': '*mut blkcg_gq'}, {'name': 'blkg_list', 'type': 'list_head'}, {'name': 'blkcg_mutex', 'type': 'mutex'}, {'name': 'node', 'type': 'ffi::c_int'}, {'name': 'requeue_lock', 'type': 'spinlock_t'}, {'name': 'requeue_list', 'type': 'list_head'}, {'name': 'requeue_work', 'type': 'delayed_work'}, {'name': 'blk_trace', 'type': '*mut blk_trace'}, {'name': 'fq', 'type': '*mut blk_flush_queue'}, {'name': 'flush_list', 'type': 'list_head'}, {'name': 'elevator_lock', 'type': 'mutex'}, {'name': 'sysfs_lock', 'type': 'mutex'}, {'name': 'limits_lock', 'type': 'mutex'}, {'name': 'unused_hctx_list', 'type': 'list_head'}, {'name': 'unused_hctx_lock', 'type': 'spinlock_t'}, {'name': 'mq_freeze_depth', 'type': 'ffi::c_int'}, {'name': 'callback_head', 'type': 'callback_head'}, {'name': 'mq_freeze_wq', 'type': 'wait_queue_head_t'}, {'name': 'mq_freeze_lock', 'type': 'mutex'}, {'name': 'tag_set', 'type': '*mut blk_mq_tag_set'}, {'name': 'tag_set_list', 'type': 'list_head'}, {'name': 'debugfs_dir', 'type': '*mut dentry'}, {'name': 'sched_debugfs_dir', 'type': '*mut dentry'}, {'name': 'rqos_debugfs_dir', 'type': '*mut dentry'}, {'name': 'debugfs_mutex', 'type': 'mutex'}]`
- New: `[{'name': 'queuedata', 'type': '*mut ffi::c_void'}, {'name': 'elevator', 'type': '*mut elevator_queue'}, {'name': 'mq_ops', 'type': '*const blk_mq_ops'}, {'name': 'queue_ctx', 'type': '*mut blk_mq_ctx'}, {'name': 'queue_flags', 'type': 'ffi::c_ulong'}, {'name': 'rq_timeout', 'type': 'ffi::c_uint'}, {'name': 'queue_depth', 'type': 'ffi::c_uint'}, {'name': 'refs', 'type': 'refcount_t'}, {'name': 'nr_hw_queues', 'type': 'ffi::c_uint'}, {'name': 'queue_hw_ctx', 'type': '*mut *mut blk_mq_hw_ctx'}, {'name': 'q_usage_counter', 'type': 'percpu_ref'}, {'name': 'io_lock_cls_key', 'type': 'lock_class_key'}, {'name': 'io_lockdep_map', 'type': 'lockdep_map'}, {'name': 'q_lock_cls_key', 'type': 'lock_class_key'}, {'name': 'q_lockdep_map', 'type': 'lockdep_map'}, {'name': 'last_merge', 'type': '*mut request'}, {'name': 'queue_lock', 'type': 'spinlock_t'}, {'name': 'quiesce_depth', 'type': 'ffi::c_int'}, {'name': 'disk', 'type': '*mut gendisk'}, {'name': 'mq_kobj', 'type': '*mut kobject'}, {'name': 'limits', 'type': 'queue_limits'}, {'name': 'dev', 'type': '*mut device'}, {'name': 'rpm_status', 'type': 'rpm_status'}, {'name': 'pm_only', 'type': 'atomic_t'}, {'name': 'stats', 'type': '*mut blk_queue_stats'}, {'name': 'rq_qos', 'type': '*mut rq_qos'}, {'name': 'rq_qos_mutex', 'type': 'mutex'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'nr_requests', 'type': 'ffi::c_uint'}, {'name': 'async_depth', 'type': 'ffi::c_uint'}, {'name': 'timeout', 'type': 'timer_list'}, {'name': 'timeout_work', 'type': 'work_struct'}, {'name': 'nr_active_requests_shared_tags', 'type': 'atomic_t'}, {'name': 'sched_shared_tags', 'type': '*mut blk_mq_tags'}, {'name': 'icq_list', 'type': 'list_head'}, {'name': 'blkcg_pols', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'root_blkg', 'type': '*mut blkcg_gq'}, {'name': 'blkg_list', 'type': 'list_head'}, {'name': 'blkcg_mutex', 'type': 'mutex'}, {'name': 'node', 'type': 'ffi::c_int'}, {'name': 'requeue_lock', 'type': 'spinlock_t'}, {'name': 'requeue_list', 'type': 'list_head'}, {'name': 'requeue_work', 'type': 'delayed_work'}, {'name': 'blk_trace', 'type': '*mut blk_trace'}, {'name': 'fq', 'type': '*mut blk_flush_queue'}, {'name': 'flush_list', 'type': 'list_head'}, {'name': 'elevator_lock', 'type': 'mutex'}, {'name': 'sysfs_lock', 'type': 'mutex'}, {'name': 'limits_lock', 'type': 'mutex'}, {'name': 'unused_hctx_list', 'type': 'list_head'}, {'name': 'unused_hctx_lock', 'type': 'spinlock_t'}, {'name': 'mq_freeze_depth', 'type': 'ffi::c_int'}, {'name': 'callback_head', 'type': 'callback_head'}, {'name': 'mq_freeze_wq', 'type': 'wait_queue_head_t'}, {'name': 'mq_freeze_lock', 'type': 'mutex'}, {'name': 'tag_set', 'type': '*mut blk_mq_tag_set'}, {'name': 'tag_set_list', 'type': 'list_head'}, {'name': 'debugfs_dir', 'type': '*mut dentry'}, {'name': 'sched_debugfs_dir', 'type': '*mut dentry'}, {'name': 'rqos_debugfs_dir', 'type': '*mut dentry'}, {'name': 'debugfs_mutex', 'type': 'mutex'}]`

### Rust Evidence

- Graph edges: `1`

## W-000390 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: restart_block__bindgen_ty_1__bindgen_ty_3
- Explanation: restart_block__bindgen_ty_1__bindgen_ty_3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'ufds', 'type': '*mut pollfd'}, {'name': 'nfds', 'type': 'ffi::c_int'}, {'name': 'has_timeout', 'type': 'ffi::c_int'}, {'name': 'tv_sec', 'type': 'ffi::c_ulong'}, {'name': 'tv_nsec', 'type': 'ffi::c_ulong'}]`
- New: `[{'name': 'ufds', 'type': '*mut pollfd'}, {'name': 'nfds', 'type': 'ffi::c_int'}, {'name': 'has_timeout', 'type': 'ffi::c_int'}, {'name': 'end_time', 'type': 'timespec64'}]`

### Rust Evidence

- Graph edges: `1`

## W-000391 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: sched_entity
- Explanation: sched_entity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'load', 'type': 'load_weight'}, {'name': 'run_node', 'type': 'rb_node'}, {'name': 'deadline', 'type': 'u64_'}, {'name': 'min_vruntime', 'type': 'u64_'}, {'name': 'min_slice', 'type': 'u64_'}, {'name': 'group_node', 'type': 'list_head'}, {'name': 'on_rq', 'type': 'ffi::c_uchar'}, {'name': 'sched_delayed', 'type': 'ffi::c_uchar'}, {'name': 'rel_deadline', 'type': 'ffi::c_uchar'}, {'name': 'custom_slice', 'type': 'ffi::c_uchar'}, {'name': 'exec_start', 'type': 'u64_'}, {'name': 'sum_exec_runtime', 'type': 'u64_'}, {'name': 'prev_sum_exec_runtime', 'type': 'u64_'}, {'name': 'vruntime', 'type': 'u64_'}, {'name': '__bindgen_anon_1', 'type': 'sched_entity__bindgen_ty_1'}, {'name': 'slice', 'type': 'u64_'}, {'name': 'nr_migrations', 'type': 'u64_'}, {'name': 'depth', 'type': 'ffi::c_int'}, {'name': 'parent', 'type': '*mut sched_entity'}, {'name': 'cfs_rq', 'type': '*mut cfs_rq'}, {'name': 'my_q', 'type': '*mut cfs_rq'}, {'name': 'runnable_weight', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': 'u64'}, {'name': 'avg', 'type': 'sched_avg'}]`
- New: `[{'name': 'load', 'type': 'load_weight'}, {'name': 'run_node', 'type': 'rb_node'}, {'name': 'deadline', 'type': 'u64_'}, {'name': 'min_vruntime', 'type': 'u64_'}, {'name': 'min_slice', 'type': 'u64_'}, {'name': 'max_slice', 'type': 'u64_'}, {'name': 'group_node', 'type': 'list_head'}, {'name': 'on_rq', 'type': 'ffi::c_uchar'}, {'name': 'sched_delayed', 'type': 'ffi::c_uchar'}, {'name': 'rel_deadline', 'type': 'ffi::c_uchar'}, {'name': 'custom_slice', 'type': 'ffi::c_uchar'}, {'name': 'exec_start', 'type': 'u64_'}, {'name': 'sum_exec_runtime', 'type': 'u64_'}, {'name': 'prev_sum_exec_runtime', 'type': 'u64_'}, {'name': 'vruntime', 'type': 'u64_'}, {'name': 'vlag', 'type': 's64'}, {'name': 'vprot', 'type': 'u64_'}, {'name': 'slice', 'type': 'u64_'}, {'name': 'nr_migrations', 'type': 'u64_'}, {'name': 'depth', 'type': 'ffi::c_int'}, {'name': 'parent', 'type': '*mut sched_entity'}, {'name': 'cfs_rq', 'type': '*mut cfs_rq'}, {'name': 'my_q', 'type': '*mut cfs_rq'}, {'name': 'runnable_weight', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': 'avg', 'type': 'sched_avg'}]`

### Rust Evidence

- Graph edges: `1`

## W-000392 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: sched_info
- Explanation: sched_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'pcount', 'type': 'ffi::c_ulong'}, {'name': 'run_delay', 'type': 'ffi::c_ulonglong'}, {'name': 'max_run_delay', 'type': 'ffi::c_ulonglong'}, {'name': 'min_run_delay', 'type': 'ffi::c_ulonglong'}, {'name': 'last_arrival', 'type': 'ffi::c_ulonglong'}, {'name': 'last_queued', 'type': 'ffi::c_ulonglong'}]`
- New: `[{'name': 'pcount', 'type': 'ffi::c_ulong'}, {'name': 'run_delay', 'type': 'ffi::c_ulonglong'}, {'name': 'max_run_delay', 'type': 'ffi::c_ulonglong'}, {'name': 'min_run_delay', 'type': 'ffi::c_ulonglong'}, {'name': 'last_arrival', 'type': 'ffi::c_ulonglong'}, {'name': 'last_queued', 'type': 'ffi::c_ulonglong'}, {'name': 'max_run_delay_ts', 'type': 'timespec64'}]`

### Rust Evidence

- Graph edges: `1`

## W-000394 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: srcu_data
- Explanation: srcu_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'srcu_ctrs', 'type': '[srcu_ctr; 2usize]'}, {'name': 'srcu_reader_flavor', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': '[u32; 7usize]'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'srcu_cblist', 'type': 'rcu_segcblist'}, {'name': 'srcu_gp_seq_needed', 'type': 'ffi::c_ulong'}, {'name': 'srcu_gp_seq_needed_exp', 'type': 'ffi::c_ulong'}, {'name': 'srcu_cblist_invoking', 'type': 'bool_'}, {'name': 'delay_work', 'type': 'timer_list'}, {'name': 'work', 'type': 'work_struct'}, {'name': 'srcu_barrier_head', 'type': 'callback_head'}, {'name': 'srcu_ec_head', 'type': 'callback_head'}, {'name': 'srcu_ec_state', 'type': 'ffi::c_int'}, {'name': 'mynode', 'type': '*mut srcu_node'}, {'name': 'grpmask', 'type': 'ffi::c_ulong'}, {'name': 'cpu', 'type': 'ffi::c_int'}, {'name': 'ssp', 'type': '*mut srcu_struct'}]`
- New: `[{'name': 'srcu_ctrs', 'type': '[srcu_ctr; 2usize]'}, {'name': 'srcu_reader_flavor', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': '[u32; 7usize]'}, {'name': 'lock', 'type': 'raw_spinlock_t'}, {'name': 'srcu_cblist', 'type': 'rcu_segcblist'}, {'name': 'srcu_gp_seq_needed', 'type': 'ffi::c_ulong'}, {'name': 'srcu_gp_seq_needed_exp', 'type': 'ffi::c_ulong'}, {'name': 'srcu_cblist_invoking', 'type': 'bool_'}, {'name': 'delay_work', 'type': 'timer_list'}, {'name': 'work', 'type': 'work_struct'}, {'name': 'srcu_barrier_head', 'type': 'callback_head'}, {'name': 'srcu_ec_head', 'type': 'callback_head'}, {'name': 'srcu_ec_state', 'type': 'ffi::c_int'}, {'name': 'mynode', 'type': '*mut srcu_node'}, {'name': 'grpmask', 'type': 'ffi::c_ulong'}, {'name': 'cpu', 'type': 'ffi::c_int'}, {'name': 'ssp', 'type': '*mut srcu_struct'}]`

### Rust Evidence

- Graph edges: `1`

## W-000395 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: srcu_node
- Explanation: srcu_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'lock', 'type': 'spinlock_t'}, {'name': 'srcu_have_cbs', 'type': '[ffi::c_ulong; 4usize]'}, {'name': 'srcu_data_have_cbs', 'type': '[ffi::c_ulong; 4usize]'}, {'name': 'srcu_gp_seq_needed_exp', 'type': 'ffi::c_ulong'}, {'name': 'srcu_parent', 'type': '*mut srcu_node'}, {'name': 'grplo', 'type': 'ffi::c_int'}, {'name': 'grphi', 'type': 'ffi::c_int'}]`
- New: `[{'name': 'lock', 'type': 'raw_spinlock_t'}, {'name': 'srcu_have_cbs', 'type': '[ffi::c_ulong; 4usize]'}, {'name': 'srcu_data_have_cbs', 'type': '[ffi::c_ulong; 4usize]'}, {'name': 'srcu_gp_seq_needed_exp', 'type': 'ffi::c_ulong'}, {'name': 'srcu_parent', 'type': '*mut srcu_node'}, {'name': 'grplo', 'type': 'ffi::c_int'}, {'name': 'grphi', 'type': 'ffi::c_int'}]`

### Rust Evidence

- Graph edges: `1`

## W-000396 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: srcu_usage
- Explanation: srcu_usage changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'node', 'type': '*mut srcu_node'}, {'name': 'level', 'type': '[*mut srcu_node; 3usize]'}, {'name': 'srcu_size_state', 'type': 'ffi::c_int'}, {'name': 'srcu_cb_mutex', 'type': 'mutex'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'srcu_gp_mutex', 'type': 'mutex'}, {'name': 'srcu_gp_seq', 'type': 'ffi::c_ulong'}, {'name': 'srcu_gp_seq_needed', 'type': 'ffi::c_ulong'}, {'name': 'srcu_gp_seq_needed_exp', 'type': 'ffi::c_ulong'}, {'name': 'srcu_gp_start', 'type': 'ffi::c_ulong'}, {'name': 'srcu_last_gp_end', 'type': 'ffi::c_ulong'}, {'name': 'srcu_size_jiffies', 'type': 'ffi::c_ulong'}, {'name': 'srcu_n_lock_retries', 'type': 'ffi::c_ulong'}, {'name': 'srcu_n_exp_nodelay', 'type': 'ffi::c_ulong'}, {'name': 'sda_is_static', 'type': 'bool_'}, {'name': 'srcu_barrier_seq', 'type': 'ffi::c_ulong'}, {'name': 'srcu_barrier_mutex', 'type': 'mutex'}, {'name': 'srcu_barrier_completion', 'type': 'completion'}, {'name': 'srcu_barrier_cpu_cnt', 'type': 'atomic_t'}, {'name': 'reschedule_jiffies', 'type': 'ffi::c_ulong'}, {'name': 'reschedule_count', 'type': 'ffi::c_ulong'}, {'name': 'work', 'type': 'delayed_work'}, {'name': 'srcu_ssp', 'type': '*mut srcu_struct'}]`
- New: `[{'name': 'node', 'type': '*mut srcu_node'}, {'name': 'level', 'type': '[*mut srcu_node; 3usize]'}, {'name': 'srcu_size_state', 'type': 'ffi::c_int'}, {'name': 'srcu_cb_mutex', 'type': 'mutex'}, {'name': 'lock', 'type': 'raw_spinlock_t'}, {'name': 'srcu_gp_mutex', 'type': 'mutex'}, {'name': 'srcu_gp_seq', 'type': 'ffi::c_ulong'}, {'name': 'srcu_gp_seq_needed', 'type': 'ffi::c_ulong'}, {'name': 'srcu_gp_seq_needed_exp', 'type': 'ffi::c_ulong'}, {'name': 'srcu_gp_start', 'type': 'ffi::c_ulong'}, {'name': 'srcu_last_gp_end', 'type': 'ffi::c_ulong'}, {'name': 'srcu_size_jiffies', 'type': 'ffi::c_ulong'}, {'name': 'srcu_n_lock_retries', 'type': 'ffi::c_ulong'}, {'name': 'srcu_n_exp_nodelay', 'type': 'ffi::c_ulong'}, {'name': 'sda_is_static', 'type': 'bool_'}, {'name': 'srcu_barrier_seq', 'type': 'ffi::c_ulong'}, {'name': 'srcu_barrier_mutex', 'type': 'mutex'}, {'name': 'srcu_barrier_completion', 'type': 'completion'}, {'name': 'srcu_barrier_cpu_cnt', 'type': 'atomic_t'}, {'name': 'reschedule_jiffies', 'type': 'ffi::c_ulong'}, {'name': 'reschedule_count', 'type': 'ffi::c_ulong'}, {'name': 'work', 'type': 'delayed_work'}, {'name': 'irq_work', 'type': 'irq_work'}, {'name': 'srcu_ssp', 'type': '*mut srcu_struct'}]`

### Rust Evidence

- Graph edges: `1`

## W-000397 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: super_block
- Explanation: super_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 's_list', 'type': 'list_head'}, {'name': 's_dev', 'type': 'dev_t'}, {'name': 's_blocksize_bits', 'type': 'ffi::c_uchar'}, {'name': 's_blocksize', 'type': 'ffi::c_ulong'}, {'name': 's_maxbytes', 'type': 'loff_t'}, {'name': 's_type', 'type': '*mut file_system_type'}, {'name': 's_op', 'type': '*const super_operations'}, {'name': 'dq_op', 'type': '*const dquot_operations'}, {'name': 's_qcop', 'type': '*const quotactl_ops'}, {'name': 's_export_op', 'type': '*const export_operations'}, {'name': 's_flags', 'type': 'ffi::c_ulong'}, {'name': 's_iflags', 'type': 'ffi::c_ulong'}, {'name': 's_magic', 'type': 'ffi::c_ulong'}, {'name': 's_root', 'type': '*mut dentry'}, {'name': 's_umount', 'type': 'rw_semaphore'}, {'name': 's_count', 'type': 'ffi::c_int'}, {'name': 's_active', 'type': 'atomic_t'}, {'name': 's_security', 'type': '*mut ffi::c_void'}, {'name': 's_xattr', 'type': '*const *const xattr_handler'}, {'name': 's_roots', 'type': 'hlist_bl_head'}, {'name': 's_mounts', 'type': '*mut mount'}, {'name': 's_bdev', 'type': '*mut block_device'}, {'name': 's_bdev_file', 'type': '*mut file'}, {'name': 's_bdi', 'type': '*mut backing_dev_info'}, {'name': 's_mtd', 'type': '*mut mtd_info'}, {'name': 's_instances', 'type': 'hlist_node'}, {'name': 's_quota_types', 'type': 'ffi::c_uint'}, {'name': 's_dquot', 'type': 'quota_info'}, {'name': 's_writers', 'type': 'sb_writers'}, {'name': 's_fs_info', 'type': '*mut ffi::c_void'}, {'name': 's_time_gran', 'type': 'u32_'}, {'name': 's_time_min', 'type': 'time64_t'}, {'name': 's_time_max', 'type': 'time64_t'}, {'name': 's_fsnotify_mask', 'type': 'u32_'}, {'name': 's_fsnotify_info', 'type': '*mut fsnotify_sb_info'}, {'name': 's_id', 'type': '[ffi::c_char; 32usize]'}, {'name': 's_uuid', 'type': 'uuid_t'}, {'name': 's_uuid_len', 'type': 'u8_'}, {'name': 's_sysfs_name', 'type': '[ffi::c_char; 37usize]'}, {'name': 's_max_links', 'type': 'ffi::c_uint'}, {'name': 's_d_flags', 'type': 'ffi::c_uint'}, {'name': 's_vfs_rename_mutex', 'type': 'mutex'}, {'name': 's_subtype', 'type': '*const ffi::c_char'}, {'name': '__s_d_op', 'type': '*const dentry_operations'}, {'name': 's_shrink', 'type': '*mut shrinker'}, {'name': 's_remove_count', 'type': 'atomic_long_t'}, {'name': 's_readonly_remount', 'type': 'ffi::c_int'}, {'name': 's_wb_err', 'type': 'errseq_t'}, {'name': 's_dio_done_wq', 'type': '*mut workqueue_struct'}, {'name': 's_pins', 'type': 'hlist_head'}, {'name': 's_user_ns', 'type': '*mut user_namespace'}, {'name': 's_dentry_lru', 'type': 'list_lru'}, {'name': 's_inode_lru', 'type': 'list_lru'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 's_sync_lock', 'type': 'mutex'}, {'name': 's_stack_depth', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': 'u32'}, {'name': 's_inode_list_lock', 'type': 'spinlock_t'}, {'name': 's_inodes', 'type': 'list_head'}, {'name': 's_inode_wblist_lock', 'type': 'spinlock_t'}, {'name': 's_inodes_wb', 'type': 'list_head'}, {'name': 's_min_writeback_pages', 'type': 'ffi::c_long'}]`
- New: `[{'name': 's_list', 'type': 'list_head'}, {'name': 's_dev', 'type': 'dev_t'}, {'name': 's_blocksize_bits', 'type': 'ffi::c_uchar'}, {'name': 's_blocksize', 'type': 'ffi::c_ulong'}, {'name': 's_maxbytes', 'type': 'loff_t'}, {'name': 's_type', 'type': '*mut file_system_type'}, {'name': 's_op', 'type': '*const super_operations'}, {'name': 'dq_op', 'type': '*const dquot_operations'}, {'name': 's_qcop', 'type': '*const quotactl_ops'}, {'name': 's_export_op', 'type': '*const export_operations'}, {'name': 's_flags', 'type': 'ffi::c_ulong'}, {'name': 's_iflags', 'type': 'ffi::c_ulong'}, {'name': 's_magic', 'type': 'ffi::c_ulong'}, {'name': 's_root', 'type': '*mut dentry'}, {'name': 's_umount', 'type': 'rw_semaphore'}, {'name': 's_count', 'type': 'ffi::c_int'}, {'name': 's_active', 'type': 'atomic_t'}, {'name': 's_security', 'type': '*mut ffi::c_void'}, {'name': 's_xattr', 'type': '*const *const xattr_handler'}, {'name': 's_roots', 'type': 'hlist_bl_head'}, {'name': 's_mounts', 'type': '*mut mount'}, {'name': 's_bdev', 'type': '*mut block_device'}, {'name': 's_bdev_file', 'type': '*mut file'}, {'name': 's_bdi', 'type': '*mut backing_dev_info'}, {'name': 's_mtd', 'type': '*mut mtd_info'}, {'name': 's_instances', 'type': 'hlist_node'}, {'name': 's_quota_types', 'type': 'ffi::c_uint'}, {'name': 's_dquot', 'type': 'quota_info'}, {'name': 's_writers', 'type': 'sb_writers'}, {'name': 's_fs_info', 'type': '*mut ffi::c_void'}, {'name': 's_time_gran', 'type': 'u32_'}, {'name': 's_time_min', 'type': 'time64_t'}, {'name': 's_time_max', 'type': 'time64_t'}, {'name': 's_fsnotify_mask', 'type': 'u32_'}, {'name': 's_fsnotify_info', 'type': '*mut fsnotify_sb_info'}, {'name': 's_id', 'type': '[ffi::c_char; 32usize]'}, {'name': 's_uuid', 'type': 'uuid_t'}, {'name': 's_uuid_len', 'type': 'u8_'}, {'name': 's_sysfs_name', 'type': '[ffi::c_char; 37usize]'}, {'name': 's_max_links', 'type': 'ffi::c_uint'}, {'name': 's_d_flags', 'type': 'ffi::c_uint'}, {'name': 's_vfs_rename_mutex', 'type': 'mutex'}, {'name': 's_subtype', 'type': '*const ffi::c_char'}, {'name': '__s_d_op', 'type': '*const dentry_operations'}, {'name': 's_shrink', 'type': '*mut shrinker'}, {'name': 's_remove_count', 'type': 'atomic_long_t'}, {'name': 's_readonly_remount', 'type': 'ffi::c_int'}, {'name': 's_wb_err', 'type': 'errseq_t'}, {'name': 's_dio_done_wq', 'type': '*mut workqueue_struct'}, {'name': 's_pins', 'type': 'hlist_head'}, {'name': 's_user_ns', 'type': '*mut user_namespace'}, {'name': 's_dentry_lru', 'type': 'list_lru'}, {'name': 's_inode_lru', 'type': 'list_lru'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 's_sync_lock', 'type': 'mutex'}, {'name': 's_stack_depth', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': 'u32'}, {'name': 's_inode_list_lock', 'type': 'spinlock_t'}, {'name': 's_inodes', 'type': 'list_head'}, {'name': 's_inode_wblist_lock', 'type': 'spinlock_t'}, {'name': 's_inodes_wb', 'type': 'list_head'}, {'name': 's_min_writeback_pages', 'type': 'ffi::c_long'}, {'name': 's_pending_errors', 'type': 'refcount_t'}]`

### Rust Evidence

- Graph edges: `1`

## W-000398 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: super_operations
- Explanation: super_operations changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'destroy_inode', 'type': '::core::option::Option<unsafe extern "C" fn(inode: *mut inode)>'}, {'name': 'free_inode', 'type': '::core::option::Option<unsafe extern "C" fn(inode: *mut inode)>'}, {'name': 'write_inode', 'type': '::core::option::Option<'}, {'name': 'drop_inode', 'type': '::core::option::Option<unsafe extern "C" fn(inode: *mut inode) -> ffi::c_int>'}, {'name': 'evict_inode', 'type': '::core::option::Option<unsafe extern "C" fn(inode: *mut inode)>'}, {'name': 'put_super', 'type': '::core::option::Option<unsafe extern "C" fn(sb: *mut super_block)>'}, {'name': 'sync_fs', 'type': '::core::option::Option<'}, {'name': 'freeze_super', 'type': '::core::option::Option<'}, {'name': 'freeze_fs', 'type': '::core::option::Option<unsafe extern "C" fn(sb: *mut super_block) -> ffi::c_int>'}, {'name': 'thaw_super', 'type': '::core::option::Option<'}, {'name': 'statfs', 'type': '::core::option::Option<'}, {'name': 'remount_fs', 'type': '::core::option::Option<'}, {'name': 'umount_begin', 'type': '::core::option::Option<unsafe extern "C" fn(sb: *mut super_block)>'}, {'name': 'show_options', 'type': '::core::option::Option<'}, {'name': 'show_devname', 'type': '::core::option::Option<'}, {'name': 'show_path', 'type': '::core::option::Option<'}, {'name': 'show_stats', 'type': '::core::option::Option<'}, {'name': 'quota_read', 'type': '::core::option::Option<'}, {'name': 'quota_write', 'type': '::core::option::Option<'}, {'name': 'nr_cached_objects', 'type': '::core::option::Option<'}, {'name': 'free_cached_objects', 'type': '::core::option::Option<'}, {'name': 'remove_bdev', 'type': '::core::option::Option<'}, {'name': 'shutdown', 'type': '::core::option::Option<unsafe extern "C" fn(sb: *mut super_block)>'}]`
- New: `[{'name': 'destroy_inode', 'type': '::core::option::Option<unsafe extern "C" fn(inode: *mut inode)>'}, {'name': 'free_inode', 'type': '::core::option::Option<unsafe extern "C" fn(inode: *mut inode)>'}, {'name': 'write_inode', 'type': '::core::option::Option<'}, {'name': 'drop_inode', 'type': '::core::option::Option<unsafe extern "C" fn(inode: *mut inode) -> ffi::c_int>'}, {'name': 'evict_inode', 'type': '::core::option::Option<unsafe extern "C" fn(inode: *mut inode)>'}, {'name': 'put_super', 'type': '::core::option::Option<unsafe extern "C" fn(sb: *mut super_block)>'}, {'name': 'sync_fs', 'type': '::core::option::Option<'}, {'name': 'freeze_super', 'type': '::core::option::Option<'}, {'name': 'freeze_fs', 'type': '::core::option::Option<unsafe extern "C" fn(sb: *mut super_block) -> ffi::c_int>'}, {'name': 'thaw_super', 'type': '::core::option::Option<'}, {'name': 'statfs', 'type': '::core::option::Option<'}, {'name': 'umount_begin', 'type': '::core::option::Option<unsafe extern "C" fn(sb: *mut super_block)>'}, {'name': 'show_options', 'type': '::core::option::Option<'}, {'name': 'show_devname', 'type': '::core::option::Option<'}, {'name': 'show_path', 'type': '::core::option::Option<'}, {'name': 'show_stats', 'type': '::core::option::Option<'}, {'name': 'quota_read', 'type': '::core::option::Option<'}, {'name': 'quota_write', 'type': '::core::option::Option<'}, {'name': 'nr_cached_objects', 'type': '::core::option::Option<'}, {'name': 'free_cached_objects', 'type': '::core::option::Option<'}, {'name': 'remove_bdev', 'type': '::core::option::Option<'}, {'name': 'shutdown', 'type': '::core::option::Option<unsafe extern "C" fn(sb: *mut super_block)>'}, {'name': 'report_error', 'type': '::core::option::Option<unsafe extern "C" fn(event: *const fserror_event)>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000402 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: user_namespace
- Explanation: user_namespace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'uid_map', 'type': 'uid_gid_map'}, {'name': 'gid_map', 'type': 'uid_gid_map'}, {'name': 'projid_map', 'type': 'uid_gid_map'}, {'name': 'parent', 'type': '*mut user_namespace'}, {'name': 'level', 'type': 'ffi::c_int'}, {'name': 'owner', 'type': 'kuid_t'}, {'name': 'group', 'type': 'kgid_t'}, {'name': 'ns', 'type': 'ns_common'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'parent_could_setfcap', 'type': 'bool_'}, {'name': 'keyring_name_list', 'type': 'list_head'}, {'name': 'user_keyring_register', 'type': '*mut key'}, {'name': 'keyring_sem', 'type': 'rw_semaphore'}, {'name': 'work', 'type': 'work_struct'}, {'name': 'set', 'type': 'ctl_table_set'}, {'name': 'sysctls', 'type': '*mut ctl_table_header'}, {'name': 'ucounts', 'type': '*mut ucounts'}, {'name': 'ucount_max', 'type': '[ffi::c_long; 10usize]'}, {'name': 'rlimit_max', 'type': '[ffi::c_long; 4usize]'}, {'name': 'binfmt_misc', 'type': '*mut binfmt_misc'}]`
- New: `[{'name': 'uid_map', 'type': 'uid_gid_map'}, {'name': 'gid_map', 'type': 'uid_gid_map'}, {'name': 'projid_map', 'type': 'uid_gid_map'}, {'name': 'parent', 'type': '*mut user_namespace'}, {'name': 'level', 'type': 'ffi::c_int'}, {'name': 'owner', 'type': 'kuid_t'}, {'name': 'group', 'type': 'kgid_t'}, {'name': '__bindgen_padding_0', 'type': '[u64; 5usize]'}, {'name': 'ns', 'type': 'ns_common'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'parent_could_setfcap', 'type': 'bool_'}, {'name': 'keyring_name_list', 'type': 'list_head'}, {'name': 'user_keyring_register', 'type': '*mut key'}, {'name': 'keyring_sem', 'type': 'rw_semaphore'}, {'name': 'work', 'type': 'work_struct'}, {'name': 'set', 'type': 'ctl_table_set'}, {'name': 'sysctls', 'type': '*mut ctl_table_header'}, {'name': 'ucounts', 'type': '*mut ucounts'}, {'name': 'ucount_max', 'type': '[ffi::c_long; 10usize]'}, {'name': 'rlimit_max', 'type': '[ffi::c_long; 4usize]'}, {'name': 'binfmt_misc', 'type': '*mut binfmt_misc'}]`

### Rust Evidence

- Graph edges: `1`

## W-000403 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vm_area_desc
- Explanation: vm_area_desc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mm', 'type': '*const mm_struct'}, {'name': 'file', 'type': '*mut file'}, {'name': 'start', 'type': 'ffi::c_ulong'}, {'name': 'end', 'type': 'ffi::c_ulong'}, {'name': 'pgoff', 'type': 'ffi::c_ulong'}, {'name': 'vm_file', 'type': '*mut file'}, {'name': '__bindgen_anon_1', 'type': 'vm_area_desc__bindgen_ty_1'}, {'name': 'page_prot', 'type': 'pgprot_t'}, {'name': 'vm_ops', 'type': '*const vm_operations_struct'}, {'name': 'private_data', 'type': '*mut ffi::c_void'}, {'name': 'action', 'type': 'mmap_action'}]`
- New: `[{'name': 'mm', 'type': '*const mm_struct'}, {'name': 'file', 'type': '*mut file'}, {'name': 'start', 'type': 'ffi::c_ulong'}, {'name': 'end', 'type': 'ffi::c_ulong'}, {'name': 'pgoff', 'type': 'ffi::c_ulong'}, {'name': 'vm_file', 'type': '*mut file'}, {'name': 'vma_flags', 'type': 'vma_flags_t'}, {'name': 'page_prot', 'type': 'pgprot_t'}, {'name': 'vm_ops', 'type': '*const vm_operations_struct'}, {'name': 'private_data', 'type': '*mut ffi::c_void'}, {'name': 'action', 'type': 'mmap_action'}]`

### Rust Evidence

- Graph edges: `1`

## W-000405 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: AT_VECTOR_SIZE
- Explanation: AT_VECTOR_SIZE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `52`
- New: `56`

### Rust Evidence

- Graph edges: `3`

## W-000404 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ACPI_CA_VERSION
- Explanation: ACPI_CA_VERSION changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `539297799`
- New: `539300370`

### Rust Evidence

- Graph edges: `1`

## W-000406 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: AT_VECTOR_SIZE_BASE
- Explanation: AT_VECTOR_SIZE_BASE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `22`
- New: `24`

### Rust Evidence

- Graph edges: `1`

## W-000407 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: IA32_NR_syscalls
- Explanation: IA32_NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `471`
- New: `472`

### Rust Evidence

- Graph edges: `1`

## W-000408 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: MSR_AMD64_SNP_RESV_BIT
- Explanation: MSR_AMD64_SNP_RESV_BIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `19`
- New: `24`

### Rust Evidence

- Graph edges: `1`

## W-000409 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: NR_syscalls
- Explanation: NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `471`
- New: `472`

### Rust Evidence

- Graph edges: `1`

## W-000410 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: PCI_CAP_EXP_ENDPOINT_SIZEOF_V2
- Explanation: PCI_CAP_EXP_ENDPOINT_SIZEOF_V2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `50`
- New: `52`

### Rust Evidence

- Graph edges: `1`

## W-000411 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: REQUIRED_MASK3
- Explanation: REQUIRED_MASK3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `36700160`
- New: `36732928`

### Rust Evidence

- Graph edges: `1`

## W-000412 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: RQ_nr_pinned
- Explanation: RQ_nr_pinned changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `3200`
- New: `3216`

### Rust Evidence

- Graph edges: `1`

## W-000413 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TASKSTATS_VERSION
- Explanation: TASKSTATS_VERSION changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `17`

### Rust Evidence

- Graph edges: `1`

## W-000414 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TASK_stack_canary
- Explanation: TASK_stack_canary changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `1432`
- New: `1464`

### Rust Evidence

- Graph edges: `1`

## W-000415 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TASK_threadsp
- Explanation: TASK_threadsp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `2976`
- New: `3032`

### Rust Evidence

- Graph edges: `1`

## W-000416 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TIF_ADDR32
- Explanation: TIF_ADDR32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `28`
- New: `27`

### Rust Evidence

- Graph edges: `1`

## W-000417 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __NR_ia32_syscalls
- Explanation: __NR_ia32_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `471`
- New: `472`

### Rust Evidence

- Graph edges: `1`

## W-000418 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __NR_syscalls
- Explanation: __NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `471`
- New: `472`

### Rust Evidence

- Graph edges: `1`

## W-000419 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __TCA_CAKE_STATS_MAX
- Explanation: __TCA_CAKE_STATS_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `17`
- New: `18`

### Rust Evidence

- Graph edges: `1`

## W-000420 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: _slab_flag_bits__SLAB_FLAGS_LAST_BIT
- Explanation: _slab_flag_bits__SLAB_FLAGS_LAST_BIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `17`
- New: `18`

### Rust Evidence

- Graph edges: `1`

## W-000421 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: acpi_irq_model_id_ACPI_IRQ_MODEL_COUNT
- Explanation: acpi_irq_model_id_ACPI_IRQ_MODEL_COUNT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `7`
- New: `8`

### Rust Evidence

- Graph edges: `1`

## W-000422 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: acpi_irq_model_id_ACPI_IRQ_MODEL_LPIC
- Explanation: acpi_irq_model_id_ACPI_IRQ_MODEL_LPIC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `6`

### Rust Evidence

- Graph edges: `1`

## W-000423 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: acpi_irq_model_id_ACPI_IRQ_MODEL_RINTC
- Explanation: acpi_irq_model_id_ACPI_IRQ_MODEL_RINTC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `6`
- New: `7`

### Rust Evidence

- Graph edges: `1`

## W-000424 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: acpi_madt_gic_version_ACPI_MADT_GIC_VERSION_RESERVED
- Explanation: acpi_madt_gic_version_ACPI_MADT_GIC_VERSION_RESERVED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `6`

### Rust Evidence

- Graph edges: `1`

## W-000425 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: acpi_madt_type_ACPI_MADT_TYPE_RESERVED
- Explanation: acpi_madt_type_ACPI_MADT_TYPE_RESERVED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `28`
- New: `31`

### Rust Evidence

- Graph edges: `1`

## W-000426 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_attach_type___MAX_BPF_ATTACH_TYPE
- Explanation: bpf_attach_type___MAX_BPF_ATTACH_TYPE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `58`
- New: `59`

### Rust Evidence

- Graph edges: `1`

## W-000427 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_cmd___MAX_BPF_CMD
- Explanation: bpf_cmd___MAX_BPF_CMD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `38`
- New: `39`

### Rust Evidence

- Graph edges: `1`

## W-000428 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: lockdown_reason_LOCKDOWN_BPF_READ_KERNEL
- Explanation: lockdown_reason_LOCKDOWN_BPF_READ_KERNEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `23`
- New: `24`

### Rust Evidence

- Graph edges: `1`

## W-000429 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: lockdown_reason_LOCKDOWN_CONFIDENTIALITY_MAX
- Explanation: lockdown_reason_LOCKDOWN_CONFIDENTIALITY_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `29`
- New: `30`

### Rust Evidence

- Graph edges: `1`

## W-000430 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: lockdown_reason_LOCKDOWN_DBG_READ_KERNEL
- Explanation: lockdown_reason_LOCKDOWN_DBG_READ_KERNEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `24`
- New: `25`

### Rust Evidence

- Graph edges: `1`

## W-000431 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: lockdown_reason_LOCKDOWN_INTEGRITY_MAX
- Explanation: lockdown_reason_LOCKDOWN_INTEGRITY_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `20`
- New: `21`

### Rust Evidence

- Graph edges: `1`

## W-000432 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: lockdown_reason_LOCKDOWN_KCORE
- Explanation: lockdown_reason_LOCKDOWN_KCORE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `21`
- New: `22`

### Rust Evidence

- Graph edges: `1`

## W-000433 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: lockdown_reason_LOCKDOWN_KPROBES
- Explanation: lockdown_reason_LOCKDOWN_KPROBES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `22`
- New: `23`

### Rust Evidence

- Graph edges: `1`

## W-000434 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: lockdown_reason_LOCKDOWN_PERF
- Explanation: lockdown_reason_LOCKDOWN_PERF changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `25`
- New: `26`

### Rust Evidence

- Graph edges: `1`

## W-000435 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: lockdown_reason_LOCKDOWN_TRACEFS
- Explanation: lockdown_reason_LOCKDOWN_TRACEFS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `26`
- New: `27`

### Rust Evidence

- Graph edges: `1`

## W-000436 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: lockdown_reason_LOCKDOWN_XFRM_SECRET
- Explanation: lockdown_reason_LOCKDOWN_XFRM_SECRET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `28`
- New: `29`

### Rust Evidence

- Graph edges: `1`

## W-000437 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: lockdown_reason_LOCKDOWN_XMON_RW
- Explanation: lockdown_reason_LOCKDOWN_XMON_RW changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `27`
- New: `28`

### Rust Evidence

- Graph edges: `1`

## W-000438 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: wb_reason_WB_REASON_FOREIGN_FLUSH
- Explanation: wb_reason_WB_REASON_FOREIGN_FLUSH changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `7`
- New: `6`

### Rust Evidence

- Graph edges: `1`

## W-000439 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: wb_reason_WB_REASON_FORKER_THREAD
- Explanation: wb_reason_WB_REASON_FORKER_THREAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `6`
- New: `5`

### Rust Evidence

- Graph edges: `1`

## W-000440 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: wb_reason_WB_REASON_FS_FREE_SPACE
- Explanation: wb_reason_WB_REASON_FS_FREE_SPACE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `4`

### Rust Evidence

- Graph edges: `1`

## W-000441 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: wb_reason_WB_REASON_MAX
- Explanation: wb_reason_WB_REASON_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `7`

### Rust Evidence

- Graph edges: `1`

## W-000442 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ACPI_CA_VERSION
- Explanation: ACPI_CA_VERSION changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x20250807`
- New: `0x20251212`

### Rust Evidence

- Graph edges: `1`

## W-000443 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: BIO_MAX_SECTORS
- Explanation: BIO_MAX_SECTORS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `(UINT_MAX >> SECTOR_SHIFT)`
- New: `(BIO_MAX_SIZE >> SECTOR_SHIFT)`

### Rust Evidence

- Graph edges: `1`

## W-000550 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __getname
- Explanation: __getname changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `kmem_cache_alloc(names_cachep, GFP_KERNEL)`
- New: `kmalloc(PATH_MAX, GFP_KERNEL)`

### Rust Evidence

- Graph edges: `1`

## W-000552 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: res_spin_lock
- Explanation: res_spin_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `resilient_tas_spin_lock(lock)`
- New: `({ grab_held_lock_entry(lock); resilient_tas_spin_lock(lock); })`

### Rust Evidence

- Graph edges: `1`

## W-000444 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: BLK_FEAT_ATOMIC_WRITES
- Explanation: BLK_FEAT_ATOMIC_WRITES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `\`
- New: `((__force blk_features_t)(1u << 14))`

### Rust Evidence

- Graph edges: `0`

## W-000445 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_12M
- Explanation: CLKID_12M changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `71`
- New: `34`

### Rust Evidence

- Graph edges: `0`

## W-000446 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_24M
- Explanation: CLKID_24M changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `70`
- New: `32`

### Rust Evidence

- Graph edges: `0`

## W-000447 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_24M_DIV2
- Explanation: CLKID_24M_DIV2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `120`
- New: `33`

### Rust Evidence

- Graph edges: `0`

## W-000448 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AXI_CLK
- Explanation: CLKID_AXI_CLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `14`

### Rust Evidence

- Graph edges: `0`

## W-000449 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CPU_CLK
- Explanation: CLKID_CPU_CLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `11`
- New: `31`

### Rust Evidence

- Graph edges: `0`

## W-000450 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CPU_CLK_DIV16
- Explanation: CLKID_CPU_CLK_DIV16 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `15`
- New: `34`

### Rust Evidence

- Graph edges: `0`

## W-000451 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_ETH_125M
- Explanation: CLKID_ETH_125M changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `155`
- New: `68`

### Rust Evidence

- Graph edges: `0`

## W-000452 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_ETH_PLL_OSC
- Explanation: CLKID_ETH_PLL_OSC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `7`
- New: `8`

### Rust Evidence

- Graph edges: `0`

## W-000453 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_ETH_RMII
- Explanation: CLKID_ETH_RMII changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `157`
- New: `66`

### Rust Evidence

- Graph edges: `0`

## W-000454 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_ETH_RMII_DIV
- Explanation: CLKID_ETH_RMII_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `156`
- New: `65`

### Rust Evidence

- Graph edges: `0`

## W-000455 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_FCLK_50M
- Explanation: CLKID_FCLK_50M changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `1`
- New: `30`

### Rust Evidence

- Graph edges: `0`

## W-000456 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_FCLK_DIV2P5
- Explanation: CLKID_FCLK_DIV2P5 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `13`
- New: `20`

### Rust Evidence

- Graph edges: `0`

## W-000457 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_FCLK_DIV2P5_DIV
- Explanation: CLKID_FCLK_DIV2P5_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `12`
- New: `19`

### Rust Evidence

- Graph edges: `0`

## W-000458 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HDMI_PLL
- Explanation: CLKID_HDMI_PLL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `20`
- New: `2`

### Rust Evidence

- Graph edges: `0`

## W-000459 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HDMI_PLL_DCO
- Explanation: CLKID_HDMI_PLL_DCO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `18`
- New: `0`

### Rust Evidence

- Graph edges: `0`

## W-000460 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HDMI_PLL_OD
- Explanation: CLKID_HDMI_PLL_OD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `19`
- New: `1`

### Rust Evidence

- Graph edges: `0`

## W-000461 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MALI
- Explanation: CLKID_MALI changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `172`
- New: `63`

### Rust Evidence

- Graph edges: `0`

## W-000462 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MALI_0
- Explanation: CLKID_MALI_0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `72`
- New: `59`

### Rust Evidence

- Graph edges: `0`

## W-000463 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MALI_0_DIV
- Explanation: CLKID_MALI_0_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `71`
- New: `58`

### Rust Evidence

- Graph edges: `0`

## W-000464 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MALI_0_SEL
- Explanation: CLKID_MALI_0_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `70`
- New: `57`

### Rust Evidence

- Graph edges: `0`

## W-000465 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MALI_1
- Explanation: CLKID_MALI_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `75`
- New: `62`

### Rust Evidence

- Graph edges: `0`

## W-000466 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MALI_1_DIV
- Explanation: CLKID_MALI_1_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `74`
- New: `61`

### Rust Evidence

- Graph edges: `0`

## W-000467 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MALI_1_SEL
- Explanation: CLKID_MALI_1_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `73`
- New: `60`

### Rust Evidence

- Graph edges: `0`

## W-000468 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MCLK_PLL
- Explanation: CLKID_MCLK_PLL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `20`
- New: `2`

### Rust Evidence

- Graph edges: `0`

## W-000469 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MCLK_PLL_DCO
- Explanation: CLKID_MCLK_PLL_DCO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `18`
- New: `0`

### Rust Evidence

- Graph edges: `0`

## W-000470 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MCLK_PLL_OSC
- Explanation: CLKID_MCLK_PLL_OSC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `6`

### Rust Evidence

- Graph edges: `0`

## W-000471 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_A
- Explanation: CLKID_PWM_A changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `135`
- New: `101`

### Rust Evidence

- Graph edges: `0`

## W-000472 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_A_DIV
- Explanation: CLKID_PWM_A_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `134`
- New: `100`

### Rust Evidence

- Graph edges: `0`

## W-000473 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_A_SEL
- Explanation: CLKID_PWM_A_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `133`
- New: `99`

### Rust Evidence

- Graph edges: `0`

## W-000474 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_B
- Explanation: CLKID_PWM_B changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `138`
- New: `104`

### Rust Evidence

- Graph edges: `0`

## W-000475 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_B_DIV
- Explanation: CLKID_PWM_B_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `137`
- New: `103`

### Rust Evidence

- Graph edges: `0`

## W-000476 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_B_SEL
- Explanation: CLKID_PWM_B_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `136`
- New: `102`

### Rust Evidence

- Graph edges: `0`

## W-000477 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_C
- Explanation: CLKID_PWM_C changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `141`
- New: `107`

### Rust Evidence

- Graph edges: `0`

## W-000478 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_C_DIV
- Explanation: CLKID_PWM_C_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `140`
- New: `106`

### Rust Evidence

- Graph edges: `0`

## W-000479 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_C_SEL
- Explanation: CLKID_PWM_C_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `139`
- New: `105`

### Rust Evidence

- Graph edges: `0`

## W-000480 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_D
- Explanation: CLKID_PWM_D changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `144`
- New: `110`

### Rust Evidence

- Graph edges: `0`

## W-000481 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_D_DIV
- Explanation: CLKID_PWM_D_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `143`
- New: `109`

### Rust Evidence

- Graph edges: `0`

## W-000482 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_D_SEL
- Explanation: CLKID_PWM_D_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `142`
- New: `108`

### Rust Evidence

- Graph edges: `0`

## W-000483 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_E
- Explanation: CLKID_PWM_E changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `147`
- New: `113`

### Rust Evidence

- Graph edges: `0`

## W-000484 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_E_DIV
- Explanation: CLKID_PWM_E_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `146`
- New: `112`

### Rust Evidence

- Graph edges: `0`

## W-000485 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_E_SEL
- Explanation: CLKID_PWM_E_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `145`
- New: `111`

### Rust Evidence

- Graph edges: `0`

## W-000486 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_F
- Explanation: CLKID_PWM_F changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `150`
- New: `116`

### Rust Evidence

- Graph edges: `0`

## W-000487 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_F_DIV
- Explanation: CLKID_PWM_F_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `149`
- New: `115`

### Rust Evidence

- Graph edges: `0`

## W-000488 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PWM_F_SEL
- Explanation: CLKID_PWM_F_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `148`
- New: `114`

### Rust Evidence

- Graph edges: `0`

## W-000489 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SARADC
- Explanation: CLKID_SARADC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `165`
- New: `98`

### Rust Evidence

- Graph edges: `0`

## W-000490 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SARADC_DIV
- Explanation: CLKID_SARADC_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `164`
- New: `97`

### Rust Evidence

- Graph edges: `0`

## W-000491 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SARADC_SEL
- Explanation: CLKID_SARADC_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `163`
- New: `96`

### Rust Evidence

- Graph edges: `0`

## W-000492 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SC
- Explanation: CLKID_SC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `24`
- New: `17`

### Rust Evidence

- Graph edges: `0`

## W-000493 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_A
- Explanation: CLKID_SD_EMMC_A changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `126`
- New: `71`

### Rust Evidence

- Graph edges: `0`

## W-000494 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_A_DIV
- Explanation: CLKID_SD_EMMC_A_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `144`
- New: `70`

### Rust Evidence

- Graph edges: `0`

## W-000495 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_A_SEL
- Explanation: CLKID_SD_EMMC_A_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `143`
- New: `69`

### Rust Evidence

- Graph edges: `0`

## W-000496 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_B_DIV
- Explanation: CLKID_SD_EMMC_B_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `147`
- New: `73`

### Rust Evidence

- Graph edges: `0`

## W-000497 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_B_SEL
- Explanation: CLKID_SD_EMMC_B_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `146`
- New: `72`

### Rust Evidence

- Graph edges: `0`

## W-000498 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_C_DIV
- Explanation: CLKID_SD_EMMC_C_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `150`
- New: `76`

### Rust Evidence

- Graph edges: `0`

## W-000499 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_C_SEL
- Explanation: CLKID_SD_EMMC_C_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `149`
- New: `75`

### Rust Evidence

- Graph edges: `0`

## W-000500 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SPICC0_DIV
- Explanation: CLKID_SPICC0_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `131`
- New: `79`

### Rust Evidence

- Graph edges: `0`

## W-000501 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SPICC0_SEL
- Explanation: CLKID_SPICC0_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `130`
- New: `78`

### Rust Evidence

- Graph edges: `0`

## W-000502 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_ACODEC
- Explanation: CLKID_SYS_ACODEC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `61`
- New: `161`

### Rust Evidence

- Graph edges: `0`

## W-000503 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_CLK
- Explanation: CLKID_SYS_CLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `9`
- New: `13`

### Rust Evidence

- Graph edges: `0`

## W-000504 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_DOS
- Explanation: CLKID_SYS_DOS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `63`
- New: `142`

### Rust Evidence

- Graph edges: `0`

## W-000505 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_DSPA
- Explanation: CLKID_SYS_DSPA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `38`
- New: `202`

### Rust Evidence

- Graph edges: `0`

## W-000506 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_DSPB
- Explanation: CLKID_SYS_DSPB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `37`
- New: `203`

### Rust Evidence

- Graph edges: `0`

## W-000507 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_GIC
- Explanation: CLKID_SYS_GIC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `27`
- New: `206`

### Rust Evidence

- Graph edges: `0`

## W-000508 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_I2C_M_A
- Explanation: CLKID_SYS_I2C_M_A changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `188`

### Rust Evidence

- Graph edges: `0`

## W-000509 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_I2C_M_B
- Explanation: CLKID_SYS_I2C_M_B changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `49`
- New: `189`

### Rust Evidence

- Graph edges: `0`

## W-000510 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_I2C_M_C
- Explanation: CLKID_SYS_I2C_M_C changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `50`
- New: `190`

### Rust Evidence

- Graph edges: `0`

## W-000511 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_I2C_M_D
- Explanation: CLKID_SYS_I2C_M_D changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `51`
- New: `191`

### Rust Evidence

- Graph edges: `0`

## W-000512 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_IR_CTRL
- Explanation: CLKID_SYS_IR_CTRL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `14`
- New: `164`

### Rust Evidence

- Graph edges: `0`

## W-000513 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_MSR_CLK
- Explanation: CLKID_SYS_MSR_CLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `163`

### Rust Evidence

- Graph edges: `0`

## W-000514 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_PWM_AB
- Explanation: CLKID_SYS_PWM_AB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `37`
- New: `211`

### Rust Evidence

- Graph edges: `0`

## W-000515 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_PWM_CD
- Explanation: CLKID_SYS_PWM_CD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `38`
- New: `212`

### Rust Evidence

- Graph edges: `0`

## W-000516 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_PWM_EF
- Explanation: CLKID_SYS_PWM_EF changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `39`
- New: `213`

### Rust Evidence

- Graph edges: `0`

## W-000517 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_RSA
- Explanation: CLKID_SYS_RSA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `20`
- New: `199`

### Rust Evidence

- Graph edges: `0`

## W-000518 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_SAR_ADC
- Explanation: CLKID_SYS_SAR_ADC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `21`
- New: `205`

### Rust Evidence

- Graph edges: `0`

## W-000519 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_SD_EMMC_A
- Explanation: CLKID_SYS_SD_EMMC_A changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `35`
- New: `157`

### Rust Evidence

- Graph edges: `0`

## W-000520 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_SD_EMMC_B
- Explanation: CLKID_SYS_SD_EMMC_B changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `68`
- New: `158`

### Rust Evidence

- Graph edges: `0`

## W-000521 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_SD_EMMC_C
- Explanation: CLKID_SYS_SD_EMMC_C changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `36`
- New: `159`

### Rust Evidence

- Graph edges: `0`

## W-000522 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_SPIFC
- Explanation: CLKID_SYS_SPIFC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `24`
- New: `162`

### Rust Evidence

- Graph edges: `0`

## W-000523 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_UART_A
- Explanation: CLKID_SYS_UART_A changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `43`
- New: `167`

### Rust Evidence

- Graph edges: `0`

## W-000524 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_UART_B
- Explanation: CLKID_SYS_UART_B changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `44`
- New: `168`

### Rust Evidence

- Graph edges: `0`

## W-000525 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_UART_C
- Explanation: CLKID_SYS_UART_C changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `45`
- New: `169`

### Rust Evidence

- Graph edges: `0`

## W-000526 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_UART_D
- Explanation: CLKID_SYS_UART_D changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `46`
- New: `170`

### Rust Evidence

- Graph edges: `0`

## W-000527 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_UART_E
- Explanation: CLKID_SYS_UART_E changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `47`
- New: `171`

### Rust Evidence

- Graph edges: `0`

## W-000528 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_UART_F
- Explanation: CLKID_SYS_UART_F changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `18`
- New: `172`

### Rust Evidence

- Graph edges: `0`

## W-000529 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_USB
- Explanation: CLKID_SYS_USB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `34`
- New: `184`

### Rust Evidence

- Graph edges: `0`

## W-000530 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_TS
- Explanation: CLKID_TS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `69`
- New: `46`

### Rust Evidence

- Graph edges: `0`

## W-000531 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_TS_DIV
- Explanation: CLKID_TS_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `152`
- New: `45`

### Rust Evidence

- Graph edges: `0`

## W-000532 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_HDMI
- Explanation: CLK_HDMI changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `344`
- New: `50`

### Rust Evidence

- Graph edges: `0`

## W-000533 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_I2C0
- Explanation: CLK_I2C0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `294`
- New: `38`

### Rust Evidence

- Graph edges: `0`

## W-000534 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_I2C1
- Explanation: CLK_I2C1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `295`
- New: `39`

### Rust Evidence

- Graph edges: `0`

## W-000535 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_I2C2
- Explanation: CLK_I2C2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `296`
- New: `40`

### Rust Evidence

- Graph edges: `0`

## W-000536 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_I2C3
- Explanation: CLK_I2C3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `297`
- New: `41`

### Rust Evidence

- Graph edges: `0`

## W-000537 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_I2C4
- Explanation: CLK_I2C4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `298`
- New: `42`

### Rust Evidence

- Graph edges: `0`

## W-000538 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_I2C5
- Explanation: CLK_I2C5 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `299`
- New: `43`

### Rust Evidence

- Graph edges: `0`

## W-000539 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_PCM1
- Explanation: CLK_PCM1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `309`
- New: `81`

### Rust Evidence

- Graph edges: `0`

## W-000540 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SPDIF
- Explanation: CLK_SPDIF changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `312`
- New: `51`

### Rust Evidence

- Graph edges: `0`

## W-000541 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SPI0
- Explanation: CLK_SPI0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `304`
- New: `62`

### Rust Evidence

- Graph edges: `0`

## W-000542 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SPI1
- Explanation: CLK_SPI1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `305`
- New: `63`

### Rust Evidence

- Graph edges: `0`

## W-000543 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SPI2
- Explanation: CLK_SPI2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `306`
- New: `64`

### Rust Evidence

- Graph edges: `0`

## W-000544 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_UART0
- Explanation: CLK_UART0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `289`
- New: `67`

### Rust Evidence

- Graph edges: `0`

## W-000545 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_UART1
- Explanation: CLK_UART1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `290`
- New: `68`

### Rust Evidence

- Graph edges: `0`

## W-000546 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_UART2
- Explanation: CLK_UART2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `291`
- New: `69`

### Rust Evidence

- Graph edges: `0`

## W-000547 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_UART3
- Explanation: CLK_UART3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `292`
- New: `70`

### Rust Evidence

- Graph edges: `0`

## W-000548 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_UART4
- Explanation: CLK_UART4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `293`
- New: `71`

### Rust Evidence

- Graph edges: `0`

## W-000549 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SLAB_NO_OBJ_EXT
- Explanation: SLAB_NO_OBJ_EXT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `__SLAB_FLAG_UNUSED`
- New: `__SLAB_FLAG_BIT(_SLAB_NO_OBJ_EXT)`

### Rust Evidence

- Graph edges: `0`

## W-000551 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: __putname
- Explanation: __putname changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `kmem_cache_free(names_cachep, (void *)(name))`
- New: `kfree(name)`

### Rust Evidence

- Graph edges: `0`
