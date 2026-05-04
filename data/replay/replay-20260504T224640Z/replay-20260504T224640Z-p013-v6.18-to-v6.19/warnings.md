# BindDrift Ranked Warnings

## W-000491 SignatureDrift

- Risk: High
- Score: 14.6
- Symbol: l
- Explanation: l changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `50`

## W-000632 SignatureDrift

- Risk: High
- Score: 14.6
- Symbol: rb_first
- Explanation: rb_first changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*const rb_root'}], 'return_type': '*mut rb_node'}`
- New: `{'params': [{'name': 'root', 'type': '*const rb_root'}], 'return_type': '*mut rb_node'}`

### Rust Evidence

- Graph edges: `25`

## W-001226 SignatureDrift

- Risk: High
- Score: 14.6
- Symbol: sha256
- Explanation: sha256 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const u8 *data', 'size_t len', 'u8 out[SHA256_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['const u8 *data', 'size_t len', 'u8 out[at_least SHA256_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `20`

## W-000629 SignatureDrift

- Risk: High
- Score: 14.2
- Symbol: pwmchip_get_drvdata
- Explanation: pwmchip_get_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `18`

## W-001179 SignatureDrift

- Risk: High
- Score: 14.0
- Symbol: dev_get_drvdata
- Explanation: dev_get_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['&pdev->dev'], 'return_type': 'return'}`
- New: `{'params': ['&intf->dev'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `17`

## W-001231 SignatureDrift

- Risk: High
- Score: 14.0
- Symbol: sha512
- Explanation: sha512 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const u8 *data', 'size_t len', 'u8 out[SHA512_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['const u8 *data', 'size_t len', 'u8 out[at_least SHA512_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `17`

## W-001253 NullabilityDrift

- Risk: High
- Score: 13.7
- Symbol: pwmchip_alloc
- Explanation: pwmchip_alloc has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE', 'ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/include/linux/pwm.h:567 `return ERR_PTR(-EINVAL);`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/rust/kernel/pwm.rs:583 `bound_parent_device` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/rust/kernel/pwm.rs:595 `bound_parent_device` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/rust/kernel/pwm.rs:578 `// SAFETY: Per the function's safety contract, the parent device is bound.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/rust/kernel/pwm.rs:583 `/// Allocates and wraps a PWM chip using `bindings::pwmchip_alloc`.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/rust/kernel/pwm.rs:584 `///`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/rust/kernel/pwm.rs:585 `AREF`

## W-000300 SignatureDrift

- Risk: High
- Score: 13.6
- Symbol: i2c_get_adapter
- Explanation: i2c_get_adapter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `15`

## W-000836 FieldDrift

- Risk: High
- Score: 13.6
- Symbol: drm_device
- Explanation: drm_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'if_version', 'type': 'ffi::c_int'}, {'name': 'ref_', 'type': 'kref'}, {'name': 'dev', 'type': '*mut device'}, {'name': 'dma_dev', 'type': '*mut device'}, {'name': 'managed', 'type': 'drm_device__bindgen_ty_1'}, {'name': 'driver', 'type': '*const drm_driver'}, {'name': 'dev_private', 'type': '*mut ffi::c_void'}, {'name': 'primary', 'type': '*mut drm_minor'}, {'name': 'render', 'type': '*mut drm_minor'}, {'name': 'accel', 'type': '*mut drm_minor'}, {'name': 'registered', 'type': 'bool_'}, {'name': 'master', 'type': '*mut drm_master'}, {'name': 'driver_features', 'type': 'u32_'}, {'name': 'unplugged', 'type': 'bool_'}, {'name': 'anon_inode', 'type': '*mut inode'}, {'name': 'unique', 'type': '*mut ffi::c_char'}, {'name': 'master_mutex', 'type': 'mutex'}, {'name': 'open_count', 'type': 'atomic_t'}, {'name': 'filelist_mutex', 'type': 'mutex'}, {'name': 'filelist', 'type': 'list_head'}, {'name': 'filelist_internal', 'type': 'list_head'}, {'name': 'clientlist_mutex', 'type': 'mutex'}, {'name': 'clientlist', 'type': 'list_head'}, {'name': 'vblank_disable_immediate', 'type': 'bool_'}, {'name': 'vblank', 'type': '*mut drm_vblank_crtc'}, {'name': 'vblank_time_lock', 'type': 'spinlock_t'}, {'name': 'vbl_lock', 'type': 'spinlock_t'}, {'name': 'max_vblank_count', 'type': 'u32_'}, {'name': 'vblank_event_list', 'type': 'list_head'}, {'name': 'event_lock', 'type': 'spinlock_t'}, {'name': 'num_crtcs', 'type': 'ffi::c_uint'}, {'name': 'mode_config', 'type': 'drm_mode_config'}, {'name': 'object_name_lock', 'type': 'mutex'}, {'name': 'object_name_idr', 'type': 'idr'}, {'name': 'vma_offset_manager', 'type': '*mut drm_vma_offset_manager'}, {'name': 'vram_mm', 'type': '*mut drm_vram_mm'}, {'name': 'switch_power_state', 'type': 'switch_power_state'}, {'name': 'fb_helper', 'type': '*mut drm_fb_helper'}, {'name': 'debugfs_root', 'type': '*mut dentry'}]`
- New: `[{'name': 'if_version', 'type': 'ffi::c_int'}, {'name': 'ref_', 'type': 'kref'}, {'name': 'dev', 'type': '*mut device'}, {'name': 'dma_dev', 'type': '*mut device'}, {'name': 'managed', 'type': 'drm_device__bindgen_ty_1'}, {'name': 'driver', 'type': '*const drm_driver'}, {'name': 'dev_private', 'type': '*mut ffi::c_void'}, {'name': 'primary', 'type': '*mut drm_minor'}, {'name': 'render', 'type': '*mut drm_minor'}, {'name': 'accel', 'type': '*mut drm_minor'}, {'name': 'registered', 'type': 'bool_'}, {'name': 'master', 'type': '*mut drm_master'}, {'name': 'driver_features', 'type': 'u32_'}, {'name': 'unplugged', 'type': 'bool_'}, {'name': 'anon_inode', 'type': '*mut inode'}, {'name': 'unique', 'type': '*mut ffi::c_char'}, {'name': 'master_mutex', 'type': 'mutex'}, {'name': 'open_count', 'type': 'atomic_t'}, {'name': 'filelist_mutex', 'type': 'mutex'}, {'name': 'filelist', 'type': 'list_head'}, {'name': 'filelist_internal', 'type': 'list_head'}, {'name': 'clientlist_mutex', 'type': 'mutex'}, {'name': 'clientlist', 'type': 'list_head'}, {'name': 'client_sysrq_list', 'type': 'list_head'}, {'name': 'vblank_disable_immediate', 'type': 'bool_'}, {'name': 'vblank', 'type': '*mut drm_vblank_crtc'}, {'name': 'vblank_time_lock', 'type': 'spinlock_t'}, {'name': 'vbl_lock', 'type': 'spinlock_t'}, {'name': 'max_vblank_count', 'type': 'u32_'}, {'name': 'vblank_event_list', 'type': 'list_head'}, {'name': 'event_lock', 'type': 'spinlock_t'}, {'name': 'num_crtcs', 'type': 'ffi::c_uint'}, {'name': 'mode_config', 'type': 'drm_mode_config'}, {'name': 'object_name_lock', 'type': 'mutex'}, {'name': 'object_name_idr', 'type': 'idr'}, {'name': 'vma_offset_manager', 'type': '*mut drm_vma_offset_manager'}, {'name': 'vram_mm', 'type': '*mut drm_vram_mm'}, {'name': 'switch_power_state', 'type': 'switch_power_state'}, {'name': 'fb_helper', 'type': '*mut drm_fb_helper'}, {'name': 'debugfs_root', 'type': '*mut dentry'}]`

### Rust Evidence

- Graph edges: `50`

## W-001224 SignatureDrift

- Risk: High
- Score: 13.4
- Symbol: sha224
- Explanation: sha224 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const u8 *data', 'size_t len', 'u8 out[SHA224_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['const u8 *data', 'size_t len', 'u8 out[at_least SHA224_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `14`

## W-001229 SignatureDrift

- Risk: High
- Score: 13.4
- Symbol: sha384
- Explanation: sha384 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const u8 *data', 'size_t len', 'u8 out[SHA384_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['const u8 *data', 'size_t len', 'u8 out[at_least SHA384_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `14`

## W-000633 SignatureDrift

- Risk: High
- Score: 13.2
- Symbol: rb_last
- Explanation: rb_last changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*const rb_root'}], 'return_type': '*mut rb_node'}`
- New: `{'params': [{'name': 'root', 'type': '*const rb_root'}], 'return_type': '*mut rb_node'}`

### Rust Evidence

- Graph edges: `13`

## W-001251 NullabilityDrift

- Risk: High
- Score: 12.8
- Symbol: i2c_verify_client
- Explanation: i2c_verify_client has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/include/linux/i2c.h:493 `return NULL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/rust/kernel/i2c.rs:525 `try_from` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/rust/kernel/i2c.rs:523 `// SAFETY: By the type invariant of `Device`, `dev.as_raw()` is a valid pointer to a`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/rust/kernel/i2c.rs:522 `RESULT_RETURN`

## W-000822 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: bio
- Explanation: bio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'bi_next', 'type': '*mut bio'}, {'name': 'bi_bdev', 'type': '*mut block_device'}, {'name': 'bi_opf', 'type': 'blk_opf_t'}, {'name': 'bi_flags', 'type': 'ffi::c_ushort'}, {'name': 'bi_ioprio', 'type': 'ffi::c_ushort'}, {'name': 'bi_write_hint', 'type': 'rw_hint'}, {'name': 'bi_write_stream', 'type': 'u8_'}, {'name': 'bi_status', 'type': 'blk_status_t'}, {'name': '__bi_remaining', 'type': 'atomic_t'}, {'name': 'bi_iter', 'type': 'bvec_iter'}, {'name': '__bindgen_anon_1', 'type': 'bio__bindgen_ty_1'}, {'name': 'bi_end_io', 'type': 'bio_end_io_t'}, {'name': 'bi_private', 'type': '*mut ffi::c_void'}, {'name': 'bi_blkg', 'type': '*mut blkcg_gq'}, {'name': 'issue_time_ns', 'type': 'u64_'}, {'name': 'bi_iocost_cost', 'type': 'u64_'}, {'name': 'bi_vcnt', 'type': 'ffi::c_ushort'}, {'name': 'bi_max_vecs', 'type': 'ffi::c_ushort'}, {'name': '__bi_cnt', 'type': 'atomic_t'}, {'name': 'bi_io_vec', 'type': '*mut bio_vec'}, {'name': 'bi_pool', 'type': '*mut bio_set'}]`
- New: `[{'name': 'bi_next', 'type': '*mut bio'}, {'name': 'bi_bdev', 'type': '*mut block_device'}, {'name': 'bi_opf', 'type': 'blk_opf_t'}, {'name': 'bi_flags', 'type': 'ffi::c_ushort'}, {'name': 'bi_ioprio', 'type': 'ffi::c_ushort'}, {'name': 'bi_write_hint', 'type': 'rw_hint'}, {'name': 'bi_write_stream', 'type': 'u8_'}, {'name': 'bi_status', 'type': 'blk_status_t'}, {'name': 'bi_bvec_gap_bit', 'type': 'u8_'}, {'name': '__bi_remaining', 'type': 'atomic_t'}, {'name': 'bi_iter', 'type': 'bvec_iter'}, {'name': '__bindgen_anon_1', 'type': 'bio__bindgen_ty_1'}, {'name': 'bi_end_io', 'type': 'bio_end_io_t'}, {'name': 'bi_private', 'type': '*mut ffi::c_void'}, {'name': 'bi_blkg', 'type': '*mut blkcg_gq'}, {'name': 'issue_time_ns', 'type': 'u64_'}, {'name': 'bi_iocost_cost', 'type': 'u64_'}, {'name': 'bi_vcnt', 'type': 'ffi::c_ushort'}, {'name': 'bi_max_vecs', 'type': 'ffi::c_ushort'}, {'name': '__bi_cnt', 'type': 'atomic_t'}, {'name': 'bi_io_vec', 'type': '*mut bio_vec'}, {'name': 'bi_pool', 'type': '*mut bio_set'}]`

### Rust Evidence

- Graph edges: `50`

## W-000827 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: cgroup
- Explanation: cgroup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'self_', 'type': 'cgroup_subsys_state'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'level', 'type': 'ffi::c_int'}, {'name': 'max_depth', 'type': 'ffi::c_int'}, {'name': 'nr_descendants', 'type': 'ffi::c_int'}, {'name': 'nr_dying_descendants', 'type': 'ffi::c_int'}, {'name': 'max_descendants', 'type': 'ffi::c_int'}, {'name': 'nr_populated_csets', 'type': 'ffi::c_int'}, {'name': 'nr_populated_domain_children', 'type': 'ffi::c_int'}, {'name': 'nr_populated_threaded_children', 'type': 'ffi::c_int'}, {'name': 'nr_threaded_children', 'type': 'ffi::c_int'}, {'name': 'kill_seq', 'type': 'ffi::c_uint'}, {'name': 'kn', 'type': '*mut kernfs_node'}, {'name': 'procs_file', 'type': 'cgroup_file'}, {'name': 'events_file', 'type': 'cgroup_file'}, {'name': 'psi_files', 'type': '__IncompleteArrayField<cgroup_file>'}, {'name': 'subtree_control', 'type': 'u16_'}, {'name': 'subtree_ss_mask', 'type': 'u16_'}, {'name': 'old_subtree_control', 'type': 'u16_'}, {'name': 'old_subtree_ss_mask', 'type': 'u16_'}, {'name': 'subsys', 'type': '[*mut cgroup_subsys_state; 14usize]'}, {'name': 'nr_dying_subsys', 'type': '[ffi::c_int; 14usize]'}, {'name': 'root', 'type': '*mut cgroup_root'}, {'name': 'cset_links', 'type': 'list_head'}, {'name': 'e_csets', 'type': '[list_head; 14usize]'}, {'name': 'dom_cgrp', 'type': '*mut cgroup'}, {'name': 'old_dom_cgrp', 'type': '*mut cgroup'}, {'name': 'rstat_base_cpu', 'type': '*mut cgroup_rstat_base_cpu'}, {'name': '__bindgen_padding_0', 'type': 'u64'}, {'name': '_pad_', 'type': 'cacheline_padding'}, {'name': 'last_bstat', 'type': 'cgroup_base_stat'}, {'name': 'bstat', 'type': 'cgroup_base_stat'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'pidlists', 'type': 'list_head'}, {'name': 'pidlist_mutex', 'type': 'mutex'}, {'name': 'offline_waitq', 'type': 'wait_queue_head_t'}, {'name': 'release_agent_work', 'type': 'work_struct'}, {'name': 'psi', 'type': '*mut psi_group'}, {'name': 'bpf', 'type': 'cgroup_bpf'}, {'name': 'freezer', 'type': 'cgroup_freezer_state'}, {'name': 'ancestors', 'type': '__IncompleteArrayField<*mut cgroup>'}]`
- New: `[{'name': 'self_', 'type': 'cgroup_subsys_state'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'level', 'type': 'ffi::c_int'}, {'name': 'max_depth', 'type': 'ffi::c_int'}, {'name': 'nr_descendants', 'type': 'ffi::c_int'}, {'name': 'nr_dying_descendants', 'type': 'ffi::c_int'}, {'name': 'max_descendants', 'type': 'ffi::c_int'}, {'name': 'nr_populated_csets', 'type': 'ffi::c_int'}, {'name': 'nr_populated_domain_children', 'type': 'ffi::c_int'}, {'name': 'nr_populated_threaded_children', 'type': 'ffi::c_int'}, {'name': 'nr_threaded_children', 'type': 'ffi::c_int'}, {'name': 'kill_seq', 'type': 'ffi::c_uint'}, {'name': 'kn', 'type': '*mut kernfs_node'}, {'name': 'procs_file', 'type': 'cgroup_file'}, {'name': 'events_file', 'type': 'cgroup_file'}, {'name': 'psi_files', 'type': '__IncompleteArrayField<cgroup_file>'}, {'name': 'subtree_control', 'type': 'u16_'}, {'name': 'subtree_ss_mask', 'type': 'u16_'}, {'name': 'old_subtree_control', 'type': 'u16_'}, {'name': 'old_subtree_ss_mask', 'type': 'u16_'}, {'name': 'subsys', 'type': '[*mut cgroup_subsys_state; 14usize]'}, {'name': 'nr_dying_subsys', 'type': '[ffi::c_int; 14usize]'}, {'name': 'root', 'type': '*mut cgroup_root'}, {'name': 'cset_links', 'type': 'list_head'}, {'name': 'e_csets', 'type': '[list_head; 14usize]'}, {'name': 'dom_cgrp', 'type': '*mut cgroup'}, {'name': 'old_dom_cgrp', 'type': '*mut cgroup'}, {'name': 'rstat_base_cpu', 'type': '*mut cgroup_rstat_base_cpu'}, {'name': '__bindgen_padding_0', 'type': 'u64'}, {'name': '_pad_', 'type': 'cacheline_padding'}, {'name': 'last_bstat', 'type': 'cgroup_base_stat'}, {'name': 'bstat', 'type': 'cgroup_base_stat'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'pidlists', 'type': 'list_head'}, {'name': 'pidlist_mutex', 'type': 'mutex'}, {'name': 'offline_waitq', 'type': 'wait_queue_head_t'}, {'name': 'release_agent_work', 'type': 'work_struct'}, {'name': 'psi', 'type': '*mut psi_group'}, {'name': 'bpf', 'type': 'cgroup_bpf'}, {'name': 'freezer', 'type': 'cgroup_freezer_state'}, {'name': '__bindgen_anon_1', 'type': 'cgroup__bindgen_ty_1'}]`

### Rust Evidence

- Graph edges: `50`

## W-000837 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: drm_file
- Explanation: drm_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'authenticated', 'type': 'bool_'}, {'name': 'stereo_allowed', 'type': 'bool_'}, {'name': 'universal_planes', 'type': 'bool_'}, {'name': 'atomic', 'type': 'bool_'}, {'name': 'aspect_ratio_allowed', 'type': 'bool_'}, {'name': 'writeback_connectors', 'type': 'bool_'}, {'name': 'was_master', 'type': 'bool_'}, {'name': 'is_master', 'type': 'bool_'}, {'name': 'supports_virtualized_cursor_plane', 'type': 'bool_'}, {'name': 'master', 'type': '*mut drm_master'}, {'name': 'master_lookup_lock', 'type': 'spinlock_t'}, {'name': 'pid', 'type': '*mut pid'}, {'name': 'client_id', 'type': 'u64_'}, {'name': 'magic', 'type': 'drm_magic_t'}, {'name': 'lhead', 'type': 'list_head'}, {'name': 'minor', 'type': '*mut drm_minor'}, {'name': 'object_idr', 'type': 'idr'}, {'name': 'table_lock', 'type': 'spinlock_t'}, {'name': 'syncobj_idr', 'type': 'idr'}, {'name': 'syncobj_table_lock', 'type': 'spinlock_t'}, {'name': 'filp', 'type': '*mut file'}, {'name': 'driver_priv', 'type': '*mut ffi::c_void'}, {'name': 'fbs', 'type': 'list_head'}, {'name': 'fbs_lock', 'type': 'mutex'}, {'name': 'blobs', 'type': 'list_head'}, {'name': 'event_wait', 'type': 'wait_queue_head_t'}, {'name': 'pending_event_list', 'type': 'list_head'}, {'name': 'event_list', 'type': 'list_head'}, {'name': 'event_space', 'type': 'ffi::c_int'}, {'name': 'event_read_lock', 'type': 'mutex'}, {'name': 'prime', 'type': 'drm_prime_file_private'}, {'name': 'client_name', 'type': '*const ffi::c_char'}, {'name': 'client_name_lock', 'type': 'mutex'}, {'name': 'debugfs_client', 'type': '*mut dentry'}]`
- New: `[{'name': 'authenticated', 'type': 'bool_'}, {'name': 'stereo_allowed', 'type': 'bool_'}, {'name': 'universal_planes', 'type': 'bool_'}, {'name': 'atomic', 'type': 'bool_'}, {'name': 'aspect_ratio_allowed', 'type': 'bool_'}, {'name': 'writeback_connectors', 'type': 'bool_'}, {'name': 'plane_color_pipeline', 'type': 'bool_'}, {'name': 'was_master', 'type': 'bool_'}, {'name': 'is_master', 'type': 'bool_'}, {'name': 'supports_virtualized_cursor_plane', 'type': 'bool_'}, {'name': 'master', 'type': '*mut drm_master'}, {'name': 'master_lookup_lock', 'type': 'spinlock_t'}, {'name': 'pid', 'type': '*mut pid'}, {'name': 'client_id', 'type': 'u64_'}, {'name': 'magic', 'type': 'drm_magic_t'}, {'name': 'lhead', 'type': 'list_head'}, {'name': 'minor', 'type': '*mut drm_minor'}, {'name': 'object_idr', 'type': 'idr'}, {'name': 'table_lock', 'type': 'spinlock_t'}, {'name': 'syncobj_idr', 'type': 'idr'}, {'name': 'syncobj_table_lock', 'type': 'spinlock_t'}, {'name': 'filp', 'type': '*mut file'}, {'name': 'driver_priv', 'type': '*mut ffi::c_void'}, {'name': 'fbs', 'type': 'list_head'}, {'name': 'fbs_lock', 'type': 'mutex'}, {'name': 'blobs', 'type': 'list_head'}, {'name': 'event_wait', 'type': 'wait_queue_head_t'}, {'name': 'pending_event_list', 'type': 'list_head'}, {'name': 'event_list', 'type': 'list_head'}, {'name': 'event_space', 'type': 'ffi::c_int'}, {'name': 'event_read_lock', 'type': 'mutex'}, {'name': 'prime', 'type': 'drm_prime_file_private'}, {'name': 'client_name', 'type': '*const ffi::c_char'}, {'name': 'client_name_lock', 'type': 'mutex'}, {'name': 'debugfs_client', 'type': '*mut dentry'}]`

### Rust Evidence

- Graph edges: `47`

## W-000841 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: inode
- Explanation: inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'i_mode', 'type': 'umode_t'}, {'name': 'i_opflags', 'type': 'ffi::c_ushort'}, {'name': 'i_uid', 'type': 'kuid_t'}, {'name': 'i_gid', 'type': 'kgid_t'}, {'name': 'i_flags', 'type': 'ffi::c_uint'}, {'name': 'i_acl', 'type': '*mut posix_acl'}, {'name': 'i_default_acl', 'type': '*mut posix_acl'}, {'name': 'i_op', 'type': '*const inode_operations'}, {'name': 'i_sb', 'type': '*mut super_block'}, {'name': 'i_mapping', 'type': '*mut address_space'}, {'name': 'i_security', 'type': '*mut ffi::c_void'}, {'name': 'i_ino', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'inode__bindgen_ty_1'}, {'name': 'i_rdev', 'type': 'dev_t'}, {'name': 'i_size', 'type': 'loff_t'}, {'name': 'i_atime_sec', 'type': 'time64_t'}, {'name': 'i_mtime_sec', 'type': 'time64_t'}, {'name': 'i_ctime_sec', 'type': 'time64_t'}, {'name': 'i_atime_nsec', 'type': 'u32_'}, {'name': 'i_mtime_nsec', 'type': 'u32_'}, {'name': 'i_ctime_nsec', 'type': 'u32_'}, {'name': 'i_generation', 'type': 'u32_'}, {'name': 'i_lock', 'type': 'spinlock_t'}, {'name': 'i_bytes', 'type': 'ffi::c_ushort'}, {'name': 'i_blkbits', 'type': 'u8_'}, {'name': 'i_write_hint', 'type': 'rw_hint'}, {'name': 'i_blocks', 'type': 'blkcnt_t'}, {'name': 'i_state', 'type': 'inode_state_flags_t'}, {'name': 'i_rwsem', 'type': 'rw_semaphore'}, {'name': 'dirtied_when', 'type': 'ffi::c_ulong'}, {'name': 'dirtied_time_when', 'type': 'ffi::c_ulong'}, {'name': 'i_hash', 'type': 'hlist_node'}, {'name': 'i_io_list', 'type': 'list_head'}, {'name': 'i_lru', 'type': 'list_head'}, {'name': 'i_sb_list', 'type': 'list_head'}, {'name': 'i_wb_list', 'type': 'list_head'}, {'name': '__bindgen_anon_2', 'type': 'inode__bindgen_ty_2'}, {'name': 'i_version', 'type': 'atomic64_t'}, {'name': 'i_sequence', 'type': 'atomic64_t'}, {'name': 'i_count', 'type': 'atomic_t'}, {'name': 'i_dio_count', 'type': 'atomic_t'}, {'name': 'i_writecount', 'type': 'atomic_t'}, {'name': 'i_readcount', 'type': 'atomic_t'}, {'name': '__bindgen_anon_3', 'type': 'inode__bindgen_ty_3'}, {'name': 'i_flctx', 'type': '*mut file_lock_context'}, {'name': 'i_data', 'type': 'address_space'}, {'name': '__bindgen_anon_4', 'type': 'inode__bindgen_ty_4'}, {'name': '__bindgen_anon_5', 'type': 'inode__bindgen_ty_5'}, {'name': 'i_fsnotify_mask', 'type': '__u32'}, {'name': 'i_fsnotify_marks', 'type': '*mut fsnotify_mark_connector'}, {'name': 'i_private', 'type': '*mut ffi::c_void'}]`
- New: `[{'name': 'i_mode', 'type': 'umode_t'}, {'name': 'i_opflags', 'type': 'ffi::c_ushort'}, {'name': 'i_flags', 'type': 'ffi::c_uint'}, {'name': 'i_acl', 'type': '*mut posix_acl'}, {'name': 'i_default_acl', 'type': '*mut posix_acl'}, {'name': 'i_uid', 'type': 'kuid_t'}, {'name': 'i_gid', 'type': 'kgid_t'}, {'name': 'i_op', 'type': '*const inode_operations'}, {'name': 'i_sb', 'type': '*mut super_block'}, {'name': 'i_mapping', 'type': '*mut address_space'}, {'name': 'i_security', 'type': '*mut ffi::c_void'}, {'name': 'i_ino', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'inode__bindgen_ty_1'}, {'name': 'i_rdev', 'type': 'dev_t'}, {'name': 'i_size', 'type': 'loff_t'}, {'name': 'i_atime_sec', 'type': 'time64_t'}, {'name': 'i_mtime_sec', 'type': 'time64_t'}, {'name': 'i_ctime_sec', 'type': 'time64_t'}, {'name': 'i_atime_nsec', 'type': 'u32_'}, {'name': 'i_mtime_nsec', 'type': 'u32_'}, {'name': 'i_ctime_nsec', 'type': 'u32_'}, {'name': 'i_generation', 'type': 'u32_'}, {'name': 'i_lock', 'type': 'spinlock_t'}, {'name': 'i_bytes', 'type': 'ffi::c_ushort'}, {'name': 'i_blkbits', 'type': 'u8_'}, {'name': 'i_write_hint', 'type': 'rw_hint'}, {'name': 'i_blocks', 'type': 'blkcnt_t'}, {'name': 'i_state', 'type': 'inode_state_flags'}, {'name': 'i_rwsem', 'type': 'rw_semaphore'}, {'name': 'dirtied_when', 'type': 'ffi::c_ulong'}, {'name': 'dirtied_time_when', 'type': 'ffi::c_ulong'}, {'name': 'i_hash', 'type': 'hlist_node'}, {'name': 'i_io_list', 'type': 'list_head'}, {'name': 'i_lru', 'type': 'list_head'}, {'name': 'i_sb_list', 'type': 'list_head'}, {'name': 'i_wb_list', 'type': 'list_head'}, {'name': '__bindgen_anon_2', 'type': 'inode__bindgen_ty_2'}, {'name': 'i_version', 'type': 'atomic64_t'}, {'name': 'i_sequence', 'type': 'atomic64_t'}, {'name': 'i_count', 'type': 'atomic_t'}, {'name': 'i_dio_count', 'type': 'atomic_t'}, {'name': 'i_writecount', 'type': 'atomic_t'}, {'name': 'i_readcount', 'type': 'atomic_t'}, {'name': '__bindgen_anon_3', 'type': 'inode__bindgen_ty_3'}, {'name': 'i_flctx', 'type': '*mut file_lock_context'}, {'name': 'i_data', 'type': 'address_space'}, {'name': '__bindgen_anon_4', 'type': 'inode__bindgen_ty_4'}, {'name': '__bindgen_anon_5', 'type': 'inode__bindgen_ty_5'}, {'name': 'i_fsnotify_mask', 'type': '__u32'}, {'name': 'i_fsnotify_marks', 'type': '*mut fsnotify_mark_connector'}, {'name': 'i_private', 'type': '*mut ffi::c_void'}]`

### Rust Evidence

- Graph edges: `50`

## W-000843 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: irq_domain
- Explanation: irq_domain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'link', 'type': 'list_head'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'ops', 'type': '*const irq_domain_ops'}, {'name': 'host_data', 'type': '*mut ffi::c_void'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'mapcount', 'type': 'ffi::c_uint'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'root', 'type': '*mut irq_domain'}, {'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'bus_token', 'type': 'irq_domain_bus_token'}, {'name': 'gc', 'type': '*mut irq_domain_chip_generic'}, {'name': 'dev', 'type': '*mut device'}, {'name': 'pm_dev', 'type': '*mut device'}, {'name': 'parent', 'type': '*mut irq_domain'}, {'name': 'msi_parent_ops', 'type': '*const msi_parent_ops'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn(d: *mut irq_domain)>'}, {'name': 'hwirq_max', 'type': 'irq_hw_number_t'}, {'name': 'revmap_size', 'type': 'ffi::c_uint'}, {'name': 'revmap_tree', 'type': 'xarray'}, {'name': 'revmap', 'type': '__IncompleteArrayField<*mut irq_data>'}]`

### Rust Evidence

- Graph edges: `50`

## W-000846 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: kiocb
- Explanation: kiocb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'ki_filp', 'type': '*mut file'}, {'name': 'ki_pos', 'type': 'loff_t'}, {'name': 'private', 'type': '*mut ffi::c_void'}, {'name': 'ki_flags', 'type': 'ffi::c_int'}, {'name': 'ki_ioprio', 'type': 'u16_'}, {'name': 'ki_write_stream', 'type': 'u8_'}, {'name': '__bindgen_anon_1', 'type': 'kiocb__bindgen_ty_1'}]`
- New: `[{'name': 'ki_filp', 'type': '*mut file'}, {'name': 'ki_pos', 'type': 'loff_t'}, {'name': 'private', 'type': '*mut ffi::c_void'}, {'name': 'ki_flags', 'type': 'ffi::c_int'}, {'name': 'ki_ioprio', 'type': 'u16_'}, {'name': 'ki_write_stream', 'type': 'u8_'}, {'name': 'ki_waitq', 'type': '*mut wait_page_queue'}]`

### Rust Evidence

- Graph edges: `35`

## W-000848 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: mm_struct
- Explanation: mm_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'mm_struct__bindgen_ty_1'}, {'name': 'cpu_bitmap', 'type': '__IncompleteArrayField<ffi::c_ulong>'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'mm_struct__bindgen_ty_1'}, {'name': 'flexible_array', 'type': '__IncompleteArrayField<ffi::c_char>'}]`

### Rust Evidence

- Graph edges: `29`

## W-000852 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: phy_device
- Explanation: phy_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mdio', 'type': 'mdio_device'}, {'name': 'drv', 'type': '*const phy_driver'}, {'name': 'devlink', 'type': '*mut device_link'}, {'name': 'phyindex', 'type': 'u32_'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'c45_ids', 'type': 'phy_c45_device_ids'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'rate_matching', 'type': 'ffi::c_int'}, {'name': 'state', 'type': 'phy_state'}, {'name': 'dev_flags', 'type': 'u32_'}, {'name': 'interface', 'type': 'phy_interface_t'}, {'name': 'possible_interfaces', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'speed', 'type': 'ffi::c_int'}, {'name': 'duplex', 'type': 'ffi::c_int'}, {'name': 'port', 'type': 'ffi::c_int'}, {'name': 'pause', 'type': 'ffi::c_int'}, {'name': 'asym_pause', 'type': 'ffi::c_int'}, {'name': 'master_slave_get', 'type': 'u8_'}, {'name': 'master_slave_set', 'type': 'u8_'}, {'name': 'master_slave_state', 'type': 'u8_'}, {'name': 'supported', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'advertising', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'lp_advertising', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'adv_old', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'supported_eee', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'advertising_eee', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'eee_disabled_modes', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'enable_tx_lpi', 'type': 'bool_'}, {'name': 'eee_active', 'type': 'bool_'}, {'name': 'eee_cfg', 'type': 'eee_config'}, {'name': 'host_interfaces', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'leds', 'type': 'list_head'}, {'name': 'irq', 'type': 'ffi::c_int'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'ehdr', 'type': '*mut ffi::c_void'}, {'name': 'nest', 'type': '*mut nlattr'}, {'name': 'state_queue', 'type': 'delayed_work'}, {'name': 'lock', 'type': 'mutex'}, {'name': 'sfp_bus_attached', 'type': 'bool_'}, {'name': 'sfp_bus', 'type': '*mut sfp_bus'}, {'name': 'phylink', 'type': '*mut phylink'}, {'name': 'attached_dev', 'type': '*mut net_device'}, {'name': 'mii_ts', 'type': '*mut mii_timestamper'}, {'name': 'psec', 'type': '*mut pse_control'}, {'name': 'mdix', 'type': 'u8_'}, {'name': 'mdix_ctrl', 'type': 'u8_'}, {'name': 'pma_extable', 'type': 'ffi::c_int'}, {'name': 'link_down_events', 'type': 'ffi::c_uint'}, {'name': 'adjust_link', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut net_device)>'}]`
- New: `[{'name': 'mdio', 'type': 'mdio_device'}, {'name': 'drv', 'type': '*const phy_driver'}, {'name': 'devlink', 'type': '*mut device_link'}, {'name': 'phyindex', 'type': 'u32_'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'c45_ids', 'type': 'phy_c45_device_ids'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'rate_matching', 'type': 'ffi::c_int'}, {'name': 'state', 'type': 'phy_state'}, {'name': 'dev_flags', 'type': 'u32_'}, {'name': 'interface', 'type': 'phy_interface_t'}, {'name': 'possible_interfaces', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'speed', 'type': 'ffi::c_int'}, {'name': 'duplex', 'type': 'ffi::c_int'}, {'name': 'port', 'type': 'ffi::c_int'}, {'name': 'master_slave_get', 'type': 'u8_'}, {'name': 'master_slave_set', 'type': 'u8_'}, {'name': 'master_slave_state', 'type': 'u8_'}, {'name': 'supported', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'advertising', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'lp_advertising', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'adv_old', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'supported_eee', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'advertising_eee', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'eee_disabled_modes', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'enable_tx_lpi', 'type': 'bool_'}, {'name': 'eee_active', 'type': 'bool_'}, {'name': 'eee_cfg', 'type': 'eee_config'}, {'name': 'host_interfaces', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'leds', 'type': 'list_head'}, {'name': 'irq', 'type': 'ffi::c_int'}, {'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'ehdr', 'type': '*mut ffi::c_void'}, {'name': 'nest', 'type': '*mut nlattr'}, {'name': 'state_queue', 'type': 'delayed_work'}, {'name': 'lock', 'type': 'mutex'}, {'name': 'sfp_bus_attached', 'type': 'bool_'}, {'name': 'sfp_bus', 'type': '*mut sfp_bus'}, {'name': 'phylink', 'type': '*mut phylink'}, {'name': 'attached_dev', 'type': '*mut net_device'}, {'name': 'mii_ts', 'type': '*mut mii_timestamper'}, {'name': 'psec', 'type': '*mut pse_control'}, {'name': 'mdix', 'type': 'u8_'}, {'name': 'mdix_ctrl', 'type': 'u8_'}, {'name': 'pma_extable', 'type': 'ffi::c_int'}, {'name': 'link_down_events', 'type': 'ffi::c_uint'}, {'name': 'adjust_link', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut net_device)>'}, {'name': 'oatc14_sqi_capability', 'type': 'phy_oatc14_sqi_capability'}]`

### Rust Evidence

- Graph edges: `50`

## W-000853 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: phy_driver
- Explanation: phy_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mdiodrv', 'type': 'mdio_driver_common'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'name', 'type': '*mut ffi::c_char'}, {'name': 'phy_id_mask', 'type': 'u32_'}, {'name': 'features', 'type': '*const ffi::c_ulong'}, {'name': 'flags', 'type': 'u32_'}, {'name': 'driver_data', 'type': '*const ffi::c_void'}, {'name': 'probe', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device) -> ffi::c_int>'}, {'name': 'inband_caps', 'type': '::core::option::Option<'}, {'name': 'config_inband', 'type': '::core::option::Option<'}, {'name': 'get_rate_matching', 'type': '::core::option::Option<'}, {'name': 'resume', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device) -> ffi::c_int>'}, {'name': 'remove', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device)>'}, {'name': 'match_phy_device', 'type': '::core::option::Option<'}, {'name': 'set_wol', 'type': '::core::option::Option<'}, {'name': 'get_wol', 'type': '::core::option::Option<'}, {'name': 'link_change_notify', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device)>'}, {'name': 'read_mmd', 'type': '::core::option::Option<'}, {'name': 'write_mmd', 'type': '::core::option::Option<'}, {'name': 'read_page', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device) -> ffi::c_int>'}, {'name': 'write_page', 'type': '::core::option::Option<'}, {'name': 'module_info', 'type': '::core::option::Option<'}, {'name': 'module_eeprom', 'type': '::core::option::Option<'}, {'name': 'cable_test_tdr_start', 'type': '::core::option::Option<'}, {'name': 'cable_test_get_status', 'type': '::core::option::Option<'}, {'name': 'get_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_link_stats', 'type': '::core::option::Option<'}, {'name': 'get_stats', 'type': '::core::option::Option<'}, {'name': 'get_tunable', 'type': '::core::option::Option<'}, {'name': 'set_tunable', 'type': '::core::option::Option<'}, {'name': 'set_loopback', 'type': '::core::option::Option<'}, {'name': 'get_sqi', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device) -> ffi::c_int>'}, {'name': 'get_plca_cfg', 'type': '::core::option::Option<'}, {'name': 'set_plca_cfg', 'type': '::core::option::Option<'}, {'name': 'get_plca_status', 'type': '::core::option::Option<'}, {'name': 'led_brightness_set', 'type': '::core::option::Option<'}, {'name': 'led_blink_set', 'type': '::core::option::Option<'}, {'name': 'led_hw_is_supported', 'type': '::core::option::Option<'}, {'name': 'led_hw_control_set', 'type': '::core::option::Option<'}, {'name': 'led_hw_control_get', 'type': '::core::option::Option<'}, {'name': 'led_polarity_set', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'mdiodrv', 'type': 'mdio_driver_common'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'name', 'type': '*mut ffi::c_char'}, {'name': 'phy_id_mask', 'type': 'u32_'}, {'name': 'features', 'type': '*const ffi::c_ulong'}, {'name': 'flags', 'type': 'u32_'}, {'name': 'driver_data', 'type': '*const ffi::c_void'}, {'name': 'probe', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device) -> ffi::c_int>'}, {'name': 'inband_caps', 'type': '::core::option::Option<'}, {'name': 'config_inband', 'type': '::core::option::Option<'}, {'name': 'get_rate_matching', 'type': '::core::option::Option<'}, {'name': 'resume', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device) -> ffi::c_int>'}, {'name': 'remove', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device)>'}, {'name': 'match_phy_device', 'type': '::core::option::Option<'}, {'name': 'set_wol', 'type': '::core::option::Option<'}, {'name': 'get_wol', 'type': '::core::option::Option<'}, {'name': 'link_change_notify', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device)>'}, {'name': 'read_mmd', 'type': '::core::option::Option<'}, {'name': 'write_mmd', 'type': '::core::option::Option<'}, {'name': 'read_page', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device) -> ffi::c_int>'}, {'name': 'write_page', 'type': '::core::option::Option<'}, {'name': 'module_info', 'type': '::core::option::Option<'}, {'name': 'module_eeprom', 'type': '::core::option::Option<'}, {'name': 'cable_test_tdr_start', 'type': '::core::option::Option<'}, {'name': 'cable_test_get_status', 'type': '::core::option::Option<'}, {'name': 'get_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_link_stats', 'type': '::core::option::Option<'}, {'name': 'get_stats', 'type': '::core::option::Option<'}, {'name': 'get_tunable', 'type': '::core::option::Option<'}, {'name': 'set_tunable', 'type': '::core::option::Option<'}, {'name': 'set_loopback', 'type': '::core::option::Option<'}, {'name': 'get_sqi', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device) -> ffi::c_int>'}, {'name': 'get_mse_capability', 'type': '::core::option::Option<'}, {'name': 'get_mse_snapshot', 'type': '::core::option::Option<'}, {'name': 'get_plca_cfg', 'type': '::core::option::Option<'}, {'name': 'set_plca_cfg', 'type': '::core::option::Option<'}, {'name': 'get_plca_status', 'type': '::core::option::Option<'}, {'name': 'led_brightness_set', 'type': '::core::option::Option<'}, {'name': 'led_blink_set', 'type': '::core::option::Option<'}, {'name': 'led_hw_is_supported', 'type': '::core::option::Option<'}, {'name': 'led_hw_control_set', 'type': '::core::option::Option<'}, {'name': 'led_hw_control_get', 'type': '::core::option::Option<'}, {'name': 'led_polarity_set', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `27`

## W-000857 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: request
- Explanation: request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'q', 'type': '*mut request_queue'}, {'name': 'mq_ctx', 'type': '*mut blk_mq_ctx'}, {'name': 'mq_hctx', 'type': '*mut blk_mq_hw_ctx'}, {'name': 'cmd_flags', 'type': 'blk_opf_t'}, {'name': 'rq_flags', 'type': 'req_flags_t'}, {'name': 'tag', 'type': 'ffi::c_int'}, {'name': 'internal_tag', 'type': 'ffi::c_int'}, {'name': 'timeout', 'type': 'ffi::c_uint'}, {'name': '__data_len', 'type': 'ffi::c_uint'}, {'name': '__sector', 'type': 'sector_t'}, {'name': 'bio', 'type': '*mut bio'}, {'name': 'biotail', 'type': '*mut bio'}, {'name': '__bindgen_anon_1', 'type': 'request__bindgen_ty_1'}, {'name': 'part', 'type': '*mut block_device'}, {'name': 'alloc_time_ns', 'type': 'u64_'}, {'name': 'start_time_ns', 'type': 'u64_'}, {'name': 'io_start_time_ns', 'type': 'u64_'}, {'name': 'stats_sectors', 'type': 'ffi::c_ushort'}, {'name': 'nr_phys_segments', 'type': 'ffi::c_ushort'}, {'name': 'nr_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'state', 'type': 'mq_rq_state'}, {'name': 'ref_', 'type': 'atomic_t'}, {'name': 'deadline', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_2', 'type': 'request__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'request__bindgen_ty_3'}, {'name': 'elv', 'type': 'request__bindgen_ty_4'}, {'name': 'flush', 'type': 'request__bindgen_ty_5'}, {'name': 'fifo_time', 'type': 'u64_'}, {'name': 'end_io', 'type': 'rq_end_io_fn'}, {'name': 'end_io_data', 'type': '*mut ffi::c_void'}]`
- New: `[{'name': 'q', 'type': '*mut request_queue'}, {'name': 'mq_ctx', 'type': '*mut blk_mq_ctx'}, {'name': 'mq_hctx', 'type': '*mut blk_mq_hw_ctx'}, {'name': 'cmd_flags', 'type': 'blk_opf_t'}, {'name': 'rq_flags', 'type': 'req_flags_t'}, {'name': 'tag', 'type': 'ffi::c_int'}, {'name': 'internal_tag', 'type': 'ffi::c_int'}, {'name': 'timeout', 'type': 'ffi::c_uint'}, {'name': '__data_len', 'type': 'ffi::c_uint'}, {'name': '__sector', 'type': 'sector_t'}, {'name': 'bio', 'type': '*mut bio'}, {'name': 'biotail', 'type': '*mut bio'}, {'name': '__bindgen_anon_1', 'type': 'request__bindgen_ty_1'}, {'name': 'part', 'type': '*mut block_device'}, {'name': 'alloc_time_ns', 'type': 'u64_'}, {'name': 'start_time_ns', 'type': 'u64_'}, {'name': 'io_start_time_ns', 'type': 'u64_'}, {'name': 'stats_sectors', 'type': 'ffi::c_ushort'}, {'name': 'nr_phys_segments', 'type': 'ffi::c_ushort'}, {'name': 'nr_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'phys_gap_bit', 'type': 'ffi::c_uchar'}, {'name': 'state', 'type': 'mq_rq_state'}, {'name': 'ref_', 'type': 'atomic_t'}, {'name': 'deadline', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_2', 'type': 'request__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'request__bindgen_ty_3'}, {'name': 'elv', 'type': 'request__bindgen_ty_4'}, {'name': 'flush', 'type': 'request__bindgen_ty_5'}, {'name': 'fifo_time', 'type': 'u64_'}, {'name': 'end_io', 'type': 'rq_end_io_fn'}, {'name': 'end_io_data', 'type': '*mut ffi::c_void'}]`

### Rust Evidence

- Graph edges: `50`

## W-000308 SignatureDrift

- Risk: High
- Score: 12.4
- Symbol: i2c_new_client_device
- Explanation: i2c_new_client_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `9`

## W-000874 FieldDrift

- Risk: High
- Score: 12.2
- Symbol: urb
- Explanation: urb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'kref', 'type': 'kref'}, {'name': 'unlinked', 'type': 'ffi::c_int'}, {'name': 'hcpriv', 'type': '*mut ffi::c_void'}, {'name': 'use_count', 'type': 'atomic_t'}, {'name': 'reject', 'type': 'atomic_t'}, {'name': 'urb_list', 'type': 'list_head'}, {'name': 'anchor_list', 'type': 'list_head'}, {'name': 'anchor', 'type': '*mut usb_anchor'}, {'name': 'dev', 'type': '*mut usb_device'}, {'name': 'ep', 'type': '*mut usb_host_endpoint'}, {'name': 'pipe', 'type': 'ffi::c_uint'}, {'name': 'stream_id', 'type': 'ffi::c_uint'}, {'name': 'status', 'type': 'ffi::c_int'}, {'name': 'transfer_flags', 'type': 'ffi::c_uint'}, {'name': 'transfer_buffer', 'type': '*mut ffi::c_void'}, {'name': 'transfer_dma', 'type': 'dma_addr_t'}, {'name': 'sg', 'type': '*mut scatterlist'}, {'name': 'sgt', 'type': '*mut sg_table'}, {'name': 'num_mapped_sgs', 'type': 'ffi::c_int'}, {'name': 'num_sgs', 'type': 'ffi::c_int'}, {'name': 'transfer_buffer_length', 'type': 'u32_'}, {'name': 'actual_length', 'type': 'u32_'}, {'name': 'setup_packet', 'type': '*mut ffi::c_uchar'}, {'name': 'setup_dma', 'type': 'dma_addr_t'}, {'name': 'start_frame', 'type': 'ffi::c_int'}, {'name': 'number_of_packets', 'type': 'ffi::c_int'}, {'name': 'interval', 'type': 'ffi::c_int'}, {'name': 'error_count', 'type': 'ffi::c_int'}, {'name': 'context', 'type': '*mut ffi::c_void'}, {'name': 'complete', 'type': 'usb_complete_t'}, {'name': 'iso_frame_desc', 'type': '__IncompleteArrayField<usb_iso_packet_descriptor>'}]`

### Rust Evidence

- Graph edges: `18`

## W-000719 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: usb_deregister
- Explanation: usb_deregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-001194 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: hmac_sha224
- Explanation: hmac_sha224 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct hmac_sha224_key *key', 'const u8 *data', 'size_t data_len', 'u8 out[SHA224_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['const struct hmac_sha224_key *key', 'const u8 *data', 'size_t data_len', 'u8 out[at_least SHA224_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `7`

## W-001197 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: hmac_sha256
- Explanation: hmac_sha256 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct hmac_sha256_key *key', 'const u8 *data', 'size_t data_len', 'u8 out[SHA256_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['const struct hmac_sha256_key *key', 'const u8 *data', 'size_t data_len', 'u8 out[at_least SHA256_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `7`

## W-001200 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: hmac_sha384
- Explanation: hmac_sha384 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct hmac_sha384_key *key', 'const u8 *data', 'size_t data_len', 'u8 out[SHA384_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['const struct hmac_sha384_key *key', 'const u8 *data', 'size_t data_len', 'u8 out[at_least SHA384_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `7`

## W-001203 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: hmac_sha512
- Explanation: hmac_sha512 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct hmac_sha512_key *key', 'const u8 *data', 'size_t data_len', 'u8 out[SHA512_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['const struct hmac_sha512_key *key', 'const u8 *data', 'size_t data_len', 'u8 out[at_least SHA512_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `7`

## W-000294 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: i2c_del_driver
- Explanation: i2c_del_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000318 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: i2c_slave_event
- Explanation: i2c_slave_event changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000336 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: i2c_unregister_device
- Explanation: i2c_unregister_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000338 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: i2c_verify_client
- Explanation: i2c_verify_client changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000769 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: usb_put_intf
- Explanation: usb_put_intf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000801 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: valid
- Explanation: valid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u8_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(0usize, 1u8) as u8) } } #[inline] pub fn set_valid(&mut self, val: u8_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u32_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(2usize, 1u8) as u32) } } #[inline] pub fn set_valid(&mut self, val: u32_) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `6`

## W-000821 FieldDrift

- Risk: High
- Score: 11.8
- Symbol: auxiliary_device_id
- Explanation: auxiliary_device_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'name', 'type': '[ffi::c_char; 32usize]'}, {'name': 'driver_data', 'type': 'kernel_ulong_t'}]`
- New: `[{'name': 'name', 'type': '[ffi::c_char; 40usize]'}, {'name': 'driver_data', 'type': 'kernel_ulong_t'}]`

### Rust Evidence

- Graph edges: `16`

## W-001252 ErrorDrift

- Risk: High
- Score: 11.7
- Symbol: pwmchip_alloc
- Explanation: pwmchip_alloc has ERROR_CODE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE', 'ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/include/linux/pwm.h:567 `return ERR_PTR(-EINVAL);`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/rust/kernel/pwm.rs:583 `bound_parent_device` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/rust/kernel/pwm.rs:595 `bound_parent_device` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/rust/kernel/pwm.rs:578 `// SAFETY: Per the function's safety contract, the parent device is bound.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/rust/kernel/pwm.rs:583 `/// Allocates and wraps a PWM chip using `bindings::pwmchip_alloc`.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/rust/kernel/pwm.rs:584 `///`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/rust/kernel/pwm.rs:585 `AREF`

## W-001254 ErrorDrift

- Risk: High
- Score: 11.7
- Symbol: pwmchip_remove
- Explanation: pwmchip_remove has ERROR_CODE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/include/linux/pwm.h:584 `return -EINVAL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/rust/kernel/pwm.rs:706 `drop` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/rust/kernel/pwm.rs:709 `drop` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/rust/kernel/pwm.rs:705 `// SAFETY: `chip_raw` points to a chip that was successfully registered.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/rust/kernel/pwm.rs:714 `/// Declares a kernel module that exposes a single PWM driver.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/rust/kernel/pwm.rs:706 `LIFETIME_NAMING_PATTERN`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.19/rust/kernel/pwm.rs:709 `LIFETIME_NAMING_PATTERN`

## W-000306 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: i2c_match_id
- Explanation: i2c_match_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000345 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: interface_to_usbdev
- Explanation: interface_to_usbdev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000768 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: usb_put_dev
- Explanation: usb_put_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000789 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: usb_string
- Explanation: usb_string changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000872 FieldDrift

- Risk: High
- Score: 11.6
- Symbol: task_struct
- Explanation: task_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'ffi::c_uint'}, {'name': 'saved_state', 'type': 'ffi::c_uint'}, {'name': 'stack', 'type': '*mut ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'ptrace', 'type': 'ffi::c_uint'}, {'name': 'on_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_cpu', 'type': 'ffi::c_int'}, {'name': 'on_rq', 'type': 'ffi::c_int'}, {'name': 'prio', 'type': 'ffi::c_int'}, {'name': 'static_prio', 'type': 'ffi::c_int'}, {'name': 'normal_prio', 'type': 'ffi::c_int'}, {'name': 'rt_priority', 'type': 'ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'dl_server', 'type': '*mut sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': '__bindgen_padding_1', 'type': 'u64'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'ffi::c_uint'}, {'name': 'policy', 'type': 'ffi::c_uint'}, {'name': 'max_allowed_capacity', 'type': 'ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut ffi::c_void'}, {'name': 'migration_disabled', 'type': 'ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'rcu_tasks_exit_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_exit_list', 'type': 'list_head'}, {'name': 'trc_reader_nesting', 'type': 'ffi::c_int'}, {'name': 'trc_ipi_to_cpu', 'type': 'ffi::c_int'}, {'name': 'trc_reader_special', 'type': 'rcu_special'}, {'name': 'trc_holdout_list', 'type': 'list_head'}, {'name': 'trc_blkd_node', 'type': 'list_head'}, {'name': 'trc_blkd_cpu', 'type': 'ffi::c_int'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'faults_disabled_mapping', 'type': '*mut address_space'}, {'name': 'exit_state', 'type': 'ffi::c_int'}, {'name': 'exit_code', 'type': 'ffi::c_int'}, {'name': 'exit_signal', 'type': 'ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'ffi::c_int'}, {'name': 'jobctl', 'type': 'ffi::c_ulong'}, {'name': 'personality', 'type': 'ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'worker_private', 'type': '*mut ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'blocked_on', 'type': '*mut mutex'}, {'name': 'journal_info', 'type': '*mut ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'ffi::c_uint'}, {'name': 'perf_recursion', 'type': '[u8_; 4usize]'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'perf_ctx_data', 'type': '*mut perf_ctx_data'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'ffi::c_short'}, {'name': 'il_weight', 'type': 'u8_'}, {'name': 'pref_node_fork', 'type': 'ffi::c_short'}, {'name': 'rseq', 'type': '*mut rseq'}, {'name': 'rseq_len', 'type': 'u32_'}, {'name': 'rseq_sig', 'type': 'u32_'}, {'name': 'rseq_event_mask', 'type': 'ffi::c_ulong'}, {'name': 'mm_cid', 'type': 'ffi::c_int'}, {'name': 'last_mm_cid', 'type': 'ffi::c_int'}, {'name': 'migrate_from_cpu', 'type': 'ffi::c_int'}, {'name': 'mm_cid_active', 'type': 'ffi::c_int'}, {'name': 'cid_work', 'type': 'callback_head'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'bpf_net_context', 'type': '*mut bpf_net_context'}, {'name': 'mce_vaddr', 'type': '*mut ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': 'thread', 'type': 'thread_struct'}]`
- New: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'ffi::c_uint'}, {'name': 'saved_state', 'type': 'ffi::c_uint'}, {'name': 'stack', 'type': '*mut ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'ptrace', 'type': 'ffi::c_uint'}, {'name': 'on_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_cpu', 'type': 'ffi::c_int'}, {'name': 'on_rq', 'type': 'ffi::c_int'}, {'name': 'prio', 'type': 'ffi::c_int'}, {'name': 'static_prio', 'type': 'ffi::c_int'}, {'name': 'normal_prio', 'type': 'ffi::c_int'}, {'name': 'rt_priority', 'type': 'ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'dl_server', 'type': '*mut sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': '__bindgen_padding_1', 'type': 'u64'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'ffi::c_uint'}, {'name': 'policy', 'type': 'ffi::c_uint'}, {'name': 'max_allowed_capacity', 'type': 'ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut ffi::c_void'}, {'name': 'migration_disabled', 'type': 'ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'rcu_tasks_exit_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_exit_list', 'type': 'list_head'}, {'name': 'trc_reader_nesting', 'type': 'ffi::c_int'}, {'name': 'trc_ipi_to_cpu', 'type': 'ffi::c_int'}, {'name': 'trc_reader_special', 'type': 'rcu_special'}, {'name': 'trc_holdout_list', 'type': 'list_head'}, {'name': 'trc_blkd_node', 'type': 'list_head'}, {'name': 'trc_blkd_cpu', 'type': 'ffi::c_int'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'faults_disabled_mapping', 'type': '*mut address_space'}, {'name': 'exit_state', 'type': 'ffi::c_int'}, {'name': 'exit_code', 'type': 'ffi::c_int'}, {'name': 'exit_signal', 'type': 'ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'ffi::c_int'}, {'name': 'jobctl', 'type': 'ffi::c_ulong'}, {'name': 'personality', 'type': 'ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'worker_private', 'type': '*mut ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'blocked_on', 'type': '*mut mutex'}, {'name': 'journal_info', 'type': '*mut ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'ffi::c_uint'}, {'name': 'perf_recursion', 'type': '[u8_; 4usize]'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'perf_ctx_data', 'type': '*mut perf_ctx_data'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'ffi::c_short'}, {'name': 'il_weight', 'type': 'u8_'}, {'name': 'pref_node_fork', 'type': 'ffi::c_short'}, {'name': 'rseq', 'type': 'rseq_data'}, {'name': 'mm_cid', 'type': 'sched_mm_cid'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'bpf_net_context', 'type': '*mut bpf_net_context'}, {'name': 'mce_vaddr', 'type': '*mut ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': 'unwind_info', 'type': 'unwind_task_info'}, {'name': 'thread', 'type': 'thread_struct'}]`

### Rust Evidence

- Graph edges: `15`

## W-000313 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: i2c_put_adapter
- Explanation: i2c_put_adapter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000317 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: i2c_register_driver
- Explanation: i2c_register_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000396 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: irq_domain_free_irqs
- Explanation: irq_domain_free_irqs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000504 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: mempool_free
- Explanation: mempool_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'element', 'type': '*mut ffi::c_void'}, {'name': 'pool', 'type': '*mut mempool_t'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'element', 'type': '*mut ffi::c_void'}, {'name': 'pool', 'type': '*mut mempool'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `4`

## W-000641 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: reserved
- Explanation: reserved changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u8_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(1usize, 7u8) as u8) } } #[inline] pub fn set_reserved(&mut self, val: u8_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u32_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(0usize, 8u8) as u32) } } #[inline] pub fn set_reserved(&mut self, val: u32_) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `4`

## W-000676 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: udelay
- Explanation: udelay changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000746 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: usb_get_dev
- Explanation: usb_get_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000748 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: usb_get_intf
- Explanation: usb_get_intf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000773 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: usb_register_driver
- Explanation: usb_register_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000108 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: cgroup_free
- Explanation: cgroup_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `3`

## W-000235 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: gpio_device_get
- Explanation: gpio_device_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000286 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: i2c_acpi_new_device_by_fwnode
- Explanation: i2c_acpi_new_device_by_fwnode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000434 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: irq_matrix_alloc
- Explanation: irq_matrix_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000446 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: irq_matrix_reserve
- Explanation: irq_matrix_reserve changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000458 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: irq_set_chip
- Explanation: irq_set_chip changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000673 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: truncate_inode_pages
- Explanation: truncate_inode_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut address_space'}, {'name': 'arg2', 'type': 'loff_t'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'mapping', 'type': '*mut address_space'}, {'name': 'lstart', 'type': 'loff_t'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `3`

## W-000701 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: usb_autopm_get_interface
- Explanation: usb_autopm_get_interface changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000704 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: usb_autopm_put_interface
- Explanation: usb_autopm_put_interface changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000714 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: usb_control_msg
- Explanation: usb_control_msg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000829 FieldDrift

- Risk: High
- Score: 11.2
- Symbol: config_item_type
- Explanation: config_item_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'ct_owner', 'type': '*mut module'}, {'name': 'ct_item_ops', 'type': '*mut configfs_item_operations'}, {'name': 'ct_group_ops', 'type': '*mut configfs_group_operations'}, {'name': 'ct_attrs', 'type': '*mut *mut configfs_attribute'}, {'name': 'ct_bin_attrs', 'type': '*mut *mut configfs_bin_attribute'}]`
- New: `[{'name': 'ct_owner', 'type': '*mut module'}, {'name': 'ct_item_ops', 'type': '*const configfs_item_operations'}, {'name': 'ct_group_ops', 'type': '*const configfs_group_operations'}, {'name': 'ct_attrs', 'type': '*mut *mut configfs_attribute'}, {'name': 'ct_bin_attrs', 'type': '*mut *mut configfs_bin_attribute'}]`

### Rust Evidence

- Graph edges: `13`

## W-001236 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: truncate_inode_pages
- Explanation: truncate_inode_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct address_space *', 'loff_t'], 'return_type': 'extern void'}`
- New: `{'params': ['struct address_space *mapping', 'loff_t lstart'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `3`

## W-000004 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __bpf_dynptr_data
- Explanation: __bpf_dynptr_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'ptr', 'type': '*const bpf_dynptr_kern'}, {'name': 'len', 'type': 'u32_'}], 'return_type': '*const ffi::c_void'}`
- New: `{'params': [{'name': 'ptr', 'type': '*const bpf_dynptr_kern'}, {'name': 'len', 'type': 'u64_'}], 'return_type': '*const ffi::c_void'}`

### Rust Evidence

- Graph edges: `2`

## W-000077 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: bpf_insn_array_adjust
- Explanation: bpf_insn_array_adjust changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000147 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: device_links_read_lock
- Explanation: device_links_read_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000164 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: devm_pinctrl_register
- Explanation: devm_pinctrl_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000223 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: generic_handle_domain_irq
- Explanation: generic_handle_domain_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000226 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: generic_handle_irq
- Explanation: generic_handle_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000231 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: genphy_c45_oatc14_get_sqi
- Explanation: genphy_c45_oatc14_get_sqi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000283 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: i2c_acpi_find_adapter_by_handle
- Explanation: i2c_acpi_find_adapter_by_handle changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000295 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: i2c_find_adapter_by_fwnode
- Explanation: i2c_find_adapter_by_fwnode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000296 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: i2c_find_device_by_fwnode
- Explanation: i2c_find_device_by_fwnode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000301 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: i2c_get_adapter_by_fwnode
- Explanation: i2c_get_adapter_by_fwnode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000323 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: i2c_smbus_read_byte
- Explanation: i2c_smbus_read_byte changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000325 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: i2c_smbus_read_i2c_block_data
- Explanation: i2c_smbus_read_i2c_block_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000329 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: i2c_smbus_write_byte
- Explanation: i2c_smbus_write_byte changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000334 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: i2c_transfer
- Explanation: i2c_transfer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000341 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: init_srcu_struct_fast
- Explanation: init_srcu_struct_fast changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000358 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: irq_cfg
- Explanation: irq_cfg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000389 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: irq_domain_associate
- Explanation: irq_domain_associate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000437 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: irq_matrix_assign
- Explanation: irq_matrix_assign changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000464 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: irq_set_msi_desc
- Explanation: irq_set_msi_desc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000500 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: mempool_create
- Explanation: mempool_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'min_nr', 'type': 'ffi::c_int'}, {'name': 'alloc_fn', 'type': 'mempool_alloc_t'}, {'name': 'free_fn', 'type': 'mempool_free_t'}, {'name': 'pool_data', 'type': '*mut ffi::c_void'}], 'return_type': '*mut mempool_t'}`
- New: `{'params': [{'name': 'min_nr', 'type': 'ffi::c_int'}, {'name': 'alloc_fn', 'type': 'mempool_alloc_t'}, {'name': 'free_fn', 'type': 'mempool_free_t'}, {'name': 'pool_data', 'type': '*mut ffi::c_void'}], 'return_type': '*mut mempool'}`

### Rust Evidence

- Graph edges: `2`

## W-000511 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: mm_get_unmapped_area
- Explanation: mm_get_unmapped_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'filp', 'type': '*mut file'}, {'name': 'addr', 'type': 'ffi::c_ulong'}, {'name': 'len', 'type': 'ffi::c_ulong'}, {'name': 'pgoff', 'type': 'ffi::c_ulong'}, {'name': 'flags', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_ulong'}`
- New: `{'params': [{'name': 'filp', 'type': '*mut file'}, {'name': 'addr', 'type': 'ffi::c_ulong'}, {'name': 'len', 'type': 'ffi::c_ulong'}, {'name': 'pgoff', 'type': 'ffi::c_ulong'}, {'name': 'flags', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_ulong'}`

### Rust Evidence

- Graph edges: `2`

## W-000550 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pagetable_free_kernel
- Explanation: pagetable_free_kernel changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000554 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_get_device_reverse
- Explanation: pci_get_device_reverse changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000570 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pinconf_generic_dt_node_to_map
- Explanation: pinconf_generic_dt_node_to_map changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000573 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pinctrl_add_gpio_range
- Explanation: pinctrl_add_gpio_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000582 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pinctrl_register
- Explanation: pinctrl_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000619 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: proc_dointvec_ms_jiffies
- Explanation: proc_dointvec_ms_jiffies changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*const ctl_table'}, {'name': 'arg2', 'type': 'ffi::c_int'}, {'name': 'arg3', 'type': '*mut ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'table', 'type': '*const ctl_table'}, {'name': 'dir', 'type': 'ffi::c_int'}, {'name': 'buffer', 'type': '*mut ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `2`

## W-000659 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: simple_offset_rename
- Explanation: simple_offset_rename changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'old_dir', 'type': '*mut inode'}, {'name': 'old_dentry', 'type': '*mut dentry'}, {'name': 'new_dir', 'type': '*mut inode'}, {'name': 'new_dentry', 'type': '*mut dentry'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'old_dir', 'type': '*mut inode'}, {'name': 'old_dentry', 'type': '*mut dentry'}, {'name': 'new_dir', 'type': '*mut inode'}, {'name': 'new_dentry', 'type': '*mut dentry'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `2`

## W-000662 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: software_node_notify
- Explanation: software_node_notify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000720 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: usb_deregister_dev
- Explanation: usb_deregister_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000736 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: usb_find_common_endpoints
- Explanation: usb_find_common_endpoints changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000771 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: usb_register_dev
- Explanation: usb_register_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000802 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vector
- Explanation: vector changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u64_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(32usize, 8u8) as u64) } } #[inline] pub fn set_vector(&mut self, val: u64_) { unsafe { let val: u64 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u32_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(0usize, 8u8) as u32) } } #[inline] pub fn set_vector(&mut self, val: u32_) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `2`

## W-000804 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vfs_create
- Explanation: vfs_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut mnt_idmap'}, {'name': 'arg2', 'type': '*mut inode'}, {'name': 'arg3', 'type': '*mut dentry'}, {'name': 'arg4', 'type': 'umode_t'}, {'name': 'arg5', 'type': 'bool_'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*mut mnt_idmap'}, {'name': 'arg2', 'type': '*mut dentry'}, {'name': 'arg3', 'type': 'umode_t'}, {'name': 'arg4', 'type': '*mut delegated_inode'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `2`

## W-000854 FieldDrift

- Risk: High
- Score: 11.0
- Symbol: queue_limits
- Explanation: queue_limits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'min_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_write_streams', 'type': 'ffi::c_ushort'}, {'name': 'write_stream_granularity', 'type': 'ffi::c_uint'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`
- New: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'max_fast_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_write_streams', 'type': 'ffi::c_ushort'}, {'name': 'write_stream_granularity', 'type': 'ffi::c_uint'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`

### Rust Evidence

- Graph edges: `12`

## W-001228 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: sha256_finup_2x
- Explanation: sha256_finup_2x changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct sha256_ctx *ctx', 'const u8 *data1', 'const u8 *data2', 'size_t len', 'u8 out1[SHA256_DIGEST_SIZE]', 'u8 out2[SHA256_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['const struct sha256_ctx *ctx', 'const u8 *data1', 'const u8 *data2', 'size_t len', 'u8 out1[at_least SHA256_DIGEST_SIZE]', 'u8 out2[at_least SHA256_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `2`

## W-001233 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: simple_offset_rename
- Explanation: simple_offset_rename changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct inode *old_dir', 'struct dentry *old_dentry', 'struct inode *new_dir', 'struct dentry *new_dentry'], 'return_type': 'int'}`
- New: `{'params': ['struct inode *old_dir', 'struct dentry *old_dentry', 'struct inode *new_dir', 'struct dentry *new_dentry'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `2`

## W-001242 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vfs_create
- Explanation: vfs_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mnt_idmap *', 'struct inode *', 'struct dentry *', 'umode_t', 'bool'], 'return_type': 'int'}`
- New: `{'params': ['struct mnt_idmap *', 'struct dentry *', 'umode_t', 'struct delegated_inode *'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `2`

## W-000001 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __SCT__WARN_trap
- Explanation: __SCT__WARN_trap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000002 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __WARN_trap
- Explanation: __WARN_trap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000003 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __bitmap_weighted_or
- Explanation: __bitmap_weighted_or changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000005 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __bpf_dynptr_data_rw
- Explanation: __bpf_dynptr_data_rw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'ptr', 'type': '*const bpf_dynptr_kern'}, {'name': 'len', 'type': 'u32_'}], 'return_type': '*mut ffi::c_void'}`
- New: `{'params': [{'name': 'ptr', 'type': '*const bpf_dynptr_kern'}, {'name': 'len', 'type': 'u64_'}], 'return_type': '*mut ffi::c_void'}`

### Rust Evidence

- Graph edges: `1`

## W-000006 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __bpf_dynptr_size
- Explanation: __bpf_dynptr_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'ptr', 'type': '*const bpf_dynptr_kern'}], 'return_type': 'u32_'}`
- New: `{'params': [{'name': 'ptr', 'type': '*const bpf_dynptr_kern'}], 'return_type': 'u64_'}`

### Rust Evidence

- Graph edges: `1`

## W-000007 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __bpf_dynptr_write
- Explanation: __bpf_dynptr_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'dst', 'type': '*const bpf_dynptr_kern'}, {'name': 'offset', 'type': 'u32_'}, {'name': 'src', 'type': '*mut ffi::c_void'}, {'name': 'len', 'type': 'u32_'}, {'name': 'flags', 'type': 'u64_'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'dst', 'type': '*const bpf_dynptr_kern'}, {'name': 'offset', 'type': 'u64_'}, {'name': 'src', 'type': '*mut ffi::c_void'}, {'name': 'len', 'type': 'u64_'}, {'name': 'flags', 'type': 'u64_'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000008 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __compat_vma_mmap
- Explanation: __compat_vma_mmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000010 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __devm_irq_alloc_descs
- Explanation: __devm_irq_alloc_descs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000022 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __filemap_get_folio
- Explanation: __filemap_get_folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000023 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __filemap_get_folio_mpol
- Explanation: __filemap_get_folio_mpol changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000024 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __i2c_smbus_xfer
- Explanation: __i2c_smbus_xfer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000025 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __i2c_transfer
- Explanation: __i2c_transfer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000026 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __ipi_send_mask
- Explanation: __ipi_send_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000027 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __ipi_send_single
- Explanation: __ipi_send_single changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000028 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __irq_alloc_descs
- Explanation: __irq_alloc_descs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000029 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __irq_alloc_domain_generic_chips
- Explanation: __irq_alloc_domain_generic_chips changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000030 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __irq_domain_alloc_fwnode
- Explanation: __irq_domain_alloc_fwnode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000031 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __irq_domain_alloc_irqs
- Explanation: __irq_domain_alloc_irqs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000032 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __irq_move_irq
- Explanation: __irq_move_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000033 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __irq_resolve_mapping
- Explanation: __irq_resolve_mapping changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000034 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __irq_set_handler
- Explanation: __irq_set_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000035 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __irq_set_lockdep_class
- Explanation: __irq_set_lockdep_class changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000036 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __ns_ref_active_get
- Explanation: __ns_ref_active_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000037 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __ns_ref_active_put
- Explanation: __ns_ref_active_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000038 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __pci_p2pdma_update_state
- Explanation: __pci_p2pdma_update_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000039 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __pm_runtime_disable
- Explanation: __pm_runtime_disable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000040 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __pm_runtime_idle
- Explanation: __pm_runtime_idle changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000041 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __pm_runtime_resume
- Explanation: __pm_runtime_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000042 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __pm_runtime_set_status
- Explanation: __pm_runtime_set_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000043 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __pm_runtime_suspend
- Explanation: __pm_runtime_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000044 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __pm_runtime_use_autosuspend
- Explanation: __pm_runtime_use_autosuspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000045 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __request_percpu_irq
- Explanation: __request_percpu_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'handler', 'type': 'irq_handler_t'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'devname', 'type': '*const ffi::c_char'}, {'name': 'percpu_dev_id', 'type': '*mut ffi::c_void'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'handler', 'type': 'irq_handler_t'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'devname', 'type': '*const ffi::c_char'}, {'name': 'affinity', 'type': '*const cpumask_t'}, {'name': 'percpu_dev_id', 'type': '*mut ffi::c_void'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000046 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __scoped_seqlock_bug
- Explanation: __scoped_seqlock_bug changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000047 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __scoped_seqlock_invalid_target
- Explanation: __scoped_seqlock_invalid_target changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000048 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __simple_rmdir
- Explanation: __simple_rmdir changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000049 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __simple_unlink
- Explanation: __simple_unlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000051 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sys_getsockname
- Explanation: __sys_getsockname changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'fd', 'type': 'ffi::c_int'}, {'name': 'usockaddr', 'type': '*mut sockaddr'}, {'name': 'usockaddr_len', 'type': '*mut ffi::c_int'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'fd', 'type': 'ffi::c_int'}, {'name': 'usockaddr', 'type': '*mut sockaddr'}, {'name': 'usockaddr_len', 'type': '*mut ffi::c_int'}, {'name': 'peer', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000052 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __usb_get_extra_descriptor
- Explanation: __usb_get_extra_descriptor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000053 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __vma_start_write
- Explanation: __vma_start_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'mm_lock_seq', 'type': 'ffi::c_uint'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'mm_lock_seq', 'type': 'ffi::c_uint'}, {'name': 'state', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000054 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __warn_args
- Explanation: __warn_args changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000057 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_pci_link_allocate_irq
- Explanation: acpi_pci_link_allocate_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'handle', 'type': 'acpi_handle'}, {'name': 'index', 'type': 'ffi::c_int'}, {'name': 'triggering', 'type': '*mut ffi::c_int'}, {'name': 'polarity', 'type': '*mut ffi::c_int'}, {'name': 'name', 'type': '*mut *mut ffi::c_char'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'handle', 'type': 'acpi_handle'}, {'name': 'index', 'type': 'ffi::c_int'}, {'name': 'triggering', 'type': '*mut ffi::c_int'}, {'name': 'polarity', 'type': '*mut ffi::c_int'}, {'name': 'name', 'type': '*mut *mut ffi::c_char'}, {'name': 'gsi', 'type': '*mut u32_'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000058 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: active_low
- Explanation: active_low changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(0usize, 1u8) as u32) } } #[inline] pub fn set_active_low(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u32_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(14usize, 1u8) as u32) } } #[inline] pub fn set_active_low(&mut self, val: u32_) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000059 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: apic_ack_edge
- Explanation: apic_ack_edge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000060 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_dynirq_lower_bound
- Explanation: arch_dynirq_lower_bound changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000061 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_sched_node_distance
- Explanation: arch_sched_node_distance changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000062 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: asym_pause
- Explanation: asym_pause changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000063 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: authenticated
- Explanation: authenticated changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000064 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: authorized
- Explanation: authorized changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000065 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: auxiliary_bus_init
- Explanation: auxiliary_bus_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000067 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: b_hnp_enable
- Explanation: b_hnp_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000068 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: base_address
- Explanation: base_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000069 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_seg_gap
- Explanation: bio_seg_gap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000070 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blkdev_get_zone_info
- Explanation: blkdev_get_zone_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000071 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blkdev_report_zones_cached
- Explanation: blkdev_report_zones_cached changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000072 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_arch_text_poke
- Explanation: bpf_arch_text_poke changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'ip', 'type': '*mut ffi::c_void'}, {'name': 't', 'type': 'bpf_text_poke_type'}, {'name': 'addr1', 'type': '*mut ffi::c_void'}, {'name': 'addr2', 'type': '*mut ffi::c_void'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'ip', 'type': '*mut ffi::c_void'}, {'name': 'old_t', 'type': 'bpf_text_poke_type'}, {'name': 'new_t', 'type': 'bpf_text_poke_type'}, {'name': 'old_addr', 'type': '*mut ffi::c_void'}, {'name': 'new_addr', 'type': '*mut ffi::c_void'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000073 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_array_get_next_key
- Explanation: bpf_array_get_next_key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000074 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_dynptr_check_size
- Explanation: bpf_dynptr_check_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'size', 'type': 'u32_'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'size', 'type': 'u64_'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000075 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_dynptr_from_file_sleepable
- Explanation: bpf_dynptr_from_file_sleepable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000076 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_dynptr_slice_rdwr
- Explanation: bpf_dynptr_slice_rdwr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'p', 'type': '*const bpf_dynptr'}, {'name': 'offset', 'type': 'u32_'}, {'name': 'buffer__opt', 'type': '*mut ffi::c_void'}, {'name': 'buffer__szk', 'type': 'u32_'}], 'return_type': '*mut ffi::c_void'}`
- New: `{'params': [{'name': 'p', 'type': '*const bpf_dynptr'}, {'name': 'offset', 'type': 'u64_'}, {'name': 'buffer__opt', 'type': '*mut ffi::c_void'}, {'name': 'buffer__szk', 'type': 'u64_'}], 'return_type': '*mut ffi::c_void'}`

### Rust Evidence

- Graph edges: `1`

## W-000078 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_insn_array_adjust_after_remove
- Explanation: bpf_insn_array_adjust_after_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000079 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_insn_array_init
- Explanation: bpf_insn_array_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000080 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_insn_array_ready
- Explanation: bpf_insn_array_ready changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000081 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_insn_array_release
- Explanation: bpf_insn_array_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000082 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_map_free_internal_structs
- Explanation: bpf_map_free_internal_structs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000083 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: broken_intx_masking
- Explanation: broken_intx_masking changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(31usize, 1u8) as u32) } } #[inline] pub fn set_broken_intx_masking(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(32usize, 1u8) as u32) } } #[inline] pub fn set_broken_intx_masking(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000084 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: build_id_parse_file
- Explanation: build_id_parse_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000085 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bus_add_device
- Explanation: bus_add_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000086 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bus_add_driver
- Explanation: bus_add_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000087 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bus_find_device_reverse
- Explanation: bus_find_device_reverse changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000088 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bus_is_registered
- Explanation: bus_is_registered changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000089 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bus_notify
- Explanation: bus_notify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000090 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bus_probe_device
- Explanation: bus_probe_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000091 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bus_remove_device
- Explanation: bus_remove_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000092 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bus_remove_driver
- Explanation: bus_remove_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000093 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bus_to_subsys
- Explanation: bus_to_subsys changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000094 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: buses_init
- Explanation: buses_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000095 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: can_request_irq
- Explanation: can_request_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000096 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: can_submit
- Explanation: can_submit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000097 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cd_forget
- Explanation: cd_forget changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000098 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cdev_add
- Explanation: cdev_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000099 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cdev_alloc
- Explanation: cdev_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000100 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cdev_del
- Explanation: cdev_del changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000101 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cdev_device_add
- Explanation: cdev_device_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000102 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cdev_device_del
- Explanation: cdev_device_del changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000103 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cdev_init
- Explanation: cdev_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000104 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cdev_put
- Explanation: cdev_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000105 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cdev_set_parent
- Explanation: cdev_set_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000106 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup1_freezing
- Explanation: cgroup1_freezing changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000111 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_task_dead
- Explanation: cgroup_task_dead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000112 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_task_exit
- Explanation: cgroup_task_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000113 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_task_free
- Explanation: cgroup_task_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000114 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_task_release
- Explanation: cgroup_task_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000115 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_to_subsys
- Explanation: class_to_subsys changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000116 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: classes_init
- Explanation: classes_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000117 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: compat_vma_mmap
- Explanation: compat_vma_mmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000119 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: container_dev_init
- Explanation: container_dev_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000120 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_irq_alloc_info
- Explanation: copy_irq_alloc_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000121 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_dev_init
- Explanation: cpu_dev_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000122 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpus_peek_for_pending_ipi
- Explanation: cpus_peek_for_pending_ipi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000123 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: create_proc_profile
- Explanation: create_proc_profile changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000125 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_dispose_if_unused
- Explanation: d_dispose_if_unused changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000126 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_make_discardable
- Explanation: d_make_discardable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000127 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: d_make_persistent
- Explanation: d_make_persistent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000128 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: deactivate_nsproxy
- Explanation: deactivate_nsproxy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000129 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dead
- Explanation: dead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000130 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: decay_pcp_high
- Explanation: decay_pcp_high changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'zone', 'type': '*mut zone'}, {'name': 'pcp', 'type': '*mut per_cpu_pages'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'zone', 'type': '*mut zone'}, {'name': 'pcp', 'type': '*mut per_cpu_pages'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000131 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: default_timestamp
- Explanation: default_timestamp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(20usize, 1u8) as u32) } } #[inline] pub fn set_default_timestamp(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(22usize, 1u8) as u32) } } #[inline] pub fn set_default_timestamp(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000132 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: deferred_probe_extend_timeout
- Explanation: deferred_probe_extend_timeout changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000133 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: delivery_mode
- Explanation: delivery_mode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000134 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dest_mode_logical
- Explanation: dest_mode_logical changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000135 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: destid_0_7
- Explanation: destid_0_7 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000136 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: destid_8_31
- Explanation: destid_8_31 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000137 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_block_probing
- Explanation: device_block_probing changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000138 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_driver_detach
- Explanation: device_driver_detach changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000139 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_get_devnode
- Explanation: device_get_devnode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000140 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_link_flag_is_sync_state_only
- Explanation: device_link_flag_is_sync_state_only changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000141 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_links_busy
- Explanation: device_links_busy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000142 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_links_check_suppliers
- Explanation: device_links_check_suppliers changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000143 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_links_driver_bound
- Explanation: device_links_driver_bound changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000144 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_links_driver_cleanup
- Explanation: device_links_driver_cleanup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000145 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_links_force_bind
- Explanation: device_links_force_bind changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000146 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_links_no_driver
- Explanation: device_links_no_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000148 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_links_read_lock_held
- Explanation: device_links_read_lock_held changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000149 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_links_read_unlock
- Explanation: device_links_read_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000150 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_links_unbind_consumers
- Explanation: device_links_unbind_consumers changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000151 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_pm_move_to_tail
- Explanation: device_pm_move_to_tail changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000152 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_release_driver_internal
- Explanation: device_release_driver_internal changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000153 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_set_deferred_probe_reason
- Explanation: device_set_deferred_probe_reason changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000154 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_unblock_probing
- Explanation: device_unblock_probing changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000155 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devices_init
- Explanation: devices_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000156 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devices_kset_move_last
- Explanation: devices_kset_move_last changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000158 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_gpiochip_add_data_with_key
- Explanation: devm_gpiochip_add_data_with_key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000159 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_i2c_add_adapter
- Explanation: devm_i2c_add_adapter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000160 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_i2c_new_dummy_device
- Explanation: devm_i2c_new_dummy_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000161 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_irq_alloc_generic_chip
- Explanation: devm_irq_alloc_generic_chip changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000162 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_irq_domain_instantiate
- Explanation: devm_irq_domain_instantiate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000163 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_irq_setup_generic_chip
- Explanation: devm_irq_setup_generic_chip changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000165 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_pinctrl_register_and_init
- Explanation: devm_pinctrl_register_and_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000166 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_pinctrl_unregister
- Explanation: devm_pinctrl_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000167 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_pm_runtime_enable
- Explanation: devm_pm_runtime_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000168 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_pm_runtime_get_noresume
- Explanation: devm_pm_runtime_get_noresume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000169 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_pm_runtime_set_active_enabled
- Explanation: devm_pm_runtime_set_active_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000170 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devres_release_all
- Explanation: devres_release_all changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000171 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devtmpfs_create_node
- Explanation: devtmpfs_create_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000172 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devtmpfs_delete_node
- Explanation: devtmpfs_delete_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000173 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devtmpfs_init
- Explanation: devtmpfs_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000174 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: disable_hub_initiated_lpm
- Explanation: disable_hub_initiated_lpm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000175 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: disk_report_zone
- Explanation: disk_report_zone changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000176 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dl_defer_idle
- Explanation: dl_defer_idle changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000177 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dmar_base_address
- Explanation: dmar_base_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000178 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dmar_format
- Explanation: dmar_format changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000179 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dmar_index_0_14
- Explanation: dmar_index_0_14 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000180 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dmar_index_15
- Explanation: dmar_index_15 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000181 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dmar_reserved_0
- Explanation: dmar_reserved_0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000182 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dmar_subhandle_valid
- Explanation: dmar_subhandle_valid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000183 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_getsockname
- Explanation: do_getsockname changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000185 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_remote_wakeup
- Explanation: do_remote_wakeup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000187 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: driver_add_groups
- Explanation: driver_add_groups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000188 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: driver_deferred_probe_del
- Explanation: driver_deferred_probe_del changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000189 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: driver_deferred_probe_trigger
- Explanation: driver_deferred_probe_trigger changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000190 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: driver_detach
- Explanation: driver_detach changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000191 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: driver_remove_groups
- Explanation: driver_remove_groups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000192 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drivers_autoprobe
- Explanation: drivers_autoprobe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000199 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: elcr_set_level_irq
- Explanation: elcr_set_level_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000200 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: end_dirop
- Explanation: end_dirop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000201 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ep_devs_created
- Explanation: ep_devs_created changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000202 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: exit_cred_namespaces
- Explanation: exit_cred_namespaces changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000203 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: exit_nsproxy_namespaces
- Explanation: exit_nsproxy_namespaces changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000205 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: external_facing
- Explanation: external_facing changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(30usize, 1u8) as u32) } } #[inline] pub fn set_external_facing(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(31usize, 1u8) as u32) } } #[inline] pub fn set_external_facing(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000206 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: faux_bus_init
- Explanation: faux_bus_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000207 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_alloc_folio_noprof
- Explanation: filemap_alloc_folio_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'gfp', 'type': 'gfp_t'}, {'name': 'order', 'type': 'ffi::c_uint'}], 'return_type': '*mut folio'}`
- New: `{'params': [{'name': 'gfp', 'type': 'gfp_t'}, {'name': 'order', 'type': 'ffi::c_uint'}, {'name': 'policy', 'type': '*mut mempolicy'}], 'return_type': '*mut folio'}`

### Rust Evidence

- Graph edges: `1`

## W-000210 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_flush_nr
- Explanation: filemap_flush_nr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000211 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_flush_range
- Explanation: filemap_flush_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000212 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_get_folios_dirty
- Explanation: filemap_get_folios_dirty changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000213 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: firmware_init
- Explanation: firmware_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000214 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fm_enabled
- Explanation: fm_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000215 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_alloc_swap
- Explanation: folio_alloc_swap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'folio', 'type': '*mut folio'}, {'name': 'gfp_mask', 'type': 'gfp_t'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'folio', 'type': '*mut folio'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000216 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: freader_cleanup
- Explanation: freader_cleanup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000217 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: freader_fetch
- Explanation: freader_fetch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000218 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: freader_init_from_file
- Explanation: freader_init_from_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000219 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: freader_init_from_mem
- Explanation: freader_init_from_mem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000221 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fw_devlink_drivers_done
- Explanation: fw_devlink_drivers_done changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000222 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fw_devlink_probing_done
- Explanation: fw_devlink_probing_done changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000224 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_handle_domain_irq_safe
- Explanation: generic_handle_domain_irq_safe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000225 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_handle_domain_nmi
- Explanation: generic_handle_domain_nmi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000227 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_handle_irq_safe
- Explanation: generic_handle_irq_safe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000228 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_subclass
- Explanation: generic_subclass changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000229 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_oatc14_cable_test_get_status
- Explanation: genphy_c45_oatc14_cable_test_get_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000230 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_oatc14_cable_test_start
- Explanation: genphy_c45_oatc14_cable_test_start changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000232 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_oatc14_get_sqi_max
- Explanation: genphy_c45_oatc14_get_sqi_max changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000233 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_cred_namespaces
- Explanation: get_cred_namespaces changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000234 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpio_device_find
- Explanation: gpio_device_find changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000236 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpio_device_get_chip
- Explanation: gpio_device_get_chip changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000237 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpio_device_get_desc
- Explanation: gpio_device_get_desc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000238 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpio_device_put
- Explanation: gpio_device_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000239 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpio_device_to_device
- Explanation: gpio_device_to_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000240 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpiochip_add_data_with_key
- Explanation: gpiochip_add_data_with_key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000241 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpiochip_disable_irq
- Explanation: gpiochip_disable_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000242 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpiochip_dup_line_label
- Explanation: gpiochip_dup_line_label changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000243 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpiochip_enable_irq
- Explanation: gpiochip_enable_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000244 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpiochip_free_own_desc
- Explanation: gpiochip_free_own_desc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000245 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpiochip_generic_config
- Explanation: gpiochip_generic_config changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000246 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpiochip_generic_free
- Explanation: gpiochip_generic_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000247 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpiochip_generic_request
- Explanation: gpiochip_generic_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000248 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpiochip_get_data
- Explanation: gpiochip_get_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000249 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpiochip_irq_relres
- Explanation: gpiochip_irq_relres changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000250 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpiochip_irq_reqres
- Explanation: gpiochip_irq_reqres changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000251 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpiochip_line_is_irq
- Explanation: gpiochip_line_is_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000252 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpiochip_line_is_open_drain
- Explanation: gpiochip_line_is_open_drain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000253 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpiochip_line_is_open_source
- Explanation: gpiochip_line_is_open_source changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000254 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpiochip_line_is_persistent
- Explanation: gpiochip_line_is_persistent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000255 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpiochip_line_is_valid
- Explanation: gpiochip_line_is_valid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000256 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpiochip_populate_parent_fwspec_fourcell
- Explanation: gpiochip_populate_parent_fwspec_fourcell changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000257 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpiochip_populate_parent_fwspec_twocell
- Explanation: gpiochip_populate_parent_fwspec_twocell changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000258 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpiochip_query_valid_mask
- Explanation: gpiochip_query_valid_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000259 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpiochip_relres_irq
- Explanation: gpiochip_relres_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000260 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpiochip_remove
- Explanation: gpiochip_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000261 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpiochip_reqres_irq
- Explanation: gpiochip_reqres_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000262 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpiochip_request_own_desc
- Explanation: gpiochip_request_own_desc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000263 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: handle_bad_irq
- Explanation: handle_bad_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000264 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: handle_edge_eoi_irq
- Explanation: handle_edge_eoi_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000265 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: handle_edge_irq
- Explanation: handle_edge_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000266 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: handle_fasteoi_ack_irq
- Explanation: handle_fasteoi_ack_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000267 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: handle_fasteoi_irq
- Explanation: handle_fasteoi_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000268 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: handle_fasteoi_mask_irq
- Explanation: handle_fasteoi_mask_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000269 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: handle_fasteoi_nmi
- Explanation: handle_fasteoi_nmi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000270 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: handle_irq_desc
- Explanation: handle_irq_desc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000271 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: handle_level_irq
- Explanation: handle_level_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000272 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: handle_nested_irq
- Explanation: handle_nested_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000273 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: handle_percpu_devid_irq
- Explanation: handle_percpu_devid_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000274 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: handle_percpu_irq
- Explanation: handle_percpu_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000275 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: handle_simple_irq
- Explanation: handle_simple_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000276 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: handle_untracked_irq
- Explanation: handle_untracked_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000278 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: has_managed_zone
- Explanation: has_managed_zone changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000279 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: have_langid
- Explanation: have_langid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000280 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hide_from_rmap_until_complete
- Explanation: hide_from_rmap_until_complete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000281 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: huge_pmd_set_accessed
- Explanation: huge_pmd_set_accessed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'vmf', 'type': '*mut vm_fault'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'vmf', 'type': '*mut vm_fault'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000282 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_acpi_client_count
- Explanation: i2c_acpi_client_count changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000284 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_acpi_find_bus_speed
- Explanation: i2c_acpi_find_bus_speed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000285 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_acpi_get_i2c_resource
- Explanation: i2c_acpi_get_i2c_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000287 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_acpi_waive_d0_probe
- Explanation: i2c_acpi_waive_d0_probe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000288 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_adapter_depth
- Explanation: i2c_adapter_depth changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000289 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_add_adapter
- Explanation: i2c_add_adapter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000290 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_add_numbered_adapter
- Explanation: i2c_add_numbered_adapter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000291 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_client_get_device_id
- Explanation: i2c_client_get_device_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000292 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_clients_command
- Explanation: i2c_clients_command changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000293 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_del_adapter
- Explanation: i2c_del_adapter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000297 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_for_each_dev
- Explanation: i2c_for_each_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000298 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_freq_mode_string
- Explanation: i2c_freq_mode_string changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000299 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_generic_scl_recovery
- Explanation: i2c_generic_scl_recovery changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000302 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_get_device_id
- Explanation: i2c_get_device_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000303 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_get_dma_safe_msg_buf
- Explanation: i2c_get_dma_safe_msg_buf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000304 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_get_match_data
- Explanation: i2c_get_match_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000305 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_handle_smbus_host_notify
- Explanation: i2c_handle_smbus_host_notify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000307 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_new_ancillary_device
- Explanation: i2c_new_ancillary_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000309 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_new_dummy_device
- Explanation: i2c_new_dummy_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000310 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_new_scanned_device
- Explanation: i2c_new_scanned_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000311 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_parse_fw_timings
- Explanation: i2c_parse_fw_timings changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000312 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_probe_func_quick_read
- Explanation: i2c_probe_func_quick_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000314 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_put_dma_safe_msg_buf
- Explanation: i2c_put_dma_safe_msg_buf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000315 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_recover_bus
- Explanation: i2c_recover_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000316 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_register_board_info
- Explanation: i2c_register_board_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000319 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_slave_register
- Explanation: i2c_slave_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000320 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_slave_unregister
- Explanation: i2c_slave_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000321 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_smbus_pec
- Explanation: i2c_smbus_pec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000322 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_smbus_read_block_data
- Explanation: i2c_smbus_read_block_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000324 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_smbus_read_byte_data
- Explanation: i2c_smbus_read_byte_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000326 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_smbus_read_i2c_block_data_or_emulated
- Explanation: i2c_smbus_read_i2c_block_data_or_emulated changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000327 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_smbus_read_word_data
- Explanation: i2c_smbus_read_word_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000328 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_smbus_write_block_data
- Explanation: i2c_smbus_write_block_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000330 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_smbus_write_byte_data
- Explanation: i2c_smbus_write_byte_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000331 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_smbus_write_i2c_block_data
- Explanation: i2c_smbus_write_i2c_block_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000332 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_smbus_write_word_data
- Explanation: i2c_smbus_write_word_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000333 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_smbus_xfer
- Explanation: i2c_smbus_xfer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000335 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_transfer_buffer_flags
- Explanation: i2c_transfer_buffer_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000337 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: i2c_verify_adapter
- Explanation: i2c_verify_adapter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000339 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ilookup5_nowait
- Explanation: ilookup5_nowait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'sb', 'type': '*mut super_block'}, {'name': 'hashval', 'type': 'ffi::c_ulong'}, {'name': 'test', 'type': '::core::option::Option< unsafe extern "C" fn(arg1: *mut inode, arg2: *mut ffi::c_void'}], 'return_type': 'ffi::c_int, >, data: *mut ffi::c_void, ) -> *mut inode'}`
- New: `{'params': [{'name': 'sb', 'type': '*mut super_block'}, {'name': 'hashval', 'type': 'ffi::c_ulong'}, {'name': 'test', 'type': '::core::option::Option< unsafe extern "C" fn(arg1: *mut inode, arg2: *mut ffi::c_void'}], 'return_type': 'ffi::c_int, >, data: *mut ffi::c_void, isnew: *mut bool_, ) -> *mut inode'}`

### Rust Evidence

- Graph edges: `1`

## W-000340 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: init_irq_alloc_info
- Explanation: init_irq_alloc_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000342 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: init_srcu_struct_fast_updown
- Explanation: init_srcu_struct_fast_updown changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000344 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_lru_list_add
- Explanation: inode_lru_list_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000346 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: interrupts
- Explanation: interrupts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(17usize, 1u8) as u32) } } #[inline] pub fn set_interrupts(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(19usize, 1u8) as u32) } } #[inline] pub fn set_interrupts(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000347 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: interval_tree_subtree_search
- Explanation: interval_tree_subtree_search changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000348 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: io_window_1k
- Explanation: io_window_1k changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(32usize, 1u8) as u32) } } #[inline] pub fn set_io_window_1k(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(33usize, 1u8) as u32) } } #[inline] pub fn set_io_window_1k(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000349 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ipi_get_hwirq
- Explanation: ipi_get_hwirq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000350 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ipi_mux_create
- Explanation: ipi_mux_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000351 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ipi_mux_process
- Explanation: ipi_mux_process changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000352 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ipi_send_mask
- Explanation: ipi_send_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000353 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ipi_send_single
- Explanation: ipi_send_single changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000354 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_affinity_online_cpu
- Explanation: irq_affinity_online_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000355 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_alloc_generic_chip
- Explanation: irq_alloc_generic_chip changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000356 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_alloc_matrix
- Explanation: irq_alloc_matrix changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000357 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_can_move_in_process_context
- Explanation: irq_can_move_in_process_context changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000359 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_check_status_bit
- Explanation: irq_check_status_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000360 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_ack_parent
- Explanation: irq_chip_ack_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000361 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_compose_msi_msg
- Explanation: irq_chip_compose_msi_msg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000362 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_disable_parent
- Explanation: irq_chip_disable_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000363 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_enable_parent
- Explanation: irq_chip_enable_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000364 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_eoi_parent
- Explanation: irq_chip_eoi_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000365 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_get_parent_state
- Explanation: irq_chip_get_parent_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000366 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_mask_ack_parent
- Explanation: irq_chip_mask_ack_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000367 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_mask_parent
- Explanation: irq_chip_mask_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000368 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_pm_get
- Explanation: irq_chip_pm_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000369 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_pm_put
- Explanation: irq_chip_pm_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000370 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_release_resources_parent
- Explanation: irq_chip_release_resources_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000371 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_request_resources_parent
- Explanation: irq_chip_request_resources_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000372 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_retrigger_hierarchy
- Explanation: irq_chip_retrigger_hierarchy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000373 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_set_affinity_parent
- Explanation: irq_chip_set_affinity_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000374 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_set_parent_state
- Explanation: irq_chip_set_parent_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000375 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_set_type_parent
- Explanation: irq_chip_set_type_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000376 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_set_vcpu_affinity_parent
- Explanation: irq_chip_set_vcpu_affinity_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000377 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_set_wake_parent
- Explanation: irq_chip_set_wake_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000378 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_shutdown_parent
- Explanation: irq_chip_shutdown_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000379 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_startup_parent
- Explanation: irq_chip_startup_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000380 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_chip_unmask_parent
- Explanation: irq_chip_unmask_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000381 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_complete_move
- Explanation: irq_complete_move changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000382 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_create_fwspec_mapping
- Explanation: irq_create_fwspec_mapping changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000383 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_create_mapping_affinity
- Explanation: irq_create_mapping_affinity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000384 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_destroy_ipi
- Explanation: irq_destroy_ipi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000385 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_dispose_mapping
- Explanation: irq_dispose_mapping changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000386 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_activate_irq
- Explanation: irq_domain_activate_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000387 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_alloc_descs
- Explanation: irq_domain_alloc_descs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000388 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_alloc_irqs_parent
- Explanation: irq_domain_alloc_irqs_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000390 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_associate_many
- Explanation: irq_domain_associate_many changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000391 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_create_legacy
- Explanation: irq_domain_create_legacy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000392 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_create_simple
- Explanation: irq_domain_create_simple changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000393 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_deactivate_irq
- Explanation: irq_domain_deactivate_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000394 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_disconnect_hierarchy
- Explanation: irq_domain_disconnect_hierarchy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000395 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_free_fwnode
- Explanation: irq_domain_free_fwnode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000397 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_free_irqs_common
- Explanation: irq_domain_free_irqs_common changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000398 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_free_irqs_parent
- Explanation: irq_domain_free_irqs_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000399 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_free_irqs_top
- Explanation: irq_domain_free_irqs_top changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000400 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_get_irq_data
- Explanation: irq_domain_get_irq_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000401 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_instantiate
- Explanation: irq_domain_instantiate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000402 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_pop_irq
- Explanation: irq_domain_pop_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000403 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_push_irq
- Explanation: irq_domain_push_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000404 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_remove
- Explanation: irq_domain_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000405 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_reset_irq_data
- Explanation: irq_domain_reset_irq_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000406 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_set_hwirq_and_chip
- Explanation: irq_domain_set_hwirq_and_chip changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000407 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_set_info
- Explanation: irq_domain_set_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000408 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_translate_onecell
- Explanation: irq_domain_translate_onecell changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000409 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_translate_twocell
- Explanation: irq_domain_translate_twocell changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000410 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_translate_twothreecell
- Explanation: irq_domain_translate_twothreecell changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000411 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_update_bus_token
- Explanation: irq_domain_update_bus_token changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000412 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_xlate_onecell
- Explanation: irq_domain_xlate_onecell changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000413 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_xlate_onetwocell
- Explanation: irq_domain_xlate_onetwocell changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000414 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_xlate_twocell
- Explanation: irq_domain_xlate_twocell changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000415 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_domain_xlate_twothreecell
- Explanation: irq_domain_xlate_twothreecell changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000416 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_find_matching_fwspec
- Explanation: irq_find_matching_fwspec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000417 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_free_descs
- Explanation: irq_free_descs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000418 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_gc_ack_clr_bit
- Explanation: irq_gc_ack_clr_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000419 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_gc_ack_set_bit
- Explanation: irq_gc_ack_set_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000420 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_gc_eoi
- Explanation: irq_gc_eoi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000421 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_gc_mask_clr_bit
- Explanation: irq_gc_mask_clr_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000422 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_gc_mask_disable_and_ack_set
- Explanation: irq_gc_mask_disable_and_ack_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000423 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_gc_mask_disable_reg
- Explanation: irq_gc_mask_disable_reg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000424 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_gc_mask_set_bit
- Explanation: irq_gc_mask_set_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000425 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_gc_noop
- Explanation: irq_gc_noop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000426 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_gc_set_wake
- Explanation: irq_gc_set_wake changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000427 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_gc_unmask_enable_reg
- Explanation: irq_gc_unmask_enable_reg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000428 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_get_default_domain
- Explanation: irq_get_default_domain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000429 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_get_domain_generic_chip
- Explanation: irq_get_domain_generic_chip changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000430 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_get_irq_data
- Explanation: irq_get_irq_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000431 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_lock_sparse
- Explanation: irq_lock_sparse changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000432 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_managed
- Explanation: irq_managed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(33usize, 1u8) as u32) } } #[inline] pub fn set_irq_managed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(34usize, 1u8) as u32) } } #[inline] pub fn set_irq_managed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000433 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_map_generic_chip
- Explanation: irq_map_generic_chip changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000435 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_matrix_alloc_managed
- Explanation: irq_matrix_alloc_managed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000436 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_matrix_allocated
- Explanation: irq_matrix_allocated changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000438 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_matrix_assign_system
- Explanation: irq_matrix_assign_system changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000439 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_matrix_available
- Explanation: irq_matrix_available changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000440 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_matrix_debug_show
- Explanation: irq_matrix_debug_show changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000441 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_matrix_free
- Explanation: irq_matrix_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000442 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_matrix_offline
- Explanation: irq_matrix_offline changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000443 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_matrix_online
- Explanation: irq_matrix_online changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000444 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_matrix_remove_managed
- Explanation: irq_matrix_remove_managed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000445 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_matrix_remove_reserved
- Explanation: irq_matrix_remove_reserved changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000447 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_matrix_reserve_managed
- Explanation: irq_matrix_reserve_managed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000448 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_matrix_reserved
- Explanation: irq_matrix_reserved changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000449 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_migrate_all_off_this_cpu
- Explanation: irq_migrate_all_off_this_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000450 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_modify_status
- Explanation: irq_modify_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000451 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_move_masked_irq
- Explanation: irq_move_masked_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000452 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_populate_fwspec_info
- Explanation: irq_populate_fwspec_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000453 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_remove_generic_chip
- Explanation: irq_remove_generic_chip changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000454 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_rerun
- Explanation: irq_rerun changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(19usize, 1u8) as u32) } } #[inline] pub fn set_irq_rerun(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(21usize, 1u8) as u32) } } #[inline] pub fn set_irq_rerun(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000455 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_reserve_ipi
- Explanation: irq_reserve_ipi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000456 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_set_affinity_locked
- Explanation: irq_set_affinity_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000457 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_set_chained_handler_and_data
- Explanation: irq_set_chained_handler_and_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000459 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_set_chip_and_handler_name
- Explanation: irq_set_chip_and_handler_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000460 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_set_chip_data
- Explanation: irq_set_chip_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000461 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_set_default_domain
- Explanation: irq_set_default_domain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000462 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_set_handler_data
- Explanation: irq_set_handler_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000463 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_set_irq_type
- Explanation: irq_set_irq_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000465 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_set_msi_desc_off
- Explanation: irq_set_msi_desc_off changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000466 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_set_parent
- Explanation: irq_set_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000467 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_set_percpu_devid
- Explanation: irq_set_percpu_devid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000468 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_set_vcpu_affinity
- Explanation: irq_set_vcpu_affinity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000469 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_setup_alt_chip
- Explanation: irq_setup_alt_chip changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000470 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_setup_generic_chip
- Explanation: irq_setup_generic_chip changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000471 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_suspended
- Explanation: irq_suspended changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(18usize, 1u8) as u32) } } #[inline] pub fn set_irq_suspended(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(20usize, 1u8) as u32) } } #[inline] pub fn set_irq_suspended(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000472 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_unlock_sparse
- Explanation: irq_unlock_sparse changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000473 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_unmap_generic_chip
- Explanation: irq_unmap_generic_chip changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000474 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irqd_cfg
- Explanation: irqd_cfg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000475 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_b_host
- Explanation: is_b_host changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000476 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_current_namespace
- Explanation: is_current_namespace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000477 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_hotplug_bridge
- Explanation: is_hotplug_bridge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(25usize, 1u8) as u32) } } #[inline] pub fn set_is_hotplug_bridge(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(26usize, 1u8) as u32) } } #[inline] pub fn set_is_hotplug_bridge(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000478 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_level
- Explanation: is_level changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000479 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_managed
- Explanation: is_managed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(19usize, 1u8) as u32) } } #[inline] pub fn set_is_managed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(20usize, 1u8) as u32) } } #[inline] pub fn set_is_managed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000480 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_msi_managed
- Explanation: is_msi_managed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(20usize, 1u8) as u32) } } #[inline] pub fn set_is_msi_managed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(21usize, 1u8) as u32) } } #[inline] pub fn set_is_msi_managed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000481 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_pciehp
- Explanation: is_pciehp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(26usize, 1u8) as u32) } } #[inline] pub fn set_is_pciehp(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(27usize, 1u8) as u32) } } #[inline] pub fn set_is_pciehp(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000482 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_physfn
- Explanation: is_physfn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(23usize, 1u8) as u32) } } #[inline] pub fn set_is_physfn(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(24usize, 1u8) as u32) } } #[inline] pub fn set_is_physfn(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000483 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_probed
- Explanation: is_probed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(35usize, 1u8) as u32) } } #[inline] pub fn set_is_probed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(36usize, 1u8) as u32) } } #[inline] pub fn set_is_probed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000484 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_thunderbolt
- Explanation: is_thunderbolt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(28usize, 1u8) as u32) } } #[inline] pub fn set_is_thunderbolt(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(29usize, 1u8) as u32) } } #[inline] pub fn set_is_thunderbolt(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000485 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_uprobe_at_func_entry
- Explanation: is_uprobe_at_func_entry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000486 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_virtfn
- Explanation: is_virtfn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(24usize, 1u8) as u32) } } #[inline] pub fn set_is_virtfn(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(25usize, 1u8) as u32) } } #[inline] pub fn set_is_virtfn(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000487 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_bind
- Explanation: kernel_bind changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'sock', 'type': '*mut socket'}, {'name': 'addr', 'type': '*mut sockaddr'}, {'name': 'addrlen', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'sock', 'type': '*mut socket'}, {'name': 'addr', 'type': '*mut sockaddr_unsized'}, {'name': 'addrlen', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000488 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_connect
- Explanation: kernel_connect changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'sock', 'type': '*mut socket'}, {'name': 'addr', 'type': '*mut sockaddr'}, {'name': 'addrlen', 'type': 'ffi::c_int'}, {'name': 'flags', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'sock', 'type': '*mut socket'}, {'name': 'addr', 'type': '*mut sockaddr_unsized'}, {'name': 'addrlen', 'type': 'ffi::c_int'}, {'name': 'flags', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000490 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kvfree_rcu_barrier_on_cache
- Explanation: kvfree_rcu_barrier_on_cache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000492 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: link_active_reporting
- Explanation: link_active_reporting changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(36usize, 1u8) as u32) } } #[inline] pub fn set_link_active_reporting(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(37usize, 1u8) as u32) } } #[inline] pub fn set_link_active_reporting(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000493 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lock_vector_lock
- Explanation: lock_vector_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000494 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lpm_capable
- Explanation: lpm_capable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000495 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lpm_devinit_allow
- Explanation: lpm_devinit_allow changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000496 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: machine_kexec_mask_interrupts
- Explanation: machine_kexec_mask_interrupts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000497 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_alloc_bulk_noprof
- Explanation: mempool_alloc_bulk_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000498 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_alloc_noprof
- Explanation: mempool_alloc_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'pool', 'type': '*mut mempool_t'}, {'name': 'gfp_mask', 'type': 'gfp_t'}], 'return_type': '*mut ffi::c_void'}`
- New: `{'params': [{'name': 'pool', 'type': '*mut mempool'}, {'name': 'gfp_mask', 'type': 'gfp_t'}], 'return_type': '*mut ffi::c_void'}`

### Rust Evidence

- Graph edges: `1`

## W-000499 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_alloc_preallocated
- Explanation: mempool_alloc_preallocated changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'pool', 'type': '*mut mempool_t'}], 'return_type': '*mut ffi::c_void'}`
- New: `{'params': [{'name': 'pool', 'type': '*mut mempool'}], 'return_type': '*mut ffi::c_void'}`

### Rust Evidence

- Graph edges: `1`

## W-000501 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_create_node_noprof
- Explanation: mempool_create_node_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'min_nr', 'type': 'ffi::c_int'}, {'name': 'alloc_fn', 'type': 'mempool_alloc_t'}, {'name': 'free_fn', 'type': 'mempool_free_t'}, {'name': 'pool_data', 'type': '*mut ffi::c_void'}, {'name': 'gfp_mask', 'type': 'gfp_t'}, {'name': 'nid', 'type': 'ffi::c_int'}], 'return_type': '*mut mempool_t'}`
- New: `{'params': [{'name': 'min_nr', 'type': 'ffi::c_int'}, {'name': 'alloc_fn', 'type': 'mempool_alloc_t'}, {'name': 'free_fn', 'type': 'mempool_free_t'}, {'name': 'pool_data', 'type': '*mut ffi::c_void'}, {'name': 'gfp_mask', 'type': 'gfp_t'}, {'name': 'nid', 'type': 'ffi::c_int'}], 'return_type': '*mut mempool'}`

### Rust Evidence

- Graph edges: `1`

## W-000502 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_destroy
- Explanation: mempool_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'pool', 'type': '*mut mempool_t'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'pool', 'type': '*mut mempool'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000503 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_exit
- Explanation: mempool_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'pool', 'type': '*mut mempool_t'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'pool', 'type': '*mut mempool'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000505 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_free_bulk
- Explanation: mempool_free_bulk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000506 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_init_node
- Explanation: mempool_init_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'pool', 'type': '*mut mempool_t'}, {'name': 'min_nr', 'type': 'ffi::c_int'}, {'name': 'alloc_fn', 'type': 'mempool_alloc_t'}, {'name': 'free_fn', 'type': 'mempool_free_t'}, {'name': 'pool_data', 'type': '*mut ffi::c_void'}, {'name': 'gfp_mask', 'type': 'gfp_t'}, {'name': 'node_id', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'pool', 'type': '*mut mempool'}, {'name': 'min_nr', 'type': 'ffi::c_int'}, {'name': 'alloc_fn', 'type': 'mempool_alloc_t'}, {'name': 'free_fn', 'type': 'mempool_free_t'}, {'name': 'pool_data', 'type': '*mut ffi::c_void'}, {'name': 'gfp_mask', 'type': 'gfp_t'}, {'name': 'node_id', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000507 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_init_noprof
- Explanation: mempool_init_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'pool', 'type': '*mut mempool_t'}, {'name': 'min_nr', 'type': 'ffi::c_int'}, {'name': 'alloc_fn', 'type': 'mempool_alloc_t'}, {'name': 'free_fn', 'type': 'mempool_free_t'}, {'name': 'pool_data', 'type': '*mut ffi::c_void'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'pool', 'type': '*mut mempool'}, {'name': 'min_nr', 'type': 'ffi::c_int'}, {'name': 'alloc_fn', 'type': 'mempool_alloc_t'}, {'name': 'free_fn', 'type': 'mempool_free_t'}, {'name': 'pool_data', 'type': '*mut ffi::c_void'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000510 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mempool_resize
- Explanation: mempool_resize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'pool', 'type': '*mut mempool_t'}, {'name': 'new_min_nr', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'pool', 'type': '*mut mempool'}, {'name': 'new_min_nr', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000512 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mm_get_unmapped_area_vmflags
- Explanation: mm_get_unmapped_area_vmflags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'filp', 'type': '*mut file'}, {'name': 'addr', 'type': 'ffi::c_ulong'}, {'name': 'len', 'type': 'ffi::c_ulong'}, {'name': 'pgoff', 'type': 'ffi::c_ulong'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'vm_flags', 'type': 'vm_flags_t'}], 'return_type': 'ffi::c_ulong'}`
- New: `{'params': [{'name': 'filp', 'type': '*mut file'}, {'name': 'addr', 'type': 'ffi::c_ulong'}, {'name': 'len', 'type': 'ffi::c_ulong'}, {'name': 'pgoff', 'type': 'ffi::c_ulong'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'vm_flags', 'type': 'vm_flags_t'}], 'return_type': 'ffi::c_ulong'}`

### Rust Evidence

- Graph edges: `1`

## W-000513 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mm_init_cid
- Explanation: mm_init_cid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000514 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmap_action_complete
- Explanation: mmap_action_complete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000515 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmap_action_prepare
- Explanation: mmap_action_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000516 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: module_add_driver
- Explanation: module_add_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000517 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: module_remove_driver
- Explanation: module_remove_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000518 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mp_irqdomain_activate
- Explanation: mp_irqdomain_activate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000519 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mp_irqdomain_alloc
- Explanation: mp_irqdomain_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000520 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mp_irqdomain_deactivate
- Explanation: mp_irqdomain_deactivate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000521 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mp_irqdomain_free
- Explanation: mp_irqdomain_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000522 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mp_irqdomain_ioapic_idx
- Explanation: mp_irqdomain_ioapic_idx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000523 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: msi_device_domain_alloc_wired
- Explanation: msi_device_domain_alloc_wired changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000524 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: msi_device_domain_free_wired
- Explanation: msi_device_domain_free_wired changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000525 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mutex_init_generic
- Explanation: mutex_init_generic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000526 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: native_create_pci_msi_domain
- Explanation: native_create_pci_msi_domain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000527 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: native_play_dead
- Explanation: native_play_dead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': '()'}`
- New: `{'params': [], 'return_type': '!'}`

### Rust Evidence

- Graph edges: `1`

## W-000528 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: needs_altsetting0
- Explanation: needs_altsetting0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000529 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: needs_binding
- Explanation: needs_binding changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000530 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: needs_freset
- Explanation: needs_freset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(21usize, 1u8) as u32) } } #[inline] pub fn set_needs_freset(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(22usize, 1u8) as u32) } } #[inline] pub fn set_needs_freset(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000531 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: needs_remote_wakeup
- Explanation: needs_remote_wakeup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000532 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_bitfield_1
- Explanation: new_bitfield_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'is_c45', 'type': 'ffi::c_uint'}, {'name': 'is_internal', 'type': 'ffi::c_uint'}, {'name': 'is_pseudo_fixed_link', 'type': 'ffi::c_uint'}, {'name': 'is_gigabit_capable', 'type': 'ffi::c_uint'}, {'name': 'has_fixups', 'type': 'ffi::c_uint'}, {'name': 'suspended', 'type': 'ffi::c_uint'}, {'name': 'suspended_by_mdio_bus', 'type': 'ffi::c_uint'}, {'name': 'sysfs_links', 'type': 'ffi::c_uint'}, {'name': 'loopback_enabled', 'type': 'ffi::c_uint'}, {'name': 'downshifted_rate', 'type': 'ffi::c_uint'}, {'name': 'is_on_sfp_module', 'type': 'ffi::c_uint'}, {'name': 'mac_managed_pm', 'type': 'ffi::c_uint'}, {'name': 'wol_enabled', 'type': 'ffi::c_uint'}, {'name': 'is_genphy_driven', 'type': 'ffi::c_uint'}, {'name': 'autoneg', 'type': 'ffi::c_uint'}, {'name': 'link', 'type': 'ffi::c_uint'}, {'name': 'autoneg_complete', 'type': 'ffi::c_uint'}, {'name': 'interrupts', 'type': 'ffi::c_uint'}, {'name': 'irq_suspended', 'type': 'ffi::c_uint'}, {'name': 'irq_rerun', 'type': 'ffi::c_uint'}, {'name': 'default_timestamp', 'type': 'ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`
- New: `{'params': [{'name': 'dead', 'type': 'u8_'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`

### Rust Evidence

- Graph edges: `1`

## W-000533 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_bitfield_2
- Explanation: new_bitfield_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'pme_support', 'type': 'ffi::c_uint'}, {'name': 'pme_poll', 'type': 'ffi::c_uint'}, {'name': 'pinned', 'type': 'ffi::c_uint'}, {'name': 'config_rrs_sv', 'type': 'ffi::c_uint'}, {'name': 'imm_ready', 'type': 'ffi::c_uint'}, {'name': 'd1_support', 'type': 'ffi::c_uint'}, {'name': 'd2_support', 'type': 'ffi::c_uint'}, {'name': 'no_d1d2', 'type': 'ffi::c_uint'}, {'name': 'no_d3cold', 'type': 'ffi::c_uint'}, {'name': 'bridge_d3', 'type': 'ffi::c_uint'}, {'name': 'd3cold_allowed', 'type': 'ffi::c_uint'}, {'name': 'mmio_always_on', 'type': 'ffi::c_uint'}, {'name': 'wakeup_prepared', 'type': 'ffi::c_uint'}, {'name': 'skip_bus_pm', 'type': 'ffi::c_uint'}, {'name': 'ignore_hotplug', 'type': 'ffi::c_uint'}, {'name': 'hotplug_user_indicators', 'type': 'ffi::c_uint'}, {'name': 'clear_retrain_link', 'type': 'ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`
- New: `{'params': [{'name': 'do_remote_wakeup', 'type': 'ffi::c_uint'}, {'name': 'reset_resume', 'type': 'ffi::c_uint'}, {'name': 'port_is_suspended', 'type': 'ffi::c_uint'}, {'name': 'offload_at_suspend', 'type': 'ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`

### Rust Evidence

- Graph edges: `1`

## W-000534 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_bitfield_3
- Explanation: new_bitfield_3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'aspm_l0s_support', 'type': 'ffi::c_uint'}, {'name': 'aspm_l1_support', 'type': 'ffi::c_uint'}, {'name': 'ltr_path', 'type': 'ffi::c_uint'}, {'name': 'pasid_no_tlp', 'type': 'ffi::c_uint'}, {'name': 'eetlp_prefix_max', 'type': 'ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`
- New: `{'params': [{'name': 'use_generic_driver', 'type': 'ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`

### Rust Evidence

- Graph edges: `1`

## W-000535 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_bitfield_4
- Explanation: new_bitfield_4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'transparent', 'type': 'ffi::c_uint'}, {'name': 'io_window', 'type': 'ffi::c_uint'}, {'name': 'pref_window', 'type': 'ffi::c_uint'}, {'name': 'pref_64_window', 'type': 'ffi::c_uint'}, {'name': 'multifunction', 'type': 'ffi::c_uint'}, {'name': 'is_busmaster', 'type': 'ffi::c_uint'}, {'name': 'no_msi', 'type': 'ffi::c_uint'}, {'name': 'no_64bit_msi', 'type': 'ffi::c_uint'}, {'name': 'block_cfg_access', 'type': 'ffi::c_uint'}, {'name': 'broken_parity_status', 'type': 'ffi::c_uint'}, {'name': 'irq_reroute_variant', 'type': 'ffi::c_uint'}, {'name': 'msi_enabled', 'type': 'ffi::c_uint'}, {'name': 'msix_enabled', 'type': 'ffi::c_uint'}, {'name': 'ari_enabled', 'type': 'ffi::c_uint'}, {'name': 'ats_enabled', 'type': 'ffi::c_uint'}, {'name': 'pasid_enabled', 'type': 'ffi::c_uint'}, {'name': 'pri_enabled', 'type': 'ffi::c_uint'}, {'name': 'tph_enabled', 'type': 'ffi::c_uint'}, {'name': 'is_managed', 'type': 'ffi::c_uint'}, {'name': 'is_msi_managed', 'type': 'ffi::c_uint'}, {'name': 'needs_freset', 'type': 'ffi::c_uint'}, {'name': 'state_saved', 'type': 'ffi::c_uint'}, {'name': 'is_physfn', 'type': 'ffi::c_uint'}, {'name': 'is_virtfn', 'type': 'ffi::c_uint'}, {'name': 'is_hotplug_bridge', 'type': 'ffi::c_uint'}, {'name': 'is_pciehp', 'type': 'ffi::c_uint'}, {'name': 'shpc_managed', 'type': 'ffi::c_uint'}, {'name': 'is_thunderbolt', 'type': 'ffi::c_uint'}, {'name': 'untrusted', 'type': 'ffi::c_uint'}, {'name': 'external_facing', 'type': 'ffi::c_uint'}, {'name': 'broken_intx_masking', 'type': 'ffi::c_uint'}, {'name': 'io_window_1k', 'type': 'ffi::c_uint'}, {'name': 'irq_managed', 'type': 'ffi::c_uint'}, {'name': 'non_compliant_bars', 'type': 'ffi::c_uint'}, {'name': 'is_probed', 'type': 'ffi::c_uint'}, {'name': 'link_active_reporting', 'type': 'ffi::c_uint'}, {'name': 'no_vf_scan', 'type': 'ffi::c_uint'}, {'name': 'no_command_memory', 'type': 'ffi::c_uint'}, {'name': 'rom_bar_overlap', 'type': 'ffi::c_uint'}, {'name': 'rom_attr_enabled', 'type': 'ffi::c_uint'}, {'name': 'non_mappable_bars', 'type': 'ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`
- New: `{'params': [{'name': 'transparent', 'type': 'ffi::c_uint'}, {'name': 'io_window', 'type': 'ffi::c_uint'}, {'name': 'pref_window', 'type': 'ffi::c_uint'}, {'name': 'pref_64_window', 'type': 'ffi::c_uint'}, {'name': 'multifunction', 'type': 'ffi::c_uint'}, {'name': 'is_busmaster', 'type': 'ffi::c_uint'}, {'name': 'no_msi', 'type': 'ffi::c_uint'}, {'name': 'no_64bit_msi', 'type': 'ffi::c_uint'}, {'name': 'block_cfg_access', 'type': 'ffi::c_uint'}, {'name': 'broken_parity_status', 'type': 'ffi::c_uint'}, {'name': 'irq_reroute_variant', 'type': 'ffi::c_uint'}, {'name': 'msi_enabled', 'type': 'ffi::c_uint'}, {'name': 'msix_enabled', 'type': 'ffi::c_uint'}, {'name': 'ari_enabled', 'type': 'ffi::c_uint'}, {'name': 'ats_enabled', 'type': 'ffi::c_uint'}, {'name': 'pasid_enabled', 'type': 'ffi::c_uint'}, {'name': 'pri_enabled', 'type': 'ffi::c_uint'}, {'name': 'tph_enabled', 'type': 'ffi::c_uint'}, {'name': 'fm_enabled', 'type': 'ffi::c_uint'}, {'name': 'is_managed', 'type': 'ffi::c_uint'}, {'name': 'is_msi_managed', 'type': 'ffi::c_uint'}, {'name': 'needs_freset', 'type': 'ffi::c_uint'}, {'name': 'state_saved', 'type': 'ffi::c_uint'}, {'name': 'is_physfn', 'type': 'ffi::c_uint'}, {'name': 'is_virtfn', 'type': 'ffi::c_uint'}, {'name': 'is_hotplug_bridge', 'type': 'ffi::c_uint'}, {'name': 'is_pciehp', 'type': 'ffi::c_uint'}, {'name': 'shpc_managed', 'type': 'ffi::c_uint'}, {'name': 'is_thunderbolt', 'type': 'ffi::c_uint'}, {'name': 'untrusted', 'type': 'ffi::c_uint'}, {'name': 'external_facing', 'type': 'ffi::c_uint'}, {'name': 'broken_intx_masking', 'type': 'ffi::c_uint'}, {'name': 'io_window_1k', 'type': 'ffi::c_uint'}, {'name': 'irq_managed', 'type': 'ffi::c_uint'}, {'name': 'non_compliant_bars', 'type': 'ffi::c_uint'}, {'name': 'is_probed', 'type': 'ffi::c_uint'}, {'name': 'link_active_reporting', 'type': 'ffi::c_uint'}, {'name': 'no_vf_scan', 'type': 'ffi::c_uint'}, {'name': 'no_command_memory', 'type': 'ffi::c_uint'}, {'name': 'rom_bar_overlap', 'type': 'ffi::c_uint'}, {'name': 'rom_attr_enabled', 'type': 'ffi::c_uint'}, {'name': 'non_mappable_bars', 'type': 'ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`

### Rust Evidence

- Graph edges: `1`

## W-000536 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_command_memory
- Explanation: no_command_memory changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(38usize, 1u8) as u32) } } #[inline] pub fn set_no_command_memory(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(39usize, 1u8) as u32) } } #[inline] pub fn set_no_command_memory(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000537 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_dynamic_id
- Explanation: no_dynamic_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000538 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_sg_constraint
- Explanation: no_sg_constraint changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000539 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_stop_on_short
- Explanation: no_stop_on_short changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000540 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_vf_scan
- Explanation: no_vf_scan changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(37usize, 1u8) as u32) } } #[inline] pub fn set_no_vf_scan(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(38usize, 1u8) as u32) } } #[inline] pub fn set_no_vf_scan(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000541 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: noirqdebug_setup
- Explanation: noirqdebug_setup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000542 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: non_compliant_bars
- Explanation: non_compliant_bars changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(34usize, 1u8) as u32) } } #[inline] pub fn set_non_compliant_bars(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(35usize, 1u8) as u32) } } #[inline] pub fn set_non_compliant_bars(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000543 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: non_mappable_bars
- Explanation: non_mappable_bars changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(41usize, 1u8) as u32) } } #[inline] pub fn set_non_mappable_bars(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(42usize, 1u8) as u32) } } #[inline] pub fn set_non_mappable_bars(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000544 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: note_interrupt
- Explanation: note_interrupt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000545 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: notify_change
- Explanation: notify_change changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut mnt_idmap'}, {'name': 'arg2', 'type': '*mut dentry'}, {'name': 'arg3', 'type': '*mut iattr'}, {'name': 'arg4', 'type': '*mut *mut inode'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*mut mnt_idmap'}, {'name': 'arg2', 'type': '*mut dentry'}, {'name': 'arg3', 'type': '*mut iattr'}, {'name': 'arg4', 'type': '*mut delegated_inode'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000546 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ns_owner
- Explanation: ns_owner changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000547 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: of_phandle_args_to_fwspec
- Explanation: of_phandle_args_to_fwspec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000548 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: offload_at_suspend
- Explanation: offload_at_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000549 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: out_band_wakeup
- Explanation: out_band_wakeup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000551 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pause
- Explanation: pause changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000552 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bus_find_emul_domain_nr
- Explanation: pci_bus_find_emul_domain_nr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000553 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_bus_release_emul_domain_nr
- Explanation: pci_bus_release_emul_domain_nr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000555 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_get_host_bridge_device
- Explanation: pci_get_host_bridge_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000556 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_msi_prepare
- Explanation: pci_msi_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000557 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_rebar_bytes_to_size
- Explanation: pci_rebar_bytes_to_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000558 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_rebar_get_max_size
- Explanation: pci_rebar_get_max_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000559 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_rebar_get_possible_sizes
- Explanation: pci_rebar_get_possible_sizes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'pdev', 'type': '*mut pci_dev'}, {'name': 'bar', 'type': 'ffi::c_int'}], 'return_type': 'u32_'}`
- New: `{'params': [{'name': 'pdev', 'type': '*mut pci_dev'}, {'name': 'bar', 'type': 'ffi::c_int'}], 'return_type': 'u64_'}`

### Rust Evidence

- Graph edges: `1`

## W-000560 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_rebar_size_supported
- Explanation: pci_rebar_size_supported changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000561 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_rebar_size_to_bytes
- Explanation: pci_rebar_size_to_bytes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000562 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_resize_resource
- Explanation: pci_resize_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'dev', 'type': '*mut pci_dev'}, {'name': 'i', 'type': 'ffi::c_int'}, {'name': 'size', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'dev', 'type': '*mut pci_dev'}, {'name': 'i', 'type': 'ffi::c_int'}, {'name': 'size', 'type': 'ffi::c_int'}, {'name': 'exclude_bars', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000563 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_walk_bus_reverse
- Explanation: pci_walk_bus_reverse changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000564 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: persist_enabled
- Explanation: persist_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000566 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_find_next
- Explanation: phy_find_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000567 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_fix_phy_mode_for_mac_delays
- Explanation: phy_fix_phy_mode_for_mac_delays changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000568 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_may_wakeup
- Explanation: phy_may_wakeup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000569 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pinconf_generic_dt_free_map
- Explanation: pinconf_generic_dt_free_map changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000571 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pinconf_generic_dt_node_to_map_pinmux
- Explanation: pinconf_generic_dt_node_to_map_pinmux changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000572 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pinconf_generic_dt_subnode_to_map
- Explanation: pinconf_generic_dt_subnode_to_map changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000574 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pinctrl_add_gpio_ranges
- Explanation: pinctrl_add_gpio_ranges changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000575 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pinctrl_dev_get_devname
- Explanation: pinctrl_dev_get_devname changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000576 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pinctrl_dev_get_drvdata
- Explanation: pinctrl_dev_get_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000577 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pinctrl_dev_get_name
- Explanation: pinctrl_dev_get_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000578 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pinctrl_enable
- Explanation: pinctrl_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000579 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pinctrl_find_and_add_gpio_range
- Explanation: pinctrl_find_and_add_gpio_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000580 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pinctrl_find_gpio_range_from_pin
- Explanation: pinctrl_find_gpio_range_from_pin changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000581 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pinctrl_get_group_pins
- Explanation: pinctrl_get_group_pins changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000583 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pinctrl_register_and_init
- Explanation: pinctrl_register_and_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000584 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pinctrl_remove_gpio_range
- Explanation: pinctrl_remove_gpio_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000585 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pinctrl_unregister
- Explanation: pinctrl_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000586 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_bus_init
- Explanation: platform_bus_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000587 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: platform_get_irq_affinity
- Explanation: platform_get_irq_affinity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000588 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_generic_runtime_resume
- Explanation: pm_generic_runtime_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000589 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_generic_runtime_suspend
- Explanation: pm_generic_runtime_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000590 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_runtime_allow
- Explanation: pm_runtime_allow changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000591 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_runtime_autosuspend_expiration
- Explanation: pm_runtime_autosuspend_expiration changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000592 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_runtime_barrier
- Explanation: pm_runtime_barrier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000593 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_runtime_block_if_disabled
- Explanation: pm_runtime_block_if_disabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000594 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_runtime_drop_link
- Explanation: pm_runtime_drop_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000595 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_runtime_enable
- Explanation: pm_runtime_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000596 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_runtime_forbid
- Explanation: pm_runtime_forbid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000597 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_runtime_force_resume
- Explanation: pm_runtime_force_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000598 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_runtime_force_suspend
- Explanation: pm_runtime_force_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000599 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_runtime_get_if_active
- Explanation: pm_runtime_get_if_active changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000600 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_runtime_get_if_in_use
- Explanation: pm_runtime_get_if_in_use changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000601 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_runtime_get_suppliers
- Explanation: pm_runtime_get_suppliers changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000602 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_runtime_irq_safe
- Explanation: pm_runtime_irq_safe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000603 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_runtime_need_not_resume
- Explanation: pm_runtime_need_not_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000604 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_runtime_new_link
- Explanation: pm_runtime_new_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000605 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_runtime_no_callbacks
- Explanation: pm_runtime_no_callbacks changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000606 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_runtime_put_suppliers
- Explanation: pm_runtime_put_suppliers changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000607 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_runtime_release_supplier
- Explanation: pm_runtime_release_supplier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000608 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_runtime_set_autosuspend_delay
- Explanation: pm_runtime_set_autosuspend_delay changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000609 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_runtime_set_memalloc_noio
- Explanation: pm_runtime_set_memalloc_noio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000610 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_runtime_suspended_time
- Explanation: pm_runtime_suspended_time changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000611 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_runtime_unblock
- Explanation: pm_runtime_unblock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000612 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_schedule_suspend
- Explanation: pm_schedule_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000613 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_vt_switch_required
- Explanation: pm_vt_switch_required changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'dev', 'type': '*mut device'}, {'name': 'required', 'type': 'bool_'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'dev', 'type': '*mut device'}, {'name': 'required', 'type': 'bool_'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000614 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: poisoned
- Explanation: poisoned changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000615 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: port_is_suspended
- Explanation: port_is_suspended changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000616 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_dointvec_conv
- Explanation: proc_dointvec_conv changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000617 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_dointvec_jiffies
- Explanation: proc_dointvec_jiffies changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*const ctl_table'}, {'name': 'arg2', 'type': 'ffi::c_int'}, {'name': 'arg3', 'type': '*mut ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'table', 'type': '*const ctl_table'}, {'name': 'dir', 'type': 'ffi::c_int'}, {'name': 'buffer', 'type': '*mut ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000618 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_dointvec_minmax
- Explanation: proc_dointvec_minmax changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*const ctl_table'}, {'name': 'arg2', 'type': 'ffi::c_int'}, {'name': 'arg3', 'type': '*mut ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'table', 'type': '*const ctl_table'}, {'name': 'dir', 'type': 'ffi::c_int'}, {'name': 'buffer', 'type': '*mut ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000620 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_dointvec_ms_jiffies_minmax
- Explanation: proc_dointvec_ms_jiffies_minmax changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'table', 'type': '*const ctl_table'}, {'name': 'write', 'type': 'ffi::c_int'}, {'name': 'buffer', 'type': '*mut ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'table', 'type': '*const ctl_table'}, {'name': 'dir', 'type': 'ffi::c_int'}, {'name': 'buffer', 'type': '*mut ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000621 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_dointvec_userhz_jiffies
- Explanation: proc_dointvec_userhz_jiffies changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*const ctl_table'}, {'name': 'arg2', 'type': 'ffi::c_int'}, {'name': 'arg3', 'type': '*mut ffi::c_void'}, {'name': 'arg4', 'type': '*mut usize'}, {'name': 'arg5', 'type': '*mut loff_t'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'table', 'type': '*const ctl_table'}, {'name': 'dir', 'type': 'ffi::c_int'}, {'name': 'buffer', 'type': '*mut ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000622 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_douintvec_conv
- Explanation: proc_douintvec_conv changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000623 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_doulongvec_minmax_conv
- Explanation: proc_doulongvec_minmax_conv changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000624 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: proc_doulongvec_ms_jiffies_minmax
- Explanation: proc_doulongvec_ms_jiffies_minmax changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'table', 'type': '*const ctl_table'}, {'name': 'arg1', 'type': 'ffi::c_int'}, {'name': 'arg2', 'type': '*mut ffi::c_void'}, {'name': 'arg3', 'type': '*mut usize'}, {'name': 'arg4', 'type': '*mut loff_t'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'table', 'type': '*const ctl_table'}, {'name': 'dir', 'type': 'ffi::c_int'}, {'name': 'buffer', 'type': '*mut ffi::c_void'}, {'name': 'lenp', 'type': '*mut usize'}, {'name': 'ppos', 'type': '*mut loff_t'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000625 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: profile_hits
- Explanation: profile_hits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000626 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: profile_init
- Explanation: profile_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000627 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: profile_setup
- Explanation: profile_setup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000628 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: profile_tick
- Explanation: profile_tick changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000630 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pwmchip_parent
- Explanation: pwmchip_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000631 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pwmchip_set_drvdata
- Explanation: pwmchip_set_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000634 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: redirect_hint
- Explanation: redirect_hint changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000635 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: register_node
- Explanation: register_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000637 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: remap_pfn_range
- Explanation: remap_pfn_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut vm_area_struct'}, {'name': 'addr', 'type': 'ffi::c_ulong'}, {'name': 'pfn', 'type': 'ffi::c_ulong'}, {'name': 'size', 'type': 'ffi::c_ulong'}, {'name': 'arg2', 'type': 'pgprot_t'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'addr', 'type': 'ffi::c_ulong'}, {'name': 'pfn', 'type': 'ffi::c_ulong'}, {'name': 'size', 'type': 'ffi::c_ulong'}, {'name': 'pgprot', 'type': 'pgprot_t'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000639 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: report_bug_entry
- Explanation: report_bug_entry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000640 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: request_percpu_nmi
- Explanation: request_percpu_nmi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'handler', 'type': 'irq_handler_t'}, {'name': 'devname', 'type': '*const ffi::c_char'}, {'name': 'dev', 'type': '*mut ffi::c_void'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'handler', 'type': 'irq_handler_t'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'affinity', 'type': '*const cpumask'}, {'name': 'dev_id', 'type': '*mut ffi::c_void'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000642 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: reserved_0
- Explanation: reserved_0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000643 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: reserved_1
- Explanation: reserved_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000644 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: reset_in_progress
- Explanation: reset_in_progress changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000645 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: reset_resume
- Explanation: reset_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000646 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: resetting_device
- Explanation: resetting_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000647 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rom_attr_enabled
- Explanation: rom_attr_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(40usize, 1u8) as u32) } } #[inline] pub fn set_rom_attr_enabled(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(41usize, 1u8) as u32) } } #[inline] pub fn set_rom_attr_enabled(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000648 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rom_bar_overlap
- Explanation: rom_bar_overlap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(39usize, 1u8) as u32) } } #[inline] pub fn set_rom_bar_overlap(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(40usize, 1u8) as u32) } } #[inline] pub fn set_rom_bar_overlap(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000649 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sched_mm_cid_exit
- Explanation: sched_mm_cid_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000651 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sched_set_fifo_secondary
- Explanation: sched_set_fifo_secondary changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000652 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_cpu_possible
- Explanation: set_cpu_possible changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000653 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_cpus_allowed_force
- Explanation: set_cpus_allowed_force changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000654 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: setup_percpu_irq
- Explanation: setup_percpu_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000655 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: setup_profiling_timer
- Explanation: setup_profiling_timer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000656 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: shpc_managed
- Explanation: shpc_managed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(27usize, 1u8) as u32) } } #[inline] pub fn set_shpc_managed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(28usize, 1u8) as u32) } } #[inline] pub fn set_shpc_managed(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000657 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: shrink_dentry_list
- Explanation: shrink_dentry_list changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000658 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_done_creating
- Explanation: simple_done_creating changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000660 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: simple_remove_by_name
- Explanation: simple_remove_by_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000661 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: soft_unbind
- Explanation: soft_unbind changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000663 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: software_node_notify_remove
- Explanation: software_node_notify_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000664 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: srcu_expedite_current
- Explanation: srcu_expedite_current changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000665 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: state_saved
- Explanation: state_saved changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(22usize, 1u8) as u32) } } #[inline] pub fn set_state_saved(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(23usize, 1u8) as u32) } } #[inline] pub fn set_state_saved(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000666 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: strict_midlayer
- Explanation: strict_midlayer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_2.get(7usize, 1u8) as u8) } } #[inline] pub fn set_strict_midlayer(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'bool_ { unsafe { ::core::mem::transmute(self._bitfield_2.get(8usize, 1u8) as u8) } } #[inline] pub fn set_strict_midlayer(&mut self, val: bool_) { unsafe { let val: u8 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000667 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: supports_autosuspend
- Explanation: supports_autosuspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000668 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: switch_cred_namespaces
- Explanation: switch_cred_namespaces changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000669 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysctl_kern_to_user_uint_conv
- Explanation: sysctl_kern_to_user_uint_conv changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000670 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_files_created
- Explanation: sysfs_files_created changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000671 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: tlb_gather_mmu_vma
- Explanation: tlb_gather_mmu_vma changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000672 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: tmigr_isolated_exclude_cpumask
- Explanation: tmigr_isolated_exclude_cpumask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000674 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: truncate_inode_pages_final
- Explanation: truncate_inode_pages_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut address_space'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'mapping', 'type': '*mut address_space'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000675 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: truncate_inode_pages_range
- Explanation: truncate_inode_pages_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut address_space'}, {'name': 'lstart', 'type': 'loff_t'}, {'name': 'lend', 'type': 'loff_t'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'mapping', 'type': '*mut address_space'}, {'name': 'lstart', 'type': 'loff_t'}, {'name': 'lend', 'type': 'uoff_t'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000677 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unlock_vector_lock
- Explanation: unlock_vector_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000678 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unmap_vmas
- Explanation: unmap_vmas changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'tlb', 'type': '*mut mmu_gather'}, {'name': 'mas', 'type': '*mut ma_state'}, {'name': 'start_vma', 'type': '*mut vm_area_struct'}, {'name': 'start', 'type': 'ffi::c_ulong'}, {'name': 'end', 'type': 'ffi::c_ulong'}, {'name': 'tree_end', 'type': 'ffi::c_ulong'}, {'name': 'mm_wr_locked', 'type': 'bool_'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'tlb', 'type': '*mut mmu_gather'}, {'name': 'mas', 'type': '*mut ma_state'}, {'name': 'start_vma', 'type': '*mut vm_area_struct'}, {'name': 'start', 'type': 'ffi::c_ulong'}, {'name': 'end', 'type': 'ffi::c_ulong'}, {'name': 'tree_end', 'type': 'ffi::c_ulong'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000679 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unregister_node
- Explanation: unregister_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'node', 'type': '*mut node'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'nid', 'type': 'ffi::c_int'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000681 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unregistering
- Explanation: unregistering changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000682 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: untrusted
- Explanation: untrusted changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(29usize, 1u8) as u32) } } #[inline] pub fn set_untrusted(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_4.get(30usize, 1u8) as u32) } } #[inline] pub fn set_untrusted(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000683 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb2_hw_lpm_allowed
- Explanation: usb2_hw_lpm_allowed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000684 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb2_hw_lpm_besl_capable
- Explanation: usb2_hw_lpm_besl_capable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000685 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb2_hw_lpm_capable
- Explanation: usb2_hw_lpm_capable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000686 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb2_hw_lpm_enabled
- Explanation: usb2_hw_lpm_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000687 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb3_lpm_u1_enabled
- Explanation: usb3_lpm_u1_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000688 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb3_lpm_u2_enabled
- Explanation: usb3_lpm_u2_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000689 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_acpi_port_lpm_incapable
- Explanation: usb_acpi_port_lpm_incapable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000690 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_acpi_power_manageable
- Explanation: usb_acpi_power_manageable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000691 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_acpi_set_power_state
- Explanation: usb_acpi_set_power_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000692 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_alloc_coherent
- Explanation: usb_alloc_coherent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000693 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_alloc_noncoherent
- Explanation: usb_alloc_noncoherent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000694 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_alloc_streams
- Explanation: usb_alloc_streams changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000695 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_alloc_urb
- Explanation: usb_alloc_urb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000696 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_altnum_to_altsetting
- Explanation: usb_altnum_to_altsetting changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000697 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_anchor_empty
- Explanation: usb_anchor_empty changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000698 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_anchor_resume_wakeups
- Explanation: usb_anchor_resume_wakeups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000699 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_anchor_suspend_wakeups
- Explanation: usb_anchor_suspend_wakeups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000700 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_anchor_urb
- Explanation: usb_anchor_urb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000702 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_autopm_get_interface_async
- Explanation: usb_autopm_get_interface_async changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000703 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_autopm_get_interface_no_resume
- Explanation: usb_autopm_get_interface_no_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000705 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_autopm_put_interface_async
- Explanation: usb_autopm_put_interface_async changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000706 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_autopm_put_interface_no_suspend
- Explanation: usb_autopm_put_interface_no_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000707 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_block_urb
- Explanation: usb_block_urb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000708 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_bulk_msg
- Explanation: usb_bulk_msg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000709 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_cache_string
- Explanation: usb_cache_string changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000710 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_check_bulk_endpoints
- Explanation: usb_check_bulk_endpoints changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000711 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_check_int_endpoints
- Explanation: usb_check_int_endpoints changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000712 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_choose_configuration
- Explanation: usb_choose_configuration changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000713 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_clear_halt
- Explanation: usb_clear_halt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000715 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_control_msg_recv
- Explanation: usb_control_msg_recv changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000716 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_control_msg_send
- Explanation: usb_control_msg_send changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000717 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_decode_ctrl
- Explanation: usb_decode_ctrl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000718 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_decode_interval
- Explanation: usb_decode_interval changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000721 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_deregister_device_driver
- Explanation: usb_deregister_device_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000722 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_disable_autosuspend
- Explanation: usb_disable_autosuspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000723 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_disable_lpm
- Explanation: usb_disable_lpm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000724 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_disable_ltm
- Explanation: usb_disable_ltm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000725 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_disabled
- Explanation: usb_disabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000726 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_driver_claim_interface
- Explanation: usb_driver_claim_interface changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000727 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_driver_release_interface
- Explanation: usb_driver_release_interface changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000728 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_driver_set_configuration
- Explanation: usb_driver_set_configuration changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000729 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_enable_autosuspend
- Explanation: usb_enable_autosuspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000730 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_enable_lpm
- Explanation: usb_enable_lpm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000731 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_enable_ltm
- Explanation: usb_enable_ltm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000732 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_endpoint_is_hs_isoc_double
- Explanation: usb_endpoint_is_hs_isoc_double changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000733 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_endpoint_max_periodic_payload
- Explanation: usb_endpoint_max_periodic_payload changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000734 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_ep_type_string
- Explanation: usb_ep_type_string changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000735 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_find_alt_setting
- Explanation: usb_find_alt_setting changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000737 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_find_common_endpoints_reverse
- Explanation: usb_find_common_endpoints_reverse changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000738 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_find_interface
- Explanation: usb_find_interface changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000739 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_for_each_dev
- Explanation: usb_for_each_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000740 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_free_coherent
- Explanation: usb_free_coherent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000741 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_free_noncoherent
- Explanation: usb_free_noncoherent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000742 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_free_streams
- Explanation: usb_free_streams changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000743 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_free_urb
- Explanation: usb_free_urb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000744 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_get_current_frame_number
- Explanation: usb_get_current_frame_number changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000745 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_get_descriptor
- Explanation: usb_get_descriptor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000747 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_get_from_anchor
- Explanation: usb_get_from_anchor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000749 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_get_maximum_speed
- Explanation: usb_get_maximum_speed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000750 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_get_maximum_ssp_rate
- Explanation: usb_get_maximum_ssp_rate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000751 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_get_status
- Explanation: usb_get_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000752 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_get_urb
- Explanation: usb_get_urb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000753 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_hub_claim_port
- Explanation: usb_hub_claim_port changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000754 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_hub_find_child
- Explanation: usb_hub_find_child changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000755 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_hub_release_port
- Explanation: usb_hub_release_port changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000756 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_ifnum_to_if
- Explanation: usb_ifnum_to_if changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000757 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_init_urb
- Explanation: usb_init_urb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000758 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_interrupt_msg
- Explanation: usb_interrupt_msg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000759 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_intf_get_dma_device
- Explanation: usb_intf_get_dma_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000760 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_kill_anchored_urbs
- Explanation: usb_kill_anchored_urbs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000761 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_kill_urb
- Explanation: usb_kill_urb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000762 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_lock_device_for_reset
- Explanation: usb_lock_device_for_reset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000763 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_match_id
- Explanation: usb_match_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000764 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_match_one_id
- Explanation: usb_match_one_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000765 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_pipe_type_check
- Explanation: usb_pipe_type_check changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000766 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_poison_anchored_urbs
- Explanation: usb_poison_anchored_urbs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000767 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_poison_urb
- Explanation: usb_poison_urb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000770 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_queue_reset_device
- Explanation: usb_queue_reset_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000772 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_register_device_driver
- Explanation: usb_register_device_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000774 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_register_notify
- Explanation: usb_register_notify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000775 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_reset_configuration
- Explanation: usb_reset_configuration changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000776 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_reset_device
- Explanation: usb_reset_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000777 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_reset_endpoint
- Explanation: usb_reset_endpoint changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000778 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_scuttle_anchored_urbs
- Explanation: usb_scuttle_anchored_urbs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000779 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_set_configuration
- Explanation: usb_set_configuration changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000780 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_set_interface
- Explanation: usb_set_interface changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000781 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_set_wireless_status
- Explanation: usb_set_wireless_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000782 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_sg_cancel
- Explanation: usb_sg_cancel changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000783 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_sg_init
- Explanation: usb_sg_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000784 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_sg_wait
- Explanation: usb_sg_wait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000785 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_show_dynids
- Explanation: usb_show_dynids changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000786 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_speed_string
- Explanation: usb_speed_string changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000787 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_state_string
- Explanation: usb_state_string changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000788 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_store_new_id
- Explanation: usb_store_new_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000790 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_submit_urb
- Explanation: usb_submit_urb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000791 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_unanchor_urb
- Explanation: usb_unanchor_urb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000792 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_unlink_urb
- Explanation: usb_unlink_urb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000793 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_unlocked_disable_lpm
- Explanation: usb_unlocked_disable_lpm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000794 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_unlocked_enable_lpm
- Explanation: usb_unlocked_enable_lpm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000795 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_unpoison_anchored_urbs
- Explanation: usb_unpoison_anchored_urbs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000796 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_unpoison_urb
- Explanation: usb_unpoison_urb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000797 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_unregister_notify
- Explanation: usb_unregister_notify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000798 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_urb_ep_type_check
- Explanation: usb_urb_ep_type_check changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000799 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usb_wait_anchor_empty_timeout
- Explanation: usb_wait_anchor_empty_timeout changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000800 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: use_generic_driver
- Explanation: use_generic_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000803 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vector_schedule_cleanup
- Explanation: vector_schedule_cleanup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000805 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_link
- Explanation: vfs_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut dentry'}, {'name': 'arg2', 'type': '*mut mnt_idmap'}, {'name': 'arg3', 'type': '*mut inode'}, {'name': 'arg4', 'type': '*mut dentry'}, {'name': 'arg5', 'type': '*mut *mut inode'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*mut dentry'}, {'name': 'arg2', 'type': '*mut mnt_idmap'}, {'name': 'arg3', 'type': '*mut inode'}, {'name': 'arg4', 'type': '*mut dentry'}, {'name': 'arg5', 'type': '*mut delegated_inode'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000806 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_mkdir
- Explanation: vfs_mkdir changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut mnt_idmap'}, {'name': 'arg2', 'type': '*mut inode'}, {'name': 'arg3', 'type': '*mut dentry'}, {'name': 'arg4', 'type': 'umode_t'}], 'return_type': '*mut dentry'}`
- New: `{'params': [{'name': 'arg1', 'type': '*mut mnt_idmap'}, {'name': 'arg2', 'type': '*mut inode'}, {'name': 'arg3', 'type': '*mut dentry'}, {'name': 'arg4', 'type': 'umode_t'}, {'name': 'arg5', 'type': '*mut delegated_inode'}], 'return_type': '*mut dentry'}`

### Rust Evidence

- Graph edges: `1`

## W-000807 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_mknod
- Explanation: vfs_mknod changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut mnt_idmap'}, {'name': 'arg2', 'type': '*mut inode'}, {'name': 'arg3', 'type': '*mut dentry'}, {'name': 'arg4', 'type': 'umode_t'}, {'name': 'arg5', 'type': 'dev_t'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*mut mnt_idmap'}, {'name': 'arg2', 'type': '*mut inode'}, {'name': 'arg3', 'type': '*mut dentry'}, {'name': 'arg4', 'type': 'umode_t'}, {'name': 'arg5', 'type': 'dev_t'}, {'name': 'arg6', 'type': '*mut delegated_inode'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000808 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_rmdir
- Explanation: vfs_rmdir changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut mnt_idmap'}, {'name': 'arg2', 'type': '*mut inode'}, {'name': 'arg3', 'type': '*mut dentry'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*mut mnt_idmap'}, {'name': 'arg2', 'type': '*mut inode'}, {'name': 'arg3', 'type': '*mut dentry'}, {'name': 'arg4', 'type': '*mut delegated_inode'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000809 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_symlink
- Explanation: vfs_symlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut mnt_idmap'}, {'name': 'arg2', 'type': '*mut inode'}, {'name': 'arg3', 'type': '*mut dentry'}, {'name': 'arg4', 'type': '*const ffi::c_char'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*mut mnt_idmap'}, {'name': 'arg2', 'type': '*mut inode'}, {'name': 'arg3', 'type': '*mut dentry'}, {'name': 'arg4', 'type': '*const ffi::c_char'}, {'name': 'arg5', 'type': '*mut delegated_inode'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000810 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_unlink
- Explanation: vfs_unlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut mnt_idmap'}, {'name': 'arg2', 'type': '*mut inode'}, {'name': 'arg3', 'type': '*mut dentry'}, {'name': 'arg4', 'type': '*mut *mut inode'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*mut mnt_idmap'}, {'name': 'arg2', 'type': '*mut inode'}, {'name': 'arg3', 'type': '*mut dentry'}, {'name': 'arg4', 'type': '*mut delegated_inode'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000811 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfsmount_to_propagation_flags
- Explanation: vfsmount_to_propagation_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000812 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: virt_destid_8_14
- Explanation: virt_destid_8_14 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000813 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: virtual_device_parent
- Explanation: virtual_device_parent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000814 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_interval_tree_subtree_search
- Explanation: vma_interval_tree_subtree_search changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000815 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wait_on_new_inode
- Explanation: wait_on_new_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000816 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: x86_create_pci_msi_domain
- Explanation: x86_create_pci_msi_domain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000817 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: x86_fwspec_is_hpet
- Explanation: x86_fwspec_is_hpet changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000818 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: x86_fwspec_is_ioapic
- Explanation: x86_fwspec_is_ioapic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000819 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: x86_msi_msg_get_destid
- Explanation: x86_msi_msg_get_destid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001157 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __request_percpu_irq
- Explanation: __request_percpu_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['irq', 'handler', '0', 'devname', 'percpu_dev_id'], 'return_type': 'return'}`
- New: `{'params': ['irq', 'handler', '0', 'devname', 'affinity', 'percpu_dev_id'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `1`

## W-001158 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: acpi_pci_link_allocate_irq
- Explanation: acpi_pci_link_allocate_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['acpi_handle handle', 'int index', 'int *triggering', 'int *polarity', 'char **name'], 'return_type': 'int'}`
- New: `{'params': ['acpi_handle handle', 'int index', 'int *triggering', 'int *polarity', 'char **name', 'u32 *gsi'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-001164 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bool
- Explanation: bool changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['*dl_server_has_tasks_f)(struct sched_dl_entity *'], 'return_type': 'typedef'}`
- New: `{'params': ['*filldir_t)(struct dir_context *, const char *, int, loff_t, u64, unsigned'], 'return_type': 'typedef'}`

### Rust Evidence

- Graph edges: `1`

## W-001185 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_pagemap_page_to_dpagemap
- Explanation: drm_pagemap_page_to_dpagemap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct page *page'], 'return_type': 'struct drm_pagemap *'}`
- New: `{'params': ['struct page *page'], 'return_type': 'static inline struct drm_pagemap *'}`

### Rust Evidence

- Graph edges: `1`

## W-001195 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha224_final
- Explanation: hmac_sha224_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct hmac_sha224_ctx *ctx', 'u8 out[SHA224_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['struct hmac_sha224_ctx *ctx', 'u8 out[at_least SHA224_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-001196 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha224_usingrawkey
- Explanation: hmac_sha224_usingrawkey changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const u8 *raw_key', 'size_t raw_key_len', 'const u8 *data', 'size_t data_len', 'u8 out[SHA224_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['const u8 *raw_key', 'size_t raw_key_len', 'const u8 *data', 'size_t data_len', 'u8 out[at_least SHA224_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-001198 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha256_final
- Explanation: hmac_sha256_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct hmac_sha256_ctx *ctx', 'u8 out[SHA256_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['struct hmac_sha256_ctx *ctx', 'u8 out[at_least SHA256_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-001199 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha256_usingrawkey
- Explanation: hmac_sha256_usingrawkey changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const u8 *raw_key', 'size_t raw_key_len', 'const u8 *data', 'size_t data_len', 'u8 out[SHA256_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['const u8 *raw_key', 'size_t raw_key_len', 'const u8 *data', 'size_t data_len', 'u8 out[at_least SHA256_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-001201 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha384_final
- Explanation: hmac_sha384_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct hmac_sha384_ctx *ctx', 'u8 out[SHA384_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['struct hmac_sha384_ctx *ctx', 'u8 out[at_least SHA384_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-001202 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha384_usingrawkey
- Explanation: hmac_sha384_usingrawkey changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const u8 *raw_key', 'size_t raw_key_len', 'const u8 *data', 'size_t data_len', 'u8 out[SHA384_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['const u8 *raw_key', 'size_t raw_key_len', 'const u8 *data', 'size_t data_len', 'u8 out[at_least SHA384_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-001204 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha512_final
- Explanation: hmac_sha512_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct hmac_sha512_ctx *ctx', 'u8 out[SHA512_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['struct hmac_sha512_ctx *ctx', 'u8 out[at_least SHA512_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-001205 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha512_usingrawkey
- Explanation: hmac_sha512_usingrawkey changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const u8 *raw_key', 'size_t raw_key_len', 'const u8 *data', 'size_t data_len', 'u8 out[SHA512_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['const u8 *raw_key', 'size_t raw_key_len', 'const u8 *data', 'size_t data_len', 'u8 out[at_least SHA512_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-001206 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ilookup5_nowait
- Explanation: ilookup5_nowait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct super_block *sb', 'unsigned long hashval', 'int (*test)(struct inode *, void *)', 'void *data'], 'return_type': 'extern struct inode *'}`
- New: `{'params': ['struct super_block *sb', 'unsigned long hashval', 'int (*test)(struct inode *, void *)', 'void *data', 'bool *isnew'], 'return_type': 'extern struct inode *'}`

### Rust Evidence

- Graph edges: `1`

## W-001210 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdio_driver_register
- Explanation: mdio_driver_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['&_mdio_driver'], 'return_type': 'return'}`
- New: `{'params': ['struct mdio_driver *drv'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-001211 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: notify_change
- Explanation: notify_change changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mnt_idmap *', 'struct dentry *', 'struct iattr *', 'struct inode **'], 'return_type': 'int'}`
- New: `{'params': ['struct mnt_idmap *', 'struct dentry *', 'struct iattr *', 'struct delegated_inode *'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-001212 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_rebar_bytes_to_size
- Explanation: pci_rebar_bytes_to_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u64 bytes'], 'return_type': 'static inline int'}`
- New: `{'params': ['u64 bytes'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-001213 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_rebar_get_possible_sizes
- Explanation: pci_rebar_get_possible_sizes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct pci_dev *pdev', 'int bar'], 'return_type': 'u32'}`
- New: `{'params': ['struct pci_dev *pdev', 'int bar'], 'return_type': 'u64'}`

### Rust Evidence

- Graph edges: `1`

## W-001214 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_resize_resource
- Explanation: pci_resize_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct pci_dev *dev', 'int i', 'int size'], 'return_type': 'int __must_check'}`
- New: `{'params': ['struct pci_dev *dev', 'int i', 'int size', 'int exclude_bars'], 'return_type': 'int __must_check'}`

### Rust Evidence

- Graph edges: `1`

## W-001217 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: remap_pfn_range
- Explanation: remap_pfn_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['vma', 'addr', 'pfn', 'size', 'pgprot_decrypted(prot)'], 'return_type': 'return'}`
- New: `{'params': ['vma', 'addr', 'pfn', 'size', 'prot'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `1`

## W-001218 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: request_percpu_nmi
- Explanation: request_percpu_nmi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned int irq', 'irq_handler_t handler', 'const char *devname', 'void __percpu *dev'], 'return_type': 'extern int __must_check'}`
- New: `{'params': ['unsigned int irq', 'irq_handler_t handler', 'const char *name', 'const struct cpumask *affinity', 'void __percpu *dev_id'], 'return_type': 'extern int __must_check'}`

### Rust Evidence

- Graph edges: `1`

## W-001225 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sha224_final
- Explanation: sha224_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct sha224_ctx *ctx', 'u8 out[SHA224_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['struct sha224_ctx *ctx', 'u8 out[at_least SHA224_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-001227 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sha256_final
- Explanation: sha256_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct sha256_ctx *ctx', 'u8 out[SHA256_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['struct sha256_ctx *ctx', 'u8 out[at_least SHA256_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-001230 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sha384_final
- Explanation: sha384_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct sha384_ctx *ctx', 'u8 out[SHA384_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['struct sha384_ctx *ctx', 'u8 out[at_least SHA384_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-001232 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sha512_final
- Explanation: sha512_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct sha512_ctx *ctx', 'u8 out[SHA512_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['struct sha512_ctx *ctx', 'u8 out[at_least SHA512_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-001237 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: truncate_inode_pages_final
- Explanation: truncate_inode_pages_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct address_space *'], 'return_type': 'extern void'}`
- New: `{'params': ['struct address_space *mapping'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-001238 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: truncate_inode_pages_range
- Explanation: truncate_inode_pages_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct address_space *', 'loff_t lstart', 'loff_t lend'], 'return_type': 'extern void'}`
- New: `{'params': ['struct address_space *mapping', 'loff_t lstart', 'uoff_t lend'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-001241 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unmap_vmas
- Explanation: unmap_vmas changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mmu_gather *tlb', 'struct ma_state *mas', 'struct vm_area_struct *start_vma', 'unsigned long start', 'unsigned long end', 'unsigned long tree_end', 'bool mm_wr_locked'], 'return_type': 'void'}`
- New: `{'params': ['struct mmu_gather *tlb', 'struct ma_state *mas', 'struct vm_area_struct *start_vma', 'unsigned long start', 'unsigned long end', 'unsigned long tree_end'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-001243 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_link
- Explanation: vfs_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct dentry *', 'struct mnt_idmap *', 'struct inode *', 'struct dentry *', 'struct inode **'], 'return_type': 'int'}`
- New: `{'params': ['struct dentry *', 'struct mnt_idmap *', 'struct inode *', 'struct dentry *', 'struct delegated_inode *'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-001244 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_mkdir
- Explanation: vfs_mkdir changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mnt_idmap *', 'struct inode *', 'struct dentry *', 'umode_t'], 'return_type': 'struct dentry *'}`
- New: `{'params': ['struct mnt_idmap *', 'struct inode *', 'struct dentry *', 'umode_t', 'struct delegated_inode *'], 'return_type': 'struct dentry *'}`

### Rust Evidence

- Graph edges: `1`

## W-001245 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_mknod
- Explanation: vfs_mknod changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['idmap', 'dir', 'dentry', 'S_IFCHR | WHITEOUT_MODE', 'WHITEOUT_DEV'], 'return_type': 'return'}`
- New: `{'params': ['idmap', 'dir', 'dentry', 'S_IFCHR | WHITEOUT_MODE', 'WHITEOUT_DEV', 'NULL'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `1`

## W-001246 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_rmdir
- Explanation: vfs_rmdir changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mnt_idmap *', 'struct inode *', 'struct dentry *'], 'return_type': 'int'}`
- New: `{'params': ['struct mnt_idmap *', 'struct inode *', 'struct dentry *', 'struct delegated_inode *'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-001247 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_symlink
- Explanation: vfs_symlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mnt_idmap *', 'struct inode *', 'struct dentry *', 'const char *'], 'return_type': 'int'}`
- New: `{'params': ['struct mnt_idmap *', 'struct inode *', 'struct dentry *', 'const char *', 'struct delegated_inode *'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-001248 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfs_unlink
- Explanation: vfs_unlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mnt_idmap *', 'struct inode *', 'struct dentry *', 'struct inode **'], 'return_type': 'int'}`
- New: `{'params': ['struct mnt_idmap *', 'struct inode *', 'struct dentry *', 'struct delegated_inode *'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000838 FieldDrift

- Risk: High
- Score: 10.6
- Symbol: drm_mode_config
- Explanation: drm_mode_config changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mutex', 'type': 'mutex'}, {'name': 'connection_mutex', 'type': 'drm_modeset_lock'}, {'name': 'acquire_ctx', 'type': '*mut drm_modeset_acquire_ctx'}, {'name': 'idr_mutex', 'type': 'mutex'}, {'name': 'object_idr', 'type': 'idr'}, {'name': 'tile_idr', 'type': 'idr'}, {'name': 'fb_lock', 'type': 'mutex'}, {'name': 'num_fb', 'type': 'ffi::c_int'}, {'name': 'fb_list', 'type': 'list_head'}, {'name': 'connector_list_lock', 'type': 'spinlock_t'}, {'name': 'num_connector', 'type': 'ffi::c_int'}, {'name': 'connector_ida', 'type': 'ida'}, {'name': 'connector_list', 'type': 'list_head'}, {'name': 'connector_free_list', 'type': 'llist_head'}, {'name': 'connector_free_work', 'type': 'work_struct'}, {'name': 'num_encoder', 'type': 'ffi::c_int'}, {'name': 'encoder_list', 'type': 'list_head'}, {'name': 'num_total_plane', 'type': 'ffi::c_int'}, {'name': 'plane_list', 'type': 'list_head'}, {'name': 'panic_lock', 'type': 'raw_spinlock'}, {'name': 'num_crtc', 'type': 'ffi::c_int'}, {'name': 'crtc_list', 'type': 'list_head'}, {'name': 'property_list', 'type': 'list_head'}, {'name': 'privobj_list', 'type': 'list_head'}, {'name': 'min_width', 'type': 'ffi::c_uint'}, {'name': 'min_height', 'type': 'ffi::c_uint'}, {'name': 'max_width', 'type': 'ffi::c_uint'}, {'name': 'max_height', 'type': 'ffi::c_uint'}, {'name': 'funcs', 'type': '*const drm_mode_config_funcs'}, {'name': 'poll_enabled', 'type': 'bool_'}, {'name': 'poll_running', 'type': 'bool_'}, {'name': 'delayed_event', 'type': 'bool_'}, {'name': 'output_poll_work', 'type': 'delayed_work'}, {'name': 'blob_lock', 'type': 'mutex'}, {'name': 'property_blob_list', 'type': 'list_head'}, {'name': 'edid_property', 'type': '*mut drm_property'}, {'name': 'dpms_property', 'type': '*mut drm_property'}, {'name': 'path_property', 'type': '*mut drm_property'}, {'name': 'tile_property', 'type': '*mut drm_property'}, {'name': 'link_status_property', 'type': '*mut drm_property'}, {'name': 'plane_type_property', 'type': '*mut drm_property'}, {'name': 'prop_src_x', 'type': '*mut drm_property'}, {'name': 'prop_src_y', 'type': '*mut drm_property'}, {'name': 'prop_src_w', 'type': '*mut drm_property'}, {'name': 'prop_src_h', 'type': '*mut drm_property'}, {'name': 'prop_crtc_x', 'type': '*mut drm_property'}, {'name': 'prop_crtc_y', 'type': '*mut drm_property'}, {'name': 'prop_crtc_w', 'type': '*mut drm_property'}, {'name': 'prop_crtc_h', 'type': '*mut drm_property'}, {'name': 'prop_fb_id', 'type': '*mut drm_property'}, {'name': 'prop_in_fence_fd', 'type': '*mut drm_property'}, {'name': 'prop_out_fence_ptr', 'type': '*mut drm_property'}, {'name': 'prop_crtc_id', 'type': '*mut drm_property'}, {'name': 'prop_fb_damage_clips', 'type': '*mut drm_property'}, {'name': 'prop_active', 'type': '*mut drm_property'}, {'name': 'prop_mode_id', 'type': '*mut drm_property'}, {'name': 'prop_vrr_enabled', 'type': '*mut drm_property'}, {'name': 'dvi_i_subconnector_property', 'type': '*mut drm_property'}, {'name': 'dvi_i_select_subconnector_property', 'type': '*mut drm_property'}, {'name': 'dp_subconnector_property', 'type': '*mut drm_property'}, {'name': 'tv_subconnector_property', 'type': '*mut drm_property'}, {'name': 'tv_select_subconnector_property', 'type': '*mut drm_property'}, {'name': 'legacy_tv_mode_property', 'type': '*mut drm_property'}, {'name': 'tv_mode_property', 'type': '*mut drm_property'}, {'name': 'tv_left_margin_property', 'type': '*mut drm_property'}, {'name': 'tv_right_margin_property', 'type': '*mut drm_property'}, {'name': 'tv_top_margin_property', 'type': '*mut drm_property'}, {'name': 'tv_bottom_margin_property', 'type': '*mut drm_property'}, {'name': 'tv_brightness_property', 'type': '*mut drm_property'}, {'name': 'tv_contrast_property', 'type': '*mut drm_property'}, {'name': 'tv_flicker_reduction_property', 'type': '*mut drm_property'}, {'name': 'tv_overscan_property', 'type': '*mut drm_property'}, {'name': 'tv_saturation_property', 'type': '*mut drm_property'}, {'name': 'tv_hue_property', 'type': '*mut drm_property'}, {'name': 'scaling_mode_property', 'type': '*mut drm_property'}, {'name': 'aspect_ratio_property', 'type': '*mut drm_property'}, {'name': 'content_type_property', 'type': '*mut drm_property'}, {'name': 'degamma_lut_property', 'type': '*mut drm_property'}, {'name': 'degamma_lut_size_property', 'type': '*mut drm_property'}, {'name': 'ctm_property', 'type': '*mut drm_property'}, {'name': 'gamma_lut_property', 'type': '*mut drm_property'}, {'name': 'gamma_lut_size_property', 'type': '*mut drm_property'}, {'name': 'suggested_x_property', 'type': '*mut drm_property'}, {'name': 'suggested_y_property', 'type': '*mut drm_property'}, {'name': 'non_desktop_property', 'type': '*mut drm_property'}, {'name': 'panel_orientation_property', 'type': '*mut drm_property'}, {'name': 'writeback_fb_id_property', 'type': '*mut drm_property'}, {'name': 'writeback_pixel_formats_property', 'type': '*mut drm_property'}, {'name': 'writeback_out_fence_ptr_property', 'type': '*mut drm_property'}, {'name': 'hdr_output_metadata_property', 'type': '*mut drm_property'}, {'name': 'content_protection_property', 'type': '*mut drm_property'}, {'name': 'hdcp_content_type_property', 'type': '*mut drm_property'}, {'name': 'preferred_depth', 'type': 'u32'}, {'name': 'prefer_shadow', 'type': 'u32'}, {'name': 'quirk_addfb_prefer_xbgr_30bpp', 'type': 'bool_'}, {'name': 'quirk_addfb_prefer_host_byte_order', 'type': 'bool_'}, {'name': 'async_page_flip', 'type': 'bool_'}, {'name': 'fb_modifiers_not_supported', 'type': 'bool_'}, {'name': 'normalize_zpos', 'type': 'bool_'}, {'name': 'modifiers_property', 'type': '*mut drm_property'}, {'name': 'async_modifiers_property', 'type': '*mut drm_property'}, {'name': 'size_hints_property', 'type': '*mut drm_property'}, {'name': 'cursor_width', 'type': 'u32'}, {'name': 'cursor_height', 'type': 'u32'}, {'name': 'suspend_state', 'type': '*mut drm_atomic_state'}, {'name': 'helper_private', 'type': '*mut drm_mode_config_helper_funcs'}]`
- New: `[{'name': 'mutex', 'type': 'mutex'}, {'name': 'connection_mutex', 'type': 'drm_modeset_lock'}, {'name': 'acquire_ctx', 'type': '*mut drm_modeset_acquire_ctx'}, {'name': 'idr_mutex', 'type': 'mutex'}, {'name': 'object_idr', 'type': 'idr'}, {'name': 'tile_idr', 'type': 'idr'}, {'name': 'fb_lock', 'type': 'mutex'}, {'name': 'num_fb', 'type': 'ffi::c_int'}, {'name': 'fb_list', 'type': 'list_head'}, {'name': 'connector_list_lock', 'type': 'spinlock_t'}, {'name': 'num_connector', 'type': 'ffi::c_int'}, {'name': 'connector_ida', 'type': 'ida'}, {'name': 'connector_list', 'type': 'list_head'}, {'name': 'connector_free_list', 'type': 'llist_head'}, {'name': 'connector_free_work', 'type': 'work_struct'}, {'name': 'num_encoder', 'type': 'ffi::c_int'}, {'name': 'encoder_list', 'type': 'list_head'}, {'name': 'num_total_plane', 'type': 'ffi::c_int'}, {'name': 'plane_list', 'type': 'list_head'}, {'name': 'panic_lock', 'type': 'raw_spinlock'}, {'name': 'num_colorop', 'type': 'ffi::c_int'}, {'name': 'colorop_list', 'type': 'list_head'}, {'name': 'num_crtc', 'type': 'ffi::c_int'}, {'name': 'crtc_list', 'type': 'list_head'}, {'name': 'property_list', 'type': 'list_head'}, {'name': 'privobj_list', 'type': 'list_head'}, {'name': 'min_width', 'type': 'ffi::c_uint'}, {'name': 'min_height', 'type': 'ffi::c_uint'}, {'name': 'max_width', 'type': 'ffi::c_uint'}, {'name': 'max_height', 'type': 'ffi::c_uint'}, {'name': 'funcs', 'type': '*const drm_mode_config_funcs'}, {'name': 'poll_enabled', 'type': 'bool_'}, {'name': 'poll_running', 'type': 'bool_'}, {'name': 'delayed_event', 'type': 'bool_'}, {'name': 'output_poll_work', 'type': 'delayed_work'}, {'name': 'blob_lock', 'type': 'mutex'}, {'name': 'property_blob_list', 'type': 'list_head'}, {'name': 'edid_property', 'type': '*mut drm_property'}, {'name': 'dpms_property', 'type': '*mut drm_property'}, {'name': 'path_property', 'type': '*mut drm_property'}, {'name': 'tile_property', 'type': '*mut drm_property'}, {'name': 'link_status_property', 'type': '*mut drm_property'}, {'name': 'plane_type_property', 'type': '*mut drm_property'}, {'name': 'prop_src_x', 'type': '*mut drm_property'}, {'name': 'prop_src_y', 'type': '*mut drm_property'}, {'name': 'prop_src_w', 'type': '*mut drm_property'}, {'name': 'prop_src_h', 'type': '*mut drm_property'}, {'name': 'prop_crtc_x', 'type': '*mut drm_property'}, {'name': 'prop_crtc_y', 'type': '*mut drm_property'}, {'name': 'prop_crtc_w', 'type': '*mut drm_property'}, {'name': 'prop_crtc_h', 'type': '*mut drm_property'}, {'name': 'prop_fb_id', 'type': '*mut drm_property'}, {'name': 'prop_in_fence_fd', 'type': '*mut drm_property'}, {'name': 'prop_out_fence_ptr', 'type': '*mut drm_property'}, {'name': 'prop_crtc_id', 'type': '*mut drm_property'}, {'name': 'prop_fb_damage_clips', 'type': '*mut drm_property'}, {'name': 'prop_active', 'type': '*mut drm_property'}, {'name': 'prop_mode_id', 'type': '*mut drm_property'}, {'name': 'prop_vrr_enabled', 'type': '*mut drm_property'}, {'name': 'dvi_i_subconnector_property', 'type': '*mut drm_property'}, {'name': 'dvi_i_select_subconnector_property', 'type': '*mut drm_property'}, {'name': 'dp_subconnector_property', 'type': '*mut drm_property'}, {'name': 'tv_subconnector_property', 'type': '*mut drm_property'}, {'name': 'tv_select_subconnector_property', 'type': '*mut drm_property'}, {'name': 'legacy_tv_mode_property', 'type': '*mut drm_property'}, {'name': 'tv_mode_property', 'type': '*mut drm_property'}, {'name': 'tv_left_margin_property', 'type': '*mut drm_property'}, {'name': 'tv_right_margin_property', 'type': '*mut drm_property'}, {'name': 'tv_top_margin_property', 'type': '*mut drm_property'}, {'name': 'tv_bottom_margin_property', 'type': '*mut drm_property'}, {'name': 'tv_brightness_property', 'type': '*mut drm_property'}, {'name': 'tv_contrast_property', 'type': '*mut drm_property'}, {'name': 'tv_flicker_reduction_property', 'type': '*mut drm_property'}, {'name': 'tv_overscan_property', 'type': '*mut drm_property'}, {'name': 'tv_saturation_property', 'type': '*mut drm_property'}, {'name': 'tv_hue_property', 'type': '*mut drm_property'}, {'name': 'scaling_mode_property', 'type': '*mut drm_property'}, {'name': 'aspect_ratio_property', 'type': '*mut drm_property'}, {'name': 'content_type_property', 'type': '*mut drm_property'}, {'name': 'degamma_lut_property', 'type': '*mut drm_property'}, {'name': 'degamma_lut_size_property', 'type': '*mut drm_property'}, {'name': 'ctm_property', 'type': '*mut drm_property'}, {'name': 'gamma_lut_property', 'type': '*mut drm_property'}, {'name': 'gamma_lut_size_property', 'type': '*mut drm_property'}, {'name': 'suggested_x_property', 'type': '*mut drm_property'}, {'name': 'suggested_y_property', 'type': '*mut drm_property'}, {'name': 'non_desktop_property', 'type': '*mut drm_property'}, {'name': 'panel_orientation_property', 'type': '*mut drm_property'}, {'name': 'writeback_fb_id_property', 'type': '*mut drm_property'}, {'name': 'writeback_pixel_formats_property', 'type': '*mut drm_property'}, {'name': 'writeback_out_fence_ptr_property', 'type': '*mut drm_property'}, {'name': 'hdr_output_metadata_property', 'type': '*mut drm_property'}, {'name': 'content_protection_property', 'type': '*mut drm_property'}, {'name': 'hdcp_content_type_property', 'type': '*mut drm_property'}, {'name': 'preferred_depth', 'type': 'u32'}, {'name': 'prefer_shadow', 'type': 'u32'}, {'name': 'quirk_addfb_prefer_xbgr_30bpp', 'type': 'bool_'}, {'name': 'quirk_addfb_prefer_host_byte_order', 'type': 'bool_'}, {'name': 'async_page_flip', 'type': 'bool_'}, {'name': 'fb_modifiers_not_supported', 'type': 'bool_'}, {'name': 'normalize_zpos', 'type': 'bool_'}, {'name': 'modifiers_property', 'type': '*mut drm_property'}, {'name': 'async_modifiers_property', 'type': '*mut drm_property'}, {'name': 'size_hints_property', 'type': '*mut drm_property'}, {'name': 'cursor_width', 'type': 'u32'}, {'name': 'cursor_height', 'type': 'u32'}, {'name': 'suspend_state', 'type': '*mut drm_atomic_state'}, {'name': 'helper_private', 'type': '*mut drm_mode_config_helper_funcs'}]`

### Rust Evidence

- Graph edges: `5`

## W-000826 FieldDrift

- Risk: High
- Score: 10.4
- Symbol: cdev
- Explanation: cdev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[{'name': 'kobj', 'type': 'kobject'}, {'name': 'owner', 'type': '*mut module'}, {'name': 'ops', 'type': '*const file_operations'}, {'name': 'list', 'type': 'list_head'}, {'name': 'dev', 'type': 'dev_t'}, {'name': 'count', 'type': 'ffi::c_uint'}]`

### Rust Evidence

- Graph edges: `9`

## W-000861 FieldDrift

- Risk: High
- Score: 10.2
- Symbol: rseq
- Explanation: rseq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'cpu_id_start', 'type': '__u32'}, {'name': 'cpu_id', 'type': '__u32'}, {'name': 'rseq_cs', 'type': '__u64'}, {'name': 'flags', 'type': '__u32'}, {'name': 'node_id', 'type': '__u32'}, {'name': 'mm_cid', 'type': '__u32'}, {'name': 'end', 'type': '__IncompleteArrayField<ffi::c_char>'}]`
- New: `[]`

### Rust Evidence

- Graph edges: `8`

## W-000832 FieldDrift

- Risk: High
- Score: 10.0
- Symbol: device_driver
- Explanation: device_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'bus', 'type': '*const bus_type'}, {'name': 'owner', 'type': '*mut module'}, {'name': 'mod_name', 'type': '*const ffi::c_char'}, {'name': 'suppress_bind_attrs', 'type': 'bool_'}, {'name': 'probe_type', 'type': 'probe_type'}, {'name': 'of_match_table', 'type': '*const of_device_id'}, {'name': 'acpi_match_table', 'type': '*const acpi_device_id'}, {'name': 'probe', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'sync_state', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'remove', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'shutdown', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'suspend', 'type': '::core::option::Option<'}, {'name': 'resume', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'groups', 'type': '*mut *const attribute_group'}, {'name': 'dev_groups', 'type': '*mut *const attribute_group'}, {'name': 'pm', 'type': '*const dev_pm_ops'}, {'name': 'coredump', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'p', 'type': '*mut driver_private'}]`
- New: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'bus', 'type': '*const bus_type'}, {'name': 'owner', 'type': '*mut module'}, {'name': 'mod_name', 'type': '*const ffi::c_char'}, {'name': 'suppress_bind_attrs', 'type': 'bool_'}, {'name': 'probe_type', 'type': 'probe_type'}, {'name': 'of_match_table', 'type': '*const of_device_id'}, {'name': 'acpi_match_table', 'type': '*const acpi_device_id'}, {'name': 'probe', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'sync_state', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'remove', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'shutdown', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'suspend', 'type': '::core::option::Option<'}, {'name': 'resume', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device) -> ffi::c_int>'}, {'name': 'groups', 'type': '*mut *const attribute_group'}, {'name': 'dev_groups', 'type': '*mut *const attribute_group'}, {'name': 'pm', 'type': '*const dev_pm_ops'}, {'name': 'coredump', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'p', 'type': '*mut driver_private'}, {'name': 'p_cb', 'type': 'device_driver__bindgen_ty_1'}]`

### Rust Evidence

- Graph edges: `7`

## W-000863 FieldDrift

- Risk: High
- Score: 10.0
- Symbol: sockaddr
- Explanation: sockaddr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'sa_family', 'type': 'sa_family_t'}, {'name': '__bindgen_anon_1', 'type': 'sockaddr__bindgen_ty_1'}]`
- New: `[{'name': 'sa_family', 'type': 'sa_family_t'}, {'name': 'sa_data', 'type': '[ffi::c_char; 14usize]'}]`

### Rust Evidence

- Graph edges: `7`

## W-000862 FieldDrift

- Risk: Medium
- Score: 9.8
- Symbol: sched_domain
- Explanation: sched_domain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'parent', 'type': '*mut sched_domain'}, {'name': 'child', 'type': '*mut sched_domain'}, {'name': 'groups', 'type': '*mut sched_group'}, {'name': 'min_interval', 'type': 'ffi::c_ulong'}, {'name': 'max_interval', 'type': 'ffi::c_ulong'}, {'name': 'busy_factor', 'type': 'ffi::c_uint'}, {'name': 'imbalance_pct', 'type': 'ffi::c_uint'}, {'name': 'cache_nice_tries', 'type': 'ffi::c_uint'}, {'name': 'imb_numa_nr', 'type': 'ffi::c_uint'}, {'name': 'nohz_idle', 'type': 'ffi::c_int'}, {'name': 'flags', 'type': 'ffi::c_int'}, {'name': 'level', 'type': 'ffi::c_int'}, {'name': 'last_balance', 'type': 'ffi::c_ulong'}, {'name': 'balance_interval', 'type': 'ffi::c_uint'}, {'name': 'nr_balance_failed', 'type': 'ffi::c_uint'}, {'name': 'max_newidle_lb_cost', 'type': 'u64_'}, {'name': 'last_decay_max_lb_cost', 'type': 'ffi::c_ulong'}, {'name': 'lb_count', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_failed', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_balanced', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_imbalance_load', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_imbalance_util', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_imbalance_task', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_imbalance_misfit', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_gained', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_hot_gained', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_nobusyg', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_nobusyq', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'alb_count', 'type': 'ffi::c_uint'}, {'name': 'alb_failed', 'type': 'ffi::c_uint'}, {'name': 'alb_pushed', 'type': 'ffi::c_uint'}, {'name': 'sbe_count', 'type': 'ffi::c_uint'}, {'name': 'sbe_balanced', 'type': 'ffi::c_uint'}, {'name': 'sbe_pushed', 'type': 'ffi::c_uint'}, {'name': 'sbf_count', 'type': 'ffi::c_uint'}, {'name': 'sbf_balanced', 'type': 'ffi::c_uint'}, {'name': 'sbf_pushed', 'type': 'ffi::c_uint'}, {'name': 'ttwu_wake_remote', 'type': 'ffi::c_uint'}, {'name': 'ttwu_move_affine', 'type': 'ffi::c_uint'}, {'name': 'ttwu_move_balance', 'type': 'ffi::c_uint'}, {'name': 'name', 'type': '*mut ffi::c_char'}, {'name': '__bindgen_anon_1', 'type': 'sched_domain__bindgen_ty_1'}, {'name': 'shared', 'type': '*mut sched_domain_shared'}, {'name': 'span_weight', 'type': 'ffi::c_uint'}, {'name': 'span', 'type': '__IncompleteArrayField<ffi::c_ulong>'}]`
- New: `[{'name': 'parent', 'type': '*mut sched_domain'}, {'name': 'child', 'type': '*mut sched_domain'}, {'name': 'groups', 'type': '*mut sched_group'}, {'name': 'min_interval', 'type': 'ffi::c_ulong'}, {'name': 'max_interval', 'type': 'ffi::c_ulong'}, {'name': 'busy_factor', 'type': 'ffi::c_uint'}, {'name': 'imbalance_pct', 'type': 'ffi::c_uint'}, {'name': 'cache_nice_tries', 'type': 'ffi::c_uint'}, {'name': 'imb_numa_nr', 'type': 'ffi::c_uint'}, {'name': 'nohz_idle', 'type': 'ffi::c_int'}, {'name': 'flags', 'type': 'ffi::c_int'}, {'name': 'level', 'type': 'ffi::c_int'}, {'name': 'last_balance', 'type': 'ffi::c_ulong'}, {'name': 'balance_interval', 'type': 'ffi::c_uint'}, {'name': 'nr_balance_failed', 'type': 'ffi::c_uint'}, {'name': 'newidle_call', 'type': 'ffi::c_uint'}, {'name': 'newidle_success', 'type': 'ffi::c_uint'}, {'name': 'newidle_ratio', 'type': 'ffi::c_uint'}, {'name': 'max_newidle_lb_cost', 'type': 'u64_'}, {'name': 'last_decay_max_lb_cost', 'type': 'ffi::c_ulong'}, {'name': 'lb_count', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_failed', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_balanced', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_imbalance_load', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_imbalance_util', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_imbalance_task', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_imbalance_misfit', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_gained', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_hot_gained', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_nobusyg', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'lb_nobusyq', 'type': '[ffi::c_uint; 3usize]'}, {'name': 'alb_count', 'type': 'ffi::c_uint'}, {'name': 'alb_failed', 'type': 'ffi::c_uint'}, {'name': 'alb_pushed', 'type': 'ffi::c_uint'}, {'name': 'sbe_count', 'type': 'ffi::c_uint'}, {'name': 'sbe_balanced', 'type': 'ffi::c_uint'}, {'name': 'sbe_pushed', 'type': 'ffi::c_uint'}, {'name': 'sbf_count', 'type': 'ffi::c_uint'}, {'name': 'sbf_balanced', 'type': 'ffi::c_uint'}, {'name': 'sbf_pushed', 'type': 'ffi::c_uint'}, {'name': 'ttwu_wake_remote', 'type': 'ffi::c_uint'}, {'name': 'ttwu_move_affine', 'type': 'ffi::c_uint'}, {'name': 'ttwu_move_balance', 'type': 'ffi::c_uint'}, {'name': 'name', 'type': '*mut ffi::c_char'}, {'name': '__bindgen_anon_1', 'type': 'sched_domain__bindgen_ty_1'}, {'name': 'shared', 'type': '*mut sched_domain_shared'}, {'name': 'span_weight', 'type': 'ffi::c_uint'}, {'name': 'span', 'type': '__IncompleteArrayField<ffi::c_ulong>'}]`

### Rust Evidence

- Graph edges: `6`

## W-000009 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __compat_vma_mmap_prepare
- Explanation: __compat_vma_mmap_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000011 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __drm_dev_dbg
- Explanation: __drm_dev_dbg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000012 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __drm_err
- Explanation: __drm_err changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000013 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __drm_printfn_coredump
- Explanation: __drm_printfn_coredump changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000014 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __drm_printfn_dbg
- Explanation: __drm_printfn_dbg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000015 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __drm_printfn_err
- Explanation: __drm_printfn_err changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000016 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __drm_printfn_info
- Explanation: __drm_printfn_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000017 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __drm_printfn_line
- Explanation: __drm_printfn_line changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000018 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __drm_printfn_seq_file
- Explanation: __drm_printfn_seq_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000019 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __drm_puts_coredump
- Explanation: __drm_puts_coredump changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000020 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __drm_puts_seq_file
- Explanation: __drm_puts_seq_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000021 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __filemap_fdatawrite_range
- Explanation: __filemap_fdatawrite_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000050 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __sys_getpeername
- Explanation: __sys_getpeername changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000055 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: acpi_get_lps0_constraint
- Explanation: acpi_get_lps0_constraint changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000056 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: acpi_get_next_subnode
- Explanation: acpi_get_next_subnode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000066 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: available_idle_cpu
- Explanation: available_idle_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000107 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: cgroup_exit
- Explanation: cgroup_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000109 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: cgroup_freezing
- Explanation: cgroup_freezing changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000110 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: cgroup_release
- Explanation: cgroup_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000118 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: compat_vma_mmap_prepare
- Explanation: compat_vma_mmap_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000124 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: current_umask
- Explanation: current_umask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000157 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: devm_free_percpu
- Explanation: devm_free_percpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000184 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: do_proc_douintvec
- Explanation: do_proc_douintvec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000186 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: do_set_cpus_allowed
- Explanation: do_set_cpus_allowed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000193 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_dev_printk
- Explanation: drm_dev_printk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000194 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_print_bits
- Explanation: drm_print_bits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000195 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_print_hex_dump
- Explanation: drm_print_hex_dump changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000196 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_print_regset32
- Explanation: drm_print_regset32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000197 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_printf
- Explanation: drm_printf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000198 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_puts
- Explanation: drm_puts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000204 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: exit_task_namespaces
- Explanation: exit_task_namespaces changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000208 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: filemap_fdatawrite_range_kick
- Explanation: filemap_fdatawrite_range_kick changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000209 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: filemap_fdatawrite_wbc
- Explanation: filemap_fdatawrite_wbc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000220 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: free_nsproxy
- Explanation: free_nsproxy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000277 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: has_managed_dma
- Explanation: has_managed_dma changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000343 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: inode_add_lru
- Explanation: inode_add_lru changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000489 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: kill_litter_super
- Explanation: kill_litter_super changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000508 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mempool_kvfree
- Explanation: mempool_kvfree changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000509 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mempool_kvmalloc
- Explanation: mempool_kvmalloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000565 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_find_first
- Explanation: phy_find_first changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000636 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: register_one_node
- Explanation: register_one_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000638 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: remap_pfn_range_notrack
- Explanation: remap_pfn_range_notrack changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000650 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sched_mm_cid_exit_signals
- Explanation: sched_mm_cid_exit_signals changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000680 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: unregister_one_node
- Explanation: unregister_one_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001154 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: DIV_ROUND_CLOSEST_ULL
- Explanation: DIV_ROUND_CLOSEST_ULL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['mul_u32_u32(user_input, (1 << bit_precision) - 1)', '(1 << 16) - 1'], 'return_type': 'return'}`
- New: `{'params': ['(u64)state->duty_cycle * scale', 'state->period'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001155 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __blake2b_init
- Explanation: __blake2b_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct blake2b_state *state', 'size_t outlen', 'size_t keylen'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct blake2b_ctx *ctx', 'size_t outlen', 'const void *key', 'size_t keylen'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-001156 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __blake2s_init
- Explanation: __blake2s_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct blake2s_state *state', 'size_t outlen', 'const void *key', 'size_t keylen'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct blake2s_ctx *ctx', 'size_t outlen', 'const void *key', 'size_t keylen'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-001159 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: blake2s
- Explanation: blake2s changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u8 *out', 'const u8 *in', 'const u8 *key', 'const size_t outlen', 'const size_t inlen', 'const size_t keylen'], 'return_type': 'static inline void'}`
- New: `{'params': ['const u8 *key', 'size_t keylen', 'const u8 *in', 'size_t inlen', 'u8 *out', 'size_t outlen'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-001160 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: blake2s_final
- Explanation: blake2s_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct blake2s_state *state', 'u8 *out'], 'return_type': 'void'}`
- New: `{'params': ['struct blake2s_ctx *ctx', 'u8 *out'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001161 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: blake2s_init
- Explanation: blake2s_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct blake2s_state *state', 'const size_t outlen'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct blake2s_ctx *ctx', 'size_t outlen'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-001162 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: blake2s_init_key
- Explanation: blake2s_init_key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct blake2s_state *state', 'const size_t outlen', 'const void *key', 'const size_t keylen'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct blake2s_ctx *ctx', 'size_t outlen', 'const void *key', 'size_t keylen'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-001163 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: blake2s_update
- Explanation: blake2s_update changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct blake2s_state *state', 'const u8 *in', 'size_t inlen'], 'return_type': 'void'}`
- New: `{'params': ['struct blake2s_ctx *ctx', 'const u8 *in', 'size_t inlen'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001165 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: chacha20_block
- Explanation: chacha20_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct chacha_state *state', 'u8 out[CHACHA_BLOCK_SIZE]'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct chacha_state *state', 'u8 out[at_least CHACHA_BLOCK_SIZE]'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-001166 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: chacha20poly1305_decrypt
- Explanation: chacha20poly1305_decrypt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u8 *dst', 'const u8 *src', 'const size_t src_len', 'const u8 *ad', 'const size_t ad_len', 'const u64 nonce', 'const u8 key[CHACHA20POLY1305_KEY_SIZE]'], 'return_type': 'bool __must_check'}`
- New: `{'params': ['u8 *dst', 'const u8 *src', 'const size_t src_len', 'const u8 *ad', 'const size_t ad_len', 'const u64 nonce', 'const u8 key[at_least CHACHA20POLY1305_KEY_SIZE]'], 'return_type': 'bool __must_check'}`

### Rust Evidence

- Graph edges: `0`

## W-001167 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: chacha20poly1305_decrypt_sg_inplace
- Explanation: chacha20poly1305_decrypt_sg_inplace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct scatterlist *src', 'size_t src_len', 'const u8 *ad', 'const size_t ad_len', 'const u64 nonce', 'const u8 key[CHACHA20POLY1305_KEY_SIZE]'], 'return_type': 'bool'}`
- New: `{'params': ['struct scatterlist *src', 'size_t src_len', 'const u8 *ad', 'const size_t ad_len', 'const u64 nonce', 'const u8 key[at_least CHACHA20POLY1305_KEY_SIZE]'], 'return_type': 'bool'}`

### Rust Evidence

- Graph edges: `0`

## W-001168 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: chacha20poly1305_encrypt
- Explanation: chacha20poly1305_encrypt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u8 *dst', 'const u8 *src', 'const size_t src_len', 'const u8 *ad', 'const size_t ad_len', 'const u64 nonce', 'const u8 key[CHACHA20POLY1305_KEY_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['u8 *dst', 'const u8 *src', 'const size_t src_len', 'const u8 *ad', 'const size_t ad_len', 'const u64 nonce', 'const u8 key[at_least CHACHA20POLY1305_KEY_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001169 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: chacha20poly1305_encrypt_sg_inplace
- Explanation: chacha20poly1305_encrypt_sg_inplace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct scatterlist *src', 'size_t src_len', 'const u8 *ad', 'const size_t ad_len', 'const u64 nonce', 'const u8 key[CHACHA20POLY1305_KEY_SIZE]'], 'return_type': 'bool'}`
- New: `{'params': ['struct scatterlist *src', 'size_t src_len', 'const u8 *ad', 'const size_t ad_len', 'const u64 nonce', 'const u8 key[at_least CHACHA20POLY1305_KEY_SIZE]'], 'return_type': 'bool'}`

### Rust Evidence

- Graph edges: `0`

## W-001170 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: chacha_block_generic
- Explanation: chacha_block_generic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct chacha_state *state', 'u8 out[CHACHA_BLOCK_SIZE]', 'int nrounds'], 'return_type': 'void'}`
- New: `{'params': ['struct chacha_state *state', 'u8 out[at_least CHACHA_BLOCK_SIZE]', 'int nrounds'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001171 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: chacha_init
- Explanation: chacha_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct chacha_state *state', 'const u32 key[CHACHA_KEY_WORDS]', 'const u8 iv[CHACHA_IV_SIZE]'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct chacha_state *state', 'const u32 key[at_least CHACHA_KEY_WORDS]', 'const u8 iv[at_least CHACHA_IV_SIZE]'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-001172 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_aead_setauthsize
- Explanation: crypto_aead_setauthsize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct crypto_aead *tfm', 'unsigned int authsize'], 'return_type': 'int'}`
- New: `{'params': ['&tfm->base', 'authsize'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001173 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_aead_setkey
- Explanation: crypto_aead_setkey changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct crypto_aead *tfm', 'const u8 *key', 'unsigned int keylen'], 'return_type': 'int'}`
- New: `{'params': ['&tfm->base', 'key', 'keylen'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001174 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: curve25519
- Explanation: curve25519 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u8 mypublic[CURVE25519_KEY_SIZE]', 'const u8 secret[CURVE25519_KEY_SIZE]', 'const u8 basepoint[CURVE25519_KEY_SIZE]'], 'return_type': 'bool __must_check'}`
- New: `{'params': ['u8 mypublic[at_least CURVE25519_KEY_SIZE]', 'const u8 secret[at_least CURVE25519_KEY_SIZE]', 'const u8 basepoint[at_least CURVE25519_KEY_SIZE]'], 'return_type': 'bool __must_check'}`

### Rust Evidence

- Graph edges: `0`

## W-001175 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: curve25519_clamp_secret
- Explanation: curve25519_clamp_secret changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u8 secret[CURVE25519_KEY_SIZE]'], 'return_type': 'static inline void'}`
- New: `{'params': ['u8 secret[at_least CURVE25519_KEY_SIZE]'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-001176 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: curve25519_generate_public
- Explanation: curve25519_generate_public changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u8 pub[CURVE25519_KEY_SIZE]', 'const u8 secret[CURVE25519_KEY_SIZE]'], 'return_type': 'bool __must_check'}`
- New: `{'params': ['u8 pub[at_least CURVE25519_KEY_SIZE]', 'const u8 secret[at_least CURVE25519_KEY_SIZE]'], 'return_type': 'bool __must_check'}`

### Rust Evidence

- Graph edges: `0`

## W-001177 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: curve25519_generate_secret
- Explanation: curve25519_generate_secret changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u8 secret[CURVE25519_KEY_SIZE]'], 'return_type': 'static inline void'}`
- New: `{'params': ['u8 secret[at_least CURVE25519_KEY_SIZE]'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-001178 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: curve25519_generic
- Explanation: curve25519_generic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u8 out[CURVE25519_KEY_SIZE]', 'const u8 scalar[CURVE25519_KEY_SIZE]', 'const u8 point[CURVE25519_KEY_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['u8 out[at_least CURVE25519_KEY_SIZE]', 'const u8 scalar[at_least CURVE25519_KEY_SIZE]', 'const u8 point[at_least CURVE25519_KEY_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001180 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_buddy_block_offset
- Explanation: drm_buddy_block_offset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_buddy_block *block'], 'return_type': 'static inline u64'}`
- New: `{'params': ['const struct drm_buddy_block *block'], 'return_type': 'static inline u64'}`

### Rust Evidence

- Graph edges: `0`

## W-001181 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_client_dev_restore
- Explanation: drm_client_dev_restore changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_device *dev'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct drm_device *dev', 'bool force'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-001182 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_client_dev_resume
- Explanation: drm_client_dev_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_device *dev', 'bool holds_console_lock'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct drm_device *dev'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-001183 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_client_dev_suspend
- Explanation: drm_client_dev_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_device *dev', 'bool holds_console_lock'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct drm_device *dev'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-001184 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_pagemap_devmem_init
- Explanation: drm_pagemap_devmem_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_pagemap_devmem *devmem_allocation', 'struct device *dev', 'struct mm_struct *mm', 'const struct drm_pagemap_devmem_ops *ops', 'struct drm_pagemap *dpagemap', 'size_t size'], 'return_type': 'void'}`
- New: `{'params': ['struct drm_pagemap_devmem *devmem_allocation', 'struct device *dev', 'struct mm_struct *mm', 'const struct drm_pagemap_devmem_ops *ops', 'struct drm_pagemap *dpagemap', 'size_t size', 'struct dma_fence *pre_migrate_fence'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001186 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: hchacha_block
- Explanation: hchacha_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct chacha_state *state', 'u32 out[HCHACHA_OUT_WORDS]', 'int nrounds'], 'return_type': 'void'}`
- New: `{'params': ['const struct chacha_state *state', 'u32 out[at_least HCHACHA_OUT_WORDS]', 'int nrounds'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001187 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: hchacha_block_generic
- Explanation: hchacha_block_generic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct chacha_state *state', 'u32 out[HCHACHA_OUT_WORDS]', 'int nrounds'], 'return_type': 'void'}`
- New: `{'params': ['const struct chacha_state *state', 'u32 out[at_least HCHACHA_OUT_WORDS]', 'int nrounds'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001188 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: hmac_md5
- Explanation: hmac_md5 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct hmac_md5_key *key', 'const u8 *data', 'size_t data_len', 'u8 out[MD5_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['const struct hmac_md5_key *key', 'const u8 *data', 'size_t data_len', 'u8 out[at_least MD5_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001189 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: hmac_md5_final
- Explanation: hmac_md5_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct hmac_md5_ctx *ctx', 'u8 out[MD5_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['struct hmac_md5_ctx *ctx', 'u8 out[at_least MD5_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001190 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: hmac_md5_usingrawkey
- Explanation: hmac_md5_usingrawkey changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const u8 *raw_key', 'size_t raw_key_len', 'const u8 *data', 'size_t data_len', 'u8 out[MD5_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['const u8 *raw_key', 'size_t raw_key_len', 'const u8 *data', 'size_t data_len', 'u8 out[at_least MD5_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001191 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: hmac_sha1
- Explanation: hmac_sha1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct hmac_sha1_key *key', 'const u8 *data', 'size_t data_len', 'u8 out[SHA1_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['const struct hmac_sha1_key *key', 'const u8 *data', 'size_t data_len', 'u8 out[at_least SHA1_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001192 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: hmac_sha1_final
- Explanation: hmac_sha1_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct hmac_sha1_ctx *ctx', 'u8 out[SHA1_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['struct hmac_sha1_ctx *ctx', 'u8 out[at_least SHA1_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001193 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: hmac_sha1_usingrawkey
- Explanation: hmac_sha1_usingrawkey changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const u8 *raw_key', 'size_t raw_key_len', 'const u8 *data', 'size_t data_len', 'u8 out[SHA1_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['const u8 *raw_key', 'size_t raw_key_len', 'const u8 *data', 'size_t data_len', 'u8 out[at_least SHA1_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001207 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: io_remap_pfn_range
- Explanation: io_remap_pfn_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct vm_area_struct *vma', 'unsigned long addr', 'unsigned long pfn', 'unsigned long size', 'pgprot_t prot'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct vm_area_struct *vma', 'unsigned long addr', 'unsigned long orig_pfn', 'unsigned long size', 'pgprot_t orig_prot'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `0`

## W-001208 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: md5
- Explanation: md5 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const u8 *data', 'size_t len', 'u8 out[MD5_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['const u8 *data', 'size_t len', 'u8 out[at_least MD5_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001209 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: md5_final
- Explanation: md5_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct md5_ctx *ctx', 'u8 out[MD5_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['struct md5_ctx *ctx', 'u8 out[at_least MD5_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001215 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_find_first
- Explanation: phy_find_first changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mii_bus *bus'], 'return_type': 'struct phy_device *'}`
- New: `{'params': ['struct mii_bus *bus'], 'return_type': 'static inline struct phy_device *'}`

### Rust Evidence

- Graph edges: `0`

## W-001216 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: poly1305_init
- Explanation: poly1305_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct poly1305_desc_ctx *desc', 'const u8 key[POLY1305_KEY_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['struct poly1305_desc_ctx *desc', 'const u8 key[at_least POLY1305_KEY_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001219 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sb_start_write_trylock
- Explanation: sb_start_write_trylock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct super_block *sb'], 'return_type': 'static inline bool'}`
- New: `{'params': ['file_inode(file)->i_sb'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001220 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sb_write_not_started
- Explanation: sb_write_not_started changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct super_block *sb'], 'return_type': 'static inline bool'}`
- New: `{'params': ['file_inode(file)->i_sb'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001221 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sb_write_started
- Explanation: sb_write_started changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct super_block *sb'], 'return_type': 'static inline bool'}`
- New: `{'params': ['file_inode(file)->i_sb'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001222 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sha1
- Explanation: sha1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const u8 *data', 'size_t len', 'u8 out[SHA1_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['const u8 *data', 'size_t len', 'u8 out[at_least SHA1_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001223 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sha1_final
- Explanation: sha1_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct sha1_ctx *ctx', 'u8 out[SHA1_DIGEST_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['struct sha1_ctx *ctx', 'u8 out[at_least SHA1_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001234 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: task_mm_cid
- Explanation: task_mm_cid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct task_struct *t'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct task_struct *t'], 'return_type': 'static __always_inline int'}`

### Rust Evidence

- Graph edges: `0`

## W-001235 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: test_bit
- Explanation: test_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['PT_reserved', '&pt->pt_flags.f'], 'return_type': 'return'}`
- New: `{'params': ['PT_kernel', '&ptdesc->pt_flags.f'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001239 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ttm_device_init
- Explanation: ttm_device_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct ttm_device *bdev', 'const struct ttm_device_funcs *funcs', 'struct device *dev', 'struct address_space *mapping', 'struct drm_vma_offset_manager *vma_manager', 'bool use_dma_alloc', 'bool use_dma32'], 'return_type': 'int'}`
- New: `{'params': ['struct ttm_device *bdev', 'const struct ttm_device_funcs *funcs', 'struct device *dev', 'struct address_space *mapping', 'struct drm_vma_offset_manager *vma_manager', 'unsigned int alloc_flags'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-001240 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ttm_pool_init
- Explanation: ttm_pool_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct ttm_pool *pool', 'struct device *dev', 'int nid', 'bool use_dma_alloc', 'bool use_dma32'], 'return_type': 'void'}`
- New: `{'params': ['struct ttm_pool *pool', 'struct device *dev', 'int nid', 'unsigned int alloc_flags'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001249 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: xchacha20poly1305_decrypt
- Explanation: xchacha20poly1305_decrypt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u8 *dst', 'const u8 *src', 'const size_t src_len', 'const u8 *ad', 'const size_t ad_len', 'const u8 nonce[XCHACHA20POLY1305_NONCE_SIZE]', 'const u8 key[CHACHA20POLY1305_KEY_SIZE]'], 'return_type': 'bool __must_check'}`
- New: `{'params': ['u8 *dst', 'const u8 *src', 'const size_t src_len', 'const u8 *ad', 'const size_t ad_len', 'const u8 nonce[at_least XCHACHA20POLY1305_NONCE_SIZE]', 'const u8 key[at_least CHACHA20POLY1305_KEY_SIZE]'], 'return_type': 'bool __must_check'}`

### Rust Evidence

- Graph edges: `0`

## W-001250 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: xchacha20poly1305_encrypt
- Explanation: xchacha20poly1305_encrypt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u8 *dst', 'const u8 *src', 'const size_t src_len', 'const u8 *ad', 'const size_t ad_len', 'const u8 nonce[XCHACHA20POLY1305_NONCE_SIZE]', 'const u8 key[CHACHA20POLY1305_KEY_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['u8 *dst', 'const u8 *src', 'const size_t src_len', 'const u8 *ad', 'const size_t ad_len', 'const u8 nonce[at_least XCHACHA20POLY1305_NONCE_SIZE]', 'const u8 key[at_least CHACHA20POLY1305_KEY_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000825 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: bug_entry
- Explanation: bug_entry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'bug_addr_disp', 'type': 'ffi::c_int'}, {'name': 'file_disp', 'type': 'ffi::c_int'}, {'name': 'line', 'type': 'ffi::c_ushort'}, {'name': 'flags', 'type': 'ffi::c_ushort'}]`
- New: `[{'name': 'bug_addr_disp', 'type': 'ffi::c_int'}, {'name': 'format_disp', 'type': 'ffi::c_int'}, {'name': 'file_disp', 'type': 'ffi::c_int'}, {'name': 'line', 'type': 'ffi::c_ushort'}, {'name': 'flags', 'type': 'ffi::c_ushort'}]`

### Rust Evidence

- Graph edges: `3`

## W-000871 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: taint_flag
- Explanation: taint_flag changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'c_true', 'type': 'ffi::c_char'}, {'name': 'c_false', 'type': 'ffi::c_char'}, {'name': 'module', 'type': 'bool_'}, {'name': 'desc', 'type': '*const ffi::c_char'}]`
- New: `[{'name': 'c_true', 'type': 'ffi::c_char'}, {'name': 'c_false', 'type': 'ffi::c_char'}, {'name': 'desc', 'type': '*const ffi::c_char'}]`

### Rust Evidence

- Graph edges: `3`

## W-000849 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: mm_struct__bindgen_ty_1
- Explanation: mm_struct__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'mm_struct__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mm_mt', 'type': 'maple_tree'}, {'name': 'mmap_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'task_size', 'type': 'ffi::c_ulong'}, {'name': 'pgd', 'type': '*mut pgd_t'}, {'name': 'membarrier_state', 'type': 'atomic_t'}, {'name': 'mm_users', 'type': 'atomic_t'}, {'name': 'pcpu_cid', 'type': '*mut mm_cid'}, {'name': 'mm_cid_next_scan', 'type': 'ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_uint'}, {'name': 'max_nr_cid', 'type': 'atomic_t'}, {'name': 'cpus_allowed_lock', 'type': 'raw_spinlock_t'}, {'name': 'pgtables_bytes', 'type': 'atomic_long_t'}, {'name': 'map_count', 'type': 'ffi::c_int'}, {'name': 'page_table_lock', 'type': 'spinlock_t'}, {'name': 'mmap_lock', 'type': 'rw_semaphore'}, {'name': 'mmlist', 'type': 'list_head'}, {'name': 'vma_writer_wait', 'type': 'rcuwait'}, {'name': 'mm_lock_seq', 'type': 'seqcount_t'}, {'name': 'futex_hash_lock', 'type': 'mutex'}, {'name': 'futex_phash', 'type': '*mut futex_private_hash'}, {'name': 'futex_phash_new', 'type': '*mut futex_private_hash'}, {'name': 'futex_batches', 'type': 'ffi::c_ulong'}, {'name': 'futex_rcu', 'type': 'callback_head'}, {'name': 'futex_atomic', 'type': 'atomic_long_t'}, {'name': 'futex_ref', 'type': '*mut ffi::c_uint'}, {'name': 'hiwater_rss', 'type': 'ffi::c_ulong'}, {'name': 'hiwater_vm', 'type': 'ffi::c_ulong'}, {'name': 'total_vm', 'type': 'ffi::c_ulong'}, {'name': 'locked_vm', 'type': 'ffi::c_ulong'}, {'name': 'pinned_vm', 'type': 'atomic64_t'}, {'name': 'data_vm', 'type': 'ffi::c_ulong'}, {'name': 'exec_vm', 'type': 'ffi::c_ulong'}, {'name': 'stack_vm', 'type': 'ffi::c_ulong'}, {'name': 'def_flags', 'type': 'vm_flags_t'}, {'name': 'write_protect_seq', 'type': 'seqcount_t'}, {'name': 'arg_lock', 'type': 'spinlock_t'}, {'name': 'start_code', 'type': 'ffi::c_ulong'}, {'name': 'end_code', 'type': 'ffi::c_ulong'}, {'name': 'start_data', 'type': 'ffi::c_ulong'}, {'name': 'end_data', 'type': 'ffi::c_ulong'}, {'name': 'start_brk', 'type': 'ffi::c_ulong'}, {'name': 'brk', 'type': 'ffi::c_ulong'}, {'name': 'start_stack', 'type': 'ffi::c_ulong'}, {'name': 'arg_start', 'type': 'ffi::c_ulong'}, {'name': 'arg_end', 'type': 'ffi::c_ulong'}, {'name': 'env_start', 'type': 'ffi::c_ulong'}, {'name': 'env_end', 'type': 'ffi::c_ulong'}, {'name': 'saved_auxv', 'type': '[ffi::c_ulong; 52usize]'}, {'name': 'rss_stat', 'type': '[percpu_counter; 4usize]'}, {'name': 'binfmt', 'type': '*mut linux_binfmt'}, {'name': 'context', 'type': 'mm_context_t'}, {'name': 'flags', 'type': 'mm_flags_t'}, {'name': 'ioctx_lock', 'type': 'spinlock_t'}, {'name': 'ioctx_table', 'type': '*mut kioctx_table'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'exe_file', 'type': '*mut file'}, {'name': 'notifier_subscriptions', 'type': '*mut mmu_notifier_subscriptions'}, {'name': 'tlb_flush_pending', 'type': 'atomic_t'}, {'name': 'tlb_flush_batched', 'type': 'atomic_t'}, {'name': 'uprobes_state', 'type': 'uprobes_state'}, {'name': 'hugetlb_usage', 'type': 'atomic_long_t'}, {'name': 'async_put_work', 'type': 'work_struct'}, {'name': 'iommu_mm', 'type': '*mut iommu_mm_data'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'mm_struct__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mm_mt', 'type': 'maple_tree'}, {'name': 'mmap_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'task_size', 'type': 'ffi::c_ulong'}, {'name': 'pgd', 'type': '*mut pgd_t'}, {'name': 'membarrier_state', 'type': 'atomic_t'}, {'name': 'mm_users', 'type': 'atomic_t'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': 'mm_cid', 'type': 'mm_mm_cid'}, {'name': 'pgtables_bytes', 'type': 'atomic_long_t'}, {'name': 'map_count', 'type': 'ffi::c_int'}, {'name': 'page_table_lock', 'type': 'spinlock_t'}, {'name': 'mmap_lock', 'type': 'rw_semaphore'}, {'name': 'mmlist', 'type': 'list_head'}, {'name': 'vma_writer_wait', 'type': 'rcuwait'}, {'name': 'mm_lock_seq', 'type': 'seqcount_t'}, {'name': 'futex_hash_lock', 'type': 'mutex'}, {'name': 'futex_phash', 'type': '*mut futex_private_hash'}, {'name': 'futex_phash_new', 'type': '*mut futex_private_hash'}, {'name': 'futex_batches', 'type': 'ffi::c_ulong'}, {'name': 'futex_rcu', 'type': 'callback_head'}, {'name': 'futex_atomic', 'type': 'atomic_long_t'}, {'name': 'futex_ref', 'type': '*mut ffi::c_uint'}, {'name': 'hiwater_rss', 'type': 'ffi::c_ulong'}, {'name': 'hiwater_vm', 'type': 'ffi::c_ulong'}, {'name': 'total_vm', 'type': 'ffi::c_ulong'}, {'name': 'locked_vm', 'type': 'ffi::c_ulong'}, {'name': 'pinned_vm', 'type': 'atomic64_t'}, {'name': 'data_vm', 'type': 'ffi::c_ulong'}, {'name': 'exec_vm', 'type': 'ffi::c_ulong'}, {'name': 'stack_vm', 'type': 'ffi::c_ulong'}, {'name': 'def_flags', 'type': 'vm_flags_t'}, {'name': 'write_protect_seq', 'type': 'seqcount_t'}, {'name': 'arg_lock', 'type': 'spinlock_t'}, {'name': 'start_code', 'type': 'ffi::c_ulong'}, {'name': 'end_code', 'type': 'ffi::c_ulong'}, {'name': 'start_data', 'type': 'ffi::c_ulong'}, {'name': 'end_data', 'type': 'ffi::c_ulong'}, {'name': 'start_brk', 'type': 'ffi::c_ulong'}, {'name': 'brk', 'type': 'ffi::c_ulong'}, {'name': 'start_stack', 'type': 'ffi::c_ulong'}, {'name': 'arg_start', 'type': 'ffi::c_ulong'}, {'name': 'arg_end', 'type': 'ffi::c_ulong'}, {'name': 'env_start', 'type': 'ffi::c_ulong'}, {'name': 'env_end', 'type': 'ffi::c_ulong'}, {'name': 'saved_auxv', 'type': '[ffi::c_ulong; 52usize]'}, {'name': 'rss_stat', 'type': '[percpu_counter; 4usize]'}, {'name': 'binfmt', 'type': '*mut linux_binfmt'}, {'name': 'context', 'type': 'mm_context_t'}, {'name': 'flags', 'type': 'mm_flags_t'}, {'name': 'ioctx_lock', 'type': 'spinlock_t'}, {'name': 'ioctx_table', 'type': '*mut kioctx_table'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'exe_file', 'type': '*mut file'}, {'name': 'notifier_subscriptions', 'type': '*mut mmu_notifier_subscriptions'}, {'name': 'tlb_flush_pending', 'type': 'atomic_t'}, {'name': 'tlb_flush_batched', 'type': 'atomic_t'}, {'name': 'uprobes_state', 'type': 'uprobes_state'}, {'name': 'hugetlb_usage', 'type': 'atomic_long_t'}, {'name': 'async_put_work', 'type': 'work_struct'}, {'name': 'iommu_mm', 'type': '*mut iommu_mm_data'}]`

### Rust Evidence

- Graph edges: `2`

## W-001129 MacroConstDrift

- Risk: Medium
- Score: 9.0
- Symbol: VM_MIXEDMAP
- Explanation: VM_MIXEDMAP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x10000000	/* Can contain "struct page" and pure PFN pages */`
- New: `INIT_VM_FLAG(MIXEDMAP)`

### Rust Evidence

- Graph edges: `7`

## W-000820 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: attribute_group
- Explanation: attribute_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'is_visible', 'type': '::core::option::Option<'}, {'name': 'is_bin_visible', 'type': '::core::option::Option<'}, {'name': 'bin_size', 'type': '::core::option::Option<'}, {'name': 'attrs', 'type': '*mut *mut attribute'}, {'name': 'bin_attrs', 'type': '*const *const bin_attribute'}]`
- New: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': '__bindgen_anon_1', 'type': 'attribute_group__bindgen_ty_1'}, {'name': 'is_bin_visible', 'type': '::core::option::Option<'}, {'name': 'bin_size', 'type': '::core::option::Option<'}, {'name': '__bindgen_anon_2', 'type': 'attribute_group__bindgen_ty_2'}, {'name': 'bin_attrs', 'type': '*const *const bin_attribute'}]`

### Rust Evidence

- Graph edges: `1`

## W-000823 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bpf_ksym
- Explanation: bpf_ksym changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'start', 'type': 'ffi::c_ulong'}, {'name': 'end', 'type': 'ffi::c_ulong'}, {'name': 'name', 'type': '[ffi::c_char; 512usize]'}, {'name': 'lnode', 'type': 'list_head'}, {'name': 'tnode', 'type': 'latch_tree_node'}, {'name': 'prog', 'type': 'bool_'}]`
- New: `[{'name': 'start', 'type': 'ffi::c_ulong'}, {'name': 'end', 'type': 'ffi::c_ulong'}, {'name': 'name', 'type': '[ffi::c_char; 512usize]'}, {'name': 'lnode', 'type': 'list_head'}, {'name': 'tnode', 'type': 'latch_tree_node'}, {'name': 'prog', 'type': 'bool_'}, {'name': 'fp_start', 'type': 'u32_'}, {'name': 'fp_end', 'type': 'u32_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000824 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bpf_prog_aux
- Explanation: bpf_prog_aux changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'refcnt', 'type': 'atomic64_t'}, {'name': 'used_map_cnt', 'type': 'u32_'}, {'name': 'used_btf_cnt', 'type': 'u32_'}, {'name': 'max_ctx_offset', 'type': 'u32_'}, {'name': 'max_pkt_offset', 'type': 'u32_'}, {'name': 'max_tp_access', 'type': 'u32_'}, {'name': 'stack_depth', 'type': 'u32_'}, {'name': 'id', 'type': 'u32_'}, {'name': 'func_cnt', 'type': 'u32_'}, {'name': 'real_func_cnt', 'type': 'u32_'}, {'name': 'func_idx', 'type': 'u32_'}, {'name': 'attach_btf_id', 'type': 'u32_'}, {'name': 'attach_st_ops_member_off', 'type': 'u32_'}, {'name': 'ctx_arg_info_size', 'type': 'u32_'}, {'name': 'max_rdonly_access', 'type': 'u32_'}, {'name': 'max_rdwr_access', 'type': 'u32_'}, {'name': 'attach_btf', 'type': '*mut btf'}, {'name': 'ctx_arg_info', 'type': '*mut bpf_ctx_arg_aux'}, {'name': 'priv_stack_ptr', 'type': '*mut ffi::c_void'}, {'name': 'dst_mutex', 'type': 'mutex'}, {'name': 'dst_prog', 'type': '*mut bpf_prog'}, {'name': 'dst_trampoline', 'type': '*mut bpf_trampoline'}, {'name': 'saved_dst_prog_type', 'type': 'bpf_prog_type'}, {'name': 'saved_dst_attach_type', 'type': 'bpf_attach_type'}, {'name': 'verifier_zext', 'type': 'bool_'}, {'name': 'dev_bound', 'type': 'bool_'}, {'name': 'offload_requested', 'type': 'bool_'}, {'name': 'attach_btf_trace', 'type': 'bool_'}, {'name': 'attach_tracing_prog', 'type': 'bool_'}, {'name': 'func_proto_unreliable', 'type': 'bool_'}, {'name': 'tail_call_reachable', 'type': 'bool_'}, {'name': 'xdp_has_frags', 'type': 'bool_'}, {'name': 'exception_cb', 'type': 'bool_'}, {'name': 'exception_boundary', 'type': 'bool_'}, {'name': 'is_extended', 'type': 'bool_'}, {'name': 'jits_use_priv_stack', 'type': 'bool_'}, {'name': 'priv_stack_requested', 'type': 'bool_'}, {'name': 'changes_pkt_data', 'type': 'bool_'}, {'name': 'might_sleep', 'type': 'bool_'}, {'name': 'kprobe_write_ctx', 'type': 'bool_'}, {'name': 'prog_array_member_cnt', 'type': 'u64_'}, {'name': 'ext_mutex', 'type': 'mutex'}, {'name': 'arena', 'type': '*mut bpf_arena'}, {'name': 'recursion_detected', 'type': '::core::option::Option<unsafe extern "C" fn(prog: *mut bpf_prog)>'}, {'name': 'attach_func_proto', 'type': '*const btf_type'}, {'name': 'attach_func_name', 'type': '*const ffi::c_char'}, {'name': 'func', 'type': '*mut *mut bpf_prog'}, {'name': 'main_prog_aux', 'type': '*mut bpf_prog_aux'}, {'name': 'jit_data', 'type': '*mut ffi::c_void'}, {'name': 'poke_tab', 'type': '*mut bpf_jit_poke_descriptor'}, {'name': 'kfunc_tab', 'type': '*mut bpf_kfunc_desc_tab'}, {'name': 'kfunc_btf_tab', 'type': '*mut bpf_kfunc_btf_tab'}, {'name': 'size_poke_tab', 'type': 'u32_'}, {'name': 'ksym', 'type': 'bpf_ksym'}, {'name': 'ops', 'type': '*const bpf_prog_ops'}, {'name': 'st_ops', 'type': '*const bpf_struct_ops'}, {'name': 'used_maps', 'type': '*mut *mut bpf_map'}, {'name': 'used_maps_mutex', 'type': 'mutex'}, {'name': 'used_btfs', 'type': '*mut btf_mod_pair'}, {'name': 'prog', 'type': '*mut bpf_prog'}, {'name': 'user', 'type': '*mut user_struct'}, {'name': 'load_time', 'type': 'u64_'}, {'name': 'verified_insns', 'type': 'u32_'}, {'name': 'cgroup_atype', 'type': 'ffi::c_int'}, {'name': 'cgroup_storage', 'type': '[*mut bpf_map; 2usize]'}, {'name': 'name', 'type': '[ffi::c_char; 16usize]'}, {'name': 'bpf_exception_cb', 'type': '::core::option::Option<'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'token', 'type': '*mut bpf_token'}, {'name': 'offload', 'type': '*mut bpf_prog_offload'}, {'name': 'btf', 'type': '*mut btf'}, {'name': 'func_info', 'type': '*mut bpf_func_info'}, {'name': 'func_info_aux', 'type': '*mut bpf_func_info_aux'}, {'name': 'linfo', 'type': '*mut bpf_line_info'}, {'name': 'jited_linfo', 'type': '*mut *mut ffi::c_void'}, {'name': 'func_info_cnt', 'type': 'u32_'}, {'name': 'nr_linfo', 'type': 'u32_'}, {'name': 'linfo_idx', 'type': 'u32_'}, {'name': 'mod_', 'type': '*mut module'}, {'name': 'num_exentries', 'type': 'u32_'}, {'name': 'extable', 'type': '*mut exception_table_entry'}, {'name': '__bindgen_anon_1', 'type': 'bpf_prog_aux__bindgen_ty_1'}, {'name': 'stream', 'type': '[bpf_stream; 2usize]'}]`
- New: `[{'name': 'refcnt', 'type': 'atomic64_t'}, {'name': 'used_map_cnt', 'type': 'u32_'}, {'name': 'used_btf_cnt', 'type': 'u32_'}, {'name': 'max_ctx_offset', 'type': 'u32_'}, {'name': 'max_pkt_offset', 'type': 'u32_'}, {'name': 'max_tp_access', 'type': 'u32_'}, {'name': 'stack_depth', 'type': 'u32_'}, {'name': 'id', 'type': 'u32_'}, {'name': 'func_cnt', 'type': 'u32_'}, {'name': 'real_func_cnt', 'type': 'u32_'}, {'name': 'func_idx', 'type': 'u32_'}, {'name': 'attach_btf_id', 'type': 'u32_'}, {'name': 'attach_st_ops_member_off', 'type': 'u32_'}, {'name': 'ctx_arg_info_size', 'type': 'u32_'}, {'name': 'max_rdonly_access', 'type': 'u32_'}, {'name': 'max_rdwr_access', 'type': 'u32_'}, {'name': 'subprog_start', 'type': 'u32_'}, {'name': 'attach_btf', 'type': '*mut btf'}, {'name': 'ctx_arg_info', 'type': '*mut bpf_ctx_arg_aux'}, {'name': 'priv_stack_ptr', 'type': '*mut ffi::c_void'}, {'name': 'dst_mutex', 'type': 'mutex'}, {'name': 'dst_prog', 'type': '*mut bpf_prog'}, {'name': 'dst_trampoline', 'type': '*mut bpf_trampoline'}, {'name': 'saved_dst_prog_type', 'type': 'bpf_prog_type'}, {'name': 'saved_dst_attach_type', 'type': 'bpf_attach_type'}, {'name': 'verifier_zext', 'type': 'bool_'}, {'name': 'dev_bound', 'type': 'bool_'}, {'name': 'offload_requested', 'type': 'bool_'}, {'name': 'attach_btf_trace', 'type': 'bool_'}, {'name': 'attach_tracing_prog', 'type': 'bool_'}, {'name': 'func_proto_unreliable', 'type': 'bool_'}, {'name': 'tail_call_reachable', 'type': 'bool_'}, {'name': 'xdp_has_frags', 'type': 'bool_'}, {'name': 'exception_cb', 'type': 'bool_'}, {'name': 'exception_boundary', 'type': 'bool_'}, {'name': 'is_extended', 'type': 'bool_'}, {'name': 'jits_use_priv_stack', 'type': 'bool_'}, {'name': 'priv_stack_requested', 'type': 'bool_'}, {'name': 'changes_pkt_data', 'type': 'bool_'}, {'name': 'might_sleep', 'type': 'bool_'}, {'name': 'kprobe_write_ctx', 'type': 'bool_'}, {'name': 'prog_array_member_cnt', 'type': 'u64_'}, {'name': 'ext_mutex', 'type': 'mutex'}, {'name': 'arena', 'type': '*mut bpf_arena'}, {'name': 'recursion_detected', 'type': '::core::option::Option<unsafe extern "C" fn(prog: *mut bpf_prog)>'}, {'name': 'attach_func_proto', 'type': '*const btf_type'}, {'name': 'attach_func_name', 'type': '*const ffi::c_char'}, {'name': 'func', 'type': '*mut *mut bpf_prog'}, {'name': 'main_prog_aux', 'type': '*mut bpf_prog_aux'}, {'name': 'jit_data', 'type': '*mut ffi::c_void'}, {'name': 'poke_tab', 'type': '*mut bpf_jit_poke_descriptor'}, {'name': 'kfunc_tab', 'type': '*mut bpf_kfunc_desc_tab'}, {'name': 'kfunc_btf_tab', 'type': '*mut bpf_kfunc_btf_tab'}, {'name': 'size_poke_tab', 'type': 'u32_'}, {'name': 'ksym', 'type': 'bpf_ksym'}, {'name': 'ops', 'type': '*const bpf_prog_ops'}, {'name': 'st_ops', 'type': '*const bpf_struct_ops'}, {'name': 'used_maps', 'type': '*mut *mut bpf_map'}, {'name': 'used_maps_mutex', 'type': 'mutex'}, {'name': 'used_btfs', 'type': '*mut btf_mod_pair'}, {'name': 'prog', 'type': '*mut bpf_prog'}, {'name': 'user', 'type': '*mut user_struct'}, {'name': 'load_time', 'type': 'u64_'}, {'name': 'verified_insns', 'type': 'u32_'}, {'name': 'cgroup_atype', 'type': 'ffi::c_int'}, {'name': 'cgroup_storage', 'type': '[*mut bpf_map; 2usize]'}, {'name': 'name', 'type': '[ffi::c_char; 16usize]'}, {'name': 'bpf_exception_cb', 'type': '::core::option::Option<'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'token', 'type': '*mut bpf_token'}, {'name': 'offload', 'type': '*mut bpf_prog_offload'}, {'name': 'btf', 'type': '*mut btf'}, {'name': 'func_info', 'type': '*mut bpf_func_info'}, {'name': 'func_info_aux', 'type': '*mut bpf_func_info_aux'}, {'name': 'linfo', 'type': '*mut bpf_line_info'}, {'name': 'jited_linfo', 'type': '*mut *mut ffi::c_void'}, {'name': 'func_info_cnt', 'type': 'u32_'}, {'name': 'nr_linfo', 'type': 'u32_'}, {'name': 'linfo_idx', 'type': 'u32_'}, {'name': 'mod_', 'type': '*mut module'}, {'name': 'num_exentries', 'type': 'u32_'}, {'name': 'extable', 'type': '*mut exception_table_entry'}, {'name': '__bindgen_anon_1', 'type': 'bpf_prog_aux__bindgen_ty_1'}, {'name': 'stream', 'type': '[bpf_stream; 2usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000828 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: cgroup_root
- Explanation: cgroup_root changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'kf_root', 'type': '*mut kernfs_root'}, {'name': 'subsys_mask', 'type': 'ffi::c_uint'}, {'name': 'hierarchy_id', 'type': 'ffi::c_int'}, {'name': 'root_list', 'type': 'list_head'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': '__bindgen_padding_0', 'type': '[u64; 2usize]'}, {'name': 'cgrp', 'type': 'cgroup'}, {'name': 'cgrp_ancestor_storage', 'type': '*mut cgroup'}, {'name': 'nr_cgrps', 'type': 'atomic_t'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'release_agent_path', 'type': '[ffi::c_char; 4096usize]'}, {'name': 'name', 'type': '[ffi::c_char; 64usize]'}]`
- New: `[{'name': 'kf_root', 'type': '*mut kernfs_root'}, {'name': 'subsys_mask', 'type': 'ffi::c_uint'}, {'name': 'hierarchy_id', 'type': 'ffi::c_int'}, {'name': 'root_list', 'type': 'list_head'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'nr_cgrps', 'type': 'atomic_t'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'release_agent_path', 'type': '[ffi::c_char; 4096usize]'}, {'name': 'name', 'type': '[ffi::c_char; 64usize]'}, {'name': '__bindgen_padding_0', 'type': 'u64'}, {'name': 'cgrp', 'type': 'cgroup'}]`

### Rust Evidence

- Graph edges: `1`

## W-000830 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: dev_pagemap_ops
- Explanation: dev_pagemap_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'page_free', 'type': '::core::option::Option<unsafe extern "C" fn(page: *mut page)>'}, {'name': 'memory_failure', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'folio_free', 'type': '::core::option::Option<unsafe extern "C" fn(folio: *mut folio)>'}, {'name': 'memory_failure', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-000831 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: dev_pm_info
- Explanation: dev_pm_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'power_state', 'type': 'pm_message_t'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'driver_flags', 'type': 'u32_'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'entry', 'type': 'list_head'}, {'name': 'completion', 'type': 'completion'}, {'name': 'wakeup', 'type': '*mut wakeup_source'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'suspend_timer', 'type': 'hrtimer'}, {'name': 'timer_expires', 'type': 'u64_'}, {'name': 'work', 'type': 'work_struct'}, {'name': 'wait_queue', 'type': 'wait_queue_head_t'}, {'name': 'wakeirq', 'type': '*mut wake_irq'}, {'name': 'usage_count', 'type': 'atomic_t'}, {'name': 'child_count', 'type': 'atomic_t'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'links_count', 'type': 'ffi::c_uint'}, {'name': 'request', 'type': 'rpm_request'}, {'name': 'runtime_status', 'type': 'rpm_status'}, {'name': 'last_status', 'type': 'rpm_status'}, {'name': 'runtime_error', 'type': 'ffi::c_int'}, {'name': 'autosuspend_delay', 'type': 'ffi::c_int'}, {'name': 'last_busy', 'type': 'u64_'}, {'name': 'active_time', 'type': 'u64_'}, {'name': 'suspended_time', 'type': 'u64_'}, {'name': 'accounting_timestamp', 'type': 'u64_'}, {'name': 'subsys_data', 'type': '*mut pm_subsys_data'}, {'name': 'qos', 'type': '*mut dev_pm_qos'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 7usize]'}]`
- New: `[{'name': 'power_state', 'type': 'pm_message_t'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'driver_flags', 'type': 'u32_'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'entry', 'type': 'list_head'}, {'name': 'completion', 'type': 'completion'}, {'name': 'wakeup', 'type': '*mut wakeup_source'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'suspend_timer', 'type': 'hrtimer'}, {'name': 'timer_expires', 'type': 'u64_'}, {'name': 'work', 'type': 'work_struct'}, {'name': 'wait_queue', 'type': 'wait_queue_head_t'}, {'name': 'wakeirq', 'type': '*mut wake_irq'}, {'name': 'usage_count', 'type': 'atomic_t'}, {'name': 'child_count', 'type': 'atomic_t'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'links_count', 'type': 'ffi::c_uint'}, {'name': 'request', 'type': 'rpm_request'}, {'name': 'runtime_status', 'type': 'rpm_status'}, {'name': 'last_status', 'type': 'rpm_status'}, {'name': 'runtime_error', 'type': 'ffi::c_int'}, {'name': 'autosuspend_delay', 'type': 'ffi::c_int'}, {'name': 'last_busy', 'type': 'u64_'}, {'name': 'active_time', 'type': 'u64_'}, {'name': 'suspended_time', 'type': 'u64_'}, {'name': 'accounting_timestamp', 'type': 'u64_'}, {'name': 'subsys_data', 'type': '*mut pm_subsys_data'}, {'name': 'qos', 'type': '*mut dev_pm_qos'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 7usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000833 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: device_private
- Explanation: device_private changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'klist_children', 'type': 'klist'}, {'name': 'knode_parent', 'type': 'klist_node'}, {'name': 'knode_driver', 'type': 'klist_node'}, {'name': 'knode_bus', 'type': 'klist_node'}, {'name': 'knode_class', 'type': 'klist_node'}, {'name': 'deferred_probe', 'type': 'list_head'}, {'name': 'async_driver', 'type': '*const device_driver'}, {'name': 'deferred_probe_reason', 'type': '*mut ffi::c_char'}, {'name': 'device', 'type': '*mut device'}, {'name': 'driver_type', 'type': 'driver_type'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 7usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000834 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: dir_context
- Explanation: dir_context changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'actor', 'type': 'filldir_t'}, {'name': 'pos', 'type': 'loff_t'}, {'name': 'count', 'type': 'ffi::c_int'}]`
- New: `[{'name': 'actor', 'type': 'filldir_t'}, {'name': 'pos', 'type': 'loff_t'}, {'name': 'count', 'type': 'ffi::c_int'}, {'name': 'dt_flags_mask', 'type': 'ffi::c_uint'}]`

### Rust Evidence

- Graph edges: `1`

## W-000835 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: driver_private
- Explanation: driver_private changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'kobj', 'type': 'kobject'}, {'name': 'klist_devices', 'type': 'klist'}, {'name': 'knode_bus', 'type': 'klist_node'}, {'name': 'mkobj', 'type': '*mut module_kobject'}, {'name': 'driver', 'type': '*mut device_driver'}]`

### Rust Evidence

- Graph edges: `1`

## W-000839 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: drm_printer
- Explanation: drm_printer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'arg', 'type': '*mut ffi::c_void'}, {'name': 'origin', 'type': '*const ffi::c_void'}, {'name': 'prefix', 'type': '*const ffi::c_char'}, {'name': 'line', 'type': 'drm_printer__bindgen_ty_1'}, {'name': 'category', 'type': 'drm_debug_category'}]`
- New: `[]`

### Rust Evidence

- Graph edges: `1`

## W-000840 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: em_perf_domain
- Explanation: em_perf_domain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'em_table', 'type': '*mut em_perf_table'}, {'name': 'nr_perf_states', 'type': 'ffi::c_int'}, {'name': 'min_perf_state', 'type': 'ffi::c_int'}, {'name': 'max_perf_state', 'type': 'ffi::c_int'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'cpus', 'type': '__IncompleteArrayField<ffi::c_ulong>'}]`
- New: `[{'name': 'em_table', 'type': '*mut em_perf_table'}, {'name': 'node', 'type': 'list_head'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'nr_perf_states', 'type': 'ffi::c_int'}, {'name': 'min_perf_state', 'type': 'ffi::c_int'}, {'name': 'max_perf_state', 'type': 'ffi::c_int'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'cpus', 'type': '__IncompleteArrayField<ffi::c_ulong>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000842 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: irq_desc
- Explanation: irq_desc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'irq_common_data', 'type': 'irq_common_data'}, {'name': 'irq_data', 'type': 'irq_data'}, {'name': 'kstat_irqs', 'type': '*mut irqstat'}, {'name': 'handle_irq', 'type': 'irq_flow_handler_t'}, {'name': 'action', 'type': '*mut irqaction'}, {'name': 'status_use_accessors', 'type': 'ffi::c_uint'}, {'name': 'core_internal_state__do_not_mess_with_it', 'type': 'ffi::c_uint'}, {'name': 'depth', 'type': 'ffi::c_uint'}, {'name': 'wake_depth', 'type': 'ffi::c_uint'}, {'name': 'tot_count', 'type': 'ffi::c_uint'}, {'name': 'irq_count', 'type': 'ffi::c_uint'}, {'name': 'last_unhandled', 'type': 'ffi::c_ulong'}, {'name': 'irqs_unhandled', 'type': 'ffi::c_uint'}, {'name': 'threads_handled', 'type': 'atomic_t'}, {'name': 'threads_handled_last', 'type': 'ffi::c_int'}, {'name': 'lock', 'type': 'raw_spinlock_t'}, {'name': 'percpu_enabled', 'type': '*mut cpumask'}, {'name': 'affinity_hint', 'type': '*const cpumask'}, {'name': 'affinity_notify', 'type': '*mut irq_affinity_notify'}, {'name': 'pending_mask', 'type': 'cpumask_var_t'}, {'name': 'threads_oneshot', 'type': 'ffi::c_ulong'}, {'name': 'threads_active', 'type': 'atomic_t'}, {'name': 'wait_for_threads', 'type': 'wait_queue_head_t'}, {'name': 'nr_actions', 'type': 'ffi::c_uint'}, {'name': 'no_suspend_depth', 'type': 'ffi::c_uint'}, {'name': 'cond_suspend_depth', 'type': 'ffi::c_uint'}, {'name': 'force_resume_depth', 'type': 'ffi::c_uint'}, {'name': 'dir', 'type': '*mut proc_dir_entry'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'kobj', 'type': 'kobject'}, {'name': 'request_mutex', 'type': 'mutex'}, {'name': 'parent_irq', 'type': 'ffi::c_int'}, {'name': 'owner', 'type': '*mut module'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'resend_node', 'type': 'hlist_node'}]`

### Rust Evidence

- Graph edges: `1`

## W-000844 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: irq_domain_ops
- Explanation: irq_domain_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'match_', 'type': '::core::option::Option<'}, {'name': 'select', 'type': '::core::option::Option<'}, {'name': 'map', 'type': '::core::option::Option<'}, {'name': 'unmap', 'type': '::core::option::Option<unsafe extern "C" fn(d: *mut irq_domain'}, {'name': 'xlate', 'type': '::core::option::Option<'}, {'name': 'alloc', 'type': '::core::option::Option<'}, {'name': 'free', 'type': '::core::option::Option<'}, {'name': 'activate', 'type': '::core::option::Option<'}, {'name': 'translate', 'type': '::core::option::Option<'}, {'name': 'get_fwspec_info', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-000845 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: irqaction
- Explanation: irqaction changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'handler', 'type': 'irq_handler_t'}, {'name': 'dev_id', 'type': '*mut ffi::c_void'}, {'name': 'percpu_dev_id', 'type': '*mut ffi::c_void'}, {'name': 'next', 'type': '*mut irqaction'}, {'name': 'thread_fn', 'type': 'irq_handler_t'}, {'name': 'thread', 'type': '*mut task_struct'}, {'name': 'secondary', 'type': '*mut irqaction'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'thread_flags', 'type': 'ffi::c_ulong'}, {'name': 'thread_mask', 'type': 'ffi::c_ulong'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'dir', 'type': '*mut proc_dir_entry'}]`
- New: `[{'name': 'handler', 'type': 'irq_handler_t'}, {'name': '__bindgen_anon_1', 'type': 'irqaction__bindgen_ty_1'}, {'name': 'affinity', 'type': '*const cpumask'}, {'name': 'next', 'type': '*mut irqaction'}, {'name': 'thread_fn', 'type': 'irq_handler_t'}, {'name': 'thread', 'type': '*mut task_struct'}, {'name': 'secondary', 'type': '*mut irqaction'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'thread_flags', 'type': 'ffi::c_ulong'}, {'name': 'thread_mask', 'type': 'ffi::c_ulong'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'dir', 'type': '*mut proc_dir_entry'}]`

### Rust Evidence

- Graph edges: `1`

## W-000847 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: mii_timestamper
- Explanation: mii_timestamper changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'rxtstamp', 'type': '::core::option::Option<'}, {'name': 'txtstamp', 'type': '::core::option::Option<'}, {'name': 'hwtstamp', 'type': '::core::option::Option<'}, {'name': 'link_state', 'type': '::core::option::Option<'}, {'name': 'ts_info', 'type': '::core::option::Option<'}, {'name': 'device', 'type': '*mut device'}]`
- New: `[{'name': 'rxtstamp', 'type': '::core::option::Option<'}, {'name': 'txtstamp', 'type': '::core::option::Option<'}, {'name': 'hwtstamp_set', 'type': '::core::option::Option<'}, {'name': 'hwtstamp_get', 'type': '::core::option::Option<'}, {'name': 'link_state', 'type': '::core::option::Option<'}, {'name': 'ts_info', 'type': '::core::option::Option<'}, {'name': 'device', 'type': '*mut device'}]`

### Rust Evidence

- Graph edges: `1`

## W-000850 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: mtd_info
- Explanation: mtd_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[]`

### Rust Evidence

- Graph edges: `1`

## W-000851 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: pci_ops
- Explanation: pci_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'add_bus', 'type': '::core::option::Option<unsafe extern "C" fn(bus: *mut pci_bus) -> ffi::c_int>'}, {'name': 'remove_bus', 'type': '::core::option::Option<unsafe extern "C" fn(bus: *mut pci_bus)>'}, {'name': 'map_bus', 'type': '::core::option::Option<'}, {'name': 'read', 'type': '::core::option::Option<'}, {'name': 'write', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'add_bus', 'type': '::core::option::Option<unsafe extern "C" fn(bus: *mut pci_bus) -> ffi::c_int>'}, {'name': 'remove_bus', 'type': '::core::option::Option<unsafe extern "C" fn(bus: *mut pci_bus)>'}, {'name': 'map_bus', 'type': '::core::option::Option<'}, {'name': 'read', 'type': '::core::option::Option<'}, {'name': 'write', 'type': '::core::option::Option<'}, {'name': 'assert_perst', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-000855 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: reg_genl_event
- Explanation: reg_genl_event changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'reg_name', 'type': '[ffi::c_char; 32usize]'}, {'name': 'event', 'type': 'u64'}]`
- New: `[{'name': 'reg_name', 'type': '[ffi::c_char; 32usize]'}, {'name': 'event', 'type': '__u64'}]`

### Rust Evidence

- Graph edges: `1`

## W-000856 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: renamedata
- Explanation: renamedata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mnt_idmap', 'type': '*mut mnt_idmap'}, {'name': 'old_parent', 'type': '*mut dentry'}, {'name': 'old_dentry', 'type': '*mut dentry'}, {'name': 'new_parent', 'type': '*mut dentry'}, {'name': 'new_dentry', 'type': '*mut dentry'}, {'name': 'delegated_inode', 'type': '*mut *mut inode'}, {'name': 'flags', 'type': 'ffi::c_uint'}]`
- New: `[{'name': 'mnt_idmap', 'type': '*mut mnt_idmap'}, {'name': 'old_parent', 'type': '*mut dentry'}, {'name': 'old_dentry', 'type': '*mut dentry'}, {'name': 'new_parent', 'type': '*mut dentry'}, {'name': 'new_dentry', 'type': '*mut dentry'}, {'name': 'delegated_inode', 'type': '*mut delegated_inode'}, {'name': 'flags', 'type': 'ffi::c_uint'}]`

### Rust Evidence

- Graph edges: `1`

## W-000858 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: request_queue
- Explanation: request_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'queuedata', 'type': '*mut ffi::c_void'}, {'name': 'elevator', 'type': '*mut elevator_queue'}, {'name': 'mq_ops', 'type': '*const blk_mq_ops'}, {'name': 'queue_ctx', 'type': '*mut blk_mq_ctx'}, {'name': 'queue_flags', 'type': 'ffi::c_ulong'}, {'name': 'rq_timeout', 'type': 'ffi::c_uint'}, {'name': 'queue_depth', 'type': 'ffi::c_uint'}, {'name': 'refs', 'type': 'refcount_t'}, {'name': 'nr_hw_queues', 'type': 'ffi::c_uint'}, {'name': 'hctx_table', 'type': 'xarray'}, {'name': 'q_usage_counter', 'type': 'percpu_ref'}, {'name': 'io_lock_cls_key', 'type': 'lock_class_key'}, {'name': 'io_lockdep_map', 'type': 'lockdep_map'}, {'name': 'q_lock_cls_key', 'type': 'lock_class_key'}, {'name': 'q_lockdep_map', 'type': 'lockdep_map'}, {'name': 'last_merge', 'type': '*mut request'}, {'name': 'queue_lock', 'type': 'spinlock_t'}, {'name': 'quiesce_depth', 'type': 'ffi::c_int'}, {'name': 'disk', 'type': '*mut gendisk'}, {'name': 'mq_kobj', 'type': '*mut kobject'}, {'name': 'limits', 'type': 'queue_limits'}, {'name': 'dev', 'type': '*mut device'}, {'name': 'rpm_status', 'type': 'rpm_status'}, {'name': 'pm_only', 'type': 'atomic_t'}, {'name': 'stats', 'type': '*mut blk_queue_stats'}, {'name': 'rq_qos', 'type': '*mut rq_qos'}, {'name': 'rq_qos_mutex', 'type': 'mutex'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'nr_requests', 'type': 'ffi::c_ulong'}, {'name': 'timeout', 'type': 'timer_list'}, {'name': 'timeout_work', 'type': 'work_struct'}, {'name': 'nr_active_requests_shared_tags', 'type': 'atomic_t'}, {'name': 'sched_shared_tags', 'type': '*mut blk_mq_tags'}, {'name': 'icq_list', 'type': 'list_head'}, {'name': 'blkcg_pols', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'root_blkg', 'type': '*mut blkcg_gq'}, {'name': 'blkg_list', 'type': 'list_head'}, {'name': 'blkcg_mutex', 'type': 'mutex'}, {'name': 'node', 'type': 'ffi::c_int'}, {'name': 'requeue_lock', 'type': 'spinlock_t'}, {'name': 'requeue_list', 'type': 'list_head'}, {'name': 'requeue_work', 'type': 'delayed_work'}, {'name': 'blk_trace', 'type': '*mut blk_trace'}, {'name': 'fq', 'type': '*mut blk_flush_queue'}, {'name': 'flush_list', 'type': 'list_head'}, {'name': 'elevator_lock', 'type': 'mutex'}, {'name': 'sysfs_lock', 'type': 'mutex'}, {'name': 'limits_lock', 'type': 'mutex'}, {'name': 'unused_hctx_list', 'type': 'list_head'}, {'name': 'unused_hctx_lock', 'type': 'spinlock_t'}, {'name': 'mq_freeze_depth', 'type': 'ffi::c_int'}, {'name': 'callback_head', 'type': 'callback_head'}, {'name': 'mq_freeze_wq', 'type': 'wait_queue_head_t'}, {'name': 'mq_freeze_lock', 'type': 'mutex'}, {'name': 'tag_set', 'type': '*mut blk_mq_tag_set'}, {'name': 'tag_set_list', 'type': 'list_head'}, {'name': 'debugfs_dir', 'type': '*mut dentry'}, {'name': 'sched_debugfs_dir', 'type': '*mut dentry'}, {'name': 'rqos_debugfs_dir', 'type': '*mut dentry'}, {'name': 'debugfs_mutex', 'type': 'mutex'}]`
- New: `[{'name': 'queuedata', 'type': '*mut ffi::c_void'}, {'name': 'elevator', 'type': '*mut elevator_queue'}, {'name': 'mq_ops', 'type': '*const blk_mq_ops'}, {'name': 'queue_ctx', 'type': '*mut blk_mq_ctx'}, {'name': 'queue_flags', 'type': 'ffi::c_ulong'}, {'name': 'rq_timeout', 'type': 'ffi::c_uint'}, {'name': 'queue_depth', 'type': 'ffi::c_uint'}, {'name': 'refs', 'type': 'refcount_t'}, {'name': 'nr_hw_queues', 'type': 'ffi::c_uint'}, {'name': 'queue_hw_ctx', 'type': '*mut *mut blk_mq_hw_ctx'}, {'name': 'q_usage_counter', 'type': 'percpu_ref'}, {'name': 'io_lock_cls_key', 'type': 'lock_class_key'}, {'name': 'io_lockdep_map', 'type': 'lockdep_map'}, {'name': 'q_lock_cls_key', 'type': 'lock_class_key'}, {'name': 'q_lockdep_map', 'type': 'lockdep_map'}, {'name': 'last_merge', 'type': '*mut request'}, {'name': 'queue_lock', 'type': 'spinlock_t'}, {'name': 'quiesce_depth', 'type': 'ffi::c_int'}, {'name': 'disk', 'type': '*mut gendisk'}, {'name': 'mq_kobj', 'type': '*mut kobject'}, {'name': 'limits', 'type': 'queue_limits'}, {'name': 'dev', 'type': '*mut device'}, {'name': 'rpm_status', 'type': 'rpm_status'}, {'name': 'pm_only', 'type': 'atomic_t'}, {'name': 'stats', 'type': '*mut blk_queue_stats'}, {'name': 'rq_qos', 'type': '*mut rq_qos'}, {'name': 'rq_qos_mutex', 'type': 'mutex'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'nr_requests', 'type': 'ffi::c_ulong'}, {'name': 'timeout', 'type': 'timer_list'}, {'name': 'timeout_work', 'type': 'work_struct'}, {'name': 'nr_active_requests_shared_tags', 'type': 'atomic_t'}, {'name': 'sched_shared_tags', 'type': '*mut blk_mq_tags'}, {'name': 'icq_list', 'type': 'list_head'}, {'name': 'blkcg_pols', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'root_blkg', 'type': '*mut blkcg_gq'}, {'name': 'blkg_list', 'type': 'list_head'}, {'name': 'blkcg_mutex', 'type': 'mutex'}, {'name': 'node', 'type': 'ffi::c_int'}, {'name': 'requeue_lock', 'type': 'spinlock_t'}, {'name': 'requeue_list', 'type': 'list_head'}, {'name': 'requeue_work', 'type': 'delayed_work'}, {'name': 'blk_trace', 'type': '*mut blk_trace'}, {'name': 'fq', 'type': '*mut blk_flush_queue'}, {'name': 'flush_list', 'type': 'list_head'}, {'name': 'elevator_lock', 'type': 'mutex'}, {'name': 'sysfs_lock', 'type': 'mutex'}, {'name': 'limits_lock', 'type': 'mutex'}, {'name': 'unused_hctx_list', 'type': 'list_head'}, {'name': 'unused_hctx_lock', 'type': 'spinlock_t'}, {'name': 'mq_freeze_depth', 'type': 'ffi::c_int'}, {'name': 'callback_head', 'type': 'callback_head'}, {'name': 'mq_freeze_wq', 'type': 'wait_queue_head_t'}, {'name': 'mq_freeze_lock', 'type': 'mutex'}, {'name': 'tag_set', 'type': '*mut blk_mq_tag_set'}, {'name': 'tag_set_list', 'type': 'list_head'}, {'name': 'debugfs_dir', 'type': '*mut dentry'}, {'name': 'sched_debugfs_dir', 'type': '*mut dentry'}, {'name': 'rqos_debugfs_dir', 'type': '*mut dentry'}, {'name': 'debugfs_mutex', 'type': 'mutex'}]`

### Rust Evidence

- Graph edges: `1`

## W-000859 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: restart_block__bindgen_ty_1__bindgen_ty_1
- Explanation: restart_block__bindgen_ty_1__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'uaddr', 'type': '*mut u32_'}, {'name': 'val', 'type': 'u32_'}, {'name': 'flags', 'type': 'u32_'}, {'name': 'bitset', 'type': 'u32_'}, {'name': 'time', 'type': 'u64_'}, {'name': 'uaddr2', 'type': '*mut u32_'}]`
- New: `[{'name': 'uaddr', 'type': '*mut u32_'}, {'name': 'val', 'type': 'u32_'}, {'name': 'flags', 'type': 'u32_'}, {'name': 'bitset', 'type': 'u32_'}, {'name': 'time', 'type': 'ktime_t'}, {'name': 'uaddr2', 'type': '*mut u32_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000860 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: restart_block__bindgen_ty_1__bindgen_ty_2
- Explanation: restart_block__bindgen_ty_1__bindgen_ty_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'clockid', 'type': 'clockid_t'}, {'name': 'type_', 'type': 'timespec_type'}, {'name': '__bindgen_anon_1', 'type': 'restart_block__bindgen_ty_1__bindgen_ty_2__bindgen_ty_1'}, {'name': 'expires', 'type': 'u64_'}]`
- New: `[{'name': 'clockid', 'type': 'clockid_t'}, {'name': 'type_', 'type': 'timespec_type'}, {'name': '__bindgen_anon_1', 'type': 'restart_block__bindgen_ty_1__bindgen_ty_2__bindgen_ty_1'}, {'name': 'expires', 'type': 'ktime_t'}]`

### Rust Evidence

- Graph edges: `1`

## W-000864 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: software_node_ref_args
- Explanation: software_node_ref_args changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'node', 'type': '*const software_node'}, {'name': 'nargs', 'type': 'ffi::c_uint'}, {'name': 'args', 'type': '[u64_; 16usize]'}]`
- New: `[{'name': 'swnode', 'type': '*const software_node'}, {'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'nargs', 'type': 'ffi::c_uint'}, {'name': 'args', 'type': '[u64_; 16usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000865 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: srcu_data
- Explanation: srcu_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'srcu_ctrs', 'type': '[srcu_ctr; 2usize]'}, {'name': 'srcu_reader_flavor', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': '[u32; 7usize]'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'srcu_cblist', 'type': 'rcu_segcblist'}, {'name': 'srcu_gp_seq_needed', 'type': 'ffi::c_ulong'}, {'name': 'srcu_gp_seq_needed_exp', 'type': 'ffi::c_ulong'}, {'name': 'srcu_cblist_invoking', 'type': 'bool_'}, {'name': 'delay_work', 'type': 'timer_list'}, {'name': 'work', 'type': 'work_struct'}, {'name': 'srcu_barrier_head', 'type': 'callback_head'}, {'name': 'mynode', 'type': '*mut srcu_node'}, {'name': 'grpmask', 'type': 'ffi::c_ulong'}, {'name': 'cpu', 'type': 'ffi::c_int'}, {'name': 'ssp', 'type': '*mut srcu_struct'}]`
- New: `[{'name': 'srcu_ctrs', 'type': '[srcu_ctr; 2usize]'}, {'name': 'srcu_reader_flavor', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': '[u32; 7usize]'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'srcu_cblist', 'type': 'rcu_segcblist'}, {'name': 'srcu_gp_seq_needed', 'type': 'ffi::c_ulong'}, {'name': 'srcu_gp_seq_needed_exp', 'type': 'ffi::c_ulong'}, {'name': 'srcu_cblist_invoking', 'type': 'bool_'}, {'name': 'delay_work', 'type': 'timer_list'}, {'name': 'work', 'type': 'work_struct'}, {'name': 'srcu_barrier_head', 'type': 'callback_head'}, {'name': 'srcu_ec_head', 'type': 'callback_head'}, {'name': 'srcu_ec_state', 'type': 'ffi::c_int'}, {'name': 'mynode', 'type': '*mut srcu_node'}, {'name': 'grpmask', 'type': 'ffi::c_ulong'}, {'name': 'cpu', 'type': 'ffi::c_int'}, {'name': 'ssp', 'type': '*mut srcu_struct'}]`

### Rust Evidence

- Graph edges: `1`

## W-000866 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: srcu_struct
- Explanation: srcu_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'srcu_ctrp', 'type': '*mut srcu_ctr'}, {'name': 'sda', 'type': '*mut srcu_data'}, {'name': 'dep_map', 'type': 'lockdep_map'}, {'name': 'srcu_sup', 'type': '*mut srcu_usage'}]`
- New: `[{'name': 'srcu_ctrp', 'type': '*mut srcu_ctr'}, {'name': 'sda', 'type': '*mut srcu_data'}, {'name': 'srcu_reader_flavor', 'type': 'u8_'}, {'name': 'dep_map', 'type': 'lockdep_map'}, {'name': 'srcu_sup', 'type': '*mut srcu_usage'}]`

### Rust Evidence

- Graph edges: `1`

## W-000867 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: subsys_private
- Explanation: subsys_private changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'subsys', 'type': 'kset'}, {'name': 'devices_kset', 'type': '*mut kset'}, {'name': 'interfaces', 'type': 'list_head'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'drivers_kset', 'type': '*mut kset'}, {'name': 'klist_devices', 'type': 'klist'}, {'name': 'klist_drivers', 'type': 'klist'}, {'name': 'bus_notifier', 'type': 'blocking_notifier_head'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'bus', 'type': '*const bus_type'}, {'name': 'dev_root', 'type': '*mut device'}, {'name': 'glue_dirs', 'type': 'kset'}, {'name': 'class', 'type': '*const class'}, {'name': 'lock_key', 'type': 'lock_class_key'}]`

### Rust Evidence

- Graph edges: `1`

## W-000868 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: super_block
- Explanation: super_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 's_list', 'type': 'list_head'}, {'name': 's_dev', 'type': 'dev_t'}, {'name': 's_blocksize_bits', 'type': 'ffi::c_uchar'}, {'name': 's_blocksize', 'type': 'ffi::c_ulong'}, {'name': 's_maxbytes', 'type': 'loff_t'}, {'name': 's_type', 'type': '*mut file_system_type'}, {'name': 's_op', 'type': '*const super_operations'}, {'name': 'dq_op', 'type': '*const dquot_operations'}, {'name': 's_qcop', 'type': '*const quotactl_ops'}, {'name': 's_export_op', 'type': '*const export_operations'}, {'name': 's_flags', 'type': 'ffi::c_ulong'}, {'name': 's_iflags', 'type': 'ffi::c_ulong'}, {'name': 's_magic', 'type': 'ffi::c_ulong'}, {'name': 's_root', 'type': '*mut dentry'}, {'name': 's_umount', 'type': 'rw_semaphore'}, {'name': 's_count', 'type': 'ffi::c_int'}, {'name': 's_active', 'type': 'atomic_t'}, {'name': 's_security', 'type': '*mut ffi::c_void'}, {'name': 's_xattr', 'type': '*const *mut xattr_handler'}, {'name': 's_roots', 'type': 'hlist_bl_head'}, {'name': 's_mounts', 'type': '*mut mount'}, {'name': 's_bdev', 'type': '*mut block_device'}, {'name': 's_bdev_file', 'type': '*mut file'}, {'name': 's_bdi', 'type': '*mut backing_dev_info'}, {'name': 's_mtd', 'type': '*mut mtd_info'}, {'name': 's_instances', 'type': 'hlist_node'}, {'name': 's_quota_types', 'type': 'ffi::c_uint'}, {'name': 's_dquot', 'type': 'quota_info'}, {'name': 's_writers', 'type': 'sb_writers'}, {'name': 's_fs_info', 'type': '*mut ffi::c_void'}, {'name': 's_time_gran', 'type': 'u32_'}, {'name': 's_time_min', 'type': 'time64_t'}, {'name': 's_time_max', 'type': 'time64_t'}, {'name': 's_fsnotify_mask', 'type': 'u32_'}, {'name': 's_fsnotify_info', 'type': '*mut fsnotify_sb_info'}, {'name': 's_id', 'type': '[ffi::c_char; 32usize]'}, {'name': 's_uuid', 'type': 'uuid_t'}, {'name': 's_uuid_len', 'type': 'u8_'}, {'name': 's_sysfs_name', 'type': '[ffi::c_char; 37usize]'}, {'name': 's_max_links', 'type': 'ffi::c_uint'}, {'name': 's_d_flags', 'type': 'ffi::c_uint'}, {'name': 's_vfs_rename_mutex', 'type': 'mutex'}, {'name': 's_subtype', 'type': '*const ffi::c_char'}, {'name': '__s_d_op', 'type': '*const dentry_operations'}, {'name': 's_shrink', 'type': '*mut shrinker'}, {'name': 's_remove_count', 'type': 'atomic_long_t'}, {'name': 's_readonly_remount', 'type': 'ffi::c_int'}, {'name': 's_wb_err', 'type': 'errseq_t'}, {'name': 's_dio_done_wq', 'type': '*mut workqueue_struct'}, {'name': 's_pins', 'type': 'hlist_head'}, {'name': 's_user_ns', 'type': '*mut user_namespace'}, {'name': 's_dentry_lru', 'type': 'list_lru'}, {'name': 's_inode_lru', 'type': 'list_lru'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 's_sync_lock', 'type': 'mutex'}, {'name': 's_stack_depth', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': 'u32'}, {'name': 's_inode_list_lock', 'type': 'spinlock_t'}, {'name': 's_inodes', 'type': 'list_head'}, {'name': 's_inode_wblist_lock', 'type': 'spinlock_t'}, {'name': 's_inodes_wb', 'type': 'list_head'}]`
- New: `[{'name': 's_list', 'type': 'list_head'}, {'name': 's_dev', 'type': 'dev_t'}, {'name': 's_blocksize_bits', 'type': 'ffi::c_uchar'}, {'name': 's_blocksize', 'type': 'ffi::c_ulong'}, {'name': 's_maxbytes', 'type': 'loff_t'}, {'name': 's_type', 'type': '*mut file_system_type'}, {'name': 's_op', 'type': '*const super_operations'}, {'name': 'dq_op', 'type': '*const dquot_operations'}, {'name': 's_qcop', 'type': '*const quotactl_ops'}, {'name': 's_export_op', 'type': '*const export_operations'}, {'name': 's_flags', 'type': 'ffi::c_ulong'}, {'name': 's_iflags', 'type': 'ffi::c_ulong'}, {'name': 's_magic', 'type': 'ffi::c_ulong'}, {'name': 's_root', 'type': '*mut dentry'}, {'name': 's_umount', 'type': 'rw_semaphore'}, {'name': 's_count', 'type': 'ffi::c_int'}, {'name': 's_active', 'type': 'atomic_t'}, {'name': 's_security', 'type': '*mut ffi::c_void'}, {'name': 's_xattr', 'type': '*const *const xattr_handler'}, {'name': 's_roots', 'type': 'hlist_bl_head'}, {'name': 's_mounts', 'type': '*mut mount'}, {'name': 's_bdev', 'type': '*mut block_device'}, {'name': 's_bdev_file', 'type': '*mut file'}, {'name': 's_bdi', 'type': '*mut backing_dev_info'}, {'name': 's_mtd', 'type': '*mut mtd_info'}, {'name': 's_instances', 'type': 'hlist_node'}, {'name': 's_quota_types', 'type': 'ffi::c_uint'}, {'name': 's_dquot', 'type': 'quota_info'}, {'name': 's_writers', 'type': 'sb_writers'}, {'name': 's_fs_info', 'type': '*mut ffi::c_void'}, {'name': 's_time_gran', 'type': 'u32_'}, {'name': 's_time_min', 'type': 'time64_t'}, {'name': 's_time_max', 'type': 'time64_t'}, {'name': 's_fsnotify_mask', 'type': 'u32_'}, {'name': 's_fsnotify_info', 'type': '*mut fsnotify_sb_info'}, {'name': 's_id', 'type': '[ffi::c_char; 32usize]'}, {'name': 's_uuid', 'type': 'uuid_t'}, {'name': 's_uuid_len', 'type': 'u8_'}, {'name': 's_sysfs_name', 'type': '[ffi::c_char; 37usize]'}, {'name': 's_max_links', 'type': 'ffi::c_uint'}, {'name': 's_d_flags', 'type': 'ffi::c_uint'}, {'name': 's_vfs_rename_mutex', 'type': 'mutex'}, {'name': 's_subtype', 'type': '*const ffi::c_char'}, {'name': '__s_d_op', 'type': '*const dentry_operations'}, {'name': 's_shrink', 'type': '*mut shrinker'}, {'name': 's_remove_count', 'type': 'atomic_long_t'}, {'name': 's_readonly_remount', 'type': 'ffi::c_int'}, {'name': 's_wb_err', 'type': 'errseq_t'}, {'name': 's_dio_done_wq', 'type': '*mut workqueue_struct'}, {'name': 's_pins', 'type': 'hlist_head'}, {'name': 's_user_ns', 'type': '*mut user_namespace'}, {'name': 's_dentry_lru', 'type': 'list_lru'}, {'name': 's_inode_lru', 'type': 'list_lru'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 's_sync_lock', 'type': 'mutex'}, {'name': 's_stack_depth', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': 'u32'}, {'name': 's_inode_list_lock', 'type': 'spinlock_t'}, {'name': 's_inodes', 'type': 'list_head'}, {'name': 's_inode_wblist_lock', 'type': 'spinlock_t'}, {'name': 's_inodes_wb', 'type': 'list_head'}, {'name': 's_min_writeback_pages', 'type': 'ffi::c_long'}]`

### Rust Evidence

- Graph edges: `1`

## W-000869 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: super_operations
- Explanation: super_operations changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'destroy_inode', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut inode)>'}, {'name': 'free_inode', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut inode)>'}, {'name': 'write_inode', 'type': '::core::option::Option<'}, {'name': 'drop_inode', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut inode) -> ffi::c_int>'}, {'name': 'evict_inode', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut inode)>'}, {'name': 'put_super', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut super_block)>'}, {'name': 'sync_fs', 'type': '::core::option::Option<'}, {'name': 'freeze_super', 'type': '::core::option::Option<'}, {'name': 'thaw_super', 'type': '::core::option::Option<'}, {'name': 'statfs', 'type': '::core::option::Option<'}, {'name': 'remount_fs', 'type': '::core::option::Option<'}, {'name': 'umount_begin', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut super_block)>'}, {'name': 'show_options', 'type': '::core::option::Option<'}, {'name': 'show_devname', 'type': '::core::option::Option<'}, {'name': 'show_path', 'type': '::core::option::Option<'}, {'name': 'show_stats', 'type': '::core::option::Option<'}, {'name': 'quota_read', 'type': '::core::option::Option<'}, {'name': 'quota_write', 'type': '::core::option::Option<'}, {'name': 'nr_cached_objects', 'type': '::core::option::Option<'}, {'name': 'free_cached_objects', 'type': '::core::option::Option<'}, {'name': 'remove_bdev', 'type': '::core::option::Option<'}, {'name': 'shutdown', 'type': '::core::option::Option<unsafe extern "C" fn(sb: *mut super_block)>'}]`
- New: `[{'name': 'destroy_inode', 'type': '::core::option::Option<unsafe extern "C" fn(inode: *mut inode)>'}, {'name': 'free_inode', 'type': '::core::option::Option<unsafe extern "C" fn(inode: *mut inode)>'}, {'name': 'write_inode', 'type': '::core::option::Option<'}, {'name': 'drop_inode', 'type': '::core::option::Option<unsafe extern "C" fn(inode: *mut inode) -> ffi::c_int>'}, {'name': 'evict_inode', 'type': '::core::option::Option<unsafe extern "C" fn(inode: *mut inode)>'}, {'name': 'put_super', 'type': '::core::option::Option<unsafe extern "C" fn(sb: *mut super_block)>'}, {'name': 'sync_fs', 'type': '::core::option::Option<'}, {'name': 'freeze_super', 'type': '::core::option::Option<'}, {'name': 'freeze_fs', 'type': '::core::option::Option<unsafe extern "C" fn(sb: *mut super_block) -> ffi::c_int>'}, {'name': 'thaw_super', 'type': '::core::option::Option<'}, {'name': 'statfs', 'type': '::core::option::Option<'}, {'name': 'remount_fs', 'type': '::core::option::Option<'}, {'name': 'umount_begin', 'type': '::core::option::Option<unsafe extern "C" fn(sb: *mut super_block)>'}, {'name': 'show_options', 'type': '::core::option::Option<'}, {'name': 'show_devname', 'type': '::core::option::Option<'}, {'name': 'show_path', 'type': '::core::option::Option<'}, {'name': 'show_stats', 'type': '::core::option::Option<'}, {'name': 'quota_read', 'type': '::core::option::Option<'}, {'name': 'quota_write', 'type': '::core::option::Option<'}, {'name': 'nr_cached_objects', 'type': '::core::option::Option<'}, {'name': 'free_cached_objects', 'type': '::core::option::Option<'}, {'name': 'remove_bdev', 'type': '::core::option::Option<'}, {'name': 'shutdown', 'type': '::core::option::Option<unsafe extern "C" fn(sb: *mut super_block)>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000870 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: swap_info_struct
- Explanation: swap_info_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'users', 'type': 'percpu_ref'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'prio', 'type': 'ffi::c_short'}, {'name': 'list', 'type': 'plist_node'}, {'name': 'type_', 'type': 'ffi::c_schar'}, {'name': 'max', 'type': 'ffi::c_uint'}, {'name': 'swap_map', 'type': '*mut ffi::c_uchar'}, {'name': 'zeromap', 'type': '*mut ffi::c_ulong'}, {'name': 'cluster_info', 'type': '*mut swap_cluster_info'}, {'name': 'free_clusters', 'type': 'list_head'}, {'name': 'full_clusters', 'type': 'list_head'}, {'name': 'nonfull_clusters', 'type': '[list_head; 1usize]'}, {'name': 'frag_clusters', 'type': '[list_head; 1usize]'}, {'name': 'pages', 'type': 'ffi::c_uint'}, {'name': 'inuse_pages', 'type': 'atomic_long_t'}, {'name': 'global_cluster', 'type': '*mut swap_sequential_cluster'}, {'name': 'global_cluster_lock', 'type': 'spinlock_t'}, {'name': 'swap_extent_root', 'type': 'rb_root'}, {'name': 'bdev', 'type': '*mut block_device'}, {'name': 'swap_file', 'type': '*mut file'}, {'name': 'comp', 'type': 'completion'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'cont_lock', 'type': 'spinlock_t'}, {'name': 'discard_work', 'type': 'work_struct'}, {'name': 'reclaim_work', 'type': 'work_struct'}, {'name': 'discard_clusters', 'type': 'list_head'}, {'name': 'avail_lists', 'type': '__IncompleteArrayField<plist_node>'}]`
- New: `[{'name': 'users', 'type': 'percpu_ref'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'prio', 'type': 'ffi::c_short'}, {'name': 'list', 'type': 'plist_node'}, {'name': 'type_', 'type': 'ffi::c_schar'}, {'name': 'max', 'type': 'ffi::c_uint'}, {'name': 'swap_map', 'type': '*mut ffi::c_uchar'}, {'name': 'zeromap', 'type': '*mut ffi::c_ulong'}, {'name': 'cluster_info', 'type': '*mut swap_cluster_info'}, {'name': 'free_clusters', 'type': 'list_head'}, {'name': 'full_clusters', 'type': 'list_head'}, {'name': 'nonfull_clusters', 'type': '[list_head; 1usize]'}, {'name': 'frag_clusters', 'type': '[list_head; 1usize]'}, {'name': 'pages', 'type': 'ffi::c_uint'}, {'name': 'inuse_pages', 'type': 'atomic_long_t'}, {'name': 'global_cluster', 'type': '*mut swap_sequential_cluster'}, {'name': 'global_cluster_lock', 'type': 'spinlock_t'}, {'name': 'swap_extent_root', 'type': 'rb_root'}, {'name': 'bdev', 'type': '*mut block_device'}, {'name': 'swap_file', 'type': '*mut file'}, {'name': 'comp', 'type': 'completion'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'cont_lock', 'type': 'spinlock_t'}, {'name': 'discard_work', 'type': 'work_struct'}, {'name': 'reclaim_work', 'type': 'work_struct'}, {'name': 'discard_clusters', 'type': 'list_head'}, {'name': 'avail_list', 'type': 'plist_node'}]`

### Rust Evidence

- Graph edges: `1`

## W-000873 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: unwind_task_info
- Explanation: unwind_task_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'unwind_mask', 'type': 'ffi::c_ulong'}, {'name': 'cache', 'type': '*mut unwind_cache'}, {'name': 'work', 'type': 'callback_head'}, {'name': 'id', 'type': 'unwind_task_id'}]`
- New: `[{'name': 'unwind_mask', 'type': 'atomic_long_t'}, {'name': 'cache', 'type': '*mut unwind_cache'}, {'name': 'work', 'type': 'callback_head'}, {'name': 'id', 'type': 'unwind_task_id'}]`

### Rust Evidence

- Graph edges: `1`

## W-000875 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vm_area_desc
- Explanation: vm_area_desc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mm', 'type': '*const mm_struct'}, {'name': 'file', 'type': '*mut file'}, {'name': 'start', 'type': 'ffi::c_ulong'}, {'name': 'end', 'type': 'ffi::c_ulong'}, {'name': 'pgoff', 'type': 'ffi::c_ulong'}, {'name': 'vm_file', 'type': '*mut file'}, {'name': 'vm_flags', 'type': 'vm_flags_t'}, {'name': 'page_prot', 'type': 'pgprot_t'}, {'name': 'vm_ops', 'type': '*const vm_operations_struct'}, {'name': 'private_data', 'type': '*mut ffi::c_void'}]`
- New: `[{'name': 'mm', 'type': '*const mm_struct'}, {'name': 'file', 'type': '*mut file'}, {'name': 'start', 'type': 'ffi::c_ulong'}, {'name': 'end', 'type': 'ffi::c_ulong'}, {'name': 'pgoff', 'type': 'ffi::c_ulong'}, {'name': 'vm_file', 'type': '*mut file'}, {'name': '__bindgen_anon_1', 'type': 'vm_area_desc__bindgen_ty_1'}, {'name': 'page_prot', 'type': 'pgprot_t'}, {'name': 'vm_ops', 'type': '*const vm_operations_struct'}, {'name': 'private_data', 'type': '*mut ffi::c_void'}, {'name': 'action', 'type': 'mmap_action'}]`

### Rust Evidence

- Graph edges: `1`

## W-000876 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vmem_altmap
- Explanation: vmem_altmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'base_pfn', 'type': 'ffi::c_ulong'}, {'name': 'end_pfn', 'type': 'ffi::c_ulong'}, {'name': 'reserve', 'type': 'ffi::c_ulong'}, {'name': 'free', 'type': 'ffi::c_ulong'}, {'name': 'align', 'type': 'ffi::c_ulong'}, {'name': 'alloc', 'type': 'ffi::c_ulong'}, {'name': 'inaccessible', 'type': 'bool_'}]`
- New: `[{'name': 'base_pfn', 'type': 'ffi::c_ulong'}, {'name': 'end_pfn', 'type': 'ffi::c_ulong'}, {'name': 'reserve', 'type': 'ffi::c_ulong'}, {'name': 'free', 'type': 'ffi::c_ulong'}, {'name': 'align', 'type': 'ffi::c_ulong'}, {'name': 'alloc', 'type': 'ffi::c_ulong'}]`

### Rust Evidence

- Graph edges: `1`

## W-000877 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: wb_completion
- Explanation: wb_completion changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'cnt', 'type': 'atomic_t'}, {'name': 'waitq', 'type': '*mut wait_queue_head_t'}]`
- New: `[{'name': 'cnt', 'type': 'atomic_t'}, {'name': 'waitq', 'type': '*mut wait_queue_head_t'}, {'name': 'progress_stamp', 'type': 'ffi::c_ulong'}, {'name': 'wait_start', 'type': 'ffi::c_ulong'}]`

### Rust Evidence

- Graph edges: `1`

## W-000878 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: xattr_handler
- Explanation: xattr_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[]`

### Rust Evidence

- Graph edges: `1`

## W-001153 MacroConstDrift

- Risk: Medium
- Score: 8.8
- Symbol: __WARN
- Explanation: __WARN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `__WARN_FLAGS(BUGFLAG_TAINT(TAINT_WARN))`
- New: `__WARN_printf(TAINT_WARN, NULL)`

### Rust Evidence

- Graph edges: `6`

## W-000890 MacroConstDrift

- Risk: Medium
- Score: 8.6
- Symbol: XA_FLAGS_ALLOC
- Explanation: XA_FLAGS_ALLOC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16777220`
- New: `33554436`

### Rust Evidence

- Graph edges: `5`

## W-001118 MacroConstDrift

- Risk: Medium
- Score: 8.6
- Symbol: VM_HUGETLB
- Explanation: VM_HUGETLB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00400000	/* Huge TLB Page VM */`
- New: `INIT_VM_FLAG(HUGETLB)`

### Rust Evidence

- Graph edges: `5`

## W-001119 MacroConstDrift

- Risk: Medium
- Score: 8.4
- Symbol: VM_IO
- Explanation: VM_IO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00004000	/* Memory mapped I/O or similar */`
- New: `INIT_VM_FLAG(IO)`

### Rust Evidence

- Graph edges: `4`

## W-001128 MacroConstDrift

- Risk: Medium
- Score: 8.4
- Symbol: VM_MERGEABLE
- Explanation: VM_MERGEABLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `BIT(31)		/* KSM may merge identical pages */`
- New: `INIT_VM_FLAG(MERGEABLE)`

### Rust Evidence

- Graph edges: `4`

## W-000889 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: VM_MAYSHARE
- Explanation: VM_MAYSHARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `128`
- New: `64`

### Rust Evidence

- Graph edges: `3`

## W-001109 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: VM_ACCOUNT
- Explanation: VM_ACCOUNT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00100000	/* Is a VM accounted object */`
- New: `INIT_VM_FLAG(ACCOUNT)`

### Rust Evidence

- Graph edges: `3`

## W-001110 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: VM_ARCH_1
- Explanation: VM_ARCH_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x01000000	/* Architecture-specific flag */`
- New: `INIT_VM_FLAG(ARCH_1)`

### Rust Evidence

- Graph edges: `3`

## W-001112 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: VM_DONTCOPY
- Explanation: VM_DONTCOPY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00020000      /* Do not copy this vma on fork */`
- New: `INIT_VM_FLAG(DONTCOPY)`

### Rust Evidence

- Graph edges: `3`

## W-001113 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: VM_DONTDUMP
- Explanation: VM_DONTDUMP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x04000000	/* Do not include in the core dump */`
- New: `INIT_VM_FLAG(DONTDUMP)`

### Rust Evidence

- Graph edges: `3`

## W-001114 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: VM_DONTEXPAND
- Explanation: VM_DONTEXPAND changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00040000	/* Cannot expand with mremap() */`
- New: `INIT_VM_FLAG(DONTEXPAND)`

### Rust Evidence

- Graph edges: `3`

## W-001115 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: VM_EXEC
- Explanation: VM_EXEC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000004`
- New: `INIT_VM_FLAG(EXEC)`

### Rust Evidence

- Graph edges: `3`

## W-001117 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: VM_HUGEPAGE
- Explanation: VM_HUGEPAGE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x20000000	/* MADV_HUGEPAGE marked this vma */`
- New: `INIT_VM_FLAG(HUGEPAGE)`

### Rust Evidence

- Graph edges: `3`

## W-001121 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: VM_LOCKONFAULT
- Explanation: VM_LOCKONFAULT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00080000	/* Lock the pages covered when they are faulted in */`
- New: `INIT_VM_FLAG(LOCKONFAULT)`

### Rust Evidence

- Graph edges: `3`

## W-001123 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: VM_MAYEXEC
- Explanation: VM_MAYEXEC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000040`
- New: `INIT_VM_FLAG(MAYEXEC)`

### Rust Evidence

- Graph edges: `3`

## W-001125 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: VM_MAYREAD
- Explanation: VM_MAYREAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000010	/* limits for mprotect() etc */`
- New: `INIT_VM_FLAG(MAYREAD)`

### Rust Evidence

- Graph edges: `3`

## W-001126 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: VM_MAYSHARE
- Explanation: VM_MAYSHARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000080`
- New: `INIT_VM_FLAG(MAYSHARE)`

### Rust Evidence

- Graph edges: `3`

## W-001127 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: VM_MAYWRITE
- Explanation: VM_MAYWRITE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000020`
- New: `INIT_VM_FLAG(MAYWRITE)`

### Rust Evidence

- Graph edges: `3`

## W-001130 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: VM_NOHUGEPAGE
- Explanation: VM_NOHUGEPAGE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x40000000	/* MADV_NOHUGEPAGE marked this vma */`
- New: `INIT_VM_FLAG(NOHUGEPAGE)`

### Rust Evidence

- Graph edges: `3`

## W-001131 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: VM_NORESERVE
- Explanation: VM_NORESERVE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00200000	/* should the VM suppress accounting */`
- New: `INIT_VM_FLAG(NORESERVE)`

### Rust Evidence

- Graph edges: `3`

## W-001132 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: VM_PFNMAP
- Explanation: VM_PFNMAP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000400	/* Page-ranges managed without "struct page", just pure PFN */`
- New: `INIT_VM_FLAG(PFNMAP)`

### Rust Evidence

- Graph edges: `3`

## W-001140 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: VM_READ
- Explanation: VM_READ changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000001	/* currently active flags */`
- New: `INIT_VM_FLAG(READ)`

### Rust Evidence

- Graph edges: `3`

## W-001143 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: VM_SHARED
- Explanation: VM_SHARED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000008`
- New: `INIT_VM_FLAG(SHARED)`

### Rust Evidence

- Graph edges: `3`

## W-001144 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: VM_SOFTDIRTY
- Explanation: VM_SOFTDIRTY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0`
- New: `VM_NONE`

### Rust Evidence

- Graph edges: `3`

## W-001148 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: VM_SYNC
- Explanation: VM_SYNC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00800000	/* Synchronous page faults */`
- New: `INIT_VM_FLAG(SYNC)`

### Rust Evidence

- Graph edges: `3`

## W-001151 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: VM_WIPEONFORK
- Explanation: VM_WIPEONFORK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x02000000	/* Wipe VMA contents in child. */`
- New: `INIT_VM_FLAG(WIPEONFORK)`

### Rust Evidence

- Graph edges: `3`

## W-001152 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: VM_WRITE
- Explanation: VM_WRITE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000002`
- New: `INIT_VM_FLAG(WRITE)`

### Rust Evidence

- Graph edges: `3`

## W-000887 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: SRCU_READ_FLAVOR_FAST
- Explanation: SRCU_READ_FLAVOR_FAST changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `4`

### Rust Evidence

- Graph edges: `2`

## W-000879 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: AUXILIARY_NAME_SIZE
- Explanation: AUXILIARY_NAME_SIZE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `32`
- New: `40`

### Rust Evidence

- Graph edges: `1`

## W-000880 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ETHTOOL_MSG_KERNEL_MAX
- Explanation: ETHTOOL_MSG_KERNEL_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `53`
- New: `54`

### Rust Evidence

- Graph edges: `1`

## W-000881 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ETHTOOL_MSG_USER_MAX
- Explanation: ETHTOOL_MSG_USER_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `50`
- New: `51`

### Rust Evidence

- Graph edges: `1`

## W-000882 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: IA32_NR_syscalls
- Explanation: IA32_NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `470`
- New: `471`

### Rust Evidence

- Graph edges: `1`

## W-000883 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: IOCB_AIO_RW
- Explanation: IOCB_AIO_RW changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8388608`
- New: `4194304`

### Rust Evidence

- Graph edges: `1`

## W-000884 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: IOCB_HAS_METADATA
- Explanation: IOCB_HAS_METADATA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16777216`
- New: `8388608`

### Rust Evidence

- Graph edges: `1`

## W-000885 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: NR_syscalls
- Explanation: NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `470`
- New: `471`

### Rust Evidence

- Graph edges: `1`

## W-000886 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: SRCU_READ_FLAVOR_ALL
- Explanation: SRCU_READ_FLAVOR_ALL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `11`
- New: `15`

### Rust Evidence

- Graph edges: `1`

## W-000888 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: SRCU_READ_FLAVOR_SLOWGP
- Explanation: SRCU_READ_FLAVOR_SLOWGP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `12`

### Rust Evidence

- Graph edges: `1`

## W-000891 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: _DPRINTK_FLAGS_INCL_ANY
- Explanation: _DPRINTK_FLAGS_INCL_ANY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `62`
- New: `126`

### Rust Evidence

- Graph edges: `1`

## W-000892 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __ETHTOOL_MSG_KERNEL_CNT
- Explanation: __ETHTOOL_MSG_KERNEL_CNT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `54`
- New: `55`

### Rust Evidence

- Graph edges: `1`

## W-000893 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __ETHTOOL_MSG_USER_CNT
- Explanation: __ETHTOOL_MSG_USER_CNT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `51`
- New: `52`

### Rust Evidence

- Graph edges: `1`

## W-000894 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __NR_ia32_syscalls
- Explanation: __NR_ia32_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `470`
- New: `471`

### Rust Evidence

- Graph edges: `1`

## W-000895 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __NR_syscalls
- Explanation: __NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `470`
- New: `471`

### Rust Evidence

- Graph edges: `1`

## W-000896 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ___GFP_LAST_BIT
- Explanation: ___GFP_LAST_BIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `24`
- New: `25`

### Rust Evidence

- Graph edges: `1`

## W-000897 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_arg_type___BPF_ARG_TYPE_LIMIT
- Explanation: bpf_arg_type___BPF_ARG_TYPE_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `268435455`
- New: `536870911`

### Rust Evidence

- Graph edges: `1`

## W-000898 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_map_type___MAX_BPF_MAP_TYPE
- Explanation: bpf_map_type___MAX_BPF_MAP_TYPE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `34`
- New: `35`

### Rust Evidence

- Graph edges: `1`

## W-000899 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_reg_type_CONST_PTR_TO_DYNPTR
- Explanation: bpf_reg_type_CONST_PTR_TO_DYNPTR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `21`
- New: `22`

### Rust Evidence

- Graph edges: `1`

## W-000900 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_reg_type___BPF_REG_TYPE_LIMIT
- Explanation: bpf_reg_type___BPF_REG_TYPE_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `268435455`
- New: `536870911`

### Rust Evidence

- Graph edges: `1`

## W-000901 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_reg_type___BPF_REG_TYPE_MAX
- Explanation: bpf_reg_type___BPF_REG_TYPE_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `22`
- New: `23`

### Rust Evidence

- Graph edges: `1`

## W-000902 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_return_type___BPF_RET_TYPE_LIMIT
- Explanation: bpf_return_type___BPF_RET_TYPE_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `268435455`
- New: `536870911`

### Rust Evidence

- Graph edges: `1`

## W-000903 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_text_poke_type_BPF_MOD_CALL
- Explanation: bpf_text_poke_type_BPF_MOD_CALL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0`
- New: `1`

### Rust Evidence

- Graph edges: `1`

## W-000904 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_text_poke_type_BPF_MOD_JUMP
- Explanation: bpf_text_poke_type_BPF_MOD_JUMP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `1`
- New: `2`

### Rust Evidence

- Graph edges: `1`

## W-000905 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_type_flag___BPF_TYPE_FLAG_MAX
- Explanation: bpf_type_flag___BPF_TYPE_FLAG_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `134217729`
- New: `268435457`

### Rust Evidence

- Graph edges: `1`

## W-000906 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_type_flag___BPF_TYPE_LAST_FLAG
- Explanation: bpf_type_flag___BPF_TYPE_LAST_FLAG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `134217728`
- New: `268435456`

### Rust Evidence

- Graph edges: `1`

## W-000907 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ethtool_link_mode_bit_indices___ETHTOOL_LINK_MODE_MASK_NBITS
- Explanation: ethtool_link_mode_bit_indices___ETHTOOL_LINK_MODE_MASK_NBITS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `121`
- New: `125`

### Rust Evidence

- Graph edges: `1`

## W-000908 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: kernel_load_data_id_LOADING_MAX_ID
- Explanation: kernel_load_data_id_LOADING_MAX_ID changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `7`
- New: `8`

### Rust Evidence

- Graph edges: `1`

## W-000909 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: kernel_read_file_id_READING_MAX_ID
- Explanation: kernel_read_file_id_READING_MAX_ID changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `7`
- New: `8`

### Rust Evidence

- Graph edges: `1`

## W-000910 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_memory_event_MEMCG_NR_MEMORY_EVENTS
- Explanation: memcg_memory_event_MEMCG_NR_MEMORY_EVENTS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `9`
- New: `10`

### Rust Evidence

- Graph edges: `1`

## W-000911 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: mf_action_page_type_MF_MSG_UNKNOWN
- Explanation: mf_action_page_type_MF_MSG_UNKNOWN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `20`
- New: `21`

### Rust Evidence

- Graph edges: `1`

## W-000912 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pgdat_flags_PGDAT_RECLAIM_LOCKED
- Explanation: pgdat_flags_PGDAT_RECLAIM_LOCKED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `2`
- New: `1`

### Rust Evidence

- Graph edges: `1`

## W-000913 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pgdat_flags_PGDAT_WRITEBACK
- Explanation: pgdat_flags_PGDAT_WRITEBACK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `1`
- New: `0`

### Rust Evidence

- Graph edges: `1`

## W-000914 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: req_flag_bits___REQ_NOUNMAP
- Explanation: req_flag_bits___REQ_NOUNMAP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `29`
- New: `28`

### Rust Evidence

- Graph edges: `1`

## W-000915 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: req_flag_bits___REQ_NR_BITS
- Explanation: req_flag_bits___REQ_NR_BITS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `30`
- New: `29`

### Rust Evidence

- Graph edges: `1`

## W-000916 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_ARP_PVLAN_DISABLE
- Explanation: skb_drop_reason_SKB_DROP_REASON_ARP_PVLAN_DISABLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `117`
- New: `118`

### Rust Evidence

- Graph edges: `1`

## W-000917 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_BRIDGE_INGRESS_STP_STATE
- Explanation: skb_drop_reason_SKB_DROP_REASON_BRIDGE_INGRESS_STP_STATE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `119`
- New: `120`

### Rust Evidence

- Graph edges: `1`

## W-000918 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_CAKE_FLOOD
- Explanation: skb_drop_reason_SKB_DROP_REASON_CAKE_FLOOD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `67`
- New: `68`

### Rust Evidence

- Graph edges: `1`

## W-000919 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_CANFD_RX_INVALID_FRAME
- Explanation: skb_drop_reason_SKB_DROP_REASON_CANFD_RX_INVALID_FRAME changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `121`
- New: `122`

### Rust Evidence

- Graph edges: `1`

## W-000920 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_CANXL_RX_INVALID_FRAME
- Explanation: skb_drop_reason_SKB_DROP_REASON_CANXL_RX_INVALID_FRAME changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `122`
- New: `123`

### Rust Evidence

- Graph edges: `1`

## W-000921 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_CAN_RX_INVALID_FRAME
- Explanation: skb_drop_reason_SKB_DROP_REASON_CAN_RX_INVALID_FRAME changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `120`
- New: `121`

### Rust Evidence

- Graph edges: `1`

## W-000922 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_CPU_BACKLOG
- Explanation: skb_drop_reason_SKB_DROP_REASON_CPU_BACKLOG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `71`
- New: `72`

### Rust Evidence

- Graph edges: `1`

## W-000923 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_DEV_HDR
- Explanation: skb_drop_reason_SKB_DROP_REASON_DEV_HDR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `78`
- New: `79`

### Rust Evidence

- Graph edges: `1`

## W-000924 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_DEV_READY
- Explanation: skb_drop_reason_SKB_DROP_REASON_DEV_READY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `79`
- New: `80`

### Rust Evidence

- Graph edges: `1`

## W-000925 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_DUALPI2_STEP_DROP
- Explanation: skb_drop_reason_SKB_DROP_REASON_DUALPI2_STEP_DROP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `124`
- New: `125`

### Rust Evidence

- Graph edges: `1`

## W-000926 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_DUP_FRAG
- Explanation: skb_drop_reason_SKB_DROP_REASON_DUP_FRAG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `94`
- New: `95`

### Rust Evidence

- Graph edges: `1`

## W-000927 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FQ_BAND_LIMIT
- Explanation: skb_drop_reason_SKB_DROP_REASON_FQ_BAND_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `68`
- New: `69`

### Rust Evidence

- Graph edges: `1`

## W-000928 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FQ_FLOW_LIMIT
- Explanation: skb_drop_reason_SKB_DROP_REASON_FQ_FLOW_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `70`
- New: `71`

### Rust Evidence

- Graph edges: `1`

## W-000929 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FQ_HORIZON_LIMIT
- Explanation: skb_drop_reason_SKB_DROP_REASON_FQ_HORIZON_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `69`
- New: `70`

### Rust Evidence

- Graph edges: `1`

## W-000930 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FRAG_REASM_TIMEOUT
- Explanation: skb_drop_reason_SKB_DROP_REASON_FRAG_REASM_TIMEOUT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `95`
- New: `96`

### Rust Evidence

- Graph edges: `1`

## W-000931 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FRAG_TOO_FAR
- Explanation: skb_drop_reason_SKB_DROP_REASON_FRAG_TOO_FAR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `96`
- New: `97`

### Rust Evidence

- Graph edges: `1`

## W-000932 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FULL_RING
- Explanation: skb_drop_reason_SKB_DROP_REASON_FULL_RING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `80`
- New: `81`

### Rust Evidence

- Graph edges: `1`

## W-000933 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_HDR_TRUNC
- Explanation: skb_drop_reason_SKB_DROP_REASON_HDR_TRUNC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `82`
- New: `83`

### Rust Evidence

- Graph edges: `1`

## W-000934 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_ICMP_CSUM
- Explanation: skb_drop_reason_SKB_DROP_REASON_ICMP_CSUM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `85`
- New: `86`

### Rust Evidence

- Graph edges: `1`

## W-000935 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_INVALID_PROTO
- Explanation: skb_drop_reason_SKB_DROP_REASON_INVALID_PROTO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `86`
- New: `87`

### Rust Evidence

- Graph edges: `1`

## W-000936 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_BAD_EXTHDR
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_BAD_EXTHDR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `98`
- New: `99`

### Rust Evidence

- Graph edges: `1`

## W-000937 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_CODE
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_CODE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `101`
- New: `102`

### Rust Evidence

- Graph edges: `1`

## W-000938 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_OPTIONS
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_OPTIONS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `102`
- New: `103`

### Rust Evidence

- Graph edges: `1`

## W-000939 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_FRAG
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_FRAG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `99`
- New: `100`

### Rust Evidence

- Graph edges: `1`

## W-000940 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_HOP_LIMIT
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_HOP_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `100`
- New: `101`

### Rust Evidence

- Graph edges: `1`

## W-000941 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_NS_OTHERHOST
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_NS_OTHERHOST changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `103`
- New: `104`

### Rust Evidence

- Graph edges: `1`

## W-000942 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INADDRERRORS
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INADDRERRORS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `87`
- New: `88`

### Rust Evidence

- Graph edges: `1`

## W-000943 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INNOROUTES
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INNOROUTES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `88`
- New: `89`

### Rust Evidence

- Graph edges: `1`

## W-000944 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_DEST
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_DEST changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `92`
- New: `93`

### Rust Evidence

- Graph edges: `1`

## W-000945 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_SOURCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_SOURCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `90`
- New: `91`

### Rust Evidence

- Graph edges: `1`

## W-000946 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_LOCALNET
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_LOCALNET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `91`
- New: `92`

### Rust Evidence

- Graph edges: `1`

## W-000947 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_LOCAL_SOURCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_LOCAL_SOURCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `89`
- New: `90`

### Rust Evidence

- Graph edges: `1`

## W-000948 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_TUNNEL_ECN
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_TUNNEL_ECN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `114`
- New: `115`

### Rust Evidence

- Graph edges: `1`

## W-000949 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_LOCAL_MAC
- Explanation: skb_drop_reason_SKB_DROP_REASON_LOCAL_MAC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `116`
- New: `117`

### Rust Evidence

- Graph edges: `1`

## W-000950 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_MAC_IEEE_MAC_CONTROL
- Explanation: skb_drop_reason_SKB_DROP_REASON_MAC_IEEE_MAC_CONTROL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `118`
- New: `119`

### Rust Evidence

- Graph edges: `1`

## W-000951 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_MAC_INVALID_SOURCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_MAC_INVALID_SOURCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `111`
- New: `112`

### Rust Evidence

- Graph edges: `1`

## W-000952 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_MAX
- Explanation: skb_drop_reason_SKB_DROP_REASON_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `127`
- New: `128`

### Rust Evidence

- Graph edges: `1`

## W-000953 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NOMEM
- Explanation: skb_drop_reason_SKB_DROP_REASON_NOMEM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `81`
- New: `82`

### Rust Evidence

- Graph edges: `1`

## W-000954 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NO_TX_TARGET
- Explanation: skb_drop_reason_SKB_DROP_REASON_NO_TX_TARGET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `113`
- New: `114`

### Rust Evidence

- Graph edges: `1`

## W-000955 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_PACKET_SOCK_ERROR
- Explanation: skb_drop_reason_SKB_DROP_REASON_PACKET_SOCK_ERROR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `106`
- New: `107`

### Rust Evidence

- Graph edges: `1`

## W-000956 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_PFMEMALLOC
- Explanation: skb_drop_reason_SKB_DROP_REASON_PFMEMALLOC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `123`
- New: `124`

### Rust Evidence

- Graph edges: `1`

## W-000957 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_PKT_TOO_BIG
- Explanation: skb_drop_reason_SKB_DROP_REASON_PKT_TOO_BIG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `93`
- New: `94`

### Rust Evidence

- Graph edges: `1`

## W-000958 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_PSP_INPUT
- Explanation: skb_drop_reason_SKB_DROP_REASON_PSP_INPUT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `125`
- New: `126`

### Rust Evidence

- Graph edges: `1`

## W-000959 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_PSP_OUTPUT
- Explanation: skb_drop_reason_SKB_DROP_REASON_PSP_OUTPUT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `126`
- New: `127`

### Rust Evidence

- Graph edges: `1`

## W-000960 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_QDISC_CONGESTED
- Explanation: skb_drop_reason_SKB_DROP_REASON_QDISC_CONGESTED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `66`
- New: `67`

### Rust Evidence

- Graph edges: `1`

## W-000961 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_QDISC_OVERLIMIT
- Explanation: skb_drop_reason_SKB_DROP_REASON_QDISC_OVERLIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `65`
- New: `66`

### Rust Evidence

- Graph edges: `1`

## W-000962 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_QUEUE_PURGE
- Explanation: skb_drop_reason_SKB_DROP_REASON_QUEUE_PURGE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `104`
- New: `105`

### Rust Evidence

- Graph edges: `1`

## W-000963 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SKB_CSUM
- Explanation: skb_drop_reason_SKB_DROP_REASON_SKB_CSUM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `75`
- New: `76`

### Rust Evidence

- Graph edges: `1`

## W-000964 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SKB_GSO_SEG
- Explanation: skb_drop_reason_SKB_DROP_REASON_SKB_GSO_SEG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `76`
- New: `77`

### Rust Evidence

- Graph edges: `1`

## W-000965 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SKB_UCOPY_FAULT
- Explanation: skb_drop_reason_SKB_DROP_REASON_SKB_UCOPY_FAULT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `77`
- New: `78`

### Rust Evidence

- Graph edges: `1`

## W-000966 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TAP_FILTER
- Explanation: skb_drop_reason_SKB_DROP_REASON_TAP_FILTER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `83`
- New: `84`

### Rust Evidence

- Graph edges: `1`

## W-000967 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TAP_TXFILTER
- Explanation: skb_drop_reason_SKB_DROP_REASON_TAP_TXFILTER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `84`
- New: `85`

### Rust Evidence

- Graph edges: `1`

## W-000968 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_MINTTL
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_MINTTL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `97`
- New: `98`

### Rust Evidence

- Graph edges: `1`

## W-000969 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_CHAIN_NOTFOUND
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_CHAIN_NOTFOUND changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `107`
- New: `108`

### Rust Evidence

- Graph edges: `1`

## W-000970 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_COOKIE_ERROR
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_COOKIE_ERROR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `105`
- New: `106`

### Rust Evidence

- Graph edges: `1`

## W-000971 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_INGRESS
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_INGRESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `73`
- New: `74`

### Rust Evidence

- Graph edges: `1`

## W-000972 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_RECLASSIFY_LOOP
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_RECLASSIFY_LOOP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `108`
- New: `109`

### Rust Evidence

- Graph edges: `1`

## W-000973 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TUNNEL_TXINFO
- Explanation: skb_drop_reason_SKB_DROP_REASON_TUNNEL_TXINFO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `115`
- New: `116`

### Rust Evidence

- Graph edges: `1`

## W-000974 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_UNHANDLED_PROTO
- Explanation: skb_drop_reason_SKB_DROP_REASON_UNHANDLED_PROTO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `74`
- New: `75`

### Rust Evidence

- Graph edges: `1`

## W-000975 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_VXLAN_ENTRY_EXISTS
- Explanation: skb_drop_reason_SKB_DROP_REASON_VXLAN_ENTRY_EXISTS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `112`
- New: `113`

### Rust Evidence

- Graph edges: `1`

## W-000976 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_VXLAN_INVALID_HDR
- Explanation: skb_drop_reason_SKB_DROP_REASON_VXLAN_INVALID_HDR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `109`
- New: `110`

### Rust Evidence

- Graph edges: `1`

## W-000977 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_VXLAN_VNI_NOT_FOUND
- Explanation: skb_drop_reason_SKB_DROP_REASON_VXLAN_VNI_NOT_FOUND changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `110`
- New: `111`

### Rust Evidence

- Graph edges: `1`

## W-000978 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_XDP
- Explanation: skb_drop_reason_SKB_DROP_REASON_XDP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `72`
- New: `73`

### Rust Evidence

- Graph edges: `1`

## W-001103 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: IOCB_AIO_RW
- Explanation: IOCB_AIO_RW changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `(1 << 23)`
- New: `(1 << 22)`

### Rust Evidence

- Graph edges: `1`

## W-001104 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: IOCB_HAS_METADATA
- Explanation: IOCB_HAS_METADATA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `(1 << 24)`
- New: `(1 << 23)`

### Rust Evidence

- Graph edges: `1`

## W-001137 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: VM_PKEY_BIT4
- Explanation: VM_PKEY_BIT4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0`
- New: `VM_NONE`

### Rust Evidence

- Graph edges: `1`

## W-001146 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: VM_STACK
- Explanation: VM_STACK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `VM_GROWSDOWN`
- New: `INIT_VM_FLAG(STACK)`

### Rust Evidence

- Graph edges: `1`

## W-001147 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: VM_STACK_EARLY
- Explanation: VM_STACK_EARLY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0`
- New: `VM_NONE`

### Rust Evidence

- Graph edges: `1`

## W-000979 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: BSS_MAIN
- Explanation: BSS_MAIN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `.bss`
- New: `.bss .bss.[0-9a-zA-Z_]* .bss..L* .bss..compoundliteral*`

### Rust Evidence

- Graph edges: `0`

## W-000980 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_ARM_CLK
- Explanation: CLK_ARM_CLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `13`
- New: `9`

### Rust Evidence

- Graph edges: `0`

## W-000981 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_CHIPID
- Explanation: CLK_CHIPID changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `301`
- New: `318`

### Rust Evidence

- Graph edges: `0`

## W-000982 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_PERI_UART1
- Explanation: CLK_DOUT_PERI_UART1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `32`
- New: `7`

### Rust Evidence

- Graph edges: `0`

## W-000983 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_PERI_UART2
- Explanation: CLK_DOUT_PERI_UART2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `33`
- New: `8`

### Rust Evidence

- Graph edges: `0`

## W-000984 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_SHARED0_DIV2
- Explanation: CLK_DOUT_SHARED0_DIV2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `19`
- New: `2`

### Rust Evidence

- Graph edges: `0`

## W-000985 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_SHARED0_DIV3
- Explanation: CLK_DOUT_SHARED0_DIV3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `18`
- New: `3`

### Rust Evidence

- Graph edges: `0`

## W-000986 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_SHARED0_DIV4
- Explanation: CLK_DOUT_SHARED0_DIV4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `22`
- New: `4`

### Rust Evidence

- Graph edges: `0`

## W-000987 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_SHARED1_DIV2
- Explanation: CLK_DOUT_SHARED1_DIV2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `21`
- New: `6`

### Rust Evidence

- Graph edges: `0`

## W-000988 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_SHARED1_DIV3
- Explanation: CLK_DOUT_SHARED1_DIV3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `20`
- New: `7`

### Rust Evidence

- Graph edges: `0`

## W-000989 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_SHARED1_DIV4
- Explanation: CLK_DOUT_SHARED1_DIV4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `23`
- New: `8`

### Rust Evidence

- Graph edges: `0`

## W-000990 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DSIM1
- Explanation: CLK_DSIM1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `411`
- New: `290 /* Exynos4210 only */`

### Rust Evidence

- Graph edges: `0`

## W-000991 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_FIMD1
- Explanation: CLK_FIMD1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `421`
- New: `339`

### Rust Evidence

- Graph edges: `0`

## W-000992 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_FOUT_BPLL
- Explanation: CLK_FOUT_BPLL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `11`
- New: `4`

### Rust Evidence

- Graph edges: `0`

## W-000993 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_FOUT_CPLL
- Explanation: CLK_FOUT_CPLL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `3`
- New: `6`

### Rust Evidence

- Graph edges: `0`

## W-000994 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_FOUT_EPLL
- Explanation: CLK_FOUT_EPLL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `7`

### Rust Evidence

- Graph edges: `0`

## W-000995 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_FOUT_MPLL
- Explanation: CLK_FOUT_MPLL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `3`

### Rust Evidence

- Graph edges: `0`

## W-000996 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_FOUT_SHARED1_PLL
- Explanation: CLK_FOUT_SHARED1_PLL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `2`
- New: `5`

### Rust Evidence

- Graph edges: `0`

## W-000997 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_FOUT_VPLL
- Explanation: CLK_FOUT_VPLL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `9`
- New: `8`

### Rust Evidence

- Graph edges: `0`

## W-000998 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_G2D
- Explanation: CLK_G2D changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `481`
- New: `345`

### Rust Evidence

- Graph edges: `0`

## W-000999 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_G3D
- Explanation: CLK_G3D changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `501`
- New: `349`

### Rust Evidence

- Graph edges: `0`

## W-001000 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_GSCL0
- Explanation: CLK_GSCL0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `465`
- New: `256`

### Rust Evidence

- Graph edges: `0`

## W-001001 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_GSCL1
- Explanation: CLK_GSCL1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `466`
- New: `257`

### Rust Evidence

- Graph edges: `0`

## W-001002 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_GSCL_WA
- Explanation: CLK_GSCL_WA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `463`
- New: `260`

### Rust Evidence

- Graph edges: `0`

## W-001003 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_GSCL_WB
- Explanation: CLK_GSCL_WB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `464`
- New: `261`

### Rust Evidence

- Graph edges: `0`

## W-001004 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_HDMI
- Explanation: CLK_HDMI changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `413`
- New: `344`

### Rust Evidence

- Graph edges: `0`

## W-001005 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_HDMI_CEC
- Explanation: CLK_HDMI_CEC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `313`
- New: `334`

### Rust Evidence

- Graph edges: `0`

## W-001006 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_I2C0
- Explanation: CLK_I2C0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `261`
- New: `294`

### Rust Evidence

- Graph edges: `0`

## W-001007 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_I2C1
- Explanation: CLK_I2C1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `262`
- New: `295`

### Rust Evidence

- Graph edges: `0`

## W-001008 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_I2C2
- Explanation: CLK_I2C2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `263`
- New: `296`

### Rust Evidence

- Graph edges: `0`

## W-001009 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_I2C3
- Explanation: CLK_I2C3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `264`
- New: `297`

### Rust Evidence

- Graph edges: `0`

## W-001010 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_I2C_HDMI
- Explanation: CLK_I2C_HDMI changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `269`
- New: `302`

### Rust Evidence

- Graph edges: `0`

## W-001011 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_I2S1
- Explanation: CLK_I2S1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `275`
- New: `307`

### Rust Evidence

- Graph edges: `0`

## W-001012 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_I2S2
- Explanation: CLK_I2S2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `276`
- New: `308`

### Rust Evidence

- Graph edges: `0`

## W-001013 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_JPEG
- Explanation: CLK_JPEG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `451`
- New: `270`

### Rust Evidence

- Graph edges: `0`

## W-001014 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_KEYIF
- Explanation: CLK_KEYIF changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `274`
- New: `347`

### Rust Evidence

- Graph edges: `0`

## W-001015 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_MCT
- Explanation: CLK_MCT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `315`
- New: `335`

### Rust Evidence

- Graph edges: `0`

## W-001016 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_MDMA0
- Explanation: CLK_MDMA0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `473`
- New: `346`

### Rust Evidence

- Graph edges: `0`

## W-001017 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_MDMA1
- Explanation: CLK_MDMA1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `442`
- New: `271`

### Rust Evidence

- Graph edges: `0`

## W-001018 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_MFC
- Explanation: CLK_MFC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `401`
- New: `266`

### Rust Evidence

- Graph edges: `0`

## W-001019 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_MIXER
- Explanation: CLK_MIXER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `431`
- New: `343`

### Rust Evidence

- Graph edges: `0`

## W-001020 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_MOUT_APLL
- Explanation: CLK_MOUT_APLL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `663`
- New: `1028`

### Rust Evidence

- Graph edges: `0`

## W-001021 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_MOUT_BPLL
- Explanation: CLK_MOUT_BPLL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `655`
- New: `9`

### Rust Evidence

- Graph edges: `0`

## W-001022 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_MOUT_EPLL
- Explanation: CLK_MOUT_EPLL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `657`
- New: `12`

### Rust Evidence

- Graph edges: `0`

## W-001023 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_MOUT_FSYS_BUS_USER
- Explanation: CLK_MOUT_FSYS_BUS_USER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `1`
- New: `4`

### Rust Evidence

- Graph edges: `0`

## W-001024 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_MOUT_G3D
- Explanation: CLK_MOUT_G3D changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `641`
- New: `394`

### Rust Evidence

- Graph edges: `0`

## W-001025 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_MOUT_HDMI
- Explanation: CLK_MOUT_HDMI changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `640`
- New: `1024`

### Rust Evidence

- Graph edges: `0`

## W-001026 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_MOUT_VPLL
- Explanation: CLK_MOUT_VPLL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `642`
- New: `27`

### Rust Evidence

- Graph edges: `0`

## W-001027 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_PCIE
- Explanation: CLK_PCIE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `115`
- New: `306`

### Rust Evidence

- Graph edges: `0`

## W-001028 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_PCM1
- Explanation: CLK_PCM1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `277`
- New: `309`

### Rust Evidence

- Graph edges: `0`

## W-001029 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_PCM2
- Explanation: CLK_PCM2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `278`
- New: `310`

### Rust Evidence

- Graph edges: `0`

## W-001030 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_PDMA0
- Explanation: CLK_PDMA0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `65`
- New: `275`

### Rust Evidence

- Graph edges: `0`

## W-001031 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_PDMA1
- Explanation: CLK_PDMA1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `64`
- New: `276`

### Rust Evidence

- Graph edges: `0`

## W-001032 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_PWM
- Explanation: CLK_PWM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `279`
- New: `311`

### Rust Evidence

- Graph edges: `0`

## W-001033 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_ROTATOR
- Explanation: CLK_ROTATOR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `441`
- New: `269`

### Rust Evidence

- Graph edges: `0`

## W-001034 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_RTC
- Explanation: CLK_RTC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `317`
- New: `337`

### Rust Evidence

- Graph edges: `0`

## W-001035 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_AUDIO0
- Explanation: CLK_SCLK_AUDIO0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `219`
- New: `138`

### Rust Evidence

- Graph edges: `0`

## W-001036 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_AUDIO1
- Explanation: CLK_SCLK_AUDIO1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `218`
- New: `151`

### Rust Evidence

- Graph edges: `0`

## W-001037 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_FIMD1
- Explanation: CLK_SCLK_FIMD1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `147`
- New: `133`

### Rust Evidence

- Graph edges: `0`

## W-001038 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_GSCL_WA
- Explanation: CLK_SCLK_GSCL_WA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `156`
- New: `131`

### Rust Evidence

- Graph edges: `0`

## W-001039 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_GSCL_WB
- Explanation: CLK_SCLK_GSCL_WB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `157`
- New: `132`

### Rust Evidence

- Graph edges: `0`

## W-001040 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_HDMI
- Explanation: CLK_SCLK_HDMI changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `143`
- New: `136`

### Rust Evidence

- Graph edges: `0`

## W-001041 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_HDMIPHY
- Explanation: CLK_SCLK_HDMIPHY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `158`
- New: `159`

### Rust Evidence

- Graph edges: `0`

## W-001042 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_I2S1
- Explanation: CLK_SCLK_I2S1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `14`
- New: `167`

### Rust Evidence

- Graph edges: `0`

## W-001043 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_I2S2
- Explanation: CLK_SCLK_I2S2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `139`
- New: `168`

### Rust Evidence

- Graph edges: `0`

## W-001044 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_JPEG
- Explanation: CLK_SCLK_JPEG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `29`
- New: `145`

### Rust Evidence

- Graph edges: `0`

## W-001045 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_MIPI1
- Explanation: CLK_SCLK_MIPI1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `146`
- New: `134`

### Rust Evidence

- Graph edges: `0`

## W-001046 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_MMC0
- Explanation: CLK_SCLK_MMC0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `139`

### Rust Evidence

- Graph edges: `0`

## W-001047 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_MMC1
- Explanation: CLK_SCLK_MMC1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `7`
- New: `140`

### Rust Evidence

- Graph edges: `0`

## W-001048 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_MMC2
- Explanation: CLK_SCLK_MMC2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `6`
- New: `141`

### Rust Evidence

- Graph edges: `0`

## W-001049 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_PCM1
- Explanation: CLK_SCLK_PCM1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `13`
- New: `165`

### Rust Evidence

- Graph edges: `0`

## W-001050 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_PCM2
- Explanation: CLK_SCLK_PCM2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `141`
- New: `166`

### Rust Evidence

- Graph edges: `0`

## W-001051 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_PIXEL
- Explanation: CLK_SCLK_PIXEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `144`
- New: `137`

### Rust Evidence

- Graph edges: `0`

## W-001052 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_PWM
- Explanation: CLK_SCLK_PWM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `58`
- New: `150`

### Rust Evidence

- Graph edges: `0`

## W-001053 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_PWM_ISP
- Explanation: CLK_SCLK_PWM_ISP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `513`
- New: `173 /* Exynos4x12 only */`

### Rust Evidence

- Graph edges: `0`

## W-001054 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_SLIMBUS
- Explanation: CLK_SCLK_SLIMBUS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `217`
- New: `162`

### Rust Evidence

- Graph edges: `0`

## W-001055 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_SPDIF
- Explanation: CLK_SCLK_SPDIF changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `12`
- New: `153`

### Rust Evidence

- Graph edges: `0`

## W-001056 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_SPI0
- Explanation: CLK_SCLK_SPI0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `7`
- New: `154`

### Rust Evidence

- Graph edges: `0`

## W-001057 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_SPI0_ISP
- Explanation: CLK_SCLK_SPI0_ISP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `511`
- New: `174 /* Exynos4x12 only */`

### Rust Evidence

- Graph edges: `0`

## W-001058 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_SPI1
- Explanation: CLK_SCLK_SPI1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `155`

### Rust Evidence

- Graph edges: `0`

## W-001059 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_SPI1_ISP
- Explanation: CLK_SCLK_SPI1_ISP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `512`
- New: `175 /* Exynos4x12 only */`

### Rust Evidence

- Graph edges: `0`

## W-001060 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_SPI2
- Explanation: CLK_SCLK_SPI2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `9`
- New: `156`

### Rust Evidence

- Graph edges: `0`

## W-001061 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_UART0
- Explanation: CLK_SCLK_UART0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `3`
- New: `146`

### Rust Evidence

- Graph edges: `0`

## W-001062 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_UART1
- Explanation: CLK_SCLK_UART1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `4`
- New: `147`

### Rust Evidence

- Graph edges: `0`

## W-001063 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_UART2
- Explanation: CLK_SCLK_UART2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `148`

### Rust Evidence

- Graph edges: `0`

## W-001064 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_UART3
- Explanation: CLK_SCLK_UART3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `6`
- New: `149`

### Rust Evidence

- Graph edges: `0`

## W-001065 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SCLK_UART_ISP
- Explanation: CLK_SCLK_UART_ISP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `510`
- New: `176 /* Exynos4x12 only */`

### Rust Evidence

- Graph edges: `0`

## W-001066 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SECKEY
- Explanation: CLK_SECKEY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `314`
- New: `148`

### Rust Evidence

- Graph edges: `0`

## W-001067 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SMMU_G2D
- Explanation: CLK_SMMU_G2D changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `503`
- New: `280`

### Rust Evidence

- Graph edges: `0`

## W-001068 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SMMU_GSCL0
- Explanation: CLK_SMMU_GSCL0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `461`
- New: `262`

### Rust Evidence

- Graph edges: `0`

## W-001069 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SMMU_GSCL1
- Explanation: CLK_SMMU_GSCL1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `462`
- New: `263`

### Rust Evidence

- Graph edges: `0`

## W-001070 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SMMU_JPEG
- Explanation: CLK_SMMU_JPEG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `453`
- New: `273`

### Rust Evidence

- Graph edges: `0`

## W-001071 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SMMU_MDMA0
- Explanation: CLK_SMMU_MDMA0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `504`
- New: `347`

### Rust Evidence

- Graph edges: `0`

## W-001072 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SMMU_MDMA1
- Explanation: CLK_SMMU_MDMA1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `444`
- New: `274`

### Rust Evidence

- Graph edges: `0`

## W-001073 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SMMU_MFCL
- Explanation: CLK_SMMU_MFCL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `402`
- New: `267`

### Rust Evidence

- Graph edges: `0`

## W-001074 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SMMU_MFCR
- Explanation: CLK_SMMU_MFCR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `403`
- New: `268`

### Rust Evidence

- Graph edges: `0`

## W-001075 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SMMU_ROTATOR
- Explanation: CLK_SMMU_ROTATOR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `443`
- New: `272`

### Rust Evidence

- Graph edges: `0`

## W-001076 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SPDIF
- Explanation: CLK_SPDIF changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `280`
- New: `312`

### Rust Evidence

- Graph edges: `0`

## W-001077 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SPI0
- Explanation: CLK_SPI0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `271`
- New: `304`

### Rust Evidence

- Graph edges: `0`

## W-001078 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SPI1
- Explanation: CLK_SPI1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `272`
- New: `305`

### Rust Evidence

- Graph edges: `0`

## W-001079 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SPI2
- Explanation: CLK_SPI2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `273`
- New: `306`

### Rust Evidence

- Graph edges: `0`

## W-001080 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SROMC
- Explanation: CLK_SROMC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `354`
- New: `284`

### Rust Evidence

- Graph edges: `0`

## W-001081 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SSS
- Explanation: CLK_SSS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `471`
- New: `348`

### Rust Evidence

- Graph edges: `0`

## W-001082 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_SYSREG
- Explanation: CLK_SYSREG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `302`
- New: `319`

### Rust Evidence

- Graph edges: `0`

## W-001083 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_TMU
- Explanation: CLK_TMU changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `318`
- New: `338`

### Rust Evidence

- Graph edges: `0`

## W-001084 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_TSADC
- Explanation: CLK_TSADC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `270`
- New: `326`

### Rust Evidence

- Graph edges: `0`

## W-001085 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_TSI
- Explanation: CLK_TSI changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `361`
- New: `296`

### Rust Evidence

- Graph edges: `0`

## W-001086 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_TZPC0
- Explanation: CLK_TZPC0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `303`
- New: `324`

### Rust Evidence

- Graph edges: `0`

## W-001087 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_TZPC1
- Explanation: CLK_TZPC1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `304`
- New: `325`

### Rust Evidence

- Graph edges: `0`

## W-001088 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_TZPC2
- Explanation: CLK_TZPC2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `305`
- New: `326`

### Rust Evidence

- Graph edges: `0`

## W-001089 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_TZPC3
- Explanation: CLK_TZPC3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `306`
- New: `327`

### Rust Evidence

- Graph edges: `0`

## W-001090 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_TZPC4
- Explanation: CLK_TZPC4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `307`
- New: `328`

### Rust Evidence

- Graph edges: `0`

## W-001091 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_TZPC5
- Explanation: CLK_TZPC5 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `308`
- New: `329`

### Rust Evidence

- Graph edges: `0`

## W-001092 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_TZPC6
- Explanation: CLK_TZPC6 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `309`
- New: `330`

### Rust Evidence

- Graph edges: `0`

## W-001093 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_TZPC7
- Explanation: CLK_TZPC7 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `310`
- New: `331`

### Rust Evidence

- Graph edges: `0`

## W-001094 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_TZPC8
- Explanation: CLK_TZPC8 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `311`
- New: `332`

### Rust Evidence

- Graph edges: `0`

## W-001095 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_TZPC9
- Explanation: CLK_TZPC9 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `312`
- New: `333`

### Rust Evidence

- Graph edges: `0`

## W-001096 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_UART0
- Explanation: CLK_UART0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `257`
- New: `289`

### Rust Evidence

- Graph edges: `0`

## W-001097 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_UART1
- Explanation: CLK_UART1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `258`
- New: `290`

### Rust Evidence

- Graph edges: `0`

## W-001098 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_UART2
- Explanation: CLK_UART2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `259`
- New: `291`

### Rust Evidence

- Graph edges: `0`

## W-001099 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_UART3
- Explanation: CLK_UART3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `260`
- New: `292`

### Rust Evidence

- Graph edges: `0`

## W-001100 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_WDT
- Explanation: CLK_WDT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `316`
- New: `336`

### Rust Evidence

- Graph edges: `0`

## W-001101 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: DATA_MAIN
- Explanation: DATA_MAIN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `.data .data.rel .data.rel.local`
- New: `.data .data.[0-9a-zA-Z_]* .data.rel.* .data..L* .data..compoundliteral* .data.$__unnamed_* .data.$L*`

### Rust Evidence

- Graph edges: `0`

## W-001102 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: DMA_BIT_MASK
- Explanation: DMA_BIT_MASK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `GENMASK_ULL(n - 1, 0)`
- New: `GENMASK_ULL((n) - 1, 0)`

### Rust Evidence

- Graph edges: `0`

## W-001105 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: RODATA_MAIN
- Explanation: RODATA_MAIN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `.rodata`
- New: `.rodata .rodata.[0-9a-zA-Z_]* .rodata..L*`

### Rust Evidence

- Graph edges: `0`

## W-001106 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SBSS_MAIN
- Explanation: SBSS_MAIN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `.sbss`
- New: `.sbss .sbss.[0-9a-zA-Z_]*`

### Rust Evidence

- Graph edges: `0`

## W-001107 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: SDATA_MAIN
- Explanation: SDATA_MAIN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `.sdata`
- New: `.sdata .sdata.[0-9a-zA-Z_]*`

### Rust Evidence

- Graph edges: `0`

## W-001108 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: TEXT_MAIN
- Explanation: TEXT_MAIN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `.text`
- New: `\`

### Rust Evidence

- Graph edges: `0`

## W-001111 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: VM_ARM64_BTI
- Explanation: VM_ARM64_BTI changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `VM_ARCH_1	/* BTI guarded page, a.k.a. GP bit */`
- New: `INIT_VM_FLAG(ARM64_BTI)`

### Rust Evidence

- Graph edges: `0`

## W-001116 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: VM_GROWSDOWN
- Explanation: VM_GROWSDOWN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000100	/* general info on the segment */`
- New: `INIT_VM_FLAG(GROWSDOWN)`

### Rust Evidence

- Graph edges: `0`

## W-001120 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: VM_LOCKED
- Explanation: VM_LOCKED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00002000`
- New: `INIT_VM_FLAG(LOCKED)`

### Rust Evidence

- Graph edges: `0`

## W-001122 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: VM_MAPPED_COPY
- Explanation: VM_MAPPED_COPY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `VM_ARCH_1	/* T if mapped copy of data (nommu mmap) */`
- New: `INIT_VM_FLAG(MAPPED_COPY)`

### Rust Evidence

- Graph edges: `0`

## W-001124 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: VM_MAYOVERLAY
- Explanation: VM_MAYOVERLAY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000200	/* nommu: R/O MAP_PRIVATE mapping that might overlay a file mapping */`
- New: `INIT_VM_FLAG(MAYOVERLAY)`

### Rust Evidence

- Graph edges: `0`

## W-001133 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: VM_PKEY_BIT0
- Explanation: VM_PKEY_BIT0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `VM_HIGH_ARCH_0`
- New: `INIT_VM_FLAG(PKEY_BIT0)`

### Rust Evidence

- Graph edges: `0`

## W-001134 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: VM_PKEY_BIT1
- Explanation: VM_PKEY_BIT1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `VM_HIGH_ARCH_1`
- New: `INIT_VM_FLAG(PKEY_BIT1)`

### Rust Evidence

- Graph edges: `0`

## W-001135 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: VM_PKEY_BIT2
- Explanation: VM_PKEY_BIT2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `VM_HIGH_ARCH_2`
- New: `INIT_VM_FLAG(PKEY_BIT2)`

### Rust Evidence

- Graph edges: `0`

## W-001136 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: VM_PKEY_BIT3
- Explanation: VM_PKEY_BIT3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0`
- New: `VM_NONE`

### Rust Evidence

- Graph edges: `0`

## W-001138 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: VM_PKEY_SHIFT
- Explanation: VM_PKEY_SHIFT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `VM_HIGH_ARCH_BIT_0`
- New: `((__force int)VMA_HIGH_ARCH_0_BIT)`

### Rust Evidence

- Graph edges: `0`

## W-001139 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: VM_RAND_READ
- Explanation: VM_RAND_READ changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00010000	/* App will not benefit from clustered reads */`
- New: `INIT_VM_FLAG(RAND_READ)`

### Rust Evidence

- Graph edges: `0`

## W-001141 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: VM_SAO
- Explanation: VM_SAO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `VM_ARCH_1	/* Strong Access Ordering (powerpc) */`
- New: `INIT_VM_FLAG(SAO)`

### Rust Evidence

- Graph edges: `0`

## W-001142 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: VM_SEQ_READ
- Explanation: VM_SEQ_READ changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00008000	/* App will access data sequentially */`
- New: `INIT_VM_FLAG(SEQ_READ)`

### Rust Evidence

- Graph edges: `0`

## W-001145 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: VM_SPARC_ADI
- Explanation: VM_SPARC_ADI changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `VM_ARCH_1	/* Uses ADI tag for access control */`
- New: `INIT_VM_FLAG(SPARC_ADI)`

### Rust Evidence

- Graph edges: `0`

## W-001149 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: VM_UFFD_MISSING
- Explanation: VM_UFFD_MISSING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0`
- New: `VM_NONE`

### Rust Evidence

- Graph edges: `0`

## W-001150 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: VM_UFFD_WP
- Explanation: VM_UFFD_WP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00001000	/* wrprotect pages tracking */`
- New: `INIT_VM_FLAG(UFFD_WP)`

### Rust Evidence

- Graph edges: `0`
