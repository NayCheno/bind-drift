# BindDrift Ranked Warnings

## W-000398 SignatureDrift

- Risk: High
- Score: 14.6
- Symbol: __alloc_size
- Explanation: __alloc_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['1', '2) void *kvcalloc(size_t n, size_t size, gfp_t flags'], 'return_type': 'static inline'}`
- New: `{'params': ['1', '2) void * kvmalloc_array_node_noprof(size_t n, size_t size, gfp_t flags, int node'], 'return_type': 'static inline'}`

### Rust Evidence

- Graph edges: `22`

## W-000210 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: bio
- Explanation: bio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'bi_next', 'type': '*mut bio'}, {'name': 'bi_bdev', 'type': '*mut block_device'}, {'name': 'bi_opf', 'type': 'blk_opf_t'}, {'name': 'bi_flags', 'type': 'core::ffi::c_ushort'}, {'name': 'bi_ioprio', 'type': 'core::ffi::c_ushort'}, {'name': 'bi_write_hint', 'type': 'rw_hint'}, {'name': 'bi_status', 'type': 'blk_status_t'}, {'name': '__bi_remaining', 'type': 'atomic_t'}, {'name': 'bi_iter', 'type': 'bvec_iter'}, {'name': 'bi_cookie', 'type': 'blk_qc_t'}, {'name': 'bi_end_io', 'type': 'bio_end_io_t'}, {'name': 'bi_private', 'type': '*mut core::ffi::c_void'}, {'name': 'bi_blkg', 'type': '*mut blkcg_gq'}, {'name': 'bi_issue', 'type': 'bio_issue'}, {'name': 'bi_iocost_cost', 'type': 'u64_'}, {'name': '__bindgen_anon_1', 'type': 'bio__bindgen_ty_1'}, {'name': 'bi_vcnt', 'type': 'core::ffi::c_ushort'}, {'name': 'bi_max_vecs', 'type': 'core::ffi::c_ushort'}, {'name': '__bi_cnt', 'type': 'atomic_t'}, {'name': 'bi_io_vec', 'type': '*mut bio_vec'}, {'name': 'bi_pool', 'type': '*mut bio_set'}, {'name': 'bi_inline_vecs', 'type': '__IncompleteArrayField<bio_vec>'}]`
- New: `[{'name': 'bi_next', 'type': '*mut bio'}, {'name': 'bi_bdev', 'type': '*mut block_device'}, {'name': 'bi_opf', 'type': 'blk_opf_t'}, {'name': 'bi_flags', 'type': 'core::ffi::c_ushort'}, {'name': 'bi_ioprio', 'type': 'core::ffi::c_ushort'}, {'name': 'bi_write_hint', 'type': 'rw_hint'}, {'name': 'bi_status', 'type': 'blk_status_t'}, {'name': '__bi_remaining', 'type': 'atomic_t'}, {'name': 'bi_iter', 'type': 'bvec_iter'}, {'name': '__bindgen_anon_1', 'type': 'bio__bindgen_ty_1'}, {'name': 'bi_end_io', 'type': 'bio_end_io_t'}, {'name': 'bi_private', 'type': '*mut core::ffi::c_void'}, {'name': 'bi_blkg', 'type': '*mut blkcg_gq'}, {'name': 'bi_issue', 'type': 'bio_issue'}, {'name': 'bi_iocost_cost', 'type': 'u64_'}, {'name': '__bindgen_anon_2', 'type': 'bio__bindgen_ty_2'}, {'name': 'bi_vcnt', 'type': 'core::ffi::c_ushort'}, {'name': 'bi_max_vecs', 'type': 'core::ffi::c_ushort'}, {'name': '__bi_cnt', 'type': 'atomic_t'}, {'name': 'bi_io_vec', 'type': '*mut bio_vec'}, {'name': 'bi_pool', 'type': '*mut bio_set'}, {'name': 'bi_inline_vecs', 'type': '__IncompleteArrayField<bio_vec>'}]`

### Rust Evidence

- Graph edges: `24`

## W-000223 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: kunit
- Explanation: kunit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'priv_', 'type': '*mut core::ffi::c_void'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'log', 'type': '*mut string_stream'}, {'name': 'try_catch', 'type': 'kunit_try_catch'}, {'name': 'param_value', 'type': '*const core::ffi::c_void'}, {'name': 'param_index', 'type': 'core::ffi::c_int'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'status', 'type': 'kunit_status'}, {'name': 'resources', 'type': 'list_head'}, {'name': 'status_comment', 'type': '[core::ffi::c_char; 256usize]'}]`
- New: `[{'name': 'priv_', 'type': '*mut core::ffi::c_void'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'log', 'type': '*mut string_stream'}, {'name': 'try_catch', 'type': 'kunit_try_catch'}, {'name': 'param_value', 'type': '*const core::ffi::c_void'}, {'name': 'param_index', 'type': 'core::ffi::c_int'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'status', 'type': 'kunit_status'}, {'name': 'resources', 'type': 'list_head'}, {'name': 'status_comment', 'type': '[core::ffi::c_char; 256usize]'}, {'name': 'last_seen', 'type': 'kunit_loc'}]`

### Rust Evidence

- Graph edges: `50`

## W-000225 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: led_trigger
- Explanation: led_trigger changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'activate', 'type': '::core::option::Option<'}, {'name': 'deactivate', 'type': '::core::option::Option<unsafe extern "C" fn(led_cdev: *mut led_classdev)>'}, {'name': 'trigger_type', 'type': '*mut led_hw_trigger_type'}, {'name': 'leddev_list_lock', 'type': 'spinlock_t'}, {'name': 'led_cdevs', 'type': 'list_head'}, {'name': 'next_trig', 'type': 'list_head'}, {'name': 'groups', 'type': '*mut *const attribute_group'}]`
- New: `[{'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'activate', 'type': '::core::option::Option<'}, {'name': 'deactivate', 'type': '::core::option::Option<unsafe extern "C" fn(led_cdev: *mut led_classdev)>'}, {'name': 'brightness', 'type': 'led_brightness'}, {'name': 'trigger_type', 'type': '*mut led_hw_trigger_type'}, {'name': 'leddev_list_lock', 'type': 'spinlock_t'}, {'name': 'led_cdevs', 'type': 'list_head'}, {'name': 'next_trig', 'type': 'list_head'}, {'name': 'groups', 'type': '*mut *const attribute_group'}]`

### Rust Evidence

- Graph edges: `23`

## W-000231 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: statx
- Explanation: statx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'stx_mask', 'type': '__u32'}, {'name': 'stx_blksize', 'type': '__u32'}, {'name': 'stx_attributes', 'type': '__u64'}, {'name': 'stx_nlink', 'type': '__u32'}, {'name': 'stx_uid', 'type': '__u32'}, {'name': 'stx_gid', 'type': '__u32'}, {'name': 'stx_mode', 'type': '__u16'}, {'name': '__spare0', 'type': '[__u16; 1usize]'}, {'name': 'stx_ino', 'type': '__u64'}, {'name': 'stx_size', 'type': '__u64'}, {'name': 'stx_blocks', 'type': '__u64'}, {'name': 'stx_attributes_mask', 'type': '__u64'}, {'name': 'stx_atime', 'type': 'statx_timestamp'}, {'name': 'stx_btime', 'type': 'statx_timestamp'}, {'name': 'stx_ctime', 'type': 'statx_timestamp'}, {'name': 'stx_mtime', 'type': 'statx_timestamp'}, {'name': 'stx_rdev_major', 'type': '__u32'}, {'name': 'stx_rdev_minor', 'type': '__u32'}, {'name': 'stx_dev_major', 'type': '__u32'}, {'name': 'stx_dev_minor', 'type': '__u32'}, {'name': 'stx_mnt_id', 'type': '__u64'}, {'name': 'stx_dio_mem_align', 'type': '__u32'}, {'name': 'stx_dio_offset_align', 'type': '__u32'}, {'name': '__spare3', 'type': '[__u64; 12usize]'}]`
- New: `[{'name': 'stx_mask', 'type': '__u32'}, {'name': 'stx_blksize', 'type': '__u32'}, {'name': 'stx_attributes', 'type': '__u64'}, {'name': 'stx_nlink', 'type': '__u32'}, {'name': 'stx_uid', 'type': '__u32'}, {'name': 'stx_gid', 'type': '__u32'}, {'name': 'stx_mode', 'type': '__u16'}, {'name': '__spare0', 'type': '[__u16; 1usize]'}, {'name': 'stx_ino', 'type': '__u64'}, {'name': 'stx_size', 'type': '__u64'}, {'name': 'stx_blocks', 'type': '__u64'}, {'name': 'stx_attributes_mask', 'type': '__u64'}, {'name': 'stx_atime', 'type': 'statx_timestamp'}, {'name': 'stx_btime', 'type': 'statx_timestamp'}, {'name': 'stx_ctime', 'type': 'statx_timestamp'}, {'name': 'stx_mtime', 'type': 'statx_timestamp'}, {'name': 'stx_rdev_major', 'type': '__u32'}, {'name': 'stx_rdev_minor', 'type': '__u32'}, {'name': 'stx_dev_major', 'type': '__u32'}, {'name': 'stx_dev_minor', 'type': '__u32'}, {'name': 'stx_mnt_id', 'type': '__u64'}, {'name': 'stx_dio_mem_align', 'type': '__u32'}, {'name': 'stx_dio_offset_align', 'type': '__u32'}, {'name': 'stx_subvol', 'type': '__u64'}, {'name': '__spare3', 'type': '[__u64; 11usize]'}]`

### Rust Evidence

- Graph edges: `31`

## W-000036 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: alloc_pages
- Explanation: alloc_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `6`

## W-000113 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: kmem_cache_alloc
- Explanation: kmem_cache_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `4`

## W-000193 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: vmalloc
- Explanation: vmalloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `4`

## W-000020 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: __kmalloc
- Explanation: __kmalloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `3`

## W-000121 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: kmemdup
- Explanation: kmemdup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `3`

## W-000031 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __vmalloc
- Explanation: __vmalloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `2`

## W-000040 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: alloc_pages_exact
- Explanation: alloc_pages_exact changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `2`

## W-000067 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: disable_delayed_work
- Explanation: disable_delayed_work changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000069 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: disable_work
- Explanation: disable_work changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000104 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: kmalloc_large
- Explanation: kmalloc_large changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `2`

## W-000131 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: mm_get_unmapped_area
- Explanation: mm_get_unmapped_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000161 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: simple_offset_rename
- Explanation: simple_offset_rename changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000002 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __alloc_pages
- Explanation: __alloc_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000004 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __alloc_pages_noprof
- Explanation: __alloc_pages_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000008 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __bpf_dynptr_is_rdonly
- Explanation: __bpf_dynptr_is_rdonly changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000009 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __dma_need_sync
- Explanation: __dma_need_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000010 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __dma_sync_sg_for_cpu
- Explanation: __dma_sync_sg_for_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000011 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __dma_sync_sg_for_device
- Explanation: __dma_sync_sg_for_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000012 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __dma_sync_single_for_cpu
- Explanation: __dma_sync_single_for_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000013 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __dma_sync_single_for_device
- Explanation: __dma_sync_single_for_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000014 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __folio_alloc
- Explanation: __folio_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000015 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __folio_alloc_noprof
- Explanation: __folio_alloc_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000017 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __get_unmapped_area
- Explanation: __get_unmapped_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000021 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kmalloc_node
- Explanation: __kmalloc_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000022 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kmalloc_node_noprof
- Explanation: __kmalloc_node_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000024 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kmalloc_noprof
- Explanation: __kmalloc_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000027 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __seq_puts
- Explanation: __seq_puts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000035 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: _find_first_and_and_bit
- Explanation: _find_first_and_and_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000037 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_pages_bulk_array_mempolicy
- Explanation: alloc_pages_bulk_array_mempolicy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000038 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_pages_bulk_array_mempolicy_noprof
- Explanation: alloc_pages_bulk_array_mempolicy_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000039 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_pages_bulk_noprof
- Explanation: alloc_pages_bulk_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000041 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_pages_exact_nid
- Explanation: alloc_pages_exact_nid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000042 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_pages_exact_nid_noprof
- Explanation: alloc_pages_exact_nid_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000043 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_pages_exact_noprof
- Explanation: alloc_pages_exact_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000044 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_pages_mpol
- Explanation: alloc_pages_mpol changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000045 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_pages_mpol_noprof
- Explanation: alloc_pages_mpol_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000046 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_pages_noprof
- Explanation: alloc_pages_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000047 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: apply_relocation
- Explanation: apply_relocation changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'buf', 'type': '*mut u8_'}, {'name': 'len', 'type': 'usize'}, {'name': 'dest', 'type': '*mut u8_'}, {'name': 'src', 'type': '*mut u8_'}, {'name': 'src_len', 'type': 'usize'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'buf', 'type': '*mut u8_'}, {'name': 'instr', 'type': '*const u8_'}, {'name': 'instrlen', 'type': 'usize'}, {'name': 'repl', 'type': '*mut u8_'}, {'name': 'repl_len', 'type': 'usize'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000048 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_get_unmapped_area_topdown_vmflags
- Explanation: arch_get_unmapped_area_topdown_vmflags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000049 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_get_unmapped_area_vmflags
- Explanation: arch_get_unmapped_area_vmflags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000050 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_protect_bpf_trampoline
- Explanation: arch_protect_bpf_trampoline changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'image', 'type': '*mut core::ffi::c_void'}, {'name': 'size', 'type': 'core::ffi::c_uint'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'image', 'type': '*mut core::ffi::c_void'}, {'name': 'size', 'type': 'core::ffi::c_uint'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000053 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_wq_cancel_and_free
- Explanation: bpf_wq_cancel_and_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000054 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgroup_rstat_flush_release
- Explanation: cgroup_rstat_flush_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': '()'}`
- New: `{'params': [{'name': 'cgrp', 'type': '*mut cgroup'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000055 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cgwb_calc_thresh
- Explanation: cgwb_calc_thresh changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000056 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: codetag_get_ct_iter
- Explanation: codetag_get_ct_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000057 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: codetag_lock_module_list
- Explanation: codetag_lock_module_list changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000058 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: codetag_next_ct
- Explanation: codetag_next_ct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000059 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: codetag_register_type
- Explanation: codetag_register_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000060 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: codetag_to_text
- Explanation: codetag_to_text changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000061 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: codetag_trylock_module_list
- Explanation: codetag_trylock_module_list changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000062 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: console_replay_all
- Explanation: console_replay_all changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000064 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_show_string
- Explanation: device_show_string changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000065 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_wakeup_disable
- Explanation: device_wakeup_disable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'dev', 'type': '*mut device'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'dev', 'type': '*mut device'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000068 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: disable_delayed_work_sync
- Explanation: disable_delayed_work_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000070 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: disable_work_sync
- Explanation: disable_work_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000072 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_skip_sync
- Explanation: dma_skip_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000077 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_accept
- Explanation: do_accept changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'file', 'type': '*mut file'}, {'name': 'file_flags', 'type': 'core::ffi::c_uint'}, {'name': 'upeer_sockaddr', 'type': '*mut sockaddr'}, {'name': 'upeer_addrlen', 'type': '*mut core::ffi::c_int'}, {'name': 'flags', 'type': 'core::ffi::c_int'}], 'return_type': '*mut file'}`
- New: `{'params': [{'name': 'file', 'type': '*mut file'}, {'name': 'arg', 'type': '*mut proto_accept_arg'}, {'name': 'upeer_sockaddr', 'type': '*mut sockaddr'}, {'name': 'upeer_addrlen', 'type': '*mut core::ffi::c_int'}, {'name': 'flags', 'type': 'core::ffi::c_int'}], 'return_type': '*mut file'}`

### Rust Evidence

- Graph edges: `1`

## W-000078 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: enable_delayed_work
- Explanation: enable_delayed_work changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000079 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: enable_work
- Explanation: enable_work changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000080 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: extra
- Explanation: extra changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000083 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_alloc
- Explanation: folio_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000084 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_alloc_noprof
- Explanation: folio_alloc_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000088 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: follow_pte
- Explanation: follow_pte changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'address', 'type': 'core::ffi::c_ulong'}, {'name': 'ptepp', 'type': '*mut *mut pte_t'}, {'name': 'ptlp', 'type': '*mut *mut spinlock_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'address', 'type': 'core::ffi::c_ulong'}, {'name': 'ptepp', 'type': '*mut *mut pte_t'}, {'name': 'ptlp', 'type': '*mut *mut spinlock_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000090 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_free_pages_noprof
- Explanation: get_free_pages_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000094 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_xsave_addr
- Explanation: get_xsave_addr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000095 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_zeroed_page
- Explanation: get_zeroed_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000096 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_zeroed_page_noprof
- Explanation: get_zeroed_page_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000099 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: in_thrashing
- Explanation: in_thrashing changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(42usize, 1u8) as u32) } } #[inline] pub fn set_in_thrashing(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(43usize, 1u8) as u32) } } #[inline] pub fn set_in_thrashing(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000101 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_free_buddy_page
- Explanation: is_free_buddy_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'page', 'type': '*mut page'}], 'return_type': 'bool_'}`
- New: `{'params': [{'name': 'page', 'type': '*const page'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000102 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: jump_label_init_ro
- Explanation: jump_label_init_ro changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000103 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_file_open
- Explanation: kernel_file_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'path', 'type': '*const path'}, {'name': 'flags', 'type': 'core::ffi::c_int'}, {'name': 'inode', 'type': '*mut inode'}, {'name': 'cred', 'type': '*const cred'}], 'return_type': '*mut file'}`
- New: `{'params': [{'name': 'path', 'type': '*const path'}, {'name': 'flags', 'type': 'core::ffi::c_int'}, {'name': 'cred', 'type': '*const cred'}], 'return_type': '*mut file'}`

### Rust Evidence

- Graph edges: `1`

## W-000105 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmalloc_large_node
- Explanation: kmalloc_large_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000106 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmalloc_large_node_noprof
- Explanation: kmalloc_large_node_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000107 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmalloc_large_noprof
- Explanation: kmalloc_large_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000108 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmalloc_node_trace
- Explanation: kmalloc_node_trace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000109 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmalloc_node_trace_noprof
- Explanation: kmalloc_node_trace_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000110 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmalloc_node_track_caller_noprof
- Explanation: kmalloc_node_track_caller_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000111 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmalloc_trace
- Explanation: kmalloc_trace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000112 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmalloc_trace_noprof
- Explanation: kmalloc_trace_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000114 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmem_cache_alloc_bulk
- Explanation: kmem_cache_alloc_bulk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000115 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmem_cache_alloc_bulk_noprof
- Explanation: kmem_cache_alloc_bulk_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000116 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmem_cache_alloc_lru
- Explanation: kmem_cache_alloc_lru changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000117 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmem_cache_alloc_lru_noprof
- Explanation: kmem_cache_alloc_lru_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000118 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmem_cache_alloc_node
- Explanation: kmem_cache_alloc_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000119 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmem_cache_alloc_node_noprof
- Explanation: kmem_cache_alloc_node_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000120 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmem_cache_alloc_noprof
- Explanation: kmem_cache_alloc_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000122 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmemdup_array
- Explanation: kmemdup_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'src', 'type': '*const core::ffi::c_void'}, {'name': 'element_size', 'type': 'usize'}, {'name': 'count', 'type': 'usize'}, {'name': 'gfp', 'type': 'gfp_t'}], 'return_type': '*mut core::ffi::c_void'}`
- New: `{'params': [{'name': 'src', 'type': '*const core::ffi::c_void'}, {'name': 'count', 'type': 'usize'}, {'name': 'element_size', 'type': 'usize'}, {'name': 'gfp', 'type': 'gfp_t'}], 'return_type': '*mut core::ffi::c_void'}`

### Rust Evidence

- Graph edges: `1`

## W-000123 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kmemdup_noprof
- Explanation: kmemdup_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000124 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: krealloc_noprof
- Explanation: krealloc_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000125 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kvmalloc_node
- Explanation: kvmalloc_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000126 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kvmalloc_node_noprof
- Explanation: kvmalloc_node_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000127 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kvrealloc
- Explanation: kvrealloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000128 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kvrealloc_noprof
- Explanation: kvrealloc_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000129 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lookup_address_in_pgd_attr
- Explanation: lookup_address_in_pgd_attr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000132 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mm_get_unmapped_area_vmflags
- Explanation: mm_get_unmapped_area_vmflags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000133 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: module_address_lookup
- Explanation: module_address_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'addr', 'type': 'core::ffi::c_ulong'}, {'name': 'symbolsize', 'type': '*mut core::ffi::c_ulong'}, {'name': 'offset', 'type': '*mut core::ffi::c_ulong'}, {'name': 'modname', 'type': '*mut *mut core::ffi::c_char'}, {'name': 'modbuildid', 'type': '*mut *const core::ffi::c_uchar'}, {'name': 'namebuf', 'type': '*mut core::ffi::c_char'}], 'return_type': '*const core::ffi::c_char'}`
- New: `{'params': [{'name': 'addr', 'type': 'core::ffi::c_ulong'}, {'name': 'symbolsize', 'type': '*mut core::ffi::c_ulong'}, {'name': 'offset', 'type': '*mut core::ffi::c_ulong'}, {'name': 'modname', 'type': '*mut *mut core::ffi::c_char'}, {'name': 'modbuildid', 'type': '*mut *const core::ffi::c_uchar'}, {'name': 'namebuf', 'type': '*mut core::ffi::c_char'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000135 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: napi_alloc_skb
- Explanation: napi_alloc_skb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000137 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: numa_fill_memblks
- Explanation: numa_fill_memblks changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000138 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: offset
- Explanation: offset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000139 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pasid_activated
- Explanation: pasid_activated changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000140 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcpu_alloc_noprof
- Explanation: pcpu_alloc_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000145 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: remap_verify_area
- Explanation: remap_verify_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000149 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: reported_split_lock
- Explanation: reported_split_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(41usize, 1u8) as u32) } } #[inline] pub fn set_reported_split_lock(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(42usize, 1u8) as u32) } } #[inline] pub fn set_reported_split_lock(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `1`

## W-000150 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rhashtable_init
- Explanation: rhashtable_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000151 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rhashtable_init_noprof
- Explanation: rhashtable_init_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000152 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rhltable_init
- Explanation: rhltable_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000153 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rhltable_init_noprof
- Explanation: rhltable_init_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000154 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sched_tick
- Explanation: sched_tick changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000156 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_audit_rule_init
- Explanation: security_audit_rule_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'field', 'type': 'u32_'}, {'name': 'op', 'type': 'u32_'}, {'name': 'rulestr', 'type': '*mut core::ffi::c_char'}, {'name': 'lsmrule', 'type': '*mut *mut core::ffi::c_void'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'field', 'type': 'u32_'}, {'name': 'op', 'type': 'u32_'}, {'name': 'rulestr', 'type': '*mut core::ffi::c_char'}, {'name': 'lsmrule', 'type': '*mut *mut core::ffi::c_void'}, {'name': 'gfp', 'type': 'gfp_t'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000157 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_copy_up_xattr
- Explanation: security_inode_copy_up_xattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'name', 'type': '*const core::ffi::c_char'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'src', 'type': '*mut dentry'}, {'name': 'name', 'type': '*const core::ffi::c_char'}], 'return_type': 'core::ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000162 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stable_page_flags
- Explanation: stable_page_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'page', 'type': '*mut page'}], 'return_type': 'u64_'}`
- New: `{'params': [{'name': 'page', 'type': '*const page'}], 'return_type': 'u64_'}`

### Rust Evidence

- Graph edges: `1`

## W-000174 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_bin_attr_simple_read
- Explanation: sysfs_bin_attr_simple_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000175 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: topology_update_hw_pressure
- Explanation: topology_update_hw_pressure changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000188 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_alloc_folio
- Explanation: vma_alloc_folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000189 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_alloc_folio_noprof
- Explanation: vma_alloc_folio_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000190 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_pgtable_walk_begin
- Explanation: vma_pgtable_walk_begin changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000191 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_pgtable_walk_end
- Explanation: vma_pgtable_walk_end changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000192 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_wants_writenotify
- Explanation: vma_wants_writenotify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'vm_page_prot', 'type': 'pgprot_t'}], 'return_type': 'core::ffi::c_int'}`
- New: `{'params': [{'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'vm_page_prot', 'type': 'pgprot_t'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000202 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmap
- Explanation: vmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000209 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xas_get_order
- Explanation: xas_get_order changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000404 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __realloc_size
- Explanation: __realloc_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['2', '3) void * __must_check krealloc_array(void *p, size_t new_n, size_t new_size, gfp_t flags'], 'return_type': 'static inline'}`
- New: `{'params': ['2', '3) void * __must_check krealloc_array_noprof(void *p, size_t new_n, size_t new_size, gfp_t flags'], 'return_type': 'static inline'}`

### Rust Evidence

- Graph edges: `1`

## W-000213 FieldDrift

- Risk: High
- Score: 10.6
- Symbol: bpf_fib_lookup
- Explanation: bpf_fib_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'family', 'type': '__u8'}, {'name': 'l4_protocol', 'type': '__u8'}, {'name': 'sport', 'type': '__be16'}, {'name': 'dport', 'type': '__be16'}, {'name': '__bindgen_anon_1', 'type': 'bpf_fib_lookup__bindgen_ty_1'}, {'name': 'ifindex', 'type': '__u32'}, {'name': '__bindgen_anon_2', 'type': 'bpf_fib_lookup__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'bpf_fib_lookup__bindgen_ty_3'}, {'name': '__bindgen_anon_4', 'type': 'bpf_fib_lookup__bindgen_ty_4'}, {'name': '__bindgen_anon_5', 'type': 'bpf_fib_lookup__bindgen_ty_5'}, {'name': 'smac', 'type': '[__u8; 6usize]'}, {'name': 'dmac', 'type': '[__u8; 6usize]'}]`
- New: `[{'name': 'family', 'type': '__u8'}, {'name': 'l4_protocol', 'type': '__u8'}, {'name': 'sport', 'type': '__be16'}, {'name': 'dport', 'type': '__be16'}, {'name': '__bindgen_anon_1', 'type': 'bpf_fib_lookup__bindgen_ty_1'}, {'name': 'ifindex', 'type': '__u32'}, {'name': '__bindgen_anon_2', 'type': 'bpf_fib_lookup__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'bpf_fib_lookup__bindgen_ty_3'}, {'name': '__bindgen_anon_4', 'type': 'bpf_fib_lookup__bindgen_ty_4'}, {'name': '__bindgen_anon_5', 'type': 'bpf_fib_lookup__bindgen_ty_5'}, {'name': '__bindgen_anon_6', 'type': 'bpf_fib_lookup__bindgen_ty_6'}]`

### Rust Evidence

- Graph edges: `10`

## W-000233 FieldDrift

- Risk: High
- Score: 10.4
- Symbol: task_struct
- Explanation: task_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'core::ffi::c_uint'}, {'name': 'saved_state', 'type': 'core::ffi::c_uint'}, {'name': 'stack', 'type': '*mut core::ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'ptrace', 'type': 'core::ffi::c_uint'}, {'name': 'on_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'core::ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'core::ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_cpu', 'type': 'core::ffi::c_int'}, {'name': 'on_rq', 'type': 'core::ffi::c_int'}, {'name': 'prio', 'type': 'core::ffi::c_int'}, {'name': 'static_prio', 'type': 'core::ffi::c_int'}, {'name': 'normal_prio', 'type': 'core::ffi::c_int'}, {'name': 'rt_priority', 'type': 'core::ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'dl_server', 'type': '*mut sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'core::ffi::c_uint'}, {'name': 'policy', 'type': 'core::ffi::c_uint'}, {'name': 'nr_cpus_allowed', 'type': 'core::ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut core::ffi::c_void'}, {'name': 'migration_disabled', 'type': 'core::ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'core::ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'core::ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'core::ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'rcu_tasks_exit_cpu', 'type': 'core::ffi::c_int'}, {'name': 'rcu_tasks_exit_list', 'type': 'list_head'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'faults_disabled_mapping', 'type': '*mut address_space'}, {'name': 'exit_state', 'type': 'core::ffi::c_int'}, {'name': 'exit_code', 'type': 'core::ffi::c_int'}, {'name': 'exit_signal', 'type': 'core::ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'core::ffi::c_int'}, {'name': 'jobctl', 'type': 'core::ffi::c_ulong'}, {'name': 'personality', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'core::ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'worker_private', 'type': '*mut core::ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[core::ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'core::ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'core::ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'core::ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'journal_info', 'type': '*mut core::ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'core::ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cpuset_slab_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'core::ffi::c_uint'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'core::ffi::c_short'}, {'name': 'il_weight', 'type': 'u8_'}, {'name': 'pref_node_fork', 'type': 'core::ffi::c_short'}, {'name': 'rseq', 'type': '*mut rseq'}, {'name': 'rseq_len', 'type': 'u32_'}, {'name': 'rseq_sig', 'type': 'u32_'}, {'name': 'rseq_event_mask', 'type': 'core::ffi::c_ulong'}, {'name': 'mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'last_mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'migrate_from_cpu', 'type': 'core::ffi::c_int'}, {'name': 'mm_cid_active', 'type': 'core::ffi::c_int'}, {'name': 'cid_work', 'type': 'callback_head'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'core::ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'core::ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'core::ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'core::ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'core::ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_vaddr', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'core::ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': '__bindgen_padding_1', 'type': '[u64; 7usize]'}, {'name': 'thread', 'type': 'thread_struct'}]`
- New: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'core::ffi::c_uint'}, {'name': 'saved_state', 'type': 'core::ffi::c_uint'}, {'name': 'stack', 'type': '*mut core::ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'ptrace', 'type': 'core::ffi::c_uint'}, {'name': 'on_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'core::ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'core::ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_cpu', 'type': 'core::ffi::c_int'}, {'name': 'on_rq', 'type': 'core::ffi::c_int'}, {'name': 'prio', 'type': 'core::ffi::c_int'}, {'name': 'static_prio', 'type': 'core::ffi::c_int'}, {'name': 'normal_prio', 'type': 'core::ffi::c_int'}, {'name': 'rt_priority', 'type': 'core::ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'dl_server', 'type': '*mut sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'core::ffi::c_uint'}, {'name': 'policy', 'type': 'core::ffi::c_uint'}, {'name': 'max_allowed_capacity', 'type': 'core::ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'core::ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut core::ffi::c_void'}, {'name': 'migration_disabled', 'type': 'core::ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'core::ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'core::ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'core::ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'rcu_tasks_exit_cpu', 'type': 'core::ffi::c_int'}, {'name': 'rcu_tasks_exit_list', 'type': 'list_head'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'faults_disabled_mapping', 'type': '*mut address_space'}, {'name': 'exit_state', 'type': 'core::ffi::c_int'}, {'name': 'exit_code', 'type': 'core::ffi::c_int'}, {'name': 'exit_signal', 'type': 'core::ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'core::ffi::c_int'}, {'name': 'jobctl', 'type': 'core::ffi::c_ulong'}, {'name': 'personality', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'core::ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'worker_private', 'type': '*mut core::ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[core::ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'core::ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'core::ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'core::ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'journal_info', 'type': '*mut core::ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'core::ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cpuset_slab_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'core::ffi::c_uint'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'core::ffi::c_short'}, {'name': 'il_weight', 'type': 'u8_'}, {'name': 'pref_node_fork', 'type': 'core::ffi::c_short'}, {'name': 'rseq', 'type': '*mut rseq'}, {'name': 'rseq_len', 'type': 'u32_'}, {'name': 'rseq_sig', 'type': 'u32_'}, {'name': 'rseq_event_mask', 'type': 'core::ffi::c_ulong'}, {'name': 'mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'last_mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'migrate_from_cpu', 'type': 'core::ffi::c_int'}, {'name': 'mm_cid_active', 'type': 'core::ffi::c_int'}, {'name': 'cid_work', 'type': 'callback_head'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'core::ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'core::ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'core::ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'core::ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'core::ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_vaddr', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'core::ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': '__bindgen_padding_1', 'type': '[u64; 6usize]'}, {'name': 'thread', 'type': 'thread_struct'}]`

### Rust Evidence

- Graph edges: `9`

## W-000216 FieldDrift

- Risk: High
- Score: 10.2
- Symbol: ctl_table
- Explanation: ctl_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'procname', 'type': '*const core::ffi::c_char'}, {'name': 'data', 'type': '*mut core::ffi::c_void'}, {'name': 'maxlen', 'type': 'core::ffi::c_int'}, {'name': 'mode', 'type': 'umode_t'}, {'name': 'type_', 'type': 'ctl_table__bindgen_ty_1'}, {'name': 'proc_handler', 'type': 'proc_handler'}, {'name': 'poll', 'type': '*mut ctl_table_poll'}, {'name': 'extra1', 'type': '*mut core::ffi::c_void'}, {'name': 'extra2', 'type': '*mut core::ffi::c_void'}]`
- New: `[{'name': 'procname', 'type': '*const core::ffi::c_char'}, {'name': 'data', 'type': '*mut core::ffi::c_void'}, {'name': 'maxlen', 'type': 'core::ffi::c_int'}, {'name': 'mode', 'type': 'umode_t'}, {'name': 'proc_handler', 'type': 'proc_handler'}, {'name': 'poll', 'type': '*mut ctl_table_poll'}, {'name': 'extra1', 'type': '*mut core::ffi::c_void'}, {'name': 'extra2', 'type': '*mut core::ffi::c_void'}]`

### Rust Evidence

- Graph edges: `8`

## W-000222 FieldDrift

- Risk: High
- Score: 10.0
- Symbol: kstat
- Explanation: kstat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'result_mask', 'type': 'u32_'}, {'name': 'mode', 'type': 'umode_t'}, {'name': 'nlink', 'type': 'core::ffi::c_uint'}, {'name': 'blksize', 'type': 'u32'}, {'name': 'attributes', 'type': 'u64_'}, {'name': 'attributes_mask', 'type': 'u64_'}, {'name': 'ino', 'type': 'u64_'}, {'name': 'dev', 'type': 'dev_t'}, {'name': 'rdev', 'type': 'dev_t'}, {'name': 'uid', 'type': 'kuid_t'}, {'name': 'gid', 'type': 'kgid_t'}, {'name': 'size', 'type': 'loff_t'}, {'name': 'atime', 'type': 'timespec64'}, {'name': 'mtime', 'type': 'timespec64'}, {'name': 'ctime', 'type': 'timespec64'}, {'name': 'btime', 'type': 'timespec64'}, {'name': 'blocks', 'type': 'u64_'}, {'name': 'mnt_id', 'type': 'u64_'}, {'name': 'dio_mem_align', 'type': 'u32_'}, {'name': 'dio_offset_align', 'type': 'u32_'}, {'name': 'change_cookie', 'type': 'u64_'}]`
- New: `[{'name': 'result_mask', 'type': 'u32_'}, {'name': 'mode', 'type': 'umode_t'}, {'name': 'nlink', 'type': 'core::ffi::c_uint'}, {'name': 'blksize', 'type': 'u32'}, {'name': 'attributes', 'type': 'u64_'}, {'name': 'attributes_mask', 'type': 'u64_'}, {'name': 'ino', 'type': 'u64_'}, {'name': 'dev', 'type': 'dev_t'}, {'name': 'rdev', 'type': 'dev_t'}, {'name': 'uid', 'type': 'kuid_t'}, {'name': 'gid', 'type': 'kgid_t'}, {'name': 'size', 'type': 'loff_t'}, {'name': 'atime', 'type': 'timespec64'}, {'name': 'mtime', 'type': 'timespec64'}, {'name': 'ctime', 'type': 'timespec64'}, {'name': 'btime', 'type': 'timespec64'}, {'name': 'blocks', 'type': 'u64_'}, {'name': 'mnt_id', 'type': 'u64_'}, {'name': 'dio_mem_align', 'type': 'u32_'}, {'name': 'dio_offset_align', 'type': 'u32_'}, {'name': 'change_cookie', 'type': 'u64_'}, {'name': 'subvol', 'type': 'u64_'}]`

### Rust Evidence

- Graph edges: `7`

## W-000234 FieldDrift

- Risk: Medium
- Score: 9.8
- Symbol: ubuf_info
- Explanation: ubuf_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'callback', 'type': '::core::option::Option<'}, {'name': 'refcnt', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'u8_'}]`
- New: `[{'name': 'ops', 'type': '*const ubuf_info_ops'}, {'name': 'refcnt', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'u8_'}]`

### Rust Evidence

- Graph edges: `6`

## W-000001 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __absent_pages_in_range
- Explanation: __absent_pages_in_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000003 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __alloc_pages_bulk
- Explanation: __alloc_pages_bulk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000005 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __alloc_percpu
- Explanation: __alloc_percpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000006 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __alloc_percpu_gfp
- Explanation: __alloc_percpu_gfp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000007 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __alloc_reserved_percpu
- Explanation: __alloc_reserved_percpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000016 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __get_free_pages
- Explanation: __get_free_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000018 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __get_vm_area_caller
- Explanation: __get_vm_area_caller changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000019 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __iowrite32_copy
- Explanation: __iowrite32_copy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000023 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __kmalloc_node_track_caller
- Explanation: __kmalloc_node_track_caller changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000025 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __mmu_notifier_change_pte
- Explanation: __mmu_notifier_change_pte changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000026 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __napi_alloc_skb
- Explanation: __napi_alloc_skb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000028 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __skb_free_datagram_locked
- Explanation: __skb_free_datagram_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000029 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __stack_depot_get_stack_record
- Explanation: __stack_depot_get_stack_record changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000030 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __vcalloc
- Explanation: __vcalloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000032 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __vmalloc_array
- Explanation: __vmalloc_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000033 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __vmalloc_node
- Explanation: __vmalloc_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000034 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __vmalloc_node_range
- Explanation: __vmalloc_node_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000051 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: arch_sync_kernel_mappings
- Explanation: arch_sync_kernel_mappings changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000052 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: arch_unprotect_bpf_trampoline
- Explanation: arch_unprotect_bpf_trampoline changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000063 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: destroy_large_folio
- Explanation: destroy_large_folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000066 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: devm_device_add_groups
- Explanation: devm_device_add_groups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000071 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: dma_need_sync
- Explanation: dma_need_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000073 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: dma_sync_sg_for_cpu
- Explanation: dma_sync_sg_for_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000074 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: dma_sync_sg_for_device
- Explanation: dma_sync_sg_for_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000075 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: dma_sync_single_for_cpu
- Explanation: dma_sync_single_for_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000076 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: dma_sync_single_for_device
- Explanation: dma_sync_single_for_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000081 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: find_vm_area
- Explanation: find_vm_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000082 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: find_vmap_area
- Explanation: find_vmap_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000085 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: folio_total_mapcount
- Explanation: folio_total_mapcount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000086 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: follow_pfn
- Explanation: follow_pfn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000087 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: follow_phys
- Explanation: follow_phys changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000089 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: free_vm_area
- Explanation: free_vm_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000091 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: get_unmapped_area
- Explanation: get_unmapped_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000092 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: get_vm_area
- Explanation: get_vm_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000093 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: get_vm_area_caller
- Explanation: get_vm_area_caller changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000097 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ia32_pick_mmap_layout
- Explanation: ia32_pick_mmap_layout changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000098 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ia32_setup_arg_pages
- Explanation: ia32_setup_arg_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000100 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: is_file_shm_hugepages
- Explanation: is_file_shm_hugepages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000130 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: memblock_find_dma_reserve
- Explanation: memblock_find_dma_reserve changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000134 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: msg_zerocopy_callback
- Explanation: msg_zerocopy_callback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000136 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: napi_pp_put_page
- Explanation: napi_pp_put_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000141 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: pcpu_free_vm_areas
- Explanation: pcpu_free_vm_areas changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000142 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: pcpu_get_vm_areas
- Explanation: pcpu_get_vm_areas changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000143 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: pool_index_plus_1
- Explanation: pool_index_plus_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000144 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: register_vmap_purge_notifier
- Explanation: register_vmap_purge_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000146 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: remap_vmalloc_range
- Explanation: remap_vmalloc_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000147 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: remap_vmalloc_range_partial
- Explanation: remap_vmalloc_range_partial changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000148 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: remove_vm_area
- Explanation: remove_vm_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000155 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: scheduler_tick
- Explanation: scheduler_tick changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000158 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: seq_puts
- Explanation: seq_puts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000159 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: set_dma_reserve
- Explanation: set_dma_reserve changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000160 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: shake_page
- Explanation: shake_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000163 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: stack_depot_early_init
- Explanation: stack_depot_early_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000164 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: stack_depot_fetch
- Explanation: stack_depot_fetch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000165 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: stack_depot_get_extra_bits
- Explanation: stack_depot_get_extra_bits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000166 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: stack_depot_init
- Explanation: stack_depot_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000167 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: stack_depot_print
- Explanation: stack_depot_print changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000168 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: stack_depot_put
- Explanation: stack_depot_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000169 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: stack_depot_request_early_init
- Explanation: stack_depot_request_early_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000170 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: stack_depot_save
- Explanation: stack_depot_save changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000171 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: stack_depot_save_flags
- Explanation: stack_depot_save_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000172 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: stack_depot_set_extra_bits
- Explanation: stack_depot_set_extra_bits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000173 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: stack_depot_snprint
- Explanation: stack_depot_snprint changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000176 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: topology_update_thermal_pressure
- Explanation: topology_update_thermal_pressure changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000177 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: unregister_vmap_purge_notifier
- Explanation: unregister_vmap_purge_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000178 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vcalloc
- Explanation: vcalloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000179 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vfree
- Explanation: vfree changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000180 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vfree_atomic
- Explanation: vfree_atomic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000181 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vm_area_add_early
- Explanation: vm_area_add_early changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000182 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vm_area_map_pages
- Explanation: vm_area_map_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000183 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vm_area_register_early
- Explanation: vm_area_register_early changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000184 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vm_area_unmap_pages
- Explanation: vm_area_unmap_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000185 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vm_map_ram
- Explanation: vm_map_ram changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000186 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vm_unmap_aliases
- Explanation: vm_unmap_aliases changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000187 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vm_unmap_ram
- Explanation: vm_unmap_ram changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000194 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vmalloc_32
- Explanation: vmalloc_32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000195 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vmalloc_32_user
- Explanation: vmalloc_32_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000196 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vmalloc_array
- Explanation: vmalloc_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000197 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vmalloc_dump_obj
- Explanation: vmalloc_dump_obj changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000198 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vmalloc_huge
- Explanation: vmalloc_huge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000199 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vmalloc_node
- Explanation: vmalloc_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000200 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vmalloc_nr_pages
- Explanation: vmalloc_nr_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000201 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vmalloc_user
- Explanation: vmalloc_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000203 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vmap_pfn
- Explanation: vmap_pfn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000204 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vread_iter
- Explanation: vread_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000205 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vunmap
- Explanation: vunmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000206 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vunmap_range
- Explanation: vunmap_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000207 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vzalloc
- Explanation: vzalloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000208 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vzalloc_node
- Explanation: vzalloc_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000399 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __fls
- Explanation: __fls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned long word'], 'return_type': 'static __always_inline unsigned long'}`
- New: `{'params': ['unsigned long word'], 'return_type': 'static __always_inline unsigned int'}`

### Rust Evidence

- Graph edges: `0`

## W-000400 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __raw_readb
- Explanation: __raw_readb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const volatile void __iomem *addr'], 'return_type': 'u8'}`
- New: `{'params': ['addr'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-000401 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __raw_readl
- Explanation: __raw_readl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const volatile void __iomem *addr'], 'return_type': 'u32'}`
- New: `{'params': ['addr'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-000402 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __raw_readq
- Explanation: __raw_readq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const volatile void __iomem *addr'], 'return_type': 'u64'}`
- New: `{'params': ['addr'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-000403 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __raw_readw
- Explanation: __raw_readw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const volatile void __iomem *addr'], 'return_type': 'u16'}`
- New: `{'params': ['addr'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-000405 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: acpi_initialize_hp_context
- Explanation: acpi_initialize_hp_context changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct acpi_device *adev', 'struct acpi_hotplug_context *hp', 'int (*notify)(struct acpi_device *, u32)', 'void (*uevent)(struct acpi_device *, u32)'], 'return_type': 'void'}`
- New: `{'params': ['struct acpi_device *adev', 'struct acpi_hotplug_context *hp', 'acpi_hp_notify notify', 'acpi_hp_uevent uevent'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000406 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: acpi_os_acquire_object
- Explanation: acpi_os_acquire_object changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['acpi_cache_t * cache'], 'return_type': 'static inline void *'}`
- New: `{'params': ['acpi_cache_t * cache'], 'return_type': 'void *'}`

### Rust Evidence

- Graph edges: `0`

## W-000407 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: acpi_os_allocate
- Explanation: acpi_os_allocate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['acpi_size size'], 'return_type': 'static inline void *'}`
- New: `{'params': ['acpi_size size'], 'return_type': 'void *'}`

### Rust Evidence

- Graph edges: `0`

## W-000408 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: acpi_os_allocate_zeroed
- Explanation: acpi_os_allocate_zeroed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['acpi_size size'], 'return_type': 'static inline void *'}`
- New: `{'params': ['acpi_size size'], 'return_type': 'void *'}`

### Rust Evidence

- Graph edges: `0`

## W-000409 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: af_alg_accept
- Explanation: af_alg_accept changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct sock *sk', 'struct socket *newsock', 'bool kern'], 'return_type': 'int'}`
- New: `{'params': ['struct sock *sk', 'struct socket *newsock', 'struct proto_accept_arg *arg'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000410 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: devm_drm_dp_hpd_bridge_add
- Explanation: devm_drm_dp_hpd_bridge_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct auxiliary_device *adev'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct device *dev', 'struct auxiliary_device *adev'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `0`

## W-000411 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_buddy_free_list
- Explanation: drm_buddy_free_list changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_buddy *mm', 'struct list_head *objects'], 'return_type': 'void'}`
- New: `{'params': ['struct drm_buddy *mm', 'struct list_head *objects', 'unsigned int flags'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000412 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_dp_add_payload_part2
- Explanation: drm_dp_add_payload_part2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_dp_mst_topology_mgr *mgr', 'struct drm_atomic_state *state', 'struct drm_dp_mst_atomic_payload *payload'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_dp_mst_topology_mgr *mgr', 'struct drm_dp_mst_atomic_payload *payload'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000413 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_dp_read_mst_cap
- Explanation: drm_dp_read_mst_cap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_dp_aux *aux', 'const u8 dpcd[DP_RECEIVER_CAP_SIZE]'], 'return_type': 'bool'}`
- New: `{'params': ['struct drm_dp_aux *aux', 'const u8 dpcd[DP_RECEIVER_CAP_SIZE]'], 'return_type': 'enum drm_dp_mst_mode'}`

### Rust Evidence

- Graph edges: `0`

## W-000414 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_edid_get_panel_id
- Explanation: drm_edid_get_panel_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct i2c_adapter *adapter'], 'return_type': 'u32'}`
- New: `{'params': ['const struct drm_edid *drm_edid'], 'return_type': 'u32'}`

### Rust Evidence

- Graph edges: `0`

## W-000415 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_gem_shmem_pin
- Explanation: drm_gem_shmem_pin changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['shmem'], 'return_type': 'return'}`
- New: `{'params': ['struct drm_gem_shmem_object *shmem'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000416 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ecc_gen_privkey
- Explanation: ecc_gen_privkey changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned int curve_id', 'unsigned int ndigits', 'u64 *privkey'], 'return_type': 'int'}`
- New: `{'params': ['unsigned int curve_id', 'unsigned int ndigits', 'u64 *private_key'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000417 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: generic___ffs
- Explanation: generic___ffs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned long word'], 'return_type': 'static __always_inline unsigned long'}`
- New: `{'params': ['unsigned long word'], 'return_type': 'static __always_inline unsigned int'}`

### Rust Evidence

- Graph edges: `0`

## W-000418 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: generic___fls
- Explanation: generic___fls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned long word'], 'return_type': 'static __always_inline unsigned long'}`
- New: `{'params': ['unsigned long word'], 'return_type': 'static __always_inline unsigned int'}`

### Rust Evidence

- Graph edges: `0`

## W-000419 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mipi_dsi_compression_mode
- Explanation: mipi_dsi_compression_mode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mipi_dsi_device *dsi', 'bool enable'], 'return_type': 'ssize_t'}`
- New: `{'params': ['struct mipi_dsi_device *dsi', 'bool enable'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000420 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mipi_dsi_picture_parameter_set
- Explanation: mipi_dsi_picture_parameter_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mipi_dsi_device *dsi', 'const struct drm_dsc_picture_parameter_set *pps'], 'return_type': 'ssize_t'}`
- New: `{'params': ['struct mipi_dsi_device *dsi', 'const struct drm_dsc_picture_parameter_set *pps'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-000421 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sys_mmap
- Explanation: sys_mmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['unsigned long addr', 'unsigned long len', 'unsigned long prot', 'unsigned long flags', 'unsigned long fd', 'off_t pgoff'], 'return_type': 'asmlinkage long'}`
- New: `{'params': ['unsigned long addr', 'unsigned long len', 'unsigned long prot', 'unsigned long flags', 'unsigned long fd', 'unsigned long off'], 'return_type': 'asmlinkage long'}`

### Rust Evidence

- Graph edges: `0`

## W-000422 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ttm_resource_compatible
- Explanation: ttm_resource_compatible changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct ttm_resource *res', 'struct ttm_placement *placement'], 'return_type': 'bool'}`
- New: `{'params': ['struct ttm_resource *res', 'struct ttm_placement *placement', 'bool evicting'], 'return_type': 'bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000217 FieldDrift

- Risk: Medium
- Score: 9.4
- Symbol: ctl_table_header
- Explanation: ctl_table_header changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'ctl_table_header__bindgen_ty_1'}, {'name': 'unregistering', 'type': '*mut completion'}, {'name': 'ctl_table_arg', 'type': '*mut ctl_table'}, {'name': 'root', 'type': '*mut ctl_table_root'}, {'name': 'set', 'type': '*mut ctl_table_set'}, {'name': 'parent', 'type': '*mut ctl_dir'}, {'name': 'node', 'type': '*mut ctl_node'}, {'name': 'inodes', 'type': 'hlist_head'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'ctl_table_header__bindgen_ty_1'}, {'name': 'unregistering', 'type': '*mut completion'}, {'name': 'ctl_table_arg', 'type': '*const ctl_table'}, {'name': 'root', 'type': '*mut ctl_table_root'}, {'name': 'set', 'type': '*mut ctl_table_set'}, {'name': 'parent', 'type': '*mut ctl_dir'}, {'name': 'node', 'type': '*mut ctl_node'}, {'name': 'inodes', 'type': 'hlist_head'}, {'name': 'type_', 'type': 'ctl_table_header__bindgen_ty_2'}]`

### Rust Evidence

- Graph edges: `4`

## W-000224 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: kunit_try_catch
- Explanation: kunit_try_catch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bindgen_opaque_blob', 'type': '[u64; 6usize]'}]`
- New: `[{'name': '_bindgen_opaque_blob', 'type': '[u64; 5usize]'}]`

### Rust Evidence

- Graph edges: `3`

## W-000235 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: vm_area_struct
- Explanation: vm_area_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'vm_area_struct__bindgen_ty_1'}, {'name': 'vm_mm', 'type': '*mut mm_struct'}, {'name': 'vm_page_prot', 'type': 'pgprot_t'}, {'name': '__bindgen_anon_2', 'type': 'vm_area_struct__bindgen_ty_2'}, {'name': 'vm_lock_seq', 'type': 'core::ffi::c_int'}, {'name': 'vm_lock', 'type': '*mut vma_lock'}, {'name': 'detached', 'type': 'bool_'}, {'name': 'shared', 'type': 'vm_area_struct__bindgen_ty_3'}, {'name': 'anon_vma_chain', 'type': 'list_head'}, {'name': 'anon_vma', 'type': '*mut anon_vma'}, {'name': 'vm_ops', 'type': '*const vm_operations_struct'}, {'name': 'vm_pgoff', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_file', 'type': '*mut file'}, {'name': 'vm_private_data', 'type': '*mut core::ffi::c_void'}, {'name': 'swap_readahead_info', 'type': 'atomic_long_t'}, {'name': 'vm_policy', 'type': '*mut mempolicy'}, {'name': 'vm_userfaultfd_ctx', 'type': 'vm_userfaultfd_ctx'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'vm_area_struct__bindgen_ty_1'}, {'name': 'vm_mm', 'type': '*mut mm_struct'}, {'name': 'vm_page_prot', 'type': 'pgprot_t'}, {'name': '__bindgen_anon_2', 'type': 'vm_area_struct__bindgen_ty_2'}, {'name': 'detached', 'type': 'bool_'}, {'name': 'vm_lock_seq', 'type': 'core::ffi::c_int'}, {'name': 'vm_lock', 'type': '*mut vma_lock'}, {'name': 'shared', 'type': 'vm_area_struct__bindgen_ty_3'}, {'name': 'anon_vma_chain', 'type': 'list_head'}, {'name': 'anon_vma', 'type': '*mut anon_vma'}, {'name': 'vm_ops', 'type': '*const vm_operations_struct'}, {'name': 'vm_pgoff', 'type': 'core::ffi::c_ulong'}, {'name': 'vm_file', 'type': '*mut file'}, {'name': 'vm_private_data', 'type': '*mut core::ffi::c_void'}, {'name': 'swap_readahead_info', 'type': 'atomic_long_t'}, {'name': 'vm_policy', 'type': '*mut mempolicy'}, {'name': 'vm_userfaultfd_ctx', 'type': 'vm_userfaultfd_ctx'}]`

### Rust Evidence

- Graph edges: `3`

## W-000215 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: cpuinfo_x86
- Explanation: cpuinfo_x86 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'x86', 'type': '__u8'}, {'name': 'x86_vendor', 'type': '__u8'}, {'name': 'x86_model', 'type': '__u8'}, {'name': 'x86_stepping', 'type': '__u8'}, {'name': 'x86_tlbsize', 'type': 'core::ffi::c_int'}, {'name': 'vmx_capability', 'type': '[__u32; 5usize]'}, {'name': 'x86_virt_bits', 'type': '__u8'}, {'name': 'x86_phys_bits', 'type': '__u8'}, {'name': 'extended_cpuid_level', 'type': '__u32'}, {'name': 'cpuid_level', 'type': 'core::ffi::c_int'}, {'name': '__bindgen_anon_1', 'type': 'cpuinfo_x86__bindgen_ty_1'}, {'name': 'x86_vendor_id', 'type': '[core::ffi::c_char; 16usize]'}, {'name': 'x86_model_id', 'type': '[core::ffi::c_char; 64usize]'}, {'name': 'topo', 'type': 'cpuinfo_topology'}, {'name': 'x86_cache_size', 'type': 'core::ffi::c_uint'}, {'name': 'x86_cache_alignment', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_max_rmid', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_occ_scale', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_mbm_width_offset', 'type': 'core::ffi::c_int'}, {'name': 'x86_power', 'type': 'core::ffi::c_int'}, {'name': 'loops_per_jiffy', 'type': 'core::ffi::c_ulong'}, {'name': 'ppin', 'type': 'u64_'}, {'name': 'x86_clflush_size', 'type': 'u16_'}, {'name': 'booted_cores', 'type': 'u16_'}, {'name': 'cpu_index', 'type': 'u16_'}, {'name': 'smt_active', 'type': 'bool_'}, {'name': 'microcode', 'type': 'u32_'}, {'name': 'x86_cache_bits', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': 'u16'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'cpuinfo_x86__bindgen_ty_1'}, {'name': 'x86_stepping', 'type': '__u8'}, {'name': 'x86_tlbsize', 'type': 'core::ffi::c_int'}, {'name': 'vmx_capability', 'type': '[__u32; 5usize]'}, {'name': 'x86_virt_bits', 'type': '__u8'}, {'name': 'x86_phys_bits', 'type': '__u8'}, {'name': 'extended_cpuid_level', 'type': '__u32'}, {'name': 'cpuid_level', 'type': 'core::ffi::c_int'}, {'name': '__bindgen_anon_2', 'type': 'cpuinfo_x86__bindgen_ty_2'}, {'name': 'x86_vendor_id', 'type': '[core::ffi::c_char; 16usize]'}, {'name': 'x86_model_id', 'type': '[core::ffi::c_char; 64usize]'}, {'name': 'topo', 'type': 'cpuinfo_topology'}, {'name': 'x86_cache_size', 'type': 'core::ffi::c_uint'}, {'name': 'x86_cache_alignment', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_max_rmid', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_occ_scale', 'type': 'core::ffi::c_int'}, {'name': 'x86_cache_mbm_width_offset', 'type': 'core::ffi::c_int'}, {'name': 'x86_power', 'type': 'core::ffi::c_int'}, {'name': 'loops_per_jiffy', 'type': 'core::ffi::c_ulong'}, {'name': 'ppin', 'type': 'u64_'}, {'name': 'x86_clflush_size', 'type': 'u16_'}, {'name': 'booted_cores', 'type': 'u16_'}, {'name': 'cpu_index', 'type': 'u16_'}, {'name': 'smt_active', 'type': 'bool_'}, {'name': 'microcode', 'type': 'u32_'}, {'name': 'x86_cache_bits', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': 'u16'}]`

### Rust Evidence

- Graph edges: `2`

## W-000226 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: mm_struct__bindgen_ty_1
- Explanation: mm_struct__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'mm_struct__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mm_mt', 'type': 'maple_tree'}, {'name': 'get_unmapped_area', 'type': '::core::option::Option<'}, {'name': 'mmap_base', 'type': 'core::ffi::c_ulong'}, {'name': 'mmap_legacy_base', 'type': 'core::ffi::c_ulong'}, {'name': 'mmap_compat_base', 'type': 'core::ffi::c_ulong'}, {'name': 'mmap_compat_legacy_base', 'type': 'core::ffi::c_ulong'}, {'name': 'task_size', 'type': 'core::ffi::c_ulong'}, {'name': 'pgd', 'type': '*mut pgd_t'}, {'name': 'membarrier_state', 'type': 'atomic_t'}, {'name': 'mm_users', 'type': 'atomic_t'}, {'name': 'pcpu_cid', 'type': '*mut mm_cid'}, {'name': 'mm_cid_next_scan', 'type': 'core::ffi::c_ulong'}, {'name': 'pgtables_bytes', 'type': 'atomic_long_t'}, {'name': 'map_count', 'type': 'core::ffi::c_int'}, {'name': 'page_table_lock', 'type': 'spinlock_t'}, {'name': 'mmap_lock', 'type': 'rw_semaphore'}, {'name': 'mmlist', 'type': 'list_head'}, {'name': 'mm_lock_seq', 'type': 'core::ffi::c_int'}, {'name': 'hiwater_rss', 'type': 'core::ffi::c_ulong'}, {'name': 'hiwater_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'total_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'locked_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'pinned_vm', 'type': 'atomic64_t'}, {'name': 'data_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'exec_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'stack_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'def_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'write_protect_seq', 'type': 'seqcount_t'}, {'name': 'arg_lock', 'type': 'spinlock_t'}, {'name': 'start_code', 'type': 'core::ffi::c_ulong'}, {'name': 'end_code', 'type': 'core::ffi::c_ulong'}, {'name': 'start_data', 'type': 'core::ffi::c_ulong'}, {'name': 'end_data', 'type': 'core::ffi::c_ulong'}, {'name': 'start_brk', 'type': 'core::ffi::c_ulong'}, {'name': 'brk', 'type': 'core::ffi::c_ulong'}, {'name': 'start_stack', 'type': 'core::ffi::c_ulong'}, {'name': 'arg_start', 'type': 'core::ffi::c_ulong'}, {'name': 'arg_end', 'type': 'core::ffi::c_ulong'}, {'name': 'env_start', 'type': 'core::ffi::c_ulong'}, {'name': 'env_end', 'type': 'core::ffi::c_ulong'}, {'name': 'saved_auxv', 'type': '[core::ffi::c_ulong; 52usize]'}, {'name': 'rss_stat', 'type': '[percpu_counter; 4usize]'}, {'name': 'binfmt', 'type': '*mut linux_binfmt'}, {'name': 'context', 'type': 'mm_context_t'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'ioctx_lock', 'type': 'spinlock_t'}, {'name': 'ioctx_table', 'type': '*mut kioctx_table'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'exe_file', 'type': '*mut file'}, {'name': 'notifier_subscriptions', 'type': '*mut mmu_notifier_subscriptions'}, {'name': 'tlb_flush_pending', 'type': 'atomic_t'}, {'name': 'tlb_flush_batched', 'type': 'atomic_t'}, {'name': 'uprobes_state', 'type': 'uprobes_state'}, {'name': 'hugetlb_usage', 'type': 'atomic_long_t'}, {'name': 'async_put_work', 'type': 'work_struct'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'mm_struct__bindgen_ty_1__bindgen_ty_1'}, {'name': 'mm_mt', 'type': 'maple_tree'}, {'name': 'mmap_base', 'type': 'core::ffi::c_ulong'}, {'name': 'mmap_legacy_base', 'type': 'core::ffi::c_ulong'}, {'name': 'mmap_compat_base', 'type': 'core::ffi::c_ulong'}, {'name': 'mmap_compat_legacy_base', 'type': 'core::ffi::c_ulong'}, {'name': 'task_size', 'type': 'core::ffi::c_ulong'}, {'name': 'pgd', 'type': '*mut pgd_t'}, {'name': 'membarrier_state', 'type': 'atomic_t'}, {'name': 'mm_users', 'type': 'atomic_t'}, {'name': 'pcpu_cid', 'type': '*mut mm_cid'}, {'name': 'mm_cid_next_scan', 'type': 'core::ffi::c_ulong'}, {'name': 'pgtables_bytes', 'type': 'atomic_long_t'}, {'name': 'map_count', 'type': 'core::ffi::c_int'}, {'name': 'page_table_lock', 'type': 'spinlock_t'}, {'name': 'mmap_lock', 'type': 'rw_semaphore'}, {'name': 'mmlist', 'type': 'list_head'}, {'name': 'mm_lock_seq', 'type': 'core::ffi::c_int'}, {'name': 'hiwater_rss', 'type': 'core::ffi::c_ulong'}, {'name': 'hiwater_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'total_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'locked_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'pinned_vm', 'type': 'atomic64_t'}, {'name': 'data_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'exec_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'stack_vm', 'type': 'core::ffi::c_ulong'}, {'name': 'def_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'write_protect_seq', 'type': 'seqcount_t'}, {'name': 'arg_lock', 'type': 'spinlock_t'}, {'name': 'start_code', 'type': 'core::ffi::c_ulong'}, {'name': 'end_code', 'type': 'core::ffi::c_ulong'}, {'name': 'start_data', 'type': 'core::ffi::c_ulong'}, {'name': 'end_data', 'type': 'core::ffi::c_ulong'}, {'name': 'start_brk', 'type': 'core::ffi::c_ulong'}, {'name': 'brk', 'type': 'core::ffi::c_ulong'}, {'name': 'start_stack', 'type': 'core::ffi::c_ulong'}, {'name': 'arg_start', 'type': 'core::ffi::c_ulong'}, {'name': 'arg_end', 'type': 'core::ffi::c_ulong'}, {'name': 'env_start', 'type': 'core::ffi::c_ulong'}, {'name': 'env_end', 'type': 'core::ffi::c_ulong'}, {'name': 'saved_auxv', 'type': '[core::ffi::c_ulong; 52usize]'}, {'name': 'rss_stat', 'type': '[percpu_counter; 4usize]'}, {'name': 'binfmt', 'type': '*mut linux_binfmt'}, {'name': 'context', 'type': 'mm_context_t'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'ioctx_lock', 'type': 'spinlock_t'}, {'name': 'ioctx_table', 'type': '*mut kioctx_table'}, {'name': 'user_ns', 'type': '*mut user_namespace'}, {'name': 'exe_file', 'type': '*mut file'}, {'name': 'notifier_subscriptions', 'type': '*mut mmu_notifier_subscriptions'}, {'name': 'tlb_flush_pending', 'type': 'atomic_t'}, {'name': 'tlb_flush_batched', 'type': 'atomic_t'}, {'name': 'uprobes_state', 'type': 'uprobes_state'}, {'name': 'hugetlb_usage', 'type': 'atomic_long_t'}, {'name': 'async_put_work', 'type': 'work_struct'}, {'name': 'iommu_mm', 'type': '*mut iommu_mm_data'}]`

### Rust Evidence

- Graph edges: `2`

## W-000211 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: block_device
- Explanation: block_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'bd_start_sect', 'type': 'sector_t'}, {'name': 'bd_nr_sectors', 'type': 'sector_t'}, {'name': 'bd_disk', 'type': '*mut gendisk'}, {'name': 'bd_queue', 'type': '*mut request_queue'}, {'name': 'bd_stats', 'type': '*mut disk_stats'}, {'name': 'bd_stamp', 'type': 'core::ffi::c_ulong'}, {'name': 'bd_read_only', 'type': 'bool_'}, {'name': 'bd_partno', 'type': 'u8_'}, {'name': 'bd_write_holder', 'type': 'bool_'}, {'name': 'bd_has_submit_bio', 'type': 'bool_'}, {'name': 'bd_dev', 'type': 'dev_t'}, {'name': 'bd_inode', 'type': '*mut inode'}, {'name': 'bd_openers', 'type': 'atomic_t'}, {'name': 'bd_size_lock', 'type': 'spinlock_t'}, {'name': 'bd_claiming', 'type': '*mut core::ffi::c_void'}, {'name': 'bd_holder', 'type': '*mut core::ffi::c_void'}, {'name': 'bd_holder_ops', 'type': '*mut blk_holder_ops'}, {'name': 'bd_holder_lock', 'type': 'mutex'}, {'name': 'bd_holders', 'type': 'core::ffi::c_int'}, {'name': 'bd_holder_dir', 'type': '*mut kobject'}, {'name': 'bd_fsfreeze_count', 'type': 'atomic_t'}, {'name': 'bd_fsfreeze_mutex', 'type': 'mutex'}, {'name': 'bd_meta_info', 'type': '*mut partition_meta_info'}, {'name': 'bd_ro_warned', 'type': 'bool_'}, {'name': 'bd_writers', 'type': 'core::ffi::c_int'}, {'name': 'bd_device', 'type': 'device'}]`
- New: `[{'name': 'bd_start_sect', 'type': 'sector_t'}, {'name': 'bd_nr_sectors', 'type': 'sector_t'}, {'name': 'bd_disk', 'type': '*mut gendisk'}, {'name': 'bd_queue', 'type': '*mut request_queue'}, {'name': 'bd_stats', 'type': '*mut disk_stats'}, {'name': 'bd_stamp', 'type': 'core::ffi::c_ulong'}, {'name': '__bd_flags', 'type': 'atomic_t'}, {'name': 'bd_dev', 'type': 'dev_t'}, {'name': 'bd_mapping', 'type': '*mut address_space'}, {'name': 'bd_openers', 'type': 'atomic_t'}, {'name': 'bd_size_lock', 'type': 'spinlock_t'}, {'name': 'bd_claiming', 'type': '*mut core::ffi::c_void'}, {'name': 'bd_holder', 'type': '*mut core::ffi::c_void'}, {'name': 'bd_holder_ops', 'type': '*mut blk_holder_ops'}, {'name': 'bd_holder_lock', 'type': 'mutex'}, {'name': 'bd_holders', 'type': 'core::ffi::c_int'}, {'name': 'bd_holder_dir', 'type': '*mut kobject'}, {'name': 'bd_fsfreeze_count', 'type': 'atomic_t'}, {'name': 'bd_fsfreeze_mutex', 'type': 'mutex'}, {'name': 'bd_meta_info', 'type': '*mut partition_meta_info'}, {'name': 'bd_writers', 'type': 'core::ffi::c_int'}, {'name': 'bd_device', 'type': 'device'}]`

### Rust Evidence

- Graph edges: `1`

## W-000212 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bpf_attr__bindgen_ty_11
- Explanation: bpf_attr__bindgen_ty_11 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'name', 'type': '__u64'}, {'name': 'prog_fd', 'type': '__u32'}]`
- New: `[{'name': 'name', 'type': '__u64'}, {'name': 'prog_fd', 'type': '__u32'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 4usize]>'}, {'name': 'cookie', 'type': '__u64'}]`

### Rust Evidence

- Graph edges: `1`

## W-000214 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: btf_record
- Explanation: btf_record changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'cnt', 'type': 'u32_'}, {'name': 'field_mask', 'type': 'u32_'}, {'name': 'spin_lock_off', 'type': 'core::ffi::c_int'}, {'name': 'timer_off', 'type': 'core::ffi::c_int'}, {'name': 'refcount_off', 'type': 'core::ffi::c_int'}, {'name': 'fields', 'type': '__IncompleteArrayField<btf_field>'}]`
- New: `[{'name': 'cnt', 'type': 'u32_'}, {'name': 'field_mask', 'type': 'u32_'}, {'name': 'spin_lock_off', 'type': 'core::ffi::c_int'}, {'name': 'timer_off', 'type': 'core::ffi::c_int'}, {'name': 'wq_off', 'type': 'core::ffi::c_int'}, {'name': 'refcount_off', 'type': 'core::ffi::c_int'}, {'name': 'fields', 'type': '__IncompleteArrayField<btf_field>'}]`

### Rust Evidence

- Graph edges: `1`

## W-000218 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: ethtool_ops
- Explanation: ethtool_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'supported_coalesce_params', 'type': 'u32_'}, {'name': 'supported_ring_params', 'type': 'u32_'}, {'name': 'get_drvinfo', 'type': '::core::option::Option<'}, {'name': 'get_regs', 'type': '::core::option::Option<'}, {'name': 'get_wol', 'type': '::core::option::Option<'}, {'name': 'set_wol', 'type': '::core::option::Option<'}, {'name': 'get_msglevel', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'get_link', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'get_link_ext_state', 'type': '::core::option::Option<'}, {'name': 'get_link_ext_stats', 'type': '::core::option::Option<'}, {'name': 'get_eeprom', 'type': '::core::option::Option<'}, {'name': 'set_eeprom', 'type': '::core::option::Option<'}, {'name': 'get_coalesce', 'type': '::core::option::Option<'}, {'name': 'set_coalesce', 'type': '::core::option::Option<'}, {'name': 'get_ringparam', 'type': '::core::option::Option<'}, {'name': 'set_ringparam', 'type': '::core::option::Option<'}, {'name': 'get_pause_stats', 'type': '::core::option::Option<'}, {'name': 'get_pauseparam', 'type': '::core::option::Option<'}, {'name': 'set_pauseparam', 'type': '::core::option::Option<'}, {'name': 'self_test', 'type': '::core::option::Option<'}, {'name': 'get_strings', 'type': '::core::option::Option<'}, {'name': 'set_phys_id', 'type': '::core::option::Option<'}, {'name': 'get_ethtool_stats', 'type': '::core::option::Option<'}, {'name': 'complete', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device)>'}, {'name': 'get_priv_flags', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'set_priv_flags', 'type': '::core::option::Option<'}, {'name': 'get_sset_count', 'type': '::core::option::Option<'}, {'name': 'get_rxnfc', 'type': '::core::option::Option<'}, {'name': 'set_rxnfc', 'type': '::core::option::Option<'}, {'name': 'flash_device', 'type': '::core::option::Option<'}, {'name': 'reset', 'type': '::core::option::Option<'}, {'name': 'get_rxfh', 'type': '::core::option::Option<'}, {'name': 'set_rxfh', 'type': '::core::option::Option<'}, {'name': 'get_channels', 'type': '::core::option::Option<'}, {'name': 'set_channels', 'type': '::core::option::Option<'}, {'name': 'get_dump_flag', 'type': '::core::option::Option<'}, {'name': 'get_dump_data', 'type': '::core::option::Option<'}, {'name': 'set_dump', 'type': '::core::option::Option<'}, {'name': 'get_ts_info', 'type': '::core::option::Option<'}, {'name': 'get_module_info', 'type': '::core::option::Option<'}, {'name': 'get_module_eeprom', 'type': '::core::option::Option<'}, {'name': 'get_eee', 'type': '::core::option::Option<'}, {'name': 'set_eee', 'type': '::core::option::Option<'}, {'name': 'get_tunable', 'type': '::core::option::Option<'}, {'name': 'set_tunable', 'type': '::core::option::Option<'}, {'name': 'get_per_queue_coalesce', 'type': '::core::option::Option<'}, {'name': 'set_per_queue_coalesce', 'type': '::core::option::Option<'}, {'name': 'get_link_ksettings', 'type': '::core::option::Option<'}, {'name': 'set_link_ksettings', 'type': '::core::option::Option<'}, {'name': 'get_fec_stats', 'type': '::core::option::Option<'}, {'name': 'get_fecparam', 'type': '::core::option::Option<'}, {'name': 'set_fecparam', 'type': '::core::option::Option<'}, {'name': 'get_ethtool_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_phy_tunable', 'type': '::core::option::Option<'}, {'name': 'set_phy_tunable', 'type': '::core::option::Option<'}, {'name': 'get_module_eeprom_by_page', 'type': '::core::option::Option<'}, {'name': 'get_eth_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_eth_mac_stats', 'type': '::core::option::Option<'}, {'name': 'get_eth_ctrl_stats', 'type': '::core::option::Option<'}, {'name': 'get_rmon_stats', 'type': '::core::option::Option<'}, {'name': 'get_module_power_mode', 'type': '::core::option::Option<'}, {'name': 'set_module_power_mode', 'type': '::core::option::Option<'}, {'name': 'get_mm', 'type': '::core::option::Option<'}, {'name': 'set_mm', 'type': '::core::option::Option<'}, {'name': 'get_mm_stats', 'type': '::core::option::Option<'}]`
- New: `[{'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'supported_coalesce_params', 'type': 'u32_'}, {'name': 'supported_ring_params', 'type': 'u32_'}, {'name': 'get_drvinfo', 'type': '::core::option::Option<'}, {'name': 'get_regs', 'type': '::core::option::Option<'}, {'name': 'get_wol', 'type': '::core::option::Option<'}, {'name': 'set_wol', 'type': '::core::option::Option<'}, {'name': 'get_msglevel', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'get_link', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'get_link_ext_state', 'type': '::core::option::Option<'}, {'name': 'get_link_ext_stats', 'type': '::core::option::Option<'}, {'name': 'get_eeprom', 'type': '::core::option::Option<'}, {'name': 'set_eeprom', 'type': '::core::option::Option<'}, {'name': 'get_coalesce', 'type': '::core::option::Option<'}, {'name': 'set_coalesce', 'type': '::core::option::Option<'}, {'name': 'get_ringparam', 'type': '::core::option::Option<'}, {'name': 'set_ringparam', 'type': '::core::option::Option<'}, {'name': 'get_pause_stats', 'type': '::core::option::Option<'}, {'name': 'get_pauseparam', 'type': '::core::option::Option<'}, {'name': 'set_pauseparam', 'type': '::core::option::Option<'}, {'name': 'self_test', 'type': '::core::option::Option<'}, {'name': 'get_strings', 'type': '::core::option::Option<'}, {'name': 'set_phys_id', 'type': '::core::option::Option<'}, {'name': 'get_ethtool_stats', 'type': '::core::option::Option<'}, {'name': 'complete', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device)>'}, {'name': 'get_priv_flags', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut net_device) -> u32_>'}, {'name': 'set_priv_flags', 'type': '::core::option::Option<'}, {'name': 'get_sset_count', 'type': '::core::option::Option<'}, {'name': 'get_rxnfc', 'type': '::core::option::Option<'}, {'name': 'set_rxnfc', 'type': '::core::option::Option<'}, {'name': 'flash_device', 'type': '::core::option::Option<'}, {'name': 'reset', 'type': '::core::option::Option<'}, {'name': 'get_rxfh', 'type': '::core::option::Option<'}, {'name': 'set_rxfh', 'type': '::core::option::Option<'}, {'name': 'get_channels', 'type': '::core::option::Option<'}, {'name': 'set_channels', 'type': '::core::option::Option<'}, {'name': 'get_dump_flag', 'type': '::core::option::Option<'}, {'name': 'get_dump_data', 'type': '::core::option::Option<'}, {'name': 'set_dump', 'type': '::core::option::Option<'}, {'name': 'get_ts_info', 'type': '::core::option::Option<'}, {'name': 'get_ts_stats', 'type': '::core::option::Option<'}, {'name': 'get_module_info', 'type': '::core::option::Option<'}, {'name': 'get_module_eeprom', 'type': '::core::option::Option<'}, {'name': 'get_eee', 'type': '::core::option::Option<'}, {'name': 'set_eee', 'type': '::core::option::Option<'}, {'name': 'get_tunable', 'type': '::core::option::Option<'}, {'name': 'set_tunable', 'type': '::core::option::Option<'}, {'name': 'get_per_queue_coalesce', 'type': '::core::option::Option<'}, {'name': 'set_per_queue_coalesce', 'type': '::core::option::Option<'}, {'name': 'get_link_ksettings', 'type': '::core::option::Option<'}, {'name': 'set_link_ksettings', 'type': '::core::option::Option<'}, {'name': 'get_fec_stats', 'type': '::core::option::Option<'}, {'name': 'get_fecparam', 'type': '::core::option::Option<'}, {'name': 'set_fecparam', 'type': '::core::option::Option<'}, {'name': 'get_ethtool_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_phy_tunable', 'type': '::core::option::Option<'}, {'name': 'set_phy_tunable', 'type': '::core::option::Option<'}, {'name': 'get_module_eeprom_by_page', 'type': '::core::option::Option<'}, {'name': 'get_eth_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_eth_mac_stats', 'type': '::core::option::Option<'}, {'name': 'get_eth_ctrl_stats', 'type': '::core::option::Option<'}, {'name': 'get_rmon_stats', 'type': '::core::option::Option<'}, {'name': 'get_module_power_mode', 'type': '::core::option::Option<'}, {'name': 'set_module_power_mode', 'type': '::core::option::Option<'}, {'name': 'get_mm', 'type': '::core::option::Option<'}, {'name': 'set_mm', 'type': '::core::option::Option<'}, {'name': 'get_mm_stats', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-000219 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: file_operations
- Explanation: file_operations changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'owner', 'type': '*mut module'}, {'name': 'llseek', 'type': '::core::option::Option<'}, {'name': 'read', 'type': '::core::option::Option<'}, {'name': 'write', 'type': '::core::option::Option<'}, {'name': 'read_iter', 'type': '::core::option::Option<'}, {'name': 'write_iter', 'type': '::core::option::Option<'}, {'name': 'iopoll', 'type': '::core::option::Option<'}, {'name': 'iterate_shared', 'type': '::core::option::Option<'}, {'name': 'poll', 'type': '::core::option::Option<'}, {'name': 'unlocked_ioctl', 'type': '::core::option::Option<'}, {'name': 'compat_ioctl', 'type': '::core::option::Option<'}, {'name': 'mmap', 'type': '::core::option::Option<'}, {'name': 'mmap_supported_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'open', 'type': '::core::option::Option<'}, {'name': 'flush', 'type': '::core::option::Option<'}, {'name': 'release', 'type': '::core::option::Option<'}, {'name': 'fsync', 'type': '::core::option::Option<'}, {'name': 'fasync', 'type': '::core::option::Option<'}, {'name': 'lock', 'type': '::core::option::Option<'}, {'name': 'get_unmapped_area', 'type': '::core::option::Option<'}, {'name': 'flock', 'type': '::core::option::Option<'}, {'name': 'splice_write', 'type': '::core::option::Option<'}, {'name': 'splice_read', 'type': '::core::option::Option<'}, {'name': 'splice_eof', 'type': '::core::option::Option<unsafe extern "C" fn(file: *mut file)>'}, {'name': 'setlease', 'type': '::core::option::Option<'}, {'name': 'fallocate', 'type': '::core::option::Option<'}, {'name': 'show_fdinfo', 'type': '::core::option::Option<unsafe extern "C" fn(m: *mut seq_file'}, {'name': 'copy_file_range', 'type': '::core::option::Option<'}, {'name': 'remap_file_range', 'type': '::core::option::Option<'}, {'name': 'fadvise', 'type': '::core::option::Option<'}, {'name': 'uring_cmd', 'type': '::core::option::Option<'}, {'name': 'uring_cmd_iopoll', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'owner', 'type': '*mut module'}, {'name': 'fop_flags', 'type': 'fop_flags_t'}, {'name': 'llseek', 'type': '::core::option::Option<'}, {'name': 'read', 'type': '::core::option::Option<'}, {'name': 'write', 'type': '::core::option::Option<'}, {'name': 'read_iter', 'type': '::core::option::Option<'}, {'name': 'write_iter', 'type': '::core::option::Option<'}, {'name': 'iopoll', 'type': '::core::option::Option<'}, {'name': 'iterate_shared', 'type': '::core::option::Option<'}, {'name': 'poll', 'type': '::core::option::Option<'}, {'name': 'unlocked_ioctl', 'type': '::core::option::Option<'}, {'name': 'compat_ioctl', 'type': '::core::option::Option<'}, {'name': 'mmap', 'type': '::core::option::Option<'}, {'name': 'open', 'type': '::core::option::Option<'}, {'name': 'flush', 'type': '::core::option::Option<'}, {'name': 'release', 'type': '::core::option::Option<'}, {'name': 'fsync', 'type': '::core::option::Option<'}, {'name': 'fasync', 'type': '::core::option::Option<'}, {'name': 'lock', 'type': '::core::option::Option<'}, {'name': 'get_unmapped_area', 'type': '::core::option::Option<'}, {'name': 'flock', 'type': '::core::option::Option<'}, {'name': 'splice_write', 'type': '::core::option::Option<'}, {'name': 'splice_read', 'type': '::core::option::Option<'}, {'name': 'splice_eof', 'type': '::core::option::Option<unsafe extern "C" fn(file: *mut file)>'}, {'name': 'setlease', 'type': '::core::option::Option<'}, {'name': 'fallocate', 'type': '::core::option::Option<'}, {'name': 'show_fdinfo', 'type': '::core::option::Option<unsafe extern "C" fn(m: *mut seq_file'}, {'name': 'copy_file_range', 'type': '::core::option::Option<'}, {'name': 'remap_file_range', 'type': '::core::option::Option<'}, {'name': 'fadvise', 'type': '::core::option::Option<'}, {'name': 'uring_cmd', 'type': '::core::option::Option<'}, {'name': 'uring_cmd_iopoll', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-000220 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: flow_dissector_key_enc_opts
- Explanation: flow_dissector_key_enc_opts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'data', 'type': '[u8_; 255usize]'}, {'name': 'len', 'type': 'u8_'}, {'name': 'dst_opt_type', 'type': '__be16'}]`
- New: `[{'name': 'data', 'type': '[u8_; 255usize]'}, {'name': 'len', 'type': 'u8_'}, {'name': 'dst_opt_type', 'type': 'u32_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000221 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: folio__bindgen_ty_2__bindgen_ty_1
- Explanation: folio__bindgen_ty_2__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_flags_1', 'type': 'core::ffi::c_ulong'}, {'name': '_head_1', 'type': 'core::ffi::c_ulong'}, {'name': '_folio_avail', 'type': 'core::ffi::c_ulong'}, {'name': '_entire_mapcount', 'type': 'atomic_t'}, {'name': '_nr_pages_mapped', 'type': 'atomic_t'}, {'name': '_pincount', 'type': 'atomic_t'}, {'name': '_folio_nr_pages', 'type': 'core::ffi::c_uint'}]`
- New: `[{'name': '_flags_1', 'type': 'core::ffi::c_ulong'}, {'name': '_head_1', 'type': 'core::ffi::c_ulong'}, {'name': '_large_mapcount', 'type': 'atomic_t'}, {'name': '_entire_mapcount', 'type': 'atomic_t'}, {'name': '_nr_pages_mapped', 'type': 'atomic_t'}, {'name': '_pincount', 'type': 'atomic_t'}, {'name': '_folio_nr_pages', 'type': 'core::ffi::c_uint'}]`

### Rust Evidence

- Graph edges: `1`

## W-000227 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: mmu_notifier_ops
- Explanation: mmu_notifier_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'release', 'type': '::core::option::Option<'}, {'name': 'clear_flush_young', 'type': '::core::option::Option<'}, {'name': 'clear_young', 'type': '::core::option::Option<'}, {'name': 'test_young', 'type': '::core::option::Option<'}, {'name': 'change_pte', 'type': '::core::option::Option<'}, {'name': 'invalidate_range_start', 'type': '::core::option::Option<'}, {'name': 'invalidate_range_end', 'type': '::core::option::Option<'}, {'name': 'arch_invalidate_secondary_tlbs', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'release', 'type': '::core::option::Option<'}, {'name': 'clear_flush_young', 'type': '::core::option::Option<'}, {'name': 'clear_young', 'type': '::core::option::Option<'}, {'name': 'test_young', 'type': '::core::option::Option<'}, {'name': 'invalidate_range_start', 'type': '::core::option::Option<'}, {'name': 'invalidate_range_end', 'type': '::core::option::Option<'}, {'name': 'arch_invalidate_secondary_tlbs', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-000228 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: per_cpu_nodestat
- Explanation: per_cpu_nodestat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'stat_threshold', 'type': 's8'}, {'name': 'vm_node_stat_diff', 'type': '[s8; 44usize]'}]`
- New: `[{'name': 'stat_threshold', 'type': 's8'}, {'name': 'vm_node_stat_diff', 'type': '[s8; 45usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000229 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: pglist_data
- Explanation: pglist_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'node_zones', 'type': '[zone; 4usize]'}, {'name': 'node_zonelists', 'type': '[zonelist; 2usize]'}, {'name': 'nr_zones', 'type': 'core::ffi::c_int'}, {'name': 'node_start_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'node_present_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'node_spanned_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'node_id', 'type': 'core::ffi::c_int'}, {'name': 'kswapd_wait', 'type': 'wait_queue_head_t'}, {'name': 'pfmemalloc_wait', 'type': 'wait_queue_head_t'}, {'name': 'reclaim_wait', 'type': '[wait_queue_head_t; 4usize]'}, {'name': 'nr_writeback_throttled', 'type': 'atomic_t'}, {'name': 'nr_reclaim_start', 'type': 'core::ffi::c_ulong'}, {'name': 'kswapd', 'type': '*mut task_struct'}, {'name': 'kswapd_order', 'type': 'core::ffi::c_int'}, {'name': 'kswapd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kswapd_failures', 'type': 'core::ffi::c_int'}, {'name': 'kcompactd_max_order', 'type': 'core::ffi::c_int'}, {'name': 'kcompactd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kcompactd_wait', 'type': 'wait_queue_head_t'}, {'name': 'kcompactd', 'type': '*mut task_struct'}, {'name': 'proactive_compact_trigger', 'type': 'bool_'}, {'name': 'totalreserve_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'min_unmapped_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'min_slab_pages', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': '__lruvec', 'type': 'lruvec'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_padding_1', 'type': '[u64; 6usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'per_cpu_nodestats', 'type': '*mut per_cpu_nodestat'}, {'name': 'vm_stat', 'type': '[atomic_long_t; 44usize]'}, {'name': 'memtier', 'type': '*mut memory_tier'}]`
- New: `[{'name': 'node_zones', 'type': '[zone; 4usize]'}, {'name': 'node_zonelists', 'type': '[zonelist; 2usize]'}, {'name': 'nr_zones', 'type': 'core::ffi::c_int'}, {'name': 'node_start_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'node_present_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'node_spanned_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'node_id', 'type': 'core::ffi::c_int'}, {'name': 'kswapd_wait', 'type': 'wait_queue_head_t'}, {'name': 'pfmemalloc_wait', 'type': 'wait_queue_head_t'}, {'name': 'reclaim_wait', 'type': '[wait_queue_head_t; 4usize]'}, {'name': 'nr_writeback_throttled', 'type': 'atomic_t'}, {'name': 'nr_reclaim_start', 'type': 'core::ffi::c_ulong'}, {'name': 'kswapd', 'type': '*mut task_struct'}, {'name': 'kswapd_order', 'type': 'core::ffi::c_int'}, {'name': 'kswapd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kswapd_failures', 'type': 'core::ffi::c_int'}, {'name': 'kcompactd_max_order', 'type': 'core::ffi::c_int'}, {'name': 'kcompactd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kcompactd_wait', 'type': 'wait_queue_head_t'}, {'name': 'kcompactd', 'type': '*mut task_struct'}, {'name': 'proactive_compact_trigger', 'type': 'bool_'}, {'name': 'totalreserve_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'min_unmapped_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'min_slab_pages', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': '__lruvec', 'type': 'lruvec'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_padding_1', 'type': '[u64; 6usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'per_cpu_nodestats', 'type': '*mut per_cpu_nodestat'}, {'name': 'vm_stat', 'type': '[atomic_long_t; 45usize]'}, {'name': 'memtier', 'type': '*mut memory_tier'}]`

### Rust Evidence

- Graph edges: `1`

## W-000230 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: scm_fp_list
- Explanation: scm_fp_list changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'count', 'type': 'core::ffi::c_short'}, {'name': 'count_unix', 'type': 'core::ffi::c_short'}, {'name': 'max', 'type': 'core::ffi::c_short'}, {'name': 'user', 'type': '*mut user_struct'}, {'name': 'fp', 'type': '[*mut file; 253usize]'}]`
- New: `[{'name': 'count', 'type': 'core::ffi::c_short'}, {'name': 'count_unix', 'type': 'core::ffi::c_short'}, {'name': 'max', 'type': 'core::ffi::c_short'}, {'name': 'inflight', 'type': 'bool_'}, {'name': 'dead', 'type': 'bool_'}, {'name': 'vertices', 'type': 'list_head'}, {'name': 'edges', 'type': '*mut unix_edge'}, {'name': 'user', 'type': '*mut user_struct'}, {'name': 'fp', 'type': '[*mut file; 253usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000232 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: super_block
- Explanation: super_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 's_list', 'type': 'list_head'}, {'name': 's_dev', 'type': 'dev_t'}, {'name': 's_blocksize_bits', 'type': 'core::ffi::c_uchar'}, {'name': 's_blocksize', 'type': 'core::ffi::c_ulong'}, {'name': 's_maxbytes', 'type': 'loff_t'}, {'name': 's_type', 'type': '*mut file_system_type'}, {'name': 's_op', 'type': '*const super_operations'}, {'name': 'dq_op', 'type': '*const dquot_operations'}, {'name': 's_qcop', 'type': '*const quotactl_ops'}, {'name': 's_export_op', 'type': '*const export_operations'}, {'name': 's_flags', 'type': 'core::ffi::c_ulong'}, {'name': 's_iflags', 'type': 'core::ffi::c_ulong'}, {'name': 's_magic', 'type': 'core::ffi::c_ulong'}, {'name': 's_root', 'type': '*mut dentry'}, {'name': 's_umount', 'type': 'rw_semaphore'}, {'name': 's_count', 'type': 'core::ffi::c_int'}, {'name': 's_active', 'type': 'atomic_t'}, {'name': 's_security', 'type': '*mut core::ffi::c_void'}, {'name': 's_xattr', 'type': '*const *mut xattr_handler'}, {'name': 's_roots', 'type': 'hlist_bl_head'}, {'name': 's_mounts', 'type': 'list_head'}, {'name': 's_bdev', 'type': '*mut block_device'}, {'name': 's_bdev_file', 'type': '*mut file'}, {'name': 's_bdi', 'type': '*mut backing_dev_info'}, {'name': 's_mtd', 'type': '*mut mtd_info'}, {'name': 's_instances', 'type': 'hlist_node'}, {'name': 's_quota_types', 'type': 'core::ffi::c_uint'}, {'name': 's_dquot', 'type': 'quota_info'}, {'name': 's_writers', 'type': 'sb_writers'}, {'name': 's_fs_info', 'type': '*mut core::ffi::c_void'}, {'name': 's_time_gran', 'type': 'u32_'}, {'name': 's_time_min', 'type': 'time64_t'}, {'name': 's_time_max', 'type': 'time64_t'}, {'name': 's_fsnotify_mask', 'type': '__u32'}, {'name': 's_fsnotify_marks', 'type': '*mut fsnotify_mark_connector'}, {'name': 's_id', 'type': '[core::ffi::c_char; 32usize]'}, {'name': 's_uuid', 'type': 'uuid_t'}, {'name': 's_uuid_len', 'type': 'u8_'}, {'name': 's_sysfs_name', 'type': '[core::ffi::c_char; 37usize]'}, {'name': 's_max_links', 'type': 'core::ffi::c_uint'}, {'name': 's_vfs_rename_mutex', 'type': 'mutex'}, {'name': 's_subtype', 'type': '*const core::ffi::c_char'}, {'name': 's_d_op', 'type': '*const dentry_operations'}, {'name': 's_shrink', 'type': '*mut shrinker'}, {'name': 's_remove_count', 'type': 'atomic_long_t'}, {'name': 's_fsnotify_connectors', 'type': 'atomic_long_t'}, {'name': 's_readonly_remount', 'type': 'core::ffi::c_int'}, {'name': 's_wb_err', 'type': 'errseq_t'}, {'name': 's_dio_done_wq', 'type': '*mut workqueue_struct'}, {'name': 's_pins', 'type': 'hlist_head'}, {'name': 's_user_ns', 'type': '*mut user_namespace'}, {'name': 's_dentry_lru', 'type': 'list_lru'}, {'name': 's_inode_lru', 'type': 'list_lru'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 's_sync_lock', 'type': 'mutex'}, {'name': 's_stack_depth', 'type': 'core::ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': '[u32; 15usize]'}, {'name': 's_inode_list_lock', 'type': 'spinlock_t'}, {'name': 's_inodes', 'type': 'list_head'}, {'name': 's_inode_wblist_lock', 'type': 'spinlock_t'}, {'name': 's_inodes_wb', 'type': 'list_head'}]`
- New: `[{'name': 's_list', 'type': 'list_head'}, {'name': 's_dev', 'type': 'dev_t'}, {'name': 's_blocksize_bits', 'type': 'core::ffi::c_uchar'}, {'name': 's_blocksize', 'type': 'core::ffi::c_ulong'}, {'name': 's_maxbytes', 'type': 'loff_t'}, {'name': 's_type', 'type': '*mut file_system_type'}, {'name': 's_op', 'type': '*const super_operations'}, {'name': 'dq_op', 'type': '*const dquot_operations'}, {'name': 's_qcop', 'type': '*const quotactl_ops'}, {'name': 's_export_op', 'type': '*const export_operations'}, {'name': 's_flags', 'type': 'core::ffi::c_ulong'}, {'name': 's_iflags', 'type': 'core::ffi::c_ulong'}, {'name': 's_magic', 'type': 'core::ffi::c_ulong'}, {'name': 's_root', 'type': '*mut dentry'}, {'name': 's_umount', 'type': 'rw_semaphore'}, {'name': 's_count', 'type': 'core::ffi::c_int'}, {'name': 's_active', 'type': 'atomic_t'}, {'name': 's_security', 'type': '*mut core::ffi::c_void'}, {'name': 's_xattr', 'type': '*const *mut xattr_handler'}, {'name': 's_roots', 'type': 'hlist_bl_head'}, {'name': 's_mounts', 'type': 'list_head'}, {'name': 's_bdev', 'type': '*mut block_device'}, {'name': 's_bdev_file', 'type': '*mut file'}, {'name': 's_bdi', 'type': '*mut backing_dev_info'}, {'name': 's_mtd', 'type': '*mut mtd_info'}, {'name': 's_instances', 'type': 'hlist_node'}, {'name': 's_quota_types', 'type': 'core::ffi::c_uint'}, {'name': 's_dquot', 'type': 'quota_info'}, {'name': 's_writers', 'type': 'sb_writers'}, {'name': 's_fs_info', 'type': '*mut core::ffi::c_void'}, {'name': 's_time_gran', 'type': 'u32_'}, {'name': 's_time_min', 'type': 'time64_t'}, {'name': 's_time_max', 'type': 'time64_t'}, {'name': 's_fsnotify_mask', 'type': '__u32'}, {'name': 's_fsnotify_info', 'type': '*mut fsnotify_sb_info'}, {'name': 's_id', 'type': '[core::ffi::c_char; 32usize]'}, {'name': 's_uuid', 'type': 'uuid_t'}, {'name': 's_uuid_len', 'type': 'u8_'}, {'name': 's_sysfs_name', 'type': '[core::ffi::c_char; 37usize]'}, {'name': 's_max_links', 'type': 'core::ffi::c_uint'}, {'name': 's_vfs_rename_mutex', 'type': 'mutex'}, {'name': 's_subtype', 'type': '*const core::ffi::c_char'}, {'name': 's_d_op', 'type': '*const dentry_operations'}, {'name': 's_shrink', 'type': '*mut shrinker'}, {'name': 's_remove_count', 'type': 'atomic_long_t'}, {'name': 's_readonly_remount', 'type': 'core::ffi::c_int'}, {'name': 's_wb_err', 'type': 'errseq_t'}, {'name': 's_dio_done_wq', 'type': '*mut workqueue_struct'}, {'name': 's_pins', 'type': 'hlist_head'}, {'name': 's_user_ns', 'type': '*mut user_namespace'}, {'name': 's_dentry_lru', 'type': 'list_lru'}, {'name': 's_inode_lru', 'type': 'list_lru'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 's_sync_lock', 'type': 'mutex'}, {'name': 's_stack_depth', 'type': 'core::ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': 'u32'}, {'name': 's_inode_list_lock', 'type': 'spinlock_t'}, {'name': 's_inodes', 'type': 'list_head'}, {'name': 's_inode_wblist_lock', 'type': 'spinlock_t'}, {'name': 's_inodes_wb', 'type': 'list_head'}]`

### Rust Evidence

- Graph edges: `1`

## W-000236 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vm_struct
- Explanation: vm_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'next', 'type': '*mut vm_struct'}, {'name': 'addr', 'type': '*mut core::ffi::c_void'}, {'name': 'size', 'type': 'core::ffi::c_ulong'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'pages', 'type': '*mut *mut page'}, {'name': 'page_order', 'type': 'core::ffi::c_uint'}, {'name': 'nr_pages', 'type': 'core::ffi::c_uint'}, {'name': 'phys_addr', 'type': 'phys_addr_t'}, {'name': 'caller', 'type': '*const core::ffi::c_void'}]`
- New: `[]`

### Rust Evidence

- Graph edges: `1`

## W-000237 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vm_unmapped_area_info
- Explanation: vm_unmapped_area_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'length', 'type': 'core::ffi::c_ulong'}, {'name': 'low_limit', 'type': 'core::ffi::c_ulong'}, {'name': 'high_limit', 'type': 'core::ffi::c_ulong'}, {'name': 'align_mask', 'type': 'core::ffi::c_ulong'}, {'name': 'align_offset', 'type': 'core::ffi::c_ulong'}]`
- New: `[{'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'length', 'type': 'core::ffi::c_ulong'}, {'name': 'low_limit', 'type': 'core::ffi::c_ulong'}, {'name': 'high_limit', 'type': 'core::ffi::c_ulong'}, {'name': 'align_mask', 'type': 'core::ffi::c_ulong'}, {'name': 'align_offset', 'type': 'core::ffi::c_ulong'}, {'name': 'start_gap', 'type': 'core::ffi::c_ulong'}]`

### Rust Evidence

- Graph edges: `1`

## W-000238 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: x86_cpu_id
- Explanation: x86_cpu_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'vendor', 'type': '__u16'}, {'name': 'family', 'type': '__u16'}, {'name': 'model', 'type': '__u16'}, {'name': 'steppings', 'type': '__u16'}, {'name': 'feature', 'type': '__u16'}, {'name': 'driver_data', 'type': 'kernel_ulong_t'}]`
- New: `[{'name': 'vendor', 'type': '__u16'}, {'name': 'family', 'type': '__u16'}, {'name': 'model', 'type': '__u16'}, {'name': 'steppings', 'type': '__u16'}, {'name': 'feature', 'type': '__u16'}, {'name': 'flags', 'type': '__u16'}, {'name': 'driver_data', 'type': 'kernel_ulong_t'}]`

### Rust Evidence

- Graph edges: `1`

## W-000287 MacroConstDrift

- Risk: Medium
- Score: 8.4
- Symbol: cpuhp_state_CPUHP_AP_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `142`
- New: `143`

### Rust Evidence

- Graph edges: `4`

## W-000288 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: cpuhp_state_CPUHP_AP_ONLINE_DYN
- Explanation: cpuhp_state_CPUHP_AP_ONLINE_DYN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `191`
- New: `192`

### Rust Evidence

- Graph edges: `2`

## W-000374 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: pageflags_PG_private
- Explanation: pageflags_PG_private changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `15`
- New: `14`

### Rust Evidence

- Graph edges: `2`

## W-000239 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: BASE_PREFETCH
- Explanation: BASE_PREFETCH changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `b"prefetcht0 %P1\0"`
- New: `b"prefetcht0 %1\0"`

### Rust Evidence

- Graph edges: `1`

## W-000240 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: BIO_FLAG_LAST
- Explanation: BIO_FLAG_LAST changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `13`
- New: `14`

### Rust Evidence

- Graph edges: `1`

## W-000241 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: BTF_FIELDS_MAX
- Explanation: BTF_FIELDS_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `11`

### Rust Evidence

- Graph edges: `1`

## W-000242 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: CONFIG_RUSTC_VERSION_TEXT
- Explanation: CONFIG_RUSTC_VERSION_TEXT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `b"rustc 1.76.0 (07dca489a 2024-02-04)\0"`
- New: `b"rustc 1.78.0 (9b00956e5 2024-04-29)\0"`

### Rust Evidence

- Graph edges: `1`

## W-000243 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: FIRST_SYSTEM_VECTOR
- Explanation: FIRST_SYSTEM_VECTOR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `236`
- New: `235`

### Rust Evidence

- Graph edges: `1`

## W-000244 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: IA32_NR_syscalls
- Explanation: IA32_NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `462`
- New: `463`

### Rust Evidence

- Graph edges: `1`

## W-000245 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: MMF_INIT_MASK
- Explanation: MMF_INIT_MASK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `1358956543`
- New: `3506440191`

### Rust Evidence

- Graph edges: `1`

## W-000246 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: NR_EXTERNAL_VECTORS
- Explanation: NR_EXTERNAL_VECTORS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `204`
- New: `203`

### Rust Evidence

- Graph edges: `1`

## W-000247 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: NR_PAGEFLAGS
- Explanation: NR_PAGEFLAGS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `23`
- New: `22`

### Rust Evidence

- Graph edges: `1`

## W-000248 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: NR_SYSTEM_VECTORS
- Explanation: NR_SYSTEM_VECTORS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `20`
- New: `21`

### Rust Evidence

- Graph edges: `1`

## W-000249 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: NR_syscalls
- Explanation: NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `462`
- New: `463`

### Rust Evidence

- Graph edges: `1`

## W-000250 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: PAGEFLAGS_MASK
- Explanation: PAGEFLAGS_MASK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8388607`
- New: `4194303`

### Rust Evidence

- Graph edges: `1`

## W-000251 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __NR_ia32_syscalls
- Explanation: __NR_ia32_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `462`
- New: `463`

### Rust Evidence

- Graph edges: `1`

## W-000252 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __NR_syscalls
- Explanation: __NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `462`
- New: `463`

### Rust Evidence

- Graph edges: `1`

## W-000253 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_attach_type___MAX_BPF_ATTACH_TYPE
- Explanation: bpf_attach_type___MAX_BPF_ATTACH_TYPE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `56`
- New: `57`

### Rust Evidence

- Graph edges: `1`

## W-000254 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: bpf_link_type___MAX_BPF_LINK_TYPE
- Explanation: bpf_link_type___MAX_BPF_LINK_TYPE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `14`
- New: `15`

### Rust Evidence

- Graph edges: `1`

## W-000255 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpu_idle_type_CPU_IDLE
- Explanation: cpu_idle_type_CPU_IDLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0`
- New: `1`

### Rust Evidence

- Graph edges: `1`

## W-000256 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ACTIVE
- Explanation: cpuhp_state_CPUHP_AP_ACTIVE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `234`
- New: `235`

### Rust Evidence

- Graph edges: `1`

## W-000257 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARC_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARC_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `125`
- New: `126`

### Rust Evidence

- Graph edges: `1`

## W-000258 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM64_DEBUG_MONITORS_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM64_DEBUG_MONITORS_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `109`
- New: `110`

### Rust Evidence

- Graph edges: `1`

## W-000259 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM64_ISNDEP_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM64_ISNDEP_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `136`
- New: `137`

### Rust Evidence

- Graph edges: `1`

## W-000260 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARMADA_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARMADA_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `123`
- New: `124`

### Rust Evidence

- Graph edges: `1`

## W-000261 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_EVTSTRM_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_EVTSTRM_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `117`
- New: `118`

### Rust Evidence

- Graph edges: `1`

## W-000262 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `116`
- New: `117`

### Rust Evidence

- Graph edges: `1`

## W-000263 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_CACHE_B15_RAC_DYING
- Explanation: cpuhp_state_CPUHP_AP_ARM_CACHE_B15_RAC_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `141`
- New: `142`

### Rust Evidence

- Graph edges: `1`

## W-000264 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_CORESIGHT_CTI_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_CORESIGHT_CTI_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `135`
- New: `136`

### Rust Evidence

- Graph edges: `1`

## W-000265 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_CORESIGHT_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_CORESIGHT_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `134`
- New: `135`

### Rust Evidence

- Graph edges: `1`

## W-000266 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_GLOBAL_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_GLOBAL_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `118`
- New: `119`

### Rust Evidence

- Graph edges: `1`

## W-000267 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_L2X0_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_L2X0_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `114`
- New: `115`

### Rust Evidence

- Graph edges: `1`

## W-000268 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_MVEBU_COHERENCY
- Explanation: cpuhp_state_CPUHP_AP_ARM_MVEBU_COHERENCY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `102`
- New: `103`

### Rust Evidence

- Graph edges: `1`

## W-000269 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_MVEBU_SYNC_CLOCKS
- Explanation: cpuhp_state_CPUHP_AP_ARM_MVEBU_SYNC_CLOCKS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `151`
- New: `152`

### Rust Evidence

- Graph edges: `1`

## W-000270 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_TWD_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_TWD_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `120`
- New: `121`

### Rust Evidence

- Graph edges: `1`

## W-000271 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_VFP_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_VFP_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `108`
- New: `109`

### Rust Evidence

- Graph edges: `1`

## W-000272 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_XEN_RUNSTATE_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_XEN_RUNSTATE_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `133`
- New: `134`

### Rust Evidence

- Graph edges: `1`

## W-000273 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_XEN_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_XEN_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `132`
- New: `133`

### Rust Evidence

- Graph edges: `1`

## W-000274 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_BASE_CACHEINFO_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_BASE_CACHEINFO_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `190`
- New: `191`

### Rust Evidence

- Graph edges: `1`

## W-000275 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_BLK_MQ_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_BLK_MQ_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `150`
- New: `151`

### Rust Evidence

- Graph edges: `1`

## W-000276 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_CLINT_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_CLINT_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `127`
- New: `128`

### Rust Evidence

- Graph edges: `1`

## W-000277 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_CSKY_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_CSKY_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `128`
- New: `129`

### Rust Evidence

- Graph edges: `1`

## W-000278 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_DUMMY_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_DUMMY_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `131`
- New: `132`

### Rust Evidence

- Graph edges: `1`

## W-000279 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_EXYNOS4_MCT_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_EXYNOS4_MCT_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `115`
- New: `116`

### Rust Evidence

- Graph edges: `1`

## W-000280 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_HRTIMERS_DYING
- Explanation: cpuhp_state_CPUHP_AP_HRTIMERS_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `138`
- New: `139`

### Rust Evidence

- Graph edges: `1`

## W-000281 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_HYPERV_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_HYPERV_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `145`
- New: `146`

### Rust Evidence

- Graph edges: `1`

## W-000282 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_HYPERV_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_HYPERV_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `130`
- New: `131`

### Rust Evidence

- Graph edges: `1`

## W-000283 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_AFFINITY_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_IRQ_AFFINITY_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `149`
- New: `150`

### Rust Evidence

- Graph edges: `1`

## W-000284 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_JCORE_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_JCORE_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `119`
- New: `120`

### Rust Evidence

- Graph edges: `1`

## W-000285 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_KVM_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_KVM_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `146`
- New: `147`

### Rust Evidence

- Graph edges: `1`

## W-000286 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_MIPS_GIC_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_MIPS_GIC_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `124`
- New: `125`

### Rust Evidence

- Graph edges: `1`

## W-000289 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ONLINE_DYN_END
- Explanation: cpuhp_state_CPUHP_AP_ONLINE_DYN_END changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `231`
- New: `232`

### Rust Evidence

- Graph edges: `1`

## W-000290 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ONLINE_IDLE
- Explanation: cpuhp_state_CPUHP_AP_ONLINE_IDLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `144`
- New: `145`

### Rust Evidence

- Graph edges: `1`

## W-000291 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_ACPI_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_ACPI_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `111`
- New: `112`

### Rust Evidence

- Graph edges: `1`

## W-000292 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_APM_XGENE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_APM_XGENE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `175`
- New: `176`

### Rust Evidence

- Graph edges: `1`

## W-000293 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_CAVIUM_TX2_UNCORE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_CAVIUM_TX2_UNCORE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `176`
- New: `177`

### Rust Evidence

- Graph edges: `1`

## W-000294 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_CCI_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_CCI_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `162`
- New: `163`

### Rust Evidence

- Graph edges: `1`

## W-000295 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_CCN_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_CCN_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `163`
- New: `164`

### Rust Evidence

- Graph edges: `1`

## W-000296 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_CPA_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_CPA_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `164`
- New: `165`

### Rust Evidence

- Graph edges: `1`

## W-000297 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_DDRC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_DDRC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `165`
- New: `166`

### Rust Evidence

- Graph edges: `1`

## W-000298 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_HHA_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_HHA_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `166`
- New: `167`

### Rust Evidence

- Graph edges: `1`

## W-000299 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_L3_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_L3_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `167`
- New: `168`

### Rust Evidence

- Graph edges: `1`

## W-000300 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PA_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PA_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `168`
- New: `169`

### Rust Evidence

- Graph edges: `1`

## W-000301 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PCIE_PMU_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PCIE_PMU_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `170`
- New: `171`

### Rust Evidence

- Graph edges: `1`

## W-000302 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_SLLC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_SLLC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `169`
- New: `170`

### Rust Evidence

- Graph edges: `1`

## W-000303 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HNS3_PMU_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HNS3_PMU_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `171`
- New: `172`

### Rust Evidence

- Graph edges: `1`

## W-000304 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HW_BREAKPOINT_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HW_BREAKPOINT_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `110`
- New: `111`

### Rust Evidence

- Graph edges: `1`

## W-000305 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_L2X0_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_L2X0_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `172`
- New: `173`

### Rust Evidence

- Graph edges: `1`

## W-000306 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_MARVELL_CN10K_DDR_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_MARVELL_CN10K_DDR_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `177`
- New: `178`

### Rust Evidence

- Graph edges: `1`

## W-000307 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L2_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L2_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `173`
- New: `174`

### Rust Evidence

- Graph edges: `1`

## W-000308 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L3_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L3_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `174`
- New: `175`

### Rust Evidence

- Graph edges: `1`

## W-000309 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `112`
- New: `113`

### Rust Evidence

- Graph edges: `1`

## W-000310 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_CSKY_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_CSKY_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `184`
- New: `185`

### Rust Evidence

- Graph edges: `1`

## W-000311 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `153`
- New: `154`

### Rust Evidence

- Graph edges: `1`

## W-000312 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_CORE_IMC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_CORE_IMC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `179`
- New: `180`

### Rust Evidence

- Graph edges: `1`

## W-000313 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_HV_24x7_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_HV_24x7_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `182`
- New: `183`

### Rust Evidence

- Graph edges: `1`

## W-000314 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_HV_GPCI_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_HV_GPCI_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `183`
- New: `184`

### Rust Evidence

- Graph edges: `1`

## W-000315 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_NEST_IMC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_NEST_IMC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `178`
- New: `179`

### Rust Evidence

- Graph edges: `1`

## W-000316 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_THREAD_IMC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_THREAD_IMC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `180`
- New: `181`

### Rust Evidence

- Graph edges: `1`

## W-000317 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_TRACE_IMC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_TRACE_IMC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `181`
- New: `182`

### Rust Evidence

- Graph edges: `1`

## W-000318 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_RISCV_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_RISCV_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `113`
- New: `114`

### Rust Evidence

- Graph edges: `1`

## W-000319 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_S390_CF_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_S390_CF_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `160`
- New: `161`

### Rust Evidence

- Graph edges: `1`

## W-000320 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_S390_SF_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_S390_SF_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `161`
- New: `162`

### Rust Evidence

- Graph edges: `1`

## W-000321 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_IBS_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_IBS_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `105`
- New: `106`

### Rust Evidence

- Graph edges: `1`

## W-000322 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_POWER_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_POWER_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `157`
- New: `158`

### Rust Evidence

- Graph edges: `1`

## W-000323 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `156`
- New: `157`

### Rust Evidence

- Graph edges: `1`

## W-000324 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `103`
- New: `104`

### Rust Evidence

- Graph edges: `1`

## W-000325 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_CSTATE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_CSTATE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `159`
- New: `160`

### Rust Evidence

- Graph edges: `1`

## W-000326 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_CSTATE_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_CSTATE_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `106`
- New: `107`

### Rust Evidence

- Graph edges: `1`

## W-000327 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `154`
- New: `155`

### Rust Evidence

- Graph edges: `1`

## W-000328 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_RAPL_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_RAPL_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `158`
- New: `159`

### Rust Evidence

- Graph edges: `1`

## W-000329 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `104`
- New: `105`

### Rust Evidence

- Graph edges: `1`

## W-000330 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_UNCORE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_UNCORE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `155`
- New: `156`

### Rust Evidence

- Graph edges: `1`

## W-000331 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_XTENSA_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_XTENSA_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `107`
- New: `108`

### Rust Evidence

- Graph edges: `1`

## W-000332 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_QCOM_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_QCOM_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `121`
- New: `122`

### Rust Evidence

- Graph edges: `1`

## W-000333 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_RANDOM_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_RANDOM_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `188`
- New: `189`

### Rust Evidence

- Graph edges: `1`

## W-000334 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_RCUTREE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_RCUTREE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `189`
- New: `190`

### Rust Evidence

- Graph edges: `1`

## W-000335 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_RISCV_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_RISCV_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `126`
- New: `127`

### Rust Evidence

- Graph edges: `1`

## W-000336 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_SCHED_WAIT_EMPTY
- Explanation: cpuhp_state_CPUHP_AP_SCHED_WAIT_EMPTY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `147`
- New: `148`

### Rust Evidence

- Graph edges: `1`

## W-000337 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_SMPBOOT_THREADS
- Explanation: cpuhp_state_CPUHP_AP_SMPBOOT_THREADS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `148`
- New: `149`

### Rust Evidence

- Graph edges: `1`

## W-000338 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_SMPCFD_DYING
- Explanation: cpuhp_state_CPUHP_AP_SMPCFD_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `137`
- New: `138`

### Rust Evidence

- Graph edges: `1`

## W-000339 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_TEGRA_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_TEGRA_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `122`
- New: `123`

### Rust Evidence

- Graph edges: `1`

## W-000340 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_TICK_DYING
- Explanation: cpuhp_state_CPUHP_AP_TICK_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `139`
- New: `140`

### Rust Evidence

- Graph edges: `1`

## W-000341 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_TI_GP_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_TI_GP_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `129`
- New: `130`

### Rust Evidence

- Graph edges: `1`

## W-000342 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_TMIGR_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_TMIGR_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `185`
- New: `186`

### Rust Evidence

- Graph edges: `1`

## W-000343 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_WATCHDOG_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_WATCHDOG_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `186`
- New: `187`

### Rust Evidence

- Graph edges: `1`

## W-000344 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_WORKQUEUE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_WORKQUEUE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `187`
- New: `188`

### Rust Evidence

- Graph edges: `1`

## W-000345 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_X86_HPET_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_X86_HPET_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `232`
- New: `233`

### Rust Evidence

- Graph edges: `1`

## W-000346 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_X86_INTEL_EPB_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_X86_INTEL_EPB_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `152`
- New: `153`

### Rust Evidence

- Graph edges: `1`

## W-000347 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_X86_KVM_CLK_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_X86_KVM_CLK_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `233`
- New: `234`

### Rust Evidence

- Graph edges: `1`

## W-000348 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_X86_TBOOT_DYING
- Explanation: cpuhp_state_CPUHP_AP_X86_TBOOT_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `140`
- New: `141`

### Rust Evidence

- Graph edges: `1`

## W-000349 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_ONLINE
- Explanation: cpuhp_state_CPUHP_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `235`
- New: `236`

### Rust Evidence

- Graph edges: `1`

## W-000350 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_TEARDOWN_CPU
- Explanation: cpuhp_state_CPUHP_TEARDOWN_CPU changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `143`
- New: `144`

### Rust Evidence

- Graph edges: `1`

## W-000351 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_KMEM
- Explanation: memcg_stat_item_MEMCG_KMEM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `49`

### Rust Evidence

- Graph edges: `1`

## W-000352 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_NR_STAT
- Explanation: memcg_stat_item_MEMCG_NR_STAT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `51`
- New: `52`

### Rust Evidence

- Graph edges: `1`

## W-000353 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_PERCPU_B
- Explanation: memcg_stat_item_MEMCG_PERCPU_B changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `46`
- New: `47`

### Rust Evidence

- Graph edges: `1`

## W-000354 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_SOCK
- Explanation: memcg_stat_item_MEMCG_SOCK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `45`
- New: `46`

### Rust Evidence

- Graph edges: `1`

## W-000355 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_SWAP
- Explanation: memcg_stat_item_MEMCG_SWAP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `44`
- New: `45`

### Rust Evidence

- Graph edges: `1`

## W-000356 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_VMALLOC
- Explanation: memcg_stat_item_MEMCG_VMALLOC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `47`
- New: `48`

### Rust Evidence

- Graph edges: `1`

## W-000357 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_ZSWAPPED
- Explanation: memcg_stat_item_MEMCG_ZSWAPPED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `50`
- New: `51`

### Rust Evidence

- Graph edges: `1`

## W-000358 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: memcg_stat_item_MEMCG_ZSWAP_B
- Explanation: memcg_stat_item_MEMCG_ZSWAP_B changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `49`
- New: `50`

### Rust Evidence

- Graph edges: `1`

## W-000359 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_SWAPCACHE
- Explanation: node_stat_item_NR_SWAPCACHE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `40`
- New: `41`

### Rust Evidence

- Graph edges: `1`

## W-000360 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_VM_NODE_STAT_ITEMS
- Explanation: node_stat_item_NR_VM_NODE_STAT_ITEMS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `44`
- New: `45`

### Rust Evidence

- Graph edges: `1`

## W-000361 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_PGDEMOTE_DIRECT
- Explanation: node_stat_item_PGDEMOTE_DIRECT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `42`
- New: `43`

### Rust Evidence

- Graph edges: `1`

## W-000362 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_PGDEMOTE_KHUGEPAGED
- Explanation: node_stat_item_PGDEMOTE_KHUGEPAGED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `43`
- New: `44`

### Rust Evidence

- Graph edges: `1`

## W-000363 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_PGDEMOTE_KSWAPD
- Explanation: node_stat_item_PGDEMOTE_KSWAPD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `41`
- New: `42`

### Rust Evidence

- Graph edges: `1`

## W-000364 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_anon_exclusive
- Explanation: pageflags_PG_anon_exclusive changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `17`
- New: `16`

### Rust Evidence

- Graph edges: `1`

## W-000365 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_arch_1
- Explanation: pageflags_PG_arch_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `13`
- New: `12`

### Rust Evidence

- Graph edges: `1`

## W-000366 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_checked
- Explanation: pageflags_PG_checked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `12`
- New: `11`

### Rust Evidence

- Graph edges: `1`

## W-000367 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_foreign
- Explanation: pageflags_PG_foreign changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `12`
- New: `11`

### Rust Evidence

- Graph edges: `1`

## W-000368 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_fscache
- Explanation: pageflags_PG_fscache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `15`

### Rust Evidence

- Graph edges: `1`

## W-000369 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_isolated
- Explanation: pageflags_PG_isolated changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `18`
- New: `17`

### Rust Evidence

- Graph edges: `1`

## W-000370 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_mappedtodisk
- Explanation: pageflags_PG_mappedtodisk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `17`
- New: `16`

### Rust Evidence

- Graph edges: `1`

## W-000371 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_mlocked
- Explanation: pageflags_PG_mlocked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `21`
- New: `20`

### Rust Evidence

- Graph edges: `1`

## W-000372 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_owner_priv_1
- Explanation: pageflags_PG_owner_priv_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `12`
- New: `11`

### Rust Evidence

- Graph edges: `1`

## W-000373 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_pinned
- Explanation: pageflags_PG_pinned changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `12`
- New: `11`

### Rust Evidence

- Graph edges: `1`

## W-000375 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_private_2
- Explanation: pageflags_PG_private_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `15`

### Rust Evidence

- Graph edges: `1`

## W-000376 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_readahead
- Explanation: pageflags_PG_readahead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `18`
- New: `17`

### Rust Evidence

- Graph edges: `1`

## W-000377 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_reclaim
- Explanation: pageflags_PG_reclaim changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `18`
- New: `17`

### Rust Evidence

- Graph edges: `1`

## W-000378 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_reserved
- Explanation: pageflags_PG_reserved changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `14`
- New: `13`

### Rust Evidence

- Graph edges: `1`

## W-000379 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_swapbacked
- Explanation: pageflags_PG_swapbacked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `19`
- New: `18`

### Rust Evidence

- Graph edges: `1`

## W-000380 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_swapcache
- Explanation: pageflags_PG_swapcache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `12`
- New: `11`

### Rust Evidence

- Graph edges: `1`

## W-000381 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_uncached
- Explanation: pageflags_PG_uncached changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `22`
- New: `21`

### Rust Evidence

- Graph edges: `1`

## W-000382 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_unevictable
- Explanation: pageflags_PG_unevictable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `20`
- New: `19`

### Rust Evidence

- Graph edges: `1`

## W-000383 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags_PG_xen_remapped
- Explanation: pageflags_PG_xen_remapped changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `12`
- New: `11`

### Rust Evidence

- Graph edges: `1`

## W-000384 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: pageflags___NR_PAGEFLAGS
- Explanation: pageflags___NR_PAGEFLAGS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `23`
- New: `22`

### Rust Evidence

- Graph edges: `1`

## W-000385 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: work_bits_WORK_OFFQ_LEFT
- Explanation: work_bits_WORK_OFFQ_LEFT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `59`
- New: `43`

### Rust Evidence

- Graph edges: `1`

## W-000386 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: work_bits_WORK_OFFQ_POOL_SHIFT
- Explanation: work_bits_WORK_OFFQ_POOL_SHIFT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `21`

### Rust Evidence

- Graph edges: `1`

## W-000387 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: wq_misc_consts_WORKER_DESC_LEN
- Explanation: wq_misc_consts_WORKER_DESC_LEN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `24`
- New: `32`

### Rust Evidence

- Graph edges: `1`

## W-000388 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: ACPI_AEST_NODE_TYPE_RESERVED
- Explanation: ACPI_AEST_NODE_TYPE_RESERVED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5	/* 5 and above are reserved */`
- New: `7 /* 7 and above are reserved */`

### Rust Evidence

- Graph edges: `0`

## W-000389 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: ACPI_AEST_XFACE_RESERVED
- Explanation: ACPI_AEST_XFACE_RESERVED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `2	/* 2 and above are reserved */`
- New: `3   /* 2 and above are reserved */`

### Rust Evidence

- Graph edges: `0`

## W-000390 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: ACPI_CA_VERSION
- Explanation: ACPI_CA_VERSION changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x20230628`
- New: `0x20240322`

### Rust Evidence

- Graph edges: `0`

## W-000391 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: ARCH_PFN_OFFSET
- Explanation: ARCH_PFN_OFFSET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `(PAGE_OFFSET >> PAGE_SHIFT)`
- New: `(0UL)`

### Rust Evidence

- Graph edges: `0`

## W-000392 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: DRM_BUDDY_HEADER_UNUSED
- Explanation: DRM_BUDDY_HEADER_UNUSED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `GENMASK_ULL(9, 6)`
- New: `GENMASK_ULL(8, 6)`

### Rust Evidence

- Graph edges: `0`

## W-000393 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: DRM_BUDDY_MAX_ORDER
- Explanation: DRM_BUDDY_MAX_ORDER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `(63 - PAGE_SHIFT)`
- New: `(63 - 12)`

### Rust Evidence

- Graph edges: `0`

## W-000394 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: ECC_MAX_DIGITS
- Explanation: ECC_MAX_DIGITS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `(512 / 64) /* due to ecrdsa */`
- New: `DIV_ROUND_UP(521, 64) /* NIST P521 */`

### Rust Evidence

- Graph edges: `0`

## W-000395 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: KUNIT_FAIL_ASSERTION
- Explanation: KUNIT_FAIL_ASSERTION changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `\`
- New: `do {		       \`

### Rust Evidence

- Graph edges: `0`

## W-000396 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: KUNIT_SUCCEED
- Explanation: KUNIT_SUCCEED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `do {} while (0)`
- New: `_KUNIT_SAVE_LOC(test)`

### Rust Evidence

- Graph edges: `0`

## W-000397 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: kmalloc_track_caller
- Explanation: kmalloc_track_caller changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `\`
- New: `kmalloc_node_track_caller(__VA_ARGS__, NUMA_NO_NODE)`

### Rust Evidence

- Graph edges: `0`
