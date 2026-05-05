# BindDrift Ranked Warnings

## W-000346 SignatureDrift

- Risk: High
- Score: 14.6
- Symbol: refcount_dec
- Explanation: refcount_dec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `20`

## W-000362 SignatureDrift

- Risk: High
- Score: 14.6
- Symbol: sha256
- Explanation: sha256 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `20`

## W-000370 SignatureDrift

- Risk: High
- Score: 14.0
- Symbol: sha512
- Explanation: sha512 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `17`

## W-000422 FieldDrift

- Risk: High
- Score: 13.6
- Symbol: drm_device
- Explanation: drm_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'if_version', 'type': 'ffi::c_int'}, {'name': 'ref_', 'type': 'kref'}, {'name': 'dev', 'type': '*mut device'}, {'name': 'dma_dev', 'type': '*mut device'}, {'name': 'managed', 'type': 'drm_device__bindgen_ty_1'}, {'name': 'driver', 'type': '*const drm_driver'}, {'name': 'dev_private', 'type': '*mut ffi::c_void'}, {'name': 'primary', 'type': '*mut drm_minor'}, {'name': 'render', 'type': '*mut drm_minor'}, {'name': 'accel', 'type': '*mut drm_minor'}, {'name': 'registered', 'type': 'bool_'}, {'name': 'master', 'type': '*mut drm_master'}, {'name': 'driver_features', 'type': 'u32_'}, {'name': 'unplugged', 'type': 'bool_'}, {'name': 'anon_inode', 'type': '*mut inode'}, {'name': 'unique', 'type': '*mut ffi::c_char'}, {'name': 'struct_mutex', 'type': 'mutex'}, {'name': 'master_mutex', 'type': 'mutex'}, {'name': 'open_count', 'type': 'atomic_t'}, {'name': 'filelist_mutex', 'type': 'mutex'}, {'name': 'filelist', 'type': 'list_head'}, {'name': 'filelist_internal', 'type': 'list_head'}, {'name': 'clientlist_mutex', 'type': 'mutex'}, {'name': 'clientlist', 'type': 'list_head'}, {'name': 'vblank_disable_immediate', 'type': 'bool_'}, {'name': 'vblank', 'type': '*mut drm_vblank_crtc'}, {'name': 'vblank_time_lock', 'type': 'spinlock_t'}, {'name': 'vbl_lock', 'type': 'spinlock_t'}, {'name': 'max_vblank_count', 'type': 'u32_'}, {'name': 'vblank_event_list', 'type': 'list_head'}, {'name': 'event_lock', 'type': 'spinlock_t'}, {'name': 'num_crtcs', 'type': 'ffi::c_uint'}, {'name': 'mode_config', 'type': 'drm_mode_config'}, {'name': 'object_name_lock', 'type': 'mutex'}, {'name': 'object_name_idr', 'type': 'idr'}, {'name': 'vma_offset_manager', 'type': '*mut drm_vma_offset_manager'}, {'name': 'vram_mm', 'type': '*mut drm_vram_mm'}, {'name': 'switch_power_state', 'type': 'switch_power_state'}, {'name': 'fb_helper', 'type': '*mut drm_fb_helper'}, {'name': 'debugfs_root', 'type': '*mut dentry'}]`
- New: `[{'name': 'if_version', 'type': 'ffi::c_int'}, {'name': 'ref_', 'type': 'kref'}, {'name': 'dev', 'type': '*mut device'}, {'name': 'dma_dev', 'type': '*mut device'}, {'name': 'managed', 'type': 'drm_device__bindgen_ty_1'}, {'name': 'driver', 'type': '*const drm_driver'}, {'name': 'dev_private', 'type': '*mut ffi::c_void'}, {'name': 'primary', 'type': '*mut drm_minor'}, {'name': 'render', 'type': '*mut drm_minor'}, {'name': 'accel', 'type': '*mut drm_minor'}, {'name': 'registered', 'type': 'bool_'}, {'name': 'master', 'type': '*mut drm_master'}, {'name': 'driver_features', 'type': 'u32_'}, {'name': 'unplugged', 'type': 'bool_'}, {'name': 'anon_inode', 'type': '*mut inode'}, {'name': 'unique', 'type': '*mut ffi::c_char'}, {'name': 'master_mutex', 'type': 'mutex'}, {'name': 'open_count', 'type': 'atomic_t'}, {'name': 'filelist_mutex', 'type': 'mutex'}, {'name': 'filelist', 'type': 'list_head'}, {'name': 'filelist_internal', 'type': 'list_head'}, {'name': 'clientlist_mutex', 'type': 'mutex'}, {'name': 'clientlist', 'type': 'list_head'}, {'name': 'vblank_disable_immediate', 'type': 'bool_'}, {'name': 'vblank', 'type': '*mut drm_vblank_crtc'}, {'name': 'vblank_time_lock', 'type': 'spinlock_t'}, {'name': 'vbl_lock', 'type': 'spinlock_t'}, {'name': 'max_vblank_count', 'type': 'u32_'}, {'name': 'vblank_event_list', 'type': 'list_head'}, {'name': 'event_lock', 'type': 'spinlock_t'}, {'name': 'num_crtcs', 'type': 'ffi::c_uint'}, {'name': 'mode_config', 'type': 'drm_mode_config'}, {'name': 'object_name_lock', 'type': 'mutex'}, {'name': 'object_name_idr', 'type': 'idr'}, {'name': 'vma_offset_manager', 'type': '*mut drm_vma_offset_manager'}, {'name': 'vram_mm', 'type': '*mut drm_vram_mm'}, {'name': 'switch_power_state', 'type': 'switch_power_state'}, {'name': 'fb_helper', 'type': '*mut drm_fb_helper'}, {'name': 'debugfs_root', 'type': '*mut dentry'}]`

### Rust Evidence

- Graph edges: `50`

## W-000259 SignatureDrift

- Risk: High
- Score: 13.4
- Symbol: devm_regulator_get_enable
- Explanation: devm_regulator_get_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `14`

## W-000359 SignatureDrift

- Risk: High
- Score: 13.4
- Symbol: sha224
- Explanation: sha224 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `14`

## W-000367 SignatureDrift

- Risk: High
- Score: 13.4
- Symbol: sha384
- Explanation: sha384 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `14`

## W-000712 NullabilityDrift

- Risk: High
- Score: 13.3
- Symbol: debugfs_create_dir
- Explanation: debugfs_create_dir has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE', 'ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.18/include/linux/debugfs.h:303 `return ERR_PTR(-ENODEV);`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.18/rust/kernel/debugfs/entry.rs:40 `Entry<::dynamic_dir` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.18/rust/kernel/debugfs/entry.rs:94 `Entry<::dir` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.18/rust/kernel/debugfs/entry.rs:36 `// SAFETY: The invariants of this function's arguments ensure the safety of this call.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.18/rust/kernel/debugfs/entry.rs:89 `// SAFETY: The invariants of this function's arguments ensure the safety of this call.`

## W-000260 SignatureDrift

- Risk: High
- Score: 12.8
- Symbol: devm_regulator_get_enable_optional
- Explanation: devm_regulator_get_enable_optional changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `11`

## W-000347 SignatureDrift

- Risk: High
- Score: 12.8
- Symbol: refcount_set
- Explanation: refcount_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `11`

## W-000025 SignatureDrift

- Risk: High
- Score: 12.6
- Symbol: atomic64_add
- Explanation: atomic64_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `10`

## W-000110 SignatureDrift

- Risk: High
- Score: 12.6
- Symbol: atomic_add
- Explanation: atomic_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `10`

## W-000202 SignatureDrift

- Risk: High
- Score: 12.6
- Symbol: clear_bit
- Explanation: clear_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `10`

## W-000406 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: bio
- Explanation: bio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'bi_next', 'type': '*mut bio'}, {'name': 'bi_bdev', 'type': '*mut block_device'}, {'name': 'bi_opf', 'type': 'blk_opf_t'}, {'name': 'bi_flags', 'type': 'ffi::c_ushort'}, {'name': 'bi_ioprio', 'type': 'ffi::c_ushort'}, {'name': 'bi_write_hint', 'type': 'rw_hint'}, {'name': 'bi_write_stream', 'type': 'u8_'}, {'name': 'bi_status', 'type': 'blk_status_t'}, {'name': '__bi_remaining', 'type': 'atomic_t'}, {'name': 'bi_iter', 'type': 'bvec_iter'}, {'name': '__bindgen_anon_1', 'type': 'bio__bindgen_ty_1'}, {'name': 'bi_end_io', 'type': 'bio_end_io_t'}, {'name': 'bi_private', 'type': '*mut ffi::c_void'}, {'name': 'bi_blkg', 'type': '*mut blkcg_gq'}, {'name': 'bi_issue', 'type': 'bio_issue'}, {'name': 'bi_iocost_cost', 'type': 'u64_'}, {'name': 'bi_vcnt', 'type': 'ffi::c_ushort'}, {'name': 'bi_max_vecs', 'type': 'ffi::c_ushort'}, {'name': '__bi_cnt', 'type': 'atomic_t'}, {'name': 'bi_io_vec', 'type': '*mut bio_vec'}, {'name': 'bi_pool', 'type': '*mut bio_set'}, {'name': 'bi_inline_vecs', 'type': '__IncompleteArrayField<bio_vec>'}]`
- New: `[{'name': 'bi_next', 'type': '*mut bio'}, {'name': 'bi_bdev', 'type': '*mut block_device'}, {'name': 'bi_opf', 'type': 'blk_opf_t'}, {'name': 'bi_flags', 'type': 'ffi::c_ushort'}, {'name': 'bi_ioprio', 'type': 'ffi::c_ushort'}, {'name': 'bi_write_hint', 'type': 'rw_hint'}, {'name': 'bi_write_stream', 'type': 'u8_'}, {'name': 'bi_status', 'type': 'blk_status_t'}, {'name': '__bi_remaining', 'type': 'atomic_t'}, {'name': 'bi_iter', 'type': 'bvec_iter'}, {'name': '__bindgen_anon_1', 'type': 'bio__bindgen_ty_1'}, {'name': 'bi_end_io', 'type': 'bio_end_io_t'}, {'name': 'bi_private', 'type': '*mut ffi::c_void'}, {'name': 'bi_blkg', 'type': '*mut blkcg_gq'}, {'name': 'issue_time_ns', 'type': 'u64_'}, {'name': 'bi_iocost_cost', 'type': 'u64_'}, {'name': 'bi_vcnt', 'type': 'ffi::c_ushort'}, {'name': 'bi_max_vecs', 'type': 'ffi::c_ushort'}, {'name': '__bi_cnt', 'type': 'atomic_t'}, {'name': 'bi_io_vec', 'type': '*mut bio_vec'}, {'name': 'bi_pool', 'type': '*mut bio_set'}]`

### Rust Evidence

- Graph edges: `50`

## W-000409 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: bpf_attr__bindgen_ty_1
- Explanation: bpf_attr__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'map_type', 'type': '__u32'}, {'name': 'key_size', 'type': '__u32'}, {'name': 'value_size', 'type': '__u32'}, {'name': 'max_entries', 'type': '__u32'}, {'name': 'map_flags', 'type': '__u32'}, {'name': 'inner_map_fd', 'type': '__u32'}, {'name': 'numa_node', 'type': '__u32'}, {'name': 'map_name', 'type': '[ffi::c_char; 16usize]'}, {'name': 'map_ifindex', 'type': '__u32'}, {'name': 'btf_fd', 'type': '__u32'}, {'name': 'btf_key_type_id', 'type': '__u32'}, {'name': 'btf_value_type_id', 'type': '__u32'}, {'name': 'btf_vmlinux_value_type_id', 'type': '__u32'}, {'name': 'map_extra', 'type': '__u64'}, {'name': 'value_type_btf_obj_fd', 'type': '__s32'}, {'name': 'map_token_fd', 'type': '__s32'}]`
- New: `[{'name': 'map_type', 'type': '__u32'}, {'name': 'key_size', 'type': '__u32'}, {'name': 'value_size', 'type': '__u32'}, {'name': 'max_entries', 'type': '__u32'}, {'name': 'map_flags', 'type': '__u32'}, {'name': 'inner_map_fd', 'type': '__u32'}, {'name': 'numa_node', 'type': '__u32'}, {'name': 'map_name', 'type': '[ffi::c_char; 16usize]'}, {'name': 'map_ifindex', 'type': '__u32'}, {'name': 'btf_fd', 'type': '__u32'}, {'name': 'btf_key_type_id', 'type': '__u32'}, {'name': 'btf_value_type_id', 'type': '__u32'}, {'name': 'btf_vmlinux_value_type_id', 'type': '__u32'}, {'name': 'map_extra', 'type': '__u64'}, {'name': 'value_type_btf_obj_fd', 'type': '__s32'}, {'name': 'map_token_fd', 'type': '__s32'}, {'name': 'excl_prog_hash', 'type': '__u64'}, {'name': 'excl_prog_hash_size', 'type': '__u32'}]`

### Rust Evidence

- Graph edges: `20`

## W-000411 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: bpf_map
- Explanation: bpf_map changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'ops', 'type': '*const bpf_map_ops'}, {'name': 'inner_map_meta', 'type': '*mut bpf_map'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'map_type', 'type': 'bpf_map_type'}, {'name': 'key_size', 'type': 'u32_'}, {'name': 'value_size', 'type': 'u32_'}, {'name': 'max_entries', 'type': 'u32_'}, {'name': 'map_extra', 'type': 'u64_'}, {'name': 'map_flags', 'type': 'u32_'}, {'name': 'id', 'type': 'u32_'}, {'name': 'record', 'type': '*mut btf_record'}, {'name': 'numa_node', 'type': 'ffi::c_int'}, {'name': 'btf_key_type_id', 'type': 'u32_'}, {'name': 'btf_value_type_id', 'type': 'u32_'}, {'name': 'btf_vmlinux_value_type_id', 'type': 'u32_'}, {'name': 'btf', 'type': '*mut btf'}, {'name': 'name', 'type': '[ffi::c_char; 16usize]'}, {'name': 'freeze_mutex', 'type': 'mutex'}, {'name': 'refcnt', 'type': 'atomic64_t'}, {'name': 'usercnt', 'type': 'atomic64_t'}, {'name': '__bindgen_anon_1', 'type': 'bpf_map__bindgen_ty_1'}, {'name': 'writecnt', 'type': 'atomic64_t'}, {'name': 'owner_lock', 'type': 'spinlock_t'}, {'name': 'owner', 'type': '*mut bpf_map_owner'}, {'name': 'bypass_spec_v1', 'type': 'bool_'}, {'name': 'frozen', 'type': 'bool_'}, {'name': 'free_after_mult_rcu_gp', 'type': 'bool_'}, {'name': 'free_after_rcu_gp', 'type': 'bool_'}, {'name': 'sleepable_refcnt', 'type': 'atomic64_t'}, {'name': 'elem_count', 'type': '*mut s64'}, {'name': 'cookie', 'type': 'u64_'}]`
- New: `[{'name': 'sha', 'type': '[u8_; 32usize]'}, {'name': 'ops', 'type': '*const bpf_map_ops'}, {'name': 'inner_map_meta', 'type': '*mut bpf_map'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'map_type', 'type': 'bpf_map_type'}, {'name': 'key_size', 'type': 'u32_'}, {'name': 'value_size', 'type': 'u32_'}, {'name': 'max_entries', 'type': 'u32_'}, {'name': 'map_extra', 'type': 'u64_'}, {'name': 'map_flags', 'type': 'u32_'}, {'name': 'id', 'type': 'u32_'}, {'name': 'record', 'type': '*mut btf_record'}, {'name': 'numa_node', 'type': 'ffi::c_int'}, {'name': 'btf_key_type_id', 'type': 'u32_'}, {'name': 'btf_value_type_id', 'type': 'u32_'}, {'name': 'btf_vmlinux_value_type_id', 'type': 'u32_'}, {'name': 'btf', 'type': '*mut btf'}, {'name': 'name', 'type': '[ffi::c_char; 16usize]'}, {'name': 'freeze_mutex', 'type': 'mutex'}, {'name': 'refcnt', 'type': 'atomic64_t'}, {'name': 'usercnt', 'type': 'atomic64_t'}, {'name': '__bindgen_anon_1', 'type': 'bpf_map__bindgen_ty_1'}, {'name': 'writecnt', 'type': 'atomic64_t'}, {'name': 'owner_lock', 'type': 'spinlock_t'}, {'name': 'owner', 'type': '*mut bpf_map_owner'}, {'name': 'bypass_spec_v1', 'type': 'bool_'}, {'name': 'frozen', 'type': 'bool_'}, {'name': 'free_after_mult_rcu_gp', 'type': 'bool_'}, {'name': 'free_after_rcu_gp', 'type': 'bool_'}, {'name': 'sleepable_refcnt', 'type': 'atomic64_t'}, {'name': 'elem_count', 'type': '*mut s64'}, {'name': 'cookie', 'type': 'u64_'}, {'name': 'excl_prog_sha', 'type': '*mut ffi::c_char'}]`

### Rust Evidence

- Graph edges: `48`

## W-000415 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: bpf_prog
- Explanation: bpf_prog changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'pages', 'type': 'u16_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'type_', 'type': 'bpf_prog_type'}, {'name': 'expected_attach_type', 'type': 'bpf_attach_type'}, {'name': 'len', 'type': 'u32_'}, {'name': 'jited_len', 'type': 'u32_'}, {'name': 'tag', 'type': '[u8_; 8usize]'}, {'name': 'stats', 'type': '*mut bpf_prog_stats'}, {'name': 'active', 'type': '*mut ffi::c_int'}, {'name': 'bpf_func', 'type': '::core::option::Option<'}, {'name': 'aux', 'type': '*mut bpf_prog_aux'}, {'name': 'orig_prog', 'type': '*mut sock_fprog_kern'}, {'name': '__bindgen_anon_1', 'type': 'bpf_prog__bindgen_ty_1'}]`
- New: `[{'name': 'pages', 'type': 'u16_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 2usize]>'}, {'name': 'type_', 'type': 'bpf_prog_type'}, {'name': 'expected_attach_type', 'type': 'bpf_attach_type'}, {'name': 'len', 'type': 'u32_'}, {'name': 'jited_len', 'type': 'u32_'}, {'name': '__bindgen_anon_1', 'type': 'bpf_prog__bindgen_ty_1'}, {'name': 'stats', 'type': '*mut bpf_prog_stats'}, {'name': 'active', 'type': '*mut ffi::c_int'}, {'name': 'bpf_func', 'type': '::core::option::Option<'}, {'name': 'aux', 'type': '*mut bpf_prog_aux'}, {'name': 'orig_prog', 'type': '*mut sock_fprog_kern'}, {'name': '__bindgen_anon_2', 'type': 'bpf_prog__bindgen_ty_2'}]`

### Rust Evidence

- Graph edges: `50`

## W-000421 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: dentry
- Explanation: dentry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'd_flags', 'type': 'ffi::c_uint'}, {'name': 'd_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'd_hash', 'type': 'hlist_bl_node'}, {'name': 'd_parent', 'type': '*mut dentry'}, {'name': 'd_name', 'type': 'qstr'}, {'name': 'd_inode', 'type': '*mut inode'}, {'name': 'd_shortname', 'type': 'shortname_store'}, {'name': 'd_op', 'type': '*const dentry_operations'}, {'name': 'd_sb', 'type': '*mut super_block'}, {'name': 'd_time', 'type': 'ffi::c_ulong'}, {'name': 'd_fsdata', 'type': '*mut ffi::c_void'}, {'name': 'd_lockref', 'type': 'lockref'}, {'name': '__bindgen_anon_1', 'type': 'dentry__bindgen_ty_1'}, {'name': 'd_sib', 'type': 'hlist_node'}, {'name': 'd_children', 'type': 'hlist_head'}, {'name': 'd_u', 'type': 'dentry__bindgen_ty_2'}]`
- New: `[{'name': 'd_flags', 'type': 'ffi::c_uint'}, {'name': 'd_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'd_hash', 'type': 'hlist_bl_node'}, {'name': 'd_parent', 'type': '*mut dentry'}, {'name': '__bindgen_anon_1', 'type': 'dentry__bindgen_ty_1'}, {'name': 'd_inode', 'type': '*mut inode'}, {'name': 'd_shortname', 'type': 'shortname_store'}, {'name': 'd_op', 'type': '*const dentry_operations'}, {'name': 'd_sb', 'type': '*mut super_block'}, {'name': 'd_time', 'type': 'ffi::c_ulong'}, {'name': 'd_fsdata', 'type': '*mut ffi::c_void'}, {'name': 'd_lockref', 'type': 'lockref'}, {'name': '__bindgen_anon_2', 'type': 'dentry__bindgen_ty_2'}, {'name': 'd_sib', 'type': 'hlist_node'}, {'name': 'd_children', 'type': 'hlist_head'}, {'name': 'd_u', 'type': 'dentry__bindgen_ty_3'}]`

### Rust Evidence

- Graph edges: `50`

## W-000424 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: file
- Explanation: file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'f_lock', 'type': 'spinlock_t'}, {'name': 'f_mode', 'type': 'fmode_t'}, {'name': 'f_op', 'type': '*const file_operations'}, {'name': 'f_mapping', 'type': '*mut address_space'}, {'name': 'private_data', 'type': '*mut ffi::c_void'}, {'name': 'f_inode', 'type': '*mut inode'}, {'name': 'f_flags', 'type': 'ffi::c_uint'}, {'name': 'f_iocb_flags', 'type': 'ffi::c_uint'}, {'name': 'f_cred', 'type': '*const cred'}, {'name': 'f_owner', 'type': '*mut fown_struct'}, {'name': 'f_path', 'type': 'path'}, {'name': '__bindgen_anon_1', 'type': 'file__bindgen_ty_1'}, {'name': 'f_pos', 'type': 'loff_t'}, {'name': 'f_security', 'type': '*mut ffi::c_void'}, {'name': 'f_wb_err', 'type': 'errseq_t'}, {'name': 'f_sb_err', 'type': 'errseq_t'}, {'name': 'f_ep', 'type': '*mut hlist_head'}, {'name': '__bindgen_anon_2', 'type': 'file__bindgen_ty_2'}, {'name': 'f_ref', 'type': 'file_ref_t'}]`
- New: `[{'name': 'f_lock', 'type': 'spinlock_t'}, {'name': 'f_mode', 'type': 'fmode_t'}, {'name': 'f_op', 'type': '*const file_operations'}, {'name': 'f_mapping', 'type': '*mut address_space'}, {'name': 'private_data', 'type': '*mut ffi::c_void'}, {'name': 'f_inode', 'type': '*mut inode'}, {'name': 'f_flags', 'type': 'ffi::c_uint'}, {'name': 'f_iocb_flags', 'type': 'ffi::c_uint'}, {'name': 'f_cred', 'type': '*const cred'}, {'name': 'f_owner', 'type': '*mut fown_struct'}, {'name': '__bindgen_anon_1', 'type': 'file__bindgen_ty_1'}, {'name': '__bindgen_anon_2', 'type': 'file__bindgen_ty_2'}, {'name': 'f_pos', 'type': 'loff_t'}, {'name': 'f_security', 'type': '*mut ffi::c_void'}, {'name': 'f_wb_err', 'type': 'errseq_t'}, {'name': 'f_sb_err', 'type': 'errseq_t'}, {'name': 'f_ep', 'type': '*mut hlist_head'}, {'name': '__bindgen_anon_3', 'type': 'file__bindgen_ty_3'}, {'name': 'f_ref', 'type': 'file_ref_t'}]`

### Rust Evidence

- Graph edges: `50`

## W-000429 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: inode
- Explanation: inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'i_mode', 'type': 'umode_t'}, {'name': 'i_opflags', 'type': 'ffi::c_ushort'}, {'name': 'i_uid', 'type': 'kuid_t'}, {'name': 'i_gid', 'type': 'kgid_t'}, {'name': 'i_flags', 'type': 'ffi::c_uint'}, {'name': 'i_acl', 'type': '*mut posix_acl'}, {'name': 'i_default_acl', 'type': '*mut posix_acl'}, {'name': 'i_op', 'type': '*const inode_operations'}, {'name': 'i_sb', 'type': '*mut super_block'}, {'name': 'i_mapping', 'type': '*mut address_space'}, {'name': 'i_security', 'type': '*mut ffi::c_void'}, {'name': 'i_ino', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'inode__bindgen_ty_1'}, {'name': 'i_rdev', 'type': 'dev_t'}, {'name': 'i_size', 'type': 'loff_t'}, {'name': 'i_atime_sec', 'type': 'time64_t'}, {'name': 'i_mtime_sec', 'type': 'time64_t'}, {'name': 'i_ctime_sec', 'type': 'time64_t'}, {'name': 'i_atime_nsec', 'type': 'u32_'}, {'name': 'i_mtime_nsec', 'type': 'u32_'}, {'name': 'i_ctime_nsec', 'type': 'u32_'}, {'name': 'i_generation', 'type': 'u32_'}, {'name': 'i_lock', 'type': 'spinlock_t'}, {'name': 'i_bytes', 'type': 'ffi::c_ushort'}, {'name': 'i_blkbits', 'type': 'u8_'}, {'name': 'i_write_hint', 'type': 'rw_hint'}, {'name': 'i_blocks', 'type': 'blkcnt_t'}, {'name': 'i_state', 'type': 'u32_'}, {'name': 'i_rwsem', 'type': 'rw_semaphore'}, {'name': 'dirtied_when', 'type': 'ffi::c_ulong'}, {'name': 'dirtied_time_when', 'type': 'ffi::c_ulong'}, {'name': 'i_hash', 'type': 'hlist_node'}, {'name': 'i_io_list', 'type': 'list_head'}, {'name': 'i_lru', 'type': 'list_head'}, {'name': 'i_sb_list', 'type': 'list_head'}, {'name': 'i_wb_list', 'type': 'list_head'}, {'name': '__bindgen_anon_2', 'type': 'inode__bindgen_ty_2'}, {'name': 'i_version', 'type': 'atomic64_t'}, {'name': 'i_sequence', 'type': 'atomic64_t'}, {'name': 'i_count', 'type': 'atomic_t'}, {'name': 'i_dio_count', 'type': 'atomic_t'}, {'name': 'i_writecount', 'type': 'atomic_t'}, {'name': 'i_readcount', 'type': 'atomic_t'}, {'name': '__bindgen_anon_3', 'type': 'inode__bindgen_ty_3'}, {'name': 'i_flctx', 'type': '*mut file_lock_context'}, {'name': 'i_data', 'type': 'address_space'}, {'name': '__bindgen_anon_4', 'type': 'inode__bindgen_ty_4'}, {'name': '__bindgen_anon_5', 'type': 'inode__bindgen_ty_5'}, {'name': 'i_fsnotify_mask', 'type': '__u32'}, {'name': 'i_fsnotify_marks', 'type': '*mut fsnotify_mark_connector'}, {'name': 'i_private', 'type': '*mut ffi::c_void'}]`
- New: `[{'name': 'i_mode', 'type': 'umode_t'}, {'name': 'i_opflags', 'type': 'ffi::c_ushort'}, {'name': 'i_uid', 'type': 'kuid_t'}, {'name': 'i_gid', 'type': 'kgid_t'}, {'name': 'i_flags', 'type': 'ffi::c_uint'}, {'name': 'i_acl', 'type': '*mut posix_acl'}, {'name': 'i_default_acl', 'type': '*mut posix_acl'}, {'name': 'i_op', 'type': '*const inode_operations'}, {'name': 'i_sb', 'type': '*mut super_block'}, {'name': 'i_mapping', 'type': '*mut address_space'}, {'name': 'i_security', 'type': '*mut ffi::c_void'}, {'name': 'i_ino', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'inode__bindgen_ty_1'}, {'name': 'i_rdev', 'type': 'dev_t'}, {'name': 'i_size', 'type': 'loff_t'}, {'name': 'i_atime_sec', 'type': 'time64_t'}, {'name': 'i_mtime_sec', 'type': 'time64_t'}, {'name': 'i_ctime_sec', 'type': 'time64_t'}, {'name': 'i_atime_nsec', 'type': 'u32_'}, {'name': 'i_mtime_nsec', 'type': 'u32_'}, {'name': 'i_ctime_nsec', 'type': 'u32_'}, {'name': 'i_generation', 'type': 'u32_'}, {'name': 'i_lock', 'type': 'spinlock_t'}, {'name': 'i_bytes', 'type': 'ffi::c_ushort'}, {'name': 'i_blkbits', 'type': 'u8_'}, {'name': 'i_write_hint', 'type': 'rw_hint'}, {'name': 'i_blocks', 'type': 'blkcnt_t'}, {'name': 'i_state', 'type': 'inode_state_flags_t'}, {'name': 'i_rwsem', 'type': 'rw_semaphore'}, {'name': 'dirtied_when', 'type': 'ffi::c_ulong'}, {'name': 'dirtied_time_when', 'type': 'ffi::c_ulong'}, {'name': 'i_hash', 'type': 'hlist_node'}, {'name': 'i_io_list', 'type': 'list_head'}, {'name': 'i_lru', 'type': 'list_head'}, {'name': 'i_sb_list', 'type': 'list_head'}, {'name': 'i_wb_list', 'type': 'list_head'}, {'name': '__bindgen_anon_2', 'type': 'inode__bindgen_ty_2'}, {'name': 'i_version', 'type': 'atomic64_t'}, {'name': 'i_sequence', 'type': 'atomic64_t'}, {'name': 'i_count', 'type': 'atomic_t'}, {'name': 'i_dio_count', 'type': 'atomic_t'}, {'name': 'i_writecount', 'type': 'atomic_t'}, {'name': 'i_readcount', 'type': 'atomic_t'}, {'name': '__bindgen_anon_3', 'type': 'inode__bindgen_ty_3'}, {'name': 'i_flctx', 'type': '*mut file_lock_context'}, {'name': 'i_data', 'type': 'address_space'}, {'name': '__bindgen_anon_4', 'type': 'inode__bindgen_ty_4'}, {'name': '__bindgen_anon_5', 'type': 'inode__bindgen_ty_5'}, {'name': 'i_fsnotify_mask', 'type': '__u32'}, {'name': 'i_fsnotify_marks', 'type': '*mut fsnotify_mark_connector'}, {'name': 'i_private', 'type': '*mut ffi::c_void'}]`

### Rust Evidence

- Graph edges: `50`

## W-000431 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: kunit
- Explanation: kunit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'log', 'type': '*mut string_stream'}, {'name': 'try_catch', 'type': 'kunit_try_catch'}, {'name': 'param_value', 'type': '*const ffi::c_void'}, {'name': 'param_index', 'type': 'ffi::c_int'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'status', 'type': 'kunit_status'}, {'name': 'resources', 'type': 'list_head'}, {'name': 'status_comment', 'type': '[ffi::c_char; 256usize]'}, {'name': 'last_seen', 'type': 'kunit_loc'}]`
- New: `[{'name': 'priv_', 'type': '*mut ffi::c_void'}, {'name': 'parent', 'type': '*mut kunit'}, {'name': 'params_array', 'type': 'kunit_params'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'log', 'type': '*mut string_stream'}, {'name': 'try_catch', 'type': 'kunit_try_catch'}, {'name': 'param_value', 'type': '*const ffi::c_void'}, {'name': 'param_index', 'type': 'ffi::c_int'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'status', 'type': 'kunit_status'}, {'name': 'resources', 'type': 'list_head'}, {'name': 'status_comment', 'type': '[ffi::c_char; 256usize]'}, {'name': 'last_seen', 'type': 'kunit_loc'}]`

### Rust Evidence

- Graph edges: `50`

## W-000432 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: kunit_case
- Explanation: kunit_case changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'run_case', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'generate_params', 'type': '::core::option::Option<'}, {'name': 'attr', 'type': 'kunit_attributes'}, {'name': 'status', 'type': 'kunit_status'}, {'name': 'module_name', 'type': '*mut ffi::c_char'}, {'name': 'log', 'type': '*mut string_stream'}]`
- New: `[{'name': 'run_case', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'generate_params', 'type': '::core::option::Option<'}, {'name': 'attr', 'type': 'kunit_attributes'}, {'name': 'param_init', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit) -> ffi::c_int>'}, {'name': 'param_exit', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'status', 'type': 'kunit_status'}, {'name': 'module_name', 'type': '*mut ffi::c_char'}, {'name': 'log', 'type': '*mut string_stream'}]`

### Rust Evidence

- Graph edges: `34`

## W-000437 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: page
- Explanation: page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'page__bindgen_ty_1'}, {'name': '__bindgen_anon_2', 'type': 'page__bindgen_ty_2'}, {'name': '_refcount', 'type': 'atomic_t'}]`
- New: `[{'name': 'flags', 'type': 'memdesc_flags_t'}, {'name': '__bindgen_anon_1', 'type': 'page__bindgen_ty_1'}, {'name': '__bindgen_anon_2', 'type': 'page__bindgen_ty_2'}, {'name': '_refcount', 'type': 'atomic_t'}]`

### Rust Evidence

- Graph edges: `50`

## W-000126 SignatureDrift

- Risk: High
- Score: 12.4
- Symbol: atomic_dec
- Explanation: atomic_dec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `9`

## W-000226 SignatureDrift

- Risk: High
- Score: 12.4
- Symbol: debugfs_create_dir
- Explanation: debugfs_create_dir changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `9`

## W-000330 SignatureDrift

- Risk: High
- Score: 12.4
- Symbol: page_to_nid
- Explanation: page_to_nid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `9`

## W-000355 SignatureDrift

- Risk: High
- Score: 12.4
- Symbol: set_bit
- Explanation: set_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&mut self'}, {'name': 'index', 'type': 'usize'}, {'name': 'val', 'type': 'bool) { debug_assert!(index / 8 < self.storage.as_ref().len()'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'nr', 'type': 'ffi::c_ulong'}, {'name': 'addr', 'type': '*mut ffi::c_ulong'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `9`

## W-000403 FieldDrift

- Risk: High
- Score: 12.4
- Symbol: arch_uprobe
- Explanation: arch_uprobe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'arch_uprobe__bindgen_ty_1'}, {'name': 'ops', 'type': '*const uprobe_xol_ops'}, {'name': '__bindgen_anon_2', 'type': 'arch_uprobe__bindgen_ty_2'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'arch_uprobe__bindgen_ty_1'}, {'name': 'ops', 'type': '*const uprobe_xol_ops'}, {'name': '__bindgen_anon_2', 'type': 'arch_uprobe__bindgen_ty_2'}, {'name': 'flags', 'type': 'ffi::c_ulong'}]`

### Rust Evidence

- Graph edges: `19`

## W-000003 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: __clear_bit
- Explanation: __clear_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000041 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: atomic64_dec
- Explanation: atomic64_dec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000054 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: atomic64_fetch_and
- Explanation: atomic64_fetch_and changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000082 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: atomic64_inc
- Explanation: atomic64_inc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000139 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: atomic_fetch_and
- Explanation: atomic_fetch_and changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000167 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: atomic_inc
- Explanation: atomic_inc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000697 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: queue_delayed_work_on
- Explanation: queue_delayed_work_on changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['cpu', 'system_wq', 'dwork', 'delay'], 'return_type': 'return'}`
- New: `{'params': ['cpu', 'system_percpu_wq', 'dwork', 'delay'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `8`

## W-000698 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: queue_work_on
- Explanation: queue_work_on changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['cpu', 'system_wq', 'work'], 'return_type': 'return'}`
- New: `{'params': ['cpu', 'system_percpu_wq', 'work'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `8`

## W-000710 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: vma_lookup
- Explanation: vma_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['mm', 'addr'], 'return_type': 'return'}`
- New: `{'params': ['struct mm_struct *mm', 'unsigned long addr'], 'return_type': 'static inline struct vm_area_struct *'}`

### Rust Evidence

- Graph edges: `8`

## W-000012 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: __set_bit
- Explanation: __set_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000227 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: debugfs_create_file_full
- Explanation: debugfs_create_file_full changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000277 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: hmac_sha224
- Explanation: hmac_sha224 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000282 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: hmac_sha256
- Explanation: hmac_sha256 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000287 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: hmac_sha384
- Explanation: hmac_sha384 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000292 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: hmac_sha512
- Explanation: hmac_sha512 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000317 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: kvrealloc_node_align
- Explanation: kvrealloc_node_align changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000328 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: mt_init_flags
- Explanation: mt_init_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000407 FieldDrift

- Risk: High
- Score: 12.0
- Symbol: blk_mq_tag_set
- Explanation: blk_mq_tag_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'ops', 'type': '*const blk_mq_ops'}, {'name': 'map', 'type': '[blk_mq_queue_map; 3usize]'}, {'name': 'nr_maps', 'type': 'ffi::c_uint'}, {'name': 'nr_hw_queues', 'type': 'ffi::c_uint'}, {'name': 'queue_depth', 'type': 'ffi::c_uint'}, {'name': 'reserved_tags', 'type': 'ffi::c_uint'}, {'name': 'cmd_size', 'type': 'ffi::c_uint'}, {'name': 'numa_node', 'type': 'ffi::c_int'}, {'name': 'timeout', 'type': 'ffi::c_uint'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'driver_data', 'type': '*mut ffi::c_void'}, {'name': 'tags', 'type': '*mut *mut blk_mq_tags'}, {'name': 'shared_tags', 'type': '*mut blk_mq_tags'}, {'name': 'tag_list_lock', 'type': 'mutex'}, {'name': 'tag_list', 'type': 'list_head'}, {'name': 'srcu', 'type': '*mut srcu_struct'}, {'name': 'update_nr_hwq_lock', 'type': 'rw_semaphore'}]`
- New: `[{'name': 'ops', 'type': '*const blk_mq_ops'}, {'name': 'map', 'type': '[blk_mq_queue_map; 3usize]'}, {'name': 'nr_maps', 'type': 'ffi::c_uint'}, {'name': 'nr_hw_queues', 'type': 'ffi::c_uint'}, {'name': 'queue_depth', 'type': 'ffi::c_uint'}, {'name': 'reserved_tags', 'type': 'ffi::c_uint'}, {'name': 'cmd_size', 'type': 'ffi::c_uint'}, {'name': 'numa_node', 'type': 'ffi::c_int'}, {'name': 'timeout', 'type': 'ffi::c_uint'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'driver_data', 'type': '*mut ffi::c_void'}, {'name': 'tags', 'type': '*mut *mut blk_mq_tags'}, {'name': 'shared_tags', 'type': '*mut blk_mq_tags'}, {'name': 'tag_list_lock', 'type': 'mutex'}, {'name': 'tag_list', 'type': 'list_head'}, {'name': 'srcu', 'type': '*mut srcu_struct'}, {'name': 'tags_srcu', 'type': 'srcu_struct'}, {'name': 'update_nr_hwq_lock', 'type': 'rw_semaphore'}]`

### Rust Evidence

- Graph edges: `17`

## W-000419 FieldDrift

- Risk: High
- Score: 12.0
- Symbol: cgroup_subsys
- Explanation: cgroup_subsys changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'css_alloc', 'type': '::core::option::Option<'}, {'name': 'css_offline', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_released', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_free', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_reset', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_killed', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_rstat_flush', 'type': '::core::option::Option<'}, {'name': 'css_extra_stat_show', 'type': '::core::option::Option<'}, {'name': 'css_local_stat_show', 'type': '::core::option::Option<'}, {'name': 'cancel_attach', 'type': '::core::option::Option<unsafe extern "C" fn(tset: *mut cgroup_taskset)>'}, {'name': 'attach', 'type': '::core::option::Option<unsafe extern "C" fn(tset: *mut cgroup_taskset)>'}, {'name': 'post_attach', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'can_fork', 'type': '::core::option::Option<'}, {'name': 'fork', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'bind', 'type': '::core::option::Option<unsafe extern "C" fn(root_css: *mut cgroup_subsys_state)>'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'legacy_name', 'type': '*const ffi::c_char'}, {'name': 'root', 'type': '*mut cgroup_root'}, {'name': 'css_idr', 'type': 'idr'}, {'name': 'cfts', 'type': 'list_head'}, {'name': 'dfl_cftypes', 'type': '*mut cftype'}, {'name': 'legacy_cftypes', 'type': '*mut cftype'}, {'name': 'depends_on', 'type': 'ffi::c_uint'}, {'name': 'rstat_ss_lock', 'type': 'spinlock_t'}, {'name': 'lhead', 'type': '*mut llist_head'}]`
- New: `[{'name': 'css_alloc', 'type': '::core::option::Option<'}, {'name': 'css_offline', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_released', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_free', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_reset', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_killed', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_rstat_flush', 'type': '::core::option::Option<'}, {'name': 'css_extra_stat_show', 'type': '::core::option::Option<'}, {'name': 'css_local_stat_show', 'type': '::core::option::Option<'}, {'name': 'cancel_attach', 'type': '::core::option::Option<unsafe extern "C" fn(tset: *mut cgroup_taskset)>'}, {'name': 'attach', 'type': '::core::option::Option<unsafe extern "C" fn(tset: *mut cgroup_taskset)>'}, {'name': 'can_fork', 'type': '::core::option::Option<'}, {'name': 'fork', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'bind', 'type': '::core::option::Option<unsafe extern "C" fn(root_css: *mut cgroup_subsys_state)>'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'legacy_name', 'type': '*const ffi::c_char'}, {'name': 'root', 'type': '*mut cgroup_root'}, {'name': 'css_idr', 'type': 'idr'}, {'name': 'cfts', 'type': 'list_head'}, {'name': 'dfl_cftypes', 'type': '*mut cftype'}, {'name': 'legacy_cftypes', 'type': '*mut cftype'}, {'name': 'depends_on', 'type': 'ffi::c_uint'}, {'name': 'rstat_ss_lock', 'type': 'spinlock_t'}, {'name': 'lhead', 'type': '*mut llist_head'}]`

### Rust Evidence

- Graph edges: `17`

## W-000095 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: atomic64_sub
- Explanation: atomic64_sub changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000180 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: atomic_sub
- Explanation: atomic_sub changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000212 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: cpu_relax
- Explanation: cpu_relax changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000256 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: debugfs_remove
- Explanation: debugfs_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000337 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: pci_dev_id
- Explanation: pci_dev_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000356 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: sg_dma_address
- Explanation: sg_dma_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000358 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: sg_next
- Explanation: sg_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000675 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: drm_bridge_get
- Explanation: drm_bridge_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_bridge *bridge'], 'return_type': 'struct drm_bridge *'}`
- New: `{'params': ['list_last_entry_or_null(&encoder->bridge_chain, struct drm_bridge, chain_node)'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `6`

## W-000049 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: atomic64_fetch_add
- Explanation: atomic64_fetch_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000134 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: atomic_fetch_add
- Explanation: atomic_fetch_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000200 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: bitmap_copy_and_extend
- Explanation: bitmap_copy_and_extend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000274 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: folio_mapping
- Explanation: folio_mapping changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut folio'}], 'return_type': '*mut address_space'}`
- New: `{'params': [{'name': 'folio', 'type': '*const folio'}], 'return_type': '*mut address_space'}`

### Rust Evidence

- Graph edges: `5`

## W-000357 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: sg_dma_len
- Explanation: sg_dma_len changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000373 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: smp_mb
- Explanation: smp_mb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000374 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: smp_rmb
- Explanation: smp_rmb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000375 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: smp_wmb
- Explanation: smp_wmb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000026 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic64_add_negative
- Explanation: atomic64_add_negative changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000030 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic64_add_return
- Explanation: atomic64_add_return changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000037 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic64_cmpxchg
- Explanation: atomic64_cmpxchg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000044 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic64_dec_return
- Explanation: atomic64_dec_return changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000058 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic64_fetch_andnot
- Explanation: atomic64_fetch_andnot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000062 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic64_fetch_dec
- Explanation: atomic64_fetch_dec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000066 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic64_fetch_inc
- Explanation: atomic64_fetch_inc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000070 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic64_fetch_or
- Explanation: atomic64_fetch_or changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000074 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic64_fetch_sub
- Explanation: atomic64_fetch_sub changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000078 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic64_fetch_xor
- Explanation: atomic64_fetch_xor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000085 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic64_inc_return
- Explanation: atomic64_inc_return changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000097 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic64_sub_return
- Explanation: atomic64_sub_return changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000101 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic64_try_cmpxchg
- Explanation: atomic64_try_cmpxchg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000105 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic64_xchg
- Explanation: atomic64_xchg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000111 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic_add_negative
- Explanation: atomic_add_negative changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000115 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic_add_return
- Explanation: atomic_add_return changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000122 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic_cmpxchg
- Explanation: atomic_cmpxchg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000129 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic_dec_return
- Explanation: atomic_dec_return changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000143 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic_fetch_andnot
- Explanation: atomic_fetch_andnot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000147 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic_fetch_dec
- Explanation: atomic_fetch_dec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000151 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic_fetch_inc
- Explanation: atomic_fetch_inc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000155 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic_fetch_or
- Explanation: atomic_fetch_or changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000159 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic_fetch_sub
- Explanation: atomic_fetch_sub changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000163 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic_fetch_xor
- Explanation: atomic_fetch_xor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000170 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic_inc_return
- Explanation: atomic_inc_return changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000182 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic_sub_return
- Explanation: atomic_sub_return changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000186 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic_try_cmpxchg
- Explanation: atomic_try_cmpxchg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000190 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: atomic_xchg
- Explanation: atomic_xchg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000218 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: debugfs_attr_write
- Explanation: debugfs_attr_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000251 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: debugfs_lookup
- Explanation: debugfs_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000263 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: dma_unmap_sgtable
- Explanation: dma_unmap_sgtable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000321 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: list_lru_walk
- Explanation: list_lru_walk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000339 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: pci_resource_start
- Explanation: pci_resource_start changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000692 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: memcpy
- Explanation: memcpy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['void *', 'const void *', '__kernel_size_t'], 'return_type': 'extern void *'}`
- New: `{'params': ['dst', 'src', 'len'], 'return_type': 'else'}`

### Rust Evidence

- Graph edges: `4`

## W-000711 ErrorDrift

- Risk: High
- Score: 11.3
- Symbol: debugfs_create_dir
- Explanation: debugfs_create_dir has ERROR_CODE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE', 'ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.18/include/linux/debugfs.h:303 `return ERR_PTR(-ENODEV);`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.18/rust/kernel/debugfs/entry.rs:40 `Entry<::dynamic_dir` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.18/rust/kernel/debugfs/entry.rs:94 `Entry<::dir` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.18/rust/kernel/debugfs/entry.rs:36 `// SAFETY: The invariants of this function's arguments ensure the safety of this call.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.18/rust/kernel/debugfs/entry.rs:89 `// SAFETY: The invariants of this function's arguments ensure the safety of this call.`

## W-000208 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: copy_pid_ns
- Explanation: copy_pid_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'ns', 'type': '*mut pid_namespace'}], 'return_type': '*mut pid_namespace'}`
- New: `{'params': [{'name': 'flags', 'type': 'u64_'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'ns', 'type': '*mut pid_namespace'}], 'return_type': '*mut pid_namespace'}`

### Rust Evidence

- Graph edges: `3`

## W-000222 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: debugfs_create_automount
- Explanation: debugfs_create_automount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000223 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: debugfs_create_blob
- Explanation: debugfs_create_blob changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000230 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: debugfs_create_file_unsafe
- Explanation: debugfs_create_file_unsafe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000234 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: debugfs_create_symlink
- Explanation: debugfs_create_symlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000311 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: krealloc
- Explanation: krealloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `3`

## W-000312 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: krealloc_node_align
- Explanation: krealloc_node_align changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000316 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: kvrealloc
- Explanation: kvrealloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `3`

## W-000320 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: list_lru_count
- Explanation: list_lru_count changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000348 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: request_irq
- Explanation: request_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000380 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: task_work_cancel
- Explanation: task_work_cancel changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000668 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: copy_pid_ns
- Explanation: copy_pid_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned long flags', 'struct user_namespace *user_ns', 'struct pid_namespace *ns'], 'return_type': 'static inline struct pid_namespace *'}`
- New: `{'params': ['u64 flags', 'struct user_namespace *user_ns', 'struct pid_namespace *ns'], 'return_type': 'static inline struct pid_namespace *'}`

### Rust Evidence

- Graph edges: `3`

## W-000035 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: atomic64_and
- Explanation: atomic64_and changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000091 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: atomic64_read
- Explanation: atomic64_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000093 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: atomic64_set
- Explanation: atomic64_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000120 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: atomic_and
- Explanation: atomic_and changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000176 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: atomic_read
- Explanation: atomic_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000178 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: atomic_set
- Explanation: atomic_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000217 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: debugfs_attr_read
- Explanation: debugfs_attr_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000219 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: debugfs_attr_write_signed
- Explanation: debugfs_attr_write_signed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000236 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: debugfs_create_u32
- Explanation: debugfs_create_u32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000254 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: debugfs_read_file_bool
- Explanation: debugfs_read_file_bool changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000255 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: debugfs_read_file_str
- Explanation: debugfs_read_file_str changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000257 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: debugfs_write_file_bool
- Explanation: debugfs_write_file_bool changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000364 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: sha256_finup_2x
- Explanation: sha256_finup_2x changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000384 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: thaw_process
- Explanation: thaw_process changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000393 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: uprobe_write
- Explanation: uprobe_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000400 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vrealloc
- Explanation: vrealloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `2`

## W-000401 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vrealloc_node_align
- Explanation: vrealloc_node_align changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000434 FieldDrift

- Risk: High
- Score: 11.0
- Symbol: ma_state
- Explanation: ma_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'tree', 'type': '*mut maple_tree'}, {'name': 'index', 'type': 'ffi::c_ulong'}, {'name': 'last', 'type': 'ffi::c_ulong'}, {'name': 'node', 'type': '*mut maple_enode'}, {'name': 'min', 'type': 'ffi::c_ulong'}, {'name': 'max', 'type': 'ffi::c_ulong'}, {'name': 'alloc', 'type': '*mut maple_alloc'}, {'name': 'status', 'type': 'maple_status'}, {'name': 'depth', 'type': 'ffi::c_uchar'}, {'name': 'offset', 'type': 'ffi::c_uchar'}, {'name': 'mas_flags', 'type': 'ffi::c_uchar'}, {'name': 'end', 'type': 'ffi::c_uchar'}, {'name': 'store_type', 'type': 'store_type'}]`
- New: `[{'name': 'tree', 'type': '*mut maple_tree'}, {'name': 'index', 'type': 'ffi::c_ulong'}, {'name': 'last', 'type': 'ffi::c_ulong'}, {'name': 'node', 'type': '*mut maple_enode'}, {'name': 'min', 'type': 'ffi::c_ulong'}, {'name': 'max', 'type': 'ffi::c_ulong'}, {'name': 'sheaf', 'type': '*mut slab_sheaf'}, {'name': 'alloc', 'type': '*mut maple_node'}, {'name': 'node_request', 'type': 'ffi::c_ulong'}, {'name': 'status', 'type': 'maple_status'}, {'name': 'depth', 'type': 'ffi::c_uchar'}, {'name': 'offset', 'type': 'ffi::c_uchar'}, {'name': 'mas_flags', 'type': 'ffi::c_uchar'}, {'name': 'end', 'type': 'ffi::c_uchar'}, {'name': 'store_type', 'type': 'store_type'}]`

### Rust Evidence

- Graph edges: `12`

## W-000693 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: memset
- Explanation: memset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['void *', 'int', '__kernel_size_t'], 'return_type': 'extern void *'}`
- New: `{'params': ['dst', '0xff', 'len'], 'return_type': 'else'}`

### Rust Evidence

- Graph edges: `2`

## W-000001 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __account_locked_vm
- Explanation: __account_locked_vm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'pages', 'type': 'ffi::c_ulong'}, {'name': 'inc', 'type': 'bool_'}, {'name': 'task', 'type': '*mut task_struct'}, {'name': 'bypass_rlim', 'type': 'bool_'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'pages', 'type': 'ffi::c_ulong'}, {'name': 'inc', 'type': 'bool_'}, {'name': 'task', 'type': '*const task_struct'}, {'name': 'bypass_rlim', 'type': 'bool_'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000002 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __cgroup_get_from_id
- Explanation: __cgroup_get_from_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000004 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __compat_vma_mmap_prepare
- Explanation: __compat_vma_mmap_prepare changed across the selected Linux versions.
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

- Old: `{'params': [{'name': 'clone_flags', 'type': 'ffi::c_ulong'}, {'name': 'tsk', 'type': '*mut task_struct'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'clone_flags', 'type': 'u64_'}, {'name': 'tsk', 'type': '*mut task_struct'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000006 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __hmac_sha256_init
- Explanation: __hmac_sha256_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000007 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __hmac_sha512_init
- Explanation: __hmac_sha512_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000008 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kvmalloc_node_noprof
- Explanation: __kvmalloc_node_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'size', 'type': 'usize'}, {'name': 'flags', 'type': 'gfp_t'}, {'name': 'node', 'type': 'ffi::c_int'}], 'return_type': '*mut ffi::c_void'}`
- New: `{'params': [{'name': 'size', 'type': 'usize'}, {'name': 'align', 'type': 'ffi::c_ulong'}, {'name': 'flags', 'type': 'gfp_t'}, {'name': 'node', 'type': 'ffi::c_int'}], 'return_type': '*mut ffi::c_void'}`

### Rust Evidence

- Graph edges: `1`

## W-000009 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mnt_is_readonly
- Explanation: __mnt_is_readonly changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'mnt', 'type': '*mut vfsmount'}], 'return_type': 'bool_'}`
- New: `{'params': [{'name': 'mnt', 'type': '*const vfsmount'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000010 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __ns_common_free
- Explanation: __ns_common_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000011 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __ns_common_init
- Explanation: __ns_common_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000013 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sha256_update
- Explanation: __sha256_update changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000014 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sha512_update
- Explanation: __sha512_update changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000015 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __vm_enough_memory
- Explanation: __vm_enough_memory changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'pages', 'type': 'ffi::c_long'}, {'name': 'cap_sys_admin', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'mm', 'type': '*const mm_struct'}, {'name': 'pages', 'type': 'ffi::c_long'}, {'name': 'cap_sys_admin', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000016 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_pages_nolock_noprof
- Explanation: alloc_pages_nolock_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'nid', 'type': 'ffi::c_int'}, {'name': 'order', 'type': 'ffi::c_uint'}], 'return_type': '*mut page'}`
- New: `{'params': [{'name': 'gfp_flags', 'type': 'gfp_t'}, {'name': 'nid', 'type': 'ffi::c_int'}, {'name': 'order', 'type': 'ffi::c_uint'}], 'return_type': '*mut page'}`

### Rust Evidence

- Graph edges: `1`

## W-000017 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_pick_mmap_layout
- Explanation: arch_pick_mmap_layout changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'rlim_stack', 'type': '*mut rlimit'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'rlim_stack', 'type': '*const rlimit'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000018 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_uprobe_clear_state
- Explanation: arch_uprobe_clear_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000019 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_uprobe_init_state
- Explanation: arch_uprobe_init_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000020 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_uprobe_optimize
- Explanation: arch_uprobe_optimize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000022 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_uretprobe_trampoline
- Explanation: arch_uretprobe_trampoline changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000023 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: aspm_l0s_support
- Explanation: aspm_l0s_support changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000024 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: aspm_l1_support
- Explanation: aspm_l1_support changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000027 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_add_negative_acquire
- Explanation: atomic64_add_negative_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000028 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_add_negative_relaxed
- Explanation: atomic64_add_negative_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000029 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_add_negative_release
- Explanation: atomic64_add_negative_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000031 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_add_return_acquire
- Explanation: atomic64_add_return_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000032 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_add_return_relaxed
- Explanation: atomic64_add_return_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000033 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_add_return_release
- Explanation: atomic64_add_return_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000034 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_add_unless
- Explanation: atomic64_add_unless changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000036 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_andnot
- Explanation: atomic64_andnot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000038 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_cmpxchg_acquire
- Explanation: atomic64_cmpxchg_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000039 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_cmpxchg_relaxed
- Explanation: atomic64_cmpxchg_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000040 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_cmpxchg_release
- Explanation: atomic64_cmpxchg_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000042 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_dec_and_test
- Explanation: atomic64_dec_and_test changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000043 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_dec_if_positive
- Explanation: atomic64_dec_if_positive changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000045 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_dec_return_acquire
- Explanation: atomic64_dec_return_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000046 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_dec_return_relaxed
- Explanation: atomic64_dec_return_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000047 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_dec_return_release
- Explanation: atomic64_dec_return_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000048 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_dec_unless_positive
- Explanation: atomic64_dec_unless_positive changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000050 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_add_acquire
- Explanation: atomic64_fetch_add_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000051 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_add_relaxed
- Explanation: atomic64_fetch_add_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000052 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_add_release
- Explanation: atomic64_fetch_add_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000053 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_add_unless
- Explanation: atomic64_fetch_add_unless changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000055 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_and_acquire
- Explanation: atomic64_fetch_and_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000056 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_and_relaxed
- Explanation: atomic64_fetch_and_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000057 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_and_release
- Explanation: atomic64_fetch_and_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000059 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_andnot_acquire
- Explanation: atomic64_fetch_andnot_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000060 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_andnot_relaxed
- Explanation: atomic64_fetch_andnot_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000061 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_andnot_release
- Explanation: atomic64_fetch_andnot_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000063 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_dec_acquire
- Explanation: atomic64_fetch_dec_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000064 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_dec_relaxed
- Explanation: atomic64_fetch_dec_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000065 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_dec_release
- Explanation: atomic64_fetch_dec_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000067 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_inc_acquire
- Explanation: atomic64_fetch_inc_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000068 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_inc_relaxed
- Explanation: atomic64_fetch_inc_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000069 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_inc_release
- Explanation: atomic64_fetch_inc_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000071 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_or_acquire
- Explanation: atomic64_fetch_or_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000072 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_or_relaxed
- Explanation: atomic64_fetch_or_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000073 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_or_release
- Explanation: atomic64_fetch_or_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000075 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_sub_acquire
- Explanation: atomic64_fetch_sub_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000076 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_sub_relaxed
- Explanation: atomic64_fetch_sub_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000077 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_sub_release
- Explanation: atomic64_fetch_sub_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000079 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_xor_acquire
- Explanation: atomic64_fetch_xor_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000080 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_xor_relaxed
- Explanation: atomic64_fetch_xor_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000081 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_fetch_xor_release
- Explanation: atomic64_fetch_xor_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000083 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_inc_and_test
- Explanation: atomic64_inc_and_test changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000084 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_inc_not_zero
- Explanation: atomic64_inc_not_zero changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000086 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_inc_return_acquire
- Explanation: atomic64_inc_return_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000087 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_inc_return_relaxed
- Explanation: atomic64_inc_return_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000088 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_inc_return_release
- Explanation: atomic64_inc_return_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000089 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_inc_unless_negative
- Explanation: atomic64_inc_unless_negative changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000090 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_or
- Explanation: atomic64_or changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000092 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_read_acquire
- Explanation: atomic64_read_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000094 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_set_release
- Explanation: atomic64_set_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000096 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_sub_and_test
- Explanation: atomic64_sub_and_test changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000098 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_sub_return_acquire
- Explanation: atomic64_sub_return_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000099 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_sub_return_relaxed
- Explanation: atomic64_sub_return_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000100 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_sub_return_release
- Explanation: atomic64_sub_return_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000102 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_try_cmpxchg_acquire
- Explanation: atomic64_try_cmpxchg_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000103 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_try_cmpxchg_relaxed
- Explanation: atomic64_try_cmpxchg_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000104 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_try_cmpxchg_release
- Explanation: atomic64_try_cmpxchg_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000106 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_xchg_acquire
- Explanation: atomic64_xchg_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000107 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_xchg_relaxed
- Explanation: atomic64_xchg_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000108 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_xchg_release
- Explanation: atomic64_xchg_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000109 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic64_xor
- Explanation: atomic64_xor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000112 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_add_negative_acquire
- Explanation: atomic_add_negative_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000113 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_add_negative_relaxed
- Explanation: atomic_add_negative_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000114 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_add_negative_release
- Explanation: atomic_add_negative_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000116 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_add_return_acquire
- Explanation: atomic_add_return_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000117 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_add_return_relaxed
- Explanation: atomic_add_return_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000118 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_add_return_release
- Explanation: atomic_add_return_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000119 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_add_unless
- Explanation: atomic_add_unless changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000121 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_andnot
- Explanation: atomic_andnot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000123 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_cmpxchg_acquire
- Explanation: atomic_cmpxchg_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000124 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_cmpxchg_relaxed
- Explanation: atomic_cmpxchg_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000125 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_cmpxchg_release
- Explanation: atomic_cmpxchg_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000127 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_dec_and_test
- Explanation: atomic_dec_and_test changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000128 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_dec_if_positive
- Explanation: atomic_dec_if_positive changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000130 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_dec_return_acquire
- Explanation: atomic_dec_return_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000131 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_dec_return_relaxed
- Explanation: atomic_dec_return_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000132 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_dec_return_release
- Explanation: atomic_dec_return_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000133 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_dec_unless_positive
- Explanation: atomic_dec_unless_positive changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000135 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_add_acquire
- Explanation: atomic_fetch_add_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000136 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_add_relaxed
- Explanation: atomic_fetch_add_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000137 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_add_release
- Explanation: atomic_fetch_add_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000138 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_add_unless
- Explanation: atomic_fetch_add_unless changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000140 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_and_acquire
- Explanation: atomic_fetch_and_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000141 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_and_relaxed
- Explanation: atomic_fetch_and_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000142 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_and_release
- Explanation: atomic_fetch_and_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000144 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_andnot_acquire
- Explanation: atomic_fetch_andnot_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000145 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_andnot_relaxed
- Explanation: atomic_fetch_andnot_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000146 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_andnot_release
- Explanation: atomic_fetch_andnot_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000148 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_dec_acquire
- Explanation: atomic_fetch_dec_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000149 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_dec_relaxed
- Explanation: atomic_fetch_dec_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000150 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_dec_release
- Explanation: atomic_fetch_dec_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000152 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_inc_acquire
- Explanation: atomic_fetch_inc_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000153 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_inc_relaxed
- Explanation: atomic_fetch_inc_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000154 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_inc_release
- Explanation: atomic_fetch_inc_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000156 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_or_acquire
- Explanation: atomic_fetch_or_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000157 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_or_relaxed
- Explanation: atomic_fetch_or_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000158 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_or_release
- Explanation: atomic_fetch_or_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000160 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_sub_acquire
- Explanation: atomic_fetch_sub_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000161 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_sub_relaxed
- Explanation: atomic_fetch_sub_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000162 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_sub_release
- Explanation: atomic_fetch_sub_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000164 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_xor_acquire
- Explanation: atomic_fetch_xor_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000165 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_xor_relaxed
- Explanation: atomic_fetch_xor_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000166 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_fetch_xor_release
- Explanation: atomic_fetch_xor_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000168 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_inc_and_test
- Explanation: atomic_inc_and_test changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000169 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_inc_not_zero
- Explanation: atomic_inc_not_zero changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000171 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_inc_return_acquire
- Explanation: atomic_inc_return_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000172 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_inc_return_relaxed
- Explanation: atomic_inc_return_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000173 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_inc_return_release
- Explanation: atomic_inc_return_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000174 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_inc_unless_negative
- Explanation: atomic_inc_unless_negative changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000175 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_or
- Explanation: atomic_or changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000177 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_read_acquire
- Explanation: atomic_read_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000179 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_set_release
- Explanation: atomic_set_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000181 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_sub_and_test
- Explanation: atomic_sub_and_test changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000183 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_sub_return_acquire
- Explanation: atomic_sub_return_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000184 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_sub_return_relaxed
- Explanation: atomic_sub_return_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000185 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_sub_return_release
- Explanation: atomic_sub_return_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000187 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_try_cmpxchg_acquire
- Explanation: atomic_try_cmpxchg_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000188 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_try_cmpxchg_relaxed
- Explanation: atomic_try_cmpxchg_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000189 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_try_cmpxchg_release
- Explanation: atomic_try_cmpxchg_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000191 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_xchg_acquire
- Explanation: atomic_xchg_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000192 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_xchg_relaxed
- Explanation: atomic_xchg_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000193 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_xchg_release
- Explanation: atomic_xchg_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000194 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: atomic_xor
- Explanation: atomic_xor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000195 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: backing_file_user_path
- Explanation: backing_file_user_path changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'f', 'type': '*const file'}], 'return_type': '*mut path'}`
- New: `{'params': [{'name': 'f', 'type': '*const file'}], 'return_type': '*const path'}`

### Rust Evidence

- Graph edges: `1`

## W-000196 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_iov_iter_get_pages
- Explanation: bio_iov_iter_get_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'bio', 'type': '*mut bio'}, {'name': 'iter', 'type': '*mut iov_iter'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'bio', 'type': '*mut bio'}, {'name': 'iter', 'type': '*mut iov_iter'}, {'name': 'len_align_mask', 'type': 'ffi::c_uint'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000197 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_split_io_at
- Explanation: bio_split_io_at changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000199 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_submit_split_bioset
- Explanation: bio_submit_split_bioset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000201 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_task_work_cancel_and_free
- Explanation: bpf_task_work_cancel_and_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000203 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: close_fd
- Explanation: close_fd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000204 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: collect_paths
- Explanation: collect_paths changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*const path'}, {'name': 'arg2', 'type': '*mut path'}, {'name': 'arg3', 'type': 'ffi::c_uint'}], 'return_type': '*mut path'}`
- New: `{'params': [{'name': 'arg1', 'type': '*const path'}, {'name': 'arg2', 'type': '*mut path'}, {'name': 'arg3', 'type': 'ffi::c_uint'}], 'return_type': '*const path'}`

### Rust Evidence

- Graph edges: `1`

## W-000205 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_cgroup_ns
- Explanation: copy_cgroup_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'old_ns', 'type': '*mut cgroup_namespace'}], 'return_type': '*mut cgroup_namespace'}`
- New: `{'params': [{'name': 'flags', 'type': 'u64_'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'old_ns', 'type': '*mut cgroup_namespace'}], 'return_type': '*mut cgroup_namespace'}`

### Rust Evidence

- Graph edges: `1`

## W-000206 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_creds
- Explanation: copy_creds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut task_struct'}, {'name': 'arg2', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'arg1', 'type': '*mut task_struct'}, {'name': 'arg2', 'type': 'u64_'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000207 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_namespaces
- Explanation: copy_namespaces changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'tsk', 'type': '*mut task_struct'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'flags', 'type': 'u64_'}, {'name': 'tsk', 'type': '*mut task_struct'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000209 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_semundo
- Explanation: copy_semundo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'clone_flags', 'type': 'ffi::c_ulong'}, {'name': 'tsk', 'type': '*mut task_struct'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'clone_flags', 'type': 'u64_'}, {'name': 'tsk', 'type': '*mut task_struct'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000210 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_cluster_flags
- Explanation: cpu_cluster_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000211 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_core_flags
- Explanation: cpu_core_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000213 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_smt_flags
- Explanation: cpu_smt_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000214 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_frequency_table_cpuinfo
- Explanation: cpufreq_frequency_table_cpuinfo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'policy', 'type': '*mut cpufreq_policy'}, {'name': 'table', 'type': '*mut cpufreq_frequency_table'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'policy', 'type': '*mut cpufreq_policy'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000215 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_frequency_table_verify
- Explanation: cpufreq_frequency_table_verify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'policy', 'type': '*mut cpufreq_policy_data'}, {'name': 'table', 'type': '*mut cpufreq_frequency_table'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'policy', 'type': '*mut cpufreq_policy_data'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000216 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: datagram_poll_queue
- Explanation: datagram_poll_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000220 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_change_name
- Explanation: debugfs_change_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000221 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_create_atomic_t
- Explanation: debugfs_create_atomic_t changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000224 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_create_bool
- Explanation: debugfs_create_bool changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000225 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_create_devm_seqfile
- Explanation: debugfs_create_devm_seqfile changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000228 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_create_file_short
- Explanation: debugfs_create_file_short changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000229 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_create_file_size
- Explanation: debugfs_create_file_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000231 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_create_regset32
- Explanation: debugfs_create_regset32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000232 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_create_size_t
- Explanation: debugfs_create_size_t changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000233 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_create_str
- Explanation: debugfs_create_str changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000235 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_create_u16
- Explanation: debugfs_create_u16 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000237 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_create_u32_array
- Explanation: debugfs_create_u32_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000238 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_create_u64
- Explanation: debugfs_create_u64 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000239 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_create_u8
- Explanation: debugfs_create_u8 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000240 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_create_ulong
- Explanation: debugfs_create_ulong changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000241 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_create_x16
- Explanation: debugfs_create_x16 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000242 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_create_x32
- Explanation: debugfs_create_x32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000243 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_create_x64
- Explanation: debugfs_create_x64 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000244 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_create_x8
- Explanation: debugfs_create_x8 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000245 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_enter_cancellation
- Explanation: debugfs_enter_cancellation changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000246 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_file_get
- Explanation: debugfs_file_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000247 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_file_put
- Explanation: debugfs_file_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000248 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_get_aux
- Explanation: debugfs_get_aux changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000249 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_initialized
- Explanation: debugfs_initialized changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000250 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_leave_cancellation
- Explanation: debugfs_leave_cancellation changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000252 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_lookup_and_remove
- Explanation: debugfs_lookup_and_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000253 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: debugfs_print_regs32
- Explanation: debugfs_print_regs32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000258 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_kmemdup_const
- Explanation: devm_kmemdup_const changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000261 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_map_phys
- Explanation: dma_map_phys changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000262 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_unmap_phys
- Explanation: dma_unmap_phys changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000264 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_close_on_exec
- Explanation: do_close_on_exec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000265 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drop_collected_paths
- Explanation: drop_collected_paths changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut path'}, {'name': 'arg2', 'type': '*mut path'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'arg1', 'type': '*const path'}, {'name': 'arg2', 'type': '*const path'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000266 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dup_fd
- Explanation: dup_fd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000267 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: eetlp_prefix_max
- Explanation: eetlp_prefix_max changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_3.get(2usize, 3u8) as u32) } } #[inline] pub fn set_eetlp_prefix_max(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_3.get(4usize, 3u8) as u32) } } #[inline] pub fn set_eetlp_prefix_max(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000269 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: file_close_fd
- Explanation: file_close_fd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000271 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filesystems_freeze
- Explanation: filesystems_freeze changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': '()'}`
- New: `{'params': [{'name': 'freeze_all', 'type': 'bool_'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000272 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_end_dropbehind
- Explanation: folio_end_dropbehind changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000273 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_end_writeback_no_dropbehind
- Explanation: folio_end_writeback_no_dropbehind changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000276 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: handle_syscall_uprobe
- Explanation: handle_syscall_uprobe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000278 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha224_final
- Explanation: hmac_sha224_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000279 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha224_init_usingrawkey
- Explanation: hmac_sha224_init_usingrawkey changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000280 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha224_preparekey
- Explanation: hmac_sha224_preparekey changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000281 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha224_usingrawkey
- Explanation: hmac_sha224_usingrawkey changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000283 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha256_final
- Explanation: hmac_sha256_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000284 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha256_init_usingrawkey
- Explanation: hmac_sha256_init_usingrawkey changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000285 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha256_preparekey
- Explanation: hmac_sha256_preparekey changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000286 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha256_usingrawkey
- Explanation: hmac_sha256_usingrawkey changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000288 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha384_final
- Explanation: hmac_sha384_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000289 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha384_init_usingrawkey
- Explanation: hmac_sha384_init_usingrawkey changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000290 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha384_preparekey
- Explanation: hmac_sha384_preparekey changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000291 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha384_usingrawkey
- Explanation: hmac_sha384_usingrawkey changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000293 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha512_final
- Explanation: hmac_sha512_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000294 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha512_init_usingrawkey
- Explanation: hmac_sha512_init_usingrawkey changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000295 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha512_preparekey
- Explanation: hmac_sha512_preparekey changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000296 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hmac_sha512_usingrawkey
- Explanation: hmac_sha512_usingrawkey changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000297 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hrtimer_cb_get_time
- Explanation: hrtimer_cb_get_time changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000299 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: init_task_work
- Explanation: init_task_work changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000300 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inode_just_drop
- Explanation: inode_just_drop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000302 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iput_not_last
- Explanation: iput_not_last changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000303 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iterate_fd
- Explanation: iterate_fd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000304 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kfree_nolock
- Explanation: kfree_nolock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000305 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmalloc_nolock_noprof
- Explanation: kmalloc_nolock_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000306 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmem_cache_alloc_from_sheaf_noprof
- Explanation: kmem_cache_alloc_from_sheaf_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000307 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmem_cache_prefill_sheaf
- Explanation: kmem_cache_prefill_sheaf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000308 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmem_cache_refill_sheaf
- Explanation: kmem_cache_refill_sheaf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000309 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmem_cache_return_sheaf
- Explanation: kmem_cache_return_sheaf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000310 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmem_cache_sheaf_size
- Explanation: kmem_cache_sheaf_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000313 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: krealloc_node_align_noprof
- Explanation: krealloc_node_align_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000315 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_array_gen_params
- Explanation: kunit_array_gen_params changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000318 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kvrealloc_node_align_noprof
- Explanation: kvrealloc_node_align_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000322 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ltr_path
- Explanation: ltr_path changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_3.get(0usize, 1u8) as u32) } } #[inline] pub fn set_ltr_path(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_3.get(2usize, 1u8) as u32) } } #[inline] pub fn set_ltr_path(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000329 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_bitfield_3
- Explanation: new_bitfield_3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'ltr_path', 'type': 'ffi::c_uint'}, {'name': 'pasid_no_tlp', 'type': 'ffi::c_uint'}, {'name': 'eetlp_prefix_max', 'type': 'ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`
- New: `{'params': [{'name': 'aspm_l0s_support', 'type': 'ffi::c_uint'}, {'name': 'aspm_l1_support', 'type': 'ffi::c_uint'}, {'name': 'ltr_path', 'type': 'ffi::c_uint'}, {'name': 'pasid_no_tlp', 'type': 'ffi::c_uint'}, {'name': 'eetlp_prefix_max', 'type': 'ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`

### Rust Evidence

- Graph edges: `1`

## W-000331 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: panic_in_progress
- Explanation: panic_in_progress changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000332 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: panic_on_other_cpu
- Explanation: panic_on_other_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000333 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: panic_on_this_cpu
- Explanation: panic_on_this_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000334 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: panic_reset
- Explanation: panic_reset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000335 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: panic_try_start
- Explanation: panic_try_start changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000336 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pasid_no_tlp
- Explanation: pasid_no_tlp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_3.get(1usize, 1u8) as u32) } } #[inline] pub fn set_pasid_no_tlp(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_3.get(3usize, 1u8) as u32) } } #[inline] pub fn set_pasid_no_tlp(&mut self, val: ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000338 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_release_resource
- Explanation: pci_release_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'dev', 'type': '*mut pci_dev'}, {'name': 'resno', 'type': 'ffi::c_int'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'dev', 'type': '*mut pci_dev'}, {'name': 'resno', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000342 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pidns_is_ancestor
- Explanation: pidns_is_ancestor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000343 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_hibernation_mode_is_suspend
- Explanation: pm_hibernation_mode_is_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000344 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: process_shares_mm
- Explanation: process_shares_mm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'p', 'type': '*mut task_struct'}, {'name': 'mm', 'type': '*mut mm_struct'}], 'return_type': 'bool_'}`
- New: `{'params': [{'name': 'p', 'type': '*const task_struct'}, {'name': 'mm', 'type': '*const mm_struct'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000345 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: put_files_struct
- Explanation: put_files_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000349 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sb_min_blocksize
- Explanation: sb_min_blocksize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut super_block'}, {'name': 'arg2', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'sb', 'type': '*mut super_block'}, {'name': 'size', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000350 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sb_set_blocksize
- Explanation: sb_set_blocksize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut super_block'}, {'name': 'arg2', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'sb', 'type': '*mut super_block'}, {'name': 'size', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000351 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sched_fork
- Explanation: sched_fork changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'clone_flags', 'type': 'ffi::c_ulong'}, {'name': 'p', 'type': '*mut task_struct'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'clone_flags', 'type': 'u64_'}, {'name': 'p', 'type': '*mut task_struct'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000352 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_dentry_create_files_as
- Explanation: security_dentry_create_files_as changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'dentry', 'type': '*mut dentry'}, {'name': 'mode', 'type': 'ffi::c_int'}, {'name': 'name', 'type': '*mut qstr'}, {'name': 'old', 'type': '*const cred'}, {'name': 'new', 'type': '*mut cred'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'dentry', 'type': '*mut dentry'}, {'name': 'mode', 'type': 'ffi::c_int'}, {'name': 'name', 'type': '*const qstr'}, {'name': 'old', 'type': '*const cred'}, {'name': 'new', 'type': '*mut cred'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000353 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_lsmprop_to_secctx
- Explanation: security_lsmprop_to_secctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'prop', 'type': '*mut lsm_prop'}, {'name': 'cp', 'type': '*mut lsm_context'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'prop', 'type': '*mut lsm_prop'}, {'name': 'cp', 'type': '*mut lsm_context'}, {'name': 'lsmid', 'type': 'ffi::c_int'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000354 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_task_alloc
- Explanation: security_task_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'task', 'type': '*mut task_struct'}, {'name': 'clone_flags', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'task', 'type': '*mut task_struct'}, {'name': 'clone_flags', 'type': 'u64_'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000360 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sha224_final
- Explanation: sha224_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000361 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sha224_init
- Explanation: sha224_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000363 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sha256_final
- Explanation: sha256_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000365 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sha256_finup_2x_is_optimized
- Explanation: sha256_finup_2x_is_optimized changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000366 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sha256_init
- Explanation: sha256_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000368 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sha384_final
- Explanation: sha384_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000369 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sha384_init
- Explanation: sha384_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000371 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sha512_final
- Explanation: sha512_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000372 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sha512_init
- Explanation: sha512_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000376 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: software_node_register_node_group
- Explanation: software_node_register_node_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'node_group', 'type': '*mut *const software_node'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'node_group', 'type': '*const *const software_node'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000377 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: software_node_unregister_node_group
- Explanation: software_node_unregister_node_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'node_group', 'type': '*mut *const software_node'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'node_group', 'type': '*const *const software_node'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000379 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: task_work_add
- Explanation: task_work_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000381 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: task_work_cancel_func
- Explanation: task_work_cancel_func changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000382 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: task_work_cancel_match
- Explanation: task_work_cancel_match changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000383 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: task_work_run
- Explanation: task_work_run changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000386 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: tl_cls_mask
- Explanation: tl_cls_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000387 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: tl_mc_mask
- Explanation: tl_mc_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000388 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: tl_pkg_mask
- Explanation: tl_pkg_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000389 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: tl_smt_mask
- Explanation: tl_smt_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000390 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unshare_files
- Explanation: unshare_files changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000391 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: uprobe_copy_from_page
- Explanation: uprobe_copy_from_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000392 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: uprobe_copy_process
- Explanation: uprobe_copy_process changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 't', 'type': '*mut task_struct'}, {'name': 'flags', 'type': 'ffi::c_ulong'}], 'return_type': '()'}`
- New: `{'params': [{'name': 't', 'type': '*mut task_struct'}, {'name': 'flags', 'type': 'u64_'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000394 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: uprobe_write_opcode
- Explanation: uprobe_write_opcode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'auprobe', 'type': '*mut arch_uprobe'}, {'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'vaddr', 'type': 'ffi::c_ulong'}, {'name': 'arg1', 'type': 'uprobe_opcode_t'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'auprobe', 'type': '*mut arch_uprobe'}, {'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'vaddr', 'type': 'ffi::c_ulong'}, {'name': 'arg1', 'type': 'uprobe_opcode_t'}, {'name': 'is_register', 'type': 'bool_'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000396 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_normal_page_pud
- Explanation: vm_normal_page_pud changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000397 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_is_anon_shmem
- Explanation: vma_is_anon_shmem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}], 'return_type': 'bool_'}`
- New: `{'params': [{'name': 'vma', 'type': '*const vm_area_struct'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000398 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_is_shmem
- Explanation: vma_is_shmem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}], 'return_type': 'bool_'}`
- New: `{'params': [{'name': 'vma', 'type': '*const vm_area_struct'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000399 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_is_stack_for_current
- Explanation: vma_is_stack_for_current changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'vma', 'type': '*const vm_area_struct'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000664 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kvmalloc_node_noprof
- Explanation: __kvmalloc_node_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['DECL_BUCKET_PARAMS(size, b)', 'gfp_t flags', 'int node) __alloc_size(1'], 'return_type': 'void *'}`
- New: `{'params': ['DECL_BUCKET_PARAMS(size, b)', 'unsigned long align', 'gfp_t flags', 'int node) __alloc_size(1'], 'return_type': 'void *'}`

### Rust Evidence

- Graph edges: `1`

## W-000667 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_creds
- Explanation: copy_creds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct task_struct *', 'unsigned long'], 'return_type': 'extern int'}`
- New: `{'params': ['struct task_struct *', 'u64'], 'return_type': 'extern int'}`

### Rust Evidence

- Graph edges: `1`

## W-000670 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_frequency_table_cpuinfo
- Explanation: cpufreq_frequency_table_cpuinfo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct cpufreq_policy *policy', 'struct cpufreq_frequency_table *table'], 'return_type': 'else int'}`
- New: `{'params': ['struct cpufreq_policy *policy'], 'return_type': 'else int'}`

### Rust Evidence

- Graph edges: `1`

## W-000671 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_frequency_table_verify
- Explanation: cpufreq_frequency_table_verify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct cpufreq_policy_data *policy', 'struct cpufreq_frequency_table *table'], 'return_type': 'int'}`
- New: `{'params': ['struct cpufreq_policy_data *policy'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000680 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filesystems_freeze
- Explanation: filesystems_freeze changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'void'}`
- New: `{'params': ['bool freeze_all'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-000694 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_release_resource
- Explanation: pci_release_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct pci_dev *dev', 'int resno'], 'return_type': 'void'}`
- New: `{'params': ['struct pci_dev *dev', 'int resno'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000699 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sb_min_blocksize
- Explanation: sb_min_blocksize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct super_block *', 'int'], 'return_type': 'extern int'}`
- New: `{'params': ['struct super_block *sb', 'int size'], 'return_type': 'int __must_check'}`

### Rust Evidence

- Graph edges: `1`

## W-000700 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sb_set_blocksize
- Explanation: sb_set_blocksize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct super_block *', 'int'], 'return_type': 'extern int'}`
- New: `{'params': ['struct super_block *sb', 'int size'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000701 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_dentry_create_files_as
- Explanation: security_dentry_create_files_as changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct dentry *dentry', 'int mode', 'struct qstr *name', 'const struct cred *old', 'struct cred *new'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct dentry *dentry', 'int mode', 'const struct qstr *name', 'const struct cred *old', 'struct cred *new'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `1`

## W-000702 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_lsmprop_to_secctx
- Explanation: security_lsmprop_to_secctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct lsm_prop *prop', 'struct lsm_context *cp'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct lsm_prop *prop', 'struct lsm_context *cp', 'int lsmid'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `1`

## W-000703 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_task_alloc
- Explanation: security_task_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct task_struct *task', 'unsigned long clone_flags'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct task_struct *task', 'u64 clone_flags'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `1`

## W-000704 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: software_node_register_node_group
- Explanation: software_node_register_node_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct software_node **node_group'], 'return_type': 'int'}`
- New: `{'params': ['const struct software_node * const *node_group'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-000705 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: software_node_unregister_node_group
- Explanation: software_node_unregister_node_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct software_node **node_group'], 'return_type': 'void'}`
- New: `{'params': ['const struct software_node * const *node_group'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-000021 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: arch_uprobe_trampoline
- Explanation: arch_uprobe_trampoline changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000198 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: bio_split_rw_at
- Explanation: bio_split_rw_at changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000268 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: exit_swap_address_space
- Explanation: exit_swap_address_space changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000270 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: file_remove_privs_flags
- Explanation: file_remove_privs_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000275 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: generic_delete_inode
- Explanation: generic_delete_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000298 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: init_swap_address_space
- Explanation: init_swap_address_space changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000301 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: iov_iter_is_aligned
- Explanation: iov_iter_is_aligned changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000314 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: krealloc_noprof
- Explanation: krealloc_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000319 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: kvrealloc_noprof
- Explanation: kvrealloc_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000323 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mdiobus_register_board_info
- Explanation: mdiobus_register_board_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000324 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mem_cgroup_charge_skmem
- Explanation: mem_cgroup_charge_skmem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000325 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mem_cgroup_uncharge_skmem
- Explanation: mem_cgroup_uncharge_skmem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000326 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mount_bdev
- Explanation: mount_bdev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000327 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mount_nodev
- Explanation: mount_nodev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000340 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_driver_register
- Explanation: phy_driver_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000341 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phy_driver_unregister
- Explanation: phy_driver_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000378 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: swp_swap_info
- Explanation: swp_swap_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000385 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: this_cpu_in_panic
- Explanation: this_cpu_in_panic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000395 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vfs_ioctl
- Explanation: vfs_ioctl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000402 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: write_cache_pages
- Explanation: write_cache_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000662 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: READ_ONCE
- Explanation: READ_ONCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['owner->on_cpu) && !vcpu_is_preempted(task_cpu(owner)'], 'return_type': 'return'}`
- New: `{'params': ['task->task_works'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-000663 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __fls
- Explanation: __fls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned long word'], 'return_type': 'static __always_inline unsigned int'}`
- New: `{'params': ['unsigned long word'], 'return_type': 'static __always_inline __attribute_const__ unsigned int'}`

### Rust Evidence

- Graph edges: `0`

## W-000665 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __this_cpu_read
- Explanation: __this_cpu_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['__irq_regs'], 'return_type': 'return'}`
- New: `{'params': ['pending_timer_softirq'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-000666 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: chacha_crypt
- Explanation: chacha_crypt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct chacha_state *state', 'u8 *dst', 'const u8 *src', 'unsigned int bytes', 'int nrounds'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct chacha_state *state', 'u8 *dst', 'const u8 *src', 'unsigned int bytes', 'int nrounds'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000669 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: cppc_get_transition_latency
- Explanation: cppc_get_transition_latency changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['int cpu'], 'return_type': 'static inline unsigned int'}`
- New: `{'params': ['int cpu'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `0`

## W-000672 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: curve25519
- Explanation: curve25519 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u8 mypublic[CURVE25519_KEY_SIZE]', 'const u8 secret[CURVE25519_KEY_SIZE]', 'const u8 basepoint[CURVE25519_KEY_SIZE]'], 'return_type': 'static inline bool __must_check'}`
- New: `{'params': ['u8 mypublic[CURVE25519_KEY_SIZE]', 'const u8 secret[CURVE25519_KEY_SIZE]', 'const u8 basepoint[CURVE25519_KEY_SIZE]'], 'return_type': 'bool __must_check'}`

### Rust Evidence

- Graph edges: `0`

## W-000673 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: curve25519_generate_public
- Explanation: curve25519_generate_public changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u8 pub[CURVE25519_KEY_SIZE]', 'const u8 secret[CURVE25519_KEY_SIZE]'], 'return_type': 'static inline bool __must_check'}`
- New: `{'params': ['u8 pub[CURVE25519_KEY_SIZE]', 'const u8 secret[CURVE25519_KEY_SIZE]'], 'return_type': 'bool __must_check'}`

### Rust Evidence

- Graph edges: `0`

## W-000674 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: curve25519_generic
- Explanation: curve25519_generic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['pub', 'secret', 'curve25519_base_point'], 'return_type': 'else'}`
- New: `{'params': ['u8 out[CURVE25519_KEY_SIZE]', 'const u8 scalar[CURVE25519_KEY_SIZE]', 'const u8 point[CURVE25519_KEY_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000676 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_gpusvm_init
- Explanation: drm_gpusvm_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_gpusvm *gpusvm', 'const char *name', 'struct drm_device *drm', 'struct mm_struct *mm', 'void *device_private_page_owner', 'unsigned long mm_start', 'unsigned long mm_range', 'unsigned long notifier_size', 'const struct drm_gpusvm_ops *ops', 'const unsigned long *chunk_sizes', 'int num_chunks'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_gpusvm *gpusvm', 'const char *name', 'struct drm_device *drm', 'struct mm_struct *mm', 'unsigned long mm_start', 'unsigned long mm_range', 'unsigned long notifier_size', 'const struct drm_gpusvm_ops *ops', 'const unsigned long *chunk_sizes', 'int num_chunks'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000677 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_gpuvm_sm_map
- Explanation: drm_gpuvm_sm_map changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_gpuvm *gpuvm', 'void *priv', 'u64 addr', 'u64 range', 'struct drm_gem_object *obj', 'u64 offset'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_gpuvm *gpuvm', 'void *priv', 'const struct drm_gpuvm_map_req *req'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000678 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_gpuvm_sm_map_exec_lock
- Explanation: drm_gpuvm_sm_map_exec_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_gpuvm *gpuvm', 'struct drm_exec *exec', 'unsigned int num_fences', 'u64 req_addr', 'u64 req_range', 'struct drm_gem_object *obj', 'u64 offset'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_gpuvm *gpuvm', 'struct drm_exec *exec', 'unsigned int num_fences', 'struct drm_gpuvm_map_req *req'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000679 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_gpuvm_sm_map_ops_create
- Explanation: drm_gpuvm_sm_map_ops_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_gpuvm *gpuvm', 'u64 addr', 'u64 range', 'struct drm_gem_object *obj', 'u64 offset'], 'return_type': 'struct drm_gpuva_ops *'}`
- New: `{'params': ['struct drm_gpuvm *gpuvm', 'const struct drm_gpuvm_map_req *req'], 'return_type': 'struct drm_gpuva_ops *'}`

### Rust Evidence

- Graph edges: `0`

## W-000681 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: generic___ffs
- Explanation: generic___ffs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned long word'], 'return_type': 'static __always_inline unsigned int'}`
- New: `{'params': ['unsigned long word'], 'return_type': 'static __always_inline __attribute_const__ unsigned int'}`

### Rust Evidence

- Graph edges: `0`

## W-000682 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: generic___fls
- Explanation: generic___fls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned long word'], 'return_type': 'static __always_inline unsigned int'}`
- New: `{'params': ['unsigned long word'], 'return_type': 'static __always_inline __attribute_const__ unsigned int'}`

### Rust Evidence

- Graph edges: `0`

## W-000683 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: generic_ci_validate_strict_name
- Explanation: generic_ci_validate_strict_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct inode *dir', 'struct qstr *name'], 'return_type': 'static inline bool'}`
- New: `{'params': ['struct inode *dir', 'const struct qstr *name'], 'return_type': 'static inline bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000684 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: generic_ffs
- Explanation: generic_ffs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['int x'], 'return_type': 'static inline int'}`
- New: `{'params': ['int x'], 'return_type': 'static inline __attribute_const__ int'}`

### Rust Evidence

- Graph edges: `0`

## W-000685 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: generic_fls
- Explanation: generic_fls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned int x'], 'return_type': 'static __always_inline int'}`
- New: `{'params': ['unsigned int x'], 'return_type': 'static __always_inline __attribute_const__ int'}`

### Rust Evidence

- Graph edges: `0`

## W-000686 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: hchacha_block
- Explanation: hchacha_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct chacha_state *state', 'u32 out[HCHACHA_OUT_WORDS]', 'int nrounds'], 'return_type': 'static inline void'}`
- New: `{'params': ['const struct chacha_state *state', 'u32 out[HCHACHA_OUT_WORDS]', 'int nrounds'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000687 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: hchacha_block_generic
- Explanation: hchacha_block_generic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['state', 'out', 'nrounds'], 'return_type': 'else'}`
- New: `{'params': ['const struct chacha_state *state', 'u32 out[HCHACHA_OUT_WORDS]', 'int nrounds'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000688 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: long
- Explanation: long changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['*get_unmapped_area)(struct file *, unsigned long, unsigned long, unsigned long, unsigned long'], 'return_type': 'unsigned'}`
- New: `{'params': ['*pagesize)(struct vm_area_struct * area'], 'return_type': 'unsigned'}`

### Rust Evidence

- Graph edges: `0`

## W-000689 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mapping_mapped
- Explanation: mapping_mapped changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct address_space *mapping'], 'return_type': 'static inline int'}`
- New: `{'params': ['const struct address_space *mapping'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `0`

## W-000690 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mapping_tagged
- Explanation: mapping_tagged changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct address_space *mapping', 'xa_mark_t tag'], 'return_type': 'static inline bool'}`
- New: `{'params': ['const struct address_space *mapping', 'xa_mark_t tag'], 'return_type': 'static inline bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000691 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mapping_writably_mapped
- Explanation: mapping_writably_mapped changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct address_space *mapping'], 'return_type': 'static inline int'}`
- New: `{'params': ['const struct address_space *mapping'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `0`

## W-000695 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: poly1305_block_init_generic
- Explanation: poly1305_block_init_generic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct poly1305_block_state *state', 'const u8 raw_key[POLY1305_BLOCK_SIZE]'], 'return_type': 'void'}`
- New: `{'params': ['struct poly1305_block_state *desc', 'const u8 raw_key[POLY1305_BLOCK_SIZE]'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-000696 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ptdesc_address
- Explanation: ptdesc_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['ptdesc'], 'return_type': 'return'}`
- New: `{'params': ['const struct ptdesc *pt'], 'return_type': 'static inline void *'}`

### Rust Evidence

- Graph edges: `0`

## W-000706 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: test_and_clear_bit
- Explanation: test_and_clear_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['cpumask_check(cpu)', 'cpumask_bits(cpumask)'], 'return_type': 'return'}`
- New: `{'params': ['flag', 'ACCESS_PRIVATE(&mm->flags, __mm_flags)'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-000707 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: test_and_set_bit
- Explanation: test_and_set_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['cpumask_check(cpu)', 'cpumask_bits(cpumask)'], 'return_type': 'return'}`
- New: `{'params': ['flag', 'ACCESS_PRIVATE(&mm->flags, __mm_flags)'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-000708 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: test_bit
- Explanation: test_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['cpumask_check(cpu)', 'cpumask_bits((cpumask))'], 'return_type': 'return'}`
- New: `{'params': ['PT_reserved', '&pt->pt_flags.f'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-000709 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vma_is_dax
- Explanation: vma_is_dax changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct vm_area_struct *vma'], 'return_type': 'static inline bool'}`
- New: `{'params': ['vma) || (vma->vm_file && (vma->vm_flags & (VM_PFNMAP | VM_MIXEDMAP))'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-000408 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: blk_mq_tags
- Explanation: blk_mq_tags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'nr_tags', 'type': 'ffi::c_uint'}, {'name': 'nr_reserved_tags', 'type': 'ffi::c_uint'}, {'name': 'active_queues', 'type': 'ffi::c_uint'}, {'name': 'bitmap_tags', 'type': 'sbitmap_queue'}, {'name': 'breserved_tags', 'type': 'sbitmap_queue'}, {'name': 'rqs', 'type': '*mut *mut request'}, {'name': 'static_rqs', 'type': '*mut *mut request'}, {'name': 'page_list', 'type': 'list_head'}, {'name': 'lock', 'type': 'spinlock_t'}]`
- New: `[{'name': 'nr_tags', 'type': 'ffi::c_uint'}, {'name': 'nr_reserved_tags', 'type': 'ffi::c_uint'}, {'name': 'active_queues', 'type': 'ffi::c_uint'}, {'name': 'bitmap_tags', 'type': 'sbitmap_queue'}, {'name': 'breserved_tags', 'type': 'sbitmap_queue'}, {'name': 'rqs', 'type': '*mut *mut request'}, {'name': 'static_rqs', 'type': '*mut *mut request'}, {'name': 'page_list', 'type': 'list_head'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'callback_head', 'type': 'callback_head'}]`

### Rust Evidence

- Graph edges: `3`

## W-000427 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: folio__bindgen_ty_1__bindgen_ty_1
- Explanation: folio__bindgen_ty_1__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'folio__bindgen_ty_1__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mapping', 'type': '*mut address_space'}, {'name': '__bindgen_anon_2', 'type': 'folio__bindgen_ty_1__bindgen_ty_1__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'folio__bindgen_ty_1__bindgen_ty_1__bindgen_ty_3'}, {'name': '_mapcount', 'type': 'atomic_t'}, {'name': '_refcount', 'type': 'atomic_t'}]`
- New: `[{'name': 'flags', 'type': 'memdesc_flags_t'}, {'name': '__bindgen_anon_1', 'type': 'folio__bindgen_ty_1__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mapping', 'type': '*mut address_space'}, {'name': '__bindgen_anon_2', 'type': 'folio__bindgen_ty_1__bindgen_ty_1__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'folio__bindgen_ty_1__bindgen_ty_1__bindgen_ty_3'}, {'name': '_mapcount', 'type': 'atomic_t'}, {'name': '_refcount', 'type': 'atomic_t'}]`

### Rust Evidence

- Graph edges: `2`

## W-000435 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: mm_struct__bindgen_ty_1
- Explanation: mm_struct__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'mm_struct__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mm_mt', 'type': 'maple_tree'}, {'name': 'mmap_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'task_size', 'type': 'ffi::c_ulong'}, {'name': 'pgd', 'type': '*mut pgd_t'}, {'name': 'membarrier_state', 'type': 'atomic_t'}, {'name': 'mm_users', 'type': 'atomic_t'}, {'name': 'pcpu_cid', 'type': '*mut mm_cid'}, {'name': 'mm_cid_next_scan', 'type': 'ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_uint'}, {'name': 'max_nr_cid', 'type': 'atomic_t'}, {'name': 'cpus_allowed_lock', 'type': 'raw_spinlock_t'}, {'name': 'pgtables_bytes', 'type': 'atomic_long_t'}, {'name': 'map_count', 'type': 'ffi::c_int'}, {'name': 'page_table_lock', 'type': 'spinlock_t'}, {'name': 'mmap_lock', 'type': 'rw_semaphore'}, {'name': 'mmlist', 'type': 'list_head'}, {'name': 'vma_writer_wait', 'type': 'rcuwait'}, {'name': 'mm_lock_seq', 'type': 'seqcount_t'}, {'name': 'futex_hash_lock', 'type': 'mutex'}, {'name': 'futex_phash', 'type': '*mut futex_private_hash'}, {'name': 'futex_phash_new', 'type': '*mut futex_private_hash'}, {'name': 'futex_batches', 'type': 'ffi::c_ulong'}, {'name': 'futex_rcu', 'type': 'callback_head'}, {'name': 'futex_atomic', 'type': 'atomic_long_t'}, {'name': 'futex_ref', 'type': '*mut ffi::c_uint'}, {'name': 'hiwater_rss', 'type': 'ffi::c_ulong'}, {'name': 'hiwater_vm', 'type': 'ffi::c_ulong'}, {'name': 'total_vm', 'type': 'ffi::c_ulong'}, {'name': 'locked_vm', 'type': 'ffi::c_ulong'}, {'name': 'pinned_vm', 'type': 'atomic64_t'}, {'name': 'data_vm', 'type': 'ffi::c_ulong'}, {'name': 'exec_vm', 'type': 'ffi::c_ulong'}, {'name': 'stack_vm', 'type': 'ffi::c_ulong'}, {'name': 'def_flags', 'type': 'vm_flags_t'}, {'name': 'write_protect_seq', 'type': 'seqcount_t'}, {'name': 'arg_lock', 'type': 'spinlock_t'}, {'name': 'start_code', 'type': 'ffi::c_ulong'}, {'name': 'end_code', 'type': 'ffi::c_ulong'}, {'name': 'start_data', 'type': 'ffi::c_ulong'}, {'name': 'end_data', 'type': 'ffi::c_ulong'}, {'name': 'start_brk', 'type': 'ffi::c_ulong'}, {'name': 'brk', 'type': 'ffi::c_ulong'}, {'name': 'start_stack', 'type': 'ffi::c_ulong'}, {'name': 'arg_start', 'type': 'ffi::c_ulong'}, {'name': 'arg_end', 'type': 'ffi::c_ulong'}, {'name': 'env_start', 'type': 'ffi::c_ulong'}, {'name': 'env_end', 'type': 'ffi::c_ulong'}, {'name': 'saved_auxv', 'type': '[ffi::c_ulong; 52usize]'}, {'name': 'rss_stat', 'type': '[percpu_counter; 4usize]'}, {'name': 'binfmt', 'type': '*mut linux_binfmt'}, {'name': 'context', 'type': 'mm_context_t'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'ioctx_lock', 'type': 'spinlock_t'}, {'name': 'ioctx_table', 'type': '*mut kioctx_table'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'exe_file', 'type': '*mut file'}, {'name': 'notifier_subscriptions', 'type': '*mut mmu_notifier_subscriptions'}, {'name': 'tlb_flush_pending', 'type': 'atomic_t'}, {'name': 'tlb_flush_batched', 'type': 'atomic_t'}, {'name': 'uprobes_state', 'type': 'uprobes_state'}, {'name': 'hugetlb_usage', 'type': 'atomic_long_t'}, {'name': 'async_put_work', 'type': 'work_struct'}, {'name': 'iommu_mm', 'type': '*mut iommu_mm_data'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'mm_struct__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mm_mt', 'type': 'maple_tree'}, {'name': 'mmap_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_base', 'type': 'ffi::c_ulong'}, {'name': 'mmap_compat_legacy_base', 'type': 'ffi::c_ulong'}, {'name': 'task_size', 'type': 'ffi::c_ulong'}, {'name': 'pgd', 'type': '*mut pgd_t'}, {'name': 'membarrier_state', 'type': 'atomic_t'}, {'name': 'mm_users', 'type': 'atomic_t'}, {'name': 'pcpu_cid', 'type': '*mut mm_cid'}, {'name': 'mm_cid_next_scan', 'type': 'ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_uint'}, {'name': 'max_nr_cid', 'type': 'atomic_t'}, {'name': 'cpus_allowed_lock', 'type': 'raw_spinlock_t'}, {'name': 'pgtables_bytes', 'type': 'atomic_long_t'}, {'name': 'map_count', 'type': 'ffi::c_int'}, {'name': 'page_table_lock', 'type': 'spinlock_t'}, {'name': 'mmap_lock', 'type': 'rw_semaphore'}, {'name': 'mmlist', 'type': 'list_head'}, {'name': 'vma_writer_wait', 'type': 'rcuwait'}, {'name': 'mm_lock_seq', 'type': 'seqcount_t'}, {'name': 'futex_hash_lock', 'type': 'mutex'}, {'name': 'futex_phash', 'type': '*mut futex_private_hash'}, {'name': 'futex_phash_new', 'type': '*mut futex_private_hash'}, {'name': 'futex_batches', 'type': 'ffi::c_ulong'}, {'name': 'futex_rcu', 'type': 'callback_head'}, {'name': 'futex_atomic', 'type': 'atomic_long_t'}, {'name': 'futex_ref', 'type': '*mut ffi::c_uint'}, {'name': 'hiwater_rss', 'type': 'ffi::c_ulong'}, {'name': 'hiwater_vm', 'type': 'ffi::c_ulong'}, {'name': 'total_vm', 'type': 'ffi::c_ulong'}, {'name': 'locked_vm', 'type': 'ffi::c_ulong'}, {'name': 'pinned_vm', 'type': 'atomic64_t'}, {'name': 'data_vm', 'type': 'ffi::c_ulong'}, {'name': 'exec_vm', 'type': 'ffi::c_ulong'}, {'name': 'stack_vm', 'type': 'ffi::c_ulong'}, {'name': 'def_flags', 'type': 'vm_flags_t'}, {'name': 'write_protect_seq', 'type': 'seqcount_t'}, {'name': 'arg_lock', 'type': 'spinlock_t'}, {'name': 'start_code', 'type': 'ffi::c_ulong'}, {'name': 'end_code', 'type': 'ffi::c_ulong'}, {'name': 'start_data', 'type': 'ffi::c_ulong'}, {'name': 'end_data', 'type': 'ffi::c_ulong'}, {'name': 'start_brk', 'type': 'ffi::c_ulong'}, {'name': 'brk', 'type': 'ffi::c_ulong'}, {'name': 'start_stack', 'type': 'ffi::c_ulong'}, {'name': 'arg_start', 'type': 'ffi::c_ulong'}, {'name': 'arg_end', 'type': 'ffi::c_ulong'}, {'name': 'env_start', 'type': 'ffi::c_ulong'}, {'name': 'env_end', 'type': 'ffi::c_ulong'}, {'name': 'saved_auxv', 'type': '[ffi::c_ulong; 52usize]'}, {'name': 'rss_stat', 'type': '[percpu_counter; 4usize]'}, {'name': 'binfmt', 'type': '*mut linux_binfmt'}, {'name': 'context', 'type': 'mm_context_t'}, {'name': 'flags', 'type': 'mm_flags_t'}, {'name': 'ioctx_lock', 'type': 'spinlock_t'}, {'name': 'ioctx_table', 'type': '*mut kioctx_table'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'exe_file', 'type': '*mut file'}, {'name': 'notifier_subscriptions', 'type': '*mut mmu_notifier_subscriptions'}, {'name': 'tlb_flush_pending', 'type': 'atomic_t'}, {'name': 'tlb_flush_batched', 'type': 'atomic_t'}, {'name': 'uprobes_state', 'type': 'uprobes_state'}, {'name': 'hugetlb_usage', 'type': 'atomic_long_t'}, {'name': 'async_put_work', 'type': 'work_struct'}, {'name': 'iommu_mm', 'type': '*mut iommu_mm_data'}]`

### Rust Evidence

- Graph edges: `2`

## W-000436 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: ns_common
- Explanation: ns_common changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'stashed', 'type': '*mut dentry'}, {'name': 'ops', 'type': '*const proc_ns_operations'}, {'name': 'inum', 'type': 'ffi::c_uint'}, {'name': 'count', 'type': 'refcount_t'}]`
- New: `[{'name': 'ns_type', 'type': 'u32_'}, {'name': 'stashed', 'type': '*mut dentry'}, {'name': 'ops', 'type': '*const proc_ns_operations'}, {'name': 'inum', 'type': 'ffi::c_uint'}, {'name': '__ns_ref', 'type': 'refcount_t'}, {'name': '__bindgen_anon_1', 'type': 'ns_common__bindgen_ty_1'}]`

### Rust Evidence

- Graph edges: `2`

## W-000440 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: ptdesc
- Explanation: ptdesc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__page_flags', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'ptdesc__bindgen_ty_1'}, {'name': '__page_mapping', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_2', 'type': 'ptdesc__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'ptdesc__bindgen_ty_3'}, {'name': '__page_type', 'type': 'ffi::c_uint'}, {'name': '__page_refcount', 'type': 'atomic_t'}]`
- New: `[{'name': 'pt_flags', 'type': 'memdesc_flags_t'}, {'name': '__bindgen_anon_1', 'type': 'ptdesc__bindgen_ty_1'}, {'name': '__page_mapping', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_2', 'type': 'ptdesc__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'ptdesc__bindgen_ty_3'}, {'name': '__page_type', 'type': 'ffi::c_uint'}, {'name': '__page_refcount', 'type': 'atomic_t'}]`

### Rust Evidence

- Graph edges: `2`

## W-000404 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: attribute_group
- Explanation: attribute_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'is_visible', 'type': '::core::option::Option<'}, {'name': 'is_bin_visible', 'type': '::core::option::Option<'}, {'name': 'bin_size', 'type': '::core::option::Option<'}, {'name': 'attrs', 'type': '*mut *mut attribute'}, {'name': '__bindgen_anon_1', 'type': 'attribute_group__bindgen_ty_1'}]`
- New: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'is_visible', 'type': '::core::option::Option<'}, {'name': 'is_bin_visible', 'type': '::core::option::Option<'}, {'name': 'bin_size', 'type': '::core::option::Option<'}, {'name': 'attrs', 'type': '*mut *mut attribute'}, {'name': 'bin_attrs', 'type': '*const *const bin_attribute'}]`

### Rust Evidence

- Graph edges: `1`

## W-000405 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bin_attribute
- Explanation: bin_attribute changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'attr', 'type': 'attribute'}, {'name': 'size', 'type': 'usize'}, {'name': 'private', 'type': '*mut ffi::c_void'}, {'name': 'f_mapping', 'type': '::core::option::Option<unsafe extern "C" fn() -> *mut address_space>'}, {'name': 'read', 'type': '::core::option::Option<'}, {'name': 'read_new', 'type': '::core::option::Option<'}, {'name': 'write', 'type': '::core::option::Option<'}, {'name': 'write_new', 'type': '::core::option::Option<'}, {'name': 'llseek', 'type': '::core::option::Option<'}, {'name': 'mmap', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'attr', 'type': 'attribute'}, {'name': 'size', 'type': 'usize'}, {'name': 'private', 'type': '*mut ffi::c_void'}, {'name': 'f_mapping', 'type': '::core::option::Option<unsafe extern "C" fn() -> *mut address_space>'}, {'name': 'read', 'type': '::core::option::Option<'}, {'name': 'write', 'type': '::core::option::Option<'}, {'name': 'llseek', 'type': '::core::option::Option<'}, {'name': 'mmap', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-000410 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bpf_attr__bindgen_ty_4
- Explanation: bpf_attr__bindgen_ty_4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'prog_type', 'type': '__u32'}, {'name': 'insn_cnt', 'type': '__u32'}, {'name': 'insns', 'type': '__u64'}, {'name': 'license', 'type': '__u64'}, {'name': 'log_level', 'type': '__u32'}, {'name': 'log_size', 'type': '__u32'}, {'name': 'log_buf', 'type': '__u64'}, {'name': 'kern_version', 'type': '__u32'}, {'name': 'prog_flags', 'type': '__u32'}, {'name': 'prog_name', 'type': '[ffi::c_char; 16usize]'}, {'name': 'prog_ifindex', 'type': '__u32'}, {'name': 'expected_attach_type', 'type': '__u32'}, {'name': 'prog_btf_fd', 'type': '__u32'}, {'name': 'func_info_rec_size', 'type': '__u32'}, {'name': 'func_info', 'type': '__u64'}, {'name': 'func_info_cnt', 'type': '__u32'}, {'name': 'line_info_rec_size', 'type': '__u32'}, {'name': 'line_info', 'type': '__u64'}, {'name': 'line_info_cnt', 'type': '__u32'}, {'name': 'attach_btf_id', 'type': '__u32'}, {'name': '__bindgen_anon_1', 'type': 'bpf_attr__bindgen_ty_4__bindgen_ty_1'}, {'name': 'core_relo_cnt', 'type': '__u32'}, {'name': 'fd_array', 'type': '__u64'}, {'name': 'core_relos', 'type': '__u64'}, {'name': 'core_relo_rec_size', 'type': '__u32'}, {'name': 'log_true_size', 'type': '__u32'}, {'name': 'prog_token_fd', 'type': '__s32'}, {'name': 'fd_array_cnt', 'type': '__u32'}]`
- New: `[{'name': 'prog_type', 'type': '__u32'}, {'name': 'insn_cnt', 'type': '__u32'}, {'name': 'insns', 'type': '__u64'}, {'name': 'license', 'type': '__u64'}, {'name': 'log_level', 'type': '__u32'}, {'name': 'log_size', 'type': '__u32'}, {'name': 'log_buf', 'type': '__u64'}, {'name': 'kern_version', 'type': '__u32'}, {'name': 'prog_flags', 'type': '__u32'}, {'name': 'prog_name', 'type': '[ffi::c_char; 16usize]'}, {'name': 'prog_ifindex', 'type': '__u32'}, {'name': 'expected_attach_type', 'type': '__u32'}, {'name': 'prog_btf_fd', 'type': '__u32'}, {'name': 'func_info_rec_size', 'type': '__u32'}, {'name': 'func_info', 'type': '__u64'}, {'name': 'func_info_cnt', 'type': '__u32'}, {'name': 'line_info_rec_size', 'type': '__u32'}, {'name': 'line_info', 'type': '__u64'}, {'name': 'line_info_cnt', 'type': '__u32'}, {'name': 'attach_btf_id', 'type': '__u32'}, {'name': '__bindgen_anon_1', 'type': 'bpf_attr__bindgen_ty_4__bindgen_ty_1'}, {'name': 'core_relo_cnt', 'type': '__u32'}, {'name': 'fd_array', 'type': '__u64'}, {'name': 'core_relos', 'type': '__u64'}, {'name': 'core_relo_rec_size', 'type': '__u32'}, {'name': 'log_true_size', 'type': '__u32'}, {'name': 'prog_token_fd', 'type': '__s32'}, {'name': 'fd_array_cnt', 'type': '__u32'}, {'name': 'signature', 'type': '__u64'}, {'name': 'signature_size', 'type': '__u32'}, {'name': 'keyring_id', 'type': '__s32'}]`

### Rust Evidence

- Graph edges: `1`

## W-000412 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bpf_map_info
- Explanation: bpf_map_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'type_', 'type': '__u32'}, {'name': 'id', 'type': '__u32'}, {'name': 'key_size', 'type': '__u32'}, {'name': 'value_size', 'type': '__u32'}, {'name': 'max_entries', 'type': '__u32'}, {'name': 'map_flags', 'type': '__u32'}, {'name': 'name', 'type': '[ffi::c_char; 16usize]'}, {'name': 'ifindex', 'type': '__u32'}, {'name': 'btf_vmlinux_value_type_id', 'type': '__u32'}, {'name': 'netns_dev', 'type': '__u64'}, {'name': 'netns_ino', 'type': '__u64'}, {'name': 'btf_id', 'type': '__u32'}, {'name': 'btf_key_type_id', 'type': '__u32'}, {'name': 'btf_value_type_id', 'type': '__u32'}, {'name': 'btf_vmlinux_id', 'type': '__u32'}, {'name': 'map_extra', 'type': '__u64'}]`
- New: `[{'name': 'type_', 'type': '__u32'}, {'name': 'id', 'type': '__u32'}, {'name': 'key_size', 'type': '__u32'}, {'name': 'value_size', 'type': '__u32'}, {'name': 'max_entries', 'type': '__u32'}, {'name': 'map_flags', 'type': '__u32'}, {'name': 'name', 'type': '[ffi::c_char; 16usize]'}, {'name': 'ifindex', 'type': '__u32'}, {'name': 'btf_vmlinux_value_type_id', 'type': '__u32'}, {'name': 'netns_dev', 'type': '__u64'}, {'name': 'netns_ino', 'type': '__u64'}, {'name': 'btf_id', 'type': '__u32'}, {'name': 'btf_key_type_id', 'type': '__u32'}, {'name': 'btf_value_type_id', 'type': '__u32'}, {'name': 'btf_vmlinux_id', 'type': '__u32'}, {'name': 'map_extra', 'type': '__u64'}, {'name': 'hash', 'type': '__u64'}, {'name': 'hash_size', 'type': '__u32'}]`

### Rust Evidence

- Graph edges: `1`

## W-000413 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bpf_map_ops
- Explanation: bpf_map_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'map_free', 'type': '::core::option::Option<unsafe extern "C" fn(map: *mut bpf_map)>'}, {'name': 'map_get_next_key', 'type': '::core::option::Option<'}, {'name': 'map_release_uref', 'type': '::core::option::Option<unsafe extern "C" fn(map: *mut bpf_map)>'}, {'name': 'map_lookup_elem_sys_only', 'type': '::core::option::Option<'}, {'name': 'map_lookup_batch', 'type': '::core::option::Option<'}, {'name': 'map_lookup_and_delete_elem', 'type': '::core::option::Option<'}, {'name': 'map_lookup_and_delete_batch', 'type': '::core::option::Option<'}, {'name': 'map_update_batch', 'type': '::core::option::Option<'}, {'name': 'map_delete_batch', 'type': '::core::option::Option<'}, {'name': 'map_lookup_elem', 'type': '::core::option::Option<'}, {'name': 'map_update_elem', 'type': '::core::option::Option<'}, {'name': 'map_delete_elem', 'type': '::core::option::Option<'}, {'name': 'map_push_elem', 'type': '::core::option::Option<'}, {'name': 'map_pop_elem', 'type': '::core::option::Option<'}, {'name': 'map_peek_elem', 'type': '::core::option::Option<'}, {'name': 'map_lookup_percpu_elem', 'type': '::core::option::Option<'}, {'name': 'map_fd_get_ptr', 'type': '::core::option::Option<'}, {'name': 'map_fd_put_ptr', 'type': '::core::option::Option<'}, {'name': 'map_gen_lookup', 'type': '::core::option::Option<'}, {'name': 'map_seq_show_elem', 'type': '::core::option::Option<'}, {'name': 'map_check_btf', 'type': '::core::option::Option<'}, {'name': 'map_poke_track', 'type': '::core::option::Option<'}, {'name': 'map_poke_run', 'type': '::core::option::Option<'}, {'name': 'map_direct_value_addr', 'type': '::core::option::Option<'}, {'name': 'map_direct_value_meta', 'type': '::core::option::Option<'}, {'name': 'map_mmap', 'type': '::core::option::Option<'}, {'name': 'map_poll', 'type': '::core::option::Option<'}, {'name': 'map_get_unmapped_area', 'type': '::core::option::Option<'}, {'name': 'map_local_storage_charge', 'type': '::core::option::Option<'}, {'name': 'map_local_storage_uncharge', 'type': '::core::option::Option<'}, {'name': 'map_owner_storage_ptr', 'type': '::core::option::Option<'}, {'name': 'map_redirect', 'type': '::core::option::Option<'}, {'name': 'map_meta_equal', 'type': '::core::option::Option<'}, {'name': 'map_set_for_each_callback_args', 'type': '::core::option::Option<'}, {'name': 'map_for_each_callback', 'type': '::core::option::Option<'}, {'name': 'map_mem_usage', 'type': '::core::option::Option<unsafe extern "C" fn(map: *const bpf_map) -> u64_>'}, {'name': 'map_btf_id', 'type': '*mut ffi::c_int'}, {'name': 'iter_seq_info', 'type': '*const bpf_iter_seq_info'}]`
- New: `[{'name': 'map_free', 'type': '::core::option::Option<unsafe extern "C" fn(map: *mut bpf_map)>'}, {'name': 'map_get_next_key', 'type': '::core::option::Option<'}, {'name': 'map_release_uref', 'type': '::core::option::Option<unsafe extern "C" fn(map: *mut bpf_map)>'}, {'name': 'map_lookup_elem_sys_only', 'type': '::core::option::Option<'}, {'name': 'map_lookup_batch', 'type': '::core::option::Option<'}, {'name': 'map_lookup_and_delete_elem', 'type': '::core::option::Option<'}, {'name': 'map_lookup_and_delete_batch', 'type': '::core::option::Option<'}, {'name': 'map_update_batch', 'type': '::core::option::Option<'}, {'name': 'map_delete_batch', 'type': '::core::option::Option<'}, {'name': 'map_lookup_elem', 'type': '::core::option::Option<'}, {'name': 'map_update_elem', 'type': '::core::option::Option<'}, {'name': 'map_delete_elem', 'type': '::core::option::Option<'}, {'name': 'map_push_elem', 'type': '::core::option::Option<'}, {'name': 'map_pop_elem', 'type': '::core::option::Option<'}, {'name': 'map_peek_elem', 'type': '::core::option::Option<'}, {'name': 'map_lookup_percpu_elem', 'type': '::core::option::Option<'}, {'name': 'map_get_hash', 'type': '::core::option::Option<'}, {'name': 'map_fd_get_ptr', 'type': '::core::option::Option<'}, {'name': 'map_fd_put_ptr', 'type': '::core::option::Option<'}, {'name': 'map_gen_lookup', 'type': '::core::option::Option<'}, {'name': 'map_seq_show_elem', 'type': '::core::option::Option<'}, {'name': 'map_check_btf', 'type': '::core::option::Option<'}, {'name': 'map_poke_track', 'type': '::core::option::Option<'}, {'name': 'map_poke_run', 'type': '::core::option::Option<'}, {'name': 'map_direct_value_addr', 'type': '::core::option::Option<'}, {'name': 'map_direct_value_meta', 'type': '::core::option::Option<'}, {'name': 'map_mmap', 'type': '::core::option::Option<'}, {'name': 'map_poll', 'type': '::core::option::Option<'}, {'name': 'map_get_unmapped_area', 'type': '::core::option::Option<'}, {'name': 'map_local_storage_charge', 'type': '::core::option::Option<'}, {'name': 'map_local_storage_uncharge', 'type': '::core::option::Option<'}, {'name': 'map_owner_storage_ptr', 'type': '::core::option::Option<'}, {'name': 'map_redirect', 'type': '::core::option::Option<'}, {'name': 'map_meta_equal', 'type': '::core::option::Option<'}, {'name': 'map_set_for_each_callback_args', 'type': '::core::option::Option<'}, {'name': 'map_for_each_callback', 'type': '::core::option::Option<'}, {'name': 'map_mem_usage', 'type': '::core::option::Option<unsafe extern "C" fn(map: *const bpf_map) -> u64_>'}, {'name': 'map_btf_id', 'type': '*mut ffi::c_int'}, {'name': 'iter_seq_info', 'type': '*const bpf_iter_seq_info'}]`

### Rust Evidence

- Graph edges: `1`

## W-000414 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bpf_map_owner
- Explanation: bpf_map_owner changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'type_', 'type': 'bpf_prog_type'}, {'name': 'jited', 'type': 'bool_'}, {'name': 'xdp_has_frags', 'type': 'bool_'}, {'name': 'storage_cookie', 'type': '[u64_; 2usize]'}, {'name': 'attach_func_proto', 'type': '*const btf_type'}]`
- New: `[{'name': 'type_', 'type': 'bpf_prog_type'}, {'name': 'jited', 'type': 'bool_'}, {'name': 'xdp_has_frags', 'type': 'bool_'}, {'name': 'storage_cookie', 'type': '[u64_; 2usize]'}, {'name': 'attach_func_proto', 'type': '*const btf_type'}, {'name': 'expected_attach_type', 'type': 'bpf_attach_type'}]`

### Rust Evidence

- Graph edges: `1`

## W-000416 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bpf_prog_aux
- Explanation: bpf_prog_aux changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'refcnt', 'type': 'atomic64_t'}, {'name': 'used_map_cnt', 'type': 'u32_'}, {'name': 'used_btf_cnt', 'type': 'u32_'}, {'name': 'max_ctx_offset', 'type': 'u32_'}, {'name': 'max_pkt_offset', 'type': 'u32_'}, {'name': 'max_tp_access', 'type': 'u32_'}, {'name': 'stack_depth', 'type': 'u32_'}, {'name': 'id', 'type': 'u32_'}, {'name': 'func_cnt', 'type': 'u32_'}, {'name': 'real_func_cnt', 'type': 'u32_'}, {'name': 'func_idx', 'type': 'u32_'}, {'name': 'attach_btf_id', 'type': 'u32_'}, {'name': 'attach_st_ops_member_off', 'type': 'u32_'}, {'name': 'ctx_arg_info_size', 'type': 'u32_'}, {'name': 'max_rdonly_access', 'type': 'u32_'}, {'name': 'max_rdwr_access', 'type': 'u32_'}, {'name': 'attach_btf', 'type': '*mut btf'}, {'name': 'ctx_arg_info', 'type': '*mut bpf_ctx_arg_aux'}, {'name': 'priv_stack_ptr', 'type': '*mut ffi::c_void'}, {'name': 'dst_mutex', 'type': 'mutex'}, {'name': 'dst_prog', 'type': '*mut bpf_prog'}, {'name': 'dst_trampoline', 'type': '*mut bpf_trampoline'}, {'name': 'saved_dst_prog_type', 'type': 'bpf_prog_type'}, {'name': 'saved_dst_attach_type', 'type': 'bpf_attach_type'}, {'name': 'verifier_zext', 'type': 'bool_'}, {'name': 'dev_bound', 'type': 'bool_'}, {'name': 'offload_requested', 'type': 'bool_'}, {'name': 'attach_btf_trace', 'type': 'bool_'}, {'name': 'attach_tracing_prog', 'type': 'bool_'}, {'name': 'func_proto_unreliable', 'type': 'bool_'}, {'name': 'tail_call_reachable', 'type': 'bool_'}, {'name': 'xdp_has_frags', 'type': 'bool_'}, {'name': 'exception_cb', 'type': 'bool_'}, {'name': 'exception_boundary', 'type': 'bool_'}, {'name': 'is_extended', 'type': 'bool_'}, {'name': 'jits_use_priv_stack', 'type': 'bool_'}, {'name': 'priv_stack_requested', 'type': 'bool_'}, {'name': 'changes_pkt_data', 'type': 'bool_'}, {'name': 'might_sleep', 'type': 'bool_'}, {'name': 'prog_array_member_cnt', 'type': 'u64_'}, {'name': 'ext_mutex', 'type': 'mutex'}, {'name': 'arena', 'type': '*mut bpf_arena'}, {'name': 'recursion_detected', 'type': '::core::option::Option<unsafe extern "C" fn(prog: *mut bpf_prog)>'}, {'name': 'attach_func_proto', 'type': '*const btf_type'}, {'name': 'attach_func_name', 'type': '*const ffi::c_char'}, {'name': 'func', 'type': '*mut *mut bpf_prog'}, {'name': 'jit_data', 'type': '*mut ffi::c_void'}, {'name': 'poke_tab', 'type': '*mut bpf_jit_poke_descriptor'}, {'name': 'kfunc_tab', 'type': '*mut bpf_kfunc_desc_tab'}, {'name': 'kfunc_btf_tab', 'type': '*mut bpf_kfunc_btf_tab'}, {'name': 'size_poke_tab', 'type': 'u32_'}, {'name': 'ksym', 'type': 'bpf_ksym'}, {'name': 'ops', 'type': '*const bpf_prog_ops'}, {'name': 'st_ops', 'type': '*const bpf_struct_ops'}, {'name': 'used_maps', 'type': '*mut *mut bpf_map'}, {'name': 'used_maps_mutex', 'type': 'mutex'}, {'name': 'used_btfs', 'type': '*mut btf_mod_pair'}, {'name': 'prog', 'type': '*mut bpf_prog'}, {'name': 'user', 'type': '*mut user_struct'}, {'name': 'load_time', 'type': 'u64_'}, {'name': 'verified_insns', 'type': 'u32_'}, {'name': 'cgroup_atype', 'type': 'ffi::c_int'}, {'name': 'cgroup_storage', 'type': '[*mut bpf_map; 2usize]'}, {'name': 'name', 'type': '[ffi::c_char; 16usize]'}, {'name': 'bpf_exception_cb', 'type': '::core::option::Option<'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'token', 'type': '*mut bpf_token'}, {'name': 'offload', 'type': '*mut bpf_prog_offload'}, {'name': 'btf', 'type': '*mut btf'}, {'name': 'func_info', 'type': '*mut bpf_func_info'}, {'name': 'func_info_aux', 'type': '*mut bpf_func_info_aux'}, {'name': 'linfo', 'type': '*mut bpf_line_info'}, {'name': 'jited_linfo', 'type': '*mut *mut ffi::c_void'}, {'name': 'func_info_cnt', 'type': 'u32_'}, {'name': 'nr_linfo', 'type': 'u32_'}, {'name': 'linfo_idx', 'type': 'u32_'}, {'name': 'mod_', 'type': '*mut module'}, {'name': 'num_exentries', 'type': 'u32_'}, {'name': 'extable', 'type': '*mut exception_table_entry'}, {'name': '__bindgen_anon_1', 'type': 'bpf_prog_aux__bindgen_ty_1'}, {'name': 'stream', 'type': '[bpf_stream; 2usize]'}]`
- New: `[{'name': 'refcnt', 'type': 'atomic64_t'}, {'name': 'used_map_cnt', 'type': 'u32_'}, {'name': 'used_btf_cnt', 'type': 'u32_'}, {'name': 'max_ctx_offset', 'type': 'u32_'}, {'name': 'max_pkt_offset', 'type': 'u32_'}, {'name': 'max_tp_access', 'type': 'u32_'}, {'name': 'stack_depth', 'type': 'u32_'}, {'name': 'id', 'type': 'u32_'}, {'name': 'func_cnt', 'type': 'u32_'}, {'name': 'real_func_cnt', 'type': 'u32_'}, {'name': 'func_idx', 'type': 'u32_'}, {'name': 'attach_btf_id', 'type': 'u32_'}, {'name': 'attach_st_ops_member_off', 'type': 'u32_'}, {'name': 'ctx_arg_info_size', 'type': 'u32_'}, {'name': 'max_rdonly_access', 'type': 'u32_'}, {'name': 'max_rdwr_access', 'type': 'u32_'}, {'name': 'attach_btf', 'type': '*mut btf'}, {'name': 'ctx_arg_info', 'type': '*mut bpf_ctx_arg_aux'}, {'name': 'priv_stack_ptr', 'type': '*mut ffi::c_void'}, {'name': 'dst_mutex', 'type': 'mutex'}, {'name': 'dst_prog', 'type': '*mut bpf_prog'}, {'name': 'dst_trampoline', 'type': '*mut bpf_trampoline'}, {'name': 'saved_dst_prog_type', 'type': 'bpf_prog_type'}, {'name': 'saved_dst_attach_type', 'type': 'bpf_attach_type'}, {'name': 'verifier_zext', 'type': 'bool_'}, {'name': 'dev_bound', 'type': 'bool_'}, {'name': 'offload_requested', 'type': 'bool_'}, {'name': 'attach_btf_trace', 'type': 'bool_'}, {'name': 'attach_tracing_prog', 'type': 'bool_'}, {'name': 'func_proto_unreliable', 'type': 'bool_'}, {'name': 'tail_call_reachable', 'type': 'bool_'}, {'name': 'xdp_has_frags', 'type': 'bool_'}, {'name': 'exception_cb', 'type': 'bool_'}, {'name': 'exception_boundary', 'type': 'bool_'}, {'name': 'is_extended', 'type': 'bool_'}, {'name': 'jits_use_priv_stack', 'type': 'bool_'}, {'name': 'priv_stack_requested', 'type': 'bool_'}, {'name': 'changes_pkt_data', 'type': 'bool_'}, {'name': 'might_sleep', 'type': 'bool_'}, {'name': 'kprobe_write_ctx', 'type': 'bool_'}, {'name': 'prog_array_member_cnt', 'type': 'u64_'}, {'name': 'ext_mutex', 'type': 'mutex'}, {'name': 'arena', 'type': '*mut bpf_arena'}, {'name': 'recursion_detected', 'type': '::core::option::Option<unsafe extern "C" fn(prog: *mut bpf_prog)>'}, {'name': 'attach_func_proto', 'type': '*const btf_type'}, {'name': 'attach_func_name', 'type': '*const ffi::c_char'}, {'name': 'func', 'type': '*mut *mut bpf_prog'}, {'name': 'main_prog_aux', 'type': '*mut bpf_prog_aux'}, {'name': 'jit_data', 'type': '*mut ffi::c_void'}, {'name': 'poke_tab', 'type': '*mut bpf_jit_poke_descriptor'}, {'name': 'kfunc_tab', 'type': '*mut bpf_kfunc_desc_tab'}, {'name': 'kfunc_btf_tab', 'type': '*mut bpf_kfunc_btf_tab'}, {'name': 'size_poke_tab', 'type': 'u32_'}, {'name': 'ksym', 'type': 'bpf_ksym'}, {'name': 'ops', 'type': '*const bpf_prog_ops'}, {'name': 'st_ops', 'type': '*const bpf_struct_ops'}, {'name': 'used_maps', 'type': '*mut *mut bpf_map'}, {'name': 'used_maps_mutex', 'type': 'mutex'}, {'name': 'used_btfs', 'type': '*mut btf_mod_pair'}, {'name': 'prog', 'type': '*mut bpf_prog'}, {'name': 'user', 'type': '*mut user_struct'}, {'name': 'load_time', 'type': 'u64_'}, {'name': 'verified_insns', 'type': 'u32_'}, {'name': 'cgroup_atype', 'type': 'ffi::c_int'}, {'name': 'cgroup_storage', 'type': '[*mut bpf_map; 2usize]'}, {'name': 'name', 'type': '[ffi::c_char; 16usize]'}, {'name': 'bpf_exception_cb', 'type': '::core::option::Option<'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'token', 'type': '*mut bpf_token'}, {'name': 'offload', 'type': '*mut bpf_prog_offload'}, {'name': 'btf', 'type': '*mut btf'}, {'name': 'func_info', 'type': '*mut bpf_func_info'}, {'name': 'func_info_aux', 'type': '*mut bpf_func_info_aux'}, {'name': 'linfo', 'type': '*mut bpf_line_info'}, {'name': 'jited_linfo', 'type': '*mut *mut ffi::c_void'}, {'name': 'func_info_cnt', 'type': 'u32_'}, {'name': 'nr_linfo', 'type': 'u32_'}, {'name': 'linfo_idx', 'type': 'u32_'}, {'name': 'mod_', 'type': '*mut module'}, {'name': 'num_exentries', 'type': 'u32_'}, {'name': 'extable', 'type': '*mut exception_table_entry'}, {'name': '__bindgen_anon_1', 'type': 'bpf_prog_aux__bindgen_ty_1'}, {'name': 'stream', 'type': '[bpf_stream; 2usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000417 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: btf_record
- Explanation: btf_record changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'cnt', 'type': 'u32_'}, {'name': 'field_mask', 'type': 'u32_'}, {'name': 'spin_lock_off', 'type': 'ffi::c_int'}, {'name': 'res_spin_lock_off', 'type': 'ffi::c_int'}, {'name': 'timer_off', 'type': 'ffi::c_int'}, {'name': 'wq_off', 'type': 'ffi::c_int'}, {'name': 'refcount_off', 'type': 'ffi::c_int'}, {'name': 'fields', 'type': '__IncompleteArrayField<btf_field>'}]`
- New: `[{'name': 'cnt', 'type': 'u32_'}, {'name': 'field_mask', 'type': 'u32_'}, {'name': 'spin_lock_off', 'type': 'ffi::c_int'}, {'name': 'res_spin_lock_off', 'type': 'ffi::c_int'}, {'name': 'timer_off', 'type': 'ffi::c_int'}, {'name': 'wq_off', 'type': 'ffi::c_int'}, {'name': 'refcount_off', 'type': 'ffi::c_int'}, {'name': 'task_work_off', 'type': 'ffi::c_int'}, {'name': 'fields', 'type': '__IncompleteArrayField<btf_field>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000418 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: cgroup_freezer_state
- Explanation: cgroup_freezer_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'freeze', 'type': 'bool_'}, {'name': 'e_freeze', 'type': 'bool_'}, {'name': 'nr_frozen_descendants', 'type': 'ffi::c_int'}, {'name': 'nr_frozen_tasks', 'type': 'ffi::c_int'}]`
- New: `[{'name': 'freeze', 'type': 'bool_'}, {'name': 'e_freeze', 'type': 'bool_'}, {'name': 'nr_frozen_descendants', 'type': 'ffi::c_int'}, {'name': 'nr_frozen_tasks', 'type': 'ffi::c_int'}, {'name': 'freeze_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'freeze_start_nsec', 'type': 'u64_'}, {'name': 'frozen_nsec', 'type': 'u64_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000420 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: debugfs_regset32
- Explanation: debugfs_regset32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'regs', 'type': '*const debugfs_reg32'}, {'name': 'nregs', 'type': 'ffi::c_int'}, {'name': 'base', 'type': '*mut ffi::c_void'}, {'name': 'dev', 'type': '*mut device'}]`

### Rust Evidence

- Graph edges: `1`

## W-000423 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: drm_gem_object__bindgen_ty_1
- Explanation: drm_gem_object__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'list', 'type': 'list_head'}]`
- New: `[{'name': 'list', 'type': 'list_head'}, {'name': 'lock', 'type': 'mutex'}]`

### Rust Evidence

- Graph edges: `1`

## W-000425 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: files_struct
- Explanation: files_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[{'name': 'count', 'type': 'atomic_t'}, {'name': 'resize_in_progress', 'type': 'bool_'}, {'name': 'resize_wait', 'type': 'wait_queue_head_t'}, {'name': 'fdt', 'type': '*mut fdtable'}, {'name': 'fdtab', 'type': 'fdtable'}, {'name': '__bindgen_padding_0', 'type': '[u32; 8usize]'}, {'name': 'file_lock', 'type': 'spinlock_t'}, {'name': 'next_fd', 'type': 'ffi::c_uint'}, {'name': 'close_on_exec_init', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'open_fds_init', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'full_fds_bits_init', 'type': '[ffi::c_ulong; 1usize]'}, {'name': 'fd_array', 'type': '[*mut file; 64usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000426 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: flowi_common
- Explanation: flowi_common changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'flowic_oif', 'type': 'ffi::c_int'}, {'name': 'flowic_iif', 'type': 'ffi::c_int'}, {'name': 'flowic_l3mdev', 'type': 'ffi::c_int'}, {'name': 'flowic_mark', 'type': '__u32'}, {'name': 'flowic_tos', 'type': '__u8'}, {'name': 'flowic_scope', 'type': '__u8'}, {'name': 'flowic_proto', 'type': '__u8'}, {'name': 'flowic_flags', 'type': '__u8'}, {'name': 'flowic_secid', 'type': '__u32'}, {'name': 'flowic_uid', 'type': 'kuid_t'}, {'name': 'flowic_multipath_hash', 'type': '__u32'}, {'name': 'flowic_tun_key', 'type': 'flowi_tunnel'}]`
- New: `[{'name': 'flowic_oif', 'type': 'ffi::c_int'}, {'name': 'flowic_iif', 'type': 'ffi::c_int'}, {'name': 'flowic_l3mdev', 'type': 'ffi::c_int'}, {'name': 'flowic_mark', 'type': '__u32'}, {'name': 'flowic_dscp', 'type': 'dscp_t'}, {'name': 'flowic_scope', 'type': '__u8'}, {'name': 'flowic_proto', 'type': '__u8'}, {'name': 'flowic_flags', 'type': '__u8'}, {'name': 'flowic_secid', 'type': '__u32'}, {'name': 'flowic_uid', 'type': 'kuid_t'}, {'name': 'flowic_multipath_hash', 'type': '__u32'}, {'name': 'flowic_tun_key', 'type': 'flowi_tunnel'}]`

### Rust Evidence

- Graph edges: `1`

## W-000428 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: hrtimer_clock_base
- Explanation: hrtimer_clock_base changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'cpu_base', 'type': '*mut hrtimer_cpu_base'}, {'name': 'index', 'type': 'ffi::c_uint'}, {'name': 'clockid', 'type': 'clockid_t'}, {'name': 'seq', 'type': 'seqcount_raw_spinlock_t'}, {'name': 'running', 'type': '*mut hrtimer'}, {'name': 'active', 'type': 'timerqueue_head'}, {'name': 'get_time', 'type': '::core::option::Option<unsafe extern "C" fn() -> ktime_t>'}, {'name': 'offset', 'type': 'ktime_t'}]`
- New: `[{'name': 'cpu_base', 'type': '*mut hrtimer_cpu_base'}, {'name': 'index', 'type': 'ffi::c_uint'}, {'name': 'clockid', 'type': 'clockid_t'}, {'name': 'seq', 'type': 'seqcount_raw_spinlock_t'}, {'name': 'running', 'type': '*mut hrtimer'}, {'name': 'active', 'type': 'timerqueue_head'}, {'name': 'offset', 'type': 'ktime_t'}]`

### Rust Evidence

- Graph edges: `1`

## W-000430 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: kmem_cache_args
- Explanation: kmem_cache_args changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'align', 'type': 'ffi::c_uint'}, {'name': 'useroffset', 'type': 'ffi::c_uint'}, {'name': 'usersize', 'type': 'ffi::c_uint'}, {'name': 'freeptr_offset', 'type': 'ffi::c_uint'}, {'name': 'use_freeptr_offset', 'type': 'bool_'}, {'name': 'ctor', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut ffi::c_void)>'}]`
- New: `[{'name': 'align', 'type': 'ffi::c_uint'}, {'name': 'useroffset', 'type': 'ffi::c_uint'}, {'name': 'usersize', 'type': 'ffi::c_uint'}, {'name': 'freeptr_offset', 'type': 'ffi::c_uint'}, {'name': 'use_freeptr_offset', 'type': 'bool_'}, {'name': 'ctor', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut ffi::c_void)>'}, {'name': 'sheaf_capacity', 'type': 'ffi::c_uint'}]`

### Rust Evidence

- Graph edges: `1`

## W-000433 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: local_trylock_t
- Explanation: local_trylock_t changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'llock', 'type': 'local_lock_t'}, {'name': 'acquired', 'type': 'u8_'}]`
- New: `[{'name': 'acquired', 'type': 'u8_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000438 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: per_cpu_nodestat
- Explanation: per_cpu_nodestat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'stat_threshold', 'type': 's8'}, {'name': 'vm_node_stat_diff', 'type': '[s8; 47usize]'}]`
- New: `[{'name': 'stat_threshold', 'type': 's8'}, {'name': 'vm_node_stat_diff', 'type': '[s8; 48usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000439 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: pglist_data
- Explanation: pglist_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'node_zones', 'type': '[zone; 4usize]'}, {'name': 'node_zonelists', 'type': '[zonelist; 2usize]'}, {'name': 'nr_zones', 'type': 'ffi::c_int'}, {'name': 'node_start_pfn', 'type': 'ffi::c_ulong'}, {'name': 'node_present_pages', 'type': 'ffi::c_ulong'}, {'name': 'node_spanned_pages', 'type': 'ffi::c_ulong'}, {'name': 'node_id', 'type': 'ffi::c_int'}, {'name': 'kswapd_wait', 'type': 'wait_queue_head_t'}, {'name': 'pfmemalloc_wait', 'type': 'wait_queue_head_t'}, {'name': 'reclaim_wait', 'type': '[wait_queue_head_t; 4usize]'}, {'name': 'nr_writeback_throttled', 'type': 'atomic_t'}, {'name': 'nr_reclaim_start', 'type': 'ffi::c_ulong'}, {'name': 'kswapd', 'type': '*mut task_struct'}, {'name': 'kswapd_order', 'type': 'ffi::c_int'}, {'name': 'kswapd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kswapd_failures', 'type': 'ffi::c_int'}, {'name': 'kcompactd_max_order', 'type': 'ffi::c_int'}, {'name': 'kcompactd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kcompactd_wait', 'type': 'wait_queue_head_t'}, {'name': 'kcompactd', 'type': '*mut task_struct'}, {'name': 'proactive_compact_trigger', 'type': 'bool_'}, {'name': 'totalreserve_pages', 'type': 'ffi::c_ulong'}, {'name': 'min_unmapped_pages', 'type': 'ffi::c_ulong'}, {'name': 'min_slab_pages', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': '__lruvec', 'type': 'lruvec'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_padding_1', 'type': '[u64; 6usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'per_cpu_nodestats', 'type': '*mut per_cpu_nodestat'}, {'name': 'vm_stat', 'type': '[atomic_long_t; 47usize]'}, {'name': 'memtier', 'type': '*mut memory_tier'}]`
- New: `[{'name': 'node_zones', 'type': '[zone; 4usize]'}, {'name': 'node_zonelists', 'type': '[zonelist; 2usize]'}, {'name': 'nr_zones', 'type': 'ffi::c_int'}, {'name': 'node_start_pfn', 'type': 'ffi::c_ulong'}, {'name': 'node_present_pages', 'type': 'ffi::c_ulong'}, {'name': 'node_spanned_pages', 'type': 'ffi::c_ulong'}, {'name': 'node_id', 'type': 'ffi::c_int'}, {'name': 'kswapd_wait', 'type': 'wait_queue_head_t'}, {'name': 'pfmemalloc_wait', 'type': 'wait_queue_head_t'}, {'name': 'reclaim_wait', 'type': '[wait_queue_head_t; 4usize]'}, {'name': 'nr_writeback_throttled', 'type': 'atomic_t'}, {'name': 'nr_reclaim_start', 'type': 'ffi::c_ulong'}, {'name': 'kswapd', 'type': '*mut task_struct'}, {'name': 'kswapd_order', 'type': 'ffi::c_int'}, {'name': 'kswapd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kswapd_failures', 'type': 'atomic_t'}, {'name': 'kcompactd_max_order', 'type': 'ffi::c_int'}, {'name': 'kcompactd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kcompactd_wait', 'type': 'wait_queue_head_t'}, {'name': 'kcompactd', 'type': '*mut task_struct'}, {'name': 'proactive_compact_trigger', 'type': 'bool_'}, {'name': 'totalreserve_pages', 'type': 'ffi::c_ulong'}, {'name': 'min_unmapped_pages', 'type': 'ffi::c_ulong'}, {'name': 'min_slab_pages', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': '__lruvec', 'type': 'lruvec'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_padding_1', 'type': '[u64; 6usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'per_cpu_nodestats', 'type': '*mut per_cpu_nodestat'}, {'name': 'vm_stat', 'type': '[atomic_long_t; 48usize]'}, {'name': 'memtier', 'type': '*mut memory_tier'}]`

### Rust Evidence

- Graph edges: `1`

## W-000441 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: renamedata
- Explanation: renamedata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'old_mnt_idmap', 'type': '*mut mnt_idmap'}, {'name': 'old_parent', 'type': '*mut dentry'}, {'name': 'old_dentry', 'type': '*mut dentry'}, {'name': 'new_mnt_idmap', 'type': '*mut mnt_idmap'}, {'name': 'new_parent', 'type': '*mut dentry'}, {'name': 'new_dentry', 'type': '*mut dentry'}, {'name': 'delegated_inode', 'type': '*mut *mut inode'}, {'name': 'flags', 'type': 'ffi::c_uint'}]`
- New: `[{'name': 'mnt_idmap', 'type': '*mut mnt_idmap'}, {'name': 'old_parent', 'type': '*mut dentry'}, {'name': 'old_dentry', 'type': '*mut dentry'}, {'name': 'new_parent', 'type': '*mut dentry'}, {'name': 'new_dentry', 'type': '*mut dentry'}, {'name': 'delegated_inode', 'type': '*mut *mut inode'}, {'name': 'flags', 'type': 'ffi::c_uint'}]`

### Rust Evidence

- Graph edges: `1`

## W-000442 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: signal_struct
- Explanation: signal_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'sigcnt', 'type': 'refcount_t'}, {'name': 'live', 'type': 'atomic_t'}, {'name': 'nr_threads', 'type': 'ffi::c_int'}, {'name': 'quick_threads', 'type': 'ffi::c_int'}, {'name': 'thread_head', 'type': 'list_head'}, {'name': 'wait_chldexit', 'type': 'wait_queue_head_t'}, {'name': 'curr_target', 'type': '*mut task_struct'}, {'name': 'shared_pending', 'type': 'sigpending'}, {'name': 'multiprocess', 'type': 'hlist_head'}, {'name': 'group_exit_code', 'type': 'ffi::c_int'}, {'name': 'notify_count', 'type': 'ffi::c_int'}, {'name': 'group_exec_task', 'type': '*mut task_struct'}, {'name': 'group_stop_count', 'type': 'ffi::c_int'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'core_state', 'type': '*mut core_state'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'next_posix_timer_id', 'type': 'atomic_t'}, {'name': 'posix_timers', 'type': 'hlist_head'}, {'name': 'ignored_posix_timers', 'type': 'hlist_head'}, {'name': 'real_timer', 'type': 'hrtimer'}, {'name': 'it_real_incr', 'type': 'ktime_t'}, {'name': 'it', 'type': '[cpu_itimer; 2usize]'}, {'name': 'cputimer', 'type': 'thread_group_cputimer'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'pids', 'type': '[*mut pid; 4usize]'}, {'name': 'tty_old_pgrp', 'type': '*mut pid'}, {'name': 'leader', 'type': 'ffi::c_int'}, {'name': 'tty', 'type': '*mut tty_struct'}, {'name': 'stats_lock', 'type': 'seqlock_t'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'cutime', 'type': 'u64_'}, {'name': 'cstime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'cgtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'ffi::c_ulong'}, {'name': 'cnvcsw', 'type': 'ffi::c_ulong'}, {'name': 'cnivcsw', 'type': 'ffi::c_ulong'}, {'name': 'min_flt', 'type': 'ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'ffi::c_ulong'}, {'name': 'cmin_flt', 'type': 'ffi::c_ulong'}, {'name': 'cmaj_flt', 'type': 'ffi::c_ulong'}, {'name': 'inblock', 'type': 'ffi::c_ulong'}, {'name': 'oublock', 'type': 'ffi::c_ulong'}, {'name': 'cinblock', 'type': 'ffi::c_ulong'}, {'name': 'coublock', 'type': 'ffi::c_ulong'}, {'name': 'maxrss', 'type': 'ffi::c_ulong'}, {'name': 'cmaxrss', 'type': 'ffi::c_ulong'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'sum_sched_runtime', 'type': 'ffi::c_ulonglong'}, {'name': 'rlim', 'type': '[rlimit; 16usize]'}, {'name': 'pacct', 'type': 'pacct_struct'}, {'name': 'stats', 'type': '*mut taskstats'}, {'name': 'audit_tty', 'type': 'ffi::c_uint'}, {'name': 'tty_audit_buf', 'type': '*mut tty_audit_buf'}, {'name': 'oom_flag_origin', 'type': 'bool_'}, {'name': 'oom_score_adj', 'type': 'ffi::c_short'}, {'name': 'oom_score_adj_min', 'type': 'ffi::c_short'}, {'name': 'oom_mm', 'type': '*mut mm_struct'}, {'name': 'cred_guard_mutex', 'type': 'mutex'}, {'name': 'exec_update_lock', 'type': 'rw_semaphore'}]`
- New: `[{'name': 'sigcnt', 'type': 'refcount_t'}, {'name': 'live', 'type': 'atomic_t'}, {'name': 'nr_threads', 'type': 'ffi::c_int'}, {'name': 'quick_threads', 'type': 'ffi::c_int'}, {'name': 'thread_head', 'type': 'list_head'}, {'name': 'wait_chldexit', 'type': 'wait_queue_head_t'}, {'name': 'curr_target', 'type': '*mut task_struct'}, {'name': 'shared_pending', 'type': 'sigpending'}, {'name': 'multiprocess', 'type': 'hlist_head'}, {'name': 'group_exit_code', 'type': 'ffi::c_int'}, {'name': 'notify_count', 'type': 'ffi::c_int'}, {'name': 'group_exec_task', 'type': '*mut task_struct'}, {'name': 'group_stop_count', 'type': 'ffi::c_int'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'core_state', 'type': '*mut core_state'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'next_posix_timer_id', 'type': 'atomic_t'}, {'name': 'posix_timers', 'type': 'hlist_head'}, {'name': 'ignored_posix_timers', 'type': 'hlist_head'}, {'name': 'real_timer', 'type': 'hrtimer'}, {'name': 'it_real_incr', 'type': 'ktime_t'}, {'name': 'it', 'type': '[cpu_itimer; 2usize]'}, {'name': 'cputimer', 'type': 'thread_group_cputimer'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'pids', 'type': '[*mut pid; 4usize]'}, {'name': 'tty_old_pgrp', 'type': '*mut pid'}, {'name': 'leader', 'type': 'ffi::c_int'}, {'name': 'tty', 'type': '*mut tty_struct'}, {'name': 'stats_lock', 'type': 'seqlock_t'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'cutime', 'type': 'u64_'}, {'name': 'cstime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'cgtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'ffi::c_ulong'}, {'name': 'cnvcsw', 'type': 'ffi::c_ulong'}, {'name': 'cnivcsw', 'type': 'ffi::c_ulong'}, {'name': 'min_flt', 'type': 'ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'ffi::c_ulong'}, {'name': 'cmin_flt', 'type': 'ffi::c_ulong'}, {'name': 'cmaj_flt', 'type': 'ffi::c_ulong'}, {'name': 'inblock', 'type': 'ffi::c_ulong'}, {'name': 'oublock', 'type': 'ffi::c_ulong'}, {'name': 'cinblock', 'type': 'ffi::c_ulong'}, {'name': 'coublock', 'type': 'ffi::c_ulong'}, {'name': 'maxrss', 'type': 'ffi::c_ulong'}, {'name': 'cmaxrss', 'type': 'ffi::c_ulong'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'sum_sched_runtime', 'type': 'ffi::c_ulonglong'}, {'name': 'rlim', 'type': '[rlimit; 16usize]'}, {'name': 'pacct', 'type': 'pacct_struct'}, {'name': 'stats', 'type': '*mut taskstats'}, {'name': 'audit_tty', 'type': 'ffi::c_uint'}, {'name': 'tty_audit_buf', 'type': '*mut tty_audit_buf'}, {'name': 'cgroup_threadgroup_rwsem', 'type': 'rw_semaphore'}, {'name': 'oom_flag_origin', 'type': 'bool_'}, {'name': 'oom_score_adj', 'type': 'ffi::c_short'}, {'name': 'oom_score_adj_min', 'type': 'ffi::c_short'}, {'name': 'oom_mm', 'type': '*mut mm_struct'}, {'name': 'cred_guard_mutex', 'type': 'mutex'}, {'name': 'exec_update_lock', 'type': 'rw_semaphore'}]`

### Rust Evidence

- Graph edges: `1`

## W-000443 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: super_block
- Explanation: super_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 's_list', 'type': 'list_head'}, {'name': 's_dev', 'type': 'dev_t'}, {'name': 's_blocksize_bits', 'type': 'ffi::c_uchar'}, {'name': 's_blocksize', 'type': 'ffi::c_ulong'}, {'name': 's_maxbytes', 'type': 'loff_t'}, {'name': 's_type', 'type': '*mut file_system_type'}, {'name': 's_op', 'type': '*const super_operations'}, {'name': 'dq_op', 'type': '*const dquot_operations'}, {'name': 's_qcop', 'type': '*const quotactl_ops'}, {'name': 's_export_op', 'type': '*const export_operations'}, {'name': 's_flags', 'type': 'ffi::c_ulong'}, {'name': 's_iflags', 'type': 'ffi::c_ulong'}, {'name': 's_magic', 'type': 'ffi::c_ulong'}, {'name': 's_root', 'type': '*mut dentry'}, {'name': 's_umount', 'type': 'rw_semaphore'}, {'name': 's_count', 'type': 'ffi::c_int'}, {'name': 's_active', 'type': 'atomic_t'}, {'name': 's_security', 'type': '*mut ffi::c_void'}, {'name': 's_xattr', 'type': '*const *mut xattr_handler'}, {'name': 's_roots', 'type': 'hlist_bl_head'}, {'name': 's_mounts', 'type': 'list_head'}, {'name': 's_bdev', 'type': '*mut block_device'}, {'name': 's_bdev_file', 'type': '*mut file'}, {'name': 's_bdi', 'type': '*mut backing_dev_info'}, {'name': 's_mtd', 'type': '*mut mtd_info'}, {'name': 's_instances', 'type': 'hlist_node'}, {'name': 's_quota_types', 'type': 'ffi::c_uint'}, {'name': 's_dquot', 'type': 'quota_info'}, {'name': 's_writers', 'type': 'sb_writers'}, {'name': 's_fs_info', 'type': '*mut ffi::c_void'}, {'name': 's_time_gran', 'type': 'u32_'}, {'name': 's_time_min', 'type': 'time64_t'}, {'name': 's_time_max', 'type': 'time64_t'}, {'name': 's_fsnotify_mask', 'type': 'u32_'}, {'name': 's_fsnotify_info', 'type': '*mut fsnotify_sb_info'}, {'name': 's_id', 'type': '[ffi::c_char; 32usize]'}, {'name': 's_uuid', 'type': 'uuid_t'}, {'name': 's_uuid_len', 'type': 'u8_'}, {'name': 's_sysfs_name', 'type': '[ffi::c_char; 37usize]'}, {'name': 's_max_links', 'type': 'ffi::c_uint'}, {'name': 's_d_flags', 'type': 'ffi::c_uint'}, {'name': 's_vfs_rename_mutex', 'type': 'mutex'}, {'name': 's_subtype', 'type': '*const ffi::c_char'}, {'name': '__s_d_op', 'type': '*const dentry_operations'}, {'name': 's_shrink', 'type': '*mut shrinker'}, {'name': 's_remove_count', 'type': 'atomic_long_t'}, {'name': 's_readonly_remount', 'type': 'ffi::c_int'}, {'name': 's_wb_err', 'type': 'errseq_t'}, {'name': 's_dio_done_wq', 'type': '*mut workqueue_struct'}, {'name': 's_pins', 'type': 'hlist_head'}, {'name': 's_user_ns', 'type': '*mut user_namespace'}, {'name': 's_dentry_lru', 'type': 'list_lru'}, {'name': 's_inode_lru', 'type': 'list_lru'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 's_sync_lock', 'type': 'mutex'}, {'name': 's_stack_depth', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': '[u32; 15usize]'}, {'name': 's_inode_list_lock', 'type': 'spinlock_t'}, {'name': 's_inodes', 'type': 'list_head'}, {'name': 's_inode_wblist_lock', 'type': 'spinlock_t'}, {'name': 's_inodes_wb', 'type': 'list_head'}]`
- New: `[{'name': 's_list', 'type': 'list_head'}, {'name': 's_dev', 'type': 'dev_t'}, {'name': 's_blocksize_bits', 'type': 'ffi::c_uchar'}, {'name': 's_blocksize', 'type': 'ffi::c_ulong'}, {'name': 's_maxbytes', 'type': 'loff_t'}, {'name': 's_type', 'type': '*mut file_system_type'}, {'name': 's_op', 'type': '*const super_operations'}, {'name': 'dq_op', 'type': '*const dquot_operations'}, {'name': 's_qcop', 'type': '*const quotactl_ops'}, {'name': 's_export_op', 'type': '*const export_operations'}, {'name': 's_flags', 'type': 'ffi::c_ulong'}, {'name': 's_iflags', 'type': 'ffi::c_ulong'}, {'name': 's_magic', 'type': 'ffi::c_ulong'}, {'name': 's_root', 'type': '*mut dentry'}, {'name': 's_umount', 'type': 'rw_semaphore'}, {'name': 's_count', 'type': 'ffi::c_int'}, {'name': 's_active', 'type': 'atomic_t'}, {'name': 's_security', 'type': '*mut ffi::c_void'}, {'name': 's_xattr', 'type': '*const *mut xattr_handler'}, {'name': 's_roots', 'type': 'hlist_bl_head'}, {'name': 's_mounts', 'type': '*mut mount'}, {'name': 's_bdev', 'type': '*mut block_device'}, {'name': 's_bdev_file', 'type': '*mut file'}, {'name': 's_bdi', 'type': '*mut backing_dev_info'}, {'name': 's_mtd', 'type': '*mut mtd_info'}, {'name': 's_instances', 'type': 'hlist_node'}, {'name': 's_quota_types', 'type': 'ffi::c_uint'}, {'name': 's_dquot', 'type': 'quota_info'}, {'name': 's_writers', 'type': 'sb_writers'}, {'name': 's_fs_info', 'type': '*mut ffi::c_void'}, {'name': 's_time_gran', 'type': 'u32_'}, {'name': 's_time_min', 'type': 'time64_t'}, {'name': 's_time_max', 'type': 'time64_t'}, {'name': 's_fsnotify_mask', 'type': 'u32_'}, {'name': 's_fsnotify_info', 'type': '*mut fsnotify_sb_info'}, {'name': 's_id', 'type': '[ffi::c_char; 32usize]'}, {'name': 's_uuid', 'type': 'uuid_t'}, {'name': 's_uuid_len', 'type': 'u8_'}, {'name': 's_sysfs_name', 'type': '[ffi::c_char; 37usize]'}, {'name': 's_max_links', 'type': 'ffi::c_uint'}, {'name': 's_d_flags', 'type': 'ffi::c_uint'}, {'name': 's_vfs_rename_mutex', 'type': 'mutex'}, {'name': 's_subtype', 'type': '*const ffi::c_char'}, {'name': '__s_d_op', 'type': '*const dentry_operations'}, {'name': 's_shrink', 'type': '*mut shrinker'}, {'name': 's_remove_count', 'type': 'atomic_long_t'}, {'name': 's_readonly_remount', 'type': 'ffi::c_int'}, {'name': 's_wb_err', 'type': 'errseq_t'}, {'name': 's_dio_done_wq', 'type': '*mut workqueue_struct'}, {'name': 's_pins', 'type': 'hlist_head'}, {'name': 's_user_ns', 'type': '*mut user_namespace'}, {'name': 's_dentry_lru', 'type': 'list_lru'}, {'name': 's_inode_lru', 'type': 'list_lru'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 's_sync_lock', 'type': 'mutex'}, {'name': 's_stack_depth', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': 'u32'}, {'name': 's_inode_list_lock', 'type': 'spinlock_t'}, {'name': 's_inodes', 'type': 'list_head'}, {'name': 's_inode_wblist_lock', 'type': 'spinlock_t'}, {'name': 's_inodes_wb', 'type': 'list_head'}]`

### Rust Evidence

- Graph edges: `1`

## W-000444 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: swap_cluster_info
- Explanation: swap_cluster_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'lock', 'type': 'spinlock_t'}, {'name': 'count', 'type': 'u16_'}, {'name': 'flags', 'type': 'u8_'}, {'name': 'order', 'type': 'u8_'}, {'name': 'list', 'type': 'list_head'}]`
- New: `[{'name': '_address', 'type': 'u8'}]`

### Rust Evidence

- Graph edges: `1`

## W-000445 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: swap_info_struct
- Explanation: swap_info_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'users', 'type': 'percpu_ref'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'prio', 'type': 'ffi::c_short'}, {'name': 'list', 'type': 'plist_node'}, {'name': 'type_', 'type': 'ffi::c_schar'}, {'name': 'max', 'type': 'ffi::c_uint'}, {'name': 'swap_map', 'type': '*mut ffi::c_uchar'}, {'name': 'zeromap', 'type': '*mut ffi::c_ulong'}, {'name': 'cluster_info', 'type': '*mut swap_cluster_info'}, {'name': 'free_clusters', 'type': 'list_head'}, {'name': 'full_clusters', 'type': 'list_head'}, {'name': 'nonfull_clusters', 'type': '[list_head; 1usize]'}, {'name': 'frag_clusters', 'type': '[list_head; 1usize]'}, {'name': 'frag_cluster_nr', 'type': '[atomic_long_t; 1usize]'}, {'name': 'pages', 'type': 'ffi::c_uint'}, {'name': 'inuse_pages', 'type': 'atomic_long_t'}, {'name': 'global_cluster', 'type': '*mut swap_sequential_cluster'}, {'name': 'global_cluster_lock', 'type': 'spinlock_t'}, {'name': 'swap_extent_root', 'type': 'rb_root'}, {'name': 'bdev', 'type': '*mut block_device'}, {'name': 'swap_file', 'type': '*mut file'}, {'name': 'comp', 'type': 'completion'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'cont_lock', 'type': 'spinlock_t'}, {'name': 'discard_work', 'type': 'work_struct'}, {'name': 'reclaim_work', 'type': 'work_struct'}, {'name': 'discard_clusters', 'type': 'list_head'}, {'name': 'avail_lists', 'type': '__IncompleteArrayField<plist_node>'}]`
- New: `[{'name': 'users', 'type': 'percpu_ref'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'prio', 'type': 'ffi::c_short'}, {'name': 'list', 'type': 'plist_node'}, {'name': 'type_', 'type': 'ffi::c_schar'}, {'name': 'max', 'type': 'ffi::c_uint'}, {'name': 'swap_map', 'type': '*mut ffi::c_uchar'}, {'name': 'zeromap', 'type': '*mut ffi::c_ulong'}, {'name': 'cluster_info', 'type': '*mut swap_cluster_info'}, {'name': 'free_clusters', 'type': 'list_head'}, {'name': 'full_clusters', 'type': 'list_head'}, {'name': 'nonfull_clusters', 'type': '[list_head; 1usize]'}, {'name': 'frag_clusters', 'type': '[list_head; 1usize]'}, {'name': 'pages', 'type': 'ffi::c_uint'}, {'name': 'inuse_pages', 'type': 'atomic_long_t'}, {'name': 'global_cluster', 'type': '*mut swap_sequential_cluster'}, {'name': 'global_cluster_lock', 'type': 'spinlock_t'}, {'name': 'swap_extent_root', 'type': 'rb_root'}, {'name': 'bdev', 'type': '*mut block_device'}, {'name': 'swap_file', 'type': '*mut file'}, {'name': 'comp', 'type': 'completion'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'cont_lock', 'type': 'spinlock_t'}, {'name': 'discard_work', 'type': 'work_struct'}, {'name': 'reclaim_work', 'type': 'work_struct'}, {'name': 'discard_clusters', 'type': 'list_head'}, {'name': 'avail_lists', 'type': '__IncompleteArrayField<plist_node>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000446 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: time_namespace
- Explanation: time_namespace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[]`

### Rust Evidence

- Graph edges: `1`

## W-000447 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: uprobes_state
- Explanation: uprobes_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'xol_area', 'type': '*mut xol_area'}]`
- New: `[{'name': 'xol_area', 'type': '*mut xol_area'}, {'name': 'head_tramps', 'type': 'hlist_head'}]`

### Rust Evidence

- Graph edges: `1`

## W-000448 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vm_area_desc
- Explanation: vm_area_desc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'start', 'type': 'ffi::c_ulong'}, {'name': 'end', 'type': 'ffi::c_ulong'}, {'name': 'pgoff', 'type': 'ffi::c_ulong'}, {'name': 'file', 'type': '*mut file'}, {'name': 'vm_flags', 'type': 'vm_flags_t'}, {'name': 'page_prot', 'type': 'pgprot_t'}, {'name': 'vm_ops', 'type': '*const vm_operations_struct'}, {'name': 'private_data', 'type': '*mut ffi::c_void'}]`
- New: `[{'name': 'mm', 'type': '*const mm_struct'}, {'name': 'file', 'type': '*mut file'}, {'name': 'start', 'type': 'ffi::c_ulong'}, {'name': 'end', 'type': 'ffi::c_ulong'}, {'name': 'pgoff', 'type': 'ffi::c_ulong'}, {'name': 'vm_file', 'type': '*mut file'}, {'name': 'vm_flags', 'type': 'vm_flags_t'}, {'name': 'page_prot', 'type': 'pgprot_t'}, {'name': 'vm_ops', 'type': '*const vm_operations_struct'}, {'name': 'private_data', 'type': '*mut ffi::c_void'}]`

### Rust Evidence

- Graph edges: `1`

## W-000449 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vm_operations_struct
- Explanation: vm_operations_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'open', 'type': '::core::option::Option<unsafe extern "C" fn(area: *mut vm_area_struct)>'}, {'name': 'close', 'type': '::core::option::Option<unsafe extern "C" fn(area: *mut vm_area_struct)>'}, {'name': 'may_split', 'type': '::core::option::Option<'}, {'name': 'mprotect', 'type': '::core::option::Option<'}, {'name': 'fault', 'type': '::core::option::Option<unsafe extern "C" fn(vmf: *mut vm_fault) -> vm_fault_t>'}, {'name': 'huge_fault', 'type': '::core::option::Option<'}, {'name': 'map_pages', 'type': '::core::option::Option<'}, {'name': 'pfn_mkwrite', 'type': '::core::option::Option<unsafe extern "C" fn(vmf: *mut vm_fault) -> vm_fault_t>'}, {'name': 'access', 'type': '::core::option::Option<'}, {'name': 'name', 'type': '::core::option::Option<'}, {'name': 'set_policy', 'type': '::core::option::Option<'}, {'name': 'get_policy', 'type': '::core::option::Option<'}, {'name': 'find_special_page', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'open', 'type': '::core::option::Option<unsafe extern "C" fn(area: *mut vm_area_struct)>'}, {'name': 'close', 'type': '::core::option::Option<unsafe extern "C" fn(area: *mut vm_area_struct)>'}, {'name': 'may_split', 'type': '::core::option::Option<'}, {'name': 'mprotect', 'type': '::core::option::Option<'}, {'name': 'fault', 'type': '::core::option::Option<unsafe extern "C" fn(vmf: *mut vm_fault) -> vm_fault_t>'}, {'name': 'huge_fault', 'type': '::core::option::Option<'}, {'name': 'map_pages', 'type': '::core::option::Option<'}, {'name': 'pfn_mkwrite', 'type': '::core::option::Option<unsafe extern "C" fn(vmf: *mut vm_fault) -> vm_fault_t>'}, {'name': 'access', 'type': '::core::option::Option<'}, {'name': 'name', 'type': '::core::option::Option<'}, {'name': 'set_policy', 'type': '::core::option::Option<'}, {'name': 'get_policy', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-000658 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: krealloc
- Explanation: krealloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `alloc_hooks(krealloc_noprof(__VA_ARGS__))`
- New: `krealloc_node(__VA_ARGS__, NUMA_NO_NODE)`

### Rust Evidence

- Graph edges: `3`

## W-000661 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: kvrealloc
- Explanation: kvrealloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `alloc_hooks(kvrealloc_noprof(__VA_ARGS__))`
- New: `kvrealloc_node(__VA_ARGS__, NUMA_NO_NODE)`

### Rust Evidence

- Graph edges: `3`

## W-000455 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: SKB_GSO_TCP_FIXEDID
- Explanation: SKB_GSO_TCP_FIXEDID changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `1073741824`

### Rust Evidence

- Graph edges: `2`

## W-000460 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: TIF_NEED_RESCHED
- Explanation: TIF_NEED_RESCHED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `3`
- New: `4`

### Rust Evidence

- Graph edges: `2`

## W-000494 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: req_op_REQ_OP_ZONE_RESET
- Explanation: req_op_REQ_OP_ZONE_RESET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `15`
- New: `17`

### Rust Evidence

- Graph edges: `2`

## W-000450 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ACPI_CA_VERSION
- Explanation: ACPI_CA_VERSION changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `539296772`
- New: `539297799`

### Rust Evidence

- Graph edges: `1`

## W-000451 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: AE_CODE_AML_MAX
- Explanation: AE_CODE_AML_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `37`
- New: `39`

### Rust Evidence

- Graph edges: `1`

## W-000452 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ETHTOOL_A_FEC_STAT_MAX
- Explanation: ETHTOOL_A_FEC_STAT_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `4`
- New: `5`

### Rust Evidence

- Graph edges: `1`

## W-000453 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: MSR_AMD64_SNP_RESV_BIT
- Explanation: MSR_AMD64_SNP_RESV_BIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `18`
- New: `19`

### Rust Evidence

- Graph edges: `1`

## W-000454 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: QUEUE_FLAG_MAX
- Explanation: QUEUE_FLAG_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `17`

### Rust Evidence

- Graph edges: `1`

## W-000456 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TIF_ADDR32
- Explanation: TIF_ADDR32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `29`
- New: `28`

### Rust Evidence

- Graph edges: `1`

## W-000457 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TIF_BLOCKSTEP
- Explanation: TIF_BLOCKSTEP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `25`
- New: `26`

### Rust Evidence

- Graph edges: `1`

## W-000458 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TIF_MEMDIE
- Explanation: TIF_MEMDIE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `20`
- New: `3`

### Rust Evidence

- Graph edges: `1`

## W-000459 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TIF_NEED_FPU_LOAD
- Explanation: TIF_NEED_FPU_LOAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `14`
- New: `19`

### Rust Evidence

- Graph edges: `1`

## W-000461 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TIF_NEED_RESCHED_LAZY
- Explanation: TIF_NEED_RESCHED_LAZY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `4`
- New: `5`

### Rust Evidence

- Graph edges: `1`

## W-000462 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TIF_NOCPUID
- Explanation: TIF_NOCPUID changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `15`
- New: `20`

### Rust Evidence

- Graph edges: `1`

## W-000463 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TIF_NOTIFY_RESUME
- Explanation: TIF_NOTIFY_RESUME changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `1`
- New: `0`

### Rust Evidence

- Graph edges: `1`

## W-000464 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TIF_NOTIFY_SIGNAL
- Explanation: TIF_NOTIFY_SIGNAL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `17`
- New: `2`

### Rust Evidence

- Graph edges: `1`

## W-000465 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TIF_NOTSC
- Explanation: TIF_NOTSC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `21`

### Rust Evidence

- Graph edges: `1`

## W-000466 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TIF_PATCH_PENDING
- Explanation: TIF_PATCH_PENDING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `13`
- New: `9`

### Rust Evidence

- Graph edges: `1`

## W-000467 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TIF_POLLING_NRFLAG
- Explanation: TIF_POLLING_NRFLAG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `21`
- New: `6`

### Rust Evidence

- Graph edges: `1`

## W-000468 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TIF_SIGPENDING
- Explanation: TIF_SIGPENDING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `2`
- New: `1`

### Rust Evidence

- Graph edges: `1`

## W-000469 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TIF_SINGLESTEP
- Explanation: TIF_SINGLESTEP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `25`

### Rust Evidence

- Graph edges: `1`

## W-000470 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TIF_SPEC_IB
- Explanation: TIF_SPEC_IB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `9`
- New: `17`

### Rust Evidence

- Graph edges: `1`

## W-000471 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TIF_SPEC_L1D_FLUSH
- Explanation: TIF_SPEC_L1D_FLUSH changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `18`

### Rust Evidence

- Graph edges: `1`

## W-000472 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TIF_SSBD
- Explanation: TIF_SSBD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `6`
- New: `16`

### Rust Evidence

- Graph edges: `1`

## W-000473 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TIF_UPROBE
- Explanation: TIF_UPROBE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `12`
- New: `8`

### Rust Evidence

- Graph edges: `1`

## W-000474 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: TIF_USER_RETURN_NOTIFY
- Explanation: TIF_USER_RETURN_NOTIFY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `11`
- New: `7`

### Rust Evidence

- Graph edges: `1`

## W-000475 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __ETHTOOL_A_FEC_STAT_CNT
- Explanation: __ETHTOOL_A_FEC_STAT_CNT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `6`

### Rust Evidence

- Graph edges: `1`

## W-000476 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_arg_type___BPF_ARG_TYPE_LIMIT
- Explanation: bpf_arg_type___BPF_ARG_TYPE_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `134217727`
- New: `268435455`

### Rust Evidence

- Graph edges: `1`

## W-000477 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_reg_type___BPF_REG_TYPE_LIMIT
- Explanation: bpf_reg_type___BPF_REG_TYPE_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `134217727`
- New: `268435455`

### Rust Evidence

- Graph edges: `1`

## W-000478 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_return_type___BPF_RET_TYPE_LIMIT
- Explanation: bpf_return_type___BPF_RET_TYPE_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `134217727`
- New: `268435455`

### Rust Evidence

- Graph edges: `1`

## W-000479 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_type_flag___BPF_TYPE_FLAG_MAX
- Explanation: bpf_type_flag___BPF_TYPE_FLAG_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `67108865`
- New: `134217729`

### Rust Evidence

- Graph edges: `1`

## W-000480 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_type_flag___BPF_TYPE_LAST_FLAG
- Explanation: bpf_type_flag___BPF_TYPE_LAST_FLAG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `67108864`
- New: `134217728`

### Rust Evidence

- Graph edges: `1`

## W-000481 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_KMEM
- Explanation: memcg_stat_item_MEMCG_KMEM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `51`
- New: `52`

### Rust Evidence

- Graph edges: `1`

## W-000482 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_NR_STAT
- Explanation: memcg_stat_item_MEMCG_NR_STAT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `54`
- New: `55`

### Rust Evidence

- Graph edges: `1`

## W-000483 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_PERCPU_B
- Explanation: memcg_stat_item_MEMCG_PERCPU_B changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `49`
- New: `50`

### Rust Evidence

- Graph edges: `1`

## W-000484 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_SOCK
- Explanation: memcg_stat_item_MEMCG_SOCK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `49`

### Rust Evidence

- Graph edges: `1`

## W-000485 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_SWAP
- Explanation: memcg_stat_item_MEMCG_SWAP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `47`
- New: `48`

### Rust Evidence

- Graph edges: `1`

## W-000486 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_VMALLOC
- Explanation: memcg_stat_item_MEMCG_VMALLOC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `50`
- New: `51`

### Rust Evidence

- Graph edges: `1`

## W-000487 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_ZSWAPPED
- Explanation: memcg_stat_item_MEMCG_ZSWAPPED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `53`
- New: `54`

### Rust Evidence

- Graph edges: `1`

## W-000488 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_ZSWAP_B
- Explanation: memcg_stat_item_MEMCG_ZSWAP_B changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `52`
- New: `53`

### Rust Evidence

- Graph edges: `1`

## W-000489 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: mount_flags_MNT_INTERNAL_FLAGS
- Explanation: mount_flags_MNT_INTERNAL_FLAGS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `58737152`
- New: `58736640`

### Rust Evidence

- Graph edges: `1`

## W-000490 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_VM_NODE_STAT_ITEMS
- Explanation: node_stat_item_NR_VM_NODE_STAT_ITEMS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `47`
- New: `48`

### Rust Evidence

- Graph edges: `1`

## W-000491 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: req_op_REQ_OP_ZONE_CLOSE
- Explanation: req_op_REQ_OP_ZONE_CLOSE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `11`
- New: `13`

### Rust Evidence

- Graph edges: `1`

## W-000492 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: req_op_REQ_OP_ZONE_FINISH
- Explanation: req_op_REQ_OP_ZONE_FINISH changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `13`
- New: `15`

### Rust Evidence

- Graph edges: `1`

## W-000493 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: req_op_REQ_OP_ZONE_OPEN
- Explanation: req_op_REQ_OP_ZONE_OPEN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `11`

### Rust Evidence

- Graph edges: `1`

## W-000495 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: req_op_REQ_OP_ZONE_RESET_ALL
- Explanation: req_op_REQ_OP_ZONE_RESET_ALL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `17`
- New: `19`

### Rust Evidence

- Graph edges: `1`

## W-000496 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_MAX
- Explanation: skb_drop_reason_SKB_DROP_REASON_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `125`
- New: `127`

### Rust Evidence

- Graph edges: `1`

## W-000497 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ssb_mitigation_SPEC_STORE_BYPASS_DISABLE
- Explanation: ssb_mitigation_SPEC_STORE_BYPASS_DISABLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `1`
- New: `2`

### Rust Evidence

- Graph edges: `1`

## W-000498 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ssb_mitigation_SPEC_STORE_BYPASS_PRCTL
- Explanation: ssb_mitigation_SPEC_STORE_BYPASS_PRCTL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `2`
- New: `3`

### Rust Evidence

- Graph edges: `1`

## W-000499 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ssb_mitigation_SPEC_STORE_BYPASS_SECCOMP
- Explanation: ssb_mitigation_SPEC_STORE_BYPASS_SECCOMP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `3`
- New: `4`

### Rust Evidence

- Graph edges: `1`

## W-000500 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: wq_flags___WQ_BH_ALLOWS
- Explanation: wq_flags___WQ_BH_ALLOWS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `17`
- New: `273`

### Rust Evidence

- Graph edges: `1`

## W-000501 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: ACPI_CA_VERSION
- Explanation: ACPI_CA_VERSION changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x20250404`
- New: `0x20250807`

### Rust Evidence

- Graph edges: `1`

## W-000502 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: AE_CODE_AML_MAX
- Explanation: AE_CODE_AML_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x0025`
- New: `0x0027`

### Rust Evidence

- Graph edges: `1`

## W-000503 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AHB_ARB0
- Explanation: CLKID_AHB_ARB0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `49`
- New: `43`

### Rust Evidence

- Graph edges: `0`

## W-000504 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AHB_CTRL_BUS
- Explanation: CLKID_AHB_CTRL_BUS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `51`
- New: `47`

### Rust Evidence

- Graph edges: `0`

## W-000505 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AHB_DATA_BUS
- Explanation: CLKID_AHB_DATA_BUS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `50`
- New: `46`

### Rust Evidence

- Graph edges: `0`

## W-000506 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_32K
- Explanation: CLKID_AO_32K changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `23`
- New: `15`

### Rust Evidence

- Graph edges: `0`

## W-000507 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_32K_DIV
- Explanation: CLKID_AO_32K_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `21`
- New: `13`

### Rust Evidence

- Graph edges: `0`

## W-000508 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_32K_PRE
- Explanation: CLKID_AO_32K_PRE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `20`
- New: `12`

### Rust Evidence

- Graph edges: `0`

## W-000509 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_32K_SEL
- Explanation: CLKID_AO_32K_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `22`
- New: `14`

### Rust Evidence

- Graph edges: `0`

## W-000510 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_AHB_SRAM
- Explanation: CLKID_AO_AHB_SRAM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `11`
- New: `55`

### Rust Evidence

- Graph edges: `0`

## W-000511 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_CLK81
- Explanation: CLKID_AO_CLK81 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `15`
- New: `7`

### Rust Evidence

- Graph edges: `0`

## W-000512 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_CTS_OSCIN
- Explanation: CLKID_AO_CTS_OSCIN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `19`
- New: `11`

### Rust Evidence

- Graph edges: `0`

## W-000513 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_CTS_RTC_OSCIN
- Explanation: CLKID_AO_CTS_RTC_OSCIN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `28`
- New: `16`

### Rust Evidence

- Graph edges: `0`

## W-000514 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_SAR_ADC
- Explanation: CLKID_AO_SAR_ADC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `6`

### Rust Evidence

- Graph edges: `0`

## W-000515 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_SAR_ADC_CLK
- Explanation: CLKID_AO_SAR_ADC_CLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `18`
- New: `10`

### Rust Evidence

- Graph edges: `0`

## W-000516 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_SAR_ADC_DIV
- Explanation: CLKID_AO_SAR_ADC_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `17`
- New: `9`

### Rust Evidence

- Graph edges: `0`

## W-000517 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_SAR_ADC_SEL
- Explanation: CLKID_AO_SAR_ADC_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `8`

### Rust Evidence

- Graph edges: `0`

## W-000518 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_UART2
- Explanation: CLKID_AO_UART2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `6`
- New: `4`

### Rust Evidence

- Graph edges: `0`

## W-000519 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_ASSIST_MISC
- Explanation: CLKID_ASSIST_MISC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `32`
- New: `30`

### Rust Evidence

- Graph edges: `0`

## W-000520 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AUDIO
- Explanation: CLKID_AUDIO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `37`
- New: `35`

### Rust Evidence

- Graph edges: `0`

## W-000521 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AUDIO_LOCKER
- Explanation: CLKID_AUDIO_LOCKER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `17`
- New: `16`

### Rust Evidence

- Graph edges: `0`

## W-000522 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CPU_CLK
- Explanation: CLKID_CPU_CLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `187`
- New: `11`

### Rust Evidence

- Graph edges: `0`

## W-000523 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CPU_CLK_DIV16
- Explanation: CLKID_CPU_CLK_DIV16 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `189`
- New: `15`

### Rust Evidence

- Graph edges: `0`

## W-000524 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CTS_ENCI
- Explanation: CLKID_CTS_ENCI changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `162`
- New: `61`

### Rust Evidence

- Graph edges: `0`

## W-000525 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CTS_ENCI_SEL
- Explanation: CLKID_CTS_ENCI_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `158`
- New: `57`

### Rust Evidence

- Graph edges: `0`

## W-000526 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CTS_ENCL
- Explanation: CLKID_CTS_ENCL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `271`
- New: `133`

### Rust Evidence

- Graph edges: `0`

## W-000527 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CTS_ENCL_SEL
- Explanation: CLKID_CTS_ENCL_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `272`
- New: `132`

### Rust Evidence

- Graph edges: `0`

## W-000528 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CTS_ENCP
- Explanation: CLKID_CTS_ENCP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `163`
- New: `62`

### Rust Evidence

- Graph edges: `0`

## W-000529 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CTS_ENCP_SEL
- Explanation: CLKID_CTS_ENCP_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `159`
- New: `58`

### Rust Evidence

- Graph edges: `0`

## W-000530 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CTS_VDAC
- Explanation: CLKID_CTS_VDAC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `164`
- New: `63`

### Rust Evidence

- Graph edges: `0`

## W-000531 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CTS_VDAC_SEL
- Explanation: CLKID_CTS_VDAC_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `160`
- New: `59`

### Rust Evidence

- Graph edges: `0`

## W-000532 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_DMA
- Explanation: CLKID_DMA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `105`
- New: `33`

### Rust Evidence

- Graph edges: `0`

## W-000533 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_DOS
- Explanation: CLKID_DOS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `170`

### Rust Evidence

- Graph edges: `0`

## W-000534 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_EFUSE
- Explanation: CLKID_EFUSE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `106`
- New: `44`

### Rust Evidence

- Graph edges: `0`

## W-000535 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_ETH
- Explanation: CLKID_ETH changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `38`
- New: `36`

### Rust Evidence

- Graph edges: `0`

## W-000536 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_FCLK_DIV2P5
- Explanation: CLKID_FCLK_DIV2P5 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `99`
- New: `13`

### Rust Evidence

- Graph edges: `0`

## W-000537 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_FCLK_DIV2P5_DIV
- Explanation: CLKID_FCLK_DIV2P5_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `100`
- New: `12`

### Rust Evidence

- Graph edges: `0`

## W-000538 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_FCLK_DIV2_DIV
- Explanation: CLKID_FCLK_DIV2_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `75`
- New: `71`

### Rust Evidence

- Graph edges: `0`

## W-000539 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_FCLK_DIV3_DIV
- Explanation: CLKID_FCLK_DIV3_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `76`
- New: `72`

### Rust Evidence

- Graph edges: `0`

## W-000540 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_FCLK_DIV4_DIV
- Explanation: CLKID_FCLK_DIV4_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `77`
- New: `73`

### Rust Evidence

- Graph edges: `0`

## W-000541 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_FCLK_DIV5_DIV
- Explanation: CLKID_FCLK_DIV5_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `78`
- New: `74`

### Rust Evidence

- Graph edges: `0`

## W-000542 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_FCLK_DIV7_DIV
- Explanation: CLKID_FCLK_DIV7_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `79`
- New: `75`

### Rust Evidence

- Graph edges: `0`

## W-000543 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_FIXED_PLL_DCO
- Explanation: CLKID_FIXED_PLL_DCO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `101`
- New: `86`

### Rust Evidence

- Graph edges: `0`

## W-000544 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_G2D
- Explanation: CLKID_G2D changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `43`
- New: `38`

### Rust Evidence

- Graph edges: `0`

## W-000545 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_GIC
- Explanation: CLKID_GIC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `59`
- New: `53`

### Rust Evidence

- Graph edges: `0`

## W-000546 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_GP0_PLL_DCO
- Explanation: CLKID_GP0_PLL_DCO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `103`
- New: `87`

### Rust Evidence

- Graph edges: `0`

## W-000547 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HDMI
- Explanation: CLKID_HDMI changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `168`
- New: `67`

### Rust Evidence

- Graph edges: `0`

## W-000548 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HDMI_DIV
- Explanation: CLKID_HDMI_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `167`
- New: `66`

### Rust Evidence

- Graph edges: `0`

## W-000549 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HDMI_PLL
- Explanation: CLKID_HDMI_PLL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `128`
- New: `20`

### Rust Evidence

- Graph edges: `0`

## W-000550 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HDMI_PLL_DCO
- Explanation: CLKID_HDMI_PLL_DCO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `125`
- New: `18`

### Rust Evidence

- Graph edges: `0`

## W-000551 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HDMI_PLL_OD
- Explanation: CLKID_HDMI_PLL_OD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `126`
- New: `19`

### Rust Evidence

- Graph edges: `0`

## W-000552 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HDMI_SEL
- Explanation: CLKID_HDMI_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `166`
- New: `65`

### Rust Evidence

- Graph edges: `0`

## W-000553 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HDMI_TX
- Explanation: CLKID_HDMI_TX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `165`
- New: `64`

### Rust Evidence

- Graph edges: `0`

## W-000554 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HDMI_TX_SEL
- Explanation: CLKID_HDMI_TX_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `161`
- New: `60`

### Rust Evidence

- Graph edges: `0`

## W-000555 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HIFI_PLL
- Explanation: CLKID_HIFI_PLL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `74`
- New: `69`

### Rust Evidence

- Graph edges: `0`

## W-000556 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HIFI_PLL_DCO
- Explanation: CLKID_HIFI_PLL_DCO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `104`
- New: `88`

### Rust Evidence

- Graph edges: `0`

## W-000557 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HIU_IFACE
- Explanation: CLKID_HIU_IFACE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `30`
- New: `29`

### Rust Evidence

- Graph edges: `0`

## W-000558 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_I2C
- Explanation: CLKID_I2C changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `24`
- New: `22`

### Rust Evidence

- Graph edges: `0`

## W-000559 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_ISA
- Explanation: CLKID_ISA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `20`
- New: `18`

### Rust Evidence

- Graph edges: `0`

## W-000560 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MALI
- Explanation: CLKID_MALI changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `175`
- New: `172`

### Rust Evidence

- Graph edges: `0`

## W-000561 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MALI_0
- Explanation: CLKID_MALI_0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `171`
- New: `72`

### Rust Evidence

- Graph edges: `0`

## W-000562 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MALI_0_DIV
- Explanation: CLKID_MALI_0_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `170`
- New: `71`

### Rust Evidence

- Graph edges: `0`

## W-000563 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MALI_0_SEL
- Explanation: CLKID_MALI_0_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `169`
- New: `70`

### Rust Evidence

- Graph edges: `0`

## W-000564 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MALI_1
- Explanation: CLKID_MALI_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `174`
- New: `75`

### Rust Evidence

- Graph edges: `0`

## W-000565 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MALI_1_DIV
- Explanation: CLKID_MALI_1_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `173`
- New: `74`

### Rust Evidence

- Graph edges: `0`

## W-000566 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MALI_1_SEL
- Explanation: CLKID_MALI_1_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `172`
- New: `73`

### Rust Evidence

- Graph edges: `0`

## W-000567 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MIPI_DSI_HOST
- Explanation: CLKID_MIPI_DSI_HOST changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `18`
- New: `17`

### Rust Evidence

- Graph edges: `0`

## W-000568 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MIPI_DSI_PHY
- Explanation: CLKID_MIPI_DSI_PHY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `31`
- New: `25`

### Rust Evidence

- Graph edges: `0`

## W-000569 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MMC_PCLK
- Explanation: CLKID_MMC_PCLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `56`
- New: `50`

### Rust Evidence

- Graph edges: `0`

## W-000570 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MPLL0_DIV
- Explanation: CLKID_MPLL0_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `69`
- New: `65`

### Rust Evidence

- Graph edges: `0`

## W-000571 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MPLL1_DIV
- Explanation: CLKID_MPLL1_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `70`
- New: `66`

### Rust Evidence

- Graph edges: `0`

## W-000572 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MPLL2_DIV
- Explanation: CLKID_MPLL2_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `71`
- New: `67`

### Rust Evidence

- Graph edges: `0`

## W-000573 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MPLL3_DIV
- Explanation: CLKID_MPLL3_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `72`
- New: `68`

### Rust Evidence

- Graph edges: `0`

## W-000574 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MPLL_50M
- Explanation: CLKID_MPLL_50M changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `177`
- New: `22`

### Rust Evidence

- Graph edges: `0`

## W-000575 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MPLL_50M_DIV
- Explanation: CLKID_MPLL_50M_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `176`
- New: `21`

### Rust Evidence

- Graph edges: `0`

## W-000576 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MPLL_PREDIV
- Explanation: CLKID_MPLL_PREDIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `73`
- New: `70`

### Rust Evidence

- Graph edges: `0`

## W-000577 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PCIE_PLL
- Explanation: CLKID_PCIE_PLL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `201`
- New: `76`

### Rust Evidence

- Graph edges: `0`

## W-000578 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PCIE_PLL_DCO
- Explanation: CLKID_PCIE_PLL_DCO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `198`
- New: `89`

### Rust Evidence

- Graph edges: `0`

## W-000579 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PCIE_PLL_OD
- Explanation: CLKID_PCIE_PLL_OD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `200`
- New: `90`

### Rust Evidence

- Graph edges: `0`

## W-000580 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PERIPHS
- Explanation: CLKID_PERIPHS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `22`
- New: `20`

### Rust Evidence

- Graph edges: `0`

## W-000581 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PL301
- Explanation: CLKID_PL301 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `21`
- New: `19`

### Rust Evidence

- Graph edges: `0`

## W-000582 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_RESET
- Explanation: CLKID_RESET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `44`
- New: `41`

### Rust Evidence

- Graph edges: `0`

## W-000583 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_RNG0
- Explanation: CLKID_RNG0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `27`
- New: `23`

### Rust Evidence

- Graph edges: `0`

## W-000584 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_A
- Explanation: CLKID_SD_EMMC_A changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `33`
- New: `126`

### Rust Evidence

- Graph edges: `0`

## W-000585 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_B
- Explanation: CLKID_SD_EMMC_B changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `34`
- New: `31`

### Rust Evidence

- Graph edges: `0`

## W-000586 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_B_CLK0
- Explanation: CLKID_SD_EMMC_B_CLK0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `61`
- New: `59`

### Rust Evidence

- Graph edges: `0`

## W-000587 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_B_CLK0_DIV
- Explanation: CLKID_SD_EMMC_B_CLK0_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `66`
- New: `62`

### Rust Evidence

- Graph edges: `0`

## W-000588 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_B_CLK0_SEL
- Explanation: CLKID_SD_EMMC_B_CLK0_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `65`
- New: `61`

### Rust Evidence

- Graph edges: `0`

## W-000589 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_C
- Explanation: CLKID_SD_EMMC_C changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `35`
- New: `32`

### Rust Evidence

- Graph edges: `0`

## W-000590 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_C_CLK0
- Explanation: CLKID_SD_EMMC_C_CLK0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `62`
- New: `60`

### Rust Evidence

- Graph edges: `0`

## W-000591 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_C_CLK0_DIV
- Explanation: CLKID_SD_EMMC_C_CLK0_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `68`
- New: `64`

### Rust Evidence

- Graph edges: `0`

## W-000592 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_C_CLK0_SEL
- Explanation: CLKID_SD_EMMC_C_CLK0_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `67`
- New: `63`

### Rust Evidence

- Graph edges: `0`

## W-000593 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SPICC0
- Explanation: CLKID_SPICC0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `23`
- New: `21`

### Rust Evidence

- Graph edges: `0`

## W-000594 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SPICC1
- Explanation: CLKID_SPICC1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `29`
- New: `26`

### Rust Evidence

- Graph edges: `0`

## W-000595 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_PLL_DCO
- Explanation: CLKID_SYS_PLL_DCO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `102`
- New: `85`

### Rust Evidence

- Graph edges: `0`

## W-000596 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_PLL_DIV16
- Explanation: CLKID_SYS_PLL_DIV16 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `179`
- New: `14`

### Rust Evidence

- Graph edges: `0`

## W-000597 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_TS
- Explanation: CLKID_TS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `212`
- New: `69`

### Rust Evidence

- Graph edges: `0`

## W-000598 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_TS_DIV
- Explanation: CLKID_TS_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `211`
- New: `152`

### Rust Evidence

- Graph edges: `0`

## W-000599 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_UART0
- Explanation: CLKID_UART0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `28`
- New: `24`

### Rust Evidence

- Graph edges: `0`

## W-000600 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_UART1
- Explanation: CLKID_UART1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `42`
- New: `37`

### Rust Evidence

- Graph edges: `0`

## W-000601 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_USB
- Explanation: CLKID_USB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `47`
- New: `42`

### Rust Evidence

- Graph edges: `0`

## W-000602 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_USB1_DDR_BRIDGE
- Explanation: CLKID_USB1_DDR_BRIDGE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `55`
- New: `48`

### Rust Evidence

- Graph edges: `0`

## W-000603 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VAPB
- Explanation: CLKID_VAPB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `124`
- New: `105`

### Rust Evidence

- Graph edges: `0`

## W-000604 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VAPB_0
- Explanation: CLKID_VAPB_0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `119`
- New: `100`

### Rust Evidence

- Graph edges: `0`

## W-000605 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VAPB_0_DIV
- Explanation: CLKID_VAPB_0_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `118`
- New: `98`

### Rust Evidence

- Graph edges: `0`

## W-000606 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VAPB_0_SEL
- Explanation: CLKID_VAPB_0_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `117`
- New: `99`

### Rust Evidence

- Graph edges: `0`

## W-000607 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VAPB_1
- Explanation: CLKID_VAPB_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `122`
- New: `103`

### Rust Evidence

- Graph edges: `0`

## W-000608 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VAPB_1_DIV
- Explanation: CLKID_VAPB_1_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `121`
- New: `101`

### Rust Evidence

- Graph edges: `0`

## W-000609 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VAPB_1_SEL
- Explanation: CLKID_VAPB_1_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `120`
- New: `102`

### Rust Evidence

- Graph edges: `0`

## W-000610 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VAPB_SEL
- Explanation: CLKID_VAPB_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `123`
- New: `104`

### Rust Evidence

- Graph edges: `0`

## W-000611 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK
- Explanation: CLKID_VCLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `138`
- New: `106`

### Rust Evidence

- Graph edges: `0`

## W-000612 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2
- Explanation: CLKID_VCLK2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `139`
- New: `107`

### Rust Evidence

- Graph edges: `0`

## W-000613 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_DIV
- Explanation: CLKID_VCLK2_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `137`
- New: `113`

### Rust Evidence

- Graph edges: `0`

## W-000614 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_DIV1
- Explanation: CLKID_VCLK2_DIV1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `153`
- New: `127`

### Rust Evidence

- Graph edges: `0`

## W-000615 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_DIV12
- Explanation: CLKID_VCLK2_DIV12 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `157`
- New: `131`

### Rust Evidence

- Graph edges: `0`

## W-000616 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_DIV12_EN
- Explanation: CLKID_VCLK2_DIV12_EN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `147`
- New: `121`

### Rust Evidence

- Graph edges: `0`

## W-000617 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_DIV2
- Explanation: CLKID_VCLK2_DIV2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `154`
- New: `128`

### Rust Evidence

- Graph edges: `0`

## W-000618 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_DIV2_EN
- Explanation: CLKID_VCLK2_DIV2_EN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `144`
- New: `118`

### Rust Evidence

- Graph edges: `0`

## W-000619 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_DIV4
- Explanation: CLKID_VCLK2_DIV4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `155`
- New: `129`

### Rust Evidence

- Graph edges: `0`

## W-000620 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_DIV4_EN
- Explanation: CLKID_VCLK2_DIV4_EN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `145`
- New: `119`

### Rust Evidence

- Graph edges: `0`

## W-000621 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_DIV6
- Explanation: CLKID_VCLK2_DIV6 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `156`
- New: `130`

### Rust Evidence

- Graph edges: `0`

## W-000622 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_DIV6_EN
- Explanation: CLKID_VCLK2_DIV6_EN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `146`
- New: `120`

### Rust Evidence

- Graph edges: `0`

## W-000623 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_INPUT
- Explanation: CLKID_VCLK2_INPUT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `135`
- New: `111`

### Rust Evidence

- Graph edges: `0`

## W-000624 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_SEL
- Explanation: CLKID_VCLK2_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `133`
- New: `109`

### Rust Evidence

- Graph edges: `0`

## W-000625 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_DIV
- Explanation: CLKID_VCLK_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `136`
- New: `112`

### Rust Evidence

- Graph edges: `0`

## W-000626 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_DIV1
- Explanation: CLKID_VCLK_DIV1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `148`
- New: `122`

### Rust Evidence

- Graph edges: `0`

## W-000627 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_DIV12
- Explanation: CLKID_VCLK_DIV12 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `152`
- New: `126`

### Rust Evidence

- Graph edges: `0`

## W-000628 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_DIV12_EN
- Explanation: CLKID_VCLK_DIV12_EN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `143`
- New: `117`

### Rust Evidence

- Graph edges: `0`

## W-000629 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_DIV2
- Explanation: CLKID_VCLK_DIV2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `149`
- New: `123`

### Rust Evidence

- Graph edges: `0`

## W-000630 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_DIV2_EN
- Explanation: CLKID_VCLK_DIV2_EN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `140`
- New: `114`

### Rust Evidence

- Graph edges: `0`

## W-000631 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_DIV4
- Explanation: CLKID_VCLK_DIV4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `150`
- New: `124`

### Rust Evidence

- Graph edges: `0`

## W-000632 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_DIV4_EN
- Explanation: CLKID_VCLK_DIV4_EN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `141`
- New: `115`

### Rust Evidence

- Graph edges: `0`

## W-000633 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_DIV6
- Explanation: CLKID_VCLK_DIV6 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `151`
- New: `125`

### Rust Evidence

- Graph edges: `0`

## W-000634 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_DIV6_EN
- Explanation: CLKID_VCLK_DIV6_EN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `142`
- New: `116`

### Rust Evidence

- Graph edges: `0`

## W-000635 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_INPUT
- Explanation: CLKID_VCLK_INPUT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `134`
- New: `110`

### Rust Evidence

- Graph edges: `0`

## W-000636 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_SEL
- Explanation: CLKID_VCLK_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `132`
- New: `108`

### Rust Evidence

- Graph edges: `0`

## W-000637 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VID_PLL
- Explanation: CLKID_VID_PLL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `129`
- New: `30`

### Rust Evidence

- Graph edges: `0`

## W-000638 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VID_PLL_DIV
- Explanation: CLKID_VID_PLL_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `131`
- New: `28`

### Rust Evidence

- Graph edges: `0`

## W-000639 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VID_PLL_SEL
- Explanation: CLKID_VID_PLL_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `130`
- New: `29`

### Rust Evidence

- Graph edges: `0`

## W-000640 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VPU
- Explanation: CLKID_VPU changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `116`
- New: `97`

### Rust Evidence

- Graph edges: `0`

## W-000641 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VPU_0
- Explanation: CLKID_VPU_0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `112`
- New: `93`

### Rust Evidence

- Graph edges: `0`

## W-000642 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VPU_0_DIV
- Explanation: CLKID_VPU_0_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `111`
- New: `91`

### Rust Evidence

- Graph edges: `0`

## W-000643 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VPU_0_SEL
- Explanation: CLKID_VPU_0_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `110`
- New: `92`

### Rust Evidence

- Graph edges: `0`

## W-000644 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VPU_1
- Explanation: CLKID_VPU_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `115`
- New: `96`

### Rust Evidence

- Graph edges: `0`

## W-000645 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VPU_1_DIV
- Explanation: CLKID_VPU_1_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `114`
- New: `94`

### Rust Evidence

- Graph edges: `0`

## W-000646 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VPU_1_SEL
- Explanation: CLKID_VPU_1_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `113`
- New: `95`

### Rust Evidence

- Graph edges: `0`

## W-000647 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VPU_INTR
- Explanation: CLKID_VPU_INTR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `58`
- New: `51`

### Rust Evidence

- Graph edges: `0`

## W-000648 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_CMU_MIF_BUSP
- Explanation: CLK_DOUT_CMU_MIF_BUSP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `125`
- New: `27`

### Rust Evidence

- Graph edges: `0`

## W-000649 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_DOUT_CMU_OTP
- Explanation: CLK_DOUT_CMU_OTP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `128`
- New: `13`

### Rust Evidence

- Graph edges: `0`

## W-000650 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLK_FOUT_USB_PLL
- Explanation: CLK_FOUT_USB_PLL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `1`
- New: `13`

### Rust Evidence

- Graph edges: `0`

## W-000651 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: DMA_BIT_MASK
- Explanation: DMA_BIT_MASK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `(((n) == 64) ? ~0ULL : ((1ULL<<(n))-1))`
- New: `GENMASK_ULL(n - 1, 0)`

### Rust Evidence

- Graph edges: `0`

## W-000652 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: HASH_MAX_DESCSIZE
- Explanation: HASH_MAX_DESCSIZE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `(sizeof(struct shash_desc) + 361)`
- New: `(sizeof(struct shash_desc) + \`

### Rust Evidence

- Graph edges: `0`

## W-000653 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: HASH_MAX_STATESIZE
- Explanation: HASH_MAX_STATESIZE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `200 + 144 + 1`
- New: `HASH_STATE_AND_BLOCK(200, 144)`

### Rust Evidence

- Graph edges: `0`

## W-000654 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: PHY_ID_MATCH_EXACT
- Explanation: PHY_ID_MATCH_EXACT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `.phy_id = (id), .phy_id_mask = GENMASK(31, 0)`
- New: `.phy_id = (id), .phy_id_mask = PHY_ID_MATCH_EXTACT_MASK`

### Rust Evidence

- Graph edges: `0`

## W-000655 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: PHY_ID_MATCH_MODEL
- Explanation: PHY_ID_MATCH_MODEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `.phy_id = (id), .phy_id_mask = GENMASK(31, 4)`
- New: `.phy_id = (id), .phy_id_mask = PHY_ID_MATCH_MODEL_MASK`

### Rust Evidence

- Graph edges: `0`

## W-000656 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: PHY_ID_MATCH_VENDOR
- Explanation: PHY_ID_MATCH_VENDOR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `.phy_id = (id), .phy_id_mask = GENMASK(31, 10)`
- New: `.phy_id = (id), .phy_id_mask = PHY_ID_MATCH_VENDOR_MASK`

### Rust Evidence

- Graph edges: `0`

## W-000657 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: TTM_NUM_MEM_TYPES
- Explanation: TTM_NUM_MEM_TYPES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `9`

### Rust Evidence

- Graph edges: `0`

## W-000659 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: kvmalloc
- Explanation: kvmalloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `kvmalloc_node(_size, _flags, NUMA_NO_NODE)`
- New: `kvmalloc_node(__VA_ARGS__, NUMA_NO_NODE)`

### Rust Evidence

- Graph edges: `0`

## W-000660 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: kvmalloc_node
- Explanation: kvmalloc_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `alloc_hooks(kvmalloc_node_noprof(__VA_ARGS__))`
- New: `kvmalloc_node_align(_s, 1, _f, _n)`

### Rust Evidence

- Graph edges: `0`
